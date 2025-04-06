from rest_framework import serializers
from .models import Lesson, Test, Question, Result


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True, read_only=True)  # Включаем связанные тесты
    
    class Meta:
        model = Lesson
        fields = "__all__"
