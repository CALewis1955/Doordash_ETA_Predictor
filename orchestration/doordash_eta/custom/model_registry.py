if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from mlflow.tracking import MlflowClient
from mlflow.entities import ViewType
import mlflow
from datetime import datetime

#@transformer
#def transform(data, *args, **kwargs):
@transformer
def get_best_run_by_rmse(data):
    # Initialize the MLflow client
    client = MlflowClient()

    # Variables to track the best run and its RMSE
    best_run_id = None
    best_experiment_id = None
    lowest_rmse = float('inf')

    # List all experiments
    experiments = client.search_experiments()

    # Loop through each experiment
    for experiment in experiments:
        experiment_id = experiment.experiment_id

        # List all runs in the experiment
        runs = client.search_runs(
            experiment_ids=[experiment_id],
            order_by=["metrics.rmse ASC"]
        )

        # Check if there are any runs
        if not runs:
            continue

        # Get the run with the lowest RMSE in this experiment
        best_run_in_experiment = runs[0]
        best_rmse_in_experiment = best_run_in_experiment.data.metrics["rmse"]

        # Update if this run has a lower RMSE than the current best
        if best_rmse_in_experiment < lowest_rmse:
            best_run_id = best_run_in_experiment.info.run_id
            best_experiment_id = experiment_id
            lowest_rmse = best_rmse_in_experiment

    # Return the best run's information
    return best_run_id, best_experiment_id, lowest_rmse

def register_best_model(best_run_id, model_name):
    # Register the model from the best run
    model_uri = f"runs:/{best_run_id}/model"
    registered_model = mlflow.register_model(model_uri, model_name)

    print(f"Model registered with name: {registered_model.name} and version: {registered_model.version}")

# Example usage
best_run_id, best_experiment_id, best_rmse = get_best_run_by_rmse()

if best_run_id:
    print(f"Best Run ID: {best_run_id}")
    print(f"Experiment ID: {best_experiment_id}")
    print(f"Lowest RMSE: {best_rmse}")

    # Register the best model
    model_name = "Best_RMSE_Model"
    register_best_model(best_run_id, model_name)
else:
    print("No runs with RMSE found.")


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
