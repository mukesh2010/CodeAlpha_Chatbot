def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    elif "name" in user_input:
        return "I'm a simple chatbot built in Python."
    elif "help" in user_input:
        return "You can say hello, ask how I am, or say bye to leave."
    else:
        return "Sorry, I don't understand that. Try saying hello, how are you, or bye."


def start_chat():
    print("Chatbot: Hi! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


start_chat()
