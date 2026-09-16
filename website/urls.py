from django.urls import path
from website.views import * 

urlpatterns = [
    path('', home_page),
    path('contact/', contact),
    path('about/', about_us),
]
