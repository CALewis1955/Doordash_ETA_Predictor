import pandas as pd

def add_target(df: pd.DataFrame) -> pd.DataFrame:    
    # our target is actual duration
    # the created_at and actual_delivery_time are dates;  let's convert them
    df['created_at'] = pd.to_datetime(df['created_at']).astype(int) / (10**9 * 60)
    df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time']).astype(int) / (10**9 * 60)
    df['actual_duration'] = (df['actual_delivery_time'] - df['created_at'])
    return df