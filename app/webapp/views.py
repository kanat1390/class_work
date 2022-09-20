from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404

def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'webapp/index.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'webapp/article-detail.html', context)
