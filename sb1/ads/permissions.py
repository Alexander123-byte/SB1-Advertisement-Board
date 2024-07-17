# TODO здесь производится настройка пермишенов для нашего проекта

from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAdmin(BasePermission):
    """
    Класс премишенов для проверки, является ли пользователь администратором.

    Методы:
        - has_permission(self, request, view): Проверяет, аутентифицирован ли пользователь.
        - has_object_permission(self, request, view, obj): Проверяет, является ли пользователь администратором.

    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN


class IsOwner(BasePermission):
    """
    Класс премишенов для проверки, является ли пользователь владельцем объекта.

    Методы:
        - has_permission(self, request, view): Проверяет, аутентифицирован ли пользователь.
        - has_object_permission(self, request, view, obj): Проверяет, является ли пользователь владельцем объекта.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user and request.user and obj.author == request.user
