# T13 v0.1 Results: Signed And Interfering Readout

Date: 2026-06-16

## Reproduction

```bash
python -m unittest tests.test_t13_signed_readout tests.test_t13_characterization -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t13
```

Result: T13 focused tests pass `15/15`; the current full branch suite passes
`91/91` after T17 was added.
Machine-readable output:
[t13-signed-readout-v0.1.json](t13-signed-readout-v0.1.json).

## Separation Result

On a finite causal record graph with no global time order, using the
observer-indexed finality profile of `FORMALISM.md`:

1. W1 gives identical finality profiles with different readouts. The
   profiles are `(2,2,2,2)` in both cases; Born-style readouts are `4.0` and
   `0.0`. Therefore no function from finality profiles to readouts exists.
2. W2 gives a causal chain where evidence count and every profile dimension
   grow monotonically while readout follows `1.0, 0.0, 1.0`. Therefore no
   monotone relationship from profile to readout survives even along one
   trajectory.
3. The measure has nonzero pairwise interference: `I2 = 2.0` for constructive
   pairing and `I2 = -2.0` for destructive pairing.
4. `I3 = 0` is checked two ways: numerically over 200 random complex
   configurations and symbolically by coefficient cancellation.
5. Observer consistency holds. Different access can change readout, but equal
   access gives equal readout.
6. Temporal reconstruction is weight-blind.

## Honesty Clauses

- Linear signed readout is trivial. It factors exactly as `P - N` through two
  monotone counters.
- Phase-class counters recover the Born-style readout. The result is not that
  no monotone bookkeeping can recover readout. The result is that the
  phase-blind finality profile cannot.
- This is a structural result on weighted record graphs. It does not derive
  quantum mechanics, the Born rule, or an interference experiment.

## Limits

- Witnesses use two or three records.
- The readout map is fixed to `|sum w(r)|^2`.
- Robustness under larger graphs, mixed T12 channels, and T9-style dynamical
  record generation remains open.

## Verdict

T13 supports [C3](../claims/C3-signed-readout-separation.md): record
evidence, finality profile, temporal reconstruction, and signed readout are
separate typed stages. The strongest publishable result is the finite witness
separating finality profile from readout.
