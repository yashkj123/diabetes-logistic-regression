from flask import Flask, render_template, request
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform([data])
    result = model.predict(final_input)[0]
    return render_template('index.html', prediction_text=f'Diabetes Prediction: {"Positive" if result == 1 else "Negative"}')

if __name__ == "__main__":
    app.run(debug=True)
