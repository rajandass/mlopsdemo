# 🚀 End-to-End MLOps Project (Churn Prediction)

## 📌 Overview

This project demonstrates a **production-ready MLOps pipeline** — from model training to automated deployment on Azure using CI/CD.

It includes:

* Model training (Scikit-learn)
* Experiment tracking (MLflow - local)
* API serving (FastAPI)
* Monitoring & logging
* Docker containerization
* Cloud deployment (Azure Container Apps)
* CI/CD automation (GitHub Actions)

---

## 🏗️ Architecture

```
Data → Train → Model → API → Docker → Azure → CI/CD → Monitoring → Retraining
```

---

## 🧠 Problem Statement

Predict **customer churn** using:

* Tenure
* Monthly charges
* Contract length

---

## 🛠️ Tech Stack

| Layer      | Technology                     |
| ---------- | ------------------------------ |
| ML         | Scikit-learn                   |
| Tracking   | MLflow (local)                 |
| API        | FastAPI                        |
| Container  | Docker                         |
| Cloud      | Azure Container Apps           |
| Registry   | Azure Container Registry (ACR) |
| CI/CD      | GitHub Actions                 |
| Monitoring | JSON logs + Python script      |

---

## 📁 Project Structure

```
mlopsdemo/
│
├── app.py                  # FastAPI app
├── train.py               # Model training + MLflow logging
├── monitor.py             # Drift detection + auto-retraining
├── model.pkl              # Saved model (used in Docker)
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── .github/workflows/
    └── deploy.yml         # CI/CD pipeline
```

---

## ⚙️ Local Setup

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

1. Create Resource Group
2. Create Azure Container Registry (ACR)
3. Push Docker image
4. Deploy to Azure Container Apps

### Example:

```
az containerapp up --name churn-api-app \
--resource-group mlops-rg \
--image <ACR_NAME>.azurecr.io/churn-api:v1 \
--target-port 8000 \
--ingress external
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

### Location:

```
.github/workflows/deploy.yml
```

### Trigger:

* Runs automatically on every `git push` to `main`

### Pipeline Steps:

1. Build Docker image
2. Push image to Azure Container Registry
3. Deploy to Azure Container Apps

---

## 🔐 GitHub Secrets Required

| Secret            | Description            |
| ----------------- | ---------------------- |
| AZURE_CREDENTIALS | Service principal JSON |
| ACR_LOGIN_SERVER  | `<acr>.azurecr.io`     |
| ACR_USERNAME      | ACR name               |
| ACR_PASSWORD      | ACR password           |

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

If drift is detected:

* Model retrains automatically
* New model is generated

---

## 🧪 API Example

### Request

```json
{
  "tenure": 10,
  "monthly_charges": 75,
  "contract_length": 24
}
```

### Response

```json
{
  "churn_prediction": 1
}
```

---

## ⚠️ Important Notes

* Docker uses **model.pkl** (not MLflow registry) due to container isolation
* MLflow tracking is local (not production setup)
* `.gitignore` excludes logs, venv, and ML artifacts
* `.dockerignore` reduces build size

---

## 🔮 Future Improvements

* MLflow server on Azure (model registry)
* Azure Blob Storage for model artifacts
* Authentication (JWT / API key)
* Monitoring dashboard (Prometheus + Grafana)
* Blue-green deployment strategy
* Data pipeline integration

---

## 👨‍💻 Author

**Rajan Dass**

---

## ⭐ Key Highlights

* End-to-end MLOps lifecycle
* Cloud deployment on Azure
* Automated CI/CD pipeline
* Monitoring + retraining
* Production-ready architecture

---

## 📌 Conclusion

This project demonstrates how to move from:

```
ML Model → Production System → Automated Deployment
```

---

⭐ If you found this useful, consider starring the repo!
