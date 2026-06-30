import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("house_price_model.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("🏠 House Price Predictor")

st.markdown("""
Predict the estimated selling price of a house using a **Random Forest Regressor**
trained on the **Ames Housing Dataset**.
""")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🏠 About This Project")

st.sidebar.success("Machine Learning Regression Project")

st.sidebar.markdown("""
### 📖 Overview
Predict the estimated selling price of a house using a **Random Forest Regressor** trained on the **Ames Housing Dataset**.

### ⚙️ Model Information
- **Algorithm:** Random Forest Regressor
- **Dataset:** Ames Housing Dataset
- **Input Features:** 21 Numerical Features
- **Prediction:** House Sale Price (USD)

### 🎓 Developer
**Subhansh Yadav**  
B.Tech CSE (AI & ML)  
IIIT Nagpur

---

💡 **Project Highlights**
- Data Cleaning & Preprocessing
- Feature Selection
- Exploratory Data Analysis (EDA)
- Regression Modeling
- Streamlit Deployment

---

🚀 *Built with Python, Scikit-learn & Streamlit*
""")

st.sidebar.markdown("---")
st.sidebar.markdown("[🌐 GitHub Profile](https://github.com/Subhu0110)")

# -----------------------------
# Input Section
# -----------------------------
st.header("🏡 Enter Property Details")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Basic Information")

    lot_frontage = st.number_input(
        "Lot Frontage (ft)",
        min_value=0.0,
        value=70.0
    )

    lot_area = st.number_input(
        "Lot Area (sq ft)",
        min_value=0.0,
        value=9500.0
    )

    overall_qual = st.slider(
        "Overall Quality",
        1,
        10,
        5
    )

    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2050,
        value=2000
    )

    year_remod = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2050,
        value=2005
    )

    mas_vnr_area = st.number_input(
        "Masonry Veneer Area",
        min_value=0.0,
        value=100.0
    )

    bsmt_fin_sf = st.number_input(
        "Finished Basement Area",
        min_value=0.0,
        value=500.0
    )

    total_bsmt_sf = st.number_input(
        "Total Basement Area",
        min_value=0.0,
        value=900.0
    )

    first_flr_sf = st.number_input(
        "1st Floor Area",
        min_value=0.0,
        value=1200.0
    )

    second_flr_sf = st.number_input(
        "2nd Floor Area",
        min_value=0.0,
        value=300.0
    )

    gr_liv_area = st.number_input(
        "Ground Living Area",
        min_value=0.0,
        value=1500.0
    )

with col2:

    st.subheader("House Amenities")

    bsmt_full_bath = st.number_input(
        "Basement Full Bath",
        min_value=0,
        max_value=5,
        value=1
    )

    full_bath = st.number_input(
        "Full Bathrooms",
        min_value=0,
        max_value=5,
        value=2
    )

    half_bath = st.number_input(
        "Half Bathrooms",
        min_value=0,
        max_value=5,
        value=1
    )

    total_rooms = st.number_input(
        "Total Rooms Above Ground",
        min_value=1,
        value=7
    )

    fireplaces = st.number_input(
        "Fireplaces",
        min_value=0,
        value=1
    )

    garage_year = st.number_input(
        "Garage Year Built",
        min_value=1800,
        max_value=2050,
        value=2000
    )

    garage_cars = st.number_input(
        "Garage Capacity",
        min_value=0,
        value=2
    )

    garage_area = st.number_input(
        "Garage Area",
        min_value=0.0,
        value=500.0
    )

    wood_deck = st.number_input(
        "Wood Deck Area",
        min_value=0.0,
        value=100.0
    )

    open_porch = st.number_input(
        "Open Porch Area",
        min_value=0.0,
        value=50.0
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict House Price", use_container_width=True):

    input_data = pd.DataFrame({
        'Lot Frontage': [lot_frontage],
        'Lot Area': [lot_area],
        'Overall Qual': [overall_qual],
        'Year Built': [year_built],
        'Year Remod/Add': [year_remod],
        'Mas Vnr Area': [mas_vnr_area],
        'BsmtFin SF 1': [bsmt_fin_sf],
        'Total Bsmt SF': [total_bsmt_sf],
        '1st Flr SF': [first_flr_sf],
        '2nd Flr SF': [second_flr_sf],
        'Gr Liv Area': [gr_liv_area],
        'Bsmt Full Bath': [bsmt_full_bath],
        'Full Bath': [full_bath],
        'Half Bath': [half_bath],
        'TotRms AbvGrd': [total_rooms],
        'Fireplaces': [fireplaces],
        'Garage Yr Blt': [garage_year],
        'Garage Cars': [garage_cars],
        'Garage Area': [garage_area],
        'Wood Deck SF': [wood_deck],
        'Open Porch SF': [open_porch]
    })

    prediction = model.predict(input_data)

    st.success("Prediction Generated Successfully!")

    st.metric(
        label="🏠 Estimated House Price",
        value=f"${prediction[0]:,.2f}"
    )

st.divider()

st.caption(
    "⚠️ This prediction is generated using a Machine Learning model trained on the Ames Housing Dataset. "
    "It should be considered an estimate and not an actual market valuation."
)