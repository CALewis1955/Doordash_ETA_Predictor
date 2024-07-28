FROM python:3.12.3-slim

# Define build arguments
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

# Use the build arguments to set environment variables
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_DEFAULT_REGION=us-east-1

# Install AWS CLI
RUN apt-get update && apt-get install -y \
    curl \
    unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

# Example command using AWS CLI
RUN aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}
RUN aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}
RUN aws configure set region ${AWS_DEFAULT_REGION}

# poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_CREATE=false

# Set PATH to include poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org |python3 - \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY .env /app/.env

COPY ["pyproject.toml", "poetry.lock", "./"]

RUN poetry install --no-dev

COPY ["predict_mlflow.py",  "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict_mlflow:app"]


