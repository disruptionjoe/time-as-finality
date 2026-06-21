# Bell Contextuality Finality

## Abstract

T21 maps the T13 finality-sheaf obstruction to a Bell/CHSH-style
contextuality certificate. The model has four local measurement contexts. Each
context admits valid local finality sections, and the sections agree on named
single-setting overlaps. But no global assignment exists.

This gives the H1/sheaf obstruction a concrete physical referent: local
measurement records can be final in their own contexts without admitting a
single global noncontextual record assignment.

The first result is structural. The current extension adds probability-bearing
CHSH scores for three reference cases: classical noncontextual, quantum
Tsirelson, and PR-box no-signalling. It still does not simulate detector
dynamics, decoherence, or experimental noise.

## 1. Model

The model uses four measurement settings:

```text
Alice: A0, A1
Bob:   B0, B1
```

The four contexts are:

```text
A0B0 = same
A0B1 = same
A1B0 = same
A1B1 = different
```

Equivalently, using outcomes `{-1, +1}`:

```text
A0 * B0 = +1
A0 * B1 = +1
A1 * B0 = +1
A1 * B1 = -1
```

Each context has local finality sections:

```text
same      -> (-1, -1), (+1, +1)
different -> (-1, +1), (+1, -1)
```

## 2. Bell/CHSH Witness

Multiply the four observed context equations:

```text
(A0B0)(A0B1)(A1B0)(A1B1) = (+1)(+1)(+1)(-1) = -1
```

But if a single global assignment existed, the same product would be:

```text
A0^2 A1^2 B0^2 B1^2 = +1
```

This is the parity contradiction. The local contexts are individually
consistent, but no global assignment can satisfy all of them.

## 3. Finality-Sheaf Reading

T13 says local finality sections may fail to glue into a global section.
T21 gives a CHSH-shaped instance:

```text
local context sections exist
named overlaps are compatible
global finality section does not exist
```

The obstruction is not a pairwise failure. It is a global-section failure.
That is why the result belongs to the sheaf/H1 layer rather than to the
quorum-safety layer tested by T20.

## 4. Relationship To T20

T20 showed that quorum-intersection safety transfers from distributed
consensus into physical-record finality. That theorem blocks two directly
contradictory final certificates when enough holders overlap.

T21 shows the next layer. Even when local records are valid in every context,
there may be no global noncontextual assignment. The issue is not direct
certificate contradiction; it is contextual gluing failure.

## 5. Probability-Bearing CHSH Extension

T21 now compares three correlation models:

| Model | CHSH score | Global assignment? | Interpretation |
| --- | ---: | --- | --- |
| classical deterministic | `2.0` | yes | noncontextual baseline |
| quantum Tsirelson target | `2.8284271247461903` | no | quantum contextual target |
| PR-box no-signalling extreme | `4.0` | no | post-quantum no-signalling boundary |

The bounds are:

```text
classical <= 2
quantum <= 2*sqrt(2)
no-signalling <= 4
```

The quantum model uses angle correlations:

```text
E(A, B) = cos(theta_A - theta_B)
```

with settings chosen to produce:

```text
S = E(A0B0) + E(A0B1) + E(A1B0) - E(A1B1) = 2*sqrt(2)
```

The finality reading is:

```text
classical: global noncontextual section available
quantum: local probability-bearing sections without global classical section
PR-box: no-signalling local sections beyond quantum finality constraints
```

This makes the Bell bridge numerical rather than only parity-based.

## 6. Claim Impact

T21 strengthens [Q1](claims/Q1-quantum-under-finalization.md): quantum
under-finalization now has a finite contextuality model where local classical
records exist but global classical assignment fails.

T21 strengthens [T13](tests/T13-finality-sheaf-cohomology.md): the H1/sheaf
obstruction now has a Bell/CHSH-style physical referent.

T21 narrows [A1](claims/A1-distributed-systems-finality-analogy.md):
distributed quorum safety is useful, but contextuality/global-section failure
requires the sheaf layer.

## 7. Limits

- The model is finite.
- The probability extension uses ideal correlation formulas; it does not
  simulate detectors, amplitudes, decoherence, or spacetime
  separation.
- It gives a contextuality and CHSH-score certificate, not a full Bell
  experiment.

## 8. Reproduction

```bash
python -m unittest tests.test_bell_contextuality_finality -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t21
```

Machine-readable output:

- [results/bell-contextuality-finality-v0.1.json](results/bell-contextuality-finality-v0.1.json)

Human-readable result note:

- [results/bell-contextuality-finality-v0.1-results.md](results/bell-contextuality-finality-v0.1-results.md)
