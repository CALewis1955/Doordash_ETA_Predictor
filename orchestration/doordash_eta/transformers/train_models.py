if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import os
import mlflow
from hyperopt import fmin, tpe, Trials, hp, STATUS_OK
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from hyperopt.pyll.base import scope
from datetime import datetime


# Get the current timestamp for the experiment name
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

mlflow.set_tracking_uri("http://ec2-34-233-122-168.compute-1.amazonaws.com:5000")
mlflow.end_run()

class ModelOptimizer:
    def __init__(self, model_name, model, search_space, train_data, val_data):
        self.model_name = model_name
        self.model = model
        self.search_space = search_space
        self.train_dict, self.y_train = train_data
        self.y_val_dict, self.y_val = val_data

    def objective(self, params):
        with mlflow.start_run():
            mlflow.set_tag("model", self.model_name)
            mlflow.log_params(params)
            pipeline = make_pipeline(DictVectorizer(), self.model(**params))
            pipeline.fit(self.train_dict, self.y_train)
            y_pred = pipeline.predict(self.y_val_dict)
            y_true = [value for d in self.y_val for value in d.values()]
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            mlflow.log_metric("rmse", rmse)
            mlflow.sklearn.log_model(pipeline, artifact_path="model")


        return {'loss': rmse, 'status': STATUS_OK}

    def optimize(self, max_evals=50):
        mlflow.set_experiment(f'{self.model_name}-{now}')
        best_result = fmin(
            fn=self.objective,
            space=self.search_space,
            algo=tpe.suggest,
            max_evals=max_evals,
            trials=Trials()
        )
        print(f'The best result for {self.model_name} is: {best_result}')
        return best_result


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
    train_data = (train_dict, y_train)
    val_data = (val_dict, y_val)

     # Random Forest configuration
    random_forest_search_space = {
        'n_estimators': scope.int(hp.quniform('n_estimators', 10, 100, 10)),
        'max_depth': scope.int(hp.quniform('max_depth', 3, 10, 1)),
        'min_samples_split': scope.int(hp.quniform('min_samples_split', 2, 10, 1)),
        'min_samples_leaf': scope.int(hp.quniform('min_samples_leaf', 1, 4, 1)),
    }

    random_forest_optimizer = ModelOptimizer('RandomForest', RandomForestRegressor, random_forest_search_space, train_data, val_data)
    #random_forest_best_result = random_forest_optimizer.optimize()

    # LinearSVR configuration
    linear_svr_search_space = {
        'epsilon': hp.uniform('epsilon', 0.0, 1.0),
        'C': hp.loguniform('C', -7, 3),
        'max_iter': scope.int(hp.quniform('max_iter', 1, 100, 1)),
    }

    linear_svr_optimizer = ModelOptimizer('LinearSVR', LinearSVR, linear_svr_search_space, train_data, val_data)
    linear_svr_best_result = linear_svr_optimizer.optimize()

    # Linear Regression configuration
    linear_reg_search_space = {
        'fit_intercept': hp.choice('fit_intercept', [True, False]),
    }

    linear_reg_optimizer = ModelOptimizer('LinearRegression', LinearRegression, linear_reg_search_space, train_data, val_data)
    linear_reg_best_result = linear_reg_optimizer.optimize()

   

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
