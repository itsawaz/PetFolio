from django.urls import path
from blog import views
from .views import post

urlpatterns = [
    path('', views.blog, name='blog-home')
]
