#!/usr/bin/env python3


import pandas as pd
import requests

# import predict_mlflow

features = {
    "market_id": 1.0,
    "created_at": "2015-02-06 22:24:17",
    "actual_delivery_time": "2015-02-06 23:27:16",
    "store_id": 1845,
    "store_primary_category": "american",
    "order_protocol": 1.0,
    "total_items": 4,
    "subtotal": 3441,
    "num_distinct_items": 4,
    "min_item_price": 557,
    "max_item_price": 1239,
    "total_onshift_dashers": 33.0,
    "total_busy_dashers": 14.0,
    "total_outstanding_orders": 21.0,
    "estimated_order_place_duration": 446,
    "estimated_store_to_consumer_driving_duration": 861.0,
}

URL = "http://ec2-34-233-122-168.compute-1.amazonaws.com:9696/predict"

expected_response = {
    "model_version": "00626caf235b409ead10c3c344b913aa",
    "prediction": round(48.8391668520550, 2),
}
actual_response = requests.post(URL, json=features, timeout=10)

print(actual_response.json())
assert actual_response.json() == expected_response
print("Passed integration test")
