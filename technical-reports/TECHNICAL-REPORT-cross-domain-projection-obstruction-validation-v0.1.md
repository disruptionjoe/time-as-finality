# Technical Report: Cross-Domain Projection-Obstruction Validation v0.1

## Summary

T30 hostile-tests PO1 outside the physics and GU examples that motivated it.
The revised candidate set is intentionally sharper:

1. Git merge conflicts
2. Financial risk model
3. Translator / poet

The result is stronger but still constrained:

```text
PO1 has two unrelated non-physics finite positives, but translator/poet shows
that PO1 must not absorb every case of lost meaning or lossy projection.
```

T30 recommends keeping PO1 at `partially_supported`, with stronger evidence
inside that status and explicit admissibility constraints.

## Method

T30 reuses the T29 `ProjectionCase` and `analyze_projection_case` machinery.
Each hostile domain is encoded as:

```text
richer D1RestrictionSystem
projection / restriction morphism
restricted D1RestrictionSystem
classification
```

No category or sheaf upgrade was needed.

## Case Classification

| Domain | Case | Classification | PO1 support |
| --- | --- | --- | --- |
| Git merge conflict | `git_semantic_merge` | projection-created obstruction | yes |
| Financial risk model | `financial_tail_risk_model` | projection-created obstruction | yes |
| Translator / poet | `translator_poet_boundary` | no meaningful PO1 fit | no |

## Case Notes

### Git Merge Conflict

The richer object is a rename-aware semantic merge. The restricted object is a
path-only merge model.

The richer system has a global section. The restricted system is locally
satisfiable but globally obstructed. The projection is definable and forgets
rename metadata plus the semantic merge driver.

Verdict:

```text
positive PO1 instance
```

This rejects H0 in finite scope: PO1 is not only a GU or physics pattern.

### Financial Risk Model

The richer object is a toy tail-aware stress model with stress regimes, tail
dependence, liquidity feedback, and a capital buffer. The restricted object is
a flat local-risk-limit model.

The richer system has a global section. The restricted system is locally
satisfiable but globally obstructed after the projection forgets the structures
that resolve joint stress behavior.

Verdict:

```text
positive PO1 instance, high-stakes toy only
```

This is the strongest hostile case in T30 because it is not adjacent to the
GU examples and because vague analogies in financial-risk language are
dangerous. The model is finite and illustrative only. It is not a theorem
about real portfolios, regulatory capital, market risk, liquidity risk, or
investment decisions.

### Translator / Poet

The richer object carries poetic image, rhythm, register, translator judgment,
and cultural resonance. The restricted object keeps only literal word mapping.

The projection is lossy, but the finite model does not produce a canonical
gluing obstruction. More importantly, there is no obvious domain-independent
finite same/different restriction system that captures poetic force.

Verdict:

```text
no meaningful PO1 fit
```

This is the anti-overclaim result. It prevents PO1 from becoming:

```text
any loss of meaning = projection-obstruction
```

## Hypothesis Evaluation

| Hypothesis | Status | T30 verdict |
| --- | --- | --- |
| H0: PO1 is domain-specific to GU/no-go style cases | rejected in finite scope | Git and financial risk are positive |
| H1: PO1 applies to at least one non-physics inherited domain | supported | Git and financial risk are positive |
| H2: PO1 applies across multiple unrelated domains | supported in finite scope | two unrelated non-physics positives |
| H3: PO1 requires modification for non-physics domains | not supported by this set | no new machinery was needed |
| H4: PO1 is too broad or underconstrained | partially supported as warning | translator/poet blocks overclaiming |

Best supported verdict:

```text
H2 with H4 admissibility constraints
```

## Recommendation

Keep PO1 at `partially_supported`.

Do not promote PO1 to a universal schema. T30 strengthens the evidence inside
the current status, but the translator/poet case shows that PO1 needs an
admissibility test before new examples count.

Future PO1 evidence should require:

1. The projection is independently motivated by the domain.
2. The richer system has a global section.
3. The restricted system is obstructed.
4. The forgotten structure is the same structure that resolves the restricted
   obstruction.
5. Lossy projection without obstruction is excluded.
6. Shared obstruction is excluded.
7. Incomplete site maps are boundary cases, not failed positives.
8. Loss of meaning, nuance, or interpretation is not sufficient unless it is
   represented by a canonical finite obstruction.

## Non-Claims

T30 does not claim PO1 is universal.

T30 does not prove external theorems about Git, financial systems, translation,
or poetry.

T30 does not provide financial advice, risk-management advice, legal advice,
or investment guidance.

T30 does not promote PO1 beyond `partially_supported`.

## Artifacts

| Artifact | Path |
| --- | --- |
| Model | `models/cross_domain_projection_obstruction_validation.py` |
| Runner | `models/run_t30.py` |
| Tests | `tests/test_cross_domain_projection_obstruction_validation.py` |
| Test spec | `tests/T30-cross-domain-projection-obstruction-validation.md` |
| JSON results | `results/cross-domain-projection-obstruction-validation-v0.1.json` |
| Results summary | `results/cross-domain-projection-obstruction-validation-v0.1-results.md` |
