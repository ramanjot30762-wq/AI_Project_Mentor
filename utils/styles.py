import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .main {
        padding-top: 1rem;
    }

    .hero-title{
        font-size:48px;
        font-weight:800;
        color:#2563EB;
        margin-bottom:0;
    }

    .hero-subtitle{
        font-size:22px;
        color:#555;
        margin-top:0;
    }

    .feature-card{
        background:#F8FAFC;
        padding:20px;
        border-radius:15px;
        border:1px solid #E5E7EB;
        margin-bottom:15px;
    }

    .feature-title{
        font-size:22px;
        font-weight:700;
        color:#111827;
    }

    .feature-text{
        color:#6B7280;
        font-size:16px;
    }

    div.stButton > button{
        background:#2563EB;
        color:white;
        border:none;
        border-radius:10px;
        padding:12px 30px;
        font-size:18px;
        font-weight:600;
    }

    div.stButton > button:hover{
        background:#1D4ED8;
    }

    </style>
    """, unsafe_allow_html=True)