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
        name = request.POST.get('vet_name')
        email = request.POST.get('vet_email')
        calendly = request.POST.get('vet_calendly')
        description = request.POST.get('vet_description')

        vet = Vets(vet_name=name, vet_email=email, vet_calendly=calendly, vet_description=description)
        vet.save()
        context = {'vet_list': Vets.objects.all()}
        return redirect('doctor-list')
    vets = Vets.objects.all()
    context = {'vet_list': vets}
    return render(request, 'doctor/doctor_list.html')
