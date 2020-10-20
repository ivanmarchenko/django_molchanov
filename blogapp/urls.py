from django.urls import path
# from django.urls import include
from .views import *


urlpatterns = [
    path('', posts_list, name='blog'),
    # <str:slug> - slug равен имени slug в параметрах функции post_detail(..., slug)
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
]
