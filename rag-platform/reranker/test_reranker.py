from reranker.ai_label_reviewer import AILabelReviewer
from reranker.dataset_splitter import DatasetSplitter
from reranker.dataset_validator import DatasetValidator
from reranker.evaluation.model_evaluator import ModelEvaluator
from reranker.training.model_trainer import ModelTrainer
from shared.config import get_settings


def run_dataset_validator():
    validator = DatasetValidator()
    validator.run()


def run_ai_label_review():
    settings = get_settings()
    reviewer = AILabelReviewer(
        settings,
    )
    records_requiring_review = reviewer.review_records()
    print(f"Records requiring review: {len(records_requiring_review)}")


def run_dataset_spliiter():
    splitter = DatasetSplitter()
    splitter.run()


def train_model():
    ModelTrainer().run()


def evaluate_trained_model():
    ModelEvaluator().run()


def main():
    # run_dataset_validator()
    # run_ai_label_review()
    print("inside re-ranker")
    # run_dataset_spliiter()
    # train_model()
    evaluate_trained_model()


if __name__ == "__main__":
    main()
