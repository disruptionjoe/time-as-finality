# Technical Report: Detector Manifest Workflow Fit v0.1

## Claim Under Test

T136 says a detector deployment needs one pre-event manifest binding T97 table
hashes, T121/T133 wrapper commitments, T100 authority separation, the claimed
tier, the no-data boundary, and a top-level manifest hash.

T138 asks the operational follow-up:

```text
Can one concrete lab workflow fill that manifest before detector events without
post hoc assembly or authority-collapsed self-certification?
```

## Result

The common single-lab route is null for Q1B.

A typical photonic coincidence workflow can have time tags, calibration notes,
signed exports, and local provenance while still failing T136 if the review
packet is assembled after data or if one lab authority owns analysis,
instrument operation, control design, archive custody, and trust audit.

The smallest survivor in this audit is not a detector prediction. It is a
federated pre-data scaffold:

```text
T136 manifest fields
+ T97 table hashes
+ T121/T133 wrapper commitments
+ T100-compatible independent authority domains
+ export-rule payload commitment
+ pre-event top-level hash
-> claim-review scaffold fit
```

That scaffold is still not evidence. It only says a future run would be
reviewable if real event rows later populate the frozen packet without changing
schema, tier, authority, or wrapper policy.

## Human-Fillable Template

T138 reduces the manifest to the following reviewer-facing fills:

| Section | Required fill |
| --- | --- |
| `run_identity` | run id, claimed tier, first-event lower bound |
| `t97_tables` | schema hash and empty-export checksum for every T97 table |
| `authority` | at least four T100-compatible domains with independent trust audit |
| `wrapper` | T121/T133 provisional fields and, for claim review, witness/reconstruction/challenge fields |
| `payload_boundary` | export-rule commitment for `raw_measurement_payload`, never observed values |
| `integrity` | top-level hash binding the manifest contents |

## Workflow Audits

| Workflow | Verdict | Reason |
| --- | --- | --- |
| `common_single_lab_photonic_coincidence_workflow` | null for Q1B | post hoc boundary plus authority collapse; missing provisional and claim-review fields |
| `predata_single_lab_with_public_archive_workflow` | null for Q1B | wrapper and timing are repaired, but the T100 authority partition still fails |
| `federated_predata_claim_review_workflow` | claim-review scaffold fit | clears T136 only as a pre-data scaffold; no real rows or detector support |
| `federated_but_preknown_payload_workflow` | null for Q1B | tries to commit observed payload values before the event boundary |

## Current Strongest Claim

Q1B is an evidence-admissibility protocol whose active detector route is now
strictly organizational:

```text
Only a federated, pre-data, T136-signed detector workflow can remain non-null.
Single-lab or authority-collapsed workflows do not support Q1B, even with good
timing hardware and signed raw exports.
```

## What This Improved

T138 makes the T136 gate human-fillable and workflow-facing. A reviewer can now
ask a detector group for a concrete manifest before the run and reject the
route without waiting for detector outcomes.

## What This Weakened Or Falsified

This weakens the detector-provenance branch. The route is not "find a detector
stack with accurate event timing." It is "find an organization willing to sign
independent analysis, control, archive, and audit commitments before data."

The common single-lab route is falsified for Q1B unless it adds real
independent authority domains before event collection.

## Boundary Of The Result

T138 does not prove that a real detector deployment is impossible. It shows
that the repo's current admissibility protocol cannot be honestly instantiated
by ordinary post hoc or role-collapsed workflows.

The federated positive case is deliberately only a scaffold. It does not fill
event rows, score D1, test quantum mechanics, or distinguish Time as Finality
from Quantum Darwinism.

## Falsification Condition

T138 fails if a common single-lab or three-domain workflow can legitimately
claim provisional or claim-review status without the T100-compatible authority
split, or if the federated scaffold cannot actually be signed before data
despite satisfying every manifest field.

## Open Blocker

No named real lab has agreed to fill and sign the federated T138/T136 template
before detector event collection.

## Claim Ledger Update

Q1B should remain `externally_blocked`. Add T138 as a workflow-fit gate:
the human-fillable manifest template rejects the common single-lab photonic
workflow and a public-archive repair with merged authorities. Only a federated
pre-data scaffold clears T136, and even that is not detector evidence until
real rows populate the bound packet.

## Recommended Next Move

Send the T138 template to one realistic detector group or map one named public
experiment against it. If the group cannot provide independent archive and
trust-audit roles pre-data, demote Q1B below active quantum-measurement work.

## Reproduction

```bash
python -m unittest tests.test_detector_manifest_workflow_fit -v
python -m models.run_t138
```
