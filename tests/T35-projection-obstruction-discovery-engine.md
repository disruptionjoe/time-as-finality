# T35 Test Specification: Projection-Obstruction Discovery Engine

## Purpose

T35 tests whether the finite PO1 framework can generate candidate structures
rather than only classify hand-selected examples.

The engine searches bounded finite `D1RestrictionSystem` families, enumerates
projection candidates, classifies them using T31, and reduces interesting
cases to minimal witnesses.

## Target Claims

- PO1: Projection-Obstruction Schema.
- T31: PO1 admissibility conditions.
- T33: partial derivation from IPT, RMT, and named forgetting.
- T34: PO1 chain and boundary behavior.

## Search Space

The generator uses only structural finite shapes:

| Shape | Meaning |
| --- | --- |
| `empty` | no patch constraints |
| `consistent_chain` | satisfiable same-chain constraints |
| `triangle_obstruction` | three-patch finite gluing obstruction |
| `square_obstruction` | four-patch finite gluing obstruction |
| `local_failure` | locally inconsistent patch |

The engine generates high-profile source systems and low-profile restricted
systems, then enumerates total and partial site maps.

## Classification Labels

| Label | Expected source |
| --- | --- |
| `admissible_po1` | T31 fully admissible |
| `boundary_non_definable` | AC3 fails |
| `shared_obstruction` | richer and restricted systems obstructed |
| `lossy_non_obstructing` | AC6 fails with measurable loss |
| `obstruction_removed` | richer obstructed but restricted endpoint clean |
| `trivial_local_failure` | local satisfiability fails |
| `outside_po1` | no interesting current PO1 class |

## Acceptance Criteria

T35 succeeds if it produces:

1. an executable finite exploration engine;
2. automated generation of candidate projection structures;
3. automatic classification using T31/T33 machinery;
4. at least one generated positive PO1 candidate;
5. at least one generated boundary case;
6. at least one generated minimal counterexample;
7. a recommendation on the framework's exploratory power.

## Expected Executable Results

| Result | Expected |
| --- | --- |
| generated systems | at least 8 |
| projection candidates | more than 20 |
| positive PO1 candidates | at least 1 |
| boundary candidates | at least 1 |
| minimal counterexamples | at least 1 |
| novel positive signatures | at least 1 |
| best hypothesis | `H2 with H3 caution` |

## Focused Unit Tests

| Test class | Key assertions |
| --- | --- |
| `TestT35Generator` | bounded systems and projection candidates are generated |
| `TestT35Discovery` | positive, boundary, counterexample, and novel signatures exist |
| `TestT35EvaluationShape` | T31 verdicts are reused; JSON shape is stable |

## Non-Goals

- Do not claim automated theorem discovery.
- Do not use machine learning.
- Do not encode domain-specific examples.
- Do not treat generated structures as scientific discoveries.

## Artifacts

- `TECHNICAL-REPORT-projection-obstruction-discovery-engine-v0.1.md`
- `models/projection_obstruction_discovery.py`
- `models/run_t35.py`
- `tests/test_projection_obstruction_discovery.py`
- `results/projection-obstruction-discovery-engine-v0.1.json`
- `results/projection-obstruction-discovery-engine-v0.1-results.md`
