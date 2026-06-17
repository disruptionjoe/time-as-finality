# T14 Integrated Observer-Context Finality Results

Result: T14 focused tests pass `5/5`; the current full branch suite passes
`83/83` after T16 was added.

## Pipeline

```text
hidden state
  -> record generation
  -> inherited expression
  -> observer coupling
  -> coarse-graining and proof validation
  -> Snowball-style reconciliation
  -> finality profile
  -> signed readout
```

## Main Witness

The core destructive observer sees three verified records with weights:

```text
1, -1, 1
```

Its finality profile is:

```text
(3, 3, 1, 3)
```

Its signed readout is:

```text
|1 - 1 + 1|^2 = 1
```

The constructive variant keeps the same topology, holders, proof status, and
finality profile, but changes the middle weight:

```text
1, 1, 1
```

The profile remains:

```text
(3, 3, 1, 3)
```

The readout becomes:

```text
|1 + 1 + 1|^2 = 9
```

Therefore the integrated pipeline preserves the T13 separation: finality
profiles do not determine signed readout.

## Observer And Context Effects

| Observer | Visible records | Profile | Readout |
| --- | ---: | --- | ---: |
| core verified | 3 | `(3, 3, 1, 3)` | `1.0` |
| gravity-only | 2 | `(2, 2, 1, 2)` | `4.0` |
| phase-silenced | 2 | `(2, 2, 1, 2)` | `4.0` |
| raw social | 5 | `(5, 5, 1, 5)` | `1.0` |
| verified social | 4 | `(4, 4, 1, 4)` | `0.0` |

The phase-silenced observer does not delete the stored phase record. It changes
expression and visibility. The stored record count remains 5.

## Proof And Consensus Limit

The proof stage rejects the forged social record. It does not reject the valid
dissent record, because validity checks relation satisfaction rather than
truth of the common claim.

In the Snowball-style probe, proof-carrying reconciliation reduces forged
false finality relative to raw Snowball, but valid dissent remains a failure
case. This preserves the T10 guardrail: protocol confidence is not physical
truth.

## Verdict

T14 supports the typed-pipeline interpretation:

- observer-relative finality profiles remain well typed;
- coupling and inherited expression alter access, not stored identity;
- proof validity filters forgery, not valid disagreement;
- consensus confidence is not truth;
- finality profiles still do not determine signed readout.

T14 does not derive quantum mechanics, replace relativity, prove a fractal
hierarchy, or turn distributed consensus into physical law.

## Reproduction

```bash
python -m unittest tests.test_t14_integrated_finality -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t14
```

Machine-readable output:

- [t14-integrated-finality-v0.1.json](t14-integrated-finality-v0.1.json)
