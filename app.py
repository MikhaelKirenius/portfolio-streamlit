import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages import profile, streamlit_app,overview, perfomance

st.set_page_config(page_title="Portfolio App", page_icon="📈", layout="centered")

st.markdown("""
<style>
    [data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)


# Navigation dari pages
st.sidebar.title("🚀 Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["👨‍💼 Profile", "📋 Butterfly Project Overview", "🎯 Model Performance", "🔮 Prediction"]
)

if page == "👨‍💼 Profile":
    profile.show()
elif page == "📋 Butterfly Project Overview":
    overview.show()
elif page == "🎯 Model Performance":
    perfomance.show()
elif page == "🔮 Prediction":
    streamlit_app.show()


st.markdown("---")