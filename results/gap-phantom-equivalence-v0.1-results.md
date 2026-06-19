# T58 Gap-Phantom Equivalence Results v0.1

## Command

```bash
python -m pytest tests/test_gap_phantom_equivalence.py -v
python -m models.run_t58
```

## Verification

The focused pytest suite passed:

```text
10 passed
```

The runner wrote:

```text
results/gap-phantom-equivalence-v0.1.json
```

## Result

T58 supports the refined T56 Q1 claim in the bounded T51/T52 witness class:

```text
For each tested well-formed observer view,

  G(U) = A(U) - F(U)

equals the independently reported phantom incomparability witnesses.
```

## Witness Table

| Source | Observer | G(U) | Phantom witnesses | Classification |
| --- | --- | --- | --- | --- |
| T51 | Observer_A | empty | empty | exact_match |
| T51 | Observer_B | (e1_A_locking, e3_composite_locking) | (e1_A_locking, e3_composite_locking) | exact_match |
| T52 | Observer_A | (e1_alpha_locking, e4_delta_locking) | (e1_alpha_locking, e4_delta_locking) | exact_match |
| T52 | Observer_B | (e1_alpha_locking, e3_gamma_locking) | (e1_alpha_locking, e3_gamma_locking) | exact_match |

## Boundary Control

The hostile local-reversal control has:

```text
A(U) = {(a,b)}
F(U) = {(b,a)}
G(U) = {(a,b)}
phantoms = empty
spurious local order = {(b,a)}
```

This is not a phantom incomparability. It is a local/ambient conflict. The
control shows that the gap-phantom equivalence requires a well-formed extension
condition:

```text
F(U) subset A(U)
```

Without that condition, `A(U)-F(U)` can mix missing ambient order with local
conflict.

## Evidence Verdict

Supported inside the tested finite witness class:

- T51 gap sections equal T51 phantom witnesses.
- T52 gap sections equal T52 phantom witnesses.
- The extension condition is necessary for interpreting gap pairs as phantom
  incomparability rather than conflict.

Not promoted:

- No universal theorem for arbitrary observer assignments.
- No resolution of T56 Q2 sheafification.
- No resolution of T56 Q3 nerve cohomology.
- No resolution of T56 Q4 arrow-direction circularity.
