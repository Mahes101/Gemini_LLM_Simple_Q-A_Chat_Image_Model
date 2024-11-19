from dotenv import load_dotenv
load_dotenv() ##Loading all the enviromnet variables

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load the gemini model for responses

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo", page_icon=":robot:")

st.title("Q&A Demo")

st.header("Gemini Application")

input = st.text_input("input: ",key="input")
submit = st.button("Ask the Question")

## When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.header("The Response is:")
    st.write(response)
        
    
