
from django.urls import path, include
from . import views
from home.views import home_view


urlpatterns = [
    path('', home_view.as_view(), name='home'),
]


