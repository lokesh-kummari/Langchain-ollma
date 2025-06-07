import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")    
os.environ["LANGCHAIN_TRACING_V2"] = "true"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can answer questions and help with tasks."),
        ("user", "question: {question}"),
    ]
)

st.title("Langchain demo with Ollama")
input_text=st.text_input("what question do you want to ask?")

llm=Ollama(model="llama3.2:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))














