# T136: Detector Pre-registration Manifest

## Route

Quantum measurement / classical records, with experimental-discriminator
pressure on detector evidence infrastructure.

## Question

What must be frozen before detector event collection so that a future Q1B
packet can honestly claim raw-log preservation, provisional admission, or
claim-review readiness?

## Motivation

T134 showed that T97 raw-log rows are necessary but not sufficient. The next
risk is a post hoc tier upgrade: a lab could freeze T97 tables, collect data,
then add wrapper fields, authority evidence, or a stronger claimed tier after
seeing the run. T136 blocks that move by defining the pre-event manifest object.

The manifest must not require impossible knowledge of detector outcomes before
the run. It must freeze export rules, schemas, hashes, wrapper-field
commitments, authority separation, and the claimed tier.

## Setup

The audit composes:

- the T97 table-hash scaffold;
- the T121/T133 wrapper-field requirements;
- the T100 authority-domain lower bound;
- an explicit claimed tier: `raw_log_preservation`,
  `provisional_admission`, or `claim_review`.

## Success Criteria

- A complete manifest clears the claim-review gate.
- An honest provisional manifest clears provisional admission without claiming
  claim-review readiness.
- A T97-only manifest cannot claim provisional admission.
- A manifest missing witness, reconstruction, or dispute commitments cannot
  claim review readiness.
- Post hoc, invalid-authority, undeclared-tier, hash-mismatch, and
  pre-known-payload variants fail.
- The result does not upgrade Q1B or claim detector physics.

## Failure Criteria

- The manifest demands actual detector outcome values before the first event.
- A lab can claim a stronger tier after data without a pre-event declaration.
- T97-only rows clear provisional admission.
- A three-domain or self-audited authority partition passes the gate.

## Claim Impact

No Q1B promotion. T136 makes the detector branch more falsifiable: a real
deployment must publish one pre-event manifest binding T97 table hashes,
T121/T133 wrapper commitments, T100 authority separation, and the claimed tier.
Without that manifest, the detector route is null for the claimed tier.

## Reproduction

```bash
python -m unittest tests.test_detector_preregistration_manifest -v
python -m models.run_t136
```
