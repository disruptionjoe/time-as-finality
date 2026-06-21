# Technical Report: Physical Provenance Protocol v0.1

## Claim Under Test

T68 showed that intervention-sensitive provenance metadata can separate copied
archives from independent readout chains when passive detector statistics are
identical. T70 showed that this result survives some Boolean metadata
degradations but fails when trusted channels are absent or threshold-dependent.

T72 asks a stricter question: can those trusted channels be represented as a
physical protocol with explicit uncertainty, authentication, batching, trust,
back-action, and DAG-observability parameters?

## Model

T72 keeps the T68 hostile pair:

- dependent copied archive;
- independent overlapping readout.

Both retain identical passive statistics:

```text
agreement = 0.92
phi       = 0.84
```

The model replaces Boolean degradation flags with protocol-valued parameters:

- timestamp error bounds and archive batching windows;
- declared copy-latency intervals;
- tag retention, verification, forgery, spoofing, and independent-tag
  uniqueness probabilities;
- detector/archive/transport trust multipliers;
- perturbation response and back-action probabilities;
- signed-edge probability, DAG observability, DAG truncation, and false shared
  ancestry probability.

## Pre-Registered Acceptance Rule

Each channel produces:

```text
support in {same, distinct, none}
confidence
false_risk
```

The channel is accepted only when:

```text
confidence >= confidence_floor
false_risk <= max_false_risk
threshold_source = declared_physical_protocol
```

D1 is computed only after the protocol fixes a partition. If no channel clears
the declared bounds, if accepted channels conflict, or if the threshold source
is ad hoc, D1 is withheld.

## Regime Table

T72 produces five kinds of regime outcome:

1. robust provenance recovery;
2. ambiguous / withhold region;
3. threshold-dependent provenance failure;
4. false independence risk;
5. false dependence risk.

The robust regimes show that provenance recovery is not impossible in
principle. The risk regimes show that it is unsafe without physical protocol
assumptions.

## Current Strongest Claim

A physical provenance protocol can fix D1 independence classes before finality
scoring when at least one dependence channel and one independence channel clear
declared reliability bounds from the protocol rather than ad hoc post hoc
thresholds.

## What This Improved

T72 replaces T70's Boolean flags with explicit protocol parameters. The detector
branch now has a concrete next interface: clock distributions, authentication
failure rates, archive batching, trust boundaries, back-action matrices, and
DAG observability can be varied before D1 scoring.

This makes Q1 more testable. A detector implementation can now be asked:

```text
Do its provenance channels land in robust recovery, withhold, false
independence, or false dependence regimes?
```

## What This Weakened

T72 makes the detector branch more fragile, not stronger. The result is
protocol-relative. In hostile regimes, forged tags can create false
independence, and perturbation back-action can create false dependence.

Therefore TaF should not claim detector-level provenance recovery without
explicit physical protocol assumptions.

## Minimal Physical Conditions

Non-arbitrary D1 detector finality requires:

- declared clock/error bounds;
- authenticated tags or signed ancestry with high verification probability;
- trusted detector/archive/transport boundaries;
- bounded archive batching;
- a perturbation channel whose back-action risk is below the protocol's
  false-risk ceiling;
- acceptance thresholds justified by the protocol, not tuned to D1 outcomes.

## Falsification Criterion

The detector branch should be demoted if physically realistic protocol
parameters generically fall into withhold, false independence, or false
dependence regimes.

It should also be demoted if the confidence floors and false-risk ceilings
cannot be justified independently of the desired D1 result.

## Q1 Recommendation

Keep Q1 `partially_supported`, but narrow the detector branch to:

```text
D1 is a detector-record provenance accounting predicate under explicit physical
protocol assumptions.
```

Do not claim provenance recovery from detector outcomes alone.

## Next Work

Replace the finite regime table with calibration data or a Monte Carlo protocol
simulation over:

- clock distributions;
- signature failure probabilities;
- archive batching distributions;
- subsystem trust boundaries;
- perturbation back-action matrices;
- partial DAG observability.

## Reproduction

```bash
python -m unittest tests.test_physical_provenance_protocol -v
python -m models.run_t72
```
