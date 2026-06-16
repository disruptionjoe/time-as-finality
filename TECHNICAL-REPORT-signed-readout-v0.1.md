# Signed Readout Separates Finality From Reconstruction

## Abstract

T13 extends the finite causal record graph with complex readout weights. The
extension is conservative over temporal reconstruction: finality profiles and
reconstructed temporal relations ignore weights. The readout stage does not.

The result is a finite separation. Two states can have identical
observer-indexed finality profiles and different Born-style readouts.
Likewise, a causal chain can have monotonically growing evidence and finality
while readout cancels and returns. Therefore the D1 finality profile does not
determine signed or phase-sensitive readout.

This is not a derivation of quantum mechanics or the Born rule. It is a
structural result: finality, reconstruction, and readout are different typed
stages.

## 1. Motivation

Earlier experiments weakened the idea that finality is one scalar. T9 showed
that several raw dimensions collapse in simple local dynamics. T10 separated
proof validity, protocol confidence, and metastable decision. T11 showed that
evidence can join while finality profiles do not universally compose.

T13 asks a sharper question:

> If records are stable and finality grows monotonically, does that determine
> the value read from those records?

The answer is no for the D1 profile.

## 2. Model

Start with the T1 causal record graph. A record has proposition, value, event,
holder, and erasure-cost proxy. T13 adds one field:

```text
weight(r) in C
```

The finality profile remains:

```text
F = (accessible support, holders, branches, reversal cost)
```

The profile is weight-blind by construction.

The readout used in the nontrivial phase is:

```text
R(S) = |sum_{r in S} weight(r)|^2
```

where `S` is the accessible supporting record set.

## 3. Trivial Signed Readout

Linear signed readout is:

```text
R1(S) = sum_{r in S} weight(r)
```

for weights `+1` and `-1`. This factors as:

```text
R1 = P - N
```

where `P` and `N` are monotone counters. T13 includes this as a passing test
so the result cannot rest on a trivial Jordan-decomposition case.

## 4. W1: No Function From Profile To Readout

Construct two graphs with the same causal shape and same two records.

Constructive weights:

```text
(1, 1)
```

Destructive weights:

```text
(1, -1)
```

Both states have the same finality profile:

```text
(2, 2, 2, 2)
```

Their readouts differ:

```text
|1 + 1|^2 = 4
|1 - 1|^2 = 0
```

Therefore no function from the D1 finality profile to readout exists. The same
input profile maps to two outputs.

## 5. W2: No Monotone Profile-To-Readout Relation

Construct a causal chain with three records:

```text
e1 -> e2 -> e3
```

Weights:

```text
1, -1, 1
```

Evidence count grows:

```text
1, 2, 3
```

Profiles grow componentwise:

```text
(1,1,1,1)
(2,2,1,2)
(3,3,1,3)
```

Readout cancels and returns:

```text
1, 0, 1
```

Therefore even along one trajectory with monotone finality, the readout is not
monotone in the profile.

## 6. Sorkin-Level Positioning

For disjoint record sets, define:

```text
mu(S) = |sum_{r in S} weight(r)|^2
```

The second-order interference term is:

```text
I2(A,B) = mu(A union B) - mu(A) - mu(B)
```

T13 gives:

```text
I2((1), (1)) = 2
I2((1), (-1)) = -2
```

The third-order term is:

```text
I3(A,B,C) =
  mu(A union B union C)
  - mu(A union B)
  - mu(A union C)
  - mu(B union C)
  + mu(A)
  + mu(B)
  + mu(C)
```

For `mu(S) = |sum S|^2`, expand into ordered pair terms
`w_i * conjugate(w_j)`. Every contribution has coefficient zero in `I3`:

```text
within A: 1 - 1 - 1 + 1 = 0
within B: 1 - 1 - 1 + 1 = 0
within C: 1 - 1 - 1 + 1 = 0
cross AB: 1 - 1 = 0
cross AC: 1 - 1 = 0
cross BC: 1 - 1 = 0
```

The implementation checks this symbolically and also verifies random complex
configurations numerically.

## 7. Observer Consistency

Two observers can have different access to the same graph. If one observer
cannot access the `-1` record, it computes a different readout. This is not a
contradiction: the access boundary differs.

When access agrees, readout agrees. Each observer still sees monotone
profiles along the chain.

## 8. Claim Verdict

T13 supports [C3](claims/C3-signed-readout-separation.md):

> Record evidence, finality profile, temporal reconstruction, and signed
> readout are distinct typed stages.

The result also sharpens D1. A finality profile is a useful observer-indexed
stability summary, but it is not a complete readout state.

## 9. Limits

- The witnesses are finite and minimal.
- The readout is fixed to `|sum w|^2`.
- Phase-class counters recover the readout.
- Larger graphs, mixed T12 channels, and T9-style dynamical record generation
  are untested.
- No physical quantum experiment is derived.

## 10. Reproduction

```bash
python -m unittest tests.test_t13_signed_readout tests.test_t13_characterization -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t13
```

Machine-readable output:

- [results/t13-signed-readout-v0.1.json](results/t13-signed-readout-v0.1.json)

Known-neighbor positioning:

- [literature/N7-signed-readout-known-neighbors.md](literature/N7-signed-readout-known-neighbors.md)
