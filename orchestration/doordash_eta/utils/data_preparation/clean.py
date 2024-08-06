import pandas as pd
from typing import Callable

def clean(
    df: pd.DataFrame,
    include_extreme_durations: bool = False,
) -> pd.DataFrame:

    # Drop rows with missing data if count of missing rows is less than 3% of all rows
    # in columns: 'market_id', 'actual_delivery_time' and 3 other columns
    columns_with_insubstantial_missing_data = [col for col in df.columns if df[col].isnull().sum() < 0.03 * len(df)]
    # market_id', 'actual_delivery_time', 'store_primary_category', 'order_protocol', 'estimated_store_to_consumer_driving_duration'
    df.dropna(subset=columns_with_insubstantial_missing_data, inplace=True)

    # if more than 3%, replace missing values with mean
    columns_with_substantial_missing_data = [col for col in df.columns if df[col].isnull().sum() >= 0.03 * len(df)] 
    for column in columns_with_substantial_missing_data:
        df = df.fillna({column: df[column].mean()})

    
    return df
    

