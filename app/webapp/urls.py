from django.urls import path
from .views import index_view, article_detail

urlpatterns = [
    path('', index_view, name='index'),
    path('articles/', article_detail, name='detail')
]