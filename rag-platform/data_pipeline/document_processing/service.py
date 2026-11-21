from data_pipeline.document_processing.processor import ClinicalTrialProcessor
from data_pipeline.document_processing.repository import TrialProcessingRepository


class TrialProcessingService:
    def __init__(self, repository: TrialProcessingRepository):
        self.repository = repository

    def process_trials(self) -> int:
        raw_trials = self.repository.get_all_raw_trials()

        processed_trials = [
            ClinicalTrialProcessor.process(trial.raw_data) for trial in raw_trials
        ]

        self.repository.save_all(processed_trials)

        return len(processed_trials)
