# T412 Separator Refactorization Gate - Results v0.1

- **Artifact:** `T412-separator-refactorization-gate-v0.1`
- **Spec:** [tests/T412-separator-refactorization-gate.md](../tests/T412-separator-refactorization-gate.md)
- **Model:** [models/separator_refactorization_gate.py](../models/separator_refactorization_gate.py)
- **Test:** [tests/test_separator_refactorization_gate.py](../tests/test_separator_refactorization_gate.py)
- **Numbers:** [T412-separator-refactorization-gate-v0.1.json](T412-separator-refactorization-gate-v0.1.json)
- **Tags:** separator_refactorization_gate, factorization_guardrail_required,
  global_correlation_separator, no_claim_promotion

## Verdict

The T411 fallback separator survives product-structure-preserving relabels,
but not arbitrary entangling refactorization.

In the declared three-qubit parity fixture, all nonempty proper-subset
marginals are identical while the full joint parity readout separates
perfectly. This stays true across all qubit permutations, all local bit flips,
and a product-basis spot check.

The same datum localizes immediately under the entangling refactorization

```text
y0 = x0 xor x1 xor x2
y1 = x1
y2 = x2
```

After that change of factors, the one-qubit marginal on factor `0` separates
the pair with trace distance `1.0`.

## Result

The anti-relabel fallback is real only with an admissibility rule:

```text
admissible refactorizations must preserve the operational tensor product,
coupling graph, or declared access factorization
```

Without that guardrail, the global-correlation separator demotes to a
coordinate-dependent exhibit. This does not promote a claim, resolve the
region-indexed capability discriminator, or revive physical-boundary language.

## Key Values

| Check | Value |
| --- | --- |
| Declared-factorization max proper-subset trace distance | `0.0` |
| Declared-factorization full trace distance | `1.0` |
| Product/permutation/local-flip relabel count | `48` |
| Max proper-subset distance after product relabels | `0.0` |
| Product-basis spot-check max proper-subset distance | `0.0` |
| Entangling refactorized factor-0 trace distance | `1.0` |
| Full trace distance after entangling refactorization | `1.0` |

## Guardrail

T412 answers the persona-pass linchpin test in the conservative direction:

- yes, the separator beats support/light-cone and product-relabel attacks;
- no, it is not factorization-free;
- therefore the next transport/scrambling rung must derive the relevant
  operational factorization from dynamics before relying on the separator.

## Tests

```bash
python -m pytest tests/test_separator_refactorization_gate.py -q
python -m models.separator_refactorization_gate
```

## What This Does Not Earn

No physical-boundary result. No new physics. No claim-ledger update. No
North Star, canon, public-posture, or cross-repo truth change.
