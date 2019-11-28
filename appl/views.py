from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render
from appl.models import Post
from appl.models import Article

def index(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')




def blog(request):
    latest_articles_list = Article.objects.order_by('-pub.date')[:5]
    return render(request, 'blog.html', {'latest_articles_list' : latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Not found!")

    return render(request, 'detail.html', {'article': a})

def contact(request):
    return render(request, 'contact.html')

