# T121: Real Detector Packet Schema Audit

## Route

Quantum measurement / classical records, detector infrastructure only.

## Question

What is the minimal real detector evidence packet object that must exist before
the detector branch can reason about admissibility?

## Motivation

T78, T87, T97, and T100 define pre-registration, event-level raw logs, dry-run
packet scaffolding, and authority-domain separation. They do not yet define one
minimal evidence packet carrying publication, revocation, key-compromise,
witness, reconstruction, admissibility-token, and challenge/dispute state.

T121 defines that object before any D1 scoring or detector-claim reasoning.

## Packet Schema

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

## Finite Cases

1. valid packet;
2. missing provenance;
3. key compromised;
4. revoked authority;
5. publication delayed;
6. authority domains collapsed;
7. valid raw data but inadmissible packet;
8. same raw data, different future operation rights.

## Success Criteria

- The schema is explicit and finite.
- The validator separates raw-payload validity from packet admissibility.
- Each negative case identifies whether admissibility changes, FOA changes, or
  both.
- Existing detector protocol artifacts absorb already-covered failures.
- Missing packet-level requirements are identified without promoting Q1.

## Failure Criteria

- Valid raw detector data is treated as enough for admissibility.
- Revocation, key-compromise, publication, challenge, or authority state is
  omitted from the packet.
- The result is described as detector evidence or Q1 support.

## Claim Impact

No Q1 or detector-physics promotion. T121 is infrastructure: a minimal
evidence packet object required before D1 scoring or detector-branch
admissibility claims.

## Reproduction

```bash
python -m unittest tests.test_real_detector_packet_schema_audit -v
python -m models.run_t121
```
