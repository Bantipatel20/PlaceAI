import os
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])
        
        # Prepare input array
        input_data = np.array([[cgpa, iq]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "✅ Placement Ho Jayega" if prediction == 1 else "❌ Placement Nahi Hoga"
        
        return render_template('index.html', prediction=result)
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Railway-assigned port
    app.run(host="0.0.0.0", port=port)
