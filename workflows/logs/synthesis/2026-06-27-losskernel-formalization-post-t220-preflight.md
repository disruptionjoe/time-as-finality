---
document_type: synthesis_preflight
primary_reader: governance
read_pattern: current_state
write_pattern: append
authority: non_authoritative
summarizable: true
source_queue_item: fifth_batch_1
claim_status_change: none
---

# LossKernel Formalization Post-T220 Preflight

## Status

Non-authoritative preflight artifact for fifth-batch task 1. This file does
not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or
open-problem files. It is not TF1 promotion, not a theorem, not prior-art
separation, and not public-facing novelty language.

## Read Surfaces

- `open-problems/loss-kernel-formalization.md`.
- `open-problems/loss-kernel-witness-obligation-normal-form.md`.
- `CLAIM-LEDGER.md`: TF1 row and T99/T108/T127/T220 context.
- Existing synthesis checklist:
  `workflows/logs/synthesis/2026-06-27-losskernel-normal-form-integration-checklist.md`.

## Preflight Verdict

Current classification:

```text
LossKernel remains an open TF1 formal target only in a narrowed,
non-promotional recast.
```

Post-T220, the canonical witness obligation factors through the
neighbor-visible data map:

```text
obligation = psi . nu
```

That makes the canonical object constant on each `nu` fiber. The
same-neighbor-data novelty route is therefore retired for the canonical
construction. A formalization may still be useful as typed integration
vocabulary, but it cannot be presented as a prior-art-separated theorem unless
a later artifact supplies a non-factoring source object and shows that mature
neighbors cannot absorb it even after it is named.

## Formalization Boundary

The post-T220 LossKernel target should separate two roles.

| Role | Safe use | Blocked use |
| --- | --- | --- |
| Typed annotation value | A checkable vocabulary for source/target structures, lost types, witness obligations, and admissibility review. | A claim that the annotation is already a new mathematical obstruction object. |
| Composition bookkeeping | A finite-family law such as powerset-union accumulation, unless a stronger law is proved. | A categorical kernel, universal property, congruence, or theorem-level law by default. |
| Witness obligation review | A way to normalize source-derived audit duties and expose absorber ownership. | A prior-art-separated attribution theorem without quotient survival. |
| Path-dependence explanation | A disciplined restatement of known T34/T37 path cases. | A novelty claim if the same verdict is already recoverable from CSP, provenance, effects, lenses, or abstraction data. |

## Useful Integration Vocabulary

A useful non-promotional artifact may define `LossKernel(f)` as a typed packet
with these fields:

| Field | Required content |
| --- | --- |
| `morphism_id` | The projection or typed transport being audited. |
| `source_structure` | Source object and admissible structure before projection. |
| `target_structure` | Target object and target-side judgment family. |
| `lost_types` | Typed kinds of structure removed by the map. |
| `lost_witnesses` | Source-side witnesses or constraints no longer visible at the target. |
| `preserved_types` | Structure still visible after the map. |
| `obligation_generators` | Derived witness duties needed to settle the target judgment. |
| `neighbor_absorber_map` | CSP, provenance, why-not provenance, abstract interpretation, lens, or effect account that sees the same duty. |
| `composition_rule` | Explicit law used in the finite family, with scope and null cases. |
| `absorbed_vs_live` | Classification as absorbed, audit-useful, or live only under a named escape gate. |

This vocabulary is valuable if it makes admissibility review easier, exposes
where absorber data are being used, and prevents label-only loss from being
mistaken for theorem-level work.

## Non-Factoring Admission Gate

A later artifact may test a non-factoring route only if it freezes all of the
following before selecting the witness pair:

- A named source object or relation not reconstructible from the frozen
  `nu` signature.
- A task-natural target judgment and comparison relation.
- Same endpoints, same composite map, same endpoint satisfiability behavior,
  and same admitted neighbor-visible data across the candidate pair.
- A repeatable derivation rule for the obligation, not prose metadata.
- An explicit attempt to enlarge the neighbor package to `nu_prime` by
  admitting the named source field.
- A survival check showing the split remains after CSP, provenance, why-not
  provenance, abstract interpretation, lenses, effects, path data, and
  category data receive `nu_prime`.
- A negative control where the harness correctly reports collapse when the
  source field is absorbed.

Failing any item keeps the result in integration-vocabulary territory.

## Acceptance Criteria

| Criterion | Preflight handling |
| --- | --- |
| Separates typed annotation value from prior-art-separated theorem language. | The Formalization Boundary table distinguishes safe audit use from blocked theorem use. |
| States the post-T220 demotion burden. | The verdict states `obligation = psi . nu` and same-neighbor-data collapse in the canonical construction. |
| Names what would count as useful integration vocabulary. | The Useful Integration Vocabulary table freezes a non-promotional packet shape. |
| Blocks same-neighbor-data novelty revival without a non-factoring source object that neighbors cannot absorb. | The Non-Factoring Admission Gate requires a named source field and a failed `nu_prime` absorption attempt. |

## Null Or Demotion Conditions

Treat a proposed LossKernel formalization as null or demoted if any condition
holds:

- `LossKernel(f)` is only renamed `forgotten_structure`.
- Lost structure is an author-chosen label set with no derived witness
  obligation.
- The best law is only union accumulation and no stronger semantic role is
  claimed or needed.
- The target verdict is recoverable from CSP, provenance, why-not provenance,
  abstract interpretation, lenses, effects, path data, or category data once
  the same inputs are granted.
- Path dependence disappears after endpoints, composite map, endpoint behavior,
  and admitted neighbor data are matched.
- The object cannot express absorbed-obstruction or recovery cases without ad
  hoc exceptions.
- A hidden source field produces a split only until that field is admitted to
  a mature neighbor package.
- The artifact drops finite-family, constructed-fixture, or
  absorber-admissibility scope guards.

## No-Promotion Guardrails

- Do not change TF1 out of `open_formal_target`.
- Do not call LossKernel a prior-art-separated obstruction theorem.
- Do not treat same-neighbor-data separation as a live novelty route for the
  canonical construction.
- Do not cite T220 as an impossibility theorem for all future formulations.
- Do not promote a hidden-source split before the `nu_prime` absorption attempt
  is run.
- Do not edit ledger, roadmap, tests, models, results, or open problems from
  this preflight.

## Next Executable Artifact Shape

The next artifact should be a single finite formalization packet:

```text
artifact_type: losskernel_formalization_packet
morphism_id:
source_structure:
target_structure:
target_judgment:
nu_signature:
losskernel_fields:
  lost_types:
  lost_witnesses:
  preserved_types:
  obligation_generators:
composition_rule:
identity_case:
path_cases:
neighbor_absorber_map:
same_neighbor_data_check:
non_factoring_source_object:
nu_prime_absorption_attempt:
negative_control:
verdict: integration_vocabulary | absorbed | admit_for_later_escape_audit
claim_impact: no_status_change
```

The executable packet may justify a cleaner audit workflow. It may not update
claim status without a later hostile absorber run.
