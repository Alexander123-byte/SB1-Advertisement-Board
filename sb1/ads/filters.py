import django_filters

from ads.models import Ad


class AdFilter(django_filters.rest_framework.FilterSet):
    """
    Класс фильтрации для модели "Ad".

    Поля:
        - title (CharFilter): Фильтр по названию товара с использованием операции 'icontains'.

    Метаданные:
        - model (Model): Указывает модель, к которой применяется данный набор фильтров (Ad).
        - fields (tuple): Указывает поля модели, которые будут доступны для фильтрации.
    """
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title", )
