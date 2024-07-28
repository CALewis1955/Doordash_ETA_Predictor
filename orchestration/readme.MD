
# DoorDash ETA

    This is an end-to-end MLOps project built for the 2024 cohort of DataTalksClub MLOps Zoomcamp.  The Github page for the course is [https://github.com/DataTalksClub/mlops-zoomcamp/tree/main].  I am profoundly grateful to Alexey Grigorev and the course lecturers for organizing and presenting this free material.


## Architecture

    Orchestration -- Mage
    Experiment Tracking -- Mlflow
    Monitoring -- Evidently
    Containerization -- Docker
    Dependency Management -- Poetry
    Cloud Deployment -- AWS

    This project is developed entirely on the cloud.  It utilizes an AWS EC2 instance to run all the servers, and an AWS S3 bucket and AWS RDS database to store the model and Evidently report.

    We use Mage to orchestrate the workflow.  As depicted by the Mage tree, the workflow follows two paths after loading the data.  One path runs through the machine learning algorithms and reports the results to Mlflow for tracking.  Experiments are tracked and models are registered in the registry.
    
    The other path creates a dummy set of data and then uses Evidently to monitor whether data drift has occurred.  This path also stores the Evidently report in the s3 bucket.

    Finally, I have implemented a prediction web service as a Flask app that runs on port 9696.  A user can make an HTTP post request to the web service to obtain a prediction of the duration of the delivery.  

    All services are run on Docker containers, and Poetry has been used for dependency management. 


## Issues

    During the coding of this project, I encountered a multitude of errors.  My best friends were  ChatGPT and the course's Slack channel [https://datatalks-club.slack.com/join/shared_invite/zt-2hu0sjeic-ESN7uHt~aVWc8tD3PefSlA#/shared-invite/email].

    I ran out of time to implement many features, including using Grafana, which would require code to store the Evidently report in a database, implementing the best practices addressed in module 06 of the course, and optimizing the machine learning models.

    I switched to Poetry after spending a week in "dependency hell" using pipenv and conda.  As an example, I could not run Mlflow with Python 3.12.  The problem I encountered is described here:  [https://github.com/mlflow/mlflow/issues/11330].  I found Poetry to be relatively straightforward for dependency management and for using different versions of Python.   


## Reproducibility

### Step 1 -- Clone the Github Repo

    Clone the Github repository locally.

    {

    }

### Step 2 -- Setup your AWS account

    Create an AWS account [https://signin.aws.amazon.com/signup?request_type=register].

    You will need to create the User and Access keys in IAM.  You will also need to copy your AWS_ACCESS_KEY_ID and your AWS_SECRET_ACCESS_KEY.

    AWS requires that you assign permissions to each user.  I assigned admin permissions (i.e., the broadest scope), but you should assign permissions that are reasonable for your use case.

    Create an EC2 instance of type t2.large.  I found that the AWS free tier has neither the memory nor the storage to run the machine learning models.

    Create an s3 bucket and an RDS database.  You will need to record the RDS database username, the  RDS database password, and the s3 bucket name in order to start the mlflow server.

    On the EC2 instance page, copy the Public IPv4 DNS.  You will need it to retrieve the logged model.

    Create appropriate permissions for your EC2 instance to write and retrieve data from the RDS database and s3 bucket.  These include allowing communication with the mlflow server on port 5000 and allowing Custom TCP traffic on port 9696 for the duration predictions.  I also used port 22 for SSH to transfer files to and from the EC2 instance as well as for a remote connection through Visual Code Studio. 

    Configure your EC2 instance by installing Docker, docker-compose, and Poetry.  This video provides instruction on setting up the environment:  [https://www.youtube.com/watch?v=IXSiYkP23zo&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=3.]

### Step 3 -- Start Mage

    Navigate to the orchestration directory, and run "./start.sh".  This will invoke a Dockerfile to start Mage and a Postgres database.  Please note that this uses pip to install the dependencies and does not need Poetry.

    You must add your AWS credentials to the .env.dev file so they can be accessed as environment variables, since Mage will be writing info to the s3 bucket.

    Here is a screenshot of the Mage workflow:

    ![Screenshot](~/images/mage_screenshot.png)

    To view Mage in your browser, go to localhost:6789.  (If you encounter difficulty, ensure you've forwarded the port in VS Code, and ensure that no earlier processes are using the port on your local machine.  You can do the latter with the following command:  "lsof -i:6789".  If earlier processes are interfering with your use, kill them with this command:  "kill -9 <process id>" and then try to forward the port again.)

    The Evidently report is stored in both html and JSON format in the "mage_data" directory.

### Step 4 -- Start Mlflow

    Navigate to the experiment-tracking directory.  To start Mlflow, we need Python 3.11.9, so run the following commands:
        {
            poetry env use 3.11.9
            poetry install
            poetry shell
            mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri postgresql://<your_RDSdb_Master_username>:<your_RDSdb_password>@<your_AWS_RDS_endpoint>your_AWS_RDS_port>/<your AWS_RDSdb_Configuration_DBname> --artifacts-destination s3://<your AWs _s3_bucket_name> --serve-artifacts
        }
    
    Note that Mlflow requires the installation of both boto3 and psycop2g.

    The "poetry" commands are necessary to ensure that the appropriate packages are installed.

    You can view the Mlflow tracking server by putting the following URL in your browser:  http://<your AWS EC2 Public IPv4 DNS>:5000.  Note that this is "http", NOT "https".

### Step 5 -- Start Monitoring

    The Evidently report is run automatically using Mage.  However, a Grafana dashboard can be viewed by running "docker-compose up" in the Mage directory.  The dashboard will have no data because the JSON from the Evidently report needs to be sent to a database for the Grafana dashboard to view it.

### Ste[ 6 -- Web Servuce]

    In the web-service directory, run the following command to build the Dockerfile:
     "docker build --build-arg AWS_ACCESS_KEY_ID=<your AWS Access Key> --build-arg AWS_SECRET_ACCESS_KEY=<your AWS Secret Access Key> -t web-service:v1 ."

    Note that the AWS default region has been hard-coded as an environmental variable in the Dockerfile.  You will need to change this to your AWS default region or modify the Dockerfile to pass in the AWS default region as an additional build argument.   

    To run the web-service, use this command:
        "docker run -it --rm -p 9696:9696  web-service:v1"

    To test the web-sever, open a new terminal window and go to prediction-server/tests directory.  Run the following commands:
         "poetry env use 3.11.9"
         "poetry install"
         "poetry run ./test-web-server.py"












# Command to start mlflow server

mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri postgresql://mlflow:Firefly5793@mlflow-database.c5kyce0me9kt.us-east-1.rds.amazonaws.com:5432/mlflow_db --artifacts-destination s3://mlflow-clewis916-remote --serve-artifacts


# Packages to install for mlflow
Include boto3 and psycop2g-binary

# Add your AWS credentials to the .env.dev file so they can be accessed as environment variables.

# Use "http", not "https" to connect to AWS EC2 instance.

# Use the command "poetry run" to run Python scripts from the Poetry virtual environment.

# Architecture
    - Mage on 6789
    - Mlflow on 5000
    - Flask on 9696
    - Grafana on 3000

# Running Project

    - In the orchestration directory, run "./start.sh"
    - In exp-tracking directory, create a new poetry environment using python 3.11
    "poetry env use 3.11.9"
        --mlflow throws an error if we use python 3.12.
        --start mlflow tracking server
            "poetry install"
            "mlflow server..."
    - View the mlflow run in a browser by going to http://AWS_Public_IPv4_DNS:5000
    -Monitoring
        - In the monitoring directory, 
    - In the web-service directory, run the following command to build the Dockerfile:
         docker build --build-arg AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id) --build-arg AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key) -t web-service:v1 .
        To run the web-service, use this command:
        docker run -it --rm -p 9696:9696  web-service:v1

    go to prediction-server/tests directory; run predict_mlflow.py.
        -  The command is "poetry run ./predict_mlflow.py"
    - To test web-server, open a new terminal.
        - poetry env use 3.11.9
        - poetry run ./test-web-server.py