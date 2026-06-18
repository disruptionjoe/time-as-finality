# T39: CSP / Satisfiability Reframing

## Target Claims

- PO1 (Projection-Obstruction Principle)
- D1RestrictionSystem (patch language = binary CSP)
- T26 (3-site gluing obstruction)
- T27, T28, T29 (class-relative bridge and obstruction schema)
- T31, T32, T33 (admissibility conditions and derivation)

## Central Question

Is PO1 best understood as a finite CSP theorem — satisfiability loss under
typed projection?

Specifically: does the D1RestrictionSystem patch language already reduce to
known CSP theory, or does PO1 add structure beyond what CSP satisfiability
can express?

## Setup

The D1RestrictionSystem patch language is a binary {-1, 1} CSP:
- **Variables**: named items in each patch's variable list.
- **Domain**: {-1, 1} for every variable.
- **Constraints**: `PatchConstraint(left, right, "same")` or `("different")`.
- **Global section**: a satisfying assignment for ALL patch constraints jointly.
- **Gluing obstruction**: each patch locally satisfiable but no joint assignment exists.

Four scenarios provide the witnesses:
1. Minimum direct conflict: 2 variables, 2 patches (same + different on same pair).
2. Minimum transitive conflict: 3 variables, 3 patches (T26 A=B, B=C, A≠C).
3. Tree-structured CSP: 4 variables, 3 patches, no cycles — globally satisfiable.
4. Satisfiable all-same CSP: 3 variables, 2 patches — globally satisfiable.

Four PO1 bridge cases (from T27, T29, T30):
- witten_1981, nielsen_ninomiya, synthetic_lossy_no_obstruction, synthetic_shared_obstruction.

## Success Criteria

1. Every binary same/different constraint over {-1, 1} is arc-consistent
   (Theorem 1 — Arc-Consistency Triviality).
2. Global satisfiability is determined exactly by absence of negative cycles in
   the signed constraint graph (Theorem 2 — Signed-Graph Parity).
3. D1 obstruction iff CSP parity conflict — verified on all four scenarios
   (Theorem 3 — D1-CSP Equivalence).
4. PO1 bridge cases: CSP detects the obstruction but cannot express AC5 or AC7
   (Theorem 4 — PO1-as-CSP).
5. Hypothesis H_B is best supported: PO1 IS a CSP theorem at the obstruction
   level; typed projection and admissibility classification are new structure.

## Failure Criteria

- Any binary same/different constraint is not arc-consistent.
- A globally unsatisfiable CSP passes the signed-graph parity check.
- A globally satisfiable CSP fails the parity check.
- D1 obstruction and CSP obstruction disagree on any witness case.
- H_A is supported (PO1 is entirely reducible to CSP — would imply no new
  structure from typed projection and admissibility classification).
- H_C is best supported over H_B (would imply admissibility classification
  is more important than typed projection itself).

## Known Physics Constraints

- Binary {-1, 1} domain captures the finality / non-finality assignment.
- "same" = consistent patch agreement; "different" = contradictory constraint.
- Signed-graph 2-colorability is known for binary CSPs over Boolean domains;
  this test establishes the exact equivalence for D1RestrictionSystems.
- The typed structure (AC5, AC7) is framework-specific and has no natural
  encoding in standard CSP languages.

## Contribution Needed

- Valued CSP (VCSP) comparison: does AC5 (named forgotten structure) map to a
  cost function in VCSP? If so, how much of PO1's admissibility can VCSP express?
- Algebraic CSP: does the signed-graph parity condition correspond to a known
  polymorphism-based tractability class?
- Composition law for typed projections: is the PO1-as-CSP classification
  preserved under composition of morphisms?
