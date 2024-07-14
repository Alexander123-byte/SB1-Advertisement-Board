from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {
    "blank": True,
    "null": True
}


class UserRoles(models.TextChoices):
    """
    Класс для определения ролей пользователя.
    """
    # TODO закончите enum-класс для пользователя
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractBaseUser):
    """
    Кастомная модель пользователя.

    Поля:
        - first_name (str): Имя пользователя, макс. длина 50 символов.
        - last_name (str): Фамилия пользователя, макс. длина 50 символов.
        - email (EmailField): Электронная почта пользователя (уникальная).
        - phone (PhoneNumberField): Номер телефона пользователя.
        - role (str): Роль пользователя (по умолчанию - user).
        - image (ImageField): Фото пользователя.
        - is_active (bool): Активен ли аккаунт пользователя.

    Методы:
        - is_superuser(): Возвращает 'True', если пользователь является администратором.
        - is_staff(): Возвращает 'True', если пользователь является администратором.
        - has_perm(): Проверяет, имеет ли пользователь определенное разрешение. Возвращает 'True' для администратора.
        - has_module_perms(): Проверяет, имеет ли пользователь разрешение для определенного модуля. Возвращает 'True'
        для администраторов.
        - is_admin(): Свойство, возвращающее 'True', если пользователь является администратором.
        - is_user(): Свойство, возвращающее 'True', если пользователь является обычным пользователем.
        - __str__(): Возвращает строковое представление пользователя (его email).

    Метаданные:
        - verbose_name: Имя модели.
        - verbose_name_plural: Имя модели во множественном числе.
        - ordering: Поле, по которому выполняется сортировка объектов модели.
    """
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    username = None
    first_name = models.CharField(max_length=50, verbose_name='Имя', help_text='Укажите имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Укажите фамилию')
    email = models.EmailField(verbose_name='Электронная почта', unique=True, help_text='Укажите электронную почту')
    phone = PhoneNumberField(verbose_name='Номер телефона', help_text='Укажите номер телефона')
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.USER,
                            verbose_name='Роль пользователя', help_text='Укажите роль пользователя')
    image = models.ImageField(upload_to='avatars/', verbose_name='Фото', help_text='Загрузите Ваше фото', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Аккаунт активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
