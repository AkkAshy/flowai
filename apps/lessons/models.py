from django.db import models
from apps.courses.models import Course  # Импортируем модель курсов



class Lesson(models.Model):
    course = models.ForeignKey('courses.Course', related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField()  # Порядок урока в курсе
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"
    


class Test(models.Model):
    TEST_TYPES = (
        ('choice', 'Выбор ответа'),
        ('text', 'Текстовый ответ'),
        ('interactive', 'Интерактивный вопрос'),
    )
    lesson = models.ForeignKey(Lesson, related_name='tests', on_delete=models.CASCADE)  # Связь с уроком
    title = models.CharField(max_length=255)
    test_type = models.CharField(max_length=20, choices=TEST_TYPES)
    content = models.JSONField()  # Вопросы и варианты ответов
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    options = models.JSONField(null=True, blank=True)  # Для выбора ответа
    correct_answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text

class Result(models.Model):
    student = models.ForeignKey('users.User', related_name='results', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='results', on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.test.title}"

