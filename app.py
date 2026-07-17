import streamlit as st

st.set_page_config(
    page_title="AI-Powered Final Year Project Mentor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Redirect to Home page
st.switch_page("pages/Home.py")