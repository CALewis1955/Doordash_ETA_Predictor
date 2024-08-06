if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

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
   

def create_pipelines() -> Dict[str, Pipeline]:
    pipelines = {
        'linear_regression': make_pipeline(DictVectorizer(), LinearRegression()),
        'ridge': make_pipeline(DictVectorizer(), Ridge()),
        'decision_tree': make_pipeline(DictVectorizer(), DecisionTreeRegressor()),
        'random_forest': make_pipeline(DictVectorizer(), RandomForestRegressor())
    }
    return pipelines

def evaluate_model():
    pipeline.fit(train_dict, y_train)
    y_pred = pipeline.predict(val_dict)

    rmse = mean_squared_error(y_pred, y_val, squared=False)

# Example usage
pipelines = c
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
