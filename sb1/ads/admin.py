from django.contrib import admin

from ads.models import Ad, Comment

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Регистрация модели "Comment" в админке.
    """
    list_display = ('pk', 'author', 'text')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Регистрация модели "Ad" в админке.
    """
    list_display = ('pk', 'author', 'title', 'price', 'image')
