# T521: Detector Manifest Template Gate

## Target Claims

No claim-ledger target. This is the executable follow-up to T136's recommended
next step: make the pre-event detector manifest human-fillable while preserving
the T136 gates. It touches Q1B only as review infrastructure and does not move
Q1B, D1, detector evidence, public posture, or claim status.

## Setup

Treat `templates/detector-preregistration-manifest.template.md` as the artifact
under test. The gate checks that the template contains:

- every T97 raw-log table commitment;
- every T121/T133 wrapper field commitment;
- the T136 commitment kinds for export-rule, state, and schema commitments;
- every T100 authority domain;
- exactly the allowed claimed-tier choices;
- a no-data pre-event boundary that forbids observed detector payload values.

## Success Criteria

The template passes only if it can support the T136 claim-review manifest shape
without post hoc schema, authority, tier, wrapper-policy, or payload-value
changes. The raw payload and causal-order fields must be export-rule
commitments, not observed-value commitments.

## Failure Criteria

Fail if any required table, wrapper field, authority domain, or tier choice is
missing; if any wrapper field has the wrong commitment kind; if the pre-data
boundary is absent; or if the template includes `observed_value_commitment`.

## Known Physics Constraints

None. This is detector packet infrastructure, not detector physics or a Q1
upgrade.

## Verdict

`DETECTOR_MANIFEST_TEMPLATE_GATE_BUILT_REVIEW_ONLY`. The template covers all T97
tables, all T121/T133 wrapper fields, all T100 authority domains, all T136 tier
choices, and the no-observed-payload pre-data boundary. It remains a review
artifact only: no detector evidence, Q1B movement, claim-ledger movement, public
posture movement, external publication, or observed payload value commitment.

## Contribution Needed

A future real deployment would need a signed pre-event manifest filled from this
template and then real detector event rows collected under the frozen packet. That
external deployment remains outside this repo-local run.
