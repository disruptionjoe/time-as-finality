# Technical Report: Detector Packet Tiered Minimality v0.1

## Claim Under Test

T121 and T123 made the detector packet broad and load-bearing, but they still
left one ambiguity: whether every packet field is equally necessary at the
first admissibility step. T133 tests that directly on the same-payload packet
family.

## Result

The current detector packet burden is tiered, not flat.

The finite family supports three distinct levels:

```text
raw evidence preserved
provisionally admissible for review
claim-review ready with reconstruction and dispute handling
```

Under this split:

- provenance chain, signatures, authority domains, publication status,
  revocation status, key state, and admissibility tokens form the
  provisional-admission core;
- witness references, reconstruction paths, and challenge/dispute state are
  additional claim-review requirements;
- raw payload sameness remains weaker than either tier.

## Finite Witness Family

T133 reuses T123's same-payload variants. Every case keeps fixed:

- raw detector payload;
- immediate measurement result;
- coarse detector summary.

Only packet wrapper fields vary.

## Tier Matrix

| Variant class | Raw preserved | Provisionally admissible | Claim-review ready |
| --- | --- | --- | --- |
| missing provenance / invalid signatures / authority collapse / publication delay / revocation / key compromise | yes | no | no |
| missing witnesses | yes | yes | no |
| missing reconstruction paths | yes | yes | no |
| open challenge / dispute | yes | yes | no |
| reference packet | yes | yes | yes |

This is the main result. The packet burden is not one undifferentiated wall.

## What This Improved

T133 makes Q1B easier to evaluate honestly. A reviewer can now ask two
separate questions:

1. did the lab freeze enough packet structure to admit the run for review?
2. did it freeze enough additional structure to support full claim review,
   reconstruction, and challenge resolution?

That is a cleaner and more falsifiable burden than "all packet fields are
equally necessary immediately."

## What This Weakened

T133 weakens the flat reading of T121. The broad packet remains important, but
its fields do different jobs. The current detector branch should not present
witness references, reconstruction paths, and dispute state as if they were
the same kind of prerequisite as provenance, signatures, authority separation,
publication timing, revocation, or key integrity.

## Current Strongest Claim

Detector-side Q1 remains externally blocked, but its packet burden can now be
stated more precisely:

```text
Q1B requires a provisional-admission core for any review at all, plus a
claim-review extension for reconstruction, certification, and dispute-ready
detector claims.
```

This is still detector evidence infrastructure, not detector physics.

## Falsification Condition

T133 fails if either of the following occurs:

1. witness references, reconstruction paths, or challenge state can be removed
   while full claim-review rights remain intact; or
2. provenance, signature, authority, publication, revocation, and key-state
   failures no longer block even provisional packet admission.

## Open Blocker

The tier split is still synthetic. The T97 dry-run packet does not yet expose
separate provisional-admission and claim-review outputs, and no real detector
deployment freezes those tiers before data collection.

## Recommended Next

Refactor T97 so the packet emits explicit tier verdicts:

- raw evidence preserved;
- provisionally admitted;
- claim-review ready.

Then require any future real deployment to pre-register which tier it is
claiming before event collection begins.

## Reproduction

```bash
python -m unittest tests.test_detector_packet_tiered_minimality -v
python -m models.run_t133
```
