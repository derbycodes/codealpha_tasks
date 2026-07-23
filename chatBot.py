def get_response(user_input):
    """
    Look at what the user typed and return a matching reply,
    using a simple if-elif chain of predefined rules.
    """
    message = user_input.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif "how are you" in message:
        return "I'm fine, thanks! How about you?"
    elif message in ("bye", "goodbye", "see you"):
        return "Goodbye!"
    elif "your name" in message:
        return "I'm a simple rule-based chatbot!"
    elif "thank" in message:
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that yet. Try saying 'hello', 'how are you', or 'bye'."


def chat():
    print("Chatbot: Hi! Type 'bye' anytime to end our chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ("bye", "goodbye", "see you"):
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()