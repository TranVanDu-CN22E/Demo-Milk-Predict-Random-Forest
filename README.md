# 🥛 Milk Quality Prediction using Random Forest

<div align="center">

Machine Learning Web Application for Milk Quality Classification

Built with **FastAPI • Random Forest • Svelte • Docker**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)
![Svelte](https://img.shields.io/badge/Svelte-5-FF3E00?logo=svelte)
![Vite](https://img.shields.io/badge/Vite-7-646CFF?logo=vite)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-RandomForest-F7931E?logo=scikitlearn)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-success)

</div>

---

## 📖 Overview

This project is a complete Machine Learning web application that predicts **milk quality** using a trained **Random Forest Classifier**.

The system allows users to enter the physicochemical characteristics of milk and instantly predicts its quality level through a modern web interface.

The project includes:

- 🧠 Random Forest Machine Learning model
- 🚀 FastAPI RESTful API
- 🧡 Svelte + Vite frontend
- 🐳 Docker deployment
- 📦 Joblib model serialization

---

## ✨ Features

- Predict milk quality in real time
- Random Forest classification model
- FastAPI REST API
- Interactive Swagger documentation
- Modern Svelte interface
- Docker support
- Responsive design
- Lightweight deployment

---

## 🧠 Machine Learning

### Algorithm

- Random Forest Classifier

### Input Features

| Feature | Description |
|----------|-------------|
| pH | Milk pH |
| Temprature | Milk Temperature |
| Taste | Taste |
| Odor | Odor |
| Fat | Fat Content |
| Turbidity | Turbidity |
| Colour | Milk Colour |

### Output Labels

| Label | Quality |
|------:|----------|
| 0 | Low |
| 1 | Medium |
| 2 | High |

---

## ⚙️ Technology Stack

### Backend

- Python 3.11
- FastAPI
- Scikit-learn
- Joblib
- Uvicorn

### Frontend

- Svelte 5
- Vite
- Axios

### Machine Learning

- Random Forest
- Pandas
- NumPy

### Deployment

- Docker
- Docker Compose

---

## 📁 Project Structure

```text
Demo-Milk-Predict-Random-Forest
│
├── backend/
│   ├── app.py
│   ├── milk_quality_model.pkl
│   ├── requirements.txt
│   ├── Dockerfile
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── ...
│
├── docker-compose.yml
│
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/TranVanDu-CN22E/Demo-Milk-Predict-Random-Forest.git

cd Demo-Milk-Predict-Random-Forest
```

---

## 💻 Run Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Open:

```
http://localhost:8000
```

Swagger API

```
http://localhost:8000/docs
```

---

## 💻 Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

## 🐳 Docker

Build the containers

```bash
docker compose build
```

Run

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

## 📡 REST API

### POST `/predict`

Request

```json
{
    "pH": 6.6,
    "Temprature": 35,
    "Taste": 1,
    "Odor": 0,
    "Fat": 1,
    "Turbidity": 0,
    "Colour": 254
}
```

Response

```json
{
    "prediction": 2,
    "grade": "High"
}
```

---

## 📊 Machine Learning Workflow

```text
Milk Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Train / Test Split
      │
      ▼
Random Forest Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Model (.pkl)
      │
      ▼
FastAPI REST API
      │
      ▼
Svelte Frontend
```

---

## 📈 Model Evaluation

The Random Forest model was evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score

The best model was selected based on the highest **Weighted F1-score** and exported using **Joblib** for deployment with FastAPI.

---

## 📷 Screenshots

### Home Page

> Add screenshot here

---

### Prediction Result

> Add screenshot here

---

### Swagger API

> Add screenshot here

---

### Docker Containers

> Add screenshot here

---

## 🔮 Future Improvements

- XGBoost implementation
- LightGBM implementation
- Prediction history
- User authentication
- Cloud deployment
- Model comparison dashboard
- Explainable AI (SHAP)

---

## 👨‍💻 Author

**Tran Van Du**

GitHub

https://github.com/TranVanDu-CN22E

---

## ⭐ Support

If this project helps you, please consider giving it a **⭐ Star** on GitHub.

Your support is greatly appreciated!

---

## 📄 License

This project is released under the **MIT License**.
