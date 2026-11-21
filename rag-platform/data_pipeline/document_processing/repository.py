import json

from data_pipeline.document_processing.processed_trial_model import ProcessedTrial
from data_pipeline.models.clinical_trials import RawClinicalTrialDTO
from shared.database_repository import DatabaseRepository


class TrialProcessingRepository:
    def __init__(self, db: DatabaseRepository) -> None:
        self.db = db

    def get_all_raw_trials(self) -> list[RawClinicalTrialDTO]:
        query = """
            SELECT nct_id, raw_data, source_updated_at
            FROM raw_clinical_trials
        """

        return self.db.fetch_all(query, RawClinicalTrialDTO)

    def save_all(self, trials: list[ProcessedTrial]) -> None:
        if not trials:
            return

        query = """
            INSERT INTO processed_clinical_trials (
                nct_id, identification, status, description, conditions,
                interventions, design, eligibility, outcomes, sponsor,
                locations, medical_terms
            )
            VALUES (
                :nct_id,
                CAST(:identification AS JSONB),
                CAST(:status AS JSONB),
                CAST(:description AS JSONB),
                CAST(:conditions AS JSONB),
                CAST(:interventions AS JSONB),
                CAST(:design AS JSONB),
                CAST(:eligibility AS JSONB),
                CAST(:outcomes AS JSONB),
                CAST(:sponsor AS JSONB),
                CAST(:locations AS JSONB),
                CAST(:medical_terms AS JSONB)
            )
            ON CONFLICT (nct_id)
            DO UPDATE SET
                identification = EXCLUDED.identification,
                status = EXCLUDED.status,
                description = EXCLUDED.description,
                conditions = EXCLUDED.conditions,
                interventions = EXCLUDED.interventions,
                design = EXCLUDED.design,
                eligibility = EXCLUDED.eligibility,
                outcomes = EXCLUDED.outcomes,
                sponsor = EXCLUDED.sponsor,
                locations = EXCLUDED.locations,
                medical_terms = EXCLUDED.medical_terms,
                processed_at = CURRENT_TIMESTAMP
        """

        params = [
            {
                "nct_id": trial.nct_id,
                "identification": json.dumps(
                    trial.identification.model_dump(mode="json")
                ),
                "status": json.dumps(trial.status.model_dump(mode="json")),
                "description": json.dumps(trial.description.model_dump(mode="json")),
                "conditions": json.dumps(trial.conditions),
                "interventions": json.dumps(
                    [item.model_dump(mode="json") for item in trial.interventions]
                ),
                "design": json.dumps(trial.design.model_dump(mode="json")),
                "eligibility": json.dumps(trial.eligibility.model_dump(mode="json")),
                "outcomes": json.dumps(
                    [item.model_dump(mode="json") for item in trial.outcomes]
                ),
                "sponsor": json.dumps(trial.sponsor.model_dump(mode="json")),
                "locations": json.dumps(
                    [item.model_dump(mode="json") for item in trial.locations]
                ),
                "medical_terms": json.dumps(
                    [item.model_dump(mode="json") for item in trial.medical_terms]
                ),
            }
            for trial in trials
        ]

        self.db.execute_many(query, params)
