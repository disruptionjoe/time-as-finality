# T123: Same-Payload Packet FOA Witness

## Route

Quantum measurement / classical records, detector evidence infrastructure only.

## Question

Can packet-level structure change future operation availability while leaving
the raw detector payload, immediate measurement result, and coarse detector
summary unchanged?

## Setup

Hold fixed:

- raw measurement payload;
- immediate measurement result;
- coarse detector summary.

Vary only packet fields:

- provenance completeness;
- authority separation;
- signature validity;
- key-compromise status;
- revocation status;
- publication timing;
- witness availability;
- reconstruction path;
- challenge/dispute state.

## Success Criteria

- The reference packet and every negative packet share the same raw payload.
- The immediate measurement result is unchanged across all variants.
- The coarse detector summary is unchanged across all variants.
- At least one packet-level change alters admissibility or future operation
  availability.
- The model reports which operations are removed: reconstruction, challenge,
  certification, lineage verification, claim review, or publication.

## Failure Criteria

- Any variant changes the raw payload, immediate result, or coarse summary.
- The result is treated as Q1 support or detector physics.
- Packet fields are allowed to affect the measurement result itself.

## Claim Impact

No Q1 promotion. T123 is detector evidence infrastructure: raw measurement
sameness does not imply equal packet admissibility or equal future operation
rights.

## Reproduction

```bash
python -m unittest tests.test_same_payload_packet_foa_witness -v
python -m models.run_t123
```
