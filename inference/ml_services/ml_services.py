
import importlib

from inference.core.config import DEFAULT_MODEL_CATEGORY, DEFAULT_MODEL_CLASS

PredictionPayload = importlib.import_module("inference.ml_services." + DEFAULT_MODEL_CATEGORY + ("." if DEFAULT_MODEL_CATEGORY else "") + "payloads").__dict__["PredictionPayload"]
PredictionResult = importlib.import_module("inference.ml_services." + DEFAULT_MODEL_CATEGORY + ("." if DEFAULT_MODEL_CATEGORY else "") + "payloads").__dict__["PredictionResult"]
Model = importlib.import_module("inference.ml_services." + DEFAULT_MODEL_CATEGORY + ("." if DEFAULT_MODEL_CATEGORY else "") + "model").__dict__[DEFAULT_MODEL_CLASS]

model_registry = {
    DEFAULT_MODEL_CATEGORY: Model
}

def getModel(model_path: str, model_category: str, model_name: str) -> Model:
    if DEFAULT_MODEL_CATEGORY == "question_answering":
            return Model(model_path)

    if DEFAULT_MODEL_CATEGORY == "text_classifier":
            return Model(model_path)

    return None