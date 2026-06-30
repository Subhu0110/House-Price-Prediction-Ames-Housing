# 🏠 House Price Prediction using Ames Housing Dataset

## 📌 Project Overview

This project aims to predict house prices using the Ames Housing Dataset by applying multiple Machine Learning regression algorithms and comparing their performance.

The project covers the complete Machine Learning workflow:

✔ Data Cleaning
✔ Missing Value Handling
✔ Feature Selection
✔ Model Building
✔ Hyperparameter Tuning
✔ Model Evaluation
✔ Model Comparison

---

## 🎯 Objective

Predict the **SalePrice** of houses based on various property features and identify the best-performing regression model.

---

## 📊 Dataset Information

**Dataset:** Ames Housing Dataset

**Target Variable:** `SalePrice`

The dataset contains information about:

* Property Size
* Overall Quality
* Year Built
* Garage Features
* Basement Features
* Lot Area
* Living Area
* And many other housing attributes

---

## ⚙️ Data Preprocessing

### 🔹 Missing Value Handling

* Numerical Features → Median Imputation
* Categorical Features → Mode Imputation

### 🔹 Feature Selection

Correlation analysis was performed to select features having meaningful relationships with the target variable.

### 🔹 Train-Test Split

* Training Data: 80%
* Testing Data: 20%

---

## 🤖 Models Implemented

### 1️⃣ Linear Regression

A baseline model used to understand the linear relationship between features and house prices.

**R² Score:** 0.80

---

### 2️⃣ Decision Tree Regressor

Captures non-linear relationships by recursively splitting the dataset.

**R² Score:** 0.8517

---

### 3️⃣ DT Best (RandomizedSearchCV)

Hyperparameter tuning was performed using RandomizedSearchCV.

**Best Parameters Found:**

* max_depth = 9
* min_samples_leaf = 9
* min_samples_split = 8
* criterion = squared_error

**R² Score:** 0.8242

---

### 4️⃣ Random Forest Regressor 🏆

An ensemble learning technique that combines multiple decision trees.

**R² Score:** 0.9073

---

## 📈 Model Performance Comparison

| Model                        | R² Score   |
| ---------------------------- | ---------- |
| Linear Regression            | 0.8000     |
| Decision Tree Regressor      | 0.8517     |
| DT Best (RandomizedSearchCV) | 0.8242     |
| Random Forest Regressor      | **0.9073** |

🏆 **Best Model: Random Forest Regressor**

---

## 📉 Evaluation Metrics Used

* R² Score
* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)

---

## 🧠 Key Learnings

### ✅ Data Leakage Matters

Initially, feature scaling was applied before train-test splitting, causing data leakage.

After fixing the issue, the model evaluation became more reliable.

### ✅ Tree-Based Models Do Not Need Scaling

Decision Trees and Random Forests performed effectively without feature scaling.

### ✅ Hyperparameter Tuning Is Not Guaranteed To Improve Results

Although RandomizedSearchCV found optimized parameters, the tuned model performed worse than the default Decision Tree on the test set.

### ✅ Ensemble Models Perform Better

Random Forest significantly outperformed both Linear Regression and a single Decision Tree.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* SciPy
* Jupyter Notebook

---

## 🚀 Future Improvements

* Gradient Boosting Regressor
* XGBoost Regressor
* Feature Engineering
* Cross Validation
* Model Deployment using Flask/Streamlit

---

## 👨‍💻 Author

**Subhansh Yadav**

Machine Learning Enthusiast | CSE (AI & ML)

---

## ⭐ Project Status

✅ Completed

Final Best Model: **Random Forest Regressor (R² = 90.73%)**
