from phonenumber_field import serializerfields
from rest_framework import serializers

from ads.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Comment.

    Поля:
        - author_id (ReadOnlyField): ID автора комментария.
        - ad_id (ReadOnlyField): ID объявления, к которому относится комментарий.
        - author_first_name (ReadOnlyField): Имя автора комментария.
        - author_last_name (ReadOnlyField): Фамилия автора комментария.
        - author_image (ImageField): Изображение автора комментария.
    """
    author_id = serializers.ReadOnlyField(source="author.id")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_image = serializers.ImageField(source="author.image", read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "text", "created_at", "author_id", "ad_id", "author_first_name", "author_last_name",
                  "author_image")


class AdSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Ad.

    Поля:
        - pk (IntegerField): Первичный ключ объявления.
        - image (ImageField): Изображение объявления.
        - title (CharField): Название товара.
        - price (PositiveIntegerField): Цена товара.
        - description (CharField): Описание товара.
    """
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Детализированный сериалайзер для модели Ad.

    Поля:
        - author_first_name (ReadOnlyField): Имя автора объявления.
        - author_last_name (ReadOnlyField): Фамилия автора объявления.
        - phone (PhoneNumberField): Телефонный номер автора объявления.
        - author_id (ReadOnlyField): ID автора объявления.
    """
    # TODO сериалайзер для модели
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "phone", "author_first_name", "author_last_name", "description",
                  "author_id")
