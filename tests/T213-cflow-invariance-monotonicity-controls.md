# T213: C_flow Invariance And Monotonicity Controls

## Target Claims

- T210 executable `C_flow` solver
- T212 projection-insufficiency witness

## Origin

Before using `C_flow` as a guardrail, it needs basic sanity controls:
representation invariance and capacity monotonicity.

## Formal Target

Check:

```text
isomorphic relabeling preserves C_flow
increasing a bottleneck capacity does not increase C_flow
shared-edge detection distinguishes proxy-only from flow-sensitive fixtures
```

## Setup / Fixtures

Use:

```text
disjoint_two_path_network()
shared_prefix_two_path_network()
```

from `models/mti_cflow_solver.py`.

## Positive Control

Doubling the shared-prefix capacity lowers `C_flow`.

## Negative Control

Pure relabeling preserves `C_flow`.

## Absorber Pass

These are ordinary network model invariants. If they failed, the executable
suite would be too fragile for research use.

## Results

Pytest verifies relabeling invariance, bottleneck capacity improvement, and
shared-edge detection.

## Verdict: promoted

Promoted as the basic executable control suite for `C_flow`.

## Falsification Conditions

Demote if future solver changes violate these invariants.

## Next Step

T214 revisits refinement once capacity state is explicit.
