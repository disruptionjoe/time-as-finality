# Bell Contextuality Finality Results

Result: T21 focused tests pass `10/10`.

## Model

T21 uses four CHSH-style contexts:

```text
A0B0 = same
A0B1 = same
A1B0 = same
A1B1 = different
```

Each context has two local sections:

```text
same      -> (-1, -1), (1, 1)
different -> (-1, 1), (1, -1)
```

## Checks

| Check | Result |
| --- | --- |
| all local sections exist | pass |
| contexts compatible on named overlaps | pass |
| no global assignment exists | pass |
| H1-style obstruction detected | pass |

## Contextuality Witness

The observed context parities multiply to:

```text
(+1)(+1)(+1)(-1) = -1
```

But any global assignment to `A0`, `A1`, `B0`, and `B1` would multiply each
variable twice:

```text
A0^2 A1^2 B0^2 B1^2 = +1
```

So local finality sections exist, but no global finality section exists.

## Probability-Bearing CHSH Models

T21 now compares three probability-bearing cases:

| Model | CHSH score | Global assignment? | Status |
| --- | ---: | --- | --- |
| classical deterministic | `2.0` | yes | classical bound |
| quantum Tsirelson target | `2.8284271247461903` | no | exceeds classical, respects Tsirelson |
| PR-box no-signalling extreme | `4.0` | no | exceeds Tsirelson, post-quantum |

The bounds are:

```text
classical <= 2
quantum <= 2*sqrt(2)
no-signalling <= 4
```

The quantum target uses angle correlations to reach `2*sqrt(2)`. The PR-box
case preserves no-signalling but exceeds the quantum bound.

## Interpretation

T21 gives T13's sheaf obstruction a Bell/CHSH-style physical referent:

```text
local measurement records can be final in their contexts
without admitting one global noncontextual record assignment.
```

The first T21 result is a finite contextuality certificate. The probability
extension adds the standard CHSH numerical separation, but still does not
simulate detector dynamics, decoherence, or experimental noise.

## Reproduction

```bash
python -m unittest tests.test_bell_contextuality_finality -v
python -m models.run_t21
```

Machine-readable output:

- [bell-contextuality-finality-v0.1.json](bell-contextuality-finality-v0.1.json)
