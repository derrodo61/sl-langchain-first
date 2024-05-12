import streamlit as st
from langchain_openai import OpenAI

st.title("RD - Minimalistic first app")


openai_api_key = st.sidebar.text_input("OpenAI API Key")
submit_button = st.sidebar.button("Submit")


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Enter some text here to generate a response from the OpenAI language model.",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
