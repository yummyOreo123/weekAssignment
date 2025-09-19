from botclass import Bot

def main():
    print("This is the main function.")
    chatbot1 = Bot("Chatgpt A")
    chatbot2 = Bot("Chatgpt B")

    for x in range(100):
        print(f"Iteration {x+1}")
        chatbot1.send_question()
        chatbot2.answer()
      

if __name__ == "__main__":
    main()

