import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.chat import consumers

# Устанавливаем переменную окружения для настройки проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Определяем маршруты и конфигурируем ASGI приложение
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # для обычных HTTP запросов
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<course_id>/', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
