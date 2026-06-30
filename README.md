# 🏠 House Price Prediction using Random Forest Regressor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Machine Learning web application that predicts the **estimated selling price of a house** using a **Random Forest Regressor** trained on the **Ames Housing Dataset**.

---

## 🌐 Live Demo

🔗 **Streamlit App:** *https://house-price-prediction-ames-housing-kenuylyeyvmdvtwzymzbg3.streamlit.app/*

## 📂 GitHub Repository

🔗 https://github.com/Subhu0110/House-Price-Prediction-Ames-Housing

---

# 📖 Project Overview

House prices are influenced by several factors such as lot size, overall quality, living area, garage capacity, basement area, and many more.

This project aims to estimate the selling price of a house based on **21 important numerical features** extracted from the Ames Housing Dataset.

The project follows a complete Machine Learning workflow, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Selection
- Model Training
- Model Evaluation
- Streamlit Web Application
- Deployment on Streamlit Cloud

---

# 📊 Dataset

**Dataset:** Ames Housing Dataset

The dataset contains detailed information about residential properties including:

- Lot Area
- Overall Quality
- Year Built
- Basement Area
- Living Area
- Garage Information
- Bathrooms
- Outdoor Features

Target Variable:

- **SalePrice**

---

# 🤖 Machine Learning Model

**Algorithm Used**

- Random Forest Regressor

The model was selected because it effectively captures non-linear relationships and provides strong performance on structured tabular data.

---

# 📈 Features Used

The model uses the following **21 numerical features**:

- Lot Frontage
- Lot Area
- Overall Qual
- Year Built
- Year Remod/Add
- Mas Vnr Area
- BsmtFin SF 1
- Total Bsmt SF
- 1st Flr SF
- 2nd Flr SF
- Gr Liv Area
- Bsmt Full Bath
- Full Bath
- Half Bath
- TotRms AbvGrd
- Fireplaces
- Garage Yr Blt
- Garage Cars
- Garage Area
- Wood Deck SF
- Open Porch SF

---

# 🚀 Features of the Application

- Predict house prices instantly
- Clean and user-friendly Streamlit interface
- Interactive input fields
- Fast prediction using a trained Random Forest model
- Responsive layout
- Easy to use

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git
- GitHub

---

# 📁 Project Structure

```text
House-Price-Prediction-Ames-Housing/
│
├── app.py
├── house_price_model.pkl
├── House_predictor.ipynb
├── README.md
├── requirements.txt
├── AmesHousing.csv
└── images/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Subhu0110/House-Price-Prediction-Ames-Housing.git
```

Move into the project directory

```bash
cd House-Price-Prediction-Ames-Housing
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 🔮 Future Improvements

- Hyperparameter tuning using RandomizedSearchCV/GridSearchCV
- Feature engineering
- Improved UI with custom CSS
- Support for categorical features
- Model comparison with XGBoost and Gradient Boosting
- Explainable AI using SHAP values

---

# 👨‍💻 Developer

**Subhansh Yadav**

B.Tech CSE (AI & ML)

Indian Institute of Information Technology (IIIT) Nagpur

GitHub:
https://github.com/Subhu0110

LinkedIn:
https://www.linkedin.com/in/subhansh-yadav-081116365/

---

## ⭐ If you found this project useful, consider giving it a star!
