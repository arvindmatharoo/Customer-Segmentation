import joblib
import numpy as np
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCALER_PATH = os.path.join(BASE_DIR,"..","models","rfm_scaler.pkl")
MODEL_PATH = os.path.join(BASE_DIR,"..","models","kmeans_model.pkl")


scaler = joblib.load(SCALER_PATH)
kmeans = joblib.load(MODEL_PATH)

CLUSTER_LABELS = {
    0 : "Loyal High-Value",
    1 : "Churn Risk",
    2 : "Occasional Buyers" ,
    3 : "Potential Loyalists"
}

def predict_segment(recency,frequency,monetary):
    data = np.array([[recency,frequency,monetary]])
    scaled_data = scaler.transform(data)
    cluster = int(kmeans.predict(scaled_data)[0])
    segment = CLUSTER_LABELS.get(cluster, "Unknown")
    return cluster,segment

