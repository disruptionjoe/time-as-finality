# Compositional Finality v0.1 Results

Date: 2026-06-11

## Reproduction

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_compositional_finality
```

Machine-readable output is in
[`compositional-finality-v0.1.json`](compositional-finality-v0.1.json).

## Evidence-State Algebra

Provenance-preserving token union satisfies:

| Law | Result |
| --- | --- |
| associative | pass |
| commutative | pass |
| idempotent | pass |

This is the CRDT-like layer of the model.

## Complete Four-Source Sweep

The sweep evaluates 15 non-empty evidence states and all 225 ordered pairs.

| Quantity | Result |
| --- | ---: |
| transparent merge monotonicity | 1.000000 |
| conflict-free decision preservation | 1.000000 |
| merged profile equals componentwise LUB | 0.511111 |
| provenance checkpoint preserves support | 1.000000 |
| provenance checkpoint preserves holders | 0.266667 |
| provenance checkpoint preserves branches | 0.266667 |
| lossy checkpoint preserves support | 0.266667 |

The underlying evidence join is clean. The observer-facing profile is not the
same algebra.

## Minimal Counterexamples

1. **Profile join failure, two records.** Two profiles `(1,1,1,1)` have
   componentwise LUB `(1,1,1,1)`, while their physical merge is `(2,2,2,2)`.
2. **Conflict, two records.** Each local record resolves at threshold one;
   their opposing values merge to no unique decision.
3. **Duplicate inflation, two tokens.** Naive support is two while unique
   provenance support is one.
4. **Coarse-graining order change, two records.** Different checkpoint
   policies reverse the before/after comparison.
5. **Local-to-global obstruction, two contexts.** Each assignment is locally
   valid, but they assign different values to the shared variable.
6. **Inherited expression, one record.** The same stored source has support
   one when expressed, zero after inherited silencing, and one after local
   reprogramming.

## Depth And Grouping

- every depth from zero through 1,024 was evaluated;
- neutral profiles were invariant across depth;
- inherited silencing reached the record at every positive depth;
- neutral grouping preserved evidence in all 500 randomized trials;
- local versus ancestor placement of the same mark produced different visible
  evidence in all 500 targeted comparisons.

This supports arbitrary finite recursion in the model. It does not establish
an infinite hierarchy or fractal scaling law.

## Verdict

The strongest surviving statement is:

> Stored evidence can compose monotonically while finality remains
> context-dependent and stage-specific.

Composition is real, but "finality composes" is too coarse a sentence.
