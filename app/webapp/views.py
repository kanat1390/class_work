from django.shortcuts import render
from .models import Article

def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'webapp/index.html', context)

def article_detail(request):
    pk = request.GET.get('id')
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'webapp/article-detail.html', context)
