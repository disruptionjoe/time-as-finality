# T100: Detector Authority-Domain Bound

## Route

Quantum measurement / classical records.

## Question

After T98 identified admissible and inadmissible staffing examples, what is
the exact minimal number of authority domains required by the current T97
packet? Is the four-domain requirement a contingent example, or a structural
lower bound?

## Motivation

The detector branch is already narrow. If its surviving real-deployment path
depends on organizational separation, that dependence should be stated exactly.
An explicit lower bound is more valuable than more example profiles because it
tells a skeptical reader when a proposed lab deployment is dead on arrival.

## Success Criteria

- Enumerate every partition of the five T97 authority domains.
- Reject every partition that violates trust-auditor independence or the
  governance/control/archive separation rule.
- Determine the exact minimal admissible authority count.
- List the surviving minimal merge classes.

## Failure Criteria

- The result relies only on hand-picked examples.
- The trust-auditor independence rule is not enforced structurally.
- The report treats an operational staffing bound as detector evidence.

## Claim Impact

If T100 passes, Q1 remains `partially_supported`, but the detector branch
narrows again: under the current packet, any proposed deployment with fewer
than four authority domains should be rejected before data collection.

## Reproduction

```bash
python -m unittest tests.test_detector_authority_domain_bound -v
python -m models.run_t100
```
