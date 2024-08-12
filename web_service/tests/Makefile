AWS_ACCESS_KEY_ID:=$(AWS_ACCESS_KEY_ID)
AWS_SECRET_ACCESS_KEY:=$(AWS_SECRET_ACCESS_KEY)

LOCAL_TAG:=$(shell date +"%Y-%m-%d-%H-%M")
LOCAL_IMAGE_NAME:=web_service-${LOCAL_TAG}

DOCKERFILE_DIR:= $(shell echo ~/web_service)
INTEGRATION_TEST_DIR:= $(shell echo ~/web_service/tests)

build:
	docker build --build-arg AWS_ACCESS_KEY_ID --build-arg AWS_SECRET_ACCESS_KEY -t ${LOCAL_IMAGE_NAME} ${DOCKERFILE_DIR}

run: build
	(cd ${DOCKERFILE_DIR} && docker run -d --name ${LOCAL_IMAGE_NAME} -p 9696:9696 ${LOCAL_IMAGE_NAME})
	sleep 2

integration_test: run
	cd ${INTEGRATION_TEST_DIR} && bash -c "poetry run ./integration_test.py"

stop:
	docker stop ${LOCAL_IMAGE_NAME}
	docker rm ${LOCAL_IMAGE_NAME}

setup:
	poetry env use 3.11.9
	poetry install

all: setup build run integration_test stop
