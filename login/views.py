# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        email_username = request.POST['email_username']
        password = request.POST['password']
        user = authenticate(request, username=email_username, password=password)
        if user is None:
            user = User.objects.filter(email=email_username).first()
            if user:
                user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog-home')  # Replace 'home' with the name of your home page URL pattern
        else:
            messages.error(request, f'Invalid username or password')
            return redirect('login-home')
    return render(request, 'login/login.html', {"title": "Login"})
