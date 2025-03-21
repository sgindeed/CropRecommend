from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with a specific origin (e.g., ["http://localhost:5173"]) to restrict access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('model.pkl', 'rb') as f:
    randclf = pickle.load(f)

with open('minmaxscaler.pkl', 'rb') as f:
    mx = pickle.load(f)

reverse_crop_dict = {
    1: 'rice', 2: 'maize', 3: 'chickpea', 4: 'kidneybeans', 5: 'pigeonpeas',
    6: 'mothbeans', 7: 'mungbean', 8: 'blackgram', 9: 'lentil', 10: 'pomegranate',
    11: 'banana', 12: 'mango', 13: 'grapes', 14: 'watermelon', 15: 'muskmelon',
    16: 'apple', 17: 'orange', 18: 'papaya', 19: 'coconut', 20: 'cotton',
    21: 'jute', 22: 'coffee'
}


class CropRecommendationInput(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Crop Recommendation API! Go to /docs for API documentation."}

@app.post("/recommend")
def recommend_crop(input: CropRecommendationInput):
    # Extract values from the input
    N = input.N
    P = input.P
    K = input.K
    temperature = input.temperature
    humidity = input.humidity
    ph = input.ph
    rainfall = input.rainfall
    
    
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    mx_features = mx.transform(features)
    
    
    label = randclf.predict(mx_features)[0]
    crop_name = reverse_crop_dict[label]
    
    return {"Recommended Crop": crop_name}