# 🌾 Crop Recommendation System

This project predicts the most suitable crop to grow based on soil nutrients and weather conditions using a **Random Forest** machine learning model. The application is built with **Streamlit**, containerized with **Docker**, and deployed on **Azure Web Apps**.

## 📊 Dataset

The model is trained on a dataset with the following features:

| Feature       | Description                           |
|---------------|---------------------------------------|
| `N`           | Nitrogen content in soil              |
| `P`           | Phosphorus content in soil            |
| `K`           | Potassium content in soil             |
| `temperature` | Temperature in °C                     |
| `humidity`    | Relative Humidity in %                |
| `ph`          | Soil pH value                         |
| `rainfall`    | Rainfall in mm                        |
| `label`       | Recommended crop (Target variable)    |

## 🧠 Model

- The model used is **RandomForestClassifier** from `scikit-learn`.
- Data preprocessing includes:
  - Removing any null values.
  - Standardizing feature values using `StandardScaler`.
- Predictions are made from a dummy DataFrame for demonstration.

## 🚀 Deployment

- **Frontend**: Built with [Streamlit](https://streamlit.io/)
- **Backend**: Python (scikit-learn)
- **Containerization**: Docker
- **Cloud Deployment**: Microsoft Azure Web Apps

Access the deployed app here 👉 [https://crop-predictor-app.azurewebsites.net](https://crop-predictor-app.azurewebsites.net)

