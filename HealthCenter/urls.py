from django.urls import path
from .views import *



urlpatterns = [
    path('',view_home, name='home'),
    path('register/',view_register, name='register'),
    path('login/',view_login, name='login'),
    path('secure/',view_secure, name='secure'),
    path('unsecure/',view_unsecure, name='unsecure'),
]
