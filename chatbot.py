
def chatbot(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "python": "Python is an amazing programming language!",
    }
    return responses.get(user_input.lower(), "I didn't understand that.")

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    print(f"Bot: {chatbot(user_input)}")

