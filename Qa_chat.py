from dotenv import load_dotenv
load_dotenv() ##Loading all the enviromnet variables

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the gemini model for responses

model = genai.GenerativeModel("models/gemini-1.5-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo", page_icon=":robot:")

st.title("Q & A Chat Demo")
st.header("Gemini LLM Application for Q & A")

#Initialize Session State for Chat History if does not exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

input = st.text_input("Input: ",key="input")
submit = st.button("Ask the Question")

# When submit is clicked    
if submit and input:    
    response = get_gemini_response(input)
    ## Add the user query to the chat history
    st.session_state.chat_history.append({"You", input})
    
    st.header("The Response is:")
    for chunk in response:
        st.write(chunk.text)
        ## Add the response to the chat history
        st.session_state.chat_history.append({"Bot",chunk.text})

    
st.header("Chat History")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")    