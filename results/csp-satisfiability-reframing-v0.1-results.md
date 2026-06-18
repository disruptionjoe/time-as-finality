# T39: CSP / Satisfiability Reframing — Results v0.1

**Status: implemented**
**Tests: 65/65 pass**
**Best-supported hypothesis: H_B**

## Central Question

Is PO1 best understood as a finite CSP theorem?

**Answer: yes at the obstruction level; no as a complete reduction.**

PO1's gluing obstruction is exactly a parity-conflicting binary CSP. However,
PO1 adds typed projection (AC5, AC7) and admissibility classification (AC1-AC7)
that have no direct CSP analogues. The obstruction mechanism is known; the
classification framework on top of it is new.

## Theorem Results

### Theorem 1 — Arc-Consistency Triviality

Every binary same/different constraint over {-1, 1} is arc-consistent.

- "same" is witnessed by (left=1, right=1).
- "different" is witnessed by (left=1, right=-1).
- Arc consistency is universally true for our constraint language.
- Result: arc consistency cannot distinguish PO1 from non-PO1 cases.
  It adds no information here.

Verified on all four scenario CSPs (all arc-consistent regardless of
global satisfiability).

### Theorem 2 — Signed-Graph Parity

A binary {-1, 1} CSP with same/different constraints is globally satisfiable
iff its signed constraint graph contains no negative cycle.

- Signed graph: vertices = variables; edges labeled +1 (same) or -1 (different).
- Negative cycle: cycle whose edge-label product is -1 (odd number of "different"
  edges around the cycle).
- Two obstruction subtypes:
  - **direct_parity_conflict**: same pair appears with both same and different
    constraints. Minimum: 2 variables, 2 patches.
  - **transitive_parity_conflict**: odd cycle of length ≥ 3. Minimum: 3 variables,
    3 patches (the T26 3-site case).

### Theorem 3 — D1-CSP Equivalence

`D1RestrictionSystem.global_section().obstruction_detected` equals
`NOT globally_satisfiable` for the corresponding binary CSP.

| Scenario | Variables | Constraints | D1 obstructed | CSP obstructed | Equiv |
| --- | --- | --- | --- | --- | --- |
| min_direct_conflict | 2 | 2 | True | True | ✓ |
| min_transitive_conflict | 3 | 3 | True | True | ✓ |
| tree_structured | 4 | 3 | False | False | ✓ |
| satisfiable_all_same | 3 | 2 | False | False | ✓ |

All four D1 equivalence checks pass.

### Theorem 4 — PO1-as-CSP

PO1 IS a CSP theorem at the obstruction level. The gluing obstruction maps
exactly to a parity-conflicting binary CSP. However, PO1 adds three layers
not present in standard CSP theory:

**(A) Typed source (AC7)**: the source system must be globally satisfiable.
CSP has no notion of a "source" system that was satisfiable before projection.

**(B) Typed forgotten structure (AC5)**: the projection discards named structure
(forgotten_dimensions annotated on the morphism). CSP constraints are added or
removed; they are not "forgotten" with a typed annotation.

**(C) Admissibility classification (AC1-AC7)**: CSP satisfiability is binary
(satisfiable or not). PO1 classifies the satisfiability-loss event as meaningful
(fully_admissible), shared (non-admissible), or degenerate (non-admissible).
This classification has no CSP analogue.

## PO1 Bridge Results

| Case | PO1 | Source sat. | Target obstruction | CSP detects |
| --- | --- | --- | --- | --- |
| witten_1981 | True | True | transitive_parity_conflict | True |
| nielsen_ninomiya | True | True | transitive_parity_conflict | True |
| synthetic_lossy_no_obstruction | False | True | none | True |
| synthetic_shared_obstruction | False | False | transitive_parity_conflict | True |

In all cases:
- `ac5_expressible_in_csp = False`
- `ac7_expressible_in_csp = False`

CSP correctly detects the presence or absence of obstruction. It cannot
distinguish PO1-admissible from non-admissible cases (shared obstruction
source passes CSP detection but fails AC7).

## Hypothesis Verdicts

**H_A** (PO1 entirely reducible to CSP): **rejected**.
The gluing obstruction is a known CSP phenomenon, but PO1's typed structure
(AC5, AC7, admissibility classification) has no CSP analogue.

**H_B** (PO1 obstruction = CSP; typed projection and admissibility are new):
**best supported**.
Theorems 1-4 confirm: the obstruction mechanism is equivalent to parity
conflict; the typed structure on top is the genuine new contribution.

**H_C** (admissibility classification is the primary new contribution):
**partially supported**.
Admissibility is part of the new contribution, but typed projection (AC5 + AC7
together) is equally important. H_C undersells the projection structure.

## Boundary

- Equivalence holds for binary {-1, 1} domains with same/different constraints.
- Richer CSP languages (n-ary constraints, non-binary domains, soft constraints,
  algebraic CSP, valued CSP) may capture more of PO1's structure.
- Valued CSP (VCSP) may partially capture AC5: forgetting named structure could
  map to an increased constraint-violation cost. Not yet tested.
- The AC1-AC2 validity checks (D1 profile axioms) are domain-specific and have
  no natural CSP analogue.
- The admissibility classification (7 conditions) is specific to the typed
  morphism / D1 profile framework.

## Recommendation

Adopt PO1-as-CSP as a named theorem (T39 result). The publishable statement:

> *Typed Projection-Obstruction is a CSP classification scheme: a finite
> framework for identifying when satisfiability loss under projection is
> meaningful — requiring a typed source, named forgotten structure, and
> admissibility classification not expressible in standard CSP.*

Next steps:
1. Test whether Valued CSP captures AC5.
2. Check composition law: is PO1-as-CSP preserved under morphism composition?
3. Compare against algebraic CSP polymorphism theory.
