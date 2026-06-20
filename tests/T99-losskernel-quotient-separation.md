# T99: LossKernel Quotient Separation

## Route

Mathematical machinery / adoption elsewhere.

## Question

Does LossKernel still do attribution work after quotienting by same source,
same target, same ordinary composite map, same endpoint behavior, and same
naive lost-label set?

## Motivation

T73 established only a finite powerset-union law:

```text
LossKernel(g o f) = LossKernel(f) union LossKernel(g)
```

That is honest but weak. It may be no more than provenance/effect bookkeeping.
The open TF1 gate asks for a quotient-survival or separation result. T99 tests
the most direct version of that gate.

## Success Criteria

- Construct two finite path cases with the same naive quotient key.
- Give the cases different attribution verdicts only because their typed
  source-witness obligations differ.
- Show that label-only LossKernel collapses the cases.
- Show that the typed witness version separates them.
- Include controls where identical typed witness data collapses and endpoint
  differences are not counted as quotient evidence.

## Failure Criteria

- The cases differ in ordinary composite map, endpoint behavior, or naive
  label set.
- The typed distinction is just a renamed label with no source anchor.
- The result is described as proving LossKernel novelty rather than as a
  conditional salvage path.

## Claim Impact

TF1 remains an `open_formal_target`. T99 weakens the label-only reading of
LossKernel: the T73 union object fails the quotient gate. A stronger
witness-carrying LossKernel remains possible only if source-anchored witness
obligations can be derived canonically from the morphism and finite
source/target structures.

## Reproduction

```bash
python -m unittest tests.test_losskernel_quotient_separation -v
python -m models.run_t99
```
