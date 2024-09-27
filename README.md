

```markdown
# Crop Recommendation System

This repository contains a Crop Recommendation System that predicts the best crops to grow based on various environmental factors. It includes a machine learning model, an API for crop recommendations, and a Streamlit application for user interaction.

## Project Structure

- `api.py`: This file contains the FastAPI application that serves as the backend for crop recommendations. The API allows users to send POST requests with environmental factors (N, P, K, temperature, humidity, ph, and rainfall) and receive a recommended crop in response.

- `Crop_recommendation.ipynb`: This Jupyter notebook includes the workflow for training the machine learning model. It covers data loading, preprocessing, model training, and evaluation.

## API Usage

The API is available at: [https://croprecommend-w0h6.onrender.com](https://croprecommend-w0h6.onrender.com)

### Endpoint

- **POST** `/recommend`: This endpoint accepts a JSON body with the following fields:
  - `N`: Nitrogen value (int)
  - `P`: Phosphorus value (int)
  - `K`: Potassium value (int)
  - `temperature`: Temperature value (float)
  - `humidity`: Humidity value (float)
  - `ph`: pH value (float)
  - `rainfall`: Rainfall value (float)

### Example Request

```bash
curl -X POST "https://croprecommend-w0h6.onrender.com/recommend" -H "Content-Type: application/json" -d '{"N":59,"P":69,"K":80,"temperature":19.07,"humidity":17.86,"ph":8.165,"rainfall":69.406}'
```

### Example Response

```json
{
  "Recommended Crop": "rice"
}
```

## Streamlit App

Users can also interact with the crop recommendation system through the Streamlit application available at: [https://crop-recommender-sssaa.streamlit.app/](https://crop-recommender-sssaa.streamlit.app/)

## Getting Started

To run the Jupyter notebook and API locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/sgindeed/CropRecommend.git
   cd CropRecommend
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```bash
   uvicorn api:app --reload
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the API documentation.

## Acknowledgements

- Thank you for checking out this repository!
```

You can copy this content into a file named `README.md` in your GitHub repository. Let me know if you need any changes!