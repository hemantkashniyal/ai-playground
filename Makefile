BASH_SHELL := $(shell which bash)
SHELL := $(BASH_SHELL)
APP_CONDA_ENV_NAME ?= base

default:

.PHONY: install
install:
	conda env update -n $(APP_CONDA_ENV_NAME) -f environment.yaml

.PHONY: stop_jupyterlab
stop_jupyterlab:
	docker-compose -f ./docker/jupyterlab/docker-compose.yaml stop || true

.PHONY: start_jupyterlab
start_jupyterlab: stop_jupyterlab
	docker-compose -f ./docker/jupyterlab/docker-compose.yaml up -d
	echo Access JupyterLab: http://localhost:28888

.PHONY: install
install:
	pip install --upgrade pip && pip install -r requirements.txt

.PHONY: serve
serve:
	PYTHONPATH=inference/ uvicorn inference.main:app --reload --host 0.0.0.0 --log-level trace

.PHONY: serve_question_answering
serve_question_answering:
	cp .env.question_answering .env;
	make -C . serve

.PHONY: serve_text_classifier
serve_text_classifier:
	cp .env.text_classifier .env;
	make -C . serve

.PHONY: generate_dot_env
generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi