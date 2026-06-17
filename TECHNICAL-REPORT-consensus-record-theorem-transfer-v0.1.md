# Consensus-Record Theorem Transfer

## Abstract

T20 tests the repo's strongest convergence claim: distributed computing and
physical record formation may be solving the same mathematical problem in
different notation.

The result is positive but narrow. A quorum-intersection safety theorem
transfers from distributed consensus into D1-style physical record finality
without changing its proof structure. The transfer works only when the
assumptions are preserved: finite holder set, certificate threshold,
intersection condition, local consistency, and typed incompatibility.

The same lab also finds two boundaries. Weak quorum fails because certificate
sets can be disjoint. A contextual record case fails globally even though
local quorum certificates exist, showing that quorum safety does not prove
T13-style global-section existence.

## 1. Typed Dictionary

| Distributed computing | Physical record formation | Preserved structure | Caveat |
| --- | --- | --- | --- |
| process local state | observer-local finality domain | bounded local view | physical observers are not engineered processes |
| message or commit certificate | record fragment or environmental witness | portable evidence | physical records need not be symbolic messages |
| quorum intersection | redundant-holder overlap | shared support blocks contradiction | holder independence must be justified physically |
| fork or conflicting commit | incompatible finality sections | local commitments may fail to globalize | fork safety is weaker than global-section existence |
| safety | no contradictory stabilized records | incompatible final facts are excluded | does not imply liveness or objectivity |
| liveness | record-amplification progress | eventual availability under bounded conditions | progress is not a D1 dimension |
| Byzantine fault or adversarial delay | bounded causal access or decoherence lag | reconciliation limits | physical noise is not adversarial intent |

This dictionary is intentionally typed. The claim is not that the words are
similar. The claim is that the same proof can be run after translating the
objects.

## 2. Transferred Theorem

Source theorem:

```text
In a quorum system with 2q > n and locally consistent processes,
two conflicting commit certificates cannot both be valid.
```

Target theorem:

```text
In a physical record system with redundant-holder threshold 2q > n
and locally consistent record fragments, two incompatible classical
records cannot both be finalized.
```

Proof structure:

1. Every final certificate contains at least `q` holders.
2. If `2q > n`, any two final certificates intersect.
3. A shared locally consistent holder cannot certify incompatible values.
4. Therefore incompatible certificates cannot both be final.

T20 checks that the same four proof steps apply on the consensus side and the
physical-record side.

## 3. Positive Transfer

Consensus case:

```text
n = 5
q = 3
commit_A = {n1, n2, n3}
commit_B = {n3, n4, n5}
intersection = {n3}
```

Physical-record case:

```text
n = 5
q = 3
spin_up_record = {e1, e2, e3}
spin_down_record = {e3, e4, e5}
intersection = {e3}
```

The D1 profile of each physical-record certificate is:

```text
(accessible support = 3,
 holder redundancy = 3,
 branch support = 1,
 reversal cost = 3)
```

The theorem transfers because the preserved assumptions are exactly the
assumptions used in the proof.

## 4. Boundary: Weak Quorum

If `2q > n` fails, the theorem does not transfer.

```text
n = 4
q = 2
spin_up_record = {e1, e2}
spin_down_record = {e3, e4}
intersection = {}
```

Both certificates meet threshold, but they do not intersect. The model
therefore detects an unsafe conflict.

## 5. Boundary: Global Section

T20 also tests a contextual record case:

```text
A = B
B = C
A != C
```

Each relation has a quorum certificate. Each local relation is satisfiable.
But no global assignment exists.

This is the important T13 boundary: quorum safety can block contradictory
certificates, but it does not prove that all locally certified records glue
into a global finality section. H1/sheaf structure is not optional if the
claim concerns global objectivity rather than pairwise safety.

## 6. Claim Impact

T20 strengthens [A1](claims/A1-distributed-systems-finality-analogy.md). The
distributed-systems analogy is now a theorem-transfer claim for at least one
proof pattern, not only a metaphor or crosswalk.

T20 strengthens [D1](claims/D1-physical-finality-definition.md) by connecting
holder redundancy to a theorem-bearing role: redundant-holder overlap is the
physical-record analogue of quorum intersection.

T20 also clarifies [T13](tests/T13-finality-sheaf-cohomology.md). Quorum
safety is not enough for global objectivity. Global-section questions require
the sheaf layer.

## 7. Limits

- Only one theorem pattern is transferred in v0.1.
- The target theorem is conditional on local consistency and independent
  holders.
- The lab does not model quantum amplitudes or decoherence dynamics.
- The contextual boundary is finite and logical, not a Bell-test simulation.
- The result does not claim physics literally runs a distributed protocol.

## 8. Reproduction

```bash
python -m unittest tests.test_consensus_record_theorem_transfer -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t20
```

Machine-readable output:

- [results/consensus-record-theorem-transfer-v0.1.json](results/consensus-record-theorem-transfer-v0.1.json)

Human-readable result note:

- [results/consensus-record-theorem-transfer-v0.1-results.md](results/consensus-record-theorem-transfer-v0.1-results.md)
