from typing import Dict, List
from loguru import logger

from transformers import AutoTokenizer
from transformers import AutoModelForQuestionAnswering
from transformers import pipeline

from inference.ml_services.question_answering.payloads import PredictionPayload, PredictionResult
from inference.core.utils.nlp_model_loader import NLPModelLoader
from inference.core.messages import NO_VALID_PAYLOAD
from inference.core.config import (
    DEFAULT_MODEL_PATH,
    DEFAULT_MODEL_CACHE_DIR,
    DEFAULT_MODEL_NAME,
)


class QAModel(object):
    def __init__(self, path=DEFAULT_MODEL_PATH):
        self.path = path
        self._load_local_model()

    def _load_local_model(self):

        tokenizer, model = NLPModelLoader(
            model_name=DEFAULT_MODEL_NAME,
            model_directory=DEFAULT_MODEL_PATH,
            model_cache_directory=DEFAULT_MODEL_CACHE_DIR,
            tokenizer_loader=AutoTokenizer,
            model_loader=AutoModelForQuestionAnswering,
        ).retrieve()

        self.nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)
        logger.debug("Local model loaded.")

    def _pre_process(self, payload: PredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = [payload.context, payload.question]
        return result

    def _post_process(self, prediction: Dict) -> PredictionResult:
        logger.debug("Post-processing prediction.")

        qa = PredictionResult(**prediction)

        return qa

    def _predict(self, features: List) -> tuple:
        logger.debug("Predicting.")

        context, question = features

        QA_input = {
            "question": question,
            "context": context,
        }

        prediction_result = self.nlp(QA_input)

        return prediction_result

    def predict(self, payload: PredictionPayload):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result
