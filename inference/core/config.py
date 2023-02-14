from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

APP_VERSION: str = config("APP_VERSION", default="0.i.0")
APP_NAME: str = config("APP_NAME", default="Prediction FastAPI")
API_PREFIX: str = config("API_PREFIX", default="/api")


API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

DEFAULT_MODEL_CACHE_DIR: str = config("DEFAULT_MODEL_CACHE_DIR", default="model_cache/")
DEFAULT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH", default="ml_models/text_classifier")
DEFAULT_MODEL_CATEGORY: str = config("DEFAULT_MODEL_CATEGORY", default="text_classifier")
DEFAULT_MODEL_CLASS: str = config("DEFAULT_MODEL_CLASS", default="TextClassifier")
DEFAULT_MODEL_NAME: str = config("DEFAULT_MODEL_NAME", default=None)
DEFAULT_MODEL_ENDPOINT: str = config("DEFAULT_MODEL_ENDPOINT", default="/predict")
