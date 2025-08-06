import streamlit as st
import pandas as pd
from utils.styling import create_metric_card

def show():

    st.title("🔍 Customer Segmentation Project Overview")

    st.header("📦 Dataset Information")
    st.markdown("""
    - **Dataset:** *Customer Segmentation: Clustering* by Vishakh Patel on Kaggle  
    - **Source:** [Kaggle Dataset – Customer Segmentation: Clustering](https://www.kaggle.com/datasets/vishakhdapat/customer-segmentation-clustering)  
    - **License:** Apache License 2.0 — a permissive open-source license that allows usage, modification, and redistribution with attribution  
    - **Description:** This dataset contains behavioral data of active credit cardholders over the last 6 months, with ~8,000 customers and multiple features such as demographics, spending habits, purchase channels, and tenure.
    """)

    st.markdown("---")

    st.header("🛠️ Workflow Pipeline")
    st.markdown("""
    This project follows a structured pipeline:

    1. **Data Download & Preprocessing**  
    - Download dataset from Kaggle  
    - Convert date fields, handle missing values, create new features (Age, Tenure, Total Spent)

    2. **Outlier Removal**  
    - Apply IQR method to remove extreme values

    3. **Feature Scaling**  
    - Standardize numeric features using `StandardScaler`

    4. **Model Training & Tuning**  
    - Train K-Means clustering  
    - Evaluate with **Elbow Method** and **Silhouette Score**

    5. **Cluster Profiling & Insights**  
    - Generate summary stats for each cluster  
    - Provide business recommendations based on segment characteristics

    6. **Inference / Prediction**  
    - Predict cluster for new customer data using the saved model and scaler
    """)

    st.markdown("---")

    st.header("🧭 Navigation")
    st.markdown("""
    Use the sidebar to navigate through different pages:

    | Page            | Description                                                       |
    |-----------------|-------------------------------------------------------------------|
    | **Performance** | Elbow Method, Silhouette Score, and optimal cluster analysis     |
    | **Results**     | Cluster summary, and business insights      |
    | **Prediction**  | Predict a new customer's cluster using input features            |
    """)

    try:
        df = pd.read_csv("models/clustered_data.csv")
        
        st.subheader("📊 Processed Dataset Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(create_metric_card(f"{df.shape[0]} rows", "Total Data"), unsafe_allow_html=True)

        with col2:
            st.markdown(create_metric_card(f"{df.shape[1]} columns", "Total Features"), unsafe_allow_html=True)


    except FileNotFoundError:
        st.info("Processed dataset not found. Please run `main.py` first.")


