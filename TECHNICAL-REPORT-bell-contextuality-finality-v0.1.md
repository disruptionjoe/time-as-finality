# Bell Contextuality Finality

## Abstract

T21 maps the T13 finality-sheaf obstruction to a Bell/CHSH-style
contextuality certificate. The model has four local measurement contexts. Each
context admits valid local finality sections, and the sections agree on named
single-setting overlaps. But no global assignment exists.

This gives the H1/sheaf obstruction a concrete physical referent: local
measurement records can be final in their own contexts without admitting a
single global noncontextual record assignment.

The result is structural. It does not simulate quantum amplitudes, derive Bell
probabilities, or claim to reproduce a full laboratory Bell experiment.

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

## 5. Claim Impact

T21 strengthens [Q1](claims/Q1-quantum-under-finalization.md): quantum
under-finalization now has a finite contextuality model where local classical
records exist but global classical assignment fails.

T21 strengthens [T13](tests/T13-finality-sheaf-cohomology.md): the H1/sheaf
obstruction now has a Bell/CHSH-style physical referent.

T21 narrows [A1](claims/A1-distributed-systems-finality-analogy.md):
distributed quorum safety is useful, but contextuality/global-section failure
requires the sheaf layer.

## 6. Limits

- The model is finite and parity-based.
- It does not calculate quantum probabilities.
- It does not simulate detectors, amplitudes, decoherence, or spacetime
  separation.
- It gives a structural contextuality certificate, not a full Bell experiment.

## 7. Reproduction

```bash
python -m unittest tests.test_bell_contextuality_finality -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t21
```

Machine-readable output:

- [results/bell-contextuality-finality-v0.1.json](results/bell-contextuality-finality-v0.1.json)

Human-readable result note:

- [results/bell-contextuality-finality-v0.1-results.md](results/bell-contextuality-finality-v0.1-results.md)
