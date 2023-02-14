from pydantic import BaseModel
from enum import Enum, IntEnum

class PredictionPayload(BaseModel):
    text: str


class PredictionResult(BaseModel):
    score: float = 0.0
    category: str = "unknown"
