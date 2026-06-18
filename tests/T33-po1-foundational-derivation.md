# T33 Test Specification: PO1 Foundational Derivation

## Purpose

T33 asks whether the PO1 admissibility conditions (AC1-AC7, narrowed to six by
T32) arise from two deeper mathematical frameworks:

- **IPT**: Invariant-Preservation Theorem framework — local-to-global
  consistency of structural invariants
- **RMT**: Resource-Monotonicity Theorem framework — global satisfiability
  resource is non-increasing under restriction

T33 does not add new application domains. It works inside the finite
`D1RestrictionSystem`, `D1RestrictionMorphism`, and `ProjectionCase` machinery
established by T26-T32.

## Target Claim

PO1: Projection-Obstruction Schema.

## Competing Hypotheses

| ID | Statement |
| --- | --- |
| H0 | AC1-AC7 are independent empirical conditions with no deeper derivation |
| H1 | All conditions arise from IPT alone |
| H2 | All conditions arise from RMT alone |
| H3 | Both IPT and RMT are required; neither alone is sufficient |
| H4 | A single deeper principle explains all conditions more economically |
| H5 | No derivation from these principles is currently justified |

## Candidate Foundations

### IPT Framework
- Local-to-global consistency of structural invariants
- Covers typing obligations (AC1, AC2), projection definability (AC3),
  inherited constraints (AC4), and detectable profile loss (AC5-measurable)
- Does NOT directly require obstruction polarity (AC6, AC7)

### RMT Framework
- Global satisfiability resource R = global_assignment_exists
- Covers strict decrease (AC6+AC7 together), measurable loss (AC5-measurable)
- Does NOT enforce total site map (AC3) or full T26 axiom validity (AC1, AC2)

## Core Questions

1. Which conditions are derivable from IPT alone?
2. Which conditions are derivable from RMT alone?
3. Is any condition independent of both frameworks?
4. What is the best-supported hypothesis (H0-H5)?
5. What is the smallest theorem candidate for PO1?

## Expected Results

| Result | Expected value |
| --- | --- |
| Best hypothesis | H3 |
| H0 verdict | rejected |
| H1 verdict | partially_supported |
| H2 verdict | partially_supported |
| H3 verdict | supported |
| H4 verdict | boundary |
| H5 verdict | rejected |
| IPT derives | AC1, AC2, AC3, AC4 (fully); AC5-measurable (partially) |
| RMT derives | AC4, AC5-measurable, AC6, AC7 (fully) |
| Not derivable from either | AC5-naming |
| Counterexamples required | 3 |
| T31 resource monotones | 4 (all strictly decreasing) |

## Executable Tests

| Test class | Key assertions |
| --- | --- |
| `TestResourceExtraction` | 4 T31 monotones; all richer_value=1, restricted_value=0 |
| `TestInvariantProfiles` | H1 class for obstructed; no-obstruction for clean; certificates correct |
| `TestDerivationAttempts` | 16 attempts (8 IPT + 8 RMT); AC1-AC4 derived from IPT; AC5-naming independent from both; AC6-AC7 derived from RMT; AC3 not_applicable for RMT |
| `TestHypothesisVerdicts` | H0 rejected, H1-H2 partial, H3 supported, H4 boundary, H5 rejected; best_hypothesis=H3 |
| `TestCounterexamples` | AC5-naming witness fails AC5 (verdict non_admissible_no_forgotten_structure); AC3-RMT witness fails AC3; AC6-IPT witness fails AC6 |
| `TestResourceMonotone` | Strict decrease from rich to restricted; identical systems not strictly |
| `TestT33ResultStructure` | T32 basis loaded; AC5-naming in remaining_independence; theorem candidate present; P5 in recommendation |

## Counterexample Requirements

T33 must generate witnesses for:

| Target | Required witness |
| --- | --- |
| AC5-naming not in RMT | ProjectionCase with resource drop and profile loss but `forgotten_structure=()` |
| AC3 not in RMT | ProjectionCase with resource drop and partial site map |
| AC6 not in IPT | ProjectionCase with valid typed pair and total map but no restricted obstruction |

## Acceptance Criteria

T33 succeeds if it produces:

1. An evaluated H0-H5 hypothesis matrix;
2. A derivation attempt for each AC against each principle (IPT and RMT);
3. Resource monotone computation for all four T31 positive cases;
4. Three finite counterexamples marking the IPT/RMT boundary;
5. A smaller theorem candidate for PO1;
6. A recommendation for whether to treat AC5-naming as a first-class principle (P5).

Negative results (H1, H2 partially supported; AC5-naming independent) count as
success if they precisely identify the mathematical boundary.

## Artifacts

- `models/po1_foundational_derivation.py`
- `models/run_t33.py`
- `tests/test_po1_foundational_derivation.py`
- `tests/T33-po1-foundational-derivation.md`
- `results/po1-foundational-derivation-v0.1.json`
- `results/po1-foundational-derivation-v0.1-results.md`
- `TECHNICAL-REPORT-po1-foundational-derivation-v0.1.md`
