# T138: Detector Manifest Workflow Fit

## Route

Quantum measurement / classical records, with experimental-discriminator
pressure on detector evidence infrastructure.

## Question

Can the T136 preregistration manifest be filled by a concrete lab workflow
without turning Q1B into post hoc or authority-collapsed self-certification?

## Motivation

T136 made the detector manifest executable but still abstract. The next risk is
that the repo overestimates feasibility: a lab may have good time tags, signed
exports, and calibration records while still failing because the manifest is
assembled after data or because analysis, control design, archive custody, and
trust audit collapse into one authority.

## Setup

T138 adds:

- a human-fillable T136 manifest template;
- a common single-lab photonic coincidence workflow;
- a pre-data single-lab plus public-archive repair;
- a federated pre-data claim-review scaffold;
- an outcome-smuggling control that tries to commit observed payload values
  before the event boundary.

Each workflow is converted into a T136 manifest and audited by the existing
T136 validator.

## Success Criteria

- The common single-lab photonic workflow fails Q1B admission.
- A pre-data public-archive repair still fails if authority domains collapse.
- A federated five-domain preregistration scaffold clears the manifest only as
  a scaffold, not as evidence.
- A manifest that pre-commits observed detector outcomes fails even with clean
  authorities.
- No Q1B promotion or detector-physics claim is made.

## Failure Criteria

- A post hoc or authority-collapsed workflow clears provisional or claim-review
  admission.
- A passing scaffold is described as empirical detector support.
- The raw payload field is allowed to contain observed values before events.
- T138 duplicates T136 logic instead of using the T136 validator.

## Claim Impact

Q1B remains externally blocked and becomes less attractive as an active
quantum-measurement route. The current non-null path is no longer "a lab with
time tags"; it is a federated preregistration scaffold with T136 fields and
T100-compatible authorities fixed before the first detector event. Common
single-lab workflows are null for Q1B.

## Reproduction

```bash
python -m unittest tests.test_detector_manifest_workflow_fit -v
python -m models.run_t138
```
