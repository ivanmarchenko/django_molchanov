from django.urls import path
# from django.urls import include
from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    # <str:slug> - slug равен имени slug в параметрах функции post_detail(..., slug)
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url')
]
