cd orchestration
./start.sh
cd ~/experiment_tracking
poetry env use 3.11.9
poetry install
poetry shell
sleep 2
poetry run mlflow server -h 0.0.0.0 -p 5000 \
--backend-store-uri postgresql://<Your AWS RDS Master Username>:<Your AWS RDS Master Password@<Your RDS endpoint>:5432/<Your RDS DB name>  \
	--artifacts-destination s3:/<Name of your s3 bucket>  \
	--serve-artifacts" &
