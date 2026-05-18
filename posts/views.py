from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/post_detail.html', {'post': post})
