import numpy as np
import joblib

MODEL_PATH = "models/kmeans_model.pkl"
SCALER_PATH = "models/scaler.pkl"

def load_model_and_scaler():
    kmeans = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return kmeans, scaler

def predict_cluster(input_data):
    kmeans, scaler = load_model_and_scaler()

    if isinstance(input_data, dict):
        features = np.array([[input_data['Income'],
                               input_data['TotalChildren'],
                               input_data['Customer_Tenure'],
                               input_data['TotalSpent'],
                               input_data['NumWebVisitsMonth'],
                               input_data['Age']]])
    else:
        features = np.array([input_data])

    features_scaled = scaler.transform(features)

    cluster = kmeans.predict(features_scaled)[0]
    return cluster
