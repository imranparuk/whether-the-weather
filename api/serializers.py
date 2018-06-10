from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from forecast.models import Forecasts

class forecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forecasts
        fields = ('date', 'min_temp', 'max_temp', 'wind_speed', 'rain_probability')



