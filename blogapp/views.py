from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin



def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blogapp/tags_list.html', context={'tags': tags})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blogapp/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blogapp/tag_detail.html'