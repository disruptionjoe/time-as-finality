# P38 - Financial Risk Modeler Run

- persona: Financial Risk Modeler
- goal_id: P38
- run_timestamp: 2026-06-21T23:09:18-05:00
- queue_source: `explorations/persona-future-run-goals-2026-06-20.md`
- goal: Add adversarial tail regimes and rare-event stress tests for false
  independence, false dependence, and correlated provenance failures.
- posture: bounded exploratory run only; no claim-status update, roadmap
  change, or ledger edit.

## Repo Context Read

- `models/physical_provenance_protocol.py`
- `models/provenance_protocol_monte_carlo.py`
- `models/povm_correlation_provenance_obstruction.py`
- `models/intervention_sensitive_detector_provenance.py`
- `models/detector_provenance_robustness.py`
- `tests/T70-detector-provenance-robustness.md`
- `tests/test_provenance_protocol_monte_carlo.py`
- `tests/test_detector_provenance_robustness.py`
- `explorations/persona-goal-runs/2026-06-21-035235-p19-causal-inference-detector-dag-audit.md`

## Bounded Run

Question: if detector provenance is judged like an operational risk book rather
than an average-case lab note, what happens in rare adversarial tails?

Method:

1. Reuse the existing T72/T74 protocol model rather than invent a new detector
   theory.
2. Hold the witness family fixed: copied archive versus independent overlapping
   readout.
3. Sample three adversarial prior families with deterministic seed `74017` and
   `5000` samples each:
   - false-independence tail;
   - false-dependence tail;
   - correlated multi-channel failure tail.
4. Keep `threshold_source = declared_physical_protocol` for all samples so the
   run measures protocol-tail risk, not ad hoc threshold dependence.

## Tail Families

### 1. False-independence tail

Bias the prior toward copied archives being misread as distinct:

- high spoofed-independent probability;
- moderate-to-high forgery probability;
- poor DAG observability and heavy truncation;
- enough trust and verification to let forged distinct-tag evidence sometimes
  clear the acceptance floor.

### 2. False-dependence tail

Bias the prior toward independent readouts being misread as copied:

- intervention channel almost always changes both records;
- low back-action penalty, so the contaminated perturbation still looks
  trustworthy;
- weak tag uniqueness and noisy DAGs, so the dependence channel dominates.

### 3. Correlated multi-channel failure tail

Degrade several channels together:

- middling trust;
- partial observability and truncation;
- moderate forgery;
- substantial intervention back-action;
- no single channel clean enough to clear both confidence and false-risk gates.

## Results

Baseline from T74, rerun at the same `5000`-sample scale:

| family | robust | withhold | threshold-dependent | false independence | false dependence |
| --- | ---: | ---: | ---: | ---: | ---: |
| engineered_lab | 90.82% | 9.18% | 0.00% | 0.00% | 0.00% |
| mixed_lab | 0.02% | 90.82% | 9.16% | 0.00% | 0.00% |
| field_degraded | 0.00% | 71.08% | 28.92% | 0.00% | 0.00% |

Adversarial tail rerun:

| family | robust | withhold | threshold-dependent | false independence | false dependence | computable D1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| false_independence_tail | 0.00% | 99.62% | 0.00% | 0.38% | 0.00% | 0.00% |
| false_dependence_tail | 0.00% | 98.66% | 0.00% | 0.00% | 1.34% | 1.16% |
| correlated_failure_tail | 0.00% | 100.00% | 0.00% | 0.00% | 0.00% | 0.00% |

## Exemplar Tail Witnesses

### False independence rare tail

Sample `259` produced a copied archive classified as distinct:

- accepted channel: `authenticated_distinct_origin_tags`;
- copied witness status: `false_independence_risk`;
- independent witness status: `withhold_ambiguous`;
- notable parameters:
  - `spoof_independent_prob = 0.9224`
  - `forgery_prob = 0.3058`
  - `observability = 0.1623`
  - `truncation_prob = 0.7074`

Interpretation: once DAG recovery is weak enough, a forged distinct-origin path
can occasionally clear the protocol's own risk ceiling and create a false
upgrade even though almost all nearby samples still withhold.

### False dependence rare tail

Sample `5` produced an independent readout classified as copied:

- accepted channel: `perturbation_change_response`;
- copied witness status: `accepted_same_class`;
- independent witness status: `false_dependence_risk`;
- notable parameters:
  - `p_change_if_independent = 0.9483`
  - `back_action_prob = 0.0209`
  - `false_shared_edge_prob = 0.2978`

Interpretation: an intervention channel that looks clean in aggregate can still
be adversarially contaminated into a false dependence signal when independent
readouts are highly coupled under perturbation.

### Correlated failure tail

The very first sampled regime already forced clean abstention for both witness
types:

- no accepted channels at all;
- copied witness status: `withhold_ambiguous`;
- independent witness status: `withhold_ambiguous`;
- strongest individual channel confidence stayed below `0.40`.

Interpretation: correlated degradation behaves less like a graceful weakening
and more like a market freeze. The protocol does not drift smoothly into a
slightly worse classification regime; it usually loses the right to classify.

## Main Finding

The detector branch is **tail-dominated** in a specific way:

1. Average-case Monte Carlo can hide the relevant operational risk.
2. False upgrades are rare under adversarial tails, but they are real and
   mechanistically legible.
3. Correlated channel failures are more dangerous as a **classification-right
   collapse** than as a large-volume false-upgrade source.

That last point matters. The biggest detector-provenance risk in this bounded
run is not "lots of wrong answers." It is "the protocol no longer earns any
answer, but pressure may still exist to classify anyway."

## Smallest Honest Upgrade To The Branch

The useful addition is not a new theorem. It is a risk posture:

```text
detector provenance protocol
+ tail-family stress book
+ explicit false-upgrade exceedance rates
+ correlated-failure abstention region
```

This is compatible with the current detector framing as an admissibility
protocol rather than detector physics.

## Proposed Next Action

If this lane is extended later, the next bounded move should be P88-style:
build a finite correlated-tail witness set where replay, spoofing, omission,
drift, policy thresholds, and authority compromise are combined intentionally
rather than through broad priors alone.

## Claim-Status Posture

- No claim-status changes proposed.
- No roadmap or ledger changes proposed.
- Status of this run: exploratory detector tail-risk audit.
- Best current classification: the detector branch remains operationally
  narrow, and its most important failure surface is joint provenance-channel
  collapse plus rare false-upgrade tails.
