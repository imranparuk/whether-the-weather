
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.register.as_view(), name='signup'),
    #APPEND_SLASH = True




]

