from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Lesson, Test, Question, Result
from .serializers import LessonSerializer, TestSerializer, QuestionSerializer, ResultSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class SubmitTestAnswers(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, test_id):
        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            return Response({"error": "Тест не найден."}, status=404)

        if not test.is_published:
            return Response({"error": "Тест не опубликован."}, status=403)

        student = request.user
        if hasattr(test, 'attempts_allowed') and test.attempts_allowed <= test.attempts.filter(student=student).count():
            return Response({"error": "Превышено количество попыток."}, status=403)

        answers = request.data.get('answers', {})
        score = 0
        total_questions = 0

        for question in test.questions.all():
            total_questions += 1
            user_answer = answers.get(str(question.id))
            if user_answer == question.correct_answer:
                score += 1

        final_score = (score / total_questions) * 100 if total_questions > 0 else 0
        Result.objects.create(student=student, test=test, score=final_score)

        return Response({
            "message": "Тест завершен!",
            "score": final_score,
        })