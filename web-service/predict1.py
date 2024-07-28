
import pickle
import pandas as pd

from flask import Flask, request, jsonify

with open('new_lr_model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)
    

def predict(features):
    X = dv.transform(features)
    predictions = model.predict(X)
    return predictions[0]

app = Flask('doordash_eta')

# get the features from the request

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    features = request.get_json()
    prediction = predict(features)
    result = {
        'prediction': prediction
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

    