# 📊 Student Performance Analysis (Pandas Project)

## 🚀 Overview

This project analyzes student performance data using **Python (Pandas, NumPy, Matplotlib)**.
The goal is to extract meaningful insights such as toppers, low performers, subject difficulty, and the relationship between study habits and results.

---

## 📁 Dataset

The dataset contains the following columns:

* Name
* Math Marks
* Science Marks
* English Marks
* Study Hours
* Attendance

---

## ⚙️ Features & Analysis

### 📌 Data Exploration

* Viewed dataset using `head()`, `tail()`
* Checked structure using `info()`
* Statistical summary using `describe()`

---

### 🧹 Data Processing

* Removed non-numeric column (`name`) for correlation analysis
* Checked for missing values

---

### 📊 Insights Generated

* 🏆 **Topper Identification**
* 📉 **Lowest Scorer Detection**
* 📈 **Average Performance Calculation**
* 🎯 **High Performers (>80%)**
* ⚠️ **Low Performers (<60%)**
* 🕒 **Low Attendance Students**

---

### 📚 Subject Analysis

* Compared subject performance
* Identified toughest and easiest subjects based on performance trends

---

### 🔗 Correlation Analysis

* Found strong relationships between:

  * Study Hours & Marks
  * Attendance & Performance
* Conclusion:
  Students with higher study hours and attendance tend to score better.

---

### 📉 Visualization

* 📊 Bar Chart → Top Performers
* 📈 Line Plot → Study Hours vs Percentage

---

## 🧠 Key Learnings

* Data cleaning and preprocessing
* Using Pandas for analysis
* Applying correlation for insights
* Basic data visualization
* Writing logic without relying on AI

---

## 💻 Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install pandas numpy matplotlib
```

2. Run the script:

```bash
python your_script_name.py
```

---

## 📌 Future Improvements

* Replace loops with optimized Pandas operations
* Use average-based subject comparison
* Add more visualizations
* Use larger real-world dataset

---

## 👨‍💻 Author

Built with pure logic, documentation, and trial-error approach.
No AI used in core development.

---

## ⭐ Final Note

This project demonstrates strong fundamentals in data analysis and problem-solving, making it a solid beginner-to-intermediate level project.
