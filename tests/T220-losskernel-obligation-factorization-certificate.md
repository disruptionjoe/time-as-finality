# T220: LossKernel Witness-Obligation Factorization Certificate

## Route

Mathematical machinery / prior-art separation audit.

## Anchors

- `open-problems/loss-kernel-formalization.md`
- `open-problems/loss-kernel-witness-obligation-normal-form.md`
- `claims/TF1-typed-forgetting-attribution.md`
- `tests/T99-losskernel-quotient-separation.md`
- `tests/T107-loss-relocation.md`
- `tests/T108-loss-relocation-prior-art.md`
- `tests/T127-same-neighbor-data-losskernel-audit.md`
- `papers/typed-loss-kernels-obstruction-attribution-v0.1.md`

## Question

T127 ran the same-neighbor-data promotion gate as a search over a finite
fixture family and returned negative: no fixture pair kept every
neighbor-visible package fixed while changing the LossKernel attribution
verdict. T220 asks the stronger structural question T127 left open:

```text
Is the T127 negative an accident of the chosen fixtures, or is it forced by the
way the canonical witness obligation is derived?
```

If it is forced, then the same-neighbor-data quotient route is closed
structurally, not just empirically, and the honest surviving target is the
canonical witness-obligation normal form rather than a prior-art-separated
obstruction theorem.

## Setup

The T107 -> T127 lineage derives the canonical witness obligation as a
deterministic function of the source-lift judgment table. Let:

```text
nu : Case -> neighbor-visible signature
```

be the realization map that records the data every mature neighbor is allowed
to read (CSP explanation, why-not provenance, abstract interpretation, lenses,
effect annotations, categorical bookkeeping). The lift table, the ordinary
composite map, and the target endpoint behavior are all inside `nu`.

The canonical obligation map is:

```text
obligation : Case -> witness-obligation normal form
```

T220 checks whether `obligation` factors through `nu`:

```text
obligation = psi . nu
```

A map factors through `nu` iff it is constant on every fiber of `nu`. The fibers
of `nu` are exactly the same-neighbor-data equivalence classes. The model
`models/losskernel_obligation_factorization.py` verifies fiber-constancy by
exhaustive finite check, reconstructs the obligation from `nu` alone, probes all
canonical pairs, and builds the one structural escape.

## Positive Control

`mixed_a` and `mixed_b_relabelled` share the full neighbor signature but differ
in their free label and path tag. They receive the same derived obligation and
the same verdict: classification `collapse`. Free decorations do not move the
obligation.

## Negative / Escape Control

`hidden_escape_a` and `hidden_escape_b` are neighbor-identical (uniform-true
lift tables, same composite map, same endpoint behavior) but carry different
hidden source data. Their obligations diverge, so they separate. But the
separation is non-factoring: the obligation reads a source datum no neighbor
package exposes. This is the only way to escape the factorization, and it is not
a prior-art separation: admitting that datum as legitimate audit data enlarges
the neighbor package to `nu'`, and absorption returns one level up.

## Result

The factorization holds.

1. `canonical_factorization_holds = True`: every fiber of `nu` has a constant
   obligation and a constant verdict, so `obligation = psi . nu` on the
   canonical regime.
2. `neighbor_reconstruction_matches = True`: a neighbor handed only `nu(case)`
   recomputes the obligation exactly.
3. `same_neighbor_separation_impossible_in_canonical_regime = True` and
   `strict_separation_found = False`: no pair both shares the neighbor signature
   and separates while factoring through `nu`. The T127 negative is forced, not
   accidental.
4. The hidden-source escape separates (`hidden_escape_separates = True`) only by
   a non-factoring obligation (`hidden_escape_factors_through_neighbor = False`)
   and is therefore not a prior-art separation
   (`hidden_escape_is_prior_art_separation = False`).

This is the collapse theorem requested by
`open-problems/loss-kernel-witness-obligation-normal-form.md`: the
neighbor-visible realization map recovers the obligation object, so LossKernel
collapses into neighbor data on the canonical regime.

## Verdict: narrowed

T220 does not kill TF1, and it does not promote LossKernel. It narrows the
LossKernel sub-target from "prior-art-separated obstruction theorem" to
"certified witness-obligation normal form (collapse-into-neighbor)". The
same-neighbor-data quotient route is closed structurally. The repo should stop
treating that route as a live rescue path for the current canonical derivation.

Consistent with the ROADMAP language guardrails, LossKernel remains "a proposed
typed annotation and attribution object under active prior-art and quotient
testing" and is not called a new mathematical object. The promotion gate is not
cleared.

## Claim Impact

- `TF1` remains `open_formal_target`.
- The default rescue path "same-neighbor-data separation should appear if we
  keep searching" is closed by a factorization certificate, strengthening the
  T127 search-negative into a structural one.
- The strongest surviving value of LossKernel is a canonical, neighbor-
  reconstructible normal form for source-derived witness obligations: an
  audit/integration vocabulary, not a separation theorem.
- No prior-art-separated theorem claim is earned.

## Failure Criteria

T220 is overturned in TF1's favor only by exhibiting an obligation map that
both (a) separates two cases sharing the full neighbor-visible signature `nu`,
and (b) is itself a function of `nu`. The factorization theorem shows these two
requirements are contradictory. A would-be falsifier must instead argue that
some source field used by the obligation is legitimately outside every mature
neighbor package; T108 and T127 already show mature provenance/effect/
abstraction systems absorb any declared source field once it is named.

## Known Physics Constraints

None. T220 is a finite typed-machinery audit. It uses no time, consciousness,
quantum-interpretation, or observer-metaphysics language.

## Reproduction

```bash
python -m unittest tests.test_losskernel_obligation_factorization -v
python -m models.run_t220
```
