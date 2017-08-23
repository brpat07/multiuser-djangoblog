from urllib.parse import quote_plus

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            messages.success(request, "blog has been added successfully",
                             extra_tags='alert alert-success')
            return HttpResponseRedirect(form_obj.get_absolute_url())
        else:
            messages.error(request, "Failed to add the blog",
                           extra_tags='alert alert-danger')
            return HttpResponseRedirect("create")


class blog_read(View):
    def get(self, request, id, *args, **kwargs):
        query = get_object_or_404(Post, id=id)
        url_string = quote_plus(query.content)
        context = {
            "post": query,
            "url_string": url_string
        }
        return render(request, "post.html", context)


class blog_list(View):
    def get(self, request, *args, **kwargs):
        query = Post.objects.all().order_by("-postupdate")
        queryset = request.GET.get("q")
        if queryset:
            query = query.filter(title__icontains=queryset)
        context = {
            "list": query,
        }
        return render(request, "blogs.html", context)


class blog_recent(View):
    def get(self, request, *args, **kwargs):
        query = Post.objects.all().order_by("-postupdate")[:10]
        queryset = request.GET.get("q")
        if queryset:
            query = Post.objects.all().order_by("-postupdate")
            query = query.filter(title__icontains=queryset)
        context = {
            "list": query,
        }
        return render(request, "blogs.html", context)


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
        form = PostForm(request.POST, request.FILES, instance=query)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.save()
            messages.success(request, "blog has been edited successfully",
                             extra_tags='alert alert-success')
            return HttpResponseRedirect(form_obj.get_absolute_url())
        else:
            context = {
                "form": form,
            }
            messages.error(request, "Failed to edit the blog",
                           extra_tags='alert alert-danger')
            return render(request, "post_create.html", context)


class blog_delete(View):
    def get(self, request, id, *args, **kwargs):
        query = get_object_or_404(Post, id=id)
        query.delete()
        context = {
            "error": "Post has been deleted!"
        }
        messages.success(request, "blog has been deleted successfully",
                         extra_tags='alert alert-success')
        return redirect("posts:show_blogs")
