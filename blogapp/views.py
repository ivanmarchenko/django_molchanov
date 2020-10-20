from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def posts_list(request):
    n = ['Oleg', 'Masha', 'Olya', 'Peter']
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})

def post_detail(request, slug): 
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blogapp/post_detail.html', context={'post': post})