# Python Chatbot with ChatGPT API Integration  

## Project Overview  
This project is a hybrid chatbot built using Python. It combines rule-based responses for predefined queries and dynamic, AI-generated responses from OpenAI's ChatGPT API via RapidAPI. The chatbot is designed to simulate human-like conversations while demonstrating efficient API integration and error handling.

---

## Features  
- **Rule-Based Responses**: Predefined patterns and responses for common queries.  
- **AI-Powered Responses**: Dynamic responses generated using the ChatGPT API.  
- **Hybrid Design**: Combines the speed of rule-based logic with the intelligence of AI-powered conversations.  
- **Error Handling**: Handles API errors gracefully and provides informative feedback.  
- **Interactive Chat**: Users can chat with the bot in real time, exiting the session with the `exit` command.  

---

## Prerequisites  
1. **Python**: Ensure Python 3.7 or later is installed.  
2. **API Key**: Obtain an API key from [RapidAPI](https://rapidapi.com).  
3. **Libraries**: Install required Python libraries (see Installation section).  

---

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/python-chatbot.git
   cd python-chatbot
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate          # On Windows
Install dependencies:

bash:
pip install -r requirements.txt
Set up your API key:

Open the chatbot.py file.
Replace the placeholder <Your-RapidAPI-Key> with your actual RapidAPI key.


Run the chatbot:
python chatbot.py
Start chatting! Type your queries into the console and receive responses. To exit, type exit.


The main script that:
Handles rule-based responses using NLTK's Chat module.
Integrates with ChatGPT API via HTTP requests to generate dynamic responses.
Manages the interactive chatbot loop.

Example Interaction
Chatbot: Hi! I'm here to assist you. Type 'exit' to end the conversation.  
You: Hi  
Chatbot: Hello! How can I assist you today?  
You: Can you tell me a joke?  
Chatbot: Why don't scientists trust atoms? Because they make up everything!  
You: What is your name?  
Chatbot: I am a chatbot created to assist you.  
You: exit  
Chatbot: Goodbye!  

API Details
Endpoint:
https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions

Headers:
json
{
  "X-RapidAPI-Key": "<Your-RapidAPI-Key>",
  "X-RapidAPI-Host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com"
}
Request Payload:

json
{
  "prompt": "User's input",
  "max_tokens": 50
}

Dependencies
nltk
requests


Improvements & Future Work
Add more rule-based patterns and responses for better user experience.
Extend API integration for more advanced AI responses (e.g., context-aware chats).
Develop a GUI using tkinter or PyQt for a user-friendly interface.
Integrate voice input/output for accessibility.
License
This project is licensed under the MIT License.
AUTHOR : PUJALISANDHYASREE
