# Technical Report: Loss Relocation Prior-Art Audit v0.1

## Claim Under Test

T108 asks whether T107 source-fiber loss relocation separates from five nearby
formal families:

- why-not provenance;
- abstract interpretation;
- lenses;
- CSP explanation;
- effect annotations.

## Result

No strict separation is earned yet.

Given the same source fiber and target judgment relation, each named family can
absorb the current finite behavior, at least in a rich enough version. The
surviving delta is not a new obstruction mechanism. It is a possible typed
normal form for source-derived witness obligations under projection.

## Neighbor Verdicts

| Neighbor | Verdict | Reason |
| --- | --- | --- |
| why-not provenance | absorbed except taxonomy | Mixed source-lift verdicts can be reported as missing witnesses or missing derivation choices. |
| abstract interpretation | absorbed | The source fiber is a concretization set; mixed verdicts are loss of precision and uniform verdicts are sound abstract judgments. |
| lenses | absorbed | The target is a view and the forgotten source fiber is complement/update information. |
| CSP explanation | absorbed | Mixed lift verdicts are ambiguity over solutions; uniformly forbidden lifts are conflicts. |
| effect annotations | absorbed by rich effects, not label-only effects | Label-only effects fail, but witness-carrying effects can encode the same obligations. |

## Current Strongest Claim

Source-fiber loss relocation is a useful audit normal form, not yet a
prior-art-separated mathematical object.

The most defensible TF1 claim is now:

```text
LossKernel may become useful as a typed normal form that packages source-fiber
witness obligations for projection-created reconstruction debt. It is not yet
known to express anything unavailable to why-not provenance, abstract
interpretation, lenses, CSP explanation, or rich effect annotations.
```

## What This Improved

T108 prevents premature theorem language. It identifies the real burden:

```text
same neighbor data, different LossKernel attribution verdict
```

Without that quotient witness, TF1 should remain an open formal target.

## What This Weakened Or Falsified

T108 weakens T107's novelty reading. Source-fiber dependence is not by itself
new. In mature language it is close to:

- concretization under abstraction;
- view complement under lenses;
- missing derivation or why-not explanation;
- solution/conflict structure in CSP;
- witness-carrying effect annotation.

This does not make T107 useless. It makes it an integration and normal-form
candidate rather than a separation theorem.

## Falsification Condition

T108 fails in TF1's favor only if a future fixture has:

- the same ordinary provenance;
- the same abstraction/concretization fibers;
- the same lens complement;
- the same CSP conflicts and diagnoses;
- the same rich effect annotations;

but still requires a different LossKernel attribution verdict.

## Claim Ledger Update

Add T108 to TF1:

```text
Source-fiber loss relocation does not yet separate from why-not provenance,
abstract interpretation, lenses, CSP explanation, or rich effect annotations.
The surviving delta is a possible typed normal form for source-derived witness
obligations, not a new obstruction mechanism.
```

## Open Blocker

Construct a same-neighbor-data quotient fixture. If that cannot be built, TF1
should be demoted from candidate novel object to integration vocabulary over
existing formal tools.

## Literature Anchors

- Buneman, Khanna, and Tan, "Why and Where: A Characterization of Data
  Provenance" (ICDT 2001).
- Cousot and Cousot, "Abstract Interpretation: A Unified Lattice Model for
  Static Analysis of Programs by Construction or Approximation of Fixpoints"
  (POPL 1977).
- Foster, Greenwald, Moore, Pierce, and Schmitt, "Combinators for
  Bidirectional Tree Transformations" (TOPLAS 2007).
- Green, Karvounarakis, and Tannen, "Provenance Semirings" (PODS 2007).
- Wadler, "Monads for Functional Programming" (1992 lecture notes).

## Next Work

Try to build the same-neighbor-data quotient fixture. If it fails, rewrite
LossKernel as a cross-framework packaging discipline:

```text
projection loss = typed source-fiber witness obligation
```

and stop treating it as a novel invariant.

## Reproduction

```bash
python -m unittest tests.test_loss_relocation_prior_art -v
python -m models.run_t108
```
