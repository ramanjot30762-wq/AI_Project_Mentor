import streamlit as st

st.set_page_config(
    page_title="About - AI Project Mentor",
    page_icon="ℹ️",
    layout="wide"
)

# Title
st.title("ℹ️ About AI-Powered Final Year Project Mentor")

st.markdown("---")

# Introduction
st.subheader("🎓 Project Overview")

st.write("""
The **AI-Powered Final Year Project Mentor** is an intelligent assistant
designed to help university students select suitable final-year project
topics based on their interests, technical skills, career goals, and
emerging technology trends.

The system uses Generative AI to provide personalized project guidance
instead of generic project lists.
""")

# Problem
st.subheader("❓ Problem Statement")

st.write("""
Many students struggle to select appropriate final-year projects because:

- They are unaware of current technology trends.
- They find it difficult to match projects with their skills.
- Existing project repositories provide generic ideas without personalization.
- Students need guidance on technology selection and project scope.
""")

# Solution
st.subheader("💡 Proposed Solution")

st.write("""
This application provides an AI-powered mentor that:

- Understands student requirements through conversation.
- Suggests personalized project ideas.
- Recommends suitable technologies.
- Provides project scope and implementation guidance.
- Helps students move from idea selection to project planning.
""")

# Technology Stack
st.subheader("🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Frontend**

    • Streamlit

    • Python

    • Custom UI Components
    """)

with col2:
    st.info("""
    **AI Engine**

    • Groq API

    • Llama 3.3 Model

    • Prompt Engineering
    """)

with col3:
    st.info("""
    **Development**

    • VS Code

    • Git

    • GitHub
    """)


# Future Enhancement
st.subheader("🚀 Future Enhancements")

st.write("""
Future versions of this system can include:

- 📚 Research paper recommendation using RAG
- 📄 Automatic project proposal generation
- 📅 Project timeline planning
- 👨‍🏫 Faculty mentoring dashboard
- 📊 Student project progress tracking
- 🗂️ University project repository integration
""")

# Developer section
st.markdown("---")

st.subheader("👨‍💻 Project Vision")

st.write("""
The goal of this project is to bridge the gap between students and
innovative project ideas by providing accessible AI-based academic
guidance.
""")