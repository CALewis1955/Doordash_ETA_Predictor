#!/usr/bin/env python3

# import pandas as pd
import mlflow
from flask import Flask, jsonify, request

EXPERIMENT_ID = 57
RUN_ID = "00626caf235b409ead10c3c344b913aa"
LOGGED_MODEL = f"s3://mlflow-clewis916-remote/{EXPERIMENT_ID}/{RUN_ID}/artifacts/model/"
model = mlflow.pyfunc.load_model(LOGGED_MODEL)


# Define a function to predict the ETA
def predict(features):
    predictions = model.predict(features)
    return round(predictions[0], 2)


app = Flask("doordash_eta")

# get the features from the request


@app.route("/predict", methods=["POST"])
def predict_endpoint(run_id=RUN_ID):
    features = request.get_json()
    prediction = predict(features)
    result = {"prediction": prediction, "model_version": run_id}
    print("This is the result:", jsonify(result))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
