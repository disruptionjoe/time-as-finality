# P20 - Physics-Informed Machine Learning Researcher Run

- persona: Physics-Informed Machine Learning Researcher
- goal_id: P20
- run_timestamp: 2026-06-21T04:54:54-05:00
- queue_source: `explorations/persona-future-run-goals-2026-06-20.md`
- goal: Train or specify an inverse problem that tries to recover D1 axes,
  branch support, provenance, and reversal cost from synthetic trajectories
  without labels.
- posture: bounded exploratory run only; no claim-status update, roadmap
  change, or ledger edit.

## Repo Context Read

- `FORMALISM.md`
- `tests/T90-weak-measurement-reparameterization-obstruction.md`
- `tests/T91-weak-measurement-platform-audit.md`
- `tests/T93-weak-measurement-undo-cost-independence.md`
- `tests/T109-q1a-branch-support-collapse.md`
- `tests/T118-q1a-reversal-cost-collapse.md`
- `tests/T79-dashboard-summary-nonidentifiability.md`
- `tests/test_weak_measurement_reparameterization_obstruction.py`
- `tests/test_weak_measurement_platform_audit.py`
- `tests/test_weak_measurement_undo_cost_independence.py`
- `tests/test_q1a_branch_support_collapse.py`
- `tests/test_q1a_reversal_cost_collapse.py`
- `explorations/persona-goal-runs/2026-06-21-035235-p19-causal-inference-detector-dag-audit.md`

## Bounded Run

Question: what is the smallest honest inverse problem the repo can support for
trajectory-like data, and which TaF coordinates are actually identifiable from
synthetic trajectories rather than smuggled in by labels or side-channel
choices?

Method:

1. Treat the inverse problem as latent-state recovery under declared
   observables, not as a free-form supervised predictor.
2. Use the weak-measurement audits (`T90/T91/T93`) to test whether branch
   support or reversal cost can be recovered from the same monitored trajectory
   record.
3. Use the Q1A collapse audits (`T109/T118`) to test whether branch support
   and reversal cost survive as independent coordinates inside the current
   fixed-data witness family.
4. Use the provenance audits (`P19`, `T79`) to test whether provenance is
   identifiable from coarse summaries or only from authenticated raw-log and
   intervention channels.

## Work Performed

I rewrote the requested ML task as an observability table.

Let the latent TaF state be

```text
z = (A, R, B, C, P)
```

where:

- `A` = accessible support;
- `R` = holder redundancy;
- `B` = branch support;
- `C` = reversal-cost coordinate;
- `P` = provenance / independence partition.

Let the observable family be split into:

```text
y_std = standard monitored trajectory data
      = coherence, fragment redundancy, access, control schedule

y_raw = authenticated raw-log / ancestry / intervention channels

y_aux = independent branch witness or independent undo-cost meter
```

The identifiability question is not "can a model fit labels?" It is:

```text
does y determine z up to the declared equivalence?
```

I then mapped the current repo evidence onto that question.

## Result

### Main Finding

The current repo does **not** support an honest inverse problem that recovers
all of `(A, R, B, C, P)` from synthetic trajectories alone.

What it supports is a stricter conclusion:

- `A` and `R` are trajectory-adjacent and can be part of the declared observed
  record profile.
- `B` and `C` are **not** identifiable from the same monitored trajectory in
  the present weak-measurement lane.
- `P` is **not** identifiable from coarse summaries and requires authenticated
  raw-log / intervention structure.

### Evidence Table

| observable regime | identifiable content | blocker or condition | repo evidence |
| --- | --- | --- | --- |
| `y_std` only | at most standard monitored-record timelines and any D1 coordinates already encoded in the same record | cannot separate independent TaF content from reparameterized thresholds | `T90`, `T91`, `T93` |
| current fixed-data Q1A family | audited accessible provenance-support count | branch support is single-root trivial; reversal-cost proxy collapses to support count | `T109`, `T118` |
| dashboard summaries | no honest provenance recovery | opposite raw-log completions share the same dashboard projection | `T79`, `P19` |
| `y_std + y_raw` | provenance partition `P` can become identifiable | requires pre-registered interventions or authenticated ancestry channels | `P19`, `T68/T70` as summarized in `P19` |
| `y_std + y_aux(branch)` | branch support `B` can be a candidate target | only if the branch witness is pre-registered and independent of the standard record | `T90`, `T91` |
| `y_std + y_aux(cost)` | reversal cost `C` can be a candidate target | only if the cost meter is calibrated and distinct from control-schedule bookkeeping or postselected success | `T93` |

### Smallest Honest Inverse Problem

The first admissible ML benchmark is not "recover all D1 axes without labels."

It is:

```text
Given a declared observable bundle (y_std, optional y_raw, optional y_aux),
classify which latent coordinates are identifiable, which are underidentified,
and when the model must abstain.
```

That benchmark should be physics-informed in the strict sense:

- the latent variables are declared before fitting;
- the observable channels are typed before fitting;
- symmetries and coarsening maps are explicit; and
- abstention is a success mode, not an error.

### Minimal Synthetic Benchmark Family

The smallest useful synthetic family would contain three case classes.

1. `standard_only_null`
   - Hold `y_std` fixed.
   - Vary only post hoc branch labels or post hoc undo labels.
   - Correct output: `B` and `C` are underidentified.

2. `provenance_requires_raw_logs`
   - Hold dashboard-level summaries fixed.
   - Vary hidden authenticated ancestry / intervention completions.
   - Correct output: `P` is underidentified from summaries and recoverable only
     from `y_raw`.

3. `independent_axis_candidate`
   - Hold standard monitored timelines fixed.
   - Vary only a declared independent branch witness or undo-cost meter.
   - Correct output: recover `B` or `C` only when the independent channel is
     present and pre-registered.

### What This Rules Out

This run rules out a large class of attractive-but-dishonest ML stories.

An inverse model should **not** be treated as evidence for TaF if it:

- predicts branch support from the same record already used by standard
  trajectory theory;
- predicts reversal cost from control-pulse bookkeeping or postselected undo
  success;
- predicts provenance from dashboard summaries alone; or
- reports a latent coordinate instead of abstaining when two distinct latent
  completions share the same declared observables.

## Proposed Next Action

If this lane is developed later, the next bounded step should be one explicit
synthetic identifiability benchmark, not a training pipeline.

Best next target:

1. define `z = (A, R, B, C, P)` and the three observable bundles
   `y_std`, `y_raw`, `y_aux`;
2. build paired fixtures with identical `y_std` but different latent
   completions;
3. require the model to output `recoverable`, `underidentified`, or `abstain`
   for each latent coordinate; and
4. only add regression/classification losses after the abstention benchmark is
   passed.

That would test identifiability honestly before introducing optimization
machinery that could hide non-identifiability behind label fitting.

## Claim-Status Posture

- No claim-status changes proposed.
- No roadmap or ledger changes proposed.
- Status of this run: exploratory inverse-problem boundary audit.
- Best current classification: the repo currently supports an
  abstention-aware identifiability benchmark with typed side channels, not an
  all-axis trajectory-only recovery claim.
