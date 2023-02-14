from typing import Callable

from fastapi import FastAPI
from loguru import logger

from inference.core.config import DEFAULT_MODEL_PATH, DEFAULT_MODEL_CATEGORY, DEFAULT_MODEL_NAME
from inference.ml_services.ml_services import Model

def _startup_model(app: FastAPI) -> None:
    model_path = DEFAULT_MODEL_PATH
    model_category = DEFAULT_MODEL_CATEGORY
    model_name = DEFAULT_MODEL_NAME
    model_instance = Model(model_path, model_category, model_name)
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
