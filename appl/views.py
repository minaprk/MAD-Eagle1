from django.shortcuts import render
from django.shortcuts import render
from appl.models import Post
# Create your views here.

def index(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

