if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

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
    

    df = data
    # Loaded variable 'df' from URI: /home/ubuntu/mage/data/historical_data.csv

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
    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    
    assert output is not None, 'The output is undefined'

