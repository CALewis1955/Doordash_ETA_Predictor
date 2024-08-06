if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from mage_ai.utils.data_preparation.target import add_target
from mage_ai.utils.data_preparation.clean import clean
from mage_ai.utils.data_preparation.prepare_dicts import prepare_dicts
from mage_ai.utils.data_preparation.select_features import select_features
from mage_ai.utils.data_preparation.splitter import split_into_train_and_val_sets
import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df = clean(data)
    df = select_features(df)
    train_df, val_df = split_into_train_and_val_sets(df)
    train_dict, val_dict = prepare_dicts(train_df, val_df)

    return df, train_df, val_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
