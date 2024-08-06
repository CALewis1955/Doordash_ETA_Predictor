import pandas as pd
from typing import Callable

def select_features(df: pd.DataFrame) -> pd.DataFrame:


    df['created_at'] = pd.to_datetime(df['created_at']).astype(int) / 10**9
    df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time']).astype(int) / 10**9
    df['actual_duration'] = (df['actual_delivery_time'] - df['created_at']) / 60

    
    return df


