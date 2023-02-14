from fastapi import APIRouter, Depends
from starlette.requests import Request


from inference.core import security
from inference.core.config import DEFAULT_MODEL_ENDPOINT, DEFAULT_MODEL_CATEGORY
from inference.ml_services.ml_services import PredictionPayload, PredictionResult, Model

router = APIRouter()

@router.post(DEFAULT_MODEL_ENDPOINT, response_model=PredictionResult, name=DEFAULT_MODEL_CATEGORY)
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: PredictionPayload = None,
) -> PredictionResult:
    model: Model = request.app.state.model
    prediction: PredictionResult = model.predict(block_data)
    return prediction
