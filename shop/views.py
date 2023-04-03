from django.shortcuts import render

# Create your views here.

# Create your views here.
def shop(request):
    return render(request,'shop/shop.html',{"title": "About"})
