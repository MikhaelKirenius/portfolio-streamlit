import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show(): 
    st.title("📊 Clustering Results & Insights")

    try:
        df = pd.read_csv("models/clustered_data.csv")
        summary = pd.read_csv("models/cluster_summary.csv")

        st.subheader("Cluster Profiles")
        st.write("### Cluster Profile Comparison")
        st.dataframe(summary)

        st.markdown("---")

        st.subheader("Segment Labels")
        st.write("Comparison of customer behavior between clusters.")

        fig, ax = plt.subplots()
        avg_spent = df.groupby('Cluster')['TotalSpent'].mean().reset_index()
        sns.barplot(x='Cluster', y='TotalSpent', data=avg_spent, palette='pastel', ax=ax)
        ax.set_title('Average Total Spent per Cluster')
        ax.set_xlabel('Cluster')
        ax.set_ylabel('Avg Total Spent')
        st.pyplot(fig)

        # Two-column description
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Cluster 0: Budget-Conscious Customers")
            st.write("- Lower income, moderate spending")
            st.write("- Price-sensitive and budget aware")
        with col2:
            st.markdown("### Cluster 1: High Spending Customers")
            st.write("- Higher income, higher spending")
            st.write("- More likely to purchase premium products")

        st.markdown("---")

        st.subheader("Business Insights")
        st.write("Recommended strategies for each segment:")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔖 Budget-Conscious Customers")
            st.write("- Offer discounts & loyalty programs")
            st.write("- Focus on affordable product bundles")
            st.write("- Use email marketing for promotions")
        with col2:
            st.markdown("#### 💎 High Spending Customers")
            st.write("- Provide exclusive deals & premium products")
            st.write("- Implement personalized recommendations")
            st.write("- Engage via premium subscription programs")

        st.markdown("---")

        st.subheader("Cluster Visualization")
        try:
            from sklearn.decomposition import PCA

            selected_features = ['Income', 'TotalChildren', 'Customer_Tenure',
                                'TotalSpent', 'NumWebVisitsMonth', 'Age']
            X = df[selected_features]
            pca = PCA(n_components=2)
            components = pca.fit_transform(X)

            df_plot = pd.DataFrame(components, columns=['PC1', 'PC2'])
            df_plot['Cluster'] = df['Cluster']

            fig2, ax2 = plt.subplots()
            sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=df_plot, palette='Set2', ax=ax2)
            ax2.set_title('PCA Visualization of Clusters')
            st.pyplot(fig2)
        except Exception as e:
            st.warning("PCA visualization skipped. Missing dependencies or invalid data.")

    except FileNotFoundError:
        st.error("Clustered data or summary not found. Please run `main.py` first.")


