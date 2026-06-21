# Technical Report: Provenance Protocol Monte Carlo v0.1

## Claim Under Test

T72 showed that detector provenance recovery is possible under explicit
physical protocol assumptions and can fail conservatively or unsafely. T74 asks
the next question: are the successful regimes broad, or do they occupy only a
narrow engineered corner of protocol space?

## Model

T74 keeps T72's hostile witness pair fixed:

- dependent copied archive;
- independent overlapping readout.

It also keeps passive detector statistics fixed, so the audit remains about
provenance protocol rather than outcome statistics.

The new ingredient is deterministic Monte Carlo sampling over three stress
prior families:

1. `engineered_lab`: tight clocks, strong authentication, high trust, low
   perturbation back-action, and high DAG observability.
2. `mixed_lab`: moderate metadata loss, moderate trust, wider timing/batching
   uncertainty, and occasional threshold-source failure.
3. `field_degraded`: partial trust, larger batching and timing uncertainty,
   weaker authentication, higher back-action, and partial ancestry visibility.

For each sampled protocol, T74 asks whether the T72 rule yields:

- robust provenance recovery;
- conservative withhold;
- threshold-dependent withhold;
- false independence risk;
- false dependence risk.

## Current Strongest Claim

Robust detector-provenance recovery is not generic. In the T74 audit it lives
in a high-trust, low-back-action, high-authentication corner and declines
rapidly under broader stress priors.

## What This Improved

T74 converts T72's existence result into a phase-volume statement. That is more
decision-relevant. A serious evaluator can now ask not only "is recovery
possible?" but "how engineered must the detector stack be before recovery is
the typical outcome rather than a special case?"

This sharpens the project's detector claim into something falsifiable:

```text
If measured detector protocols resemble the mixed/degraded stress families more
than the engineered family, detector-level Q1 should be demoted.
```

## What This Weakened

T74 weakens any reading of Q1 that treats detector-level provenance recovery as
even roughly generic. In the present audit, the mixed and degraded families
lose robust recovery entirely and are dominated by conservative withhold
outcomes, with threshold-dependence taking the remaining share.

That makes the detector branch an engineered instrumentation thesis, not a
general measurement thesis.

## Main Limitation

The priors are stress priors rather than measured calibration posteriors. T74
therefore quantifies fragility, not actual device frequencies.

## Recommendation

Keep Q1 `partially_supported`, but narrow the detector branch further:

```text
Detector-level D1 claims are credible only for apparatuses whose measured
provenance protocol parameters place them inside the engineered recovery region.
```

## Next Work

Choose one concrete detector or logging stack and infer posteriors for:

- clock uncertainty;
- archive batching;
- signature retention and verification;
- subsystem trust boundaries;
- perturbation back-action;
- provenance-DAG observability.

Then rerun T74 with measured rather than synthetic priors.

## Reproduction

```bash
python -m unittest tests.test_provenance_protocol_monte_carlo -v
python -m models.run_t74
```
