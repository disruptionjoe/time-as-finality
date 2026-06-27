---
document_type: synthesis_gate
primary_reader: governance
read_pattern: current_state
write_pattern: append
authority: non_authoritative
summarizable: true
source_queue_item: 5
owner_line: RL-004
claim_status_change: none
---

# D1Filtered Lax-Functor Coherence Gate

## Status

Non-authoritative synthesis artifact for queue item 5 in
`workflows/logs/best-next-move/2026-06-27-next-10-research-orchestration.md`.
This file records a gate/protocol and the current finite-witness decision. It
does not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or
open-problem files.

## Read Surfaces

- `ROADMAP.md`: T228, T232, T237, T242 entries.
- `CLAIM-LEDGER.md`: TTN and MMT rows, plus the 2026-06-25 T228/T232/T237/T242
  change-log entries.
- `workflows/registries/line-registry.md`: RL-004 owner-line framing.
- `tests/T228-d1cat-transfinite-colimit-decision.md`.
- `tests/T232-d1cat-filtered-colimit.md`.
- `tests/T237-d1filtered-graded-functor.md`.
- `tests/T242-compose-meet-total-functor.md`.
- `results/d1filtered-graded-functor/T237-results.json`.
- `results/d1filtered-compose-meet/T242-results.json`.
- Available downstream evidence for the named next object:
  `tests/T245-d1filtered-gr-lax-coherence.md`,
  `results/d1filtered-gr-lax-coherence/T245-results.json`, and the associated
  model/test read for gate semantics.

## Gate Verdict

Classification: `lax-but-obstructed` for the full current
`D1FilteredCat_meet` upgrade against T237's `mu`; `lax-coherent` only on the
selected full-top-anchored generator battery.

The strongest safe statement is:

```text
gr_semilattice has coherent, genuinely lax comparison cells on the selected
full-top-anchored finite generator triples. The full-category lax-functor
upgrade is blocked by an off-anchor mu-under-count obstruction. General
cocompleteness at infinity remains open.
```

This preserves the prior verdict chain:

- T228: D1Cat has the descending-chain colimit only in content-free form; no
  general cocompleteness claim.
- T232: D1FilteredCat is content-bearing for monotone-descending chains, and
  `U` recovers the T228 bare-intersection morphism.
- T237: `gr` is strict only on the gr-composable/nested subcategory; it is not
  total for the original chain-valued composition.
- T242: totality is reachable only by changing the morphism codomain from
  chains to meet-semilattices; `gr_semilattice` is total but genuinely lax.
- T245 evidence: anchored pentagons commute, but off-anchor comparison cells
  can fail to exist.

## Formal Protocol

### Objects

Use only the finite D1Filtered lane objects already present in T232/T237/T242:

```text
D = {accessible_support, holder_redundancy, branch_support, reversal_cost}
```

`D1FilteredCat` has chain-valued morphism data: a site map plus a monotone
descending filtration of subsets of `D`.

`D1FilteredCat_meet` has meet-semilattice-valued morphism data: the full
meet-closure of preserved-dimension layers. Composition is
`compose_meet_semilattice`.

The embedding

```text
J: D1FilteredCat -> D1FilteredCat_meet
```

is the chain-as-its-own-meet-closure map (`_from_chain` in the T242/T245 code).

The T232 forgetful functor

```text
U: D1FilteredCat -> D1Cat
```

keeps the bottom/bare-intersection preserved-dimension layer.

### Comparison Cell

For a composable pair `(f,g)` in the meet-semilattice category, the candidate
lax comparison cell is:

```text
c_{f,g}: gr_semilattice(f;g) -> mu(gr f, gr g)
```

where `mu` is imported from T237 as the independent schedule fold.

The cell exists exactly when the source and target record the same dropped
support and the same surviving floor. It is strict exactly when the graded
strata agree as ordered graded data. It is invertible only in the strict case.

### Pentagon Check

For each composable triple `(f,g,h)`, check:

```text
mu(mu(gr f, gr g), gr h) == mu(gr f, mu(gr g, gr h))
```

and verify that the direct cell

```text
gr_semilattice((f;g);h) -> mu(mu(gr f, gr g), gr h)
```

exists and agrees with both whiskered two-step folds.

The anchored finite battery satisfies this protocol: target `mu` associates
strictly, source composition is associative, direct cells exist, and the
pentagons commute.

### J/U Bottom Gate

The bottom-comparison gate is:

```text
bottom(gr_semilattice(J(m))) = U(m).preserved_dimensions
```

