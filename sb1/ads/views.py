from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad, Comment
from ads.pagination import AdPagination
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import AdFilter
from rest_framework.decorators import action


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Ad.

    Атрибуты:
        - queryset (QuerySet): Базовый запрос для получения всех объявлений.
        - serializer_class (Serializer): Базовый сериалайзер для обработки объявлений.
        - pagination_class (Pagination): Класс для пагинации объявлений.
        - permission_classes (tuple): Кортеж классов разрешений для обработки запросов.
        - filter_backends (tuple): Кортеж фильтров для обработки запросов.
        - filterset_class (FilterSet): Класс фильтрации объявлений.
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = (AllowAny, )
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def perform_create(self, serializer):
        """
        Метод для сохранения нового объявления с указанием текущего пользователя как автора.
        """
        user = self.request.user
        serializer.save(author=user)

    def get_serializer_class(self):
        """
        Метод для получения класса сериалайзера в зависимости от действия.
        """
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer

    def get_permissions(self):
        """
        Метод для получения классов разрешений в зависимости от действия.
        """
        permission_classes = (AllowAny, )
        if self.action in ["retrieve"]:
            permission_classes = (AllowAny, )
        elif self.action in ["create", "update", "partial_update", "destroy", "me"]:
            permission_classes = (IsOwner | IsAdmin,)
        return tuple(permission() for permission in permission_classes)

    def get_queryset(self):
        """
        Метод для получения queryset в зависимости от действия.
        """
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(
        detail=False,
        methods=[
            "get",
        ],
    )
    def me(self, request, *args, **kwargs):
        """
        Метод для получения объявлений текущего пользователя.
        """
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Comment.

    Атрибуты:
        - queryset (Queryset): Базовый запрос для получения всех комментариев.
        - serializer_class (Serializer): Базовый сериалайзер для обработки комментариев.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """
        Метод для сохранения нового комментария с указанием текущего пользователя как автора и текущего объявления.
        """
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_queryset(self):
        """
        Метод для получения queryset комментариев к конкретному объявлению.
        """
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        return ad_instance.comments.all()

    def get_permissions(self):
        """
        Метод для получения классов разрешений в зависимости от действия.
        """
        permission_classes = (IsAuthenticated,)
        if self.action in ["list", "retrieve"]:
            permission_classes = (IsAuthenticated,)
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = (IsOwner | IsAdmin,)
        return tuple(permission() for permission in permission_classes)
