import pandas as pd
import numpy as np
import joblib
import os
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from src.data_loader import load_data 
from src.preprocess import preprocess_data, remove_outliers_iqr, scale_features
from src.clustering import train_kmeans, add_cluster_labels, cluster_summary

DATA_PATH = "data/customer_segmentation.csv"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

print("Loading dataset...")
df = load_data(DATA_PATH)
print(f"Dataset shape: {df.shape}")

print("Preprocessing data...")
df_clean = preprocess_data(df)

selected_features = ['Age', 'Income', 'TotalChildren', 'Customer_Tenure',
                     'TotalSpent', 'NumWebPurchases', 'NumCatalogPurchases',
                     'NumStorePurchases', 'NumWebVisitsMonth']

new_selected_features = ['Income', 'TotalChildren', 'Customer_Tenure',
                          'TotalSpent', 'NumWebVisitsMonth', 'Age']

print("Removing outliers...")
df_iqr_clean = remove_outliers_iqr(df_clean, new_selected_features)

print("Scaling features...")
X_scaled, scaler = scale_features(df_iqr_clean, new_selected_features)

n_clusters = 2
print(f"Training KMeans with {n_clusters} clusters...")
kmeans, clusters = train_kmeans(X_scaled, n_clusters=n_clusters)

cluster_labels = {i: f"Cluster {i}" for i in range(n_clusters)}
df_clustered = add_cluster_labels(df_iqr_clean, clusters, cluster_labels)

silhouette = silhouette_score(X_scaled, clusters)
print(f"Silhouette Score for k={n_clusters}: {silhouette:.4f}")

print("Saving model and scaler...")
joblib.dump(kmeans, os.path.join(MODEL_DIR, "kmeans_model.pkl"))
joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.pkl"))
df_clustered.to_csv(os.path.join(MODEL_DIR, "clustered_data.csv"), index=False)
np.save(os.path.join(MODEL_DIR, "X_scaled.npy"), X_scaled)

print("Computing metrics for Elbow and Silhouette plots...")
metrics = {"K": list(range(2, 11)), "inertia": [], "silhouette": []}
for k in metrics["K"]:
    km = KMeans(n_clusters=k, random_state=42)
    labels = km.fit_predict(X_scaled)
    metrics["inertia"].append(km.inertia_)
    metrics["silhouette"].append(silhouette_score(X_scaled, labels))

joblib.dump(metrics, os.path.join(MODEL_DIR, "metrics.pkl"))

summary = cluster_summary(df_clustered, selected_features)
summary.to_csv(os.path.join(MODEL_DIR, "cluster_summary.csv"))

print("\n=== Training Completed ===")
print(f"Model, scaler, and metrics saved in '{MODEL_DIR}' directory.")
print(f"Silhouette Score: {silhouette:.4f}")
