# T219: C_flow / Record-Finality Integrated Guardrail

## Target Claims

- T210 executable `C_flow`
- T215 fixed-network record-finality split
- T218 reviewer packet

## Origin

The run needs a regression gate so future work cannot slide back from
capacity-aware flow or typed record capability into scalar timing rhetoric.

## Formal Target

Require future MTI/Cap_TI transport-record claims to pass:

```text
pytest tests/test_mti_cflow_solver.py tests/test_mti_lp_harmonic_sanity.py
```

## Setup / Fixtures

The integrated guardrail checks:

- LP vs harmonic mismatch;
- shared-edge path-harmonic insufficiency;
- `C_flow` disjoint/shared-prefix values;
- relabeling invariance;
- capacity monotonicity;
- fixed-network record-policy split.

## Positive Control

The current suite passes all checks.

## Negative Control

Any future claim that treats harmonic path time as `C_flow`, or transport
timing as record reconstructability, should fail this guardrail.

## Absorber Pass

The guardrail enforces native state completion before promotion.

## Results

Current verification:

```text
12 passed
```

## Verdict: promoted

Promoted as the integrated executable guardrail for this line.

## Falsification Conditions

Demote only if a stronger solver/test suite replaces it.

## Next Step

Commit and push the run so the guardrail is available to subsequent agents.
