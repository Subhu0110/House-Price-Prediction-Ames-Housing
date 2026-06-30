# 🏠 House Price Prediction using Random Forest Regressor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Machine Learning web application that predicts the **estimated selling price of a house** using a **Random Forest Regressor** trained on the **Ames Housing Dataset**.

---

## 🌐 Live Demo

🚀 **Try the App:** https://house-price-prediction-ames-housing-kenuylyeyvmdvtwzymzbg3.streamlit.app/

## 📂 GitHub Repository

🔗 https://github.com/Subhu0110/House-Price-Prediction-Ames-Housing

---

# 📖 Project Overview

This project predicts the estimated selling price of residential properties using a **Random Forest Regressor** trained on the **Ames Housing Dataset**.

The workflow covers the complete machine learning pipeline—from data preprocessing and exploratory data analysis to model training, evaluation, deployment, and building an interactive web application with Streamlit.

---

# ✨ Key Features

- 🏠 Predict house prices instantly
- 🤖 Random Forest Regression model
- 📊 Interactive Streamlit interface
- 📈 Feature selection using correlation analysis
- 🧹 Data preprocessing and cleaning
- 🚀 Deployed on Streamlit Community Cloud
- 💻 End-to-end Machine Learning workflow

---

# 📊 Dataset

**Dataset:** Ames Housing Dataset

The dataset contains detailed information about residential properties, including:

- Lot Frontage
- Lot Area
- Overall Quality
- Year Built
- Basement Features
- Living Area
- Garage Information
- Bathrooms
- Outdoor Features

**Target Variable**

- SalePrice

---

# 🤖 Machine Learning Model

**Algorithm Used**

- Random Forest Regressor

Random Forest was chosen because it can effectively capture complex, non-linear relationships in structured tabular data while providing strong predictive performance.

---

# 📈 Features Used

The model uses **21 numerical features**:

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

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Subhu0110/House-Price-Prediction-Ames-Housing.git
```

Navigate to the project directory

```bash
cd House-Price-Prediction-Ames-Housing
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🔮 Future Improvements

- Hyperparameter tuning using RandomizedSearchCV
- Model comparison with XGBoost and Gradient Boosting
- Feature engineering
- Explainable AI using SHAP
- Enhanced UI with custom styling
- Support for categorical features

---

# 👨‍💻 Developer

**Subhansh Yadav**

B.Tech CSE (AI & ML)

Indian Institute of Information Technology (IIIT) Nagpur

GitHub:
https://github.com/Subhu0110

LinkedIn:
*(Add your LinkedIn profile URL here)*

---

## ⭐ If you like this project, consider giving it a star!
