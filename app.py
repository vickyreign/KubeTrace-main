import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest

st.title("KubeTrace")
st.subheader("Kubernetes Runtime Anomaly Detection")

data = pd.DataFrame({
    "process_count": [10, 12, 15, 11, 13, 100, 120],
    "shell_count": [0, 0, 1, 0, 0, 20, 25],
    "file_access": [20, 22, 25, 21, 23, 200, 250],
    "network_connections": [5, 6, 7, 5, 6, 80, 100]
})

features = [
    "process_count",
    "shell_count",
    "file_access",
    "network_connections"
]

model = IsolationForest(
    contamination=0.3,
    random_state=42
)

data["prediction"] = model.fit_predict(data[features])

data["status"] = data["prediction"].map({
    1: "Normal",
    -1: "Anomaly"
})

st.metric("Total Events", len(data))

st.metric(
    "Anomalies Detected",
    (data["status"] == "Anomaly").sum()
)

st.dataframe(data)

st.subheader("Security Alerts")

for _, row in data.iterrows():
    if row["status"] == "Anomaly":
        st.error(
            f"⚠️ Suspicious runtime activity detected | "
            f"Processes: {row['process_count']}"
        )
