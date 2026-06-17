# Consensus Finality Impossibility

## Abstract

T17 now extracts the consensus-finality crosswalk into an executable bounded
theorem check. In the stated finite asynchronous protocol model, no admissible
configuration simultaneously maximizes all four D1 dimensions and bounded
progress.

This is not an FLP theorem and not a claim that physics literally runs a
distributed protocol. It is a theorem-shaped finite result: the assumptions,
objective functions, exhaustive search space, and counterexample condition are
all explicit and machine-checked.

## Model

A configuration is:

```text
(nodes, quorum, branches, confirmations, timeout)
```

It is admissible when:

```text
nodes + branches + confirmations + timeout <= budget
```

For the v0.1 result:

```text
budget = 10
adversarial delay = 2
checked configurations = 392
```

The D1 profile is:

```text
(accessible support, holder redundancy, branch support, reversal cost)
```

Bounded progress is kept outside D1. It is a separate distributed-systems
condition: quorum must be reachable within the adversarial delay bound.

## Theorem Statement

Within the stated bounded asynchronous protocol model, no admissible
configuration simultaneously maximizes:

- accessible support;
- holder redundancy;
- independent branch support;
- reversal cost;
- bounded progress.

## Exhaustive Verification

The objective maxima are:

```text
accessible support = 4
holder redundancy = 4
branch support = 3
reversal cost = 9
bounded progress = 1
```

No checked configuration reaches all five maxima.

The verifier also returns per-objective tradeoff witnesses:

| Objective maximized | Witness | Gives up |
| --- | --- | --- |
| accessible support | `n4-q4-b1-c1-t4` | branch support, reversal cost, bounded progress |
| holder redundancy | `n4-q4-b1-c1-t4` | branch support, reversal cost, bounded progress |
| branch support | `n3-q3-b3-c1-t3` | support, redundancy, reversal cost, bounded progress |
| reversal cost | `n3-q3-b1-c3-t3` | support, redundancy, branch support, bounded progress |
| bounded progress | `n2-q2-b2-c4-t2` | support, redundancy, branch support, reversal cost |

## Interpretation

The result says that finality has real internal tradeoffs once it is treated
as a profile rather than a scalar. Faster progress, higher accessible quorum,
more independent branch support, and larger reversal cost all compete under a
bounded resource budget.

That makes the distributed-systems analogy useful but not totalizing:

```text
D1 finality profile
  -> safety projection
  -> economic-cost projection
  -> bounded-progress side condition
```

Safety and economic finality are projections. Liveness is not a D1 dimension;
it is a protocol progress condition that can be tested beside D1.

## Claim Impact

The result strengthens [A1](claims/A1-distributed-systems-finality-analogy.md)
because the analogy now has a theorem-shaped core instead of only verbal
similarity.

It also strengthens [D1](claims/D1-physical-finality-definition.md) because
separating D1 dimensions exposes tradeoffs that a single "finality" score
would hide.

## Limits

- The theorem is exhaustive only over the finite model stated here.
- It does not prove a universal impossibility theorem for all protocols.
- It does not use the T16/T13 sheaf-obstruction machinery.
- It does not claim physical systems are engineered consensus systems.

## Reproduction

```bash
python -m unittest tests.test_consensus_finality_crosswalk -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t17
```

Machine-readable output:

- [results/consensus-finality-crosswalk-v0.1.json](results/consensus-finality-crosswalk-v0.1.json)

Human-readable result note:

- [results/consensus-finality-crosswalk-v0.1-results.md](results/consensus-finality-crosswalk-v0.1-results.md)
