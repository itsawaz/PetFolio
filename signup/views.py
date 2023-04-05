from django.shortcuts import render, redirect
from signup.models import Peto
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        pet_type = request.POST.get('pet_type')


        # Check if the username or email already exists in the database
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, f'Account already exists for {username} or {email}')
            return redirect('login-home')
        else:
            # Create a new user object and save it to the database
            signup_db = Peto(username=username, password=password, email=email, pet_type=pet_type)
            signup_db.save()
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('blog-home')

    return render(request, 'signup/signup.html', {"title": "Signup"})
