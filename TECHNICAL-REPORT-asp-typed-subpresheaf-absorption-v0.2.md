# Technical Report: ASP Typed Subpresheaf And Absorption Audit v0.2

## Claim Under Test

The persona goal proposed that `ASP_O(U)` might be a useful mathematical object
rather than elegant notation for existing ideas.

T119 tests the strongest narrowed version:

```text
ASP_O^T(U,h) = typed observer/task-indexed admissible future set
```

It does not test ASP as a physical primitive, a GU result, a scalar measure, or
a replacement for entropy, information, finality, viability, or reachability.

## Finite Definition Used

For a finite observer-access site:

```text
S(U) = finite local section/task set over U
ASP_O^T(U,h) subset S(U)
```

A section or task is in `ASP_O^T(U,h)` only when all declared predicates pass:

- causal accessibility;
- viability;
- required witnesses;
- required operation rights;
- sufficient maintenance budget;
- required reconstruction paths;
- certification/admissibility tokens.

The finite model keeps restriction separate from forward transport. It only
checks presheaf-style restriction:

```text
rho_{V,U} : ASP(V) -> ASP(U)
```

for `U subset V`.

## Result

T119 supports the narrowed formalization but kills independent promotion.

The stable predicate case forms a typed subpresheaf:

```text
ASP(U) = {build_local, merge_local}
ASP(V) = {build_global, merge_global}
merge_global|U = merge_local
build_global|U = build_local
```

The negative control breaks closure:

```text
merge_global|U = merge_local not in ASP(U)
```

because the smaller patch lacks the required merge-base/certification and
reconstruction conditions. This is the intended failure mode: predicate typing
and audit monotonicity matter.

## Checks

| Check | Result |
| --- | --- |
| Typed subpresheaf closure under stable predicates | Supported |
| Negative control breaks closure | Supported |
| Pure relabeling preserves ASP structure | Supported |
| Access-boundary refinement changes ASP covariantly | Supported |
| ASP separates from coarse baselines | Supported |
| Enriched reachability absorbs the split | Supported |
| Opportunity-set framing absorbs the split | Supported |

## Strongest Separation

The strongest split remains the version-control/provenance witness:

```text
same endpoint repository state
same entropy bits
same information bits
same finality score
same viability score
same persistence horizon
same coarse reachable count
same coarse control rank
```

but:

```text
history-preserving repo: {build, merge, revert, bisect}
squashed snapshot:       {build}
```

The split is caused by merge bases, branch history, signed-history witnesses,
operation rights, and reconstruction paths.

## Strongest Absorption

The same case is also the strongest absorption result.

Once enriched reachability, opportunity-set, provenance, access-control, or
task-enriched viability models include:

- witnesses;
- operation rights;
- certification tokens;
- maintenance budgets;
- reconstruction paths;
- observer access boundaries;

then the enriched reachable/opportunity set computes the same distinction as
ASP. In that setting ASP is not independent mathematics. It is a useful audit
name for the enriched feasible future operation set.

## Prior-Art Pressure

| Comparator | Verdict |
| --- | --- |
| Reachability analysis | Absorbs ASP when witness/right/provenance tokens are state variables. |
| Viability kernels | Absorbs ASP when viability is defined over future task availability. |
| Active inference policy spaces | Absorbs ASP when policies range over witness-bearing, authority-valid futures. |
| Reinforcement-learning action/state spaces | Absorbs ASP as augmented state plus action masks/options. |
| Affordance landscapes | Partially absorbs actionable possibility; weaker on witnesses/certification by default. |
| Opportunity sets | Directly captures ASP as a feasible task set under constraints. |
| Information-theoretic distinguishability | Does not absorb ASP alone, but enriched side information can absorb part of it. |
| Finality/reconstruction debt | Captures the TaF residue: same endpoint, different future repair/reconstruction operations. |
| Sheaf/section compatibility | Supplies type discipline, not independent separation. |
| GU source-shadow projection | Supplies scaffolding for rich source vs observer shadow; no GU validation follows. |

## What This Improved

T119 improves the ASP thread by separating three issues that were previously
easy to conflate:

1. `ASP_O(U)` can be type-disciplined as a finite subpresheaf when predicates
   restrict stably.
2. Access-boundary changes are not gauge. They change ASP covariantly.
3. The finite separation from coarse metrics is real but absorbed by enriched
   prior art.

This makes ASP usable as a test object without promoting it as a primitive.

## What This Weakened Or Falsified

T119 weakens any claim that ASP is independent of existing frameworks. It
survives coarse comparisons but collapses into enriched reachability,
opportunity-set, provenance, access-control, and task-enriched viability
machinery.

It also blocks loose GU/rate language. Restriction maps, forward transport,
viability dynamics, measures, and goal functionals must remain separate until
explicitly connected.

## Current Strongest Claim

```text
ASP_O^T(U,h) is a typed observer/task-indexed admissible-future set.
It can be modeled as a finite subpresheaf under stable predicates and can
separate systems that coarse entropy, information, finality, viability, and
reachability classify identically. Its separation is mostly absorbed by
enriched reachability, opportunity-set, provenance, and task-enriched
viability formalisms.
```

## Recommendation

Preserve and formalize narrowly. Do not promote.

ASP should remain:

```text
an observer/task-indexed audit object
```

not:

```text
a new primitive
a GU result
a physics claim
a replacement for entropy, information, finality, viability, or reachability
```

## Claim Impact

No core claim upgrade.

No roadmap, claim-ledger, or persona-registry update is warranted from this
audit. If referenced later, T119 should be cited as an absorption result with a
finite type-discipline benefit.

## Open Follow-Up

The only worthwhile next step would be a stricter absorption challenge:

```text
Find a finite case where ASP predicts future operation availability while
enriched reachability, enriched viability, opportunity sets, provenance,
information with side channels, and finality/reconstruction-debt accounting
all remain matched or less precise.
```

Absent that witness, ASP should stay as vocabulary plus audit discipline.

## Reproduction

```bash
python -m unittest tests.test_asp_typed_subpresheaf_absorption -v
python -m models.run_t119
```
