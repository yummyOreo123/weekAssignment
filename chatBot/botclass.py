import openai

class Bot:
    def __init__ (self, name):  
        self.name = name

    def send_question(self):
        print("Sending a question!")

    def answer(seld):
        print("answer!")

    def openAI_question_answer(self,content):  # method
        print(f"Hello, my name is {self.name}")
        openai.api_key = "your_api_key_here"

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello!"}]
        )
