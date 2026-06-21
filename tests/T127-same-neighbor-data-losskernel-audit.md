# T127: Same-Neighbor-Data LossKernel Audit

## Route

Mathematical machinery / prior-art separation audit.

## Anchors

- `explorations/recurring-structure-map-v0.1.md`
- `open-problems/loss-kernel-formalization.md`
- `claims/TF1-typed-forgetting-attribution.md`
- `tests/T34-po1-chained-projection.md`
- `tests/T37-typed-transport-network.md`
- `tests/T39-csp-satisfiability-reframing.md`
- `tests/T40-holarchy-lab.md`
- `tests/T69-losskernel-failure-type.md`
- `tests/T73-losskernel-composition.md`
- `tests/T99-losskernel-quotient-separation.md`
- `tests/T107-loss-relocation.md`
- `tests/T108-loss-relocation-prior-art.md`
- `papers/typed-loss-kernels-obstruction-attribution-v0.1.md`

## Question

Can LossKernel produce a different admissible-attribution verdict in two finite
cases while every mature neighboring account receives the same data package?

## Result

No strict same-neighbor-data witness survives in the current finite fixture
family.

The executable audit finds:

1. The positive separation attempt is absorbed before LossKernel is needed.
   The partner cases differ in neighbor-visible CSP/lift data, so they do not
   define a same-neighbor-data quotient witness.
2. Different free labels with the same source-derived obligation collapse.
3. Endpoint-difference and path-metadata controls are rejected as invalid
   quotient evidence.
4. A non-empty absorbed-loss case is demoted because uniform source lifts do
   not generate a source-derived witness obligation.
5. Exact same-neighbor aliases force the same derived obligation and the same
   verdict.

## Claim Impact

T127 is a negative result for the current finite family.

- `TF1` remains `open_formal_target`.
- The default rescue path "same-neighbor-data separation should appear if we
  keep searching" is weakened.
- The remaining honest value of LossKernel is narrower: possible canonical
  normal form or integration vocabulary for source-derived witness obligations.
- No prior-art-separated theorem claim is earned.

## Reproduction

```bash
python -m unittest tests.test_same_neighbor_data_losskernel_audit -v
python -m models.run_t127
```
