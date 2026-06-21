# T155: Weak-Measurement Blackwell Boundary

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)

## Question

Can the Q1C null class be stated more sharply than "zero lift for one chosen
verdict map"? In particular: if the auxiliary channel is screened off by the
full ordinary monitored transcript, does it become decision-theoretically null
across a predeclared finite loss family?

## Motivation

T149 and T150 already make Q1C operational in terms of decision-risk lift and
verdict honesty. But a reviewer can still ask whether those gates are tied too
tightly to one chosen verdict map or one loss function. T155 adds the absorber:
when the full ordinary transcript already screens off the auxiliary meter, the
meter should be redundant across the finite decision family, not just for one
preferred scoring rule.

## Setup

Declare:

```text
H = independently typed hidden axis
R = full ordinary event-level monitored record
A = auxiliary channel
L = predeclared finite loss table
```

Check whether `P(H | R, A) = P(H | R)` in the finite model. If that screening
condition holds, compare Bayes risk for predicting `H` from `R` and from
`(R, A)` across multiple loss tables.

Audit four classes:

1. `garbled_same_instrument_meter`
   The auxiliary channel is only a garbling of the ordinary record.
2. `independent_noise_meter`
   The auxiliary channel is extra noise with no hidden-axis content beyond the
   record.
3. `record_already_sufficient`
   The ordinary record already determines the hidden axis.
4. `extra_environment_candidate`
   The auxiliary channel changes the hidden-axis posterior at fixed record.

## Success Criteria

- All screened-off classes have equal Bayes risk with and without the
  auxiliary channel across the tested loss family.
- The positive control improves at least one loss and is therefore not
  screened off by the ordinary transcript.
- The artifact is framed as an absorber for Q1C, not as a new physics law.

## Failure Criteria

- A screened-off auxiliary channel improves one of the tested decision
  problems.
- The positive control fails to improve any tested loss despite changing the
  hidden-axis posterior.
- The result is overstated as a theorem about all experiments rather than an
  audit boundary under the declared full-transcript reading.

## Claim Impact

Q1C remains dormant.

Add this sharpening:

```text
Once the full ordinary monitored transcript screens off the auxiliary channel,
that auxiliary channel is null across the tested finite decision family, not
just for one chosen verdict map.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_blackwell_boundary -v
python -m models.run_t155
```
