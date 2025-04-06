from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Определяем список выборов для ролей
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    
    # Поля модели
    email = models.EmailField(unique=True)  # Email обязателен и уникален
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Телефон (необязательно)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')  # Роль пользователя
    
    def __str__(self):
        return self.username
