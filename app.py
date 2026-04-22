from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel, Field
import mlflow.pyfunc
import mlflow.sklearn
import pandas as pd
import logging
import json
from datetime import datetime
# -----------------------------
# Logging Setup
# -----------------------------
logging.basicConfig(
    filename="predictions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Input Schema (Validation)
# -----------------------------
class ChurnRequest(BaseModel):
    tenure: int = Field(..., ge=0, le=100)
    monthly_charges: float = Field(..., ge=0, le=1000)
    contract_length: int = Field(..., ge=1, le=60)

# -----------------------------
# App Init
# -----------------------------
app = FastAPI()

# 🔹 Replace <RUN_ID> with your actual MLflow run id

# model = mlflow.pyfunc.load_model("runs:/8590b345ca764d24bb7191c83aba4ee5/churn-model")
# model = mlflow.pyfunc.load_model("runs:/48ec53aba4aa4db7a75a970d53736068/churn-model")
# model = mlflow.sklearn.load_model("runs:/48ec53aba4aa4db7a75a970d53736068/churn-model")

# Load model from MLflow Registry
# model = mlflow.pyfunc.load_model("models:/churn-model/latest")

#for docker deployment, we will load the model from a local file instead of MLflow Registry
model = joblib.load("model.pkl")

# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def home():
     return {"message": "MLflow Model API Running"}

# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(request: ChurnRequest):
    #prob = model.predict_proba(data)[0][1]

    # return {
    # "prediction": int(prediction),
    # "probability": float(prob)
    #  }
    #return {"churn_prediction": int(prediction)}
     try:
        # Convert input to DataFrame
        data = pd.DataFrame([request.dict()])

        # Prediction
        prediction = model.predict(data)[0]

         # -----------------------------
        # Monitoring (JSON log)
        # -----------------------------
        log_data = {
            "timestamp": str(datetime.now()),
            "input": request.dict(),
            "prediction": int(prediction)
        }

        with open("monitoring_log.json", "a") as f:
            f.write(json.dumps(log_data) + "\n")

        # -----------------------------
        # Standard logging
        # -----------------------------
        logging.info(f"Input: {request.dict()} | Prediction: {prediction}")

        return {
            "churn_prediction": int(prediction)
        }

     except Exception as e:
        logging.error(f"Error: {str(e)} | Input: {request.dict()}")
        raise HTTPException(status_code=500, detail="Prediction failed")
     