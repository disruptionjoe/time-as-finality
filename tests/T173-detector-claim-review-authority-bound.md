# T173: Detector Claim-Review Authority Bound

## Route

Quantum measurement / classical records, detector evidence infrastructure only.

## Target Claims

- [Q1B: Detector Provenance Admissibility](../claims/Q1B-detector-provenance-admissibility.md)
- [T100: Detector Authority-Domain Bound](T100-detector-authority-domain-bound.md)
- [T161: Detector Control-Root Independence](T161-detector-control-root-independence.md)
- [T171: Detector Row-Review Substitution Screen](T171-detector-row-review-substitution-screen.md)

## Question

Does T171's surviving claim-review route still fit inside T100's four-domain
lower bound, or does independent escrow raise the exact authority requirement?

## Motivation

T100 proved a four-domain lower bound for the older T97/T98 packet. T171 then
made the only live Q1B route stricter: the full bound event rows must be
reviewable during the challenge window with independent escrow.

That phrase should carry operational weight. If independent escrow is real,
not rhetorical, then the surviving route may need an extra authority domain
beyond T100's pre-escrow packet.

## Setup

- Extend the T100 partition audit from five domains to six:
  - `analysis_governor`
  - `instrument_operator`
  - `control_designer`
  - `archive_custodian`
  - `trust_auditor`
  - `escrow_custodian`
- Keep the T100 constraints:
  - trust auditor must remain independent;
  - governance, control design, and archive custody cannot merge.
- Add the T171 constraint:
  - escrow custodian must remain independent of every other domain if the
    route is to preserve outside challenge rights rather than collapse into
    archive control, governance control, instrument self-release, or
    `private_escrow_with_auditor_statement`.
- Enumerate every six-domain set partition and find the exact minimum.

## Success Criteria

- No four-domain claim-review profile survives once escrow independence is
  included.
- The exact minimum authority count is identified.
- The surviving minimal merge classes are listed explicitly.
- The result is stated as an operational obstruction on detector evidence
  infrastructure, not detector physics.

## Failure Criteria

- "Independent escrow" is treated as a slogan with no operational separation.
- The result merely repeats T100's four-domain bound.
- A trust-auditor-plus-escrow or archive-plus-escrow merge is allowed despite
  T171's scaffold-only classifications.

## Claim Impact

Q1B remains `externally_blocked`.

Add this sharpening:

```text
T100's four-domain lower bound is insufficient for the only surviving T171
claim-review route. Once independent escrow is treated as a real authority
burden, the exact lower bound rises to five authority domains.
```

## Reproduction

```bash
python -m unittest tests.test_detector_claim_review_authority_bound -v
python -m models.run_t173
```
