import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI-Powered Final Year Project Mentor",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎓 AI Mentor")
st.sidebar.markdown("---")
st.sidebar.write("### Navigation")
st.sidebar.button("🏠 Home")
st.sidebar.button("💬 Chat")
st.sidebar.button("ℹ️ About")

# -----------------------------
# Main Page
# -----------------------------
st.title("🎓 AI-Powered Final Year Project Mentor")

st.markdown("""
Welcome to your **AI Project Mentor**.

This chatbot helps students discover personalized final-year project ideas based on:

- 🎯 Interests
- 💻 Programming Skills
- 📚 Branch
- 🚀 Career Goals
- ⭐ Difficulty Level
""")

st.success("Click the button below to start your AI mentoring journey!")

if st.button("🚀 Start AI Mentor"):
    st.info("Great! In the next step, we'll connect this app to the Grok API.")