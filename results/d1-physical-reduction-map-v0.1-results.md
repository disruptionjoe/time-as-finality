# D1 Physical Reduction Map Results

Result: T22 focused tests pass `7/7`.

## Reduction Map Verdict

| D1 dimension | Confidence | Current verdict |
| --- | --- | --- |
| accessible support | partially supported | Measurable once an observer access boundary is declared. |
| holder redundancy | partially supported | Strongest current traction; executable comparison supplied by T22. |
| branch support | formal only | Structurally useful, but physical observable status remains open. |
| reversal cost | formal only | Audited but not physically reduced; thermodynamic-work identity is not assumed. |

Confidence summary:

```text
physically supported: 0
partially supported: 2
formal only: 2
failed/rejected: 0
```

## Toy Model

T22 uses a binary pointer state:

```text
P(S0) = 0.5
P(S1) = 0.5
H(S) = 1.0 bit
delta = 0.1
information threshold = 0.9 bits
```

Environment fragments:

| Fragment | Accessible? | Independence class | Branch | I(S;fragment) |
| --- | --- | --- | --- | ---: |
| E1 | yes | left_channel | left | 1.0 |
| E2 | yes | right_channel | right | 1.0 |
| E3 | yes | left_channel | left | 1.0 |
| E4 | no | hidden_channel | hidden | 1.0 |
| N1 | yes | noise_channel | noise | 0.0 |

`E3` is intentionally a correlated duplicate of the left-channel record. It
raises raw accessible environmental redundancy but not the
independence-corrected value used by the D1 holder-redundancy reduction.

## D1 Profile

```text
(accessible support, holder redundancy, branch support, reversal cost)
= (3, 2, 2, 2)
```

## Darwinism-Style Comparison

| Quantity | Value |
| --- | ---: |
| raw accessible R_delta fragments | 3 |
| raw total R_delta fragments | 4 |
| independence-corrected accessible R_delta | 2 |
| D1 holder redundancy | 2 |

Main check:

```text
D1 holder redundancy == independence-corrected accessible R_delta
2 == 2
```

Boundary check:

```text
raw accessible R_delta != D1 holder redundancy
3 != 2
```

This shows why T22 should not identify D1 holder redundancy with raw
environmental copy count unless the fragment partition and independence
criterion are part of the observable contract.

## Guardrail

T22 does not derive D1 from quantum mechanics and does not prove quantum
Darwinism. It supplies one executable observable comparison and records
assumptions for every D1 axis.

## Reproduction

```bash
python -m unittest tests.test_d1_physical_reduction_map -v
python -m models.run_t22
```

Machine-readable output:

- [d1-physical-reduction-map-v0.1.json](d1-physical-reduction-map-v0.1.json)
