# 🏠 House Price Prediction (Day 2 - 75 Hard AI Engineer)

## 🚀 Project Overview

This project is part of my **75 Hard AI Engineer Challenge (Day 2)**.

The goal was to understand the **core concept of Machine Learning** by building a simple **House Price Prediction model using Linear Regression** — without copying code and by relying on documentation.

---

## 🎯 Objective

* Generate a dataset with meaningful relationships
* Train a Machine Learning model
* Predict house prices based on features

---

## 📊 Dataset Details

The dataset contains the following features:

* `area` → Size of the house
* `bedrooms` → Number of bedrooms
* `bathrooms` → Number of bathrooms
* `price` → Target variable

### ⚠️ Important Learning

Initially, random data was used, which resulted in poor model performance.

Later, a **pattern-based dataset** was created:

```
price = (area * factor) + (bedrooms * weight) + (bathrooms * weight) + noise
```

This helped the model learn actual relationships.

---

## 🧠 Key Concepts Learned

* Machine Learning is **not magic** — it learns patterns from data
* Random data → ❌ No learning
* Structured data → ✅ Model learns effectively
* Linear Regression tries to fit a **best possible line**
* Noise is part of real-world data and improves robustness

---

## ⚙️ Workflow

1. Load dataset using pandas
2. Split features (X) and target (y)
3. Perform train-test split
4. Train model using Linear Regression
5. Evaluate model using score
6. Predict new values

---

## 📈 Results

* Achieved accuracy: **~0.98**
* Model successfully learned the relationship between features and price

---

## ⚠️ Challenges Faced

* Poor results with random data
* Understanding why model accuracy was low
* Figuring out that **data quality matters more than code**
* Handling feature format mismatch warning

---

## 💡 Key Takeaways

* Data is more important than the algorithm
* Always ensure meaningful relationships in dataset
* Keep input format consistent during training and prediction
* Debugging and trial-error is part of the process

---

## 🔥 What Makes This Special

* Built without copying code
* Used official documentation for learning
* Focused on understanding, not memorizing
* Learned from mistakes and improved approach

---

## 🚀 Next Step

Moving towards:

* Real-world datasets
* Data cleaning
* Exploratory Data Analysis (EDA)
* More advanced ML models

---

## 💣 Final Thought

> “I didn’t just train a model today…
> I understood how Machine Learning actually works.”

---

### 👨‍💻 Author

**Shaiban Shaikh**
(75 Hard AI Engineer Challenge)
