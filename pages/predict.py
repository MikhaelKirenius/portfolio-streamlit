import streamlit as st
from src.inference import predict_cluster


def show():
    st.title("🔮 Customer Segmentation Prediction")

    st.markdown("""
    This page allows you to predict the cluster of a customer based on their attributes.
    Fill in the details below and click "Predict Cluster" to see which cluster the customer belongs to.
    """)

    st.markdown("Fill in the customer details below to predict their cluster.")

    income = st.number_input("Income", min_value=0, value=50000)
    total_children = st.number_input("Total Children", min_value=0, value=2)
    tenure = st.number_input("Customer Tenure (days)", min_value=0, value=1200)
    total_spent = st.number_input("Total Spent", min_value=0, value=2000)
    web_visits = st.number_input("Number of Web Visits per Month", min_value=0, value=8)
    age = st.number_input("Age", min_value=18, value=35)

    if st.button("Predict Cluster"):
        input_data = {
            "Income": income,
            "TotalChildren": total_children,
            "Customer_Tenure": tenure,
            "TotalSpent": total_spent,
            "NumWebVisitsMonth": web_visits,
            "Age": age
        }
        cluster = predict_cluster(input_data)

        cluster_name = ''
        if cluster == 0:
            cluster_name = "Budget-Conscious Customers"
        elif cluster == 1:
            cluster_name = "High Spending Customers"
        
        st.success(f"Predicted Cluster: **Cluster {cluster_name}**")
