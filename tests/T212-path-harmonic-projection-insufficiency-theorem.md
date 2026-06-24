# T212: Path-Harmonic Projection Insufficiency Theorem

## Target Claims

- Capability Projection
- T211 executable same-harmonic split
- T203 corrected finite DAG capability

## Origin

T211 gives a pair of finite networks where the visible path-harmonic summary is
the same but `C_flow` differs.

## Formal Target

Let:

```text
pi_H(D) = harmonic_mean(free source-to-sink path times)
Cap(D) = C_flow(D,q)
```

Then `pi_H` is not capability-sufficient for `Cap` over the admissible class of
finite path networks with shared edges.

## Setup / Fixtures

Use the T211 disjoint/shared-prefix pair:

```text
pi_H(D) = pi_H(S) = 2
C_flow(D) = 8/3
C_flow(S) = 10/3
```

## Positive Control

If incidence/capacity state is included, the pair separates visibly and the
corrected projection can determine the capability.

## Negative Control

If only free path times are visible, the pair collapses and the capability
spread is non-singleton.

## Absorber Pass

Network-flow state completion absorbs the failure: add edge incidence,
capacities, demand, and delay law. The residue is formal audit value, not a new
transport theorem.

## Results

The capability spread over the visible harmonic fiber `{T_H=2}` contains:

```text
{8/3, 10/3}
```

so the spread is non-singleton.

## Verdict: promoted

Promoted as a clean finite projection-insufficiency witness for the corrected
transport capability.

## Falsification Conditions

Demote if the admissible class forbids shared edges or declares incidence and
capacity as visible state.

## Next Step

T213 tests invariance and monotonicity controls for the corrected projection.
