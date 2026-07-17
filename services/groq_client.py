import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

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