# Predicting House Prices using Machine Learning

## Project Overview
This project aims to predict house prices based on various features such as location, number of bedrooms, square footage, and other factors. The model is built using machine learning algorithms and deployed using Flask with a React-based frontend.

## Features
- **Machine Learning Model**: Trained using regression algorithms such as Linear Regression, Random Forest, and XGBoost.
- **Flask Backend**: Handles API requests for predictions.
- **React Frontend**: Provides an interactive UI for users to enter property details and get price predictions.
- **Database Integration**: Stores user data and prediction history (MongoDB/MySQL).
- **Jupyter Notebook Support**: Enables easy experimentation and visualization.

## Installation
### Prerequisites
- Python 3.8+
- Node.js & npm
- Git
- Anaconda (Optional for Jupyter Notebook)

### Clone the Repository
```sh
git clone https://github.com/abaidurerehman/Predicting_House_Price.git
cd Predicting_House_Price
```

### Setup Backend (Flask API)
```sh
cd backend
pip install -r requirements.txt
python app.py
```

### Setup Frontend (React)
```sh
cd frontend
npm install
npm start
```

## Usage
1. Open the frontend in your browser (`http://localhost:3000`).
2. Enter property details such as size, number of rooms, and location.
3. Click **Predict** to get an estimated house price.
4. The prediction results will be displayed in real time.

## API Endpoints
| Method | Endpoint      | Description                         |
|--------|-------------|-------------------------------------|
| POST   | `/predict`  | Takes house details and returns predicted price |

## Deployment
- Flask API can be deployed on **Heroku/AWS/GCP**.
- React frontend can be deployed on **Vercel/Netlify**.

## License
This project is open-source and available under the MIT License.

## Contributors
- ABAIDUR-E-REHMAN(Lead Developer)
-

## Contact
For issues or contributions, open a pull request or contact at meharmehar1065@gmail.com.

