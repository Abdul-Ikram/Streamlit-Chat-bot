import streamlit as st
import requests
import time

# Sidebar with information and slider
st.sidebar.title("About This Chatbot📃")
st.sidebar.write("""
    You are interacting with a chatbot that is designed to assist with your queries.
    The chatbot may provide humorous or straightforward responses depending on the context.
    Use the slider below to adjust the speed at which the chatbot's responses are displayed.
""")

response_speed = st.sidebar.slider("Response Speed (seconds per character)", min_value=0.01, max_value=0.2, value=0.05, step=0.01)

# Main interface
st.title("Open AI Chatbot🤖")
st.write("Ask me Anything🙄")

# Initialize chat history in session state:
if 'responses' not in st.session_state:
    st.session_state.responses = []

# Display chat history
for message in st.session_state.responses:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input("Prompt your query here!")

if prompt:
    with st.chat_message('user'):
        st.markdown(prompt.capitalize())
    
    st.session_state.responses.append({'role': 'user', 'content': prompt})

    request = {
        "user_prompt": prompt
    }

    response = requests.post("http://127.0.0.1:8000/prompt", json=request)
    
    if response.status_code == 200:
        full_response = response.json().get('response', '')

        # Simulate streaming by showing one character at a time
        with st.chat_message('ai'):
            progress_text = st.empty()

            for i in range(len(full_response)):
                progress_text.markdown(full_response[:i + 1])
                time.sleep(0.05)

        st.session_state.responses.append({
            'role': 'assistant',
            'content': full_response
        })

    else:
        with st.chat_message('ai'):
            st.markdown("Error: Unable to get a response from the server.")
