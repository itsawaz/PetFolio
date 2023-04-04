from django.shortcuts import render
from mapbox import Maps
import mapbox


def doctor(request):

    return render(request, 'doctor/doctor.html')


