from django.shortcuts import render

from rest_framework import generics
from .models import Conversation
from .serializers import ConversationSerializer


class ConversationListCreateView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

# Retrieve, update, or delete by conversation_number
class ConversationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    lookup_field = 'conversation_number'  # since that’s your PK