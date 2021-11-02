from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/pages/index.html')

def about_us(request):
    return render(request, 'home/pages/about-us.html')

def contact_us(request):
    return render(request, 'home/pages/contact-us.html')

def pricing(request):
    return render(request, 'home/pages/pricing.html')