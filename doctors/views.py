from django.shortcuts import render,redirect
from blog.views import log_out
from mapbox import Maps
import mapbox


def doctor(request):
    if request.method == 'POST' and 'logout' in request.POST:
        log_out(request)
        return redirect('login-home')
    return render(request, 'doctor/doctor.html')


