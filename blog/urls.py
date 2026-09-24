from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('blog_detail/', blog_detail, name='index'),
]