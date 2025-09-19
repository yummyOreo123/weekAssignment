from django.db import models

class Conversation(models.Model):
    conversation_number = models.IntegerField(primary_key=True)
    chatgpt_a_question = models.TextField(default="What are your top 3 favorite foods?")
    chatgpt_b_answer = models.JSONField()  # stores list of 3 foods
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return f"Conversation {self.conversation_number}"