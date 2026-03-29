# 🚀 Day 3 ML Project — House Price Prediction API

## 📌 Overview

This project is part of my **AI Engineer journey (Day 3)** where I built a simple **Machine Learning model** and deployed it using **FastAPI**, along with a basic **HTML frontend** to take user input.

The goal was to understand:

* How ML models work (coef & intercept)
* How to connect ML with backend APIs
* How to take user input via frontend and return predictions

---

## 🧠 Tech Stack

* Python 🐍
* NumPy
* Pandas
* Scikit-learn
* FastAPI ⚡
* HTML (Frontend)

---

## 📊 Problem Statement

Predict **house prices** based on input features like:

* Area (sq ft)
* Number of bedrooms
* etc.

---

## ⚙️ How It Works

1. Train a **Linear Regression model**
2. Model learns:

   * **Coefficient (coef)** → impact of each feature
   * **Intercept** → base value
3. User inputs data via HTML form
4. FastAPI receives input
5. Model predicts price
6. Result is returned to user

---

## 🧮 ML Concept Used

### Linear Regression Formula:

Price = (coef₁ × feature₁) + (coef₂ × feature₂) + ... + intercept

* **coef** → shows how much a feature affects output
* **intercept** → base starting value when all features = 0

---

## 📂 Project Structure

```
project/
│
├── main.py              # FastAPI backend
├── model.py             # ML model training
├── templates/
│   └── index.html       # User input form
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run FastAPI server

```
uvicorn main:app --reload
```

### 3. Open in browser

```
http://127.0.0.1:8000
```

---

## 📸 Features

✅ Train ML model
✅ Understand coef & intercept
✅ Take user input via HTML
✅ FastAPI backend integration
✅ Real-time prediction

---

## 🚀 Learning Outcome

* Understood **how ML actually calculates predictions**
* Learned **how backend connects with ML**
* Built **end-to-end mini AI system**

---

## 🔥 Future Improvements

* Add more features for better prediction
* Use better dataset
* Deploy on cloud (Render / AWS)
* Add UI improvements

---

## 💡 Author

**Shaiban Shaikh**
Aspiring AI Engineer 🚀

---

## ⭐ Day 3 Status

✅ ML Model Built
✅ API Created
✅ Frontend Connected
💣 **DAY 3 COMPLETE 😤🔥**

<!-- uvicorn main:app --reload -->
