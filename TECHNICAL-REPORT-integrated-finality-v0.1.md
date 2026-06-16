# Integrated Observer-Context Finality

## Abstract

T14 composes the project's separate laboratories into one bounded experiment.
It combines dynamic records, observer coupling, inherited expression,
coarse-grained proof validation, Snowball-style reconciliation, finality
profiles, and signed readout.

The result is a stress test of coherence. The framework remains usable when
each stage is kept typed. It breaks if proof validity, protocol confidence,
finality profile, and phase-sensitive readout are collapsed into one notion
of "settled truth."

## 1. Motivation

The repo now has several local results:

- T10 separates proof validity, confidence, and truth.
- T11 separates evidence, inherited expression, profile, and decision.
- T12 makes observer coupling explicit.
- T13 separates finality profile from signed readout.

T14 asks whether those distinctions survive in one finite pipeline.

## 2. Pipeline

The implemented pipeline is:

```text
hidden state
  -> record generation
  -> inherited expression
  -> observer coupling
  -> coarse-graining and proof validation
  -> Snowball-style reconciliation
  -> finality profile
  -> signed readout
```

The hidden state is the T10 nine-bit state. Public claims are coarse-grained
through block majorities. Proof certificates expose only bounded public data
and are treated as an ideal relation check, not a cryptographic claim.

## 3. Integrated Witness

The core graph has three verified phase-bearing records:

```text
e1 -> e2 -> e3 -> observe
```

with weights:

```text
1, -1, 1
```

The observer sees finality profile:

```text
(3, 3, 1, 3)
```

and readout:

```text
1.0
```

A constructive variant changes only the middle weight:

```text
1, 1, 1
```

The profile remains `(3, 3, 1, 3)`, but readout becomes `9.0`.

Therefore T13's separation survives the integrated setting.

## 4. Coupling And Inherited Expression

A gravity-only observer sees two records and computes profile `(2, 2, 1, 2)`
with readout `4.0`.

A phase-silenced observer also sees two records and readout `4.0`, but for a
different reason: the stored phase record remains present while inherited
expression makes it invisible.

This is the epigenetic lens in its narrow operational form: expression changes
without deleting stable identity. No biological mechanism, fixed layer count,
or fractal structure is assumed.

## 5. Proofs And Reconciliation

The social channel contains:

- one forged record with an invalid certificate;
- one valid dissent record with a valid certificate for the opposite coarse
  claim.

Proof validation rejects the forged record. It does not reject valid dissent.
The Snowball-style probe keeps the same distinction: proof-carrying
reconciliation reduces forged false finality relative to raw Snowball, but
valid dissent remains a real failure mode.

## 6. Claim Verdict

T14 strengthens the typed-pipeline reading of the project:

> Finality is not one scalar and not one universal algebra. It is an
> observer-indexed stability profile inside a larger typed pipeline.

Supported:

- coupling profile changes accessible records without causal contradiction;
- inherited expression changes visibility without changing stored identity;
- proof validation filters forgery but not valid disagreement;
- protocol confidence is not truth;
- signed readout remains underdetermined by the D1 profile.

Rejected or still unsupported:

- finality determines phase-sensitive readout;
- consensus produces physical truth;
- proof validity establishes truth;
- recursive context implies fractality;
- the model derives quantum mechanics.

## 7. Reproduction

```bash
python -m unittest tests.test_t14_integrated_finality -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t14
```

Machine-readable output:

- [results/t14-integrated-finality-v0.1.json](results/t14-integrated-finality-v0.1.json)

Focused result note:

- [results/t14-integrated-finality-v0.1-results.md](results/t14-integrated-finality-v0.1-results.md)
