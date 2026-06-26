# Obstruction Relocation And Reconstruction Debt

> **DORMANT (as of 2026-06-26).** No downstream references in tests/, models/,
> results/, CLAIM-LEDGER, or ROADMAP. Kept for the record; not an active line.

## Status

Open formal target. Not a conservation law and not a main research line yet.

## Core Question

When an information-losing morphism appears to remove an obstruction, has the
obstruction been eliminated, or has a reconstruction obligation moved into a
different layer?

Candidate layers:

- object-level inconsistency;
- missing provenance;
- forgotten structure;
- LossKernel data;
- admissibility conditions;
- accessible-witness or apparent/event gap data;
- protocol assumptions;
- reconstruction uncertainty.

## Preferred Language

Use:

```text
conservation-law temptation
obstruction relocation
reconstruction debt
obstruction accounting
degree-lowering flow
```

Avoid:

```text
conservation of obstruction
conservation of information
obstruction cannot be eliminated
```

Exact conservation laws are too strong for the current evidence.

## Why The Conservation-Law Intuition Matters

The strongest intuition is conservation-like:

```text
when a projection appears to remove a reconstruction problem, the problem has
not vanished; the obligation to account for it has moved.
```

This is worth preserving because it is the pattern that makes the idea
mathematically tempting. It suggests that obstruction might behave like an
accounted quantity under admissible information-losing morphisms.

But the repo should not call this a conservation law yet. A real conservation
law needs an invariant, an equivalence relation, and a balance equation. Current
evidence supports only a weaker research target:

```text
find where the obstruction, uncertainty, or reconstruction obligation goes
after projection.
```

If T102 discovers a stable invariant across multiple cases, the language can be
upgraded. Until then, "conservation law of obstruction" is the motivating
temptation, not the theorem.

## Three Versions

### Version 1: Obstruction Displacement

Weakest and most plausible.

Target statement:

```text
For an admissible information-losing morphism, an object-level reconstruction
failure may be preserved, lowered in degree, or relocated into explicit
bookkeeping required for reconstruction.
```

This is close to existing repo patterns:

- T39: known CSP obstruction remains, while PO1 adds typed source/loss and
  admissibility layers.
- T63/T65: global assignment failure is expressed as holonomy or causal-boundary
  obstruction.
- T68/T72/T74: provenance cannot be inferred from outcomes, so the obligation
  moves into protocol assumptions and raw-log provenance.
- T73: path dependence is organized by composed LossKernel.
- Pati-Salam typed forgetting: preserved dimension and lost `T3R` structure
  separate the successful full map from the failed projection.

### Version 2: Reconstruction Debt

Stronger but still testable if weakened.

Target statement:

```text
LossKernel(f) induces a measurable target-side reconstruction debt: ambiguity,
non-uniqueness, missing witness obligations, or a lower bound on reconstruction
uncertainty.
```

This should not claim that lost information remains recoverable. It claims only
that loss may leave a measurable footprint in target reconstruction.

### Version 3: Obstruction-Degree Flow

Most theorem-shaped and most dangerous.

T69 supports a narrow finite form:

```text
H1 -> H0 can occur.
H0 -> H1 is blocked for the tested admissible loss morphisms.
```

A broader hierarchy such as:

```text
H2 -> H1 -> H0 -> none
```

requires new coefficient, support, cover, and morphism hypotheses. This version
should remain blocked until examples justify it.

## Success Criteria

- Classify at least four existing artifacts by source obstruction, target
  visible obstruction, relocated obligation, and failure degree:
  T39, T63/T65, T68/T72/T74, T73, or Pati-Salam typed forgetting.
- Include a negative control where a projected obstruction genuinely disappears
  because the source obstruction was irrelevant or non-admissible for the target.
- Define at least one reconstruction-debt observable that is not merely a prose
  restatement of `forgotten_structure`.
- State whether the result is relocation, degree-lowering, genuine elimination,
  or unresolved.

## Failure Criteria

- Every case reduces to "we chose to record the missing structure in metadata."
- The classification assumes that every source obstruction must matter to every
  target.
- Reconstruction debt cannot be measured without circularly reading
  LossKernel labels back into the result.
- The theorem requires exact conservation language.

## First Concrete Test

Build a bounded audit, tentatively:

```text
T102: Obstruction Relocation Audit
```

Minimum fields per case:

```text
source_obstruction
projection_or_loss_morphism
target_obstruction
relocated_layer
reconstruction_debt_measure
failure_degree_before
failure_degree_after
classification
```

Candidate classifications:

- `preserved_obstruction`;
- `degree_lowered`;
- `relocated_to_losskernel`;
- `relocated_to_provenance`;
- `relocated_to_admissibility`;
- `relocated_to_gap`;
- `genuinely_eliminated`;
- `non_admissible_source_obstruction`.

## Promotion Gate

Promote only if T102 finds a non-circular reconstruction-debt observable or a
stable relocation taxonomy that compresses multiple existing results. Otherwise
keep this as a useful review lens under LossKernel formalization.
