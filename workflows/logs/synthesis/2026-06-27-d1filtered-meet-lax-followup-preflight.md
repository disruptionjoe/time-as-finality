---
document_type: synthesis_preflight
batch_item: fifth_batch_task_10
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_tests: tests/T232-d1cat-filtered-colimit.md, tests/T237-d1filtered-graded-functor.md, tests/T242-compose-meet-total-functor.md
---

# D1Filtered Meet/Lax Follow-Up Preflight

## Scope

This note completes fifth-batch task 10 as a synthesis/preflight artifact. It
does not edit D1Filtered artifacts, TTN, tests, models, results, README,
ROADMAP, or the claim ledger.

The purpose is to freeze the next admissible follow-up after T242: verify lax
coherence and the `J`/`U` bottom relationship without over-reading finite
meet-semilattice totality as general cocompleteness.

## Grounding Readout

Read surfaces used:

- `tests/T232-d1cat-filtered-colimit.md`.
- `tests/T237-d1filtered-graded-functor.md`.
- `tests/T242-compose-meet-total-functor.md`.
- `CLAIM-LEDGER.md` TTN / D1Cat / D1Filtered change-log context.
- `workflows/logs/synthesis/2026-06-27-d1filtered-lax-functor-coherence-gate.md`.
- `workflows/logs/best-next-move/2026-06-27-fifth-10-research-orchestration.md`.

Current baseline:

- T232: `D1FilteredCat` is content-bearing for monotone descending chains; the
  forgetful `U` recovers T228's bare-intersection morphism; general
  cocompleteness at infinity remains open.
- T237: `gr` is strict only on the gr-composable / filtration-nested
  subcategory; original `compose_filtered` is not legality-closed for all legal
  non-nested morphisms.
- T242: totality is reachable only by changing morphism data from descending
  chains to meet-semilattices. On that changed codomain, `gr_semilattice` is
  total and genuinely lax, not strict.
- The existing coherence synthesis records a further boundary: selected
  anchored generator triples may be lax-coherent, but full current category
  coherence against the T237 `mu` is obstructed by off-anchor cases unless a
  repaired fold is named separately.

## Frozen Follow-Up Objects

Use only the finite D1Filtered objects already introduced by T232/T237/T242:

```text
D = {accessible_support, holder_redundancy, branch_support, reversal_cost}
```

Object and morphism names:

```text
D1FilteredCat:
  morphism_data = descending chain filtration of subsets of D
  composition = compose_filtered
  associated_graded = gr
  forgetful_to_D1Cat = U

D1FilteredCat_meet:
  morphism_data = meet-semilattice of preserved-dimension subsets
  composition = compose_meet_semilattice
  associated_graded = gr_semilattice

J:
  chain-as-meet-semilattice embedding

U:
  bottom or bare-intersection forgetful map from D1FilteredCat to D1Cat
```

The next follow-up must not search for a chain-valued total repair. T242 already
gives the boundary:

```text
chain-valued total composition: legal but non-associative
meet-semilattice-valued composition: associative and total, with genuine laxity
```

## Required Checks

### Lax Coherence Pentagon

For composable triples `(f, g, h)` in the meet-semilattice category, declare the
candidate comparison cell:

```text
c_{f,g}: gr_semilattice(f;g) -> mu(gr f, gr g)
```

where `mu` is the T237 schedule fold unless a new fold is explicitly named.

The next run must check:

```text
mu(mu(gr f, gr g), gr h) == mu(gr f, mu(gr g, gr h))
```

and verify that direct and two-step comparison cells agree for the declared
triple class.

Allowed coherence classifications:

```text
strict_on_nested
lax_coherent_on_declared_domain
lax_but_obstructed
comparison_cell_undefined
fold_underdeclared
```

### J/U Section-Bottom Relationship

For each legal chain morphism `m`, check:

```text
bottom(gr_semilattice(J(m))) = U(m).preserved_dimensions
```

For each nested legal chain pair `(f, g)`, check the stronger sub-functor gate:

