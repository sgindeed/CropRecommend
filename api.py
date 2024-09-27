import numpy as np
import pickle
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('minmaxscaler.pkl', 'rb') as f:
    mx = pickle.load(f)


reverse_crop_dict = {
    1: 'rice', 2: 'maize', 3: 'chickpea', 4: 'kidneybeans', 5: 'pigeonpeas', 
    6: 'mothbeans', 7: 'mungbean', 8: 'blackgram', 9: 'lentil', 10: 'pomegranate', 
    11: 'banana', 12: 'mango', 13: 'grapes', 14: 'watermelon', 15: 'muskmelon', 
    16: 'apple', 17: 'orange', 18: 'papaya', 19: 'coconut', 20: 'cotton', 
    21: 'jute', 22: 'coffee'
}


class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float


@app.post('/recommend')
def recommend(crop_input: CropInput):
    
    features = np.array([[crop_input.N, crop_input.P, crop_input.K,
                          crop_input.temperature, crop_input.humidity,
                          crop_input.ph, crop_input.rainfall]])
    mx_features = mx.transform(features)

    
    label = model.predict(mx_features)[0]

    
    crop_name = reverse_crop_dict.get(label, "Unknown Crop")

   
    return {'recommended_crop': crop_name}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
