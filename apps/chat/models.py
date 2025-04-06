from django.db import models

from django.db import models
from apps.courses.models import Course  # Импортируем модель курса

class Chat(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chats")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Чат для курса {self.course.title}"
