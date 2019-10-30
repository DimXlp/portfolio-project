from django.shortcuts import render, get_object_or_404
""" get_object_or_404, gets objects like blog_id and searches stuff in the database
    but if it doesn't find it, it returns 404 """

from .models import Blog

"""
    Added by me.

"""

def allblogs(request):
    blogs = Blog.objects # added, gets all the blog details from the db and turns them to python objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
