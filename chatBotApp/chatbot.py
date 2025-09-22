from botclass import Bot
import requests
import ast

#BASE_URL = "http://127.0.0.1:8000/api"
BASE_URL ="http://13.60.227.6:8000/api"

foods = {
    "salad": "vegetarian",
    "tofu stir-fry": "vegetarian",
    "vegetable soup": "vegetarian",
    "caprese sandwich": "vegetarian",
    "cheese pizza": "vegetarian",
    "mushroom risotto": "vegetarian",
    "falafel wrap": "vegetarian",
    "pasta primavera": "vegetarian",
    "vegetable curry": "vegetarian",
    "hummus with pita": "vegetarian",
    "grilled chicken": "non-vegetarian",
    "beef steak": "non-vegetarian",
    "pepperoni pizza": "non-vegetarian",
    "shrimp tacos": "non-vegetarian",
    "sushi (salmon)": "non-vegetarian",
    "fried chicken": "non-vegetarian",
    "lamb kebab": "non-vegetarian",
    "turkey sandwich": "non-vegetarian",
    "clam chowder": "non-vegetarian",
    "pork ribs": "non-vegetarian",
    "tuna salad": "non-vegetarian",
    "chicken curry": "non-vegetarian",
    "fish and chips": "non-vegetarian",
    "duck confit": "non-vegetarian",
    "meat lasagna": "non-vegetarian"
    }   

 #Conversation between AI and user(task3)
def chatbot_send_question(chatbot1):

    response = chatbot1.openAI_question_answer("You are now talking with an user, I want you to ask him literally only these question 'What are your top 3 favorite foods?'")   
    print(f"Bot asked you a question: {response.choices[0].message.content}")

    user_answer = input("Your answer: ")
  
    response = chatbot1.openAI_question_answer(f"You are now talking with an user, the user answered to your previews question that his favourites food are {user_answer}, please thank him for his answer, give a short opnion about his choice and say good bye")   
    print(f"Bot answered you!: {response.choices[0].message.content}")

#Simulate 100 conversations between 2 AIs(start by reseting the database)(task4)
def simulate_100_conversations(chatbot1,chatbot2):

    response = requests.delete(f"{BASE_URL}/conversations/delete_all/")
    print("DELETE response:", response.json())

    for x in range(100):
        print(f"Iteration {x+1}")

        response1 = chatbot1.openAI_question_answer("I want you to ask literelly and only these question,dont say anything else beside : 'What are your top 3 favorite foods?'")   
        print(f"Bot question!: {response1.choices[0].message.content}")

        #response2 = chatbot2.openAI_question_answer(
        #f"Using exactly this Python list {list(foods.keys())}, select 3 random items. "
        #"Return them as a valid Python list, e.g. ['food1', 'food2', 'food3']." \
        #"Answer only with the list, nothing else. " \
        #"Do NOT invent or modify names — copy them exactly from the list."
        #)

        response2 = chatbot2.openAI_question_answer(f"Using this list of foods: {list(foods.keys())},"
        "I want you to select randomly 3 elements from this list and answer in a list format like this: ['food1', 'food2', 'food3']."
        "Answer only the list, nothing else. Also dont change in any form the name of the elements, they have to be exactly the same names of the elemntes of the list I gave you "
        )   

        raw = response2.choices[0].message.content

        foods_selected = ast.literal_eval(raw)
        if(foods[foods_selected[0]] == "vegetarian" and foods[foods_selected[1]] == "vegetarian" and foods[foods_selected[2]] == "vegetarian"):
            is_vegetarian = True
        else:
            is_vegetarian = False

        #print(foods_selected) 
        #print("Is vegetarian?:", is_vegetarian)

        new_post = {
            "conversation_number": x+1,
            "chatgpt_a_question": response1.choices[0].message.content,
            "chatgpt_b_answer": foods_selected,
            "is_vegetarian": is_vegetarian
        }

        #print(new_post)

        response = requests.post(f"{BASE_URL}/conversations/", json=new_post)
        print("POST response:", response.json())
        print("\n")

#List all conversations that are vegetarian(task5)
def list_vegetarian_conversations():

    user = input("Enter username for authentication: ")
    password = input("Enter password for authentication: ")

    response = requests.get(f"{BASE_URL}/conversations/get_vegeterians/",auth=(user, password))

    if response.status_code == 200:
        print("GET response:")
        for x in response.json():
            print(x)
    elif response.status_code == 401:
        print("Authentication failed! Please check your username and password.")
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
  

def main():
    chatbot1 = Bot("Chatgpt A")
    chatbot2 = Bot("Chatgpt B")

    while(True):
        menu_choice = input("Choose an option:\n1. Chat with the bot(task3)\n2. Simulate 100 conversations between 2 bots(task4)\n3. List all vegetarian conversations(task5)\n4. Exit\nYour choice: ")
        match menu_choice:
            case "1":
                chatbot_send_question(chatbot1)
            case "2":
                simulate_100_conversations(chatbot1,chatbot2)
            case "3":
                list_vegetarian_conversations()
            case "4":
                print("Exiting...")
                break
            case _:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

