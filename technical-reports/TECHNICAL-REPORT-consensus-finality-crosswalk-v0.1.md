# Consensus Finality Crosswalk

## Abstract

T17 formalizes the repo's most publishable cross-persona signal: distributed
consensus and physical record formation share a structural problem. Bounded
systems must turn partial, local, fallible records into stable commitments
without assuming a global God's-eye state.

The lab does not claim physics literally runs a consensus protocol. It gives
a precise crosswalk: safety finality, liveness finality, and economic finality
are collapses or projections of D1-style record finality under stated
conditions.

The result is positive in a bounded finite search. Standard distributed
summaries collapse distinctions that D1 retains, and no admissible protocol
configuration under the chosen budget maximizes all four D1 dimensions at
once. A follow-on theorem report extracts this witness into an executable
bounded theorem check that also includes bounded progress as a separate
distributed-systems objective.

## 1. Motivation

The 42-persona sprint found the strongest convergence around one idea:

> distributed consensus and physical record formation are the same formal
> problem in different language.

The safe version is narrower:

> distributed finality definitions are useful collapses of a more general
> observer-indexed record-finality profile.

T17 tests that version.

## 2. Model

A protocol configuration is:

```text
(nodes, quorum, branches, confirmations, timeout)
```

The D1 vector is:

```text
(accessible support, holder redundancy, branch support, reversal cost)
```

The distributed summaries are:

- **safety finality:** quorum is majority-safe and accessible by timeout;
- **liveness:** quorum is accessible within bounded adversarial delay;
- **economic finality:** reversal cost only.

## 3. Collapse Maps

Safety finality uses support, holder redundancy, and reversal cost, but it
collapses branch support.

Liveness is not a D1 dimension. It is a protocol progress condition: whether
the system can reach a decision by a deadline under a delay assumption.

Economic finality is a strict one-dimensional collapse onto reversal cost.

This gives the crosswalk:

```text
D1 profile
  -> safety projection
  -> liveness condition
  -> economic-cost projection
```

## 4. Divergence Witnesses

The bounded search evaluates `392` configurations.

It finds:

- same safety finality with different branch support;
- same economic finality with different D1 profiles;
- same distributed signature with different D1 profiles.

Therefore D1 is not merely distributed finality renamed. It is a richer
record-finality profile that distributed definitions can collapse into.

## 5. Bounded Impossibility Witness And Theorem Check

Under budget `10`, the component maxima are:

```text
(4, 4, 3, 9)
```

No admissible configuration reaches all four values at once. The Pareto
frontier has five representative strategies:

```text
(2, 2, 2, 8)
(3, 3, 1, 9)
(3, 3, 2, 6)
(3, 3, 3, 3)
(4, 4, 1, 4)
```

This is not an FLP theorem. It is a finite witness that the D1 dimensions are
not all simultaneously maximized under bounded resources and delay.

The follow-on theorem check adds bounded progress as a fifth objective:

```text
(support, redundancy, branch support, reversal cost, bounded progress)
```

It verifies that no admissible configuration reaches:

```text
(4, 4, 3, 9, 1)
```

See
[TECHNICAL-REPORT-consensus-finality-impossibility-v0.1.md](TECHNICAL-REPORT-consensus-finality-impossibility-v0.1.md).

## 6. Claim Verdict

T17 strengthens [A1](claims/A1-distributed-systems-finality-analogy.md). The
distributed-systems analogy is no longer only rhetorical; it has explicit
collapse maps and divergence witnesses.

T17 also strengthens [D1](claims/D1-physical-finality-definition.md). Keeping
support, redundancy, branch support, and reversal cost separate exposes
distinctions that safety, liveness, and economic finality do not retain.

Limits:

- The search space is finite and stylized.
- The impossibility result is bounded, not universal.
- No claim is made that physical record formation is literally BFT, Snowball,
  or blockchain consensus.

## 7. Next Work

The next step is to generalize the bounded theorem check beyond budget `10`.
State parameterized resource bounds and prove which subsets of D1 dimensions
can or cannot be jointly maximized under adversarial delay.

That would make T17 publishable as a self-contained distributed-systems note.

## 8. Reproduction

```bash
python -m unittest tests.test_consensus_finality_crosswalk -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t17
```

Machine-readable output:

- [results/consensus-finality-crosswalk-v0.1.json](results/consensus-finality-crosswalk-v0.1.json)

Focused result note:

- [results/consensus-finality-crosswalk-v0.1-results.md](results/consensus-finality-crosswalk-v0.1-results.md)

Theorem report:

- [TECHNICAL-REPORT-consensus-finality-impossibility-v0.1.md](TECHNICAL-REPORT-consensus-finality-impossibility-v0.1.md)
