# Proof-Carrying Metastable Finality v0.1 Results

Date: 2026-06-11

## Reproduction

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_proof_carrying_finality
```

Machine-readable output is in
[`proof-carrying-metastable-finality-v0.1.json`](proof-carrying-metastable-finality-v0.1.json).

## Coarse-Graining

| Quantity | Result |
| --- | ---: |
| microstate width | 9 bits |
| microstates | 512 |
| microstates per binary claim | 256 |
| claim entropy | 1 bit |
| hidden information after claim disclosure | 8 bits |
| mean one-bit perturbation stability | 0.75 |
| mean minimum reversal radius | 1.339844 bits |
| reversal-radius range | 1 to 4 bits |

The macro claim can remain unchanged while commitments and microscopic records
change. Coarse-grained stability is therefore distinct from microscopic state
persistence.

## Primary Protocol Configuration

```text
population:          21
sample size:          7
quorum:               5
decision threshold:   4 consecutive successful polls
maximum rounds:      80
bit error rate:       0.20
single-report accuracy: 0.665981
trials per primary comparison: 300
```

## Forged Opposition

Adversary fraction: 0.30.

| Method | True consensus | False finality | Consensus rate |
| --- | ---: | ---: | ---: |
| proof-carrying Snowball | 0.8933 | 0.1000 | 0.9933 |
| raw Snowball | 0.2100 | 0.7833 | 0.9933 |
| proofless local majority | 0.1700 | 0.8300 | 1.0000 |
| verified majority / Bayesian MAP | 0.9333 | 0.0667 | 1.0000 |
| static trace persistence | 0.0000 | 0.0000 | 0.0000 |

Proof-carrying Snowball rejected about 496 sampled messages per trial and
finished with mean public evidence support of 9.15 unique sources. It greatly
improved over raw protocol dynamics, but did not outperform one-shot
aggregation of the same verified evidence.

## Valid Dissent

Adversary fraction: 0.30.

| Method | True consensus | False finality | Consensus rate |
| --- | ---: | ---: | ---: |
| proof-carrying Snowball | 0.1933 | 0.8033 | 0.9967 |
| raw Snowball | 0.1933 | 0.8033 | 0.9967 |
| proofless local majority | 0.1400 | 0.8600 | 1.0000 |
| verified majority / Bayesian MAP | 0.4267 | 0.5733 | 1.0000 |
| static trace persistence | 0.0000 | 0.0000 | 0.0000 |

All dissenting certificates were valid for their hidden records. Verification
therefore supplied no advantage. Confidence dynamics amplified the locally
dominant but globally false claim.

## Adversary Sweep

Against forged evidence, proof-carrying Snowball retained true-consensus rates
above 0.88 through a 0.30 adversary fraction. At 0.40 it made no unanimous
decision under the fixed quorum, while verified one-shot aggregation remained
accurate in 0.8933 of trials.

Against valid dissent, proof and raw Snowball were identical at every tested
fraction. Accuracy fell from 0.90 with no dissent to 0 at 0.40 dissent.

## Evidence Verdict

The combination adds operational structure:

- proof validity;
- hidden-state compression;
- independent certified support;
- path-dependent confidence;
- safety-liveness behavior under invalid participation.

It does not add a new truth criterion. Verified majority/Bayesian aggregation
matched or exceeded Snowball truth accuracy in every reported configuration.