```text
J(compose_filtered(f,g)) = compose_meet_semilattice(J(f), J(g))
bottom(gr_semilattice(J(compose_filtered(f,g)))) =
  U(compose_filtered(f,g)).preserved_dimensions
```

For non-nested legal chain inputs, do not pretend an original chain-valued
composite exists. T237 showed `compose_filtered(f,g)` can be illegal there; the
meet-semilattice composite is the T242 codomain-change object.

## Acceptance Criteria

This preflight satisfies fifth-batch task 10 if the next artifact:

- Preserves T242's result that totality requires meet-semilattice morphism
  codomain.
- Preserves that `gr_semilattice` is total but genuinely lax on newly legal
  non-nested pairs.
- Does not revive chain-valued total composition after T242's non-associativity
  counterexample.
- Names the lax coherence pentagon as a required next check.
- Names the `J`/`U` section-bottom relationship as a required next check.
- Classifies the declared domain as strict, lax-coherent, lax-but-obstructed,
  comparison-cell-undefined, or fold-underdeclared.
- Keeps general cocompleteness at infinity open.
- Keeps this D1Filtered lane separate from sheaf, cofinality,
  coefficient-aware, kappa, and continuum derived-bridge work.

## Null Or Demotion Conditions

Treat a proposed follow-up as null, demoted, or underdeclared if any of the
following occur:

- It claims a chain-valued total category without addressing T242's explicit
  non-associativity counterexample.
- It calls `gr_semilattice` strict on all non-nested meet-semilattice pairs.
- It states full-category lax functoriality under the old T237 `mu` while
  ignoring known off-anchor comparison-cell failures.
- It silently replaces `mu` without naming the new fold and rerunning controls.
- It treats non-nested chain inputs as if `compose_filtered` were legal.
- It claims `J`/`U` sub-functor recovery outside the original nested legal
  chain domain.
- It promotes finite 4-dimension subset results to general cocompleteness at
  infinity.
- It imports sheaf, cofinality, continuum, physics, geometry, kappa, or MTI
  meaning into the D1Filtered meet/lax lane.

Null result language to preserve:

```text
The D1Filtered follow-up did not clear the meet/lax gate. The safe residue is
T242's finite boundary: totality is available only after changing morphism data
to meet-semilattices, and the resulting associated-graded assignment is total
but genuinely lax, with coherence and J/U bottom recovery still separately
declared checks.
```

## No-Promotion Guardrails

- Do not promote TTN, D1Cat, or D1Filtered status from this preflight.
- Do not claim general cocompleteness at infinity.
- Do not claim a total chain-valued filtered category.
- Do not claim strict functoriality outside the nested/chain subcategory.
- Do not claim a full-category lax functor unless all comparison cells and
  pentagons pass for the declared domain and fold.
- Do not silently replace T237 `mu`; name any repaired fold separately.
- Do not merge this discrete D1Filtered lane with sheaf/cofinality,
  coefficient-aware, kappa, MTI, physics, or continuum lanes.
- Do not edit `README`, `CLAIM-LEDGER`, `ROADMAP`, tests, models, results, or
  open-problem files from this preflight.

## Next Executable Artifact Shape

Recommended next synthesis artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-d1filtered-meet-lax-coherence-and-ju-packet.md
```

Required sections:

```text
declared_domain
fold_definition_mu_or_named_repair
comparison_cell_definition
nested_pair_control
non_nested_pair_control
lax_coherence_pentagon_battery
wrong_association_control
non_vacuity_control
off_anchor_control
J_embedding_definition
U_forgetful_definition
single_morphism_bottom_recovery
nested_composite_bottom_recovery
non_nested_chain_boundary
cocompleteness_guard
lane_separation_guard
allowed_verdict
no_promotion_guardrail_check
```

If later authorized for implementation, use one bounded follow-up screen rather
than a broad refactor:

```text
tests/TXXX-d1filtered-meet-lax-coherence-and-ju.md
models/d1filtered_meet_lax_coherence_and_ju.py
results/d1filtered-meet-lax-coherence-and-ju-v0.1-results.md
```

Do not create those implementation surfaces from this preflight.
