if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from mlflow.tracking import MlflowClient
from mlflow.entities import ViewType
import mlflow
from datetime import datetime

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


    MLFLOW_TRACKING_URI = "http://ec2-34-233-122-168.compute-1.amazonaws.com:5000"
    client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
    num_experiments = len(client.search_experiments())
    
    # set the best run as the first experiment
    best_run = client.search_runs(
            experiment_ids=36, #this is the id of the first experimnt; others were deleted
            run_view_type=ViewType.ACTIVE_ONLY,
            max_results=1,
            order_by=["metrics.rmse ASC"]
        )[0]
    # iterate over remaining experiments
    for i in range(1, num_experiments):
        print(i)
        run = client.search_runs(
            experiment_ids= i + 36,
            run_view_type=ViewType.ACTIVE_ONLY,
            max_results=1,
            order_by=["metrics.rmse ASC"]
        )[0]

        if run.data.metrics['rmse'] < best_run.data.metrics['rmse']:
            best_run = run
            run_id = best_run.info.run_id

    print(f"This is the best run_id:  {run_id}")

    # register model from best run
    model_uri = f"runs:/{run_id}/model"
    model_name = f"doordash-eta-regressor"
    mlflow.register_model(model_uri=model_uri, name=model_name)
 
    # stage model
    model_version = 1
    new_stage = "Staging"
    client.transition_model_version_stage(
        name=model_name,
        version=model_version,
        stage=new_stage,
        archive_existing_versions=False
    )

    date = datetime.today().date()
    client.update_model_version(
        name=model_name,
        version=model_version,
        description=f"The model version {model_version} was transitioned to {new_stage} on {date}"
    )


    
    
    
    
    
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
