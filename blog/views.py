from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Post
from signup.models import Peto
from django.contrib.auth.models import User


def blog(request):

    user = request.user

    peto = Peto.objects.get(username=user.username)
    bio = peto.bio
    ptype = peto.pet_type

    context = {
        'peto_bio': bio,
        'peto_type': ptype,
        'posts': Post.objects.all().order_by('-date_posted')

    }
    if request.method == 'POST' and 'POST' in request.POST:
        if request.user.is_authenticated:
            post(request)
        else:
            messages.error(request, f'Log in to Continue')
    if request.method == 'POST' and 'logout' in request.POST:
        log_out(request)
    return render(request, 'blog/blog.html', context)


@login_required
def post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        author = request.user
        pet_type = request.POST.get('pet_type')

        post = Post.objects.create(title=title, content=description, pet_type=pet_type, author=author)
        post.save()
        messages.success(request, f'Posted Successfully')
        return redirect('blog-home')


def log_out(request):
    logout(request)
    messages.error(request, f'Account logged out!')
    return redirect('login-home')

