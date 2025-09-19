from rest_framework import serializers
from .models import Conversation

# Serializer for the Conversation model JSON -> Python 
class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'   # expose all fields

class ConversationGetVegetarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['chatgpt_b_answer']  # only this field