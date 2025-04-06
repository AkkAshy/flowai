# lessons/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LessonDetailView,
    LessonListCreateView,
    TestViewSet,
    QuestionViewSet,
    ResultViewSet,
    SubmitTestAnswers,
)

# Создаем роутер для ViewSet
router = DefaultRouter()
router.register(r'tests', TestViewSet)  # Маршруты для тестов
router.register(r'questions', QuestionViewSet)  # Маршруты для вопросов
router.register(r'results', ResultViewSet)  # Маршруты для результатов

urlpatterns = [
    # Уроки
    path("", LessonListCreateView.as_view(), name="lesson-list-create"),  # Список уроков + создание
    path("<int:pk>/", LessonDetailView.as_view(), name="lesson-detail"),  # Детальный просмотр урока

    # Включаем маршруты для ViewSet (тесты, вопросы, результаты)
    path("", include(router.urls)),

    # Отправка ответов на тест
    path("submit-test/<int:test_id>/", SubmitTestAnswers.as_view(), name="submit-test"),
]