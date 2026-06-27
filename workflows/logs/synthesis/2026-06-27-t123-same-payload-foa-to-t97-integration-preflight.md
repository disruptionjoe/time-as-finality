---
document_type: synthesis_preflight
batch_item: sixth_15_task_4
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# T123 Same-Payload FOA To T97 Integration Preflight

## Status

Preflight only. This note identifies the integration path from the T123 witness
into detector packet schemas. It does not promote Q1 or Q1B.

## Sources read

- `tests/T123-same-payload-packet-foa-witness.md`
- `tests/T171-detector-row-review-substitution-screen.md`
- Existing Q1B synthesis notes under `workflows/logs/synthesis/`

## Plain-English finding

Two detector packets can contain the same raw measurement and the same coarse
result while still giving different future rights. The difference lives in
packet provenance, authority, signatures, challenge state, and reconstruction
paths.

## Technical conclusion

T123 should be integrated into the T97-style detector packet family as a
future-operation-availability witness. The raw payload, immediate measurement
result, and coarse detector summary stay fixed. Only packet fields vary:

- provenance completeness;
- authority separation;
- signature and key state;
- revocation status;
- publication timing;
- witness availability;
- reconstruction path;
- challenge/dispute state.

The resulting operation losses are packet-level losses: reconstruction,
challenge, certification, lineage verification, claim review, or publication.
They are not detector-physics differences.

## Minimum next task

Add a packet-template field or result block that records which future operations
are removed by each packet-level defect while asserting raw-payload equality.

## Stop condition

Stop the integration if a fixture changes the raw payload, measurement result,
or coarse detector summary, or if the result is described as empirical Q1
support rather than admissibility infrastructure.

