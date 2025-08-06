import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import streamlit as st
from PIL import Image

profile_pic = Image.open("assets/profile.jpg")
project_image1 = Image.open("assets/Project_Rag.jpg")
project_image2 = Image.open("assets/Project_NLP.jpg")
project_image3 = Image.open("assets/Project_Clustering.jpg")

def show():
    st.markdown("""
            <style>
            .badge {
                display: inline-block;
                padding: 5px 10px;
                margin: 4px;
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
            }
            </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns([1, 3], gap="large")
        with col1:
            st.image(profile_pic, width=150, caption="Mikhael Kirenius Ranata")
        with col2:
            st.title("Hello, I'm Mikhael Kirenius Ranata 👋")
            st.write("### Aspiring Machine Learning Engineer | AI & Data Science Enthusiast | Former Full-Stack Developer")
            st.markdown("""
                I'm a tech professional transitioning from **Full-Stack Development** to **Machine Learning Engineering** and **AI solutions**.  
                I build **end-to-end intelligent systems** combining **data, models, and scalable apps**.

                Currently focused on:  
                ✔ Machine Learning & Deep Learning (CNN, Computer Vision)  
                ✔ Generative AI & LLMs (RAG, LangChain)  
                ✔ MLOps & Deployment (Docker, CI/CD, Model Serving)  
                ✔ Cloud (AWS for ML Deployment)  

                📬 Open to **Remote & Freelance Opportunities** in ML, AI, and Data Solutions.
                """)
            st.markdown("[📧 Email Me](mailto:mikhaelkireniusranata@gmail.com) "
            "| [💼 LinkedIn](https://www.linkedin.com/in/mikhaelkireniusranata/) | " \
            "[🐱 GitHub](https://github.com/MikhaelKirenius)")

    st.write("---")

    with st.container():
        st.subheader("Education")
        st.write("**Bachelor of Computer Science** - Bina Nusantara University, Jakarta, Indonesia (2019 - 2023),GPA : 3.39/4.00")
        st.write("**Machine Learning & AI Bootcamp** - Dibimbing, Jakarta, Indonesia (April 2025 - September 2025)")
  

    st.write("---")

    with st.container():
        st.subheader("Experience")
    
        experiences = [
              {
                "company": "Pro-int Dinamika, On-site Jakarta",
                "position": "Web Developer", 
                "period": "September 2024 – Jan 2025",
                "achievements": [
                    "Built robust back-end systems and APIs using C# and .NET framework for enterprise applications",
                    "Developed responsive front-end interfaces using JavaScript, React, and modern web frameworks",
                    " Performed code reviews and implemented version control using Git for team collaborations"
                ]
            },
            {
                "company": "PT. Accelist Lentera Indonesia, Remote Jakarta",
                "position": "Full Stack Developer",
                "period": "Maret 2022 – Maret 2023",
                "achievements": [
                    "Implemented responsive and user-friendly interfaces using modern front-end framework",
                    "Participated in Agile/Scrum development methodologies to ensure timely and iterative project delivery",
                    "Developed and maintained RESTful APIs for seamless communication between front-end and back-end systems"
                ]
            },
        ]
        
        for exp in experiences:
            with st.expander(f"{exp['position']} at {exp['company']} ({exp['period']})"):
                for achievement in exp['achievements']:
                    st.write(f"• {achievement}")


    st.write("---")

    with st.container():
        st.subheader("Projects")
        col1, col2 , col3 = st.columns(3, gap="large")

        with col1:
            st.image(project_image1)
            st.write("**Project:** AI-Powered Fashion Shopping Assistant.")
            st.markdown("[View Project](https://github.com/MikhaelKirenius/fashion-product-retrieval-llm)")

        with col2:
            st.image(project_image2)
            st.write("**Project:** AI-Generated Text Detection Using NLP & BERT.")
            st.markdown("[View Project](https://github.com/MikhaelKirenius/ai-generated-text-detector)")

        with col3:
            st.image(project_image3)
            st.write("**Project:** Customer Segmentation Using Clustering Algorithms.")
            st.markdown("[View Project](https://github.com/MikhaelKirenius/Customer-Segmentation-Clustering.git)")


    st.write("---")

    with st.container():
        st.subheader("Skills")

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            st.markdown("### 🌐 Web Development")
            st.markdown("""
            <span class="badge">HTML</span>
            <span class="badge">CSS</span>
            <span class="badge">JavaScript</span>
            <span class="badge">React.js</span>
            <span class="badge">Streamlit</span>
            <span class="badge">C#</span>
            <span class="badge">FastAPI</span>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("### 🤖 Machine Learning & Data Science")
            st.markdown("""
            <span class="badge">Python</span>
            <span class="badge">Pandas</span>
            <span class="badge">NumPy</span>
            <span class="badge">Scikit-learn</span>
            <span class="badge">TensorFlow</span>
            <span class="badge">PyTorch</span>
            <span class="badge">EDA</span>
            <span class="badge">Langchain</span>
            <span class="badge">NLP</span>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("### 🗄️ Database")
            st.markdown("""
            <span class="badge">MySQL</span>
            <span class="badge">PostgreSQL</span>
            <span class="badge">MongoDB</span>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown("### 🔧 Git & Tools")
            st.markdown("""
            <span class="badge">Git</span>
            <span class="badge">GitHub</span>
            <span class="badge">Docker</span>
            """, unsafe_allow_html=True)


    