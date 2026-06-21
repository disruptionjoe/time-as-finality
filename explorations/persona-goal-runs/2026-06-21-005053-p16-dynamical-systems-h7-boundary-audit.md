# P16 Bounded Run - Dynamical Systems H7 Boundary Audit

- Run timestamp: 2026-06-21T00:50:53-05:00
- Persona: P16 - Dynamical Systems Expert
- Goal id: P16
- Queue goal: Stress H7 with autonomous reversible and dissipative systems, asking whether finality monotones arise only with entropy export, attractor basins, or coarse-graining.
- Bounded scope: repo-only boundary audit over the existing H7 obstruction stack plus earlier attractor-language explorations. No claim-status, roadmap, test-index, workflow, or canonical theorem-surface edits.

## Repo Context Read

- `claims/H7-finality-induced-direction.md`
- `tests/T18-finality-direction-theorem.md`
- `tests/T80-reversible-finality-nonmonotonicity.md`
- `tests/T84-cyclic-reconciler-entropy-export.md`
- `tests/T106-bounded-sink-reversible-compression.md`
- `tests/T116-open-markov-record-entropy.md`
- `tests/T122-stationary-markov-monotone-obstruction.md`
- `tests/T128-minimal-living-arrow.md`
- `tests/T141-t1-record-graph-admissibility-ledger.md`
- `explorations/all-persona-last-24h-review-2026-06-20.md`
- `explorations/ten-persona-complexity-crosswalk.md`
- `explorations/TS-PERSONA-SPRINT-001-elena-voss-v0.1.md`
- `open-problems/arrow-of-time-as-constructor-theorem.md`

## Work Performed

1. Used the current H7 test stack as the authority surface rather than inventing a fresh dynamical model.
2. Split the dynamical-systems question into three regimes that are easy to blur together:
   - autonomous reversible dynamics;
   - autonomous dissipative or attractor-bearing dynamics;
   - observer-side coarse-grained or projected dynamics.
3. Checked whether any surviving H7 route in the repo actually lands in regime 2 without collapsing into regime 3 or into explicit resource/export bookkeeping.

## Regime Audit

| Dynamical regime | Best current verdict | Why |
| --- | --- | --- |
| Closed autonomous reversible dynamics | `blocked` | `T80`, `T106`, `T110`, and `T141` already show that raw reversible evolution, reversible memory, and explicit T1 copy/access moves do not produce a strict autonomous H7 monotone. On closed recurrent support, the monotone either fails or becomes constant. |
| Finite stationary stochastic dynamics | `blocked` | `T116` and `T122` block the stochastic version of the same hope. Positive circulation or path irreversibility alone does not produce a scalar finality monotone on stationary support. |
| Dissipative / attractor-bearing autonomous dynamics | `survives only as ordinary dissipation or basin contraction` | The repo's own dynamical-systems crosswalk already says finality-as-basin only covers the dissipative sector. Once a trajectory contracts into a basin, the live monotone is phase-space contraction, exported history, sink filling, or free-energy/resource drawdown. `T128` treats this as the smallest non-stipulative survivor, not as an H7-independent arrow. |
| Observer-side coarse-graining of reversible dynamics | `available but absorbed` | Reversible microdynamics can look monotone after observer-window restriction or retained-record accounting, but `T80`, `T84`, and `T106` show that the apparent arrow is paid for by forgetting, external history, or omitted reverse bookkeeping. |
| Holonic or macro attractor language in current explorations | `not earned as independent evidence` | `TS-PERSONA-SPRINT-001` reports that attractor-like dwell asymmetry was schedule-driven, not emergent. The repo has language for basins and lock-in, but not a new autonomous attractor theorem for H7. |

## Main Finding

The dynamical-systems route does not currently rescue H7 from the obstruction
stack. The current repo evidence supports a sharper split:

```text
reversible autonomous dynamics
  do not supply a strict finality monotone

dissipative/attractor dynamics
  can supply monotone behavior,
  but only by using ordinary basin contraction, dissipation,
  exported history, sink capacity, or resource drawdown

coarse-grained observer dynamics
  can display an apparent arrow,
  but that arrow is projection-relative and already absorbed by bookkeeping
```

So the best current P16 verdict is not:

```text
H7 has a dynamical-systems derivation independent of thermodynamics.
```

It is:

```text
Every dynamical-systems-flavored H7 survivor in the repo currently reduces to
one of three familiar mechanisms:
resource drawdown,
open-boundary/export accounting,
or coarse-grained loss of reversible detail.
```

## Smallest Useful Dynamical Rule

Attractor or Lyapunov language should be treated as H7-positive only when the
run states all three items explicitly:

1. the substrate dynamics and whether they are reversible, dissipative, or open;
2. the accounting object that makes the monotone move;
3. whether the monotone lives on the full state, a projected observer state, or
   a resource-augmented state.

If the monotone appears only after:

- dropping reverse channels;
- projecting away overwritten detail;
- adding sink or export variables;
- counting repair budget depletion;
- or moving to stationary support plus a hidden boundary condition;

then the run should be recorded as ordinary dissipation/coarse-graining
absorption, not as a new H7 route.

## Result

Bounded-run verdict:

```text
P16 strengthens the current demotion discipline around H7.
The repo has no physically autonomous attractor/dissipation story
that yields a strict finality arrow without paying in ordinary
resource, boundary, or coarse-graining terms.
```

The most honest compression is:

```text
Finality can still organize how a dynamical arrow is described,
but the tested arrow itself is not yet independent of standard
dissipative or projection-based mechanisms.
```

## Blocker

The missing object is not another reversible counterexample. It is one explicit,
physically motivated dissipative model where:

- the state space and observer projection are both declared;
- the candidate finality score is not just a renamed Lyapunov/resource function;
- the reservoir, sink, or exported history is fully accounted;
- and the model is compared directly against the standard dissipation account.

Without that comparison, attractor language is explanatory gloss, not a new
H7-bearing mechanism.

## Proposed Next Action

If Joe wants one bounded follow-on, the best next run is:

1. Build one minimal finite open dissipative model with an explicit reservoir.
2. Track two scores only:
   - a standard resource or Lyapunov-style quantity;
   - a proposed D1/finality quantity.
3. Classify the outcome:
   - same score in new words;
   - strict refinement of the standard score;
   - or no independent monotone after honest accounting.

That would turn the current P16 result from a boundary audit into a direct
collapse-or-separation test.

## Claim-Status Posture

- No claim-status changes.
- No roadmap or test-index changes.
- No new theorem or model is promoted.
- The run only narrows what counts as a legitimate future dynamical-systems
  upgrade path for H7.
