from django.urls import path, include

urlpatterns = [
    # Маршруты для пользователей
    path('users/', include('apps.users.urls')),

    # Маршруты для курсов
    path('courses/', include('apps.courses.urls')),

    # Маршруты для уроков, тестов и вопросов
    path('lessons/', include('apps.lessons.urls')),
]