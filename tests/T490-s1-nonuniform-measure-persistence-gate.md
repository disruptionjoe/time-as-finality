# T490: S1 Nonuniform Measure Persistence Gate

## Route

Spacetime reconstruction / S1 finite-colimit route.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T223: T54 Ordinal Scaling Decisive Verdict](T223-t54-ordinal-scaling-decisive-verdict.md)
- [T464: S1 Added-Assumption Admission Gate](T464-s1-added-assumption-admission-gate.md)
- [Spacetime as Finality Colimit](../open-problems/spacetime-as-finality-colimit.md)

## Question

After T464 admits only future post-T223 added-assumption packets, what does the
nonuniform-measure branch need before it can be reviewed without becoming a
tail-tuned restart of the finite S1 no-go?

## Motivation

T223 showed that the uniform finite ordinal ensemble does not concentrate on
the T54/T126/T156/T159 stable survivor tail through `n=8`. T464 blocked selected
survivors, post-hoc assumptions, missing finite audits, and promotion shortcuts.

T490 makes one specific follow-up executable: a nonuniform measure or selection
packet must not merely reweight the T223 result by conditioning on the known
survivor tail or on the existing guardrail screens.

## Setup

The model consumes the exact T223 census for `n=6,7,8`:

```text
n=6: 26/720 stable survivors, 26/156 parent-interval-conditioned survivors
n=7: 174/5040 stable survivors, 174/561 parent-interval-conditioned survivors
n=8: 361/40320 stable survivors, 361/2057 parent-interval-conditioned survivors
```

It then classifies packet shapes:

- uniform ordinal baseline;
- known-survivor tail indicator;
- parent-interval screen conditioning;
- full screen-stack conditioning;
- screen drift after T223;
- single-size positive;
- unjustified nonuniform weights;
- nonvanishing finite weights without later Lorentzian constraints;
- claim-promotion or external-action shortcuts;
- synthetic future review targets with independent generating laws and fixed
  screens.

## Success Criteria

T490 succeeds if it:

- preserves T223 as the uniform finite no-go baseline;
- rejects survivor-tail indicators as circular;
- rejects parent-interval or screen-stack conditioning as guardrail
  normalization, not an independent natural measure;
- rejects screen drift after T223;
- rejects single-size positives;
- rejects nonuniform weights with no independent finality-native or
  neighbor-theory law;
- rejects packets with no later causal, metric, covariance, locality,
  embedding, or Lorentzian constraints;
- blocks S1 promotion, public posture, and non-GitHub external action;
- admits only synthetic future measure/continuum packets for review;
- records that admitted packets count as no S1 evidence.

## Failure Criteria

T490 fails if it:

- reverses T223;
- promotes S1;
- treats screen conditioning as a natural measure;
- treats a selected tail as non-circular;
- admits a single-size positive as measure persistence;
- permits screen drift after T223;
- permits public posture, claim promotion, or non-GitHub external action;
- claims spacetime derivation, manifoldlikeness, dimension, sprinkling,
  Lorentzian metric, locality, covariance, embedding, GR/QFT, or a continuum
  theorem.

## Result

Status: implemented.

Expected verdict:

```text
S1_NONUNIFORM_MEASURE_PERSISTENCE_GATE_BUILT_SCREEN_CONDITIONING_NOT_ENOUGH
```

## Known Physics Constraints

T490 is not a physics result. It does not derive spacetime, manifoldlikeness,
dimension, Lorentzian metric, GR, QFT, random sprinkling, locality, covariance,
embedding, or a continuum limit. It only defines the next review gate for a
future post-T223 nonuniform-measure packet.

## Claim Impact

No claim-ledger movement. S1 remains `requires_added_assumption` for the finite
finality-colimit route.

## Reproduction

```bash
python -m pytest tests/test_s1_nonuniform_measure_persistence_gate.py -q
python -m models.s1_nonuniform_measure_persistence_gate --write-results
```

Artifacts:

- `models/s1_nonuniform_measure_persistence_gate.py`
- `tests/test_s1_nonuniform_measure_persistence_gate.py`
- `results/T490-s1-nonuniform-measure-persistence-gate-v0.1.json`
- `results/T490-s1-nonuniform-measure-persistence-gate-v0.1-results.md`
