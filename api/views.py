from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import viewsets

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from forecast.models import Forecasts
from api.serializers import forecastSerializer

from django.utils.timezone import get_current_timezone
from datetime import datetime

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
#curl -i -X GET -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://127.0.0.1:8000/api


@api_view(['DELETE', 'GET', 'POST',])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
@csrf_exempt
def forecast_list(request, format=None):
    if request.method == 'GET':
        forecasts = Forecasts.objects.all()

        serializer = forecastSerializer(forecasts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
		
        if ('getForecastWithDateTime' in data.keys()):
            dateTimeToGet = data['date']  
	
            tz = get_current_timezone()
            dt = tz.localize(datetime.strptime(dateTimeToGet, '%d %m %Y %H:%M:%S'))

            forecasts = Forecasts.objects.filter(date=dt)
            serializer = forecastSerializer(forecasts)
            return JsonResponse(forecasts, safe=False)
        
        elif ('getLastForecast' in data.keys()):
            forecasts = Forecasts.objects.latest('id')
            serializer = forecastSerializer(forecasts)
            return JsonResponse(serializer.data, safe=False)
        
        elif ('deleteForecastWithDateTime' in data.keys()):
            dateTimeToDelete = data['date']  
            tz = get_current_timezone()
            dt = tz.localize(datetime.strptime(dateTimeToDelete, '%d %m %Y %H:%M:%S'))
            Forecasts.objects.filter(date=dt).delete()
            return JsonResponse("Object Deleted", status=201, safe=False)

        else:
            dateTimeToChange = data['date']  
	
            tz = get_current_timezone()
            dt = tz.localize(datetime.strptime(dateTimeToChange, '%d %m %Y %H:%M:%S'))
            data['date'] = dt
        
            serializer = forecastSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Forecasts.objects.latest('id').delete()
        return JsonResponse("Object Deleted", status=201, safe=False)
        
        #{"date":"01 07 2018 00:12:02","min_temp":"0", "max_temp":"0", "wind_speed":"0", "rain_probability": "0", "getForecastWithDateTime":""}





