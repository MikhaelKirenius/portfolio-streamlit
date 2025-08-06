import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the app"""
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
        }
        
        .section-header {
            font-size: 2rem;
            font-weight: bold;
            color: #2E86C1;
            border-bottom: 2px solid #2E86C1;
            padding-bottom: 0.5rem;
            margin: 1.5rem 0;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin: 0.5rem 0;
        }
        
        .info-box {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #2E86C1;
            margin: 1rem 0;
        }
        
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }
        
        .profile-image {
            border-radius: 50%;
            border: 3px solid #2E86C1;
            margin: 1rem auto;
            display: block;
        }
        
        .success-card {
            background-color: #27AE60;
            padding: 1rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin: 0.5rem 0;
        }
        
        .error-card {
            background-color: #E74C3C;
            padding: 1rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin: 0.5rem 0;
        }
        
        .warning-card {
            background-color: #F39C12;
            padding: 1rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin: 0.5rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

def create_metric_card(value, label, color="gradient"):
    """Create a metric card with custom styling"""
    if color == "gradient":
        card_class = "metric-card"
    elif color == "success":
        card_class = "success-card"
    elif color == "error":
        card_class = "error-card"
    elif color == "warning":
        card_class = "warning-card"
    else:
        card_class = "metric-card"
    
    return f'<div class="{card_class}"><h3>{value}</h3><p>{label}</p></div>'

def create_section_header(text):
    """Create a section header with custom styling"""
    return f'<div class="section-header">{text}</div>'

def create_main_header(text):
    """Create a main header with custom styling"""
    return f'<div class="main-header">{text}</div>'

def create_info_box(content):
    """Create an info box with custom styling"""
    return f'<div class="info-box">{content}</div>'