from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("<h1>home page</h1>")

def contact(request):
    return HttpResponse("<h1>contact</h1>")

def about_us(request):
    return HttpResponse ("<h1>abot us</h1>")