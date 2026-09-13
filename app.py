
import streamlit as st
import pandas as pd
import joblib

# Load the trained Gradient Boosting pipeline
model = joblib.load("gradient_boosting_housing_model.pkl")

st.set_page_config(
    page_title="Sydney Housing Price Predictor",
    page_icon="🏡",
    layout="centered"
)

st.title(" 🏡 Sydney Housing Price Predictor")

st.write(
    "Enter the property details below to estimate its sale price "
    "using the Gradient Boosting model developed in this project."
)

suburb = st.selectbox(
    "Suburb",
    ["Blacktown", "Parramatta", "Randwick"]
)

property_type = st.selectbox(
    "Property Type",
    ["House", "Unit", "Townhouse", "Other"]
)

bedrooms = st.number_input(
    "Bedrooms", min_value=1, max_value=12, value=3, step=1
)

bathrooms = st.number_input(
    "Bathrooms", min_value=1, max_value=6, value=2, step=1
)

parking = st.number_input(
    "Parking Spaces", min_value=0, max_value=8, value=1, step=1
)

land_size = st.number_input(
    "Land Size (m²)", min_value=0.0, value=500.0, step=10.0
)

days_since_first_sale = st.number_input(
    "Days Since First Sale in Dataset",
    min_value=0,
    max_value=315,
    value=250,
    step=1
)

st.subheader("Property Description Features")

near_transport = st.checkbox("Near transport")
near_school = st.checkbox("Near school")
near_shops = st.checkbox("Near shops")
near_park = st.checkbox("Near park")
renovated = st.checkbox("Renovated")
development_potential = st.checkbox("Development potential")
granny_flat = st.checkbox("Granny flat")
premium_feature = st.checkbox("Premium feature")

if st.button("Predict Sale Price"):

    # Land size is used as individual land area only for houses
    house_land_size = land_size if property_type == "House" else 0

    total_rooms = bedrooms + bathrooms

    input_data = pd.DataFrame({
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Parking": [parking],
        "Days_Since_First_Sale": [days_since_first_sale],
        "House_Land_Size_m2": [house_land_size],
        "Total_Rooms": [total_rooms],
        "Near_Transport": [int(near_transport)],
        "Near_School": [int(near_school)],
        "Near_Shops": [int(near_shops)],
        "Near_Park": [int(near_park)],
        "Renovated": [int(renovated)],
        "Development_Potential": [int(development_potential)],
        "Granny_Flat": [int(granny_flat)],
        "Premium_Feature": [int(premium_feature)],
        "Suburb": [suburb],
        "Property_Type": [property_type]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Sale Price: ${prediction:,.0f}")

st.caption(
    "This prediction is an estimate based on the limited housing dataset "
    "used in this project and should not be treated as a professional property valuation."
)
