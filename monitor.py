import pandas as pd
import json
import subprocess

# Load training data
train_df = pd.read_csv("data.csv")

# Load prediction logs
logs = []

try:
    with open("monitoring_log.json", "r") as f:
        for line in f:
            logs.append(json.loads(line))
except FileNotFoundError:
    print("No monitoring logs found.")
    exit()

if not logs:
    print("No logs yet.")
    exit()

# Convert to DataFrame
pred_df = pd.DataFrame([log["input"] for log in logs])

print("\n--- DATA DRIFT CHECK ---")

drift_detected = False

for col in pred_df.columns:
    train_mean = train_df[col].mean()
    pred_mean = pred_df[col].mean()

    drift = abs(train_mean - pred_mean)

    print(f"{col}: Train={train_mean:.2f}, Live={pred_mean:.2f}, Drift={drift:.2f}")

    # Threshold
    if drift > 15:
        print(f"⚠️ ALERT: High drift detected in {col}")
        drift_detected = True

# -----------------------------
# Trigger retraining
# -----------------------------
if drift_detected:
    print("\n🚀 Triggering retraining pipeline...\n")

    subprocess.run(["python", "train.py"])

    print("\n✅ Retraining completed. New model version registered.")

else:
    print("\n✅ No significant drift. No retraining needed.")