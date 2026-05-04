import streamlit as st
from chatbot import get_response

st.title("🤖 Smart AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        response = get_response(user_input)
        
        
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
