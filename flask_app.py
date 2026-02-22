from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "Insurance Premium Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    age = data["age"]
    diabetes = data["diabetes"]
    bp = data["bp"]
    transplant = data["transplant"]
    chronic = data["chronic"]
    height = data["height"]
    weight = data["weight"]
    allergies = data["allergies"]
    cancer = data["cancer"]
    surgeries = data["surgeries"]

    bmi = weight / ((height / 100) ** 2)

    features = np.array([[age, diabetes, bp, transplant,
                          chronic, height, weight,
                          allergies, cancer, surgeries, bmi]])

    prediction = model.predict(features)

    return jsonify({"Predicted Premium": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)