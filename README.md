# Crop Recommendation System (Random Forest + Flask)

A machine learning–powered crop recommendation tool that suggests the best crop to grow based on soil nutrients and local climate conditions. Built to support data-driven, sustainable agriculture, especially for beginner farmers and farmers in rural areas.

## Demo
- Live app: https://croprecommendation-fask-2.onrender.com/

## Screenshots
<img width="1914" height="905" alt="image" src="https://github.com/user-attachments/assets/83cea544-3dd8-4df7-ade5-ee6eed4ff2c2" />

## What it does
Users enter:
N (Nitrogen), P (Phosphorus), K (Potassium), Temperature, Humidity, pH, Rainfall

The system predicts the most suitable crop and returns a recommendation in real time via a Flask web interface.

## Why this matters (Sustainability)
Incorrect crop selection can reduce yields and waste limited resources such as water and fertilizers. This tool helps improve crop–environment matching, supporting food security and more efficient farming decisions.

## Model & Data
Model: Random Forest Classifier
Dataset: Crop Recommendation Dataset (Kaggle)
https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset

Features: N, P, K, temperature, humidity, pH, rainfall

Reported performance: ~99% test accuracy 

## Tech stack
Python, Scikit-learn
Flask
HTML/CSS (Frontend)
Render (Deployment)

## Project Structure
bash
Copy code
.
├── app.py
├── templates/
├── static/
├── model/
│   ├── crop_model.pkl
│   └── scaler.pkl   # if used
├── notebooks/
│   └── training_notebook.ipynb
├── requirements.txt
└── README.md


## Model training
The Random Forest model was trained inside the notebook located in: https://colab.research.google.com/drive/1baIbltFl7QiofLovLY7_23afSHgsObTf#scrollTo=In32vdLWnrFc&printMode=true
The trained model was exported using pickle/joblib and loaded in the Flask application for inference.


## Future improvements
Add real-time weather integration for location-based recommendations
Expand dataset and calibrate recommendations for specific regions
Add multilingual support (Arabic/French) for accessibility
Improve UI for mobile users

## Author
Ikram Bichbich
