import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages import profile,overview,performance,predict, result

st.set_page_config(page_title="Portfolio App", page_icon="📈", layout="centered")

st.markdown("""
<style>
    [data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🚀 Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["👨‍💼 Profile", "📋 Project Overview", "🎯 Model Performance", "🗃 Result", "🔮 Prediction"]
)

if page == "👨‍💼 Profile":
    profile.show()
elif page == "📋 Project Overview":
    overview.show()
elif page == "🎯 Model Performance":
    performance.show()
elif page == "🗃 Result":
    result.show()
elif page == "🔮 Prediction":
    predict.show()


st.markdown("---")