import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import joblib
import mlflow
import mlflow.sklearn

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv('data.csv')

# Convert target variable
# -----------------------------
# Clean and Convert Target
# -----------------------------
df['churn'] = df['churn'].astype(str).str.strip().str.capitalize()

df['churn'] = df['churn'].map({
    'Yes': 1,
    'No': 0
})

# Remove rows where mapping failed
df = df.dropna(subset=['churn'])

# Features and target
X = df.drop('churn', axis=1)
y = df['churn']

# -----------------------------
# 2. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# 3. Train Model
# -----------------------------
model = RandomForestClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 4. Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 5. Evaluation Metrics
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Cross Validation
cv_scores = cross_val_score(model, X, y, cv=5)
cv_accuracy = cv_scores.mean()

# -----------------------------
# 6. Save Model
# -----------------------------
joblib.dump(model, 'model.pkl')

# -----------------------------
# 7. MLflow Tracking
# -----------------------------
mlflow.set_experiment("churn-experiment")

with mlflow.start_run():

    # Log parameters
    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_param("max_depth", 3)

    # Log metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("cv_accuracy", cv_accuracy)

    # Log confusion matrix as artifact
    with open("confusion_matrix.txt", "w") as f:
        f.write(str(cm))
    mlflow.log_artifact("confusion_matrix.txt")

    # Log model
    mlflow.sklearn.log_model(
        sk_model=model,
        name="churn-model"
    )
    # Register model
    model_uri = f"runs:/{mlflow.active_run().info.run_id}/churn-model"

    result = mlflow.register_model(
        model_uri=model_uri,
        name="churn-model"
    )

    print(f"Model registered: {result.name}, version: {result.version}")

# -----------------------------
# 8. Print Output
# -----------------------------
print("\n✅ Model Training Completed\n")

print("Train size:", len(X_train))
print("Test size:", len(X_test))

print("\nTest Predictions:")
print("y_test:", y_test.values)
print("y_pred:", y_pred)

print("\nMetrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"Cross-validation Accuracy: {cv_accuracy:.2f}")

print("\nConfusion Matrix:")
print(cm)



