---
document_type: registry
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: canonical
summarizable: false
---

# Foundation Queue

Inbound reading and concept queue for `explore/foundation-ingestion`. Foundation
work is exploration: it expands the search space. Items flow
`proposed → ingested → noted`, with `noted` items linking to a durable note in
`literature/` or `papers/`.

> **Seed note (Phase 2, Session 4).** Existing known-neighbor notes are listed as
> already `noted`; a few `proposed` items seed the new coverage areas.

## Noted (already ingested into the repo)

| item | note location |
|---|---|
| Known neighbors (core) | `literature/N1-known-neighbors.md` |
| Hoffman interface theory & trace logic | `literature/N2-hoffman-interface-theory-and-trace-logic.md` |
| Core formalism known neighbors | `literature/N3-core-formalism-known-neighbors.md` |
| Emergence-lab known neighbors | `literature/N4-emergence-lab-known-neighbors.md` |
| Signed-readout anchors | `literature/N6-signed-readout-anchors.md` |
| Distinguishing predictions | `literature/distinguishing-predictions.md` |
| Records / finality / readout separation | `papers/records-finality-readout-separation-v0.1.md` |

## Proposed (not yet ingested)

| item | why it may matter | target cluster |
|---|---|---|
| Interest management / relevance filtering in MMO netcode | bandwidth-bounded observer access to records; "what survives the relevance filter" as a finality analogue | simulation/MMO/game-mechanism |
| Virtual-economy ledger/settlement design | record stabilization and irreversibility under bounded trust | distributed-systems/consensus |
| Distributed-simulation time models (e.g. conservative/optimistic synchronization) | local commit order vs global reconciliation; maps to no-global-commit-order | distributed-systems/consensus |
| (add as discovered) | | |

## How this queue is maintained

`explore/foundation-ingestion` pulls the next `proposed` item(s), writes a note,
flips status to `noted`, and may flag new personas (to `persona-clusters`), new
tests (`tests/`), or challenges to existing claims.
