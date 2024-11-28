from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the pre-trained model
with open('crop-Recommnedation_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse form inputs

        ph = float(request.form['ph'])
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])

        # Create feature array
        features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

        # Make prediction
        prediction = model.predict(features)

        # Render template with prediction
        return render_template('index.html', prediction=prediction[0])
    except Exception as e:
        return str(e)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
