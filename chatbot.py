import requests
import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define the chatbot responses using a set of patterns and responses
patterns_and_responses = [
    (r'hi|hello', ['Hello! How can I assist you today?', 'Hi there! How can I help you?']),
    (r'how are you?', ['I am good, thank you for asking!', 'I am doing well, how about you?']),
    (r'bye', ['Goodbye! Have a great day!', 'Bye! Take care!']),
    (r'what is your name?', ['I am a chatbot created to assist you.', 'You can call me Chatbot.']),
    (r'help', ['I am here to help you. What do you need assistance with?', 'How can I assist you today?']),
    # Add more patterns and responses as needed
]

# Initialize chatbot with the defined patterns and responses
chatbot = Chat(patterns_and_responses, reflections)

# Define a function to get the response from the external API
def chatbot_response(user_input):
    url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"

    headers = {
        "X-RapidAPI-Key": "1a4b32723bmsh7e81c469b67e91ap127338jsn406e08d8124a",  # Replace with your actual RapidAPI key
        "X-RapidAPI-Host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    # Correct the data structure with 'messages' and 'model' fields
    data = {
        "model": "gpt-4",  # You can change this model name to 'gpt-3.5-turbo' if needed
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 50
    }

    # Make the POST request to the API
    response = requests.post(url, headers=headers, json=data)

    # Handle response and errors
    if response.status_code == 200:
        try:
            response_data = response.json()
            return response_data.get("choices", [{}])[0].get("message", {}).get("content", "Sorry, I couldn't understand that.")
        except ValueError:
            return "Error: Unable to parse response from the API."
    else:
        return f"Error: {response.status_code} - {response.text}"

# Define the function to start the chatbot interaction
def start_chat():
    print("Chatbot: Hi! I'm here to assist you. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Get the response from the external API or the internal chatbot logic
        response = chatbot_response(user_input)
        
        print("Chatbot:", response)

# Start the chatbot
start_chat()
