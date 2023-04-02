from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
# Create your views here.

def signup(request):
    return render(request,'signup/signup.html',{"title": "Signup"})
