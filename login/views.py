# Create your views here.
from signup.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect


def login_view(request):
    user1=User()
    if request.method == 'POST':
        email_username = request.POST['email_username']
        password = request.POST['password']
        print(email_username,password)
        user = authenticate(request, username=email_username, password=password)
       # if User.objects.filter(username=email_username).exists() or User.objects.filter(email=email_username).exists():
       #     if User.objects.filter(password=password).exists():
        if user is not None:
            login(request, user)
            return redirect('blog-home')  # Replace 'home' with the name of your home page URL pattern
        else:
            messages.info(request, f'Invalid username or password')
            return redirect('login-home')
    return render(request, 'login/login.html', {"title": "Login"})
