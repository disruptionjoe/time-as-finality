# T10: Proof-Carrying Metastable Finality

## Target Claims

- [A1: Distributed-Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D2: Observer As Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)

## Setup

Generate noisy hidden records of a common nine-bit microstate. Coarse-grain
each record to a binary proposition, certify the relation through an ideal
proof functionality, and let bounded agents repeatedly subsample one another
with Snowball-style confidence updates.

Compare forged false records with valid conflicting records.

## Success Criteria

- Proof verification rejects forged claims without revealing hidden records.
- Recursive evidence aggregation counts unique sources.
- Repeated sampling creates measurable convergence and confidence structure.
- The model separates proof validity, truth, redundancy, confidence, and
  coarse-grained reversal distance.
- Matched baselines identify which benefits come from verification, ordinary
  aggregation, or metastability.

## Failure Criteria

- Valid proof is treated as proof that the global proposition is true.
- Snowball finality is treated as absolute or physically universal.
- Confidence accumulation adds no operational behavior beyond one-shot
  aggregation.
- Invalid responses can indefinitely preserve both safety and liveness under
  the fixed quorum.
- The ideal proof functionality is misrepresented as a cryptographic scheme.

## Result

Status: **implemented; comparative success with a strong epistemic limit**.

At 30% forged opposition, proof-carrying Snowball reached the true unanimous
decision in `89.33%` of 300 trials, compared with `21.00%` for raw Snowball.
The verified majority/Bayesian baseline reached `93.33%`.

At 30% valid dissent, proof and raw Snowball were identical. They reached the
true decision in only `19.33%` of trials and falsely finalized in `80.33%`.
The one-shot Bayesian/majority baseline reached `42.67%`.

At 40% forged opposition, proof verification preserved safety by rejecting
invalid responses but produced no unanimous decisions under the fixed
seven-sample, five-vote quorum. This is a safety-liveness tradeoff.

The complete result is in
[the T10 technical report](../TECHNICAL-REPORT-proof-carrying-metastable-finality-v0.1.md).
