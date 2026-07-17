import streamlit as st

from services.groq_client import get_ai_response
from prompts.mentor_prompt import SYSTEM_PROMPT

st.set_page_config(
    page_title="AI Mentor",
    page_icon="🤖",
    layout="wide"
)
st.set_page_config(
    page_title="AI Mentor",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🎓 AI Project Mentor")

    st.markdown("---")

    st.write("### 🛠️ Built With")

    st.success("🐍 Python")
    st.success("🎨 Streamlit")
    st.success("⚡ Groq API")
    st.success("🧠 Llama 3.3 70B")

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """
# 👋 Welcome!

Chat history has been cleared.

How can I help you with your final-year project today?
"""
            }
        ]

        st.rerun()

    st.markdown("---")

    st.caption("Version 1.0")

st.title("🎓 AI-Powered Final Year Project Mentor")
st.caption("Your intelligent assistant for selecting innovative final-year projects.")
st.title("🤖 AI Project Mentor")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
# 👋 Welcome to AI-Powered Final Year Project Mentor

I'm your AI mentor, and I'll help you discover the best final-year project based on your interests, skills, and career goals.

### 🚀 I can help you with:
- 🎓 Personalized final-year project ideas
- 🤖 AI, Machine Learning, and Deep Learning projects
- 🌾 Agriculture, Healthcare, IoT, Cybersecurity, and Data Science projects
- 💻 Technology stack recommendations
- 📄 Project abstracts and problem statements
- 📈 Industry-relevant and trending project ideas

### 💡 You can ask me things like:
- Recommend AI projects for beginners
- I know Python and Machine Learning. Suggest project ideas.
- Healthcare project ideas using AI
- Final-year projects in Computer Vision
- IoT projects for engineering students

**Let's get started! Tell me about yourself or ask your first question. 😊**
"""
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
st.markdown("### 🚀 Quick Start")

col1, col2 = st.columns(2)

with col1:
    ai_project = st.button("🤖 AI Projects", use_container_width=True)
    healthcare = st.button("🏥 Healthcare", use_container_width=True)
    agriculture = st.button("🌾 Agriculture", use_container_width=True)

with col2:
    ds = st.button("📊 Data Science", use_container_width=True)
    cyber = st.button("🔐 Cyber Security", use_container_width=True)
    cv = st.button("👁️ Computer Vision", use_container_width=True)

quick_prompt = None

if ai_project:
    quick_prompt = "Recommend AI-based final-year projects."

elif healthcare:
    quick_prompt = "Suggest AI projects in Healthcare."

elif agriculture:
    quick_prompt = "Suggest AI projects in Agriculture."

elif ds:
    quick_prompt = "Recommend Data Science projects."

elif cyber:
    quick_prompt = "Recommend Cyber Security projects."

elif cv:
    quick_prompt = "Suggest Computer Vision final-year projects."
typed_input = st.chat_input("Describe your interests...")

user_input = quick_prompt if quick_prompt else typed_input

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(st.session_state.messages)

    with st.spinner("Thinking..."):
        response = get_ai_response(conversation)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)