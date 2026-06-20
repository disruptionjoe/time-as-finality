# T106: Bounded-Sink Reversible Compression

## Route

Thermodynamic arrow of time.

## Question

Can the T84 cyclic-reconciler obstruction be avoided by using logically
reversible compression plus a bounded entropy sink, so that H7 retains a
nontrivial finality monotone after the sink is included in the state space?

## Motivation

T84 showed that fixed cyclic memory becomes monotone only by exporting old
records or by erasing them. Its next recommended test was a reversible
compression/export model with a bounded sink. This is the highest-value H7
loophole because it asks whether finality direction survives as more than
ordinary resource accounting.

## Success Criteria

- Use the same T80/T84 observation and overwritten-slot sequence.
- Separate orderless compression from ordered lossless export.
- Check injectivity and logical information loss for the relevant finite maps.
- Include a bounded sink capacity audit.
- Close the reversible cycle and test whether the forward-only monotone
  remains monotone after the sink is included.

## Failure Criteria

- Treat an orderless compressed count as reversible when it merges distinct
  histories.
- Count monotonicity only on the forward branch while excluding the sink's
  reversible return path.
- Hide overwritten records in an unaccounted environment or side channel.
- Present finite sink capacity as an autonomous arrow rather than a resource.

## Claim Impact

If T106 is negative, H7 is weakened again as a physical-arrow claim. The
surviving result is only the T18 conditional constructor theorem plus an
open-system/resource-accounting reading.

## Reproduction

```bash
python -m unittest tests.test_bounded_sink_reversible_compression -v
python -m models.run_t106
```
