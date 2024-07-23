from django.contrib.auth.models import (
    BaseUserManager
)
# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту


class UserManager(BaseUserManager):
    """
    Менеджер для модели пользователя.
    """
    def create_user(self, email, first_name, last_name, phone, password=None):
        """Создает и сохраняет пользователя с указанным адресом электронной почты, именем,
        фамилией, телефоном и паролем."""
        if not email:
            raise ValueError('Поле "Электронная почта" не может быть пустым!')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user"
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """Создает и сохраняет суперпользователя с указанным адресом электронной почты, именем,
        фамилией, телефоном и паролем."""
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
        )
        user.role = "admin"
        user.save(using=self._db)
        return user
