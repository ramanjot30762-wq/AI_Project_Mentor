import os
import streamlit as st

from groq import Groq
from dotenv import load_dotenv

# Load local .env (for VS Code)
load_dotenv()

# Read API key:
# 1. Streamlit Secrets (deployment)
# 2. .env (local development)
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def get_ai_response(messages):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1200
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error:\n\n{e}"