# Установка базового образа Python
FROM python

# Добавление метаданных об авторе
LABEL maintainer="Defekret"

# Установка переменных окружения для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/local/lib/python3.x/site-packages/:/usr/local/bin/python

# Копирование всех файлов приложения в каталог рабочей директории
COPY project /app_knad

# Установка зависимостей Python
RUN pip install --upgrade pip
RUN pip install -r app_knad/requirements.txt

# Запуск приложения`
CMD ["python", "app_knad/manage.py", "runserver", "0.0.0.0:80"]
