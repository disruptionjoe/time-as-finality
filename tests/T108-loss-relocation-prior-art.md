# T108: Loss Relocation Prior-Art Audit

## Route

Mathematical machinery / adoption elsewhere.

## Question

Does T107 source-fiber loss relocation separate from why-not provenance,
abstract interpretation, lenses, CSP explanation, and effect annotations?

## Motivation

T107 produced a useful finite semantics:

```text
lost structure relocates when target judgments remain source-lift dependent.
```

But that semantics is close to several mature frameworks. T108 asks the
publication-critical question directly before TF1 is upgraded.

## Success Criteria

- Compare T107 against each named neighbor on reconstruction debt, stable
  constraint surfaces, and absorbed freedom.
- Refuse separation if the neighbor can express the same finite behavior once
  it is given the same source fiber and target judgment.
- State the remaining novelty window, if any.
- Preserve the T99 result that label-only loss is too weak.

## Failure Criteria

- Claim separation merely because the vocabulary is different.
- Compare only against weak label-only annotations while ignoring rich effect
  or provenance systems.
- Treat CSP obstruction mechanics as novel.
- Ignore abstract interpretation's concretization-fiber reading.

## Claim Impact

If T108 is negative, TF1 remains open. The surviving delta is not a new
obstruction mechanism. It is at most a typed normal form for source-derived
witness obligations under projection.

## Reproduction

```bash
python -m unittest tests.test_loss_relocation_prior_art -v
python -m models.run_t108
```
