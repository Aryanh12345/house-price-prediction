import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

model = joblib.load(MODEL_PATH)

st.title("🏠 House Price Prediction")

st.write("Enter house details to predict the price.")


area = st.number_input(
    "Area",
    min_value=401,
    max_value=5996,
    value=1000,
    step=1
)

bedrooms = st.number_input(
    "Bedrooms", min_value=1, max_value=5, step=1
)

bathrooms = st.number_input(
    "Bathrooms", min_value=1, max_value=3, step=1
)

stories = st.number_input(
    "Stories", min_value=1, max_value=3, step=1
)

parking = st.number_input(
    "Parking", min_value=0, max_value=2, step=1
)

age = st.number_input(
    "Age",
    min_value=0,
    max_value=49,
    value=10,
    step=1
)

city = st.selectbox(
    "City",
    ["Pune", "Kolkata", "Chennai", "Delhi",
     "Mumbai", "Hyderabad", "Bangalore"]
)

furnishing = st.selectbox(
    "Furnishing",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

main_road = st.selectbox("Main Road", ["Yes", "No"])
guest_room = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])

water_supply = st.selectbox(
    "Water Supply",
    ["Both", "Corporation", "Borewell"]
)

air_conditioning = st.selectbox("Air Conditioning", ["Yes", "No"])

preferred_tenant = st.selectbox(
    "Preferred Tenant",
    ["Company", "Bachelor", "Family"]
)

locality_rating = st.number_input(
    "Locality Rating",
    min_value=1.0,
    max_value=10.0,
    value=5.0
)

if st.button("Calculate Price"):

    try:
        new_house = pd.DataFrame({
            "Area": [area],
            "Bedrooms": [bedrooms],
            "Bathrooms": [bathrooms],
            "Stories": [stories],
            "Parking": [parking],
            "Age": [age],
            "City": [city],
            "Furnishing": [furnishing],
            "Main Road": [main_road],
            "Guest Room": [guest_room],
            "Basement": [basement],
            "Water Supply": [water_supply],
            "Air Conditioning": [air_conditioning],
            "Preferred Tenant": [preferred_tenant],
            "Locality Rating": [locality_rating]
        })

        try:
            prediction = model.predict(new_house)
        except Exception as e:
            st.error(f"Prediction failed: {e}")

        st.success(
            f"Predicted House Price: ₹{prediction[0]:,.2f}"
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")