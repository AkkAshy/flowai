from django.contrib import admin
from .models import Lesson, Test, Question, Result

admin.site.register(Lesson)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Result)