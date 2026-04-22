# 🚀 End-to-End MLOps Project (Churn Prediction)

## 📌 Overview

This project demonstrates a **complete MLOps pipeline** — from model training to deployment on Azure with CI/CD.

It includes:

* ML model training (Scikit-learn)
* Experiment tracking (MLflow)
* API serving (FastAPI)
* Monitoring & logging
* Docker containerization
* Cloud deployment (Azure Container Apps)
* CI/CD pipeline (GitHub Actions)

---

## 🏗️ Architecture

```
Data → Train → Model → API → Docker → Azure → CI/CD → Monitoring
```

---

## 🧠 Problem Statement

Predict **customer churn** based on:

* Tenure
* Monthly charges
* Contract length

---

## 🛠️ Tech Stack

| Layer     | Technology           |
| --------- | -------------------- |
| ML        | Scikit-learn         |
| Tracking  | MLflow               |
| API       | FastAPI              |
| Container | Docker               |
| Cloud     | Azure Container Apps |
| CI/CD     | GitHub Actions       |
| Logging   | JSON + File logs     |

---

## 📁 Project Structure

```
mlopsdemo/
│
├── app.py                # FastAPI app
├── train.py             # Model training
├── monitor.py           # Drift detection + retraining
├── model.pkl            # Saved model
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── .github/workflows/
    └── deploy.yml       # CI/CD pipeline
```

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train Model

```
python train.py
```

### 4️⃣ Run API

```
uvicorn app:app --reload
```

### 5️⃣ Test API

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Setup

### Build Image

```
docker build -t churn-api .
```

### Run Container

```
docker run -p 8000:8000 churn-api
```

---

## ☁️ Azure Deployment

### Steps:

1. Create Azure Container Registry (ACR)
2. Push Docker image
3. Deploy using:

```
az containerapp up --name churn-api-app \
--resource-group mlops-rg \
--image <ACR_NAME>.azurecr.io/churn-api:v1 \
--target-port 8000 \
--ingress external
```

---

## 🔄 CI/CD Pipeline

Located in:

```
.github/workflows/deploy.yml
```

### Trigger:

* Runs on every `git push`

### Actions:

* Build Docker image
* Push to Azure Container Registry
* Deploy to Azure Container Apps

---

## 📊 Monitoring

### Features:

* Prediction logging (`monitoring_log.json`)
* Data drift detection (`monitor.py`)
* Auto-retraining trigger

### Run Monitoring:

```
python monitor.py
```

---

## 🔁 Auto-Retraining

If drift detected:

* Model retrains automatically
* New version deployed

---

## 🧪 API Example

### Request:

```json
{
  "tenure": 10,
  "monthly_charges": 75,
  "contract_length": 24
}
```

### Response:

```json
{
  "churn_prediction": 1
}
```

---

## 🔐 Production Improvements (Future)

* MLflow server on Azure
* Azure Blob for model storage
* Authentication (JWT/API key)
* Prometheus + Grafana dashboards
* Canary deployments

---

## 👨‍💻 Author

**Rajan Dass**

---

## ⭐ Key Highlights

* End-to-end MLOps lifecycle
* Cloud-native deployment
* Automated CI/CD
* Monitoring + retraining

---

## 📌 Conclusion

This project demonstrates how to move from:

```
ML Model → Production System
```

---

⭐ If you find this useful, give it a star!
