from django.shortcuts import render, redirect
from blog.views import log_out


# Create your views here.
def health(request):
    if request.method == 'POST' and 'logout' in request.POST:
        log_out(request)
        return redirect('login-home')
    return render(request, 'health/health-home.html')

# Create your views here.
