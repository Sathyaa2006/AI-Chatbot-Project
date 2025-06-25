import streamlit as st
from difflib import get_close_matches

# Page configuration
st.set_page_config(page_title="ChitChat", layout="centered")

# Title
st.title("💬 ChitChat - Your AI Chat Companion")

# Predefined response base
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hey there! What would you like to talk about?",
    "how are you": "I'm doing great! Thanks for asking.",
    "your name": "I'm ChitChat — your smart little chatbot.",
    "bye": "Goodbye! Come back soon!",
    "exit": "See you next time!",
    "what is ai": "AI stands for Artificial Intelligence — it allows machines to learn and think.",
    "what can you do": "I can answer questions, have basic conversations, and make you smile!",
    "thank you": "You're welcome!",
    "tell me a joke": "Why was the computer cold? Because it forgot to close its Windows!",
    "how to learn python": "You can start learning Python from freeCodeCamp, Codecademy, or W3Schools!",
    "give a basic python code": 
        "Sure! Here's a simple Python program that prints 'Hello, World!':\n```python\nprint('Hello, World!')\n```",

    "what is a variable in python": 
        "A variable stores data. Example:\n```python\nx = 10\nname = 'Alice'\n```",

    "what is a function in python": 
        "A function is a block of code that runs when called:\n```python\ndef greet():\n    print('Hello!')\ngreet()\n```",

    "how to use if else in python": 
        "Here’s a basic if-else example:\n```python\nx = 5\nif x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')\n```",

    "what is a loop in python": 
        "Loops help repeat actions. Example using a for-loop:\n```python\nfor i in range(3):\n    print(i)\n```"
}

# Smart reply function
def generate_reply(user_msg):
    user_msg = user_msg.lower().strip()
    match = get_close_matches(user_msg, responses.keys(), cutoff=0.65)
    if match:
        return responses[match[0]]
    else:
        return "Hmm, I’m not sure how to respond to that. Try rephrasing?"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat messages
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.markdown(f"**🧍 You:** {msg}")
    else:
        st.markdown(f"**🤖 ChitChat:** {msg}")

# Input box stays always at bottom
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="Ask something...")
    submitted = st.form_submit_button("Send")

# Handle user input
if submitted and user_input:
    st.session_state.messages.append(("user", user_input))
    reply = generate_reply(user_input)
    st.session_state.messages.append(("bot", reply))
    st.rerun()