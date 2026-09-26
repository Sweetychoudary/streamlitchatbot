import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Chatbot")
st.caption("Powered by Ollama + Llama 3.2")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    ai_message = response["message"]["content"]

    # Add AI response to history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_message
        }
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.write(ai_message)

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

