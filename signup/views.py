from django.shortcuts import render, redirect
from signup.models import User
from django.http import HttpResponse
from django.contrib import messages




def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        pet_type = request.POST.get('pet_type')
        remember_me = request.POST.get('remember_me')

        # Check if the username or email already exists in the database
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Account already exists for {username}')
        elif User.objects.filter(email=email).exists():
            messages.error(request, f'Account already exists for {email}')
        else:
            # Create a new user object and save it to the database
            signup_db = User(username=username, password=password, email=email, pet_type=pet_type)
            signup_db.save()
            messages.success(request, 'Account created successfully!')

            # Redirect to the login page
            return redirect('login-home')

    return render(request, 'signup/signup.html', {"title": "Signup"})
