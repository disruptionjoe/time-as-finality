# P97 Run - Axis-Crossing Loss Relocation Formalist

- timestamp: 2026-06-20T16:08:04-05:00
- goal_id: P97
- selected_persona: Axis-Crossing Loss Relocation Formalist
- selected_goal: Draft and test the next bounded loss-relocation goal: a finite
  fixture where loss in one source axis becomes an admissibility condition,
  operation-right boundary, reconstruction debt, or stable constraint in a
  different target axis, while preserving T107 absorbed-loss controls and T108
  prior-art pressure.
- bounded_question: Does the post-constellation idea justify a new executable
  axis-crossing audit, or does T108 force the work to become a prior-art-bound
  quotient/separation test instead?

## Repo Context Read

- [`/C:/Users/joe/JB/Github Repos/time-as-finality/explorations/research-constellation-loss-relocation-2026-06-20-155625.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/explorations/research-constellation-loss-relocation-2026-06-20-155625.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T107-loss-relocation.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T107-loss-relocation.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/loss_relocation.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/loss_relocation.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/results/loss-relocation-v0.1-results.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/results/loss-relocation-v0.1-results.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/tests/T108-loss-relocation-prior-art.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/tests/T108-loss-relocation-prior-art.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/models/loss_relocation_prior_art.py`](</C:/Users/joe/JB/Github Repos/time-as-finality/models/loss_relocation_prior_art.py>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/results/loss-relocation-prior-art-v0.1-results.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/results/loss-relocation-prior-art-v0.1-results.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/open-problems/obstruction-relocation-reconstruction-debt.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/open-problems/obstruction-relocation-reconstruction-debt.md>)
- [`/C:/Users/joe/JB/Github Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md`](</C:/Users/joe/JB/Github Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md>)

## Drafted Goal

### P97 - Axis-Crossing Loss Relocation Formalist

- status: done
- last_run: 2026-06-20T16:08:04-05:00
- artifact: explorations/persona-goal-runs/2026-06-20-160804-p97-axis-crossing-loss-relocation.md
- goal: Draft and test the next bounded loss-relocation goal: a finite fixture
  where loss in one source axis becomes an admissibility condition,
  operation-right boundary, reconstruction debt, or stable constraint in a
  different target axis, while preserving T107 absorbed-loss controls and T108
  prior-art pressure.
- ambition: Decide whether the "track where lost structure goes" idea should
  become an executable axis-crossing audit, a same-neighbor-data quotient test,
  or be demoted to integration vocabulary over existing formal tools.

## Work Performed

1. Confirmed that `T108` is already assigned to the loss-relocation prior-art
   audit. The axis-crossing idea should not reuse that identifier.
2. Re-read the one-room constellation artifact and preserved its strongest
   target:

   ```text
   loss in one axis becomes an admissibility condition, operation-right
   boundary, or stable constraint in another axis
   ```

3. Re-read T107 and its model. T107 already gives the required base semantics:
   source-fiber lift inspection produces reconstruction debt, stable constraint
   surfaces, absorbed freedom, and no-observable-relocation controls.
4. Re-read T108 and its model. T108 is a major constraint on the new goal:
   source-fiber relocation does not yet separate from why-not provenance,
   abstract interpretation, lenses, CSP explanation, or rich effect systems.
5. Tested the proposed goal against the open obstruction-relocation guardrail:
   do not use conservation-law language; require negative controls where loss
   occurs but no meaningful relocation remains.

## Result

Bounded-run verdict: draft the next executable audit, but make it stricter than
"axis crossing exists."

Axis crossing by itself would be too easy. T108 shows that mature neighboring
frameworks can absorb the finite source-fiber behavior if they receive the same
source fibers and target judgments. Therefore the next useful goal is:

```text
axis-crossing loss relocation with same-neighbor-data pressure
```

The candidate audit should ask whether a lost source axis can force a target
operation boundary on another axis while also recording whether standard
neighbors fully explain the same fixture.

## Candidate Data Shape

```text
AxisCrossingRelocationCase =
  source_states
  target_states
  projection
  lost_source_axis
  target_effect_axis
  target_operation_or_judgment
  source_lift_rule
  source_lift_verdicts
  relocation_class
  derived_witness_obligations
  same_neighbor_data:
    why_not_provenance
    abstract_interpretation_concretization
    lens_view_and_complement
    csp_conflicts_or_solutions
    rich_effect_annotation
  neighbor_absorption_verdict
```

Required invariant:

```text
lost_source_axis != target_effect_axis
```

This is the minimum condition that separates the new fixture from T107's
single-axis examples.

## Candidate Fixture Family

### Positive Case: Phase Loss Becomes Access Admissibility Debt

```text
source axes:
  phase_history
  access_window

projection:
  forgets phase_history
  preserves coarse event identity and requested access action

target judgment:
  may_admit_access(event_a, event_b)

source rule:
  access is admissible only if a phase-history/path-memory relation establishes
  that the access window is valid

expected class:
  reconstruction_debt
```

Why this is axis-crossing:

- Lost axis: `phase_history`.
- Target effect axis: `access_window` or `access_admissibility`.
- The target cannot decide access by inspecting visible access labels alone;
  it needs a source lift of path history.

### Positive Case: Orientation Loss Becomes Merge-Authority Boundary

```text
source axes:
  spin_or_orientation
  merge_authority

projection:
  forgets spin_or_orientation
  preserves target merge request

target judgment:
  may_merge(record_x, record_y)

source rule:
  merge is allowed only for compatible hidden orientations

expected class:
  reconstruction_debt or stable_constraint_surface depending on lift verdicts
```

