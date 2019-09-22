from django.urls import path
from . import views

urlpatterns = [
    path('reg',views.registerVehicle, name='reg'),
    path('auth',views.authOfficer, name='auth')
]