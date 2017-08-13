from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

class blog_create(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello1</h1>")

class blog_read(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello2</h1>")

class blog_list(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello3</h1>")

class blog_update(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello4</h1>")

class blog_delete(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello5</h1>")
