from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from typing import Dict

def load_pipelines() -> Dict[str, Pipeline]:
    pipelines = {
        'linear_regression': make_pipeline(DictVectorizer(), LinearRegression()),
        'ridge': make_pipeline(DictVectorizer(), Ridge()),
        'decision_tree': make_pipeline(DictVectorizer(), DecisionTreeRegressor()),
        'random_forest': make_pipeline(DictVectorizer(), RandomForestRegressor())
        
    }
    return pipelines