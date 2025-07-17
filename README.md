# 🧠 Personality Prediction

🚀 Streamlit UI + FastAPI API + RandomForest ML Model | ☁️ Deployed on AWS EC2
This project is a full-stack machine learning web application that predicts human personality traits based on behavioral inputs like time spent alone, social activity, stage fear, and more. It features a Streamlit UI for users, a FastAPI backend for serving predictions, and a RandomForestClassifier trained on curated personality data. The backend is deployed on an AWS EC2 instance for global access.

# 🌐 Deployed Version
You can access the app and API here:

🔗 Streamlit App: [http://personality_pred:8501](https://personalitypredictionfastapi-drwefeh7mgpnxyrdjudfsz.streamlit.app)

🔗 FastAPI Endpoint: http://<your-ec2-ip>:8000/predict

Make sure your EC2 instance has ports 8501 and 8000 open in the security group.

# 📌 Features
🎯 Predicts personality category (e.g., Introvert, Extrovert, Ambivert) based on input behavior.

🧠 ML model trained using RandomForestClassifier.

⚡ High-performance FastAPI backend for serving predictions.

🎨 Streamlit-based frontend for a simple and clean UI.

☁️ Hosted on AWS EC2 (Ubuntu) for 24x7 access.

📊 Includes Swagger docs and JSON API endpoint for developers.


# 🛠️ Technologies Used
## Backend
Framework: FastAPI

Data Validation: Pydantic

Model Serving: joblib, scikit-learn

API Docs: Swagger UI (auto-generated)

## Machine Learning
Algorithm: RandomForestClassifier

Library: Scikit-learn

Model Serialization: joblib

## Frontend
UI Framework: Streamlit

User Input Handling: Streamlit Widgets

## Deployment
Cloud Platform: AWS EC2 (Ubuntu)

App Server: Uvicorn

Access: Port 8000 (API), Port 8501 (Streamlit UI)

## Other Tools
Language: Python 3.10+

Data Processing: Pandas, NumPy

Version Control: Git & GitHub

