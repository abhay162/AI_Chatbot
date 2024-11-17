def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif "what is your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "help" in user_input:
        return "I can help with various questions. Just ask!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you need anything else, feel free to ask."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

# Main function to run the chatbot
def chat():
    print("Chatbot: Hi there! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
