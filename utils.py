# chatbot/utils.py

import json

def load_sample_data(filename='data/sample_data.json'):
    """Load sample data for the chatbot."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return []

def save_conversation(conversation, filename='data/conversation_history.json'):
    """Save conversation history."""
    try:
        with open(filename, 'a') as file:
            json.dump(conversation, file)
            file.write("\n")
    except Exception as e:
        print(f"Error saving conversation: {e}")
