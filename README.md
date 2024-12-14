# 🌾 Crop Recommendation System 🌱  

[![Deployed FastAPI](https://img.shields.io/badge/API%20Live-Render-brightgreen?logo=render)](https://croprecommend-w0h6.onrender.com)  
[![Streamlit App](https://img.shields.io/badge/Streamlit%20App-Live-orange?logo=streamlit)](https://crop-recommender-sssaa.streamlit.app/)  

---

## 🔍 Overview  

The **Crop Recommendation System** is a machine learning-based application that predicts the most suitable crop to grow based on environmental factors such as soil nutrients and weather conditions. It includes:  

- A **FastAPI** backend for providing crop recommendations via an API.  
- A **Streamlit** web app for an interactive user experience.  
- A Jupyter Notebook for the model workflow, including training and evaluation.  

---

## 🚀 Features  

- 🌾 **Crop Prediction**: Accurate recommendations for optimal crop selection.  
- 🧪 **Data-Driven**: Based on Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall values.  
- 🔗 **API Integration**: A RESTful API to access crop recommendations programmatically.  
- 🌐 **Interactive Web App**: User-friendly interface built with Streamlit for easy access to recommendations.  

---

## 📂 Project Structure  

```
CropRecommend/
├── api.py                    # FastAPI backend for recommendations
├── Crop_recommendation.ipynb # Jupyter notebook with model training workflow
├── requirements.txt          # Dependencies for the project
├── model.pkl                 # Pre-trained machine learning model
├── minmaxscaler.pkl          # Pre-fitted scaler for feature scaling
└── README.md                 # Project documentation
```  

---

## 🌐 Live Links  

- **FastAPI Endpoint**: [https://croprecommend-w0h6.onrender.com](https://croprecommend-w0h6.onrender.com)  
- **Streamlit App**: [https://crop-recommender-sssaa.streamlit.app/](https://crop-recommender-sssaa.streamlit.app/)  

---

## 📊 API Usage  

### **Endpoint**  

**POST** `/recommend`  
Accepts a JSON payload with the following fields:  

| **Field**       | **Type**  | **Description**                  |  
|------------------|-----------|----------------------------------|  
| `N`             | `int`     | Nitrogen level in soil           |  
| `P`             | `int`     | Phosphorus level in soil         |  
| `K`             | `int`     | Potassium level in soil          |  
| `temperature`   | `float`   | Ambient temperature in °C        |  
| `humidity`      | `float`   | Air humidity percentage          |  
| `ph`            | `float`   | Soil pH value                    |  
| `rainfall`      | `float`   | Rainfall in mm                   |  

---

### **Example Request**  

```bash  
curl -X POST "https://croprecommend-w0h6.onrender.com/recommend" \
-H "Content-Type: application/json" \
-d '{"N":59,"P":69,"K":80,"temperature":19.07,"humidity":17.86,"ph":8.165,"rainfall":69.406}'
```  

---

### **Example Response**  

```json  
{
  "Recommended Crop": "rice"
}
```  

---

## 🖥️ Streamlit App  

Interact with the **Crop Recommendation System** directly on the Streamlit platform:  
👉 [Streamlit App Live Link](https://crop-recommender-sssaa.streamlit.app/)  

1. Input environmental factors like Nitrogen, Phosphorus, pH, etc.  
2. Receive instant recommendations for the best crop to grow.  

---

## 🛠️ Getting Started  

### Prerequisites  

- Python 3.x  
- Libraries listed in `requirements.txt`  

---

### Installation  

1. **Clone the Repository** 📥:  
   ```bash  
   git clone https://github.com/sgindeed/CropRecommend.git  
   cd CropRecommend  
   ```  

2. **Install Dependencies** 📦:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the FastAPI Application** 🚀:  
   ```bash  
   uvicorn api:app --reload  
   ```  
   Access the API documentation at `http://127.0.0.1:8000/docs`.  

---

## 📒 Jupyter Notebook  

The training process for the machine learning model can be explored in the **Crop_recommendation.ipynb** file. This notebook includes:  

- Data loading and preprocessing  
- Model training and evaluation  
- Saving the model and scaler for deployment  

---

## 🛠️ Tech Stack  

- **Backend**: FastAPI  
- **Web App**: Streamlit  
- **Machine Learning**: Scikit-learn  
- **Deployment**: Render  

---

## 🤝 Contributions  

We welcome contributions from the community!  

1. Fork the repository 🍴.  
2. Create a branch (`feature/YourFeatureName`) 🌱.  
3. Commit your changes 💾.  
4. Push and create a pull request 🚀.  

---

## 📬 Contact  

For questions or feedback, reach out to [@sgindeed](https://github.com/sgindeed).  

Let’s grow smarter together! 🌱
