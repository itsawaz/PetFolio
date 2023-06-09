# Create your views here.
from signup.models import Peto
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



def login_view(request):

    if request.method == 'POST':
        email_username = request.POST['email_username']
        password = request.POST['password']
        #
       # if User.objects.filter(username=email_username).exists() or User.objects.filter(email=email_username).exists():
       #     if User.objects.filter(password=password).exists():
        if User.objects.filter(username=email_username).exists():
            user = authenticate(request, username=email_username, password=password)

            if user is not None:
                    login(request, user)
                    return redirect('blog-home')  # Replace 'home' with the name of your home page URL pattern
            else:
                    messages.info(request, f'Invalid username or password')
                    return redirect('login-home')
        else:
            user1 = User.objects.filter(email=email_username).first()
            user = authenticate(request, username=user1.username, password=password)
            if user is not None:
                    login(request, user)
                    return redirect('blog-home')  # Replace 'home' with the name of your home page URL pattern
            else:
                    messages.info(request, f'Invalid username or password')
                    return redirect('login-home')

    return render(request, 'login/login.html', {"title": "Login"})
