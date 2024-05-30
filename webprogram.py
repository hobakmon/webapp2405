import streamlit as st
from langchain_community.llms import OpenAI

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

# API 키를 미리 입력
openai_api_key = "sk-proj-stcasL0GN6kgYeaosjY7T3BlbkFJCiavsPtrnQuDkN4bIb3m"

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text)
    st.write(response)

with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')

if submitted:
    generate_response(text)
