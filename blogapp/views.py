from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from .utils import ObjectDetailMixin
from .forms import TagForm



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

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blogapp/tag_create.html', context={'form': form})
    
    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blogapp/tag_create.html', context={'form': bound_form})

