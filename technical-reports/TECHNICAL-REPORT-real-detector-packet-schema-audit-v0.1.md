# Technical Report: Real Detector Packet Schema Audit v0.1

## Claim Under Test

T121 asks what the detector branch must treat as the evidence object before it
reasons about admissibility. This is not a detector-physics result and not a
Q1 upgrade. It is packet infrastructure.

## Minimal Packet Schema

The packet contains:

- detector identity;
- run/session id;
- timestamp / causal ordering data;
- raw measurement payload;
- calibration reference;
- provenance chain;
- signatures;
- authority domain;
- publication status;
- revocation status;
- key-rotation / key-compromise state;
- witness references;
- reconstruction paths;
- admissibility tokens;
- challenge / dispute status.

## Validator

The validator separates three questions:

```text
raw payload valid?
packet admissible?
future operations still available?
```

This separation is load-bearing. T121 includes cases where the raw payload is
valid but the packet is inadmissible or withheld.

## Finite Cases

| Case | Result |
| --- | --- |
| valid packet | Admissible; full future detector-review operations remain available. |
| missing provenance | Inadmissible; already handled by T87/T97 provenance contract. |
| key compromised | Inadmissible; reveals need for packet-level key-compromise state. |
| revoked authority | Inadmissible; reveals need for revocation registry/check-time state. |
| publication delayed | Inadmissible; already handled by pre-publication/preregistration gates. |
| authority domains collapsed | Inadmissible; already handled by T100 authority-domain lower bound. |
| valid raw data but inadmissible packet | Raw payload remains valid, but signatures, witnesses, paths, and tokens fail. |
| same raw data, different future operation rights | Withheld pending dispute; future claim-review operations are removed. |

## What Fields Are Strictly Necessary?

All declared schema fields are necessary for the minimal packet, but for
different reasons:

- detector identity, run/session id, causal ordering data, raw payload, and
  calibration reference identify the physical run and raw measurement content;
- provenance chain, signatures, authority domains, publication status,
  revocation status, and key state determine admissibility;
- witness references, reconstruction paths, admissibility tokens, and
  challenge/dispute status determine future operation availability over the
  packet.

## Which Failures Change Admissibility?

All negative cases change admissibility. Missing provenance, delayed
publication, collapsed authority domains, missing signatures, missing witness
references, missing reconstruction paths, and missing tokens are mostly covered
by T78/T87/T97/T100. Key compromise, revocation, and challenge lifecycle
require explicit packet-level state.

## Which Failures Change Future Operation Availability?

Every negative case reduces future operations. The cleanest separation is:

```text
same raw data
same detector identity
same calibration reference
open dispute
=> retain raw payload, but withhold detector-claim review operations
```

So FOA changes even when raw data remains valid.

## Which Failures Are Already Handled?

Existing artifacts already cover much of the packet:

- T78/T87: preregistration, raw logs, publication timing, signatures, and
  event-level joinability;
- T97: dry-run packet scaffold, witness/control references, immutable export;
- T100: authority-domain separation;
- T117/T119: reconstruction paths and future operation availability framing.

## Which Failures Reveal Missing Schema Requirements?

Three requirements need explicit packet-level ownership:

- revocation registry and check time;
- key-rotation, key-compromise, and continuity proof state;
- challenge/dispute lifecycle state.

These cannot be left as external governance prose if future detector packets
are to be validated reproducibly.

## Current Strongest Claim

Before detector admissibility can be reasoned about, the evidence object must
include raw payload plus provenance, authority, publication, revocation,
key-state, witness, reconstruction, token, and dispute fields. Valid raw data
alone is insufficient.

## What This Improved

T121 turns scattered detector-protocol requirements into one finite packet
schema with an executable validator. It prevents future runs from treating
raw detector data, signatures, publication, authority, or challenge status as
separate optional context.

## What This Weakened

This weakens detector-side Q1 operationally. A real raw log cannot be
considered admissible merely because it contains detector payload rows. The
packet wrapper is part of the evidence object.

## Claim Impact Recommendation

No Q1 or detector-physics promotion. Treat T121 as infrastructure: a minimal
detector evidence packet object required before D1 scoring or detector-branch
admissibility claims.

## Open Blocker

The packet schema has not yet been integrated into the T97 dry-run packet.
The next live blocker is to wire revocation, key-continuity, and dispute-state
checks into the existing pre-data packet workflow.

## Reproduction

```bash
python -m unittest tests.test_real_detector_packet_schema_audit -v
python -m models.run_t121
```
