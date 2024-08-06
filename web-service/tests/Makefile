AWS_ACCESS_KEY_ID:=$(AWS_ACCESS_KEY_ID)
AWS_SECRET_ACCESS_KEY:=$(AWS_SECRET_ACCESS_KEY)

LOCAL_TAG:=$(shell date +"%Y-%m-%d-%H-%M")
LOCAL_IMAGE_NAME:=web-service-${LOCAL_TAG}

DOCKERFILE_DIR:= $(shell echo ~/web-service)

##	pytest tests/

# quality_checks:
###	pylint --recursive=y .

build: #quality_checks test
	docker build --build-arg AWS_ACCESS_KEY_ID --build-arg AWS_SECRET_ACCESS_KEY -t ${LOCAL_IMAGE_NAME} ${DOCKERFILE_DIR}

run: build
	(cd ${DOCKERFILE_DIR} && docker run -d --name ${LOCAL_IMAGE_NAME} -p 9696:9696 ${LOCAL_IMAGE_NAME})
#   docker run -d --name ${LOCAL_IMAGE_NAME}-container -p 9696:9696 ${LOCAL_IMAGE_NAME}

integration_test: run
	docker exec ${LOCAL_IMAGE_NAME} bash -c "poetry run ./integration_test.py"

stop:
	docker stop ${LOCAL_IMAGE_NAME}
	docker rm ${LOCAL_IMAGE_NAME}

setup:
	poetry env use 3.11.9
	poetry install

all: setup build run integration_test stop
	
#   pre-commit install