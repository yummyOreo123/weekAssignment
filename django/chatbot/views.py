from rest_framework import generics
from .models import Conversation
from .serializers import ConversationSerializer,ConversationGetVegetarianSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation
from rest_framework.permissions import IsAuthenticated



class ConversationListCreateView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class DeleteAllConversations(APIView):
    def delete(self, request, *args, **kwargs):
        deleted_count, _ = Conversation.objects.all().delete()
        return Response(
            {"message": f"Deleted {deleted_count} conversations."},
            status=status.HTTP_200_OK
    )

class GetConversationsVegetarianTrue(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Conversation.objects.filter(is_vegetarian=True)
        serializer = ConversationGetVegetarianSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)