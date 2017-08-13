from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

class blog_creat(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello</h1>")

class blog_read(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello</h1>")

class blog_update(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello</h1>")

class blog_delete(View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello</h1>")
