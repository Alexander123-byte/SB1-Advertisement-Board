from django.conf import settings
from django.db import models

from django.utils import timezone


class Ad(models.Model):
    """
    Модель объявления.

    Поля:
        - image (ImageField): Фото для объявления (опционально).
        - title (CharField): Название товара.
        - price (PositiveIntegerField): Цена товара.
        - author (ForeignKey): Автор объявления (связь с моделью пользователя).
        - created_at (DateTimeField): Время создания объявления.
        - description (CharField): Описание товара (опционально).

    Метаданные:
        - verbose_name (str): Название модели в единственном числе.
        - verbose_name_plural (str): Название модели во множественном числе.
        - ordering (tuple): Порядок сортировки по умолчанию (сначала самые новые).
    """
    image = models.ImageField(upload_to='images/', verbose_name="Фото", help_text="Разместите фото для объявления",
                              blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="Название товара", help_text="Укажите название товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара", help_text="Укажите цену товара")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор объявления",
                               help_text="Выберите автора объявления", on_delete=models.CASCADE, related_name="ads",
                               default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания объявления",
                                      help_text="Укажите время создания объявления")
    description = models.CharField(verbose_name="Описание товара", max_length=1000, help_text="Укажите описание товара",
                                   blank=True, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)


class Comment(models.Model):
    """
    Модель для комментариев к объявлениям.

    Поля:
        - text (CharField): Текст комментария.
        - ad (ForeignKey): Объявление, к которому относится комментарий.
        - author (ForeignKey): Автор комментария (связь с моделью пользователя).
        - created_at (DateTimeField): Время создания комментария.

    Метаданные:
        - verbose_name (str): Название модели в единственном числе.
        - verbose_name_plural (str): Название модели во множественном числе.
        - ordering (tuple): Порядок сортировки по умолчанию (сначала самые новые).
    """
    text = models.CharField(verbose_name="Комментарий", max_length=1000, help_text="Напишите свой комментарий")
    ad = models.ForeignKey(Ad, verbose_name="Объявление", on_delete=models.CASCADE, related_name="comments",
                           help_text="Объявление, к которому относится комментарий")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор комментария", on_delete=models.CASCADE,
                               related_name="author_comments", help_text="Выберите автора комментария", default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания комментария",
                                      help_text="Укажите время создания комментария")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)
