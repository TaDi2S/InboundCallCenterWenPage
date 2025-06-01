from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def services(request):
    return render(request, 'pages/services.html')

# 나머지 뷰도 마찬가지
def process(request):
    return render(request, 'pages/process.html')

def advantages(request):
    return render(request, 'pages/advantages.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def faq(request):
    return render(request, 'pages/faq.html')