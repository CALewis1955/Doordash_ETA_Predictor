from typing import Tuple, List, Dict
import pandas as pd
from sklearn.model_selection import train_test_split

def split_into_train_and_val_sets(df):

    numerical = ['max_item_price', 'min_item_price', 'subtotal', 'total_items', 'num_distinct_items', 'max_item_price', 'min_item_price', 'total_onshift_dashers', 'total_busy_dashers', 'total_outstanding_orders']

    categorical = ['market_id', 'store_id', 'store_primary_category', 'order_protocol']

    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    
    y_train = df_train.actual_duration.values
    y_val = df_val.actual_duration.values

    y_train = pd.DataFrame(y_train)
    y_val = pd.DataFrame(y_val)

    train_dict = df_train[categorical + numerical].to_dict(orient='records')
    val_dict = df_val[categorical + numerical].to_dict(orient='records')

    return train_dict, val_dict, y_train, y_val