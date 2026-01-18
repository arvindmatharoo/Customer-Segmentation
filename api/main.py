from fastapi import FastAPI
from api.schemas import CustomerInput,SegmentOutput
from api.utils import predict_segment
import pandas as pd

app = FastAPI()

@app.get("/")
def health_check():
    return {"Status" : "API is running"}

@app.post("/segment", response_model=SegmentOutput)
def segment_customer(customer: CustomerInput):
    cluster, segment = predict_segment(
        customer.recency,
        customer.frequency,
        customer.monetary
    )
    return {"cluster": cluster, "segment": segment}

@app.get("/clusters/summary")
def cluster_summary():
    df = pd.read_csv("../customer-segmentation/data/processed/customer_business_segments.csv")
    summary = df.groupby("CustomerSegment").agg({
        "CustomerID": "count",
        "Recency": "mean",
        "Frequency": "mean",
        "Monetary": "mean"
    }).reset_index()

    return summary.to_dict(orient="records")