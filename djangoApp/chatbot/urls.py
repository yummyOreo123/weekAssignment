from django.urls import path
from .views import ConversationListCreateView, ConversationDetailView

urlpatterns = [
    path('conversations/', ConversationListCreateView.as_view(), name='conversation-list-create'),
    path('conversations/<int:conversation_number>/', ConversationDetailView.as_view(), name='conversation-detail'),
]

