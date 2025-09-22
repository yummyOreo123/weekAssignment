from openai import OpenAI
import os
from dotenv import load_dotenv

class Bot:
    def __init__ (self, name):  
        load_dotenv(".env")
        self.name = name
        self.client = OpenAI(api_key=os.getenv("API_KEY"))

    def openAI_question_answer(self,content):  
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": content}]
        )
        return response
        
