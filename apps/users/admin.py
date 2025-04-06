from django.contrib import admin
from .models import User

# Регистрируем модель User в админке
admin.site.register(User)
