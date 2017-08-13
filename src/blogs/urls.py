from django.conf.urls import url
from .views import blog_read

urlpatterns = [
    url(r'^$', blog_read.as_view()),
]
