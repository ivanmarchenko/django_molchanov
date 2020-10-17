from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    n = ['Oleg', 'Masha', 'Olya', 'Peter']
    return render(request, 'blogapp/index.html', context={'namess': n})