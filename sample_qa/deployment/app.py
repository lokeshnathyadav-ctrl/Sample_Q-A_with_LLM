import streamlit as st
from langchain_groq import ChatGroq
st.title("Q&A with LLM")
groq_api_key = st.sidebar.text_input("ChatGroq API Key",type="password")
def generate_response(input_text):
  llm = ChatGroq(
    model = "meta-llama/llama-4-scout-17b-16e-instruct",           
    temperature = 0,                                               
    max_tokens = 512,                                              
    groq_api_key = groq_api_key)
  st.info(llm.invoke(input_text))
with st.form("my_form"):
  text=st.text_area(
      "Enter text: ",
      "What are the three key pieces of advice for learning how to code?",
  )
submitted = st.form_submit_button("Submit")
if not groq_api_key.startswith("gsk"):
  st.warning("Please enter your GroqChat API Key!", icon = "⚠")
if submitted and groq_api_key.startswith("gsk"):
  generate_response(text)                                 
