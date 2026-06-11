# Proof-Carrying Metastable Finality Under Coarse-Grained Access

## Abstract

T9 studied persistent counterfactual traces in local dynamics. It did not
model collective confidence formation, proof verification, or explicit
coarse-graining. T10 adds those mechanisms.

A hidden nine-bit record is mapped to a binary macro claim through two-level
majority coarse-graining. An ideal proof functionality certifies that the
claim follows from a hidden record, recursively combines independent support,
and exposes no microstate. Twenty-one bounded agents then apply a binary
Snowball-style process based on repeated seven-peer samples, a five-response
quorum, and a four-success decision threshold.

The combination is operationally meaningful but epistemically limited.
Verification sharply improves resistance to forged evidence. It cannot reject
valid conflicting records, and metastable confidence can amplify a false
majority. A verified one-shot majority, equivalent here to a Bayesian MAP
decision under equal report reliability, matches or exceeds Snowball truth
accuracy. T10 therefore supports proof-carrying metastability as a model of
bounded integrity and convergence, not as a mechanism that turns consensus
into truth.

## 1. What T9 Missed

T9's observer was a passive terminal window. Its record was a changed bit. It
contained no:

- population of reconcilers;
- competing candidate histories;
- repeated local sampling;
- accumulated confidence;
- proof relation;
- recursive evidence;
- explicit map from hidden microstates to public macrostates.

T10 is a separate laboratory because those additions change the research
object from trace persistence to collective record processing.

## 2. Coarse-Grained Claim

For nine-bit microstate `x`, divide the bits into three blocks. Let `b_i` be
the majority bit of block `i`. The public claim is:

```text
C(x) = majority(b_1, b_2, b_3)
```

The map partitions the 512 microstates evenly. Revealing `C(x)` under a
uniform prior leaves eight bits hidden.

Across the complete state space, 75% of single-bit interventions preserve the
claim. The minimum number of bit flips needed to change the claim ranges from
one to four, with mean 1.339844. This produces a coarse-grained reversal
quantity that is not raw record count or protocol confidence.

## 3. Ideal Proof-Carrying Records

The modeled relation is:

```text
R(public claim, hidden record) = 1 iff C(hidden record) = public claim
```

Leaf certificates attest to one hidden record. Recursive certificates attest
to the union of unique source records supporting the same claim. Duplicate
certificates cannot increase support.

The functionality is deliberately idealized. It captures the information
contract required from a zero-knowledge or proof-carrying-data construction:

- valid witnesses are accepted;
- forged claims are rejected;
- hidden records are not public;
- recursively accumulated evidence remains verifiable.

It does not instantiate a zero-knowledge protocol, establish computational
security, or estimate proof size and verification cost.

## 4. Proof Is Not Truth

Each honest agent observes a noisy local copy of one global microstate. Its
certificate proves only that its claim matches its own record.

This permits two different false-message classes:

1. a forged claim with no satisfying hidden record;
2. a valid claim derived from a genuinely conflicting local record.

The proof system rejects the first and must accept the second. Any model that
rejects both has silently defined its proof oracle as an oracle for global
truth.

## 5. Consensus And Baselines

Agents repeatedly sample seven peers. Five matching accepted responses make a
poll successful. Snowball confidence is accumulated per candidate, and four
consecutive successes produce a decision.

The matched baselines are:

- static persistence of the original records;
- one-shot majority of valid records;
- Bayesian MAP under equal independent report reliability;
- local-majority dynamics without proof or confidence memory;
- Snowball without proof verification.

Because report reliability is equal, majority and Bayesian MAP make the same
decision. This makes the epistemic comparison exact rather than rhetorical.

## 6. Forged-Evidence Result

With 30% forged opposition:

- proof-carrying Snowball true consensus: `0.8933`;
- raw Snowball true consensus: `0.2100`;
- proofless local-majority true consensus: `0.1700`;
- verified majority/Bayesian accuracy: `0.9333`.

Verification therefore performs real work. It stops invalid claims from
entering confidence updates. Recursive proof support also grows from one
source per leaf to a mean of 9.15 independently counted sources.

But proof-carrying Snowball remains less accurate than direct aggregation of
the same valid evidence. Its benefit is decentralized convergence under
bounded samples, not superior inference.

At 40% forged opposition, the fixed quorum cannot gather enough accepted
responses reliably. The proof-carrying process produces no unanimous
decisions. Rejecting invalid evidence preserves safety while sacrificing
liveness.

## 7. Valid-Dissent Result

With 30% valid dissent:

- proof and raw Snowball true consensus: `0.1933`;
- proof and raw Snowball false finality: `0.8033`;
- verified majority/Bayesian accuracy: `0.4267`.

Proof verification has no effect because the conflicting records satisfy the
stated relation. Snowball makes the network agree more readily than it makes
the network correct.

This is the decisive negative result:

> Proof validity plus metastable consensus can transform bounded evidence into
> stable agreement, but cannot transform a bad evidence distribution into
> truth.

## 8. Comparison With T9 And D1

T9 found that support, spatial redundancy, and terminal intervention cost
collapse to one Hamming count in a raw trace.

T10 separates several quantities:

| Quantity | Source |
| --- | --- |
| coarse reversal radius | micro-to-macro map |
| certificate validity | proof relation |
| independent support count | recursive evidence |
| protocol confidence | sampling history |
| consensus decision | threshold rule |
| truth accuracy | relation to global hidden state |
| liveness | probability of gathering a quorum |

These dimensions do not collapse. However, most arise from an engineered
observer protocol. T10 therefore rehabilitates D1 as a useful typed comparison
schema while leaving its universal-physics interpretation rejected.

## 9. Metastability Versus Bayesian Inference

The Snowball process adds path dependence, distributed convergence, and a
safety-liveness tradeoff. It does not add evidence. In every reported
configuration, the verified Bayesian/majority baseline matches or exceeds its
truth accuracy.

This prevents a category error:

```text
confidence accumulation != evidence creation
proof validity != global truth
consensus finality != physical irreversibility
coarse stability != microscopic persistence
```

## 10. Verdict

The user's proposed combination was genuinely missing from T9 and is
interesting. Its strongest defensible contribution is not a universal
finality mechanism. It is a decomposition:

> Coarse-graining defines which hidden distinctions are ignored; proofs
> constrain which claims are admissible under bounded disclosure; repeated
> sampling creates metastable agreement over those admissible claims.

The three layers solve different problems. Their composition creates richer
observer-relative finality profiles, but truth remains dependent on the
quality and relevance of the underlying records.

## 11. Next Decisive Experiment

Replace the ideal proof functionality with one concrete proof relation and
explicit verification costs. Then introduce changing hidden states and stale
but valid certificates. The decisive question is whether epoching,
revocation, and proof aggregation can preserve both bounded disclosure and
timely correction without turning finality into permanent lock-in.
