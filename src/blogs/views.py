from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Post
from .forms import PostForm


class blog_create(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {
            "form": form,
        }
        return render(request, "post_create.html", context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            messages.success(request, "blog has been added successfully")
            return HttpResponseRedirect(form_obj.get_absolute_url())
        else:
            messages.error(request, "Failed to add the blog")
            return HttpResponseRedirect("create")


class blog_read(View):
    def get(self, request, id, *args, **kwargs):
        query = get_object_or_404(Post, id=id)
        context = {
            "post": query,
        }
        return render(request, "post.html", context)


class blog_list(View):
    def get(self, request, *args, **kwargs):
        query = Post.objects.all()
        context = {
            "list": query,
        }
        return render(request, "base.html", context)


class blog_edit(View):
    def get(self, request, id, *args, **kwargs):
        query = get_object_or_404(Post, id=id)
        form = PostForm(instance=query)
        context = {
            "form": form,
        }
        return render(request, "post_create.html", context)

    def post(self, request, id, *args, **kwargs):
        query = get_object_or_404(Post, id=id)
        form = PostForm(request.POST, instance=query)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            messages.success(request, "blog has been edited successfully")
            return HttpResponseRedirect(form_obj.get_absolute_url())
        else:
            context = {
                "form": form,
            }
            messages.error(request, "Failed to edit the blog")
            return render(request, "post_create.html", context)


class blog_delete(View):
    def get(self, request, id, *args, **kwargs):
        return HttpResponse("<h1>Hello5</h1>")
