# Technical Report: Detector Pre-registration Manifest v0.1

## Claim Under Test

T134 recommended a single pre-registration manifest binding T97 raw-log table
hashes, T121/T133 wrapper fields, T100 authority-domain evidence, and the
claimed tier before the first detector event. T136 asks what that manifest must
contain and which shortcut variants should be rejected.

## Result

Q1B now has a concrete pre-event manifest gate.

```text
T97 table commitments
+ T121/T133 wrapper-field commitments
+ T100 authority partition
+ claimed tier fixed before first event
+ top-level manifest hash
-> strongest certifiable detector-packet tier
```

The manifest freezes schemas, export rules, hashes, authority separation, and
the claimed review tier. It does not freeze detector outcomes before events;
the `raw_measurement_payload` field is committed as an export rule, not as an
observed value.

## Executable Audit

T136 classifies nine manifest shapes.

| Manifest | Verdict | Why |
| --- | --- | --- |
| `complete_claim_review_manifest` | `claim_review` admissible | T97 hashes, all wrapper commitments, authority split, tier, and manifest hash are frozen pre-event |
| `provisional_only_manifest` | `provisional_admission` admissible | provisional core is committed and no stronger tier is claimed |
| `raw_log_only_manifest` | inadmissible for provisional claim | T97 alone lacks provisional wrapper commitments |
| `claim_review_missing_witness_manifest` | overclaim | provisional core is present but witness, reconstruction, and dispute commitments are missing |
| `posthoc_claim_review_manifest` | inadmissible | manifest is not locked before the first event and data boundary |
| `three_domain_authority_manifest` | inadmissible | violates the T100 authority lower bound and trust-auditor independence |
| `deferred_tier_manifest` | inadmissible | refuses to declare the claimed tier pre-data |
| `manifest_hash_mismatch_case` | inadmissible | top-level manifest hash does not bind the declared contents |
| `observed_payload_value_manifest` | inadmissible | claims observed detector values before the event boundary |

## Current Strongest Claim

Q1B remains an externally blocked admissibility protocol. Its strongest current
form is:

```text
A detector deployment may claim only the strongest tier whose T97 table hashes,
T121/T133 wrapper commitments, T100 authority partition, top-level manifest
hash, no-data boundary, and claimed tier were frozen before the first event.
```

This is evidence infrastructure, not detector physics.

## What This Improved

T136 converts the T134 "combined packet" recommendation into an executable
pre-data object. A proposed deployment can now fail before data collection for
specific reasons: missing wrapper commitments, invalid authority partition,
post hoc registration, undeclared tier, hash mismatch, or impossible
pre-knowledge of payload values.

## What This Weakened

This weakens Q1B by eliminating several rescue paths:

1. T97-only raw logs cannot be upgraded to provisional admission.
2. A lab cannot declare claim-review readiness after seeing data.
3. Claim-review readiness requires witness, reconstruction, and dispute-state
   commitments before the run.
4. A manifest that appears to know outcome values before events is invalid;
   only export-rule commitments are admissible pre-data.

## Falsification Condition

T136 fails if a real detector deployment can legitimately claim provisional or
claim-review status without pre-event wrapper-field commitments and authority
evidence, or if the manifest requires actual detector outcomes before events
rather than export-rule commitments.

## Open Blocker

No real lab has signed and frozen a T136 manifest before detector event
collection.

## Claim Ledger Update

Q1B should remain `externally_blocked`. Add T136 as the current pre-event
admissibility gate: detector packet admission now requires a manifest binding
T97 table hashes, T121/T133 wrapper commitments, T100 authority separation, and
the claimed tier. T97-only, post hoc, invalid-authority, deferred-tier, and
pre-known-payload variants are null for the claimed tier.

## Recommended Next Move

Draft a human-fillable T136 manifest template and try to map one specific lab
workflow onto it. If no plausible workflow can sign it pre-data, demote Q1B
below active quantum-measurement work.

## Reproduction

```bash
python -m unittest tests.test_detector_preregistration_manifest -v
python -m models.run_t136
```
