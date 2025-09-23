from botclass import Bot
import requests
from auxiliary import  validate_food_response, validate_food_bool

#BASE_URL = "http://127.0.0.1:8000/api"
BASE_URL ="http://13.60.227.6:8000/api"

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

    #Simulate 100 conversations between 2 AIs
    for x in range(100):
        print(f"Iteration {x+1}")

        response1 = chatbot1.openAI_question_answer("I want you to ask literelly and only these question,dont say anything else beside : 'What are your top 3 favorite foods?'")   
        print(f"Bot question!: {response1.choices[0].message.content}")

        prompt = (
        "I want you to select randomly 3 dishes/foods and answer ONLY in this list format: "
        "['food1', 'food2', 'food3']"
        )

        # Ensure valid response with 3 retries, so we get exactly 3 foods in list format
        for attempt in range(3):
            response = chatbot1.openAI_question_answer(prompt)

            raw = response.choices[0].message.content.strip()

            try:
                validated = validate_food_response(raw) #validate response
                break  
            except Exception as e:
                print(f"Validation failed (attempt {attempt+1}): {e}")

 
        foods_selected = validated.foods #list of 3 foods

        final_answers = []

        for food in foods_selected: #check if each food is vegetarian or non-vegetarian
            for attempt in range(3): #3 attempts to validate each food vegetarian or not
                response = chatbot1.openAI_question_answer(
                    f"Confirm if food {food} is vegetarian or non-vegetarian, answer ONLY with the word vegetarian or non-vegetarian."
                )
                raw = response.choices[0].message.content.strip()
                try:
                    validated = validate_food_bool(raw) #validate response
                    final_answers.append(validated.type)
                    break
                except Exception as e:
                    print(f"Validation failed for {food} (attempt {attempt+1}): {e}")


        is_vegetarian = all(f == "vegetarian" for f in final_answers) #True if all foods are vegetarian
    
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

