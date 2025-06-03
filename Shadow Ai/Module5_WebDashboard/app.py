
# app.py

from flask import Flask, request, jsonify
import json
from av_classifier import AVClassifier

app = Flask(__name__)
clf = AVClassifier()
clf.load("av_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get("features")
    prediction = clf.predict(data)
    return jsonify({"prediction": int(prediction)})

@app.route("/")
def home():
    return "ShadowForgeAI Dashboard API"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
