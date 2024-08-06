if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from hyperopt.pyll import scope
from sklearn.linear_model import Lasso, LinearRegression
import mlflow
import os
from utils.model_training.load_pipelines import load_pipelines
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVR






AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_DEFAULT_REGION =os.environ['AWS_DEFAULT_REGION']


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
    train_dict, val_dict, y_train, y_val = data
    y_val = y_val.to_dict(orient='records')
    
    now = datetime.now()
    
    mlflow.set_tracking_uri(uri="http://ec2-34-233-122-168.compute-1.amazonaws.com:5000")
    mlflow.end_run()
    mlflow.set_experiment(f'LinearSVR-{now}')

    def objective(params):
        with mlflow.start_run():
            mlflow.set_tag("model", "linearSVR")
            mlflow.log_params(params)
            pipeline = make_pipeline(DictVectorizer(), LinearSVR())
            pipeline.fit(train_dict, y_train)
            y_pred = pipeline.predict(y_val)
            y_true = [value for d in y_val for value in d.values()]
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            mlflow.log_metric("rmse", rmse)

        return {'loss': rmse, 'status': STATUS_OK}

    search_space = dict(
            epsilon=hp.uniform('epsilon', 0.0, 1.0),
            C=hp.loguniform(
                'C', -7, 3
            ),  # This would give you a range of values between e^-7 and e^3
            max_iter=scope.int(hp.quniform('max_iter', 1000, 5000, 100)),
        )

    best_result = fmin(
        fn=objective,
        space=search_space,
        algo=tpe.suggest,
        max_evals=50,
        trials=Trials()
    )   

    print(f'The best result is:  {best_result}')
    return best_result 
        


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
