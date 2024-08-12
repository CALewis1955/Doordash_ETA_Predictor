
# DoorDash ETA

This is an end-to-end MLOps project built for the 2024 cohort of DataTalksClub MLOps Zoomcamp.  The Github page for the course is [https://github.com/DataTalksClub/mlops-zoomcamp/tree/main].  I am profoundly grateful to Alexey Grigorev and the course lecturers for organizing and presenting this free material.

## Problem Statement

When a consumer places an order on DoorDash, DoorDash wants to show the expected time of delivery. It is very important for DoorDash to get this right, as it has a big impact on consumer experience. In this project, I have built a model to predict the estimated time taken for a delivery.  The dataset for this project comes from Kaggle:  [https://www.kaggle.com/code/dharun4772/doordash-eta-regression-prediction-eda/input].  A description of the data is copied in the data_description.md file.

Please note that I have not attempted to optimize the prediction models, as this project was intended principally to learn the engineering of an end-to-end pipeline.

## Architecture

    Orchestration -- Mage
    Experiment Tracking -- Mlflow
    Monitoring -- Evidently
    Containerization -- Docker
    Dependency Management -- Poetry
    Cloud Deployment -- AWS

This project is developed entirely on the cloud.  It utilizes an AWS EC2 instance to run all the servers, and an AWS S3 bucket and AWS RDS database to store the model and Evidently report.

We use Mage to orchestrate the workflow.  As depicted by the Mage tree, the workflow follows two paths after loading the data.  One path runs through the machine learning algorithms and reports the results to Mlflow for tracking.  Experiments are tracked and models are registered in the registry.

The other path creates a dummy set of data and then uses Evidently to monitor whether data drift has occurred.  This path also stores the Evidently report in the s3 bucket.  Here is a screenshot of the Mage workflow:

[Screenshot](~/images/mage_workflow.png)

Finally, I have implemented a prediction web service as a Flask app that runs on port 9696.  A user can make an HTTP post request to the web service to obtain a prediction of the duration of the delivery.

All services are run on Docker containers, and Poetry has been used for dependency management.


## Issues

During the coding of this project, I encountered a multitude of errors.  My best friends were ChatGPT and the course's Slack channel [https://datatalks-club.slack.com/join/shared_invite/zt-2hu0sjeic-ESN7uHt~aVWc8tD3PefSlA#/shared-invite/email].

I ran out of time to implement many features, including using Grafana, which would require code to store the Evidently report in a database.

I switched to Poetry after spending a week in "dependency hell" using pipenv and conda.  As an example, I could not run Mlflow with Python 3.12.  The problem I encountered is described here:  [https://github.com/mlflow/mlflow/issues/11330].  I found Poetry to be relatively straightforward for dependency management and for using different versions of Python.


## Reproducibility

### Step 1 -- Clone the Github Repo

Clone the Github repository locally.

    git clone https://github.com/CALewis1955/doordash_eta_predictor/main


### Step 2 -- Setup your AWS account

Create an AWS account [https://signin.aws.amazon.com/signup?request_type=register].

You will need to create the User and Access keys in IAM.  You will also need to copy your AWS_ACCESS_KEY_ID and your AWS_SECRET_ACCESS_KEY.

AWS requires that you assign permissions to each user.  I assigned admin permissions (i.e., the broadest scope), but you should assign permissions that are reasonable for your use case.

Create an EC2 instance of type t2.large.  I found that the AWS free tier has neither the memory nor the storage to run the machine learning models.

Create an s3 bucket and an RDS database.  You will need to record the RDS database username, the  RDS database password, and the s3 bucket name in order to start the mlflow server.

On the EC2 instance page, copy the Public IPv4 DNS.  You will need it to retrieve the logged model.

Create appropriate permissions for your EC2 instance to write and retrieve data from the RDS database and s3 bucket.  These include allowing communication with the mlflow server on port 5000 and allowing Custom TCP traffic on port 9696 for the duration predictions.  I also used port 22 for SSH to transfer files to and from the EC2 instance as well as for a remote connection through Visual Code Studio.

Configure your EC2 instance by installing Docker, docker-compose, and Poetry.  This video provides instruction on setting up the environment:  [https://www.youtube.com/watch?v=IXSiYkP23zo&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=3.]

You will need to modify the following files:

~/.bashrc -- You will need to add your AWS credentials so they can be accessed by the Makefile.  Here is the code to add to your .bashrc file:

    export AWS_ACCESS_KEY_ID=<Your AWS_ACCESS_KEY_ID>
    export AWS_SECRET_ACCESS_KEY=<Your AWS_SECRET_ACCESS_KEY>
    export AWS_DEFAULT_REGION=<Your AWS_DEFAULT_REGION>

~/Makefile -- For the backend-store-uri and s3 bucket, you will need to insert your AWS RDS Master Username, your AWS RDS Master Password, your RDS endpoint, your RDS DB name, and your s3 bucket name.

~/start.sh -- As with the Makefile, you will need to insert your AWS information. 

~/orchestration/doordash_eta/.env.dev -- You will need to add the AWS credentials.  This allows the Mage orchestration to save the Evidently report to the s3 bucket.

~/orchestration/doordash_eta/transformers/train_models.py -- You will need to insert your AWS information for the URL of the MlFlow tracking server.  This takes the form:  http://<your AWS EC2 Public IPv4 DNS>:5000.

~/orchestration/doordash_eta/transformers/register_best_model.py -- Again, you will need to insert your AWS information for the URL of the MlFlow tracking server.

~/web_service/predict_mlflow.py -- In the file "predict_mlflow.py", you will need to specify your logged model information (experiment_id and RUN_ID) and replace my s3 bucket name ("mlflow-clewis916-remote") with the name of your s3 bucket. 

You will also need to ensure that Python 3.11.9 is available on your EC2 instance.  You will also need to install isort, black, and pre-commit.
 

### Step 3 -- Start the End-to-End Project

From the home directory, run the Makefile by invoking the following command:

    make all

This will automatically initiate the setup with Poetry, run quality checks on the web_service directory, start the MlFlow server on the AWS EC2 instance, start Mage and run the pipeline according to any triggers you wish to configure, start the prediction web server on port 9696, and perform an integration test.  Once the Makefile runs, the MlFlow UI will be accessible in your browser at localhost:5000, and Mage will be accessible at localhost:6789.  

Alternatively, if you merely want to start the MlFlow server and access Mage, you can run the following command:

    scripts/start.sh

To shut down the prediction server in the web_service, I use the following command:

    sudo lsof -t -i :9696 | xargs sudo kill -9

To shut down the Mage server, you can navigate to the orchestration directory and run "docker-compose down".  

To shut down the MlFlow server, you can use the following command:

    sudo lsof -t -i :5000 | xargs sudo kill -9    

The relevant Mage data_loader and transformer files are found in the Github repository at orchestration/doordash_eta/data_loaders and orchestration/doordash_eta/transformers.  The file that saves the Evidently report to the s3 bucket is found at orchestration/doordash_eta/custom/save_evidently_report_to_s3.py.

The last two blocks on the right side of the workflow train the models and then register the best one in MlFlow's model registry.  Here is a screenshot of the model registry:

[Screenshot](~/images/mlflow_registered_models.png)

Herre is a screenshot of the experiments:

[Screenshot](~/images/mlflow_experiments.png)

The left side of the workflow creates dummy data that simulates updated information on doordash delivery times.  This data is used by the Evidently report to evaluate data drift.  

If you encounter difficulty viewing either Mage or the MlFlow UI in your browser, ensure you've forwarded the port in VS Code, and ensure that no earlier processes are using the port on your local machine.  You can do the latter with the following command:  "lsof -i:6789".  If earlier processes are interfering with your use, kill them with this command:  "kill -9 <process id>" and then try to forward the port again.

The Evidently report is stored in both html and JSON format in the "mage_data" directory.

### Step 4 -- Start MlFlow

If you want to modify the code and/or play with try different machine learning models, you can start MlFlow and Mage individually.  To start MlFlow, navigate to the experiment-tracking directory.  Since we need Python 3.11.9, run the following commands:

    poetry env use 3.11.9
    poetry install
    poetry shell
    mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri postgresql://<your_RDSdb_Master_username>:<your_RDSdb_password>@<your_AWS_RDS_endpoint>your_AWS_RDS_port>/<your          AWS_RDSdb_Configuration_DBname> --artifacts-destination s3://<your AWS_s3_bucket_name> --serve-artifacts

Note that Mlflow requires the installation of both boto3 and psycop2g.

The "poetry" commands are necessary to ensure that the appropriate packages are installed.

You can view the Mlflow tracking server by putting the following URL in your browser:  http://<your AWS EC2 Public IPv4 DNS>:5000.  Note that this is "http", NOT "https".

### Step 5 -- Start Monitoring

The Evidently report is run automatically using Mage.  

### Step 6 -- Web Service

To run the prediction server individually, in the web-service directory, run the following command to build the Dockerfile:

    docker build --build-arg AWS_ACCESS_KEY_ID=<your AWS Access Key> --build-arg AWS_SECRET_ACCESS_KEY=<your AWS Secret Access Key> -t web-service:v1 .

Note that the AWS default region has been hard-coded as an environmental variable in the Dockerfile.  You will need to change this to your AWS default region or modify the Dockerfile to pass in the AWS default region as an additional build argument.  Also, in the file "predict_mlflow.py", you will need to specify your s3 bucket name and RUN_ID to retrieve the logged model.

To run the web-service, use this command:

    docker run -it --rm -p 9696:9696  web-service:v1

You will need to configure your AWS EC2 permissions to allow inbound and outbound traffic on port 9696.  To test the web-sever, open a new terminal window and go to web-service/tests directory. Run the following commands:

    poetry env use 3.11.9
    poetry install
    poetry run ./test-web-server.py

## Evaluation Criteria

Problem description -- Provided by this README.

Cloud -- The project is fully developed on AWS in the cloud.

Experiment tracking and model registry -- Both experiment tracking and model registry are used via MlFlow.

Workflow orchestration -- Fully deployed workflow using Mage.

Model deployment -- The model deployment code is fully containerized using Docker and deployed to the cloud.

Model monitoring -- The project uses Evidently for basic model monitoring that calculates and reports metrics.

Reproducibility -- Provided by this README.

Best practices

-- Unit tests have not been implemented.
-- An integration test is implemented.
-- Isort and Black are implemented for the web_service directory.  I found that pylint did not play well with Mage.
-- A Makefile has been implemented to run the entire project automatically.
-- Pre-commit hooks are implemented.
-- I have not created a CI/CD pipeline.
-- I have not deployed Terraform to provision the infrastructure.

If you have any questions about this project, please feel free to email me at clewis916@gmail.com.

