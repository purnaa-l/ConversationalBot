from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load Gemini Pro model and get gemini response

model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])
 
def get_gemini_response(question):
    response=chat.send_message(question, stream=True)
    return response

st.header("Conversational Q&A ChatBot")
if 'chat_history' not in st.session_state:
    st.session_state['chat-history']=[]

input=st.text_input("Input: ", key=input)
submit=st.button("Get the response here!")

if submit and input:
        response=get_gemini_response(input)
        st.session_state['chat-history'].append(("You", input))
        st.subheader("Your Response is:")
        for chunk in response:
             st.write(chunk.text)
             st.session_state['chat-history'].append(("Bot", chunk.text))
        st.subheader("The Chat History is: ")

for role, text in st.session_state['chat-history']:
     st.write(f"{role}:{text}")

