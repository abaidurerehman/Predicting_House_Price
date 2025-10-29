from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "🏠 House Price Prediction API is running! Use the /predict endpoint with POST requests."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        input_data = np.array([[
            data['MedInc'], data['HouseAge'], data['AveRooms'], 
            data['AveBedrms'], data['Population'], data['AveOccup'], 
            data['Latitude'], data['Longitude']
        ]])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Make prediction
        predicted_price = model.predict(input_scaled)[0] * 100000  

        return jsonify({"price": f"${predicted_price:,.2f}"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000)
