import streamlit as st
from openai import OpenAI


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets["OPENAI_API_KEY"],
)

def ask_ai(question):
    completion = client.chat.completions.create(
        model="Qwen/Qwen3.8-27B:featherless-ai",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
    )

    content=completion.choices[0].message.content
    return content

st.title("My App-Ask Anything")
question=st.chat_input("Hey! Hi... Ask your Question...")

if question:
    st.write(f"User:{question}")
    st.write(f"Agent:{ask_ai(question)}")