
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Post
from signup.models import User


def blog(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')

    }
    if request.method == 'POST':
        post(request)
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
