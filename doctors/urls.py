from django.urls import path
from . import views


urlpatterns = [
    path('', views.doctor, name='doctor-home'),
    path('doctor-list', views.doctor_list, name='doctor-list'),
]
