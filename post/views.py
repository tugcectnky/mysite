from django.shortcuts import render, HttpResponse
from .models import Post

def post_index(request):
    posts = Post.object.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request):
    return HttpResponse('Burası Post Detail sayfası')


def post_create(request):
    return HttpResponse('Burası Post Create sayfası')


def post_update(request):
    return HttpResponse('Burası Post Update sayfası')


def post_delete(request):
    return HttpResponse('Burası Post Delete sayfası')