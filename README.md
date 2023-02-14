# ai-playground
## Setup Steps
### Setup Repo
* checkout project
* run `git submodule update --init --recursive`
---
### Run Inference Service
* move to base of the repository
* setup and activate a virtual environment using either conda or venv (or run directly on the host)
* run following command to install deps
  ```
  make install
  ```
* run folloing command to serve question-answering model
  ```
  make serve_question_answering
  ```
* access service at [http://localhost:8000/docs](http://localhost:8000/docs)

---
### Run Jupyterlab
* move to base of the repository
* run following command
  ```
  make start_jupyterlab
  ```
* access at [http://localhost:28888](http://localhost:28888)

