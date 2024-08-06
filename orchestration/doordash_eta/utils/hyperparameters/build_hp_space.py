from typing import Callable, Dict, List, Tuple, Union

from hyperopt import hp, tpe
from hyperopt.pyll import scope
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso, LinearRegression
from xgboost import Booster
from sklearn.svm import LinearSVR

def build_hyperparameters_space(
    model_class: Callable[
        ...,
        Union[
            Lasso,
            LinearRegression,
            RandomForestRegressor,
            DecisionTreeRegressor
        ],
    ],
    random_state: int = 42,
    **kwargs,
) -> Tuple[Dict, Dict[str, List]]:
    params = {}
    choices = {}

    if Lasso is model_class:
        params = dict(
            alpha=hp.uniform(
                'alpha', 0.0001, 1.0
            ),  # Regularization strength; must be a positive float
            max_iter=scope.int(hp.quniform('max_iter', 1000, 5000, 100)),
        )

    if LinearRegression is model_class:
        choices['fit_intercept'] = [True, False]

    if RandomForestRegressor is model_class:
        params = dict(
            max_depth=scope.int(hp.quniform('max_depth', 5, 45, 5)),
            min_samples_leaf=scope.int(hp.quniform('min_samples_leaf', 1, 10, 1)),
            min_samples_split=scope.int(hp.quniform('min_samples_split', 2, 20, 1)),
            n_estimators=scope.int(hp.quniform('n_estimators', 10, 60, 10)),
            random_state=random_state,
        )

    if DecisionTreeRegressor is model_class:
        params = dict(
            max_depth=scope.int(hp.quniform('max_depth', 5, 45, 5)),
            min_samples_split=cope.int(hp.quniform('min_samples_split', 2, 20, 1)),
            min_samples_leaf=scope.int(hp.quniform('min_samples_leaf', 1, 10, 1)),
            random_state=random_state
        )
    if LinearSVR is model_class:
        params = dict(
            epsilon=hp.uniform('epsilon', 0.0, 1.0),
            C=hp.loguniform(
                'C', -7, 3
            ),  # This would give you a range of values between e^-7 and e^3
            max_iter=scope.int(hp.quniform('max_iter', 1000, 5000, 100)),
        )
    
    for key, value in choices.items():
        params[key] = hp.choice(key, value)

    if kwargs:
        for key, value in kwargs.items():
            if value is not None:
                kwargs[key] = value

    return params, choices