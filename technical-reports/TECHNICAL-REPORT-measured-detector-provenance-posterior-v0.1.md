# Technical Report: Measured Detector Provenance Posterior v0.1

## Claim Under Test

T75 showed that a source-anchored, posterior-modeled photon time-tagging stack
can be mapped into the T74 engineered recovery region, but its non-timing
posterior ranges were still plausible engineering ranges. T76 asks whether the
detector branch can be made testable by replacing those ranges with a measured
deployment-evidence schema.

## Artifact

T76 adds an executable adapter:

```text
measured deployment evidence
  -> conservative posterior ranges
  -> T74 PriorFamily
  -> T74 Monte Carlo classifier
```

The adapter accepts timing estimates, event-loss counts, signature and forgery
trials, trust-boundary checks, perturbation responses, DAG-observability counts,
and pre-registration coverage. Bernoulli fields are converted into conservative
Laplace-smoothed intervals. Timing fields are converted into explicit
measurement-plus-uncertainty intervals. Acceptance thresholds remain a separate
pre-registered audit policy.

## Controls

T76 includes three fixtures:

- `measured_signed_time_tag_stack`: measured-style signed provenance fixture;
- `timing_only_unsigned_control`: same timing evidence, degraded provenance
  evidence;
- `signed_stack_incomplete_preregistration_control`: strong signed evidence but
  incomplete threshold pre-registration.

These controls prevent two overclaims:

- high-resolution timing is not counted as D1 provenance;
- strong instrumentation is not upgraded when thresholds are selected after the
  fact.

## Current Strongest Claim

Detector-level D1 finality can be tested as a measured provenance-protocol
claim: deployment evidence can be converted into T72/T74 posterior coordinates
before D1 scoring.

## What This Improved

The T75 blocker is now executable. A future experimentalist no longer needs to
guess what "measured posteriors" means for this branch. The required fields and
classification path are explicit enough to fail.

## What This Weakened

T76 weakens T75 by refusing to treat plausible engineering priors as measured
support. If a deployment lacks authentication, trust-boundary, perturbation, and
DAG evidence, D1 provenance recovery is withheld even when timing evidence is
unchanged.

## Falsification Condition

The detector branch should be demoted if a real deployment's measured posterior
either withholds D1, produces false independence or false dependence risk, or
only succeeds after weakening pre-registered confidence and false-risk policy
bounds.

## Claim Ledger Update

Q1 should remain `partially_supported` with a narrower scope:

```text
Detector-level D1 finality is operational only as a measured,
pre-registered provenance-protocol claim over already formed detector records.
It is not supported by detector timing, calibrated POVM outcomes, or passive
correlations alone.
```

No upgrade is warranted until a real deployment populates the T76 evidence
schema.

## Next Work

Populate the T76 schema from one actual lab run:

- event-loss logs;
- signature-verification failures;
- replay and forgery trials;
- perturbation controls;
- trust-boundary audits;
- DAG truncation and false-edge counts.

## Reproduction

```bash
python -m unittest tests.test_measured_detector_provenance_posterior -v
python -m models.run_t76
```
