# 🎓 Student Performance Prediction System (End-to-End ML Project)

> 🚀 A production-style Machine Learning project that predicts student performance and provides actionable insights through an interactive dashboard.

---

## 🌐 Live Demo

👉 https://student-performance-prediction-hx3dnbnqw5fgffnu3kfpku.streamlit.app/

---

## 📌 Project Overview

This project uses Machine Learning to predict a student’s exam performance based on behavioral and academic features such as:

* 📚 Study Hours
* 📊 Attendance
* 📝 Previous Marks
* 😴 Sleep Hours

It not only predicts scores but also provides **insights and recommendations** to improve performance.

---

## 🎯 Problem Statement

Educational institutions often struggle to:

* Identify weak students early
* Provide personalized guidance
* Prevent poor academic outcomes

This system solves that by delivering **data-driven predictions and insights**.

---

## 🧠 ML Approach

* Supervised Learning (Regression)
* Multiple models tested:

  * Linear Regression
  * Decision Tree
  * Random Forest ✅ (Best Model)
* Evaluation Metrics:

  * R² Score
  * Mean Absolute Error (MAE)

---

## 🏗️ Project Architecture

```
Student Data → Data Processing → Model Training → Prediction → Insights → Dashboard
```

---

## ⚙️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib
* **Model Storage:** Joblib
* **Frontend:** Streamlit
* **Version Control:** Git + GitHub

---

## 📊 Features

✅ Synthetic Data Generation (Realistic Simulation)
✅ Multiple Model Comparison
✅ Best Model Selection
✅ Model Saving & Loading
✅ Interactive Dashboard (Streamlit)
✅ Performance Insights & Recommendations
✅ Visual Analytics

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Student-Performance-Prediction.git
cd Student-Performance-Prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train Model

```bash
python src/train_model.py
```

### 4️⃣ Run App

```bash
python -m streamlit run app.py
```

---

## 📁 Project Structure

```
Student-Performance-Prediction/
│
├── src/
│   ├── data_processing.py
│   ├── train_model.py
│   ├── predict.py
│
├── models/
│   └── model.pkl
│
├── outputs/
├── images/
├── app.py
├── main.py
├── README.md
└── requirements.txt
```

---

## 📈 Sample Output

* Predicted Score: 78.5
* Performance: Excellent
* Insights:

  * Improve attendance
  * Maintain study consistency

---

## 💡 Key Learnings

* End-to-end ML pipeline development
* Model comparison & evaluation
* Feature importance analysis
* Building interactive ML apps
* Deploying ML projects

---

## 🚀 Future Improvements

* Real-world dataset integration
* Model optimization (Hyperparameter tuning)
* User authentication system
* API deployment (FastAPI)
* Mobile-friendly UI

---

## 👨‍💻 Author

**Dhananjay**
Aspiring Data Scientist | Machine Learning Enthusiast

---

## ⭐ Show Your Support

If you found this project useful:

👉 Star ⭐ the repo
👉 Share it on LinkedIn
👉 Fork it and improve

---

## 🔥 Project Status

✅ Completed
🚀 Actively improving

---

> 💬 *“Turning data into decisions using Machine Learning.”*
