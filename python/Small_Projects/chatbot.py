def chatbot_response(user_input):

    user_input = user_input.strip().lower()
    rules = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "hey": "Hello!",
        "bye": "Goodbye! Have a nice day.",
        "time": "I can tell you time if you add a real clock module.",
        "your name": "I'm a simple rule-based chatbot.",
        "creator": "I was created by you!",
        "help": "Sure, tell me what you need help with."
    }

    if user_input == "Exit".strip().lower():
        print("Goodbye! Have a nice day.")

    if user_input in rules:
        return rules[user_input]

    if "weather" in user_input:
        return "I can check live weather for you, but looks like its sunny outside!"
    if "age" in user_input:
        return "I am around 20 years old!"
    if "python" in user_input:
        return "Python is a greate programming language for beginners"

    # default fallback
    return "I dont understand that yet. Try asking something else"


    # chat loop
print(f"Chatbot: Hello. Press 'bye' to exit")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print(f"Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user)}")
