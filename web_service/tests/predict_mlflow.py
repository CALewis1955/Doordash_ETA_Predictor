#!/usr/bin/env python3

import os
import pickle
import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient
from sklearn.pipeline import make_pipeline

from flask import Flask, request, jsonify

MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
logged_model = f's3://mlflow-clewis916-remote/7/be10fb2d7fbd4f96abd145479796734b/artifacts/model/'

RUN_ID = 'be10fb2d7fbd4f96abd145479796734b'
#logged_model = f's3://mlflow-clewis916-remote/mlflow-artifacts/7/{RUN_ID}/artifacts/model/'
#logged_model = f'runs:/{RUN_ID}/model'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(logged_model)

    
# Define a function to predict the ETA 
def predict(features):
    predictions = model.predict(features)
    return predictions[0]

app = Flask('doordash_eta')

# get the features from the request

@app.route('/predict', methods=['POST'])
def predict_endpoint(run_id=RUN_ID):
    features = request.get_json()
    prediction = predict(features)
    result = {
        'prediction': prediction,
        'model_version': run_id
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

    