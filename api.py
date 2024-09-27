from fastapi import FastAPI
import numpy as np
import pickle

app = FastAPI()

# Load the pre-trained model and the scaler
with open("model.pkl", "rb") as f:
    randclf = pickle.load(f)

with open("minmaxscaler.pkl", "rb") as f:
    mx = pickle.load(f)

# Crop label to name mapping
reverse_crop_dict = {
    1: 'rice',
    2: 'maize',
    3: 'chickpea',
    4: 'kidneybeans',
    5: 'pigeonpeas',
    6: 'mothbeans',
    7: 'mungbean',
    8: 'blackgram',
    9: 'lentil',
    10: 'pomegranate',
    11: 'banana',
    12: 'mango',
    13: 'grapes',
    14: 'watermelon',
    15: 'muskmelon',
    16: 'apple',
    17: 'orange',
    18: 'papaya',
    19: 'coconut',
    20: 'cotton',
    21: 'jute',
    22: 'coffee'
}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Crop Recommendation API! Go to /docs for API documentation."}

# Crop recommendation endpoint (POST request)
@app.post("/recommend")
def recommend(N: int, P: int, K: int, temperature: float, humidity: float, ph: float, rainfall: float):
    # Input features as a numpy array
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    
    # Scale the input features
    mx_features = mx.transform(features)
    
    # Predict the crop label
    label = randclf.predict(mx_features)[0]
    
    # Convert the label to the crop name
    crop_name = reverse_crop_dict[label]
    
    return {"Recommended Crop": crop_name}

