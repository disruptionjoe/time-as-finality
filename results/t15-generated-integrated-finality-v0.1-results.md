# T15 Generated Integrated Finality Stress Results

Result: T15 focused tests pass `5/5`; the current full branch suite passes
`91/91` after T17 was added.

## Sweep

T15 evaluates `448` deterministic generated cases.

Axes:

| Axis | Values |
| --- | --- |
| core size | `2, 3, 4, 5` |
| signed weights | all non-all-positive `+/-1` patterns |
| inherited expression masking | off, on |
| adversary mode | none, forged, valid dissent, both |

## Main Fractions

| Metric | Fraction |
| --- | ---: |
| robust success | `0.1161` |
| profile/readout separation | `0.9286` |
| coupling divergence | `1.0000` |
| expression hides stored identity | `0.5000` |
| forged rejection when forged records are present | `1.0000` |
| valid dissent visible when valid dissent is present | `1.0000` |

## Minimal Witnesses

Minimal robust success:

```text
case: n2-wmp-mask1-f0d0
core size: 2
weights: -1, 1
mask: phase record hidden
profile: (2, 2, 1, 2)
readout: 0.0
all-constructive readout: 4.0
```

Minimal profile/readout separation:

```text
case: n2-wmp-mask0-f0d0
core size: 2
weights: -1, 1
profile: (2, 2, 1, 2)
readout: 0.0
all-constructive readout: 4.0
```

Minimal inherited-expression hiding:

```text
case: n2-wmm-mask1-f0d0
core size: 2
weights: -1, -1
mask: phase record hidden
```

## Minimal Breakpoints

Raw access admits forgery unless proof filtering is required:

```text
case: n2-wmm-mask0-f1d0
```

Proof filtering does not eliminate valid dissent:

```text
case: n2-wmm-mask0-f0d1
```

No generated case in this sweep makes the core observer fail reconstruction.

## Verdict

T15 supports the T14 result as more than a single hand-built example:

- signed readout separation is common in the generated family;
- coupling divergence is systematic under the chosen observer profiles;
- inherited expression masking is distinct from stored identity loss;
- proof filtering rejects forged certificates when verification is required;
- valid dissent remains a valid failure mode.

The remaining limit is important: T15 still assigns phase weights by hand. It
does not derive phase-bearing records from T9-style local dynamics.

## Reproduction

```bash
python -m unittest tests.test_t15_generated_integrated_finality -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t15
```

Machine-readable output:

- [t15-generated-integrated-finality-v0.1.json](t15-generated-integrated-finality-v0.1.json)
