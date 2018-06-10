
from django.conf.urls import url, include
from api import views, models

from django.contrib import admin
from django.urls import path
from rest_framework import routers, serializers, viewsets



urlpatterns = [
    url(r'', views.forecast_list),
]
