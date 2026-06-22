# T171: Detector Row-Review Substitution Screen

## Route

Quantum measurement / classical records, detector evidence infrastructure only.

## Target Claims

- [Q1B: Detector Provenance Admissibility](../claims/Q1B-detector-provenance-admissibility.md)
- [T123: Same-Payload Packet FOA Witness](T123-same-payload-packet-foa-witness.md)
- [T133: Detector Packet Tiered Minimality](T133-detector-packet-tiered-minimality.md)
- [T169: Detector Deployment-Archetype Screen](T169-detector-deployment-archetype-screen.md)

## Question

Within the lone T169 survivor, can proofs, summaries, delayed publication,
sampled rows, or private escrow substitute for reviewable full event-level
rows without losing the claim-review operations Q1B needs?

## Motivation

T169 reduced Q1B to one narrow external candidate:

- pre-data claim-review manifest;
- distinct critical control roots; and
- later reviewable event-level rows.

That last phrase is still loose. A detector group could offer:

- aggregate summaries;
- signed proof certificates;
- private escrow with an auditor statement;
- sampled row publication; or
- delayed full rows after the challenge window closes.

If any of those preserve the same review rights as full row release, Q1B should
state that. If none do, the surviving route becomes sharper and easier to kill.

## Setup

Hold fixed the T169 survivor assumptions:

- pre-data claim-review manifest already frozen;
- critical control roots remain effectively independent; and
- schema drift after collection is disallowed.

Audit six post-data row-release substitutes:

1. `aggregate_summary_only`
2. `signed_proof_certificate_only`
3. `private_escrow_with_auditor_statement`
4. `sampled_public_rows`
5. `delayed_full_rows_after_challenge_window`
6. `reviewable_full_rows_with_independent_escrow`

Track the claim-review operation set:

- `verify_lineage`
- `reconstruct_event`
- `challenge_packet`
- `certify_packet`
- `audit_authority`
- `use_for_detector_claim_review`

## Success Criteria

- Summary-only and proof-only routes are scaffold-only.
- Private escrow without outside row review is scaffold-only.
- Sampled rows and late row release are scaffold-only.
- Only full reviewable rows with independent escrow preserve the full
  claim-review operation set.
- The result remains detector evidence infrastructure, not detector physics or
  Q1 empirical support.

## Failure Criteria

- Any proof-only, summary-only, sampled-row, escrow-only, or delayed-release
  route preserves the same claim-review operations as full reviewable rows.
- The result is described as detector support rather than admissibility
  infrastructure.

## Claim Impact

Q1B remains `externally_blocked`.

Add this sharpening:

```text
Within the surviving T169 federation class, "reviewable rows" must mean the
full bound event-level packet is reviewable during the challenge window with
independent escrow. Proofs, summaries, private escrow, sampled rows, and late
release are scaffold-only substitutes.
```

## Reproduction

```bash
python -m unittest tests.test_detector_row_review_substitution_screen -v
python -m models.run_t171
```
