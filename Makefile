AWS_ACCESS_KEY_ID:=$(AWS_ACCESS_KEY_ID)
AWS_SECRET_ACCESS_KEY:=$(AWS_SECRET_ACCESS_KEY)

LOCAL_TAG:=$(shell date +"%Y-%m-%d-%H-%M")
LOCAL_IMAGE_NAME:=web_service-${LOCAL_TAG}

WEB_SERVICE_DIR:= $(shell echo ~/web_service)
INTEGRATION_TEST_DIR:= $(shell echo ~/web_service/tests)
MAGE_DIR:=$(shell echo ~/orchestration)
MLFLOW_DIR:=$(shell echo ~/experiment_tracking)


quality_checks:
	cd ${WEB_SERVICE_DIR} && bash -c "poetry run pylint ."
	isort ./web_service
	black ./web_service

track:
	cd ${MLFLOW_DIR} && bash -c "poetry run mlflow server -h 0.0.0.0 -p 5000 \
	--backend-store-uri postgresql://<Your AWS RDS Master Username>:<Your AWS RDS Master Password@<Your RDS endpoint>:5432/<Your RDS DB name>  \
	--artifacts-destination s3:/<Name of your s3 bucket>  \
	--serve-artifacts" &

train: track
	cd ${MAGE_DIR} && bash -c "./start.sh"

build: quality_checks
	docker build --build-arg AWS_ACCESS_KEY_ID --build-arg AWS_SECRET_ACCESS_KEY -t ${LOCAL_IMAGE_NAME} ${WEB_SERVICE_DIR}

run: build
	cd ${WEB_SERVICE_DIR} && docker run -d --name ${LOCAL_IMAGE_NAME} -p 9696:9696 ${LOCAL_IMAGE_NAME}
	sleep 5

integration_test: run
	cd ${INTEGRATION_TEST_DIR} && bash -c "poetry run ./integration_test.py"

stop:
	docker stop ${LOCAL_IMAGE_NAME}
	docker rm ${LOCAL_IMAGE_NAME}

setup:
	cd ${INTEGRATION_TEST_DIR} && poetry env use 3.11.9 && poetry install

all: setup quality_checks track train build run integration_test stop

#   pre-commit install