for each legal chain morphism `m`.

For nested legal pairs, the stronger sub-functor gate is:

```text
J(compose_filtered(f,g)) = compose_meet_semilattice(J(f), J(g))
bottom(gr_semilattice(J(compose_filtered(f,g)))) =
  U(compose_filtered(f,g)).preserved_dimensions
```

For non-nested legal chain inputs, `compose_filtered(f,g)` is not legal in the
original chain category, so the protocol must not pretend there is an original
chain-valued composite to compare against. The meet-semilattice composite still
exists, but this is the T242 codomain-change object, not a T232 sub-functor
theorem.

## Controls

| Control | Expected result | Current evidence |
| --- | --- | --- |
| Nested full-top triple | Strict/invertible cell; pentagon commutes | T245 `nested_full_succ` |
| Full-top antichain triples | Directed non-invertible cells; pentagons commute | T245 anchored battery |
| Wrong association | Cell rejected; commute test is real | T245 `wrong_association_rejected` |
| Perturbed fold | Harness reports non-commute/cell absence | T245 `non_vacuity_injector` |
| `mu` non-circularity | Semilattice composite is a poset while `mu` is a chain | T242/T245 non-circularity guard |
| Chain-valued total repair | Legal but non-associative, so no chain-valued total category | T242 chain variant |
| Off-anchor triple | Comparison cell absent | T245 `break_hnest_break` and `gnest_break_kn` |
| Non-monotone filtration | Illegal/rejected | T232/T237/T242/T245 honesty boundary |

The explicit off-anchor counterexample is:

```text
(f_break ; h_nest ; g_break)
```

Here `h_nest` has non-full top `{accessible_support, holder_redundancy}` while
`g_break` drops `branch_support`, a dimension absent from that smaller top. The
genuine meet-closure composite records `branch_support` as dropped, but the
T237 `mu` fold does not. The comparison cell therefore fails because dropped
support differs.

## Acceptance Criteria Satisfaction

| Queue acceptance criterion | Satisfaction |
| --- | --- |
| Use T232/T237/T242 definitions without changing verdict language | Satisfied. The synthesis preserves T232 `conditional`, T237 `conditional`, and T242 `conditional`; T245 is read as finite downstream evidence, not as a ledger rewrite. |
| Classify coherence as strict, lax-coherent, lax-but-obstructed, or undefined | Satisfied. Anchored generator battery: `lax-coherent` and genuinely non-strict. Full current category against T237 `mu`: `lax-but-obstructed`. |
| Provide explicit counterexample if obstructed | Satisfied. Off-anchor `break_hnest_break` misses `branch_support`; `gnest_break_kn` misses `reversal_cost`. |
| Keep general cocompleteness at infinity open unless directly proved | Satisfied. This file repeats the T228/T232/T237/T242/T245 guard: finite category only; no cocompleteness-at-infinity claim. |
| Do not import physics, sheaf, or continuum language into the D1Filtered lane | Satisfied. The protocol uses only finite filtrations, meet-semilattices, graded data, comparison cells, and the fixed four-dimension universe. |
| Compare `J` and bottom-composed `gr_semilattice` against T232 `U` | Satisfied as a gate. Individual chain bottom recovery is stated; nested composite recovery is a sub-functor gate; non-nested cases are explicitly outside original chain composition. |

## No-Promotion Guardrails

- No TTN/MMT status change follows from this file.
- Do not state that `gr_semilattice` is a full-category lax functor under the
  current `mu`; the off-anchor obstruction blocks that.
- Do not state pseudofunctor: anchored antichain cells are directed and
  non-invertible.
- Do not state strict functor outside the nested/chain subcategory.
- Do not state general cocompleteness, continuum behavior, physics content,
  sheaf behavior, or geometry-facing meaning.
- Do not replace T237 `mu` silently. A future repair must be named separately,
  likely a top-aware fold such as `mu_top`, and must rerun the same controls.
- Do not claim a completed `J`/`U` sub-functor theorem for non-nested chain
  inputs; the original chain composite is illegal there.

## Durable Next Protocol

A later implementation turn, if authorized, should decide exactly one of:

1. `mu_top` repair: define a top-aware target fold and rerun pairwise,
   pentagon, wrong-association, non-vacuity, and off-anchor controls.
2. `J/U` sub-functor theorem: prove or test bottom recovery on every legal
   chain morphism and on every nested legal composite in the declared finite
   battery.

Either route must leave T228's general cocompleteness guard untouched unless a
separate proof explicitly discharges it.
