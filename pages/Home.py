import streamlit as st

st.set_page_config(
    page_title="AI Project Mentor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Final Year Project Mentor")

st.subheader("Find the perfect final-year project with Artificial Intelligence")

st.markdown("---")

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
### 🎓 Your AI Mentor will help you

1. Discover innovative project ideas

2.  Match projects with your skills

3. Recommend trending technologies

4 Suggest datasets and tools

5. Generate project summaries
""")

    if st.button("💬 Start AI Mentor", use_container_width=True):
        st.switch_page("pages/AI_Mentor.py")

with col2:
    st.info(
        """
🎯 Personalized Recommendations

🧠 AI Powered

📚 Latest Technologies

💻 Career Focused
"""
    )

st.markdown("---")

st.subheader("🔥 Popular Domains")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🤖 Artificial Intelligence")

with c2:
    st.success("🏥 Healthcare")

with c3:
    st.success("🌾 Agriculture")

c4, c5, c6 = st.columns(3)

with c4:
    st.success("🔐 Cyber Security")

with c5:
    st.success("📊 Data Science")

with c6:
    st.success("🚗 IoT")