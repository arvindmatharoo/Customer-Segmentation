# Customer Behavior Intelligence & Segmentation Platform

## 📌 Overview

This project builds an **end-to-end customer segmentation system** using transactional retail data.
By applying **RFM (Recency, Frequency, Monetary) analysis** and **unsupervised machine learning (KMeans clustering)**, customers are grouped into meaningful behavioral segments that can be used for business decision-making.

The solution goes beyond model training and includes:

* Business interpretation of clusters
* Visual insights
* A **FastAPI-based inference service**
* **Dockerized deployment** for portability and reproducibility

---

## 🎯 Problem Statement

Organizations often collect large volumes of transactional data but struggle to convert it into actionable insights such as:

* Identifying high-value customers
* Detecting customers at risk of churn
* Understanding purchasing behavior patterns
* Designing targeted marketing and retention strategies

This project addresses these challenges by:

* Analyzing customer purchase history
* Segmenting customers based on behavior
* Translating machine learning outputs into business-friendly insights
* Providing real-time predictions through an API

---

## 📂 Dataset

* **Source:** Online Retail transactional dataset [Dataset Link] (https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset)
* **Granularity:** Individual purchase transactions
* **Key fields used:**

  * Invoice date
  * Customer ID
  * Quantity
  * Unit price

After data cleaning and preprocessing, the dataset was aggregated at the **customer level** for behavioral analysis.

---

## 🧠 RFM Metrics Explained

| Metric        | Description                             | Interpretation   |
| ------------- | --------------------------------------- | ---------------- |
| **Recency**   | Days since the customer's last purchase | Lower is better  |
| **Frequency** | Number of unique purchase transactions  | Higher is better |
| **Monetary**  | Total amount spent by the customer      | Higher is better |

### Why RFM?

RFM analysis captures **customer engagement, loyalty, and value** using real purchase behavior, making it a widely used and interpretable approach in business analytics.

---

## ⚙️ Methodology

### 1️⃣ Data Understanding & Cleaning

* Removed missing customer IDs
* Filtered invalid transactions
* Created a clean transactional dataset

### 2️⃣ Feature Engineering

* Aggregated transactional data into RFM features
* One row per customer

### 3️⃣ Customer Segmentation

* Applied feature scaling (StandardScaler)
* Used the **Elbow Method** to select optimal clusters
* Performed KMeans clustering

### 4️⃣ Business Interpretation

Clusters were translated into meaningful customer segments:

| Segment                 | Description                               |
| ----------------------- | ----------------------------------------- |
| **Loyal High-Value**    | Frequent, recent, high-spending customers |
| **Potential Loyalists** | Recent customers with growth potential    |
| **Occasional Buyers**   | Moderate engagement and spending          |
| **Churn Risk**          | Inactive customers with low engagement    |

---

## 📊 Visual Insights

The following visual analyses were performed:

* Customer distribution across segments
* Average Recency by segment
* Average Frequency by segment
* Average Monetary value by segment

These visuals help stakeholders quickly understand behavioral differences between customer groups.

---

## 🔌 API Overview (FastAPI)

The project exposes customer segmentation through a REST API.

### Available Endpoints

#### `GET /health`

Health check for the API.

#### `POST /segment`

Predicts customer segment based on RFM values.

**Input**

```json
{
  "recency": 30,
  "frequency": 4,
  "monetary": 2500
}
```

**Output**

```json
{
  "cluster": 3,
  "segment": "Potential Loyalists"
}
```

#### `GET /clusters/summary`

Returns aggregated statistics for each customer segment.

---

## 🧪 Testing Parameters

| Scenario           | Recency | Frequency | Monetary |
| ------------------ | ------- | --------- | -------- |
| Loyal High-Value   | 5       | 15        | 25000    |
| Potential Loyalist | 15      | 2         | 800      |
| Occasional Buyer   | 60      | 3         | 3000     |
| Churn Risk         | 250     | 1         | 400      |

---

## 🐳 Docker Deployment

### Build the Docker image

```bash
docker build -t customer-segmentation-api .
```

### Run the container

```bash
docker run -p 8000:8000 customer-segmentation-api
```

### Access API Docs

```text
http://localhost:8000/docs
```

> **Note (Windows + WSL2):**
> If `localhost` does not work, find the WSL IP using:
>
> ```bash
> wsl hostname -I
> ```
>
> and access:
>
> ```text
> http://<WSL-IP>:8000/docs
> ```

---

## 📁 Project Structure

```
customer-segmentation/
├── api/
│   ├── main.py
│   ├── schemas.py
│   ├── utils.py
│   └── __init__.py
├── data/
│   └── processed/
├── models/
│   ├── rfm_scaler.pkl
│   └── kmeans_model.pkl
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_clustering.ipynb
│   └── 04_business_insights.ipynb
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Future Improvements

* Add a lightweight web interface (Gradio / React)
* Deploy the Docker image to cloud platforms
* Add authentication to API endpoints
* Incorporate customer lifetime value (CLV) modeling

---

## 🧾 Key Takeaways

* Demonstrates **end-to-end data science workflow**
* Converts ML output into **business intelligence**
* Shows **real deployment and Docker experience**
* Designed with **interpretability and usability** in mind


## To Contact
- **Arvind Singh**
- [Linkedin](https://www.linkedin.com/in/arvindmatharoo/)
- Gmail: iarvinddsingh@gmail.com
