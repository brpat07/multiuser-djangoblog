from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Post

class blog_create(View):
    def get(self, request, id, *args, **kwargs):
        return HttpResponse("<h1>Hello1</h1>")

class blog_read(View):
    def get(self, request, id, *args, **kwargs):
        query = get_object_or_404(Post, id=id)
        context = {
            "post" : query,
        }
        return render(request, "post.html", context)

class blog_list(View):
    def get(self, request, *args, **kwargs):
        query = Post.objects.all()
        context = {
            "list" : query,
        }
        return render(request, "base.html", context)

class blog_update(View):
    def get(self, request, id, *args, **kwargs):
        return HttpResponse("<h1>Hello4</h1>")

class blog_delete(View):
    def get(self, request, id, *args, **kwargs):
        return HttpResponse("<h1>Hello5</h1>")
