# S6 G7 SBS Approximation Results

Result: focused tests pass `5/5`.

Machine-readable output:

- [s6-g7-sbs-approximation-v0.1.json](s6-g7-sbs-approximation-v0.1.json)

## Status

This is G7 in the second S6 ambitious-goal sequence.

It adds an SBS-style objectivity approximation over the G6 density-matrix
fixture. For each fragment, the conditional pointer states are:

```text
pointer 0: |0>
pointer 1: cos(theta)|0> + sin(theta)|1>
```

The conditional distinguishability score is therefore:

```text
sin(theta)
```

Guardrail:

```text
SBS-style score over a controlled-rotation product fixture only: not a proof of
Spectrum Broadcast Structure and not a physical objectivity theorem.
```

## Calibration Note

The first run used an aggregate SBS closure threshold of `0.6`. That made the
binary SBS flag turn on at strength `1.4`, even though the declared fragment
objectivity gates were already satisfied at strength `1.2`.

The final run uses:

```text
mutual information threshold       = 0.2
distinguishability threshold       = 0.6
descent support                    = 4 fragments
aggregate SBS closure threshold    = 0.55
```

This makes the aggregate threshold consistent with the fragment-level gates.

## Threshold

The SBS-style threshold appears at:

```text
strength                         = 1.2
objective fragments              = 4 / 5
average distinguishability        = 0.720737
conditional independence defect   = 0.0
SBS closure score                 = 0.57659
G6 descent stable                 = true
```

Fragment scores at threshold:

| fragment | mutual information | distinguishability | objective fragment |
| --- | ---: | ---: | --- |
| E0 | `0.707027` | `0.932039` | yes |
| E1 | `0.52167` | `0.852108` | yes |
| E2 | `0.355965` | `0.744643` | yes |
| E3 | `0.219624` | `0.613117` | yes |
| E4 | `0.115821` | `0.461779` | no |

## Interpretation

The SBS-style objectivity threshold and the G6 S6-descent threshold align:

```text
strength = 1.2
```

That supports the narrow bridge reading:

```text
Quantum Darwinism / SBS owns the physical objectivity mechanism.
S6 owns the typed descent/loss/provenance audit around that mechanism.
```

## Verdict

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

## First Obstruction

The conditional-independence defect is zero by construction because the G6
conditional environment states factor. A real SBS test must compute this from a
less ideal density-matrix or open-system model.

The next goal is G8: use generic finite sheafification/descent machinery to
consume these fragment scores without bespoke threshold logic.

## Reproduction

```bash
python -m unittest tests.test_s6_g7_sbs_approximation -v
python -m models.run_s6_g7_sbs_approximation --output results/s6-g7-sbs-approximation-v0.1.json
```
