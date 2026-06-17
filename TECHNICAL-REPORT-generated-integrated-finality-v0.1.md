# Generated Integrated Finality Stress Lab

## Abstract

T15 replaces T14's single integrated witness with a deterministic generated
family of finite observer-context systems. The sweep varies record count,
signed weight pattern, inherited expression masking, forged records, and valid
dissent.

The result strengthens T14. The integrated typed pipeline is not merely a
hand-built example: generated cases repeatedly preserve the separation
between coupling, inherited expression, proof validation, finality profile,
and signed readout. The same sweep also identifies minimal breakpoints.

## 1. Motivation

T14 showed that the project remains coherent in one integrated setting if the
stages are kept typed. T15 asks whether that coherence survives a generated
family.

The purpose is not to prove a universal theorem. It is to stop relying on one
elegant witness and let the repo search for both successes and failures.

## 2. Generator

T15 builds finite chain graphs with core record sizes `2..5`. For each size,
it evaluates every non-all-positive signed weight pattern, with inherited
phase masking either off or on. It also varies adversary mode:

```text
none
forged
valid dissent
forged + valid dissent
```

Each case is run through the same typed stages:

```text
record generation
  -> inherited expression
  -> observer coupling
  -> proof validation
  -> finality profile
  -> signed readout
```

The sweep contains `448` cases.

## 3. Results

The generated family reports:

| Metric | Fraction |
| --- | ---: |
| robust success | `0.1161` |
| profile/readout separation | `0.9286` |
| coupling divergence | `1.0000` |
| expression hides stored identity | `0.5000` |
| forged rejection when forged records are present | `1.0000` |
| valid dissent visible when valid dissent is present | `1.0000` |

The most important number is not the robust-success fraction by itself. The
important result is that both sides appear:

- the typed pipeline has repeatable success regions;
- the generator also finds minimal breakpoints.

## 4. Minimal Success

The minimal robust success has:

```text
core size: 2
weights: -1, 1
phase mask: on
forged record: absent
valid dissent: absent
```

The finality profile is:

```text
(2, 2, 1, 2)
```

The signed readout is:

```text
0.0
```

The all-constructive readout is:

```text
4.0
```

So the same finality profile can still support different readouts in the
generated family.

## 5. Minimal Breakpoints

The first breakpoint is raw forgery:

```text
n2-wmm-mask0-f1d0
```

If proof filtering is not required, a forged record is visible.

The second breakpoint is valid dissent:

```text
n2-wmm-mask0-f0d1
```

If a dissenting record satisfies the proof relation, verification does not
remove it. This is correct behavior. Proof validity is not truth.

## 6. Claim Verdict

T15 strengthens:

- [C2](claims/C2-typed-compositional-finality.md): typed separation is needed
  across generated cases, not just one witness.
- [C3](claims/C3-signed-readout-separation.md): profile/readout separation is
  common in the generated family.
- [M1](claims/M1-coupling-profile-reconstruction.md): coupling profile
  divergence is systematic under the generated observer profiles.
- [A1](claims/A1-distributed-systems-finality-analogy.md): proof filtering
  rejects forgery but does not make consensus or validity into truth.

T15 does not strengthen the project into a physical derivation. It still
assigns signed phase weights by hand.

## 7. Next Work

The next decisive step is to make phase-bearing records arise from dynamics:
connect T15 to T9-style local-update systems instead of assigning signed
weights directly.

## 8. Reproduction

```bash
python -m unittest tests.test_t15_generated_integrated_finality -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t15
```

Machine-readable output:

- [results/t15-generated-integrated-finality-v0.1.json](results/t15-generated-integrated-finality-v0.1.json)

Focused result note:

- [results/t15-generated-integrated-finality-v0.1-results.md](results/t15-generated-integrated-finality-v0.1-results.md)
