from django.shortcuts import render,redirect
from blog.views import log_out
from doctors.models import Vets

def doctor(request):
    if request.method == 'POST' and 'logout' in request.POST:
        log_out(request)
        return redirect('login-home')
    return render(request, 'doctor/doctor.html')

def doctor_list(request):
    if request.method == 'POST' and 'logout' in request.POST:
        log_out(request)
        return redirect('login-home')
    elif request.method == 'POST':
        vet_name = request.POST.get('vet_name')
        vet_email = request.POST.get('vet_email')
        vet_calendly = request.POST.get('vet_calendly')
        vet_description = request.POST.get('vet_description')

        vet = Vets(vet_name=vet_name, vet_email=vet_email, vet_calendly=vet_calendly, vet_description=vet_description)
        vet.save()

        return redirect('doctor-list')
    vets = Vets.objects.all()
    context = {'vet_list': vets}
    return render(request, 'doctor/doctor_list.html')
