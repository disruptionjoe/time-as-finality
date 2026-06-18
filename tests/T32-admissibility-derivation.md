# T32 Test Specification: PO1 Admissibility Derivation

## Purpose

T32 determines whether the seven PO1 admissibility conditions from T31 are
independent empirical criteria or consequences of a smaller finite
restriction-system structure.

The test does not add new application domains. It works inside the finite
`D1RestrictionSystem`, `D1RestrictionMorphism`, and `ProjectionCase`
machinery already developed by T26-T31.

## Target Claim

PO1: Projection-Obstruction Schema.

## Conditions Under Audit

| Condition | Meaning |
| --- | --- |
| AC1 | Richer system satisfies all T26 axioms |
| AC2 | Restricted system satisfies all T26 axioms |
| AC3 | Projection is definable by a total site map |
| AC4 | Restricted patches are locally satisfiable |
| AC5 | Projection forgets named structure and loses measurable profile data |
| AC6 | Restricted system has a finite gluing obstruction |
| AC7 | Richer system has a global section |

## Tested Questions

1. Does any condition logically imply another?
2. Does removing a condition admit false positives?
3. Can every feasible AC subset be realized by a finite generated
   `ProjectionCase`?
4. Is there a smaller condition basis?
5. Is there a smaller principle basis?
6. Which conditions remain outside the intrinsic D1RestrictionSystem object?

## Expected Result

T32 should find:

| Result | Expected verdict |
| --- | --- |
| Dependency graph | AC6 implies AC4 |
| Minimal condition basis | AC1, AC2, AC3, AC5, AC6, AC7 |
| Principle basis | typed pair, definable projection, projection-created obstruction, informative forgetting |
| Generated feasible AC vectors | 96 |
| Impossible AC vectors | 32 |
| Impossibility rule | AC6=True and AC4=False cannot occur |
| Best hypothesis | H2 with H4 boundary |

## Counterexample Requirements

T32 must generate witnesses showing that removing each non-derived condition
admits a false positive:

| Removed | Required witness |
| --- | --- |
| AC1 | invalid richer object becomes admissible |
| AC2 | invalid restricted object becomes admissible |
| AC3 | non-definable projection becomes admissible |
| AC5 | lossless or unnamed projection becomes admissible |
| AC6 | no-obstruction projection becomes admissible |
| AC7 | shared obstruction becomes admissible |

AC4 is expected to have no removal witness under current T26 semantics because
AC6 already entails local satisfiability.

## Executable Tests

| Test class | Key assertions |
| --- | --- |
| `T32DependencyTests` | AC6 -> AC4 edge exists; AC4 absent from minimal basis |
| `T32RemovalAuditTests` | each independent condition has a false-positive witness when removed |
| `T32SubsetGenerationTests` | 96 feasible vectors generated, 32 impossible vectors identified |
| `T32AnalysisShapeTests` | JSON runner exposes dependency, derivation, removal, and subset results |

## Acceptance Criteria

T32 succeeds if it produces:

1. a dependency graph among AC1-AC7;
2. a minimal admissibility basis or a clear failure to find one;
3. at least one successful derivation or proof of independence;
4. executable counterexamples demonstrating why omitted conditions fail;
5. a recommendation to retain, reduce, replace, or treat the ACs as
   independent.

## Artifacts

- `TECHNICAL-REPORT-po1-admissibility-derivation-v0.1.md`
- `models/po1_admissibility_derivation.py`
- `models/run_t32.py`
- `tests/test_po1_admissibility_derivation.py`
- `results/po1-admissibility-derivation-v0.1.json`
- `results/po1-admissibility-derivation-v0.1-results.md`
