# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код приложения
COPY . .

# Открываем порт для приложения
ARG APP_PORT
EXPOSE $APP_PORT

# Команда для запуска приложения
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${APP_PORT}"]
