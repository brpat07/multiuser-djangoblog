from django.conf.urls import url
from .views import (
        blog_create,
        blog_read,
        blog_list,
        blog_update,
        blog_delete,
        )

urlpatterns = [
    url(r'^$', blog_list.as_view()),
    url(r'^list$', blog_list.as_view()),
    url(r'^create$', blog_create.as_view()),
    url(r'^(?P<id>\d+)/read$', blog_read.as_view(), name="show_post"),
    url(r'^(?P<id>\d+)/update$', blog_update.as_view()),
    url(r'^(?P<id>\d+)/delete$', blog_delete.as_view()),
]
