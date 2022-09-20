from django.shortcuts import render, get_object_or_404
from .models import Article

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


#redirect(reverse('article-detail', kwargs={'pk':article.pk})) 
