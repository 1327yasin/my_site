from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'website/home_page.html')

def contact(request):
    return render(request, 'website/contact.html')

def about_us(request):
    return render(request, 'website/about.html')