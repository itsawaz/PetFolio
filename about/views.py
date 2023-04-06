from django.shortcuts import render,redirect
from blog.views import log_out

# Create your views here.
def about(request):
    if request.method == 'POST' and 'logout' in request.POST:
        log_out(request)
        return redirect('login-home')
    return render(request,'about/about.html',{"title": "About"})
