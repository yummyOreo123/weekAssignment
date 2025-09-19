from django.urls import path
from .views import ConversationListCreateView,DeleteAllConversations,GetConversationsVegetarianTrue

urlpatterns = [
    path('conversations/', ConversationListCreateView.as_view(), name='conversation-list-create'),
    path('conversations/delete_all/', DeleteAllConversations.as_view(), name='delete-all-conversations'),
    path('conversations/get_vegeterians/', GetConversationsVegetarianTrue.as_view(), name='get-vegeterians'),
]

