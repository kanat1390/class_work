from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200, null=False, blank=False)
    text = models.TextField(verbose_name='Текст', max_length=3000, null=False, blank=False)
    author = models.CharField(verbose_name='Автор', max_length=100, null=False, blank=False, default='No author')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.author}'
