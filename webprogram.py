import streamlit as st
from langchain_community.llms import OpenAI

st.title('🍎🍐🍊 유선미의 AI Chat 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text)
    st.write(response)  # st.info() 대신 st.write()를 사용합니다.

with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')

if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')

if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
