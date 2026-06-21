# Technical Report: Same-Payload Packet FOA Witness v0.1

## Claim Under Test

T123 asks whether two detector evidence packets can have the same raw
measurement payload, same immediate measurement result, and same coarse
detector summary while differing in admissibility, reconstruction, challenge,
certification, or future operation availability.

This is not a detector-physics result and not a Q1 upgrade. It is detector
evidence infrastructure.

## Fixed Measurement View

The model fixes the raw payload:

```text
event:e1:+, event:e2:-, event:e3:+, event:e4:-
```

The immediate result is fixed:

```text
plus=2;minus=2;balance=0
```

The coarse detector summary is also fixed: detector identity, run/session id,
calibration reference, event count, plus count, and minus count.

## Packet Variants

The reference packet is schema-complete and has full future operation
availability. Same-payload variants then alter only packet wrapper fields:

- missing provenance;
- collapsed authority separation;
- invalid signature;
- compromised signing key;
- revoked authority;
- delayed publication;
- missing witnesses;
- missing reconstruction paths;
- open challenge/dispute state.

Every variant preserves the same raw payload, same immediate result, and same
coarse summary.

## Result

Yes. Packet-level structure changes future operation availability while the raw
measurement result is unchanged.

The reference packet preserves:

```text
read_immediate_result
retain_raw_payload
score_admissibility
verify_lineage
reconstruct_event
challenge_packet
certify_packet
publish_packet
bind_calibration
audit_authority
use_for_detector_claim_review
```

Inadmissible same-payload packets preserve only:

```text
read_immediate_result
retain_raw_payload
```

The open-challenge packet is withheld rather than raw-invalid. It preserves
raw reading and evidence preservation, but removes certification and detector
claim-review operations until dispute resolution.

## Current Strongest Claim

Same raw detector payload and same immediate result do not determine future
operation availability. Provenance completeness, authority separation,
signature validity, key-compromise status, revocation status, publication
timing, witness availability, reconstruction paths, and challenge state are
part of the evidence object for future operations.

## What This Improved

T123 sharpens T121 from "valid raw payload is insufficient" to a stricter
matched-payload witness:

```text
same raw payload
same measurement result
same coarse detector summary
different packet wrapper
different future operation availability
```

That makes the detector infrastructure requirement more difficult to dismiss
as a raw-data-quality issue.

## What This Weakened

This further weakens detector-side Q1 operationally. Even a real raw detector
payload with a stable immediate result cannot be used for detector-branch
claim review unless the packet wrapper preserves the relevant future
operations.

## Claim Impact Note

No Q1 or detector-physics promotion. T123 is detector evidence infrastructure:
raw measurement sameness does not imply equal packet admissibility or equal
future operation rights.

## Falsification Condition

T123's same-payload FOA split is falsified if packet protocols declare that
admissibility, reconstruction, challenge, certification, and claim-review
rights are functions only of raw payload, immediate measurement result, and
coarse detector summary. Such a protocol would also abandon the
T78/T87/T97/T100/T121 evidence requirements.

## Open Blocker

The audit is still schema-level. It must be integrated into the T97 dry-run
packet and then populated by a real pre-registered detector deployment before
any detector branch can be evaluated.

## Reproduction

```bash
python -m unittest tests.test_same_payload_packet_foa_witness -v
python -m models.run_t123
```
