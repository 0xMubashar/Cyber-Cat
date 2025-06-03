
# retraining_loop.py

import numpy as np
from av_classifier import AVClassifier
import joblib
import os

def generate_samples(n):
    return np.random.rand(n, 5), np.random.randint(0, 2, size=n)

def retrain():
    model_path = "av_model.pkl"

    # Load or initialize
    clf = AVClassifier()
    if os.path.exists(model_path):
        clf.load(model_path)
        print("Loaded existing model.")
    else:
        print("No existing model found. Creating new one.")

    # Simulate new data and retrain
    X_new, y_new = generate_samples(20)
    clf.train(X_new, y_new)
    clf.save(model_path)
    print("Model retrained and saved.")

if __name__ == "__main__":
    retrain()
