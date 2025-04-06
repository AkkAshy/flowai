from rest_framework import generics
from .models import Chat
from .serializers import ChatSerializer
from rest_framework.permissions import IsAuthenticated

class ChatCreateView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
