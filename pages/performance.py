import streamlit as st
import matplotlib.pyplot as plt
import joblib

def show():
    
    try:
        metrics = joblib.load("models/metrics.pkl")
        kmeans = joblib.load("models/kmeans_model.pkl")

        st.success("Model and metrics loaded successfully!")

        st.subheader("Elbow Method")
        fig1, ax1 = plt.subplots()
        ax1.plot(metrics["K"], metrics["inertia"], marker='o')
        ax1.set_title('Elbow Method - Optimal k')
        ax1.set_xlabel('Number of clusters')
        ax1.set_ylabel('Inertia')
        st.pyplot(fig1)

        st.subheader("Silhouette Score vs Number of Clusters")
        fig2, ax2 = plt.subplots()
        ax2.plot(metrics["K"], metrics["silhouette"], marker='o')
        ax2.set_title('Silhouette Score vs k')
        ax2.set_xlabel('Number of Clusters')
        ax2.set_ylabel('Silhouette Score')
        st.pyplot(fig2)

        best_k_index = metrics["silhouette"].index(max(metrics["silhouette"]))
        best_k = metrics["K"][best_k_index]
        st.success(f"Best k (based on Silhouette): **{best_k}** with score {max(metrics['silhouette']):.4f}")

    except FileNotFoundError:
        st.error("Please run `main.py` first to train the model and generate metrics.")
