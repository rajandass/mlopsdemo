# 🚀 End-to-End MLOps Project (Churn Prediction)

## 📌 Overview

This project demonstrates a **production-ready MLOps pipeline** — from model training to controlled deployment on Azure using CI/CD with **manual approval gates**.

It includes:

* ML model training (Scikit-learn)
* Experiment tracking (MLflow - local)
* API serving (FastAPI)
* Monitoring & logging
* Docker containerization
* Cloud deployment (Azure Container Apps)
* CI/CD pipeline with **approval workflow (GitHub Actions)**

---

## 🏗️ Architecture

```
Data → Train → Model → API → Docker → CI/CD → Azure → Monitoring → Retraining
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
    └── deploy.yml         # CI/CD pipeline with approval
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

## 🔄 CI/CD Pipeline (Controlled Deployment)

### 📍 Location

```
.github/workflows/deploy.yml
```

### 🔁 Trigger

* Runs on every `git push` to `main`

### ⚙️ Pipeline Flow

1. **Build Stage (Auto)**

   * Build Docker image
   * Push image to Azure Container Registry

2. **Deploy Stage (Manual Approval Required)**

   * Waits for approval via GitHub Environment
   * Deploys to Azure Container Apps

---

## 🔐 Deployment Approval (IMPORTANT)

This project uses **GitHub Environments** to control deployments.

### Setup:

```
GitHub → Settings → Environments → production
```

### Features:

* Requires **manual approval before deployment**
* Prevents accidental production updates
* Enables safe release control

### Approval Flow:

```
Git Push → Build → ⏸️ Waiting for Approval → Approve → Deploy
```

---

## 🔑 GitHub Secrets Required

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
* Updated model is generated

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
* Deployment requires manual approval
* `.gitignore` and `.dockerignore` optimize builds

---

## 🔮 Future Improvements

* MLflow server on Azure (central model registry)
* Azure Blob Storage for model artifacts
* Authentication (JWT / API key)
* Monitoring dashboard (Prometheus + Grafana)
* Blue-green deployment strategy
* Multi-environment pipeline (dev/staging/prod)

---

## 👨‍💻 Author

**Rajan Dass**

---

## ⭐ Key Highlights

* End-to-end MLOps lifecycle
* Cloud deployment on Azure
* CI/CD with manual approval
* Monitoring + auto-retraining
* Production-ready architecture

---

## 📌 Conclusion

This project demonstrates how to move from:

```
ML Model → Controlled Deployment → Production System
```

---

⭐ If you found this useful, consider starring the repo!
