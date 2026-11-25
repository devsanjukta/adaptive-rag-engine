import pandas as pd
from sentence_transformers import CrossEncoder
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

from reranker.dataset_utils import DatasetUtils
from reranker.models import RerankerDatasetRecord
from shared.config import (
    RERANKING_TEST_PATH,
    RERANKING_TRAINED_MODEL_PATH,
)


class ModelEvaluator:
    model_path = RERANKING_TRAINED_MODEL_PATH
    test_path = RERANKING_TEST_PATH

    def __init__(self):
        self.model = CrossEncoder(str(self.model_path))
        self.test_data: list[RerankerDatasetRecord] = []

    def _load_data(self):
        self.test_data = DatasetUtils.fetch_reranker_records(self.test_path)

    def _evaluate(self):
        pairs = [(record.query, record.document) for record in self.test_data]

        labels = [record.label for record in self.test_data]

        scores = self.model.predict(pairs)

        predictions = (scores >= 0.5).astype(int)

        print(f"Accuracy:  {accuracy_score(labels, predictions):.4f}")
        print(f"Precision: {precision_score(labels, predictions, zero_division=0):.4f}")
        print(f"Recall:    {recall_score(labels, predictions, zero_division=0):.4f}")
        print(f"F1 Score:  {f1_score(labels, predictions, zero_division=0):.4f}")
        print(f"ROC-AUC:   {roc_auc_score(labels, scores):.4f}")

    def run(self):
        self._load_data()
        self._evaluate()
