# T86: Ambiguous-Tag Channel Independence

## Route

Quantum measurement / classical records.

## Question

If timing and authenticated tags are intentionally ambiguous, can perturbation
response or signed provenance-DAG evidence independently recover the copied
versus independent detector-record partition in the existing T74/T76 protocol
audit?

## Motivation

T83 made the detector branch null unless it beats passive statistics,
dashboards, and post hoc provenance declarations. T85 then narrowed the
current executable route to:

```text
pre-registration gate
  + trust-boundary gate
  + authenticated-tag sufficiency
```

The remaining high-value issue is whether perturbation response and DAG
observability are removable ornamentation or whether they can be made
load-bearing in a clean raw-log fixture where tags are deliberately ambiguous.

## Construction

- Keep trust boundaries and pre-registration at the signed T76 values.
- Make timing, tag retention, signature verification, spoof resistance, and
  unique-tag evidence ambiguous.
- Compare five raw-log-count fixtures:
  - all channels ambiguous;
  - clean perturbation response only;
  - perturbation response contaminated by back-action;
  - clean signed ancestry DAG only;
  - signed ancestry contaminated by truncation and false shared edges.
- Reuse the T74 Monte Carlo audit and T76 measured-posterior adapter.

## Success Criteria

- The all-ambiguous control withholds D1.
- Clean perturbation-only evidence or clean DAG-only evidence can recover both
  canonical witness classes under ambiguous timing/tags.
- The contaminated controls withhold rather than producing false support.
- The report states that this is an internal fixture witness, not empirical
  detector support.

## Failure Criteria

- The all-ambiguous control recovers D1.
- The clean perturbation/DAG fixtures do not recover under the same policy.
- Contaminated perturbation/DAG fixtures recover despite back-action,
  truncation, or false shared-edge risk.
- The result is used to claim a detector dynamics law rather than a
  provenance-admissibility condition.

## Known Physics Constraints

- No collapse mechanism, Born-rule derivation, or detector dynamics are
  introduced.
- The audit operates on already formed classical detector records.
- Any real experimental upgrade still requires a T78-style pre-registered,
  event-level raw-log deployment.

## Contribution Needed

Use T86 to specify the raw-log columns for a real detector run: copied and
independent controls, perturbation trials, signed ancestry exports, tag
ambiguity rates, timing uncertainty, trust-boundary checks, and demotion rules.
