from flask import Flask, request, render_template
import pickle
import numpy as np

# ✅ Step 1: Initialize Flask App
app = Flask(__name__)

# ✅ Step 2: Load the ML Model
try:
    model = pickle.load(open("model.pkl", "rb"))
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None  # Prevents crashing if the model is missing

# ✅ Step 3: Define Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print(f"📥 Received Request Data: {request.form}")

        # Check if input fields are present
        if 'cgpa' not in request.form or 'iq' not in request.form:
            print("❌ Missing Input Fields!")
            return render_template('index.html', prediction="❌ Error: Missing input fields.")

        cgpa = request.form['cgpa']
        iq = request.form['iq']

        print(f"📥 Extracted Input: CGPA={cgpa}, IQ={iq}")

        # Convert inputs to float
        try:
            cgpa = float(cgpa)
            iq = float(iq)
        except ValueError:
            print("❌ Invalid Input Type: Expected Numbers")
            return render_template('index.html', prediction="❌ Error: Invalid input type.")

        if model is None:
            print("❌ Model Not Loaded")
            return render_template('index.html', prediction="❌ Error: Model not loaded.")

        # Prepare input and make prediction
        input_data = np.array([[cgpa, iq]])
        prediction = model.predict(input_data)[0]
        result = "✅ Placement Ho Jayega" if prediction == 1 else "❌ Placement Nahi Hoga"

        print(f"🔮 Model Prediction: {result}")
        return render_template('index.html', prediction=result)

    except Exception as e:
        print(f"❌ Error: {e}")
        return render_template('index.html', prediction=f"❌ Error: {str(e)}")

# ✅ Step 4: Run Flask App
if __name__ == '__main__':
    app.run(debug=True, port=8080)
