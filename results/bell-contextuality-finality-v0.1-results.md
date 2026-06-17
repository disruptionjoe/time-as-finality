# Bell Contextuality Finality Results

Result: T21 focused tests pass `5/5`.

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

## Interpretation

T21 gives T13's sheaf obstruction a Bell/CHSH-style physical referent:

```text
local measurement records can be final in their contexts
without admitting one global noncontextual record assignment.
```

This is a finite contextuality certificate. It is not a quantum probability
simulation and does not derive Bell statistics.

## Reproduction

```bash
python -m unittest tests.test_bell_contextuality_finality -v
python -m models.run_t21
```

Machine-readable output:

- [bell-contextuality-finality-v0.1.json](bell-contextuality-finality-v0.1.json)
