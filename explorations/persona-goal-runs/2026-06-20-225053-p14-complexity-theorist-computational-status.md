# P14 Bounded Run - Complexity Theorist Computational Status Audit

- Run timestamp: 2026-06-20T22:50:53-05:00
- Persona: P14 - Complexity Theorist
- Goal id: P14
- Queue goal: Classify major executable results by computational status: brute-force finite witness, polynomial decision procedure, NP-hard/CSP-complete fragment, or theorem with scalable proof.
- Bounded scope: repo-only audit of representative executable families already used as core claim carriers. No claim-status, roadmap, test-index, or workflow edits.

## Repo Context Read

- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T26-d1-restriction-system.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T26-d1-restriction-system.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/d1_restriction_system.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/d1_restriction_system.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T39-csp-satisfiability-reframing.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T39-csp-satisfiability-reframing.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/csp_satisfiability_reframing.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/csp_satisfiability_reframing.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T54-finite-finality-descent-theorem.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T54-finite-finality-descent-theorem.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/finality_descent_theorem.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/finality_descent_theorem.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T110-finite-permutation-monotone-obstruction.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T110-finite-permutation-monotone-obstruction.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/finite_permutation_monotone_obstruction.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/finite_permutation_monotone_obstruction.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/weak_measurement_nonnull_criterion.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/weak_measurement_nonnull_criterion.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/detector_manifest_workflow_fit.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/detector_manifest_workflow_fit.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T59-finite-to-infinite-boundary-audit.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T59-finite-to-infinite-boundary-audit.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md>)

## Work Performed

1. Selected a small set of representative executable branches that actually carry major repo claims or gates.
2. Inspected the implementation shape, not just the prose, to see whether each branch currently decides by exhaustive enumeration, graph-style polynomial checks, or a proof-backed structural argument.
3. Classified each branch by the strongest honest computational status the current repo has earned.

## Classification Table

| Surface | Current honest status | Why |
| --- | --- | --- |
| `T26` / `D1RestrictionSystem.global_section()` | `brute-force finite witness` | `_count_assignments_satisfying(...)` enumerates `product((-1, 1), repeat=n)`, so the current executable obstruction check is exponential in the number of patch variables. |
| `T39` / signed-graph parity reframing | `polynomial decision procedure` | `_parity_analysis(...)` reduces the same/different fragment to signed-graph 2-coloring by BFS over the constraint graph. The obstruction verdict is graph-decidable even though the file still counts witnesses exhaustively for small examples. |
| `T54` / finality descent classifier | `polynomial decision procedure` | The quotient-union completion, partial-order check, and AM check are finite map/set/product checks over the listed events; no global completion search is performed. |
| `T110` / finite-permutation monotone obstruction | `theorem with scalable proof` | The scalable content is the orbit argument: on a finite permutation orbit, edgewise nondecrease forces constancy. The file also includes small brute-force controls (`exhaustive_cycle_check`), but the main claim is not resting only on enumeration. |
| `T132` / weak-measurement non-null gate | `polynomial decision procedure` | `classify_protocol(...)` is a fixed rule audit over named protocol features; complexity scales with the number of declared cases/features, not hidden search. |
| `T138` / detector workflow-fit audit | `polynomial decision procedure` | The manifest/workflow audit is a finite field/authority validation pass over a declared scaffold. It is not combinatorial search over workflow space. |

## Main Finding

The repo's current major executable surfaces split into two dominant classes:

1. **Finite brute-force witnesses** for local-to-global obstruction when the code still counts assignments directly.
2. **Polynomial structural classifiers** once the branch has been reframed into graph parity, quotient-union consistency, or finite rule validation.

The strongest example of a genuine complexity upgrade is the move from `T26`
to `T39`:

- `T26` proves the obstruction by explicit assignment counting on the tested finite instances.
- `T39` shows the same obstruction subproblem sits in a tractable signed-graph parity fragment, so the current executable core does **not** justify vague "hard search" rhetoric for that branch.

## Negative Result

No surveyed major executable branch honestly earns the label:

```text
NP-hard / CSP-complete fragment
```

at current repo evidence level.

The closest candidate is `T39`, but the implemented fragment is explicitly the
tractable binary same/different signed-graph case, not a general CSP-hardness
result. So the complexity-honest statement is:

```text
The repo contains CSP-reducible structure, but not a demonstrated
NP-hard/CSP-complete core result.
```

## Compression of the Current State

The cleanest queue-level compression is:

- `T26` and similar older obstruction checks: **executable finite witness by enumeration**.
- `T39`, `T54`, `T132`, `T138`: **finite polynomial classifiers**.
- `T110`: **theorem-backed structural obstruction with brute-force sanity controls**.
- `NP-hard/CSP-complete`: **not yet earned anywhere in the surveyed core**.

That is enough to keep theorem language honest about scale.

## Result

Bounded-run verdict:

```text
The repo has already crossed one real complexity threshold:
some branches moved from brute-force witness generation to polynomial
decision procedures.

But the project has not earned any general hardness rhetoric.
```

So the right computational posture is neither:

```text
"everything is just tiny brute force"
```

nor:

```text
"the core is computationally hard in a deep complexity-theoretic sense"
```

It is:

```text
mixed computational status, with a tractable graph/descent/rule-check core
and a few still-enumerative finite witness engines.
```

## Blocker

The repo does not yet expose a single complexity-facing index that says, for
each major test family:

- input size;
- current algorithmic decision method;
- whether the result is only a finite witness;
- whether a scalable proof or polynomial reduction has replaced enumeration.

Without that surface, later summaries can still overstate either hardness or
scalability.

Resolution note: `COMPLEXITY-LEDGER.md` now supplies this index for T26, T39,
T54, T73, T110, T132, and T138. Use that ledger before making brute-force,
polynomial, theorem-backed, NP-hard, CSP-complete, or scalability claims.

## Proposed Next Action

If Joe wants to push this branch one step further, the next bounded follow-on
should be:

1. Build a short complexity ledger for major executable families (`T26`, `T39`,
   `T54`, `T73`, `T110`, `T132`, `T138`).
2. For each, record one primary status: `finite_witness`, `poly_decider`,
   `theorem_backed`, or `open_hardness`.
3. Treat hardness claims as blocked until one branch actually proves or reduces
   to an NP-hard/CSP-complete fragment.

## Claim-Status Posture

- No claim-status changes.
- No roadmap or test-index updates.
- No hardness claim is promoted by this run.
- The main gain is a computational-honesty lens over the existing executable stack.
