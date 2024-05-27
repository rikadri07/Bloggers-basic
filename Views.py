from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    data = {"posts": list(posts.values())}
    return JsonResponse(data)
