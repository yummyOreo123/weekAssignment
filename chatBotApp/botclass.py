from openai import OpenAI
import os
from dotenv import load_dotenv

class Bot:
    def __init__ (self, name):  
        #load_dotenv(".env")
        self.name = name
        self.client = OpenAI(api_key='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')

    def openAI_question_answer(self,content):  
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": content}]
        )
        return response
        
