from django.contrib import admin
from .models import Conversation

# Register your models here.

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_number', 'is_vegetarian','chatgpt_a_question', 'chatgpt_b_answer')
    search_fields = ('conversation_number',)
