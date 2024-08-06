from typing import Dict
import pandas as pd

def prepare_dicts(df_train, df_val):

    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)

    train_dict = df_train.to_dict(orient='records')
    val_dict = df_val.to_dict(orient='records')

    return train_dict, val_dict