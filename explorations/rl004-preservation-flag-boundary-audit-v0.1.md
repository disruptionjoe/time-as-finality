# RL-004 Preservation-Flag Boundary Audit v0.1

## Status

Exploration / executable boundary note for RL-004: Typed transport and
multiscale transport category. This note is not a claim-status change, lifecycle
move, registry edit, or architecture decision.

## Context Read

- `workflows/registries/line-registry.md`: RL-004 is incubated, active, and
  supports RL-001 and RL-002.
- `workflows/registries/research-line-scorecard.md`: RL-004 has high
  mathematical readiness, high dependency centrality, and low overclaim risk in
  the provisional health substrate.
- `tests/T37-typed-transport-network.md`: path-dependent admissibility is
  witnessed by accumulated forgotten structure.
- `tests/T38-minimal-multiscale-transport.md`: TypedTransportNetwork is the best
  supported current object, while higher category/sheaf machinery remains
  premature.
- `tests/T41-typed-transport-category.md` and
  `results/typed-transport-category-v0.1-results.md`: D1RestrictionMorphisms
  form a category under source, target, site map, and preserved-dimension
  equality, but preservation-flag behavior was listed as uncharacterized.
- `models/transport_network.py`: `_compose_morphisms` constructs composed
  morphisms with `require_trust_path_preservation=False` and
  `require_obstruction_preservation=False`.

## Bounded Audit

Added an executable audit in `models/typed_transport_flag_boundary.py` with
coverage in `tests/test_typed_transport_flag_boundary.py`.

The audit composes morphisms whose preservation requirements are both active:

```text
require_trust_path_preservation=True
require_obstruction_preservation=True
```

It then checks ordinary composition and left/right identity composition.

## Result

Current composition preserves the T41 skeleton:

- source / target;
- site map;
- preserved dimensions.

Current composition does not preserve the active preservation flags:

- `flagged_f ; flagged_g` returns a relaxed composed morphism;
- `id_A ; flagged_f` is skeleton-equal to `flagged_f` but flag-unequal;
- `flagged_f ; id_B` is skeleton-equal to `flagged_f` but flag-unequal.

## Interpretation

T41 remains useful and should not be rolled back. The safer reading is:

```text
D1RestrictionMorphisms form a category at the flag-erased skeleton level.
```

The stronger reading remains unearned:

```text
preservation-constrained D1RestrictionMorphisms form a category when
preservation requirement flags are part of morphism identity.
```

## Why This Matters

RL-004 is a high-leverage support line for RL-001 and RL-002. If later work uses
typed transport as the categorical backbone for restriction, projection, or PO1
claims, it must know whether preservation obligations are mathematical structure
or only analysis-time checks.

This audit prevents a quiet overread of T41 while preserving its current value.

## Deliberately Not Decided

This note does not choose a new semantics for preservation flags. Reasonable
future options include:

- flags compose by conjunction;
- flags compose by disjunction;
- flags are replaced by explicit obligation/evidence objects;
- flags remain analysis-time parameters outside morphism identity.

Choosing among these would be an architecture decision for a later RL-004 run.

## Governance Signal

RL-004 appears underdeveloped relative to its dependency centrality. The signal
is for future line review only: no lifecycle stage, status, registry field, claim
status, or accepted architecture was changed here.

## Recommended Next Move

Define the preservation-obligation semantics explicitly, then rerun identity and
associativity laws with those obligations included in morphism equality.
