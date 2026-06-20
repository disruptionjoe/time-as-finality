# T119 Results: ASP Typed Subpresheaf And Absorption Audit v0.2

## Strongest version

ASP_O^T(U,h) is a typed observer/task-indexed admissible future set, modeled as a subpresheaf of finite local sections when admissibility predicates restrict stably.

## Weakest point

ASP loses type discipline when restriction, forward transport, viability dynamics, measures, and goal functionals are collapsed into one symbol.

## Typed subpresheaf check

| System | Closure holds | ASP by patch | Violations |
| --- | --- | --- | --- |
| `stable_typed_predicates` | `True` | `{'U': ['build_local', 'merge_local'], 'V': ['build_global', 'merge_global']}` | `[]` |
| `audit_monotonicity_violation` | `False` | `{'U': ['build_local'], 'V': ['build_global', 'merge_global']}` | `['merge_global|U=merge_local not in ASP(U)']` |

## Relabeling invariance

Relabeling invariant: `True`

## Boundary covariance

| Coarse ASP | Refined ASP | Invariant? | Covariant change? |
| --- | --- | --- | --- |
| `['build']` | `['bisect', 'build', 'merge', 'revert']` | `False` | `True` |

Access-boundary refinement changes ASP from snapshot-only tasks to history-aware tasks. This is a declared boundary change, not gauge.

## Absorption rerun

| Check | Result |
| --- | --- |
| Coarse metrics match | `True` |
| Coarse reachability separates | `False` |
| ASP separates | `True` |
| Enriched reachability absorbs | `True` |
| Opportunity set absorbs | `True` |
| High ASP tasks | `['bisect', 'build', 'merge', 'revert']` |
| Low ASP tasks | `['build']` |

## Prior-art comparison

| Comparator | Capture |
| --- | --- |
| reachability analysis | `captures_if_enriched` |
| viability kernels | `captures_if_enriched` |
| active inference policy spaces | `captures_if_enriched` |
| reinforcement-learning action/state spaces | `captures_if_enriched` |
| affordance landscapes | `partial` |
| opportunity sets | `captures_directly` |
| information-theoretic distinguishability | `partial` |
| finality/reconstruction debt | `partial` |
| sheaf/section compatibility | `partial` |
| GU source-shadow projection | `partial` |

## Verdict

ASP separates from coarse baselines but is absorbed by enriched reachable-state, opportunity-set, provenance, and task-enriched viability formalisms.

## Recommendation

Preserve and formalize narrowly as an audit object. Do not promote ASP as a primitive, a GU result, or independent physics.

## Claim impact

No core claim upgrade.
