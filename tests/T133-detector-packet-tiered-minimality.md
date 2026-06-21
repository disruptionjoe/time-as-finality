# T133: Detector Packet Tiered Minimality

## Route

Quantum measurement / classical records, detector evidence infrastructure only.

## Question

Does the current detector packet really require one flat "all fields at once"
burden, or is the burden tiered into raw evidence preservation, provisional
packet admission, and full detector-claim review?

## Motivation

T121 defined a broad minimal packet and T123 showed that same-payload packets
can split on admissibility and future operation availability. The remaining
ambiguity is whether every packet field is equally necessary at the first
admissibility step. If not, Q1B should state the burden more honestly.

## Setup

- Reuse the T123 same-payload packet family.
- Hold fixed the raw payload, immediate measurement result, and coarse detector
  summary.
- Classify each variant under three tiers:
  - raw evidence preserved;
  - provisionally admissible for packet review;
  - claim-review ready with reconstruction and dispute handling intact.

Tier fields under test:

- raw identity: detector identity, run/session id, causal ordering data, raw
  payload, calibration reference;
- provisional admission core: provenance chain, signatures, authority domains,
  publication status, revocation status, key state, admissibility tokens;
- claim-review extension: witness references, reconstruction paths, challenge
  or dispute state.

## Success Criteria

- At least one field class is shown to block provisional admission.
- At least one field class is shown to preserve provisional admission while
  still blocking full claim review.
- The result weakens overclaim by replacing a flat packet burden with a tiered
  burden if the finite family supports that split.

## Failure Criteria

- Every field is equally necessary already at provisional admission.
- No field beyond raw identity changes claim-review rights.
- The result is described as detector physics or Q1 empirical support.

## Claim Impact

No Q1 promotion. T133 only sharpens how detector-packet burdens should be
stated before any real deployment is allowed to count as evidence.

## Reproduction

```bash
python -m unittest tests.test_detector_packet_tiered_minimality -v
python -m models.run_t133
```
