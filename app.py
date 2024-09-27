import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the dataset
crop = pd.read_csv('Crop_recommendation.csv')

# Crop dictionary to map crop names to labels
crop_dict = {
    'rice': 1,
    'maize': 2,
    'chickpea': 3,
    'kidneybeans': 4,
    'pigeonpeas': 5,
    'mothbeans': 6,
    'mungbean': 7,
    'blackgram': 8,
    'lentil': 9,
    'pomegranate': 10,
    'banana': 11,
    'mango': 12,
    'grapes': 13,
    'watermelon': 14,
    'muskmelon': 15,
    'apple': 16,
    'orange': 17,
    'papaya': 18,
    'coconut': 19,
    'cotton': 20,
    'jute': 21,
    'coffee': 22
}

# Reverse dictionary to map labels back to crop names
reverse_crop_dict = {v: k for k, v in crop_dict.items()}

# Map crop names to labels
crop['label'] = crop['label'].map(crop_dict)

# Split the dataset into features and target
X = crop.drop('label', axis=1)
y = crop['label']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the features
mx = MinMaxScaler()
X_train = mx.fit_transform(X_train)
X_test = mx.transform(X_test)

# Train the GaussianNB model
randclf = GaussianNB()
randclf.fit(X_train, y_train)

# Streamlit app interface
st.title("Crop Recommendation System")

st.write("""
### Input the values to get the recommended crop:
""")

# Input fields for features
N = st.number_input("Nitrogen Content (N)", min_value=0, max_value=140, value=59)
P = st.number_input("Phosphorus Content (P)", min_value=0, max_value=145, value=69)
K = st.number_input("Potassium Content (K)", min_value=0, max_value=205, value=80)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=19.07)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=17.86)
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=8.165)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=69.406)

# Function for crop recommendation
def recommendation(N, P, K, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    mx_features = mx.transform(features)
    label = randclf.predict(mx_features)[0]
    crop_name = reverse_crop_dict[label]  # Get the crop name from the label
    return label, crop_name

# Predict button
if st.button("Recommend Crop"):
    label, crop_name = recommendation(N, P, K, temperature, humidity, ph, rainfall)
    st.success(f"Recommended Crop Label: {label}, Crop Name: {crop_name}")
