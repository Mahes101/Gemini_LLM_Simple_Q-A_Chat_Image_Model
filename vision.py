from dotenv import load_dotenv
load_dotenv() ##Loading all the enviromnet variables

import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load the gemini model for responses

model = genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(input,image):
    if input !="":
        
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)    
    return response.text


#Initialize the Streamlit app
st.set_page_config(page_title="Gemini Image Demo", page_icon=":robot:")

st.title("Image Demo")

st.header("Gemini Image Application")

input = st.text_input("input: ",key="input")
uploaded_file = st.file_uploader("Upload an image....", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
submit = st.button("Tell Me About the Image")

## When submit is clicked

if submit:
    response = get_gemini_response(input,image)
    st.header("The Response is:")
    st.write(response)