Why this is axis-crossing:

- Lost axis: `spin_or_orientation`.
- Target effect axis: `merge_authority`.
- The hidden orientation does not need to be reconstructed for its own sake; it
  matters because it gates a future operation right.

### Stable Constraint Case: Frame Loss Becomes Ordering Impossibility

```text
source axes:
  frame_or_order_witness
  target_order_claim

projection:
  forgets frame_or_order_witness

target judgment:
  may_certify_order(event_a < event_b)

source rule:
  every lift forbids the target order certification

expected class:
  stable_constraint_surface
```

Why this matters:

- Uniformly forbidden lifts turn loss into a target-side impossibility boundary.
- This is the cleanest finite version of "forgotten structure becomes a rule."

### Absorbed-Loss Control: Gauge Representative Loss

```text
source axes:
  gauge_representative
  invariant_operation_right

projection:
  forgets gauge_representative

target judgment:
  may_apply_invariant_operation

source rule:
  all representatives give the same invariant verdict

expected class:
  absorbed_freedom
```

This preserves T107's core discipline: not all loss relocates.

### Label-Only Control

```text
source axes:
  decorative_label
  target_operation_right

projection:
  forgets decorative_label

target judgment:
  may_apply_operation

source rule:
  verdict independent of decorative_label

expected class:
  no_observable_relocation or absorbed_freedom
```

This prevents the audit from treating every lost coordinate as meaningful.

## Same-Neighbor-Data Pressure

Each positive case should carry enough data for the neighbors named in T108:

| Neighbor | What must be represented |
| --- | --- |
| why-not provenance | Missing source witness or failed derivation input. |
| abstract interpretation | Abstraction map and concretization fiber. |
| lenses | View plus complement or putback-relevant source information. |
| CSP explanation | Constraint, solution fiber, conflict, or diagnosis. |
| rich effects | Witness-carrying effect annotation, not label-only effect. |

If all neighbors produce the same attribution verdict, the result is not a
novel separation. It is still useful as an integration normal form.

If two cases have the same neighbor data but different LossKernel attribution
because the typed source axis changes the operation-right boundary, then the
fixture becomes a real candidate quotient witness.

## Acceptance Criteria For The Next Executable Audit

The next model should pass only if it has:

1. At least one mixed-lift axis-crossing reconstruction-debt case.
2. At least one axis-crossing stable-constraint-surface case.
3. At least one absorbed-freedom case.
4. At least one label-only or irrelevant-loss negative control.
5. Explicit `lost_source_axis != target_effect_axis` checks.
6. A neighbor absorption verdict for each positive case.
7. A clear result if prior art absorbs everything:

   ```text
   axis-crossing exists, but novelty remains unearned
   ```

## What This Improves

This goal sharpens the user's prose without overclaiming it.

The useful phrase remains:

```text
Track where lost structure goes.
```

But the runnable version is:

```text
Track whether a lost source axis changes a target operation boundary on another
axis, and whether that change survives prior-art absorption.
```

That turns "emergence as relocation into a stable constraint surface" into a
finite audit shape.

## What This Weakens

The run weakens any immediate plan to promote axis-crossing relocation as a new
mathematical object. T108 already shows the existing finite behavior is close to
standard machinery. The next audit can earn a stronger object only by producing
same-neighbor-data separation or by discovering a useful canonical normal form.

## Proposed Next Action

Implement a new executable audit with the next free test identifier at the time
of implementation. Do not call it T108.

Suggested working title:

```text
Axis-Crossing Loss Relocation Audit
```

Suggested files:

```text
tests/T###-axis-crossing-loss-relocation.md
models/axis_crossing_loss_relocation.py
tests/test_axis_crossing_loss_relocation.py
models/run_t###.py
results/axis-crossing-loss-relocation-v0.1-results.md
results/axis-crossing-loss-relocation-v0.1.json
```

The implementation should be allowed to return a negative result. A negative
result would be:

```text
The axis-crossing fixture works as an integration vocabulary but does not
separate from standard provenance, abstract interpretation, lenses, CSPs, or
rich effects.
```

## Claim-Status Posture

- No claim status changes.
- No `CLAIM-LEDGER.md`, `ROADMAP.md`, or `TESTS.md` updates.
- T107 remains the executable source-fiber semantics.
- T108 remains the active prior-art blocker.
- Axis-crossing loss relocation is now a drafted executable audit target, not a
  canonical object or theorem.

## Final Verdict

```text
Candidate best next move:
Build an axis-crossing loss-relocation audit with same-neighbor-data pressure.

Reason:
The user's strongest idea is not captured by T107's single-axis examples:
loss in one axis should be tested for operational residue in a different target
axis. But T108 prevents this from being treated as novelty unless prior-art
neighbors are represented in the same fixture.

Evidence:
T107 already supplies source-fiber relocation classes and absorbed-loss
controls. T108 shows those classes are prior-art-close. The missing executable
object is a finite case where lost_source_axis differs from target_effect_axis
and the resulting operation-boundary verdict is compared against the named
neighbors.

Risks:
The result may be fully absorbed by abstract interpretation, lenses,
provenance, CSPs, or rich effects. If so, the correct outcome is demotion to a
normal-form/integration vocabulary, not promotion.

What would change this recommendation:
If a same-neighbor-data fixture cannot be built without post hoc labels, stop
the axis-crossing branch. If it can be built and produces different LossKernel
attribution with the same neighbor data, promote the quotient witness as the
next formal target.
```
