# S6 G6 Density-Matrix Bridge Results

Result: focused tests pass `5/5`.

Machine-readable output:

- [s6-g6-density-matrix-bridge-v0.1.json](s6-g6-density-matrix-bridge-v0.1.json)

## Status

This is G6 in the second S6 ambitious-goal sequence.

It replaces the analytic dephasing/channel profile with an explicit finite
system-environment quantum state:

```text
system qubit starts in |+>
five environment fragments start in |0>
fixed controlled rotations entangle pointer value with each fragment
reduced density matrices are computed by partial trace
```

Guardrail:

```text
Finite controlled-rotation state-vector fixture only: not a Hamiltonian, not
Lindblad dynamics, not an SBS theorem, and not source-side issuance evidence.
```

## Checks

| check | result |
| --- | --- |
| state density computed | pass |
| decoherence monotone | pass |
| redundancy threshold detected | pass |
| descent record stabilized | pass |
| `eta_F` loss detected | pass |

## Threshold

The first S6 density-matrix threshold appears at:

```text
strength             = 1.2
redundant fragments  = 4 / 5
offdiag magnitude    = 0.044349
gluing error         = 0.2
eta_F loss           = phase_sensitive_branch
```

Fragment mutual information at threshold:

| fragment | coupling | mutual information | redundant |
| --- | ---: | ---: | --- |
| E0 | `1.0` | `0.707027` | yes |
| E1 | `0.85` | `0.52167` | yes |
| E2 | `0.7` | `0.355965` | yes |
| E3 | `0.55` | `0.219624` | yes |
| E4 | `0.4` | `0.115821` | no |

System reduced density at threshold:

```text
[[0.5,      0.044349],
 [0.044349, 0.5]]
```

## Interpretation

G6 improves the S6 evidence stack because redundancy now arises from an
explicit finite quantum state and partial traces, not a hand-set fragment
profile.

The result supports the executable bridge shape:

```text
system-environment entanglement
  -> off-diagonal suppression
  -> fragment mutual information
  -> redundancy threshold
  -> final record descent
  -> phase-sensitive capability loss
```

## Verdict

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

## First Obstruction

The fixture still uses fixed controlled rotations. It is density-matrix
evidence for executability, not physical evidence for a generic
quantum-to-classical bridge.

The next goal is G7: add SBS-style conditional distinguishability and
independence scores over the same density-matrix fragments.

## Reproduction

```bash
python -m unittest tests.test_s6_g6_density_matrix_bridge -v
python -m models.run_s6_g6_density_matrix_bridge --output results/s6-g6-density-matrix-bridge-v0.1.json
```
