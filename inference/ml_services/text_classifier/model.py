from typing import Dict, List
from loguru import logger

from torch import nn


from inference.ml_services.text_classifier.payloads import PredictionPayload, PredictionResult
from inference.core.messages import NO_VALID_PAYLOAD
from inference.core.config import (
    DEFAULT_MODEL_PATH,
    DEFAULT_MODEL_CLASS,
    DEFAULT_MODEL_CATEGORY
)

class TextClassificationModel(nn.Module):

    def __init__(self, vocab_size, embed_dim, num_class):
        super(TextClassificationModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
        self.fc = nn.Linear(embed_dim, num_class)
        self.init_weights()

    def init_weights(self):
        initrange = 0.5
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()

    def forward(self, text, offsets):
        embedded = self.embedding(text, offsets)
        return self.fc(embedded)

class TextClassifier(object):
    def __init__(self, path=DEFAULT_MODEL_PATH):
        self.path = path
        self._load_local_model()

    def _load_local_model(self):
        pass


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
