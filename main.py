# main.py

from chatbot.chatbot import SimpleChatbot
from chatbot.utils import save_conversation

def start_chat():
    print("Chatbot: Hello! How can I assist you today?")
    chatbot = SimpleChatbot()
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")
        
        conversation_history.append({"user": user_input, "bot": response})
        save_conversation(conversation_history)

if __name__ == "__main__":
    start_chat()
