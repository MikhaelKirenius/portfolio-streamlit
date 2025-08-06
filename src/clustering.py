from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd


def train_kmeans(X_scaled, n_clusters=2, random_state=42):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(X_scaled)
    return kmeans, clusters

def evaluate_clustering(X_scaled, labels):
    return silhouette_score(X_scaled, labels)

def add_cluster_labels(df, clusters, mapping=None):
    df = df.copy()
    df['Cluster'] = clusters
    if mapping:
        df['Cluster_Label'] = df['Cluster'].map(mapping)
    return df

def cluster_summary(df, selected_features):
    return df.groupby('Cluster')[selected_features].mean()