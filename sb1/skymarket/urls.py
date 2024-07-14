from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# TODO здесь необходимо подклюючит нужные нам urls к проекту

schema_view = get_schema_view(
    openapi.Info(
        title="Skymarket API",
        default_version='v1',
        description="""
        Доска объявлений

        Бэкенд-часть проекта предполагает реализацию следующего функционала:

        - Авторизация и аутентификация пользователей.
        - Распределение ролей между пользователями (пользователь и админ).
        - Восстановление пароля через электронную почту.
        - CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
        - Под каждым объявлением пользователи могут оставлять отзывы.
        - В заголовке сайта можно осуществлять поиск объявлений по названию.
        """,
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),

    path('api/', include('users.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Документация
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
