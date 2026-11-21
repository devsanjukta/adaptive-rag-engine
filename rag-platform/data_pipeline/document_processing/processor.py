from typing import Any

from data_pipeline.document_processing.processed_trial_model import (
    ProcessedTrial,
    TrialDescription,
    TrialDesign,
    TrialEligibility,
    TrialIdentification,
    TrialIntervention,
    TrialLocation,
    TrialMedicalTerm,
    TrialOutcome,
    TrialSponsor,
    TrialStatus,
)


class ClinicalTrialProcessor:
    @staticmethod
    def process(raw_data: dict[str, Any]) -> ProcessedTrial:
        protocol = raw_data.get("protocolSection", {})
        derived = raw_data.get("derivedSection", {})

        identification = protocol.get("identificationModule", {})
        status = protocol.get("statusModule", {})
        description = protocol.get("descriptionModule", {})
        conditions = protocol.get("conditionsModule", {})
        design = protocol.get("designModule", {})
        eligibility = protocol.get("eligibilityModule", {})
        sponsor = protocol.get("sponsorCollaboratorsModule", {})
        locations = protocol.get("contactsLocationsModule", {})
        outcomes = protocol.get("outcomesModule", {})
        interventions = protocol.get("armsInterventionsModule", {})

        return ProcessedTrial(
            nct_id=identification.get("nctId"),
            identification=ClinicalTrialProcessor._process_identification(
                identification
            ),
            status=ClinicalTrialProcessor._process_status(status),
            description=ClinicalTrialProcessor._process_description(description),
            conditions=ClinicalTrialProcessor._process_conditions(conditions),
            interventions=ClinicalTrialProcessor._process_interventions(interventions),
            design=ClinicalTrialProcessor._process_design(design),
            eligibility=ClinicalTrialProcessor._process_eligibility(eligibility),
            outcomes=ClinicalTrialProcessor._process_outcomes(outcomes),
            sponsor=ClinicalTrialProcessor._process_sponsor(sponsor),
            locations=ClinicalTrialProcessor._process_locations(locations),
            medical_terms=ClinicalTrialProcessor._process_medical_terms(derived),
        )

    @staticmethod
    def _process_identification(data: dict[str, Any]) -> TrialIdentification:
        return TrialIdentification(
            nct_id=data["nctId"],
            title=data["briefTitle"],
            official_title=data.get("officialTitle"),
        )

    @staticmethod
    def _process_status(data: dict[str, Any]) -> TrialStatus:
        return TrialStatus(
            overall_status=data.get("overallStatus"),
            start_date=data.get("startDateStruct", {}).get("date"),
            completion_date=data.get("completionDateStruct", {}).get("date"),
        )

    @staticmethod
    def _process_description(data: dict[str, Any]) -> TrialDescription:
        return TrialDescription(
            brief_summary=data.get("briefSummary"),
            detailed_description=data.get("detailedDescription"),
        )

    @staticmethod
    def _process_conditions(data: dict[str, Any]) -> list[str]:
        return data.get("conditions", [])

    @staticmethod
    def _process_interventions(data: dict[str, Any]) -> list[TrialIntervention]:
        return [
            TrialIntervention(
                name=item["name"],
                type=item.get("type"),
                description=item.get("description"),
                other_names=item.get("otherNames", []),
            )
            for item in data.get("interventions", [])
        ]

    @staticmethod
    def _process_design(data: dict[str, Any]) -> TrialDesign:
        enrollment = data.get("enrollmentInfo", {})

        return TrialDesign(
            study_type=data.get("studyType"),
            phases=data.get("phases", []),
            enrollment_count=enrollment.get("count"),
        )

    @staticmethod
    def _process_eligibility(data: dict[str, Any]) -> TrialEligibility:
        return TrialEligibility(
            sex=data.get("sex"),
            minimum_age=data.get("minimumAge"),
            maximum_age=data.get("maximumAge"),
            healthy_volunteers=data.get("healthyVolunteers"),
            eligibility_criteria=data.get("eligibilityCriteria"),
        )

    @staticmethod
    def _process_outcomes(data: dict[str, Any]) -> list[TrialOutcome]:
        outcomes = []

        for outcome_type in ["primaryOutcomes", "secondaryOutcomes", "otherOutcomes"]:
            for item in data.get(outcome_type, []):
                outcomes.append(
                    TrialOutcome(
                        measure=item["measure"],
                        type=outcome_type,
                        time_frame=item.get("timeFrame"),
                        description=item.get("description"),
                    )
                )

        return outcomes

    @staticmethod
    def _process_sponsor(data: dict[str, Any]) -> TrialSponsor:
        lead_sponsor = data.get("leadSponsor", {})

        return TrialSponsor(
            lead_sponsor=lead_sponsor.get("name"),
            collaborators=[item["name"] for item in data.get("collaborators", [])],
        )

    @staticmethod
    def _process_locations(data: dict[str, Any]) -> list[TrialLocation]:
        return [
            TrialLocation(
                facility=item.get("facility"),
                city=item.get("city"),
                state=item.get("state"),
                country=item.get("country"),
                zip_code=item.get("zip"),
                status=item.get("status"),
            )
            for item in data.get("locations", [])
        ]

    @staticmethod
    def _process_medical_terms(data: dict[str, Any]) -> list[TrialMedicalTerm]:
        terms = []

        condition_meshes = data.get("conditionBrowseModule", {}).get("meshes", [])
        intervention_meshes = data.get("interventionBrowseModule", {}).get("meshes", [])

        for item in condition_meshes:
            terms.append(
                TrialMedicalTerm(id=item["id"], term=item["term"], type="condition")
            )

        for item in intervention_meshes:
            terms.append(
                TrialMedicalTerm(id=item["id"], term=item["term"], type="intervention")
            )

        return terms
