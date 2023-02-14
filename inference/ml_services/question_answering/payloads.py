from pydantic import BaseModel
from enum import Enum, IntEnum

from inference.core.config import DEFAULT_MODEL_NAME


class PredictionPayload(BaseModel):
    context: str = "42 is the answer to life, the universe and everything."
    question: str = "What is the answer to life?"


class PredictionResult(BaseModel):
    score: float
    start: int
    end: int
    answer: str
    model: str = DEFAULT_MODEL_NAME
