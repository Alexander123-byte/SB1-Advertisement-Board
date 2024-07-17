from rest_framework import pagination


class AdPagination(pagination.PageNumberPagination):
    """
    Класс для пагинации объявлений.

    Атрибуты:
        - page_size (int): Количество объектов на одной странице. Установлено значение 4.
    """
    page_size = 4
