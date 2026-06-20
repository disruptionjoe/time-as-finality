# T74: Provenance Protocol Monte Carlo

## Question

Does T72's detector-provenance recovery occupy a broad region of protocol
space, or only a narrow engineered corner once clock error, batching,
authentication, trust, back-action, and DAG observability are sampled?

## Motivation

T72 established existence of robust, ambiguous, and unsafe regimes with
hand-picked parameter settings. That is not enough to decide whether the
detector branch of Q1 is generically plausible or physically fragile.

T74 replaces single witnesses with deterministic Monte Carlo stress priors over
three protocol families:

- `engineered_lab`: high trust, strong authentication, low back-action;
- `mixed_lab`: moderate instrumentation with realistic metadata loss;
- `field_degraded`: partial trust, partial observability, and degraded channels.

## Success Criteria

- Robust recovery is common only in the engineered family.
- Mixed or degraded priors are dominated by withhold or unsafe outcomes.
- The audit yields a sharper detector-branch statement than T72's existence
  table alone.

## Failure Criteria

- Robust recovery remains common under degraded priors.
- The family ordering is unstable or insensitive to authentication, trust,
  back-action, and DAG observability.
- The result depends on outcome-tuned thresholds rather than pre-registered
  protocol assumptions.

## Known Physics Constraints

- Passive detector statistics remain fixed; T74 audits provenance protocol
  assumptions, not measurement dynamics.
- No-signalling is unchanged from T66/T72 because no remote-setting channel is
  introduced.
- The priors are stress priors, not empirical calibration posteriors.

## Contribution Needed

Replace the stress priors with detector-specific calibration posteriors from a
concrete apparatus. If robust recovery does not survive measured parameters,
the detector branch of Q1 should be demoted further.
