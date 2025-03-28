import streamlit as st
import requests

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction App")

st.write("Enter house details below to predict the price.")

# Form inputs
MedInc = st.number_input("Median Income (e.g., 3.5 - 15.0)", min_value=0.5, max_value=15.0, value=5.0)
HouseAge = st.number_input("House Age (years, e.g., 5 - 50)", min_value=1, max_value=100, value=20)
AveRooms = st.number_input("Average Rooms per house (e.g., 2 - 10)", min_value=1.0, max_value=15.0, value=5.0)
AveBedrms = st.number_input("Average Bedrooms per house (e.g., 1 - 5)", min_value=0.5, max_value=5.0, value=2.0)
Population = st.number_input("Population in area (e.g., 500 - 40000)", min_value=100, max_value=50000, value=3000)
AveOccup = st.number_input("Average Occupancy per house (e.g., 1 - 6)", min_value=0.5, max_value=10.0, value=3.0)
Latitude = st.number_input("Latitude (e.g., 32.5 - 42.0)", min_value=30.0, max_value=45.0, value=37.0)
Longitude = st.number_input("Longitude (e.g., -124.3 to -114.3)", min_value=-125.0, max_value=-110.0, value=-120.0)

# Button
if st.button("Predict House Price"):
    # Send request to backend
    url = "http://127.0.0.1:5000/predict"
    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        if "price" in result:
            st.success(f"🏡 Predicted House Price: {result['price']}")
        else:
            st.error("Error in prediction!")
    else:
        st.error("Failed to connect to the backend.")
