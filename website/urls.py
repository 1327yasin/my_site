from django.urls import path
from website.views import * 

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
]
