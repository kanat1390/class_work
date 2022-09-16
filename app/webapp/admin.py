from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'author')
    fields = ('title', 'author', 'created_at', 'text')
    readonly_fields = ('id','created_at', 'changed_at')


admin.site.register(Article, ArticleAdmin)
