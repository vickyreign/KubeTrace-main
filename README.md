# KubeTrace: Cloud-Hosted Kubernetes Anomaly Detection Prototype

KubeTrace is a cloud-hosted anomaly detection prototype designed to demonstrate how machine learning can identify unusual activity in cloud-native environments.

The project uses a simulated Kubernetes runtime-event dataset and an Isolation Forest machine-learning model to classify events as normal or anomalous. The results are displayed through an interactive Streamlit dashboard.

## Project Status

This is a **cloud-hosted prototype**.

The current version demonstrates:

- Cloud-based dashboard deployment
- Machine-learning-based anomaly detection
- Simulated Kubernetes runtime events
- Real-time-style monitoring visualization
- Anomaly classification using Isolation Forest

Full Kubernetes runtime monitoring using Falco/eBPF is planned for a future phase.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Google Colab
- GitHub
- Streamlit Community Cloud

## Cloud Components

| Component | Platform |
|---|---|
| Model training | Google Colab |
| Source-code management | GitHub |
| Dashboard hosting | Streamlit Community Cloud |
| Kubernetes runtime monitoring | Planned |
| Falco/eBPF integration | Planned |

## System Workflow

```text
Simulated Runtime Events
          |
          v
Data Preprocessing
          |
          v
Isolation Forest ML Model
          |
          v
Anomaly Detection
          |
          v
Streamlit Cloud Dashboard
