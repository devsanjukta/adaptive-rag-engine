---
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:1524
- loss:BinaryCrossEntropyLoss
base_model: cross-encoder/ms-marco-MiniLM-L-6-v2
pipeline_tag: text-ranking
library_name: sentence-transformers
metrics:
- accuracy
- accuracy_threshold
- f1
- f1_threshold
- precision
- recall
- average_precision
model-index:
- name: CrossEncoder based on cross-encoder/ms-marco-MiniLM-L-6-v2
  results:
  - task:
      type: cross-encoder-binary-classification
      name: Cross Encoder Binary Classification
    dataset:
      name: clinical trials validation
      type: clinical_trials_validation
    metrics:
    - type: accuracy
      value: 0.8847262247838616
      name: Accuracy
    - type: accuracy_threshold
      value: 0.3852359652519226
      name: Accuracy Threshold
    - type: f1
      value: 0.8591549295774648
      name: F1
    - type: f1_threshold
      value: 0.31591808795928955
      name: F1 Threshold
    - type: precision
      value: 0.8714285714285714
      name: Precision
    - type: recall
      value: 0.8472222222222222
      name: Recall
    - type: average_precision
      value: 0.9165171663970653
      name: Average Precision
---

# CrossEncoder based on cross-encoder/ms-marco-MiniLM-L-6-v2

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [cross-encoder/ms-marco-MiniLM-L-6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text reranking and semantic search.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [cross-encoder/ms-marco-MiniLM-L-6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2) <!-- at revision 233902d25c440f23af6f7d6e94d2946bac0bee0a -->
- **Maximum Sequence Length:** 512 tokens
- **Number of Output Labels:** 1 label
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Documentation:** [Cross Encoder Documentation](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Cross Encoders on Hugging Face](https://huggingface.co/models?library=sentence-transformers&other=cross-encoder)

### Full Model Architecture

```
CrossEncoder(
  (0): Transformer({'transformer_task': 'sequence-classification', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'logits'}}, 'module_output_name': 'scores', 'architecture': 'BertForSequenceClassification'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import CrossEncoder

# Download from the 🤗 Hub
model = CrossEncoder("cross_encoder_model_id")
# Get scores for pairs of inputs
pairs = [
    ['Find clinical trials for primary lung cancer', 'Title: A Study of mRNA-5671/V941 as Monotherapy and in Combination With Pembrolizumab (V941-001)\nOfficial title: A Phase 1, Open-Label, Multicenter Study to Assess the Safety and Tolerability of mRNA-5671/V941 as a Monotherapy and in Combination With Pembrolizumab in Participants With KRAS Mutant Advanced or Metastatic Non-Small Cell Lung Cancer, Colorectal Cancer or Pancreatic Adenocarcinoma\nConditions: Neoplasms; Carcinoma, Non-Small-Cell Lung; Pancreatic Neoplasms; Colorectal Neoplasms\nBrief summary: This study will determine the safety and tolerability and establish a preliminary recommended Phase 2 dose of V941(mRNA-5671/V941) as a monotherapy and in combination with pembrolizumab infusion.\nInterventions: V941: V941 administered IM, Q3W for 9 3-week cycles; Pembrolizumab: Pembrolizumab 200 mg, IV for 35 3-week cycles\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: PHASE1\nEligibility: Inclusion Criteria:\n\nPart 2 Only\n\n\\- Has a histologically confirmed advanced or metastatic non-small cell lung cancer (NSCLC), non-mismatch repair deficient/microsatellite instability-high tumors colorectal cancers (non-MSI-H CRC), or pancreatic adenocarcinoma, and confirmed HLA types HLA-A11:01 and/or HLA C08:02 (and/or potentially other additional HLA types to be specified).\n\nNSCLC: Participants must have been tested for mutations affecting EGFR and/or anaplastic lymphoma kinase (ALK). Participants with ALK or epidermal growth factor receptor (EGFR)-positive NSCLC must have had recurrent or progressive disease (PD) after treatment with the corresponding inhibitor and current standard of care, in any sequence.\n\nNon-MSI-H CRC: Participant tumors must have been locally tested for MSI and have been found to be non-MSI-H.\n\nAll\n\n* Has a histologically confirmed advanced or metastatic KRAS 4MUT+ (G12D, G12V, G13D or G12C) (4 prevalent KRAS mutant antigens in solid tumors) solid tumor identified by local laboratory testing, and who have received, or been intolerant to, or ineligible for all treatment known to confer clinical benefit.\n* A male participant must agree to use study-approved contraception during the treatment period and for at least 120 days after the last dose of study intervention and refrain from donating sperm during this period.\n* A female participant was not be pregnant, not breastfeeding, and at not be a woman of childbearing potential (WOCBP) OR if a WOCBP, agrees to follow study-approved contraceptive guidance during treatment period and for at least 120 days after the last dose of study intervention.\n* Have measurable disease per RECIST 1.1 as assessed by the local site investigator/radiology. Lesions situated in a previously irradiated area are considered measurable if progression has been demonstrated in such lesions.\n* For Part 1 only: Cutaneous lesions can be considered in addition to imaging, but measurable disease should be defined by radiologic assessment.\n* Have an evaluable archival tumor sample to submit for analysis. Formalin-fixed, paraffin embedded (FFPE) tissue blocks are preferred to slides.\n* Have adequate organ function\n* Have a performance status of 0 or 1 on the Eastern Cooperative Oncology Group (ECOG) Performance Scale.\n\nExclusion Criteria:\n\n* A WOCBP who has a positive urine pregnancy test within 72 hours prior to randomization or treatment allocation\n* Has an active infection requiring therapy.\n* Has a history of interstitial lung disease.\n* Has an active autoimmune disease that has required systemic treatment in the past 2 years (ie, with use of disease modifying agents, corticosteroids, or immunosuppressive drugs) except vitiligo or resolved childhood asthma/atopy.\n* Has not fully recovered from any effects of major surgery or has evidence of detectable infection. Surgeries that required general anesthesia must be completed at least 2 weeks before first study treatment administration. Surgery requiring regional/epidural anesthesia must be completed at least 72 hours before first study treatment administration and participants should be recovered.\n* Has had chemotherapy, definitive radiation, or biological cancer therapy within 4 weeks (2 weeks for palliative radiation) prior to the first dose of study therapy, non-cytotoxic small molecule therapeutics within 5 half-lives (or 2 weeks, whichever is longer) prior to the first dose of study treatment, or has not recovered to Common Toxicity Criteria for Adverse Events (CTCAE) Grade 1 or better from any adverse events that were due to cancer therapeutics administered more than 4 weeks earlier (this includes participants with previous immunomodulatory therapy with residual immune-related adverse events).\n* Has received a live-virus vaccine within 30 days of planned treatment start. Seasonal flu vaccines that do not contain live virus are permitted.\n* Has received hematopoietic colony-stimulating growth factors (eg, granulocyte-colony stimulating factor, granulocyte-macrophage-colony stimulating factor, macrophage colony stimul'],
    ['Find lung cancer diagnosis and staging clinical trials', 'Title: Clearance Of Mucus In Stents (COMIS)\nOfficial title: Clearance Of Mucus In Stents (COMIS)\nConditions: Lung Neoplasms; Respiratory Failure; Pneumonia; Acute Coronary Syndromes; Unstable Angina; Myocardial Infarction; Cardiac Arrhythmia; Thromboembolic Disease\nBrief summary: The goal of this clinical research study is to compare the effects of sodium bicarbonate to normal saline when used for clearing mucus blockage in patients with airway stents.\nInterventions: Normal Saline: Normal saline administered in stent/airway tubes under direct visualization via the bronchoscope.; Sodium Bicarbonate: 4.2% bicarbonate solution mixed with equal volume of sterile water administered into stent/airway tubes under direct visualization via the bronchoscope.\nStudy purpose: DIAGNOSTIC\nStudy type: INTERVENTIONAL\nPhases: NA\nEligibility: Inclusion Criteria:\n\n1. Adult patients (\\>/= 18 years) with airway stents undergoing bronchoscopy.\n2. Patients previously enrolled, but excluded as no stent lumen obstruction from mucus retention identified at earlier enrollment (hence excluded at that enrollment) .\n\nExclusion Criteria:\n\n1. Patients with history of allergy or adverse reactions to sodium bicarbonate or normal saline.\n2. Patients refusing to sign informed written consent for participation in research.\n3. Patients with no stent lumen occlusion from mucus impaction as determined at the time of the initial visual bronchoscopic assessment.\n4. Previously enrolled patients who completed this protocol.'],
    ['Find lung cancer chemotherapy clinical trials', 'Title: Adjuvant Afatinib in Stage I-III NSCLC With EGFR Mutation\nOfficial title: Randomized Phase II Study Comparing Concise Versus Prolonged Afatinib as Adjuvant Therapy for Patients With Resected Stage I-III NSCLC With EGFR Mutation\nConditions: Non Small Cell Lung Cancer\nBrief summary: This research study is a Phase II clinical trial, which tests the safety and effectiveness of an investigational drug to learn whether the drug works in treating a specific cancer. "Investigational" means that the drug is still being studied. It also means that the FDA has not yet approved afatinib for use in patients.\n\nIn this research study the investigators are looking to see if taking afatinib after surgery works better when taken over a short period of time, compared to a long period of time.\nInterventions: Afatinib\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: PHASE2\nEligibility: Inclusion Criteria:\n\n* Pathologically confirmed diagnosis of non-small cell lung cancer with EGFR mutation\n* Complete surgical resection, pathologic stage IA-B, IIA-B, IIIA-B by AJCC 7th Edition staging criteria\n* Surgical resection with curative intent was at least 6 months prior to enrollment\n* At least 3 weeks have passed since completion of adjuvant chemotherapy or radiotherapy\n\nExclusion Criteria:\n\n* Pregnant or breastfeeding\n* History of allergic reactions attributed to compounds of similar chemical composition to afatinib\n* Prior exposure to EGFR tyrosine kinase inhibitor\n* Evidence of clinically active interstitial lung disease\n* Radiographic evidence of recurrent NSCLC prior to afatinib treatment\n* Receipt of any experimental treatment within 30 days of start of treatment with afatinib until the end of treatment visit\n* Use of potent P-gp inhibitors and potent P-gp inducers must be avoided during treatment with afatinib\n* Individuals with a history of a different malignancy (except: synchronous or metachronous primary non-small cell lung cancers of lower stage than the cancer for which adjuvant treatment is currently being prescribed; disease free for at least 3 years; cervical cancer in situ; basal or squamous cell carcinoma of the skin)\n* HIV positive on combination antiretroviral therapy\n* Uncontrolled intercurrent illness'],
    ['Find clinical trials for primary lung cancer', "Title: Osimertinib and Navitoclax in Treating Patients With EGFR-Positive Previously Treated Advanced or Metastatic Non-small Cell Lung Cancer\nOfficial title: A Phase 1B Study of AZD9291 in Combination With Navitoclax in EGFR-Mutant Non-Small Cell Lung Cancer Following Resistance to Initial EGFR Kinase Inhibitor\nConditions: Advanced Lung Non-Squamous Non-Small Cell Carcinoma; Metastatic Lung Non-Squamous Non-Small Cell Carcinoma; Stage III Lung Non-Small Cell Cancer AJCC v7; Stage IIIA Lung Non-Small Cell Cancer AJCC v7; Stage IIIB Lung Non-Small Cell Cancer AJCC v7; Stage IV Lung Non-Small Cell Cancer AJCC v7\nBrief summary: This phase Ib trial studies the side effects and best dose of osimertinib and navitoclax when given together and to see how well they work in treating patients with previously treated epidermal growth factor receptor (EGFR)-positive non-small cell lung cancer that has spread to other places in the body (metastatic) or has not responded to previous treatment with initial EGFR kinase inhibitor. Osimertinib and navitoclax may stop the growth of tumor cells by blocking some of the enzymes needed for cell growth.\nInterventions: Navitoclax: Given PO; Osimertinib: Given PO\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: PHASE1\nEligibility: Inclusion Criteria:\n\n* Histologically confirmed non-squamous NSCLC, with incurable advanced or metastatic disease\n* Prior genotyping positive for an EGFR activating mutation (L858R, exon 19 deletion, G719X, L861Q)\n* Progression after prior treatment with an EGFR TKI; in addition to this one prior line of therapy, any additional prior lines of therapy are permitted; prior treatment with a third-generation EGFR TKI is allowed for the dose escalation phase, but is not permitted for the expansion cohort\n* Adequate archival tissue from a biopsy performed after progression of disease on previous EGFR TKI; or willing to undergo a new tumor biopsy prior to registration (for the dose escalation portion only this requirement can be waived if T790M status has already been determined using a local assay)\n* For the dose expansion portion only, patient must: 1) have a tumor which is EGFR-T790M positive and 2) be treatment naive to T790M-directed EGFR TKI (e.g. AZD9291, rociletinib, etc); T790M testing may be done locally or centrally on study, but if done locally, tissue must be available for central confirmation\n* Measurable disease per Response Evaluation Criteria in Solid Tumors (RECIST 1.1)\n* Any number of prior therapies are allowed\n* Age \\>= 18 years. NSCLC is exceedingly rare in patients \\< 18 years of age. Because no dosing or adverse event data are currently available on the use of AZD9291 in combination with navitoclax in patients \\< 18 years of age, children are excluded from this study\n* Eastern Cooperative Oncology Group (ECOG) performance status =\\< 1 (Karnofsky \\>= 70%)\n* Patients must have the ability to swallow oral dosage forms\n* Life expectancy of greater than 3 months\n* Leukocytes \\>= 3,000/mcL\n* Absolute neutrophil count \\>= 1,500/mcL\n* Hemoglobin \\>= 8.0 g/dL\n* Platelets \\>= 100,000/mcL\n* Activated partial thromboplastin time (aPTT), prothrombin time (PT) =\\< 1.2 x upper limit of normal (ULN)\n* Total bilirubin =\\< 1.5 x ULN (patients with Gilbert's syndrome may have serum bilirubin \\> 1.5 x ULN)\n* Aspartate aminotransferase (AST) (serum glutamic oxaloacetic transaminase \\[SGOT\\])/alanine aminotransferase (ALT) (serum glutamate pyruvate transaminase \\[SGPT\\]) =\\< 3.0 x institutional ULN\n* Creatinine =\\< 2.0 mg/dL OR\n* Creatinine clearance \\>= 50 mL/min\n* The effects of AZD9291 and navitoclax on the developing human fetus are unknown; for this reason, women of child-bearing potential and men must agree to use adequate contraception using one of the methods listed below prior to study entry, for the duration of study participation, and for 3 months for women and 6 months for men following the date of the last dose of AZD9291 and/or navitoclax:\n\n  * Total abstinence from sexual intercourse (minimum one complete menstrual cycle prior to study drug administration)\n  * Vasectomized male subject or vasectomized partner of female subjects\n  * Hormonal contraceptives (oral, parenteral, transdermal or vaginal ring) for at least 3 months prior to study drug administration; if the subject is currently using a hormonal contraceptive, she should also use a barrier method during this study and for 3 months after study completion\n  * Intrauterine device (IUD)\n  * Double-barrier method: male condom plus diaphragm or vaginal cap with spermicide (contraceptive sponge, jellies or creams)\n  * Additionally, male subjects (including those who are vasectomized) whose partners are pregnant or might be pregnant must agree to use condoms for the duration of the study and 6 months following completion of therapy\n* Women of childbearing potential must have a negative urine pregnancy test within 7 days prior to initiation of treatment; women will be considered not of c"],
    ['Find clinical trials for primary lung cancer', "Title: SP Robotic Versus VATS Anatomical Pulmonary Resection for Patients With NSCLC\nOfficial title: Single-POrt Robotic Versus Video-assisted Thoracic Surgery Anatomical Pulmonary Resection for Patients With Non-small Cell Lung Cancer (SPORTS Study): a Single-center, Single-blinded, Randomized Controlled Trial\nConditions: Robotics; Lung Cancer\nBrief summary: Single-POrt Robotic-assisted thoracic surgery versus single-port video-assisted Thoracic Surgery major pulmonary resection for patients with non-small cell lung cancer (SPORTS trial): a single-center, a single blinded, randomized controlled trial\nInterventions: Single-port robotic-assisted thoracic surgery: All patients : 145 patients Single-port anatomical pulmonary resection(segmentectomy, lobectomy) with a complete mediastinal lymph node dissection will be performed using the SP robotic system. A 4-cm single incision will be made below the subcostal margin. A chest tube will be inserted in same incision.; Single-port video-assisted thoracoscopic surgery: All patients : 145 patients Single-port anatomical pulmonary resection(segmentectomy, lobectomy) with a complete mediastinal lymph node dissection will be performed using the VATS. A 4-cm single incision will be made at 5th intercostal space. A chest tube will be inserted in same incision.\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: NA\nEligibility: Inclusion Criteria:\n\n* Candidate for anatomical pulmonary resection (segmentectomy or lobectomy) via minimally invasive thoracic surgery (RATS or VATS) for patient with non-small cell lung cancer or suspected malignant lesion.\n* Age ≥ 18 years\n* Patients who can comply with the requirements of the clinical trial and who, or their legal representatives, provide written consent before the start of the clinical trial\n* Patients with the nationality of South Korea\n* American Society of Anesthesiologists score 1-3.\n* Clinical stage I, II or IIIa non-small cell lung cancer (NSCLC)\n\nExclusion Criteria:\n\n* Patients who require surgery for accompanying other organ diseases\n* Tumor invasion into the chest wall, diaphragm, another lobe or diaphragm\n* Patients who are considered unsuitable based on the researcher's judgment\n* Patients with cognitive impairments who are unable to understand the instructions and informed consent of this study\n* Patients who specifically desire a certain surgical method (robotic, thoracoscopic, open thoracotomy)\n* Patients who previously undergone a thoracic surgical procedure in the hemithorax to be operated on\n* Pathological results other than NSCLC (ex, benign nodules, metastatic lung cancer, SCLC)\n* Patients who received neoadjuvant therapy.\n* Candidate for pneumonectomy, bilobectomy, lobectomy plus segmentectomy, non-anatomic resection (ex, wedge resection).\n* History of other cancers in the past 5 years."],
]
scores = model.predict(pairs)
print(scores)
# [ 4.9928 -3.942   0.5836  4.8476  4.606 ]

# Or rank different texts based on similarity to a single text
ranks = model.rank(
    'Find clinical trials for primary lung cancer',
    [
        'Title: A Study of mRNA-5671/V941 as Monotherapy and in Combination With Pembrolizumab (V941-001)\nOfficial title: A Phase 1, Open-Label, Multicenter Study to Assess the Safety and Tolerability of mRNA-5671/V941 as a Monotherapy and in Combination With Pembrolizumab in Participants With KRAS Mutant Advanced or Metastatic Non-Small Cell Lung Cancer, Colorectal Cancer or Pancreatic Adenocarcinoma\nConditions: Neoplasms; Carcinoma, Non-Small-Cell Lung; Pancreatic Neoplasms; Colorectal Neoplasms\nBrief summary: This study will determine the safety and tolerability and establish a preliminary recommended Phase 2 dose of V941(mRNA-5671/V941) as a monotherapy and in combination with pembrolizumab infusion.\nInterventions: V941: V941 administered IM, Q3W for 9 3-week cycles; Pembrolizumab: Pembrolizumab 200 mg, IV for 35 3-week cycles\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: PHASE1\nEligibility: Inclusion Criteria:\n\nPart 2 Only\n\n\\- Has a histologically confirmed advanced or metastatic non-small cell lung cancer (NSCLC), non-mismatch repair deficient/microsatellite instability-high tumors colorectal cancers (non-MSI-H CRC), or pancreatic adenocarcinoma, and confirmed HLA types HLA-A11:01 and/or HLA C08:02 (and/or potentially other additional HLA types to be specified).\n\nNSCLC: Participants must have been tested for mutations affecting EGFR and/or anaplastic lymphoma kinase (ALK). Participants with ALK or epidermal growth factor receptor (EGFR)-positive NSCLC must have had recurrent or progressive disease (PD) after treatment with the corresponding inhibitor and current standard of care, in any sequence.\n\nNon-MSI-H CRC: Participant tumors must have been locally tested for MSI and have been found to be non-MSI-H.\n\nAll\n\n* Has a histologically confirmed advanced or metastatic KRAS 4MUT+ (G12D, G12V, G13D or G12C) (4 prevalent KRAS mutant antigens in solid tumors) solid tumor identified by local laboratory testing, and who have received, or been intolerant to, or ineligible for all treatment known to confer clinical benefit.\n* A male participant must agree to use study-approved contraception during the treatment period and for at least 120 days after the last dose of study intervention and refrain from donating sperm during this period.\n* A female participant was not be pregnant, not breastfeeding, and at not be a woman of childbearing potential (WOCBP) OR if a WOCBP, agrees to follow study-approved contraceptive guidance during treatment period and for at least 120 days after the last dose of study intervention.\n* Have measurable disease per RECIST 1.1 as assessed by the local site investigator/radiology. Lesions situated in a previously irradiated area are considered measurable if progression has been demonstrated in such lesions.\n* For Part 1 only: Cutaneous lesions can be considered in addition to imaging, but measurable disease should be defined by radiologic assessment.\n* Have an evaluable archival tumor sample to submit for analysis. Formalin-fixed, paraffin embedded (FFPE) tissue blocks are preferred to slides.\n* Have adequate organ function\n* Have a performance status of 0 or 1 on the Eastern Cooperative Oncology Group (ECOG) Performance Scale.\n\nExclusion Criteria:\n\n* A WOCBP who has a positive urine pregnancy test within 72 hours prior to randomization or treatment allocation\n* Has an active infection requiring therapy.\n* Has a history of interstitial lung disease.\n* Has an active autoimmune disease that has required systemic treatment in the past 2 years (ie, with use of disease modifying agents, corticosteroids, or immunosuppressive drugs) except vitiligo or resolved childhood asthma/atopy.\n* Has not fully recovered from any effects of major surgery or has evidence of detectable infection. Surgeries that required general anesthesia must be completed at least 2 weeks before first study treatment administration. Surgery requiring regional/epidural anesthesia must be completed at least 72 hours before first study treatment administration and participants should be recovered.\n* Has had chemotherapy, definitive radiation, or biological cancer therapy within 4 weeks (2 weeks for palliative radiation) prior to the first dose of study therapy, non-cytotoxic small molecule therapeutics within 5 half-lives (or 2 weeks, whichever is longer) prior to the first dose of study treatment, or has not recovered to Common Toxicity Criteria for Adverse Events (CTCAE) Grade 1 or better from any adverse events that were due to cancer therapeutics administered more than 4 weeks earlier (this includes participants with previous immunomodulatory therapy with residual immune-related adverse events).\n* Has received a live-virus vaccine within 30 days of planned treatment start. Seasonal flu vaccines that do not contain live virus are permitted.\n* Has received hematopoietic colony-stimulating growth factors (eg, granulocyte-colony stimulating factor, granulocyte-macrophage-colony stimulating factor, macrophage colony stimul',
        'Title: Clearance Of Mucus In Stents (COMIS)\nOfficial title: Clearance Of Mucus In Stents (COMIS)\nConditions: Lung Neoplasms; Respiratory Failure; Pneumonia; Acute Coronary Syndromes; Unstable Angina; Myocardial Infarction; Cardiac Arrhythmia; Thromboembolic Disease\nBrief summary: The goal of this clinical research study is to compare the effects of sodium bicarbonate to normal saline when used for clearing mucus blockage in patients with airway stents.\nInterventions: Normal Saline: Normal saline administered in stent/airway tubes under direct visualization via the bronchoscope.; Sodium Bicarbonate: 4.2% bicarbonate solution mixed with equal volume of sterile water administered into stent/airway tubes under direct visualization via the bronchoscope.\nStudy purpose: DIAGNOSTIC\nStudy type: INTERVENTIONAL\nPhases: NA\nEligibility: Inclusion Criteria:\n\n1. Adult patients (\\>/= 18 years) with airway stents undergoing bronchoscopy.\n2. Patients previously enrolled, but excluded as no stent lumen obstruction from mucus retention identified at earlier enrollment (hence excluded at that enrollment) .\n\nExclusion Criteria:\n\n1. Patients with history of allergy or adverse reactions to sodium bicarbonate or normal saline.\n2. Patients refusing to sign informed written consent for participation in research.\n3. Patients with no stent lumen occlusion from mucus impaction as determined at the time of the initial visual bronchoscopic assessment.\n4. Previously enrolled patients who completed this protocol.',
        'Title: Adjuvant Afatinib in Stage I-III NSCLC With EGFR Mutation\nOfficial title: Randomized Phase II Study Comparing Concise Versus Prolonged Afatinib as Adjuvant Therapy for Patients With Resected Stage I-III NSCLC With EGFR Mutation\nConditions: Non Small Cell Lung Cancer\nBrief summary: This research study is a Phase II clinical trial, which tests the safety and effectiveness of an investigational drug to learn whether the drug works in treating a specific cancer. "Investigational" means that the drug is still being studied. It also means that the FDA has not yet approved afatinib for use in patients.\n\nIn this research study the investigators are looking to see if taking afatinib after surgery works better when taken over a short period of time, compared to a long period of time.\nInterventions: Afatinib\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: PHASE2\nEligibility: Inclusion Criteria:\n\n* Pathologically confirmed diagnosis of non-small cell lung cancer with EGFR mutation\n* Complete surgical resection, pathologic stage IA-B, IIA-B, IIIA-B by AJCC 7th Edition staging criteria\n* Surgical resection with curative intent was at least 6 months prior to enrollment\n* At least 3 weeks have passed since completion of adjuvant chemotherapy or radiotherapy\n\nExclusion Criteria:\n\n* Pregnant or breastfeeding\n* History of allergic reactions attributed to compounds of similar chemical composition to afatinib\n* Prior exposure to EGFR tyrosine kinase inhibitor\n* Evidence of clinically active interstitial lung disease\n* Radiographic evidence of recurrent NSCLC prior to afatinib treatment\n* Receipt of any experimental treatment within 30 days of start of treatment with afatinib until the end of treatment visit\n* Use of potent P-gp inhibitors and potent P-gp inducers must be avoided during treatment with afatinib\n* Individuals with a history of a different malignancy (except: synchronous or metachronous primary non-small cell lung cancers of lower stage than the cancer for which adjuvant treatment is currently being prescribed; disease free for at least 3 years; cervical cancer in situ; basal or squamous cell carcinoma of the skin)\n* HIV positive on combination antiretroviral therapy\n* Uncontrolled intercurrent illness',
        "Title: Osimertinib and Navitoclax in Treating Patients With EGFR-Positive Previously Treated Advanced or Metastatic Non-small Cell Lung Cancer\nOfficial title: A Phase 1B Study of AZD9291 in Combination With Navitoclax in EGFR-Mutant Non-Small Cell Lung Cancer Following Resistance to Initial EGFR Kinase Inhibitor\nConditions: Advanced Lung Non-Squamous Non-Small Cell Carcinoma; Metastatic Lung Non-Squamous Non-Small Cell Carcinoma; Stage III Lung Non-Small Cell Cancer AJCC v7; Stage IIIA Lung Non-Small Cell Cancer AJCC v7; Stage IIIB Lung Non-Small Cell Cancer AJCC v7; Stage IV Lung Non-Small Cell Cancer AJCC v7\nBrief summary: This phase Ib trial studies the side effects and best dose of osimertinib and navitoclax when given together and to see how well they work in treating patients with previously treated epidermal growth factor receptor (EGFR)-positive non-small cell lung cancer that has spread to other places in the body (metastatic) or has not responded to previous treatment with initial EGFR kinase inhibitor. Osimertinib and navitoclax may stop the growth of tumor cells by blocking some of the enzymes needed for cell growth.\nInterventions: Navitoclax: Given PO; Osimertinib: Given PO\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: PHASE1\nEligibility: Inclusion Criteria:\n\n* Histologically confirmed non-squamous NSCLC, with incurable advanced or metastatic disease\n* Prior genotyping positive for an EGFR activating mutation (L858R, exon 19 deletion, G719X, L861Q)\n* Progression after prior treatment with an EGFR TKI; in addition to this one prior line of therapy, any additional prior lines of therapy are permitted; prior treatment with a third-generation EGFR TKI is allowed for the dose escalation phase, but is not permitted for the expansion cohort\n* Adequate archival tissue from a biopsy performed after progression of disease on previous EGFR TKI; or willing to undergo a new tumor biopsy prior to registration (for the dose escalation portion only this requirement can be waived if T790M status has already been determined using a local assay)\n* For the dose expansion portion only, patient must: 1) have a tumor which is EGFR-T790M positive and 2) be treatment naive to T790M-directed EGFR TKI (e.g. AZD9291, rociletinib, etc); T790M testing may be done locally or centrally on study, but if done locally, tissue must be available for central confirmation\n* Measurable disease per Response Evaluation Criteria in Solid Tumors (RECIST 1.1)\n* Any number of prior therapies are allowed\n* Age \\>= 18 years. NSCLC is exceedingly rare in patients \\< 18 years of age. Because no dosing or adverse event data are currently available on the use of AZD9291 in combination with navitoclax in patients \\< 18 years of age, children are excluded from this study\n* Eastern Cooperative Oncology Group (ECOG) performance status =\\< 1 (Karnofsky \\>= 70%)\n* Patients must have the ability to swallow oral dosage forms\n* Life expectancy of greater than 3 months\n* Leukocytes \\>= 3,000/mcL\n* Absolute neutrophil count \\>= 1,500/mcL\n* Hemoglobin \\>= 8.0 g/dL\n* Platelets \\>= 100,000/mcL\n* Activated partial thromboplastin time (aPTT), prothrombin time (PT) =\\< 1.2 x upper limit of normal (ULN)\n* Total bilirubin =\\< 1.5 x ULN (patients with Gilbert's syndrome may have serum bilirubin \\> 1.5 x ULN)\n* Aspartate aminotransferase (AST) (serum glutamic oxaloacetic transaminase \\[SGOT\\])/alanine aminotransferase (ALT) (serum glutamate pyruvate transaminase \\[SGPT\\]) =\\< 3.0 x institutional ULN\n* Creatinine =\\< 2.0 mg/dL OR\n* Creatinine clearance \\>= 50 mL/min\n* The effects of AZD9291 and navitoclax on the developing human fetus are unknown; for this reason, women of child-bearing potential and men must agree to use adequate contraception using one of the methods listed below prior to study entry, for the duration of study participation, and for 3 months for women and 6 months for men following the date of the last dose of AZD9291 and/or navitoclax:\n\n  * Total abstinence from sexual intercourse (minimum one complete menstrual cycle prior to study drug administration)\n  * Vasectomized male subject or vasectomized partner of female subjects\n  * Hormonal contraceptives (oral, parenteral, transdermal or vaginal ring) for at least 3 months prior to study drug administration; if the subject is currently using a hormonal contraceptive, she should also use a barrier method during this study and for 3 months after study completion\n  * Intrauterine device (IUD)\n  * Double-barrier method: male condom plus diaphragm or vaginal cap with spermicide (contraceptive sponge, jellies or creams)\n  * Additionally, male subjects (including those who are vasectomized) whose partners are pregnant or might be pregnant must agree to use condoms for the duration of the study and 6 months following completion of therapy\n* Women of childbearing potential must have a negative urine pregnancy test within 7 days prior to initiation of treatment; women will be considered not of c",
        "Title: SP Robotic Versus VATS Anatomical Pulmonary Resection for Patients With NSCLC\nOfficial title: Single-POrt Robotic Versus Video-assisted Thoracic Surgery Anatomical Pulmonary Resection for Patients With Non-small Cell Lung Cancer (SPORTS Study): a Single-center, Single-blinded, Randomized Controlled Trial\nConditions: Robotics; Lung Cancer\nBrief summary: Single-POrt Robotic-assisted thoracic surgery versus single-port video-assisted Thoracic Surgery major pulmonary resection for patients with non-small cell lung cancer (SPORTS trial): a single-center, a single blinded, randomized controlled trial\nInterventions: Single-port robotic-assisted thoracic surgery: All patients : 145 patients Single-port anatomical pulmonary resection(segmentectomy, lobectomy) with a complete mediastinal lymph node dissection will be performed using the SP robotic system. A 4-cm single incision will be made below the subcostal margin. A chest tube will be inserted in same incision.; Single-port video-assisted thoracoscopic surgery: All patients : 145 patients Single-port anatomical pulmonary resection(segmentectomy, lobectomy) with a complete mediastinal lymph node dissection will be performed using the VATS. A 4-cm single incision will be made at 5th intercostal space. A chest tube will be inserted in same incision.\nStudy purpose: TREATMENT\nStudy type: INTERVENTIONAL\nPhases: NA\nEligibility: Inclusion Criteria:\n\n* Candidate for anatomical pulmonary resection (segmentectomy or lobectomy) via minimally invasive thoracic surgery (RATS or VATS) for patient with non-small cell lung cancer or suspected malignant lesion.\n* Age ≥ 18 years\n* Patients who can comply with the requirements of the clinical trial and who, or their legal representatives, provide written consent before the start of the clinical trial\n* Patients with the nationality of South Korea\n* American Society of Anesthesiologists score 1-3.\n* Clinical stage I, II or IIIa non-small cell lung cancer (NSCLC)\n\nExclusion Criteria:\n\n* Patients who require surgery for accompanying other organ diseases\n* Tumor invasion into the chest wall, diaphragm, another lobe or diaphragm\n* Patients who are considered unsuitable based on the researcher's judgment\n* Patients with cognitive impairments who are unable to understand the instructions and informed consent of this study\n* Patients who specifically desire a certain surgical method (robotic, thoracoscopic, open thoracotomy)\n* Patients who previously undergone a thoracic surgical procedure in the hemithorax to be operated on\n* Pathological results other than NSCLC (ex, benign nodules, metastatic lung cancer, SCLC)\n* Patients who received neoadjuvant therapy.\n* Candidate for pneumonectomy, bilobectomy, lobectomy plus segmentectomy, non-anatomic resection (ex, wedge resection).\n* History of other cancers in the past 5 years.",
    ]
)
# [{'corpus_id': ..., 'score': ...}, {'corpus_id': ..., 'score': ...}, ...]
```

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Cross Encoder Binary Classification

* Dataset: `clinical_trials_validation`
* Evaluated with [<code>CEBinaryClassificationEvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CEBinaryClassificationEvaluator)

| Metric                | Value      |
|:----------------------|:-----------|
| accuracy              | 0.8847     |
| accuracy_threshold    | 0.3852     |
| f1                    | 0.8592     |
| f1_threshold          | 0.3159     |
| precision             | 0.8714     |
| recall                | 0.8472     |
| **average_precision** | **0.9165** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 1,524 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                       | sentence_1                                                                            | label                                                         |
  |:---------|:---------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type     | string                                                                           | string                                                                                | float                                                         |
  | modality | text                                                                             | text                                                                                  |                                                               |
  | details  | <ul><li>min: 8 tokens</li><li>mean: 9.45 tokens</li><li>max: 13 tokens</li></ul> | <ul><li>min: 148 tokens</li><li>mean: 461.19 tokens</li><li>max: 512 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.5</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                          | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | label            |
  |:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>Find clinical trials for primary lung cancer</code>           | <code>Title: A Study of mRNA-5671/V941 as Monotherapy and in Combination With Pembrolizumab (V941-001)<br>Official title: A Phase 1, Open-Label, Multicenter Study to Assess the Safety and Tolerability of mRNA-5671/V941 as a Monotherapy and in Combination With Pembrolizumab in Participants With KRAS Mutant Advanced or Metastatic Non-Small Cell Lung Cancer, Colorectal Cancer or Pancreatic Adenocarcinoma<br>Conditions: Neoplasms; Carcinoma, Non-Small-Cell Lung; Pancreatic Neoplasms; Colorectal Neoplasms<br>Brief summary: This study will determine the safety and tolerability and establish a preliminary recommended Phase 2 dose of V941(mRNA-5671/V941) as a monotherapy and in combination with pembrolizumab infusion.<br>Interventions: V941: V941 administered IM, Q3W for 9 3-week cycles; Pembrolizumab: Pembrolizumab 200 mg, IV for 35 3-week cycles<br>Study purpose: TREATMENT<br>Study type: INTERVENTIONAL<br>Phases: PHASE1<br>Eligibility: Inclusion Criteria:<br><br>Part 2 Only<br><br>\- Has a histologically confirmed advanced or metast...</code> | <code>1.0</code> |
  | <code>Find lung cancer diagnosis and staging clinical trials</code> | <code>Title: Clearance Of Mucus In Stents (COMIS)<br>Official title: Clearance Of Mucus In Stents (COMIS)<br>Conditions: Lung Neoplasms; Respiratory Failure; Pneumonia; Acute Coronary Syndromes; Unstable Angina; Myocardial Infarction; Cardiac Arrhythmia; Thromboembolic Disease<br>Brief summary: The goal of this clinical research study is to compare the effects of sodium bicarbonate to normal saline when used for clearing mucus blockage in patients with airway stents.<br>Interventions: Normal Saline: Normal saline administered in stent/airway tubes under direct visualization via the bronchoscope.; Sodium Bicarbonate: 4.2% bicarbonate solution mixed with equal volume of sterile water administered into stent/airway tubes under direct visualization via the bronchoscope.<br>Study purpose: DIAGNOSTIC<br>Study type: INTERVENTIONAL<br>Phases: NA<br>Eligibility: Inclusion Criteria:<br><br>1. Adult patients (\>/= 18 years) with airway stents undergoing bronchoscopy.<br>2. Patients previously enrolled, but excluded as no stent lumen o...</code>    | <code>1.0</code> |
  | <code>Find lung cancer chemotherapy clinical trials</code>          | <code>Title: Adjuvant Afatinib in Stage I-III NSCLC With EGFR Mutation<br>Official title: Randomized Phase II Study Comparing Concise Versus Prolonged Afatinib as Adjuvant Therapy for Patients With Resected Stage I-III NSCLC With EGFR Mutation<br>Conditions: Non Small Cell Lung Cancer<br>Brief summary: This research study is a Phase II clinical trial, which tests the safety and effectiveness of an investigational drug to learn whether the drug works in treating a specific cancer. "Investigational" means that the drug is still being studied. It also means that the FDA has not yet approved afatinib for use in patients.<br><br>In this research study the investigators are looking to see if taking afatinib after surgery works better when taken over a short period of time, compared to a long period of time.<br>Interventions: Afatinib<br>Study purpose: TREATMENT<br>Study type: INTERVENTIONAL<br>Phases: PHASE2<br>Eligibility: Inclusion Criteria:<br><br>* Pathologically confirmed diagnosis of non-small cell lung cancer with EGFR mutati...</code> | <code>0.0</code> |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": null
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 16
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `activation_checkpointing`: False
- `activation_checkpointing_kwargs`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 16
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch  | Step | clinical_trials_validation_average_precision |
|:------:|:----:|:--------------------------------------------:|
| 0.5208 | 50   | 0.8805                                       |
| 1.0    | 96   | 0.8991                                       |
| 1.0417 | 100  | 0.8990                                       |
| 1.5625 | 150  | 0.9078                                       |
| 2.0    | 192  | 0.9133                                       |
| 2.0833 | 200  | 0.9134                                       |
| 2.6042 | 250  | 0.9159                                       |
| 3.0    | 288  | 0.9165                                       |


### Training Time
- **Training**: 1.9 hours
- **Evaluation**: 3.9 minutes
- **Total**: 2.0 hours

### Framework Versions
- Python: 3.12.10
- Sentence Transformers: 6.3.0
- Transformers: 5.24.1
- PyTorch: 2.15.0+cpu
- Accelerate: 1.16.0
- Datasets: 5.2.0
- Tokenizers: 0.23.3

## Additional Resources

- [Training and Finetuning Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-reranker): the end-to-end guide for training or finetuning Cross Encoder (reranker) models.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video reranker models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal Cross Encoders.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->