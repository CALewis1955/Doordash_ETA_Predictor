if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

"""
from utils.data_preparation.add_target import add_target
from utils.data_preparation.clean import clean
from utils.data_preparation.prepare_dicts import prepare_dicts
from utils.data_preparation.select_features import select_features
from utils.data_preparation.splitter import split_into_train_and_val_sets
import pandas as pd
"""

import os


@transformer
def transform(data, *args, **kwargs):


    cwd = os.getcwd()
    print(cwd)

    """
    df = clean(data)
    df = add_target(df)
    train_dict, val_dict, y_train, y_val = split_into_train_and_val_sets(df)
    y_train = pd.DataFrame(y_train)
    y_val = pd.DataFrame(y_val)
    return train_dict, val_dict, y_train, y_val
    """

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output[2] is not None, 'The output is undefined'
