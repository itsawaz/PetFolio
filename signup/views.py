from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
# Create your views here.

def signup(request):
    if request.method=='POST':
        username= request.Post.get('username')
        password = request.Post.get('password')
        email = request.Post.get('email')
        pet_type = request.Post.get('pet_type')

        signup_db=User(username=username,password=password,email=email,pet_type=pet_type)
        signup_db.save()
    return render(request,'signup/signup.html',{"title": "Signup"})
