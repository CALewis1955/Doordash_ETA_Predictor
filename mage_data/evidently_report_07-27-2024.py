{
    "metrics": [
        {
            "metric": "ColumnDriftMetric",
            "result": {
                "column_name": "prediction",
                "column_type": "num",
                "stattest_name": "Wasserstein distance (normed)",
                "stattest_threshold": 0.1,
                "drift_score": 0.17656000205556535,
                "drift_detected": true,
                "current": {
                    "small_distribution": {
                        "x": [
                            13.663571107669902,
                            35.521176136896685,
                            57.378781166123474,
                            79.23638619535026,
                            101.09399122457705,
                            122.95159625380384,
                            144.8092012830306,
                            166.6668063122574,
                            188.52441134148418,
                            210.38201637071097,
                            232.23962139993776
                        ],
                        "y": [
                            0.000931950498194938,
                            0.03669838926400609,
                            0.007934845008611783,
                            0.00018237451400942225,
                            2.3902295414078933e-06,
                            4.780459082815793e-07,
                            0.0,
                            0.0,
                            0.0,
                            2.390229541407893e-07
                        ]
                    }
                },
                "reference": {
                    "small_distribution": {
                        "x": [
                            14.34722716548385,
                            36.22278477053972,
                            58.09834237559559,
                            79.97389998065145,
                            101.84945758570734,
                            123.7250151907632,
                            145.60057279581906,
                            167.47613040087495,
                            189.3516880059308,
                            211.22724561098667,
                            233.10280321604256
                        ],
                        "y": [
                            0.0017150152191214214,
                            0.03848383336075315,
                            0.00539748558030137,
                            0.00011511451547368392,
                            9.553071823542247e-07,
                            4.776535911771124e-07,
                            0.0,
                            0.0,
                            0.0,
                            2.3882679558855586e-07
                        ]
                    }
                }
            }
        },
        {
            "metric": "DatasetDriftMetric",
            "result": {
                "drift_share": 0.5,
                "number_of_columns": 13,
                "number_of_drifted_columns": 3,
                "share_of_drifted_columns": 0.23076923076923078,
                "dataset_drift": false
            }
        },
        {
            "metric": "DatasetMissingValuesMetric",
            "result": {
                "current": {
                    "different_missing_values": {
                        "": 0,
                        "-Infinity": 0,
                        "null": 0,
                        "Infinity": 0
                    },
                    "number_of_different_missing_values": 0,
                    "different_missing_values_by_column": {
                        "market_id": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "created_at": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "actual_delivery_time": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "store_id": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "store_primary_category": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "order_protocol": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_items": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "subtotal": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "num_distinct_items": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "min_item_price": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "max_item_price": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_onshift_dashers": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_busy_dashers": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_outstanding_orders": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "estimated_order_place_duration": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "estimated_store_to_consumer_driving_duration": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "actual_duration": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "prediction": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        }
                    },
                    "number_of_different_missing_values_by_column": {
                        "market_id": 0,
                        "created_at": 0,
                        "actual_delivery_time": 0,
                        "store_id": 0,
                        "store_primary_category": 0,
                        "order_protocol": 0,
                        "total_items": 0,
                        "subtotal": 0,
                        "num_distinct_items": 0,
                        "min_item_price": 0,
                        "max_item_price": 0,
                        "total_onshift_dashers": 0,
                        "total_busy_dashers": 0,
                        "total_outstanding_orders": 0,
                        "estimated_order_place_duration": 0,
                        "estimated_store_to_consumer_driving_duration": 0,
                        "actual_duration": 0,
                        "prediction": 0
                    },
                    "number_of_missing_values": 0,
                    "share_of_missing_values": 0.0,
                    "number_of_missing_values_by_column": {
                        "market_id": 0,
                        "created_at": 0,
                        "actual_delivery_time": 0,
                        "store_id": 0,
                        "store_primary_category": 0,
                        "order_protocol": 0,
                        "total_items": 0,
                        "subtotal": 0,
                        "num_distinct_items": 0,
                        "min_item_price": 0,
                        "max_item_price": 0,
                        "total_onshift_dashers": 0,
                        "total_busy_dashers": 0,
                        "total_outstanding_orders": 0,
                        "estimated_order_place_duration": 0,
                        "estimated_store_to_consumer_driving_duration": 0,
                        "actual_duration": 0,
                        "prediction": 0
                    },
                    "share_of_missing_values_by_column": {
                        "market_id": 0.0,
                        "created_at": 0.0,
                        "actual_delivery_time": 0.0,
                        "store_id": 0.0,
                        "store_primary_category": 0.0,
                        "order_protocol": 0.0,
                        "total_items": 0.0,
                        "subtotal": 0.0,
                        "num_distinct_items": 0.0,
                        "min_item_price": 0.0,
                        "max_item_price": 0.0,
                        "total_onshift_dashers": 0.0,
                        "total_busy_dashers": 0.0,
                        "total_outstanding_orders": 0.0,
                        "estimated_order_place_duration": 0.0,
                        "estimated_store_to_consumer_driving_duration": 0.0,
                        "actual_duration": 0.0,
                        "prediction": 0.0
                    },
                    "number_of_rows": 191407,
                    "number_of_rows_with_missing_values": 0,
                    "share_of_rows_with_missing_values": 0.0,
                    "number_of_columns": 18,
                    "columns_with_missing_values": [],
                    "number_of_columns_with_missing_values": 0,
                    "share_of_columns_with_missing_values": 0.0
                },
                "reference": {
                    "different_missing_values": {
                        "": 0,
                        "-Infinity": 0,
                        "null": 0,
                        "Infinity": 0
                    },
                    "number_of_different_missing_values": 0,
                    "different_missing_values_by_column": {
                        "market_id": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "created_at": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "actual_delivery_time": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "store_id": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "store_primary_category": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "order_protocol": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_items": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "subtotal": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "num_distinct_items": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "min_item_price": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "max_item_price": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_onshift_dashers": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_busy_dashers": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "total_outstanding_orders": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "estimated_order_place_duration": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "estimated_store_to_consumer_driving_duration": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "actual_duration": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        },
                        "prediction": {
                            "": 0,
                            "-Infinity": 0,
                            "null": 0,
                            "Infinity": 0
                        }
                    },
                    "number_of_different_missing_values_by_column": {
                        "market_id": 0,
                        "created_at": 0,
                        "actual_delivery_time": 0,
                        "store_id": 0,
                        "store_primary_category": 0,
                        "order_protocol": 0,
                        "total_items": 0,
                        "subtotal": 0,
                        "num_distinct_items": 0,
                        "min_item_price": 0,
                        "max_item_price": 0,
                        "total_onshift_dashers": 0,
                        "total_busy_dashers": 0,
                        "total_outstanding_orders": 0,
                        "estimated_order_place_duration": 0,
                        "estimated_store_to_consumer_driving_duration": 0,
                        "actual_duration": 0,
                        "prediction": 0
                    },
                    "number_of_missing_values": 0,
                    "share_of_missing_values": 0.0,
                    "number_of_missing_values_by_column": {
                        "market_id": 0,
                        "created_at": 0,
                        "actual_delivery_time": 0,
                        "store_id": 0,
                        "store_primary_category": 0,
                        "order_protocol": 0,
                        "total_items": 0,
                        "subtotal": 0,
                        "num_distinct_items": 0,
                        "min_item_price": 0,
                        "max_item_price": 0,
                        "total_onshift_dashers": 0,
                        "total_busy_dashers": 0,
                        "total_outstanding_orders": 0,
                        "estimated_order_place_duration": 0,
                        "estimated_store_to_consumer_driving_duration": 0,
                        "actual_duration": 0,
                        "prediction": 0
                    },
                    "share_of_missing_values_by_column": {
                        "market_id": 0.0,
                        "created_at": 0.0,
                        "actual_delivery_time": 0.0,
                        "store_id": 0.0,
                        "store_primary_category": 0.0,
                        "order_protocol": 0.0,
                        "total_items": 0.0,
                        "subtotal": 0.0,
                        "num_distinct_items": 0.0,
                        "min_item_price": 0.0,
                        "max_item_price": 0.0,
                        "total_onshift_dashers": 0.0,
                        "total_busy_dashers": 0.0,
                        "total_outstanding_orders": 0.0,
                        "estimated_order_place_duration": 0.0,
                        "estimated_store_to_consumer_driving_duration": 0.0,
                        "actual_duration": 0.0,
                        "prediction": 0.0
                    },
                    "number_of_rows": 191407,
                    "number_of_rows_with_missing_values": 0,
                    "share_of_rows_with_missing_values": 0.0,
                    "number_of_columns": 18,
                    "columns_with_missing_values": [],
                    "number_of_columns_with_missing_values": 0,
                    "share_of_columns_with_missing_values": 0.0
                }
            }
        }
    ]
}