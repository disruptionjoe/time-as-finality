# T77: Measured Detector Policy Sensitivity

## Question

Does the T76 measured detector-provenance result survive stricter
pre-registered audit policy choices, or is the positive verdict only an effect
of a permissive acceptance corridor?

## Motivation

T76 made the detector branch executable as a measured-posterior claim, but it
still used one default policy corridor:

```text
confidence floor in [0.78, 0.85]
maximum false-class risk in [0.12, 0.22]
```

T77 stress-tests that policy dependence directly.

## Policy Families

- `strict`: high confidence, very low false-class risk;
- `baseline`: the T76 default corridor;
- `permissive`: weaker confidence and higher tolerated false-class risk.

## Success Criteria

- The signed measured fixture remains robust under strict and baseline
  corridors.
- The timing-only unsigned control remains withheld under strict and baseline
  corridors, and any permissive leakage is measured explicitly.
- The incomplete-pre-registration control does not become a clean positive by
  merely loosening policy bounds.
- The analysis exposes whether the signed positive verdict is policy-invariant
  or corridor-bounded.

## Failure Criteria

- The signed measured fixture is not robust under strict or baseline policy.
- The unsigned control recovers D1 at a substantial rate when policy is
  loosened.
- The incomplete-pre-registration control upgrades to robust solely because the
  policy becomes permissive.

## Claim Impact

If T77 passes, detector-level Q1 remains a bounded protocol claim:
measured evidence matters, but the admissible policy corridor must also be
declared before the result, because permissive policy may weaken the signed
versus unsigned discriminator.

If T77 fails, detector-level Q1 should be demoted again because the positive
result would be mostly a threshold-choice artifact.

## Reproduction

```bash
python -m unittest tests.test_measured_detector_policy_sensitivity -v
python -m models.run_t77
```
