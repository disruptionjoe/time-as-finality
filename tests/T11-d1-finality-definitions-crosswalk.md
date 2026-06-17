# T11: D1 as Generalization of Existing Finality Definitions

## Target Claims

- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)

## Origin

Distributed Systems Finality Expert lens, idea sprint 2026-06-16.

## Hypothesis

TaF's D1 componentwise preorder is strictly more expressive than the three standard finality definitions in distributed systems literature — safety finality, liveness finality, and economic finality — and each is a special case of D1 under specific dimension-collapse conditions.

If the mapping holds, D1 is not merely an analogy to distributed systems finality but a formal generalization of it. Results proven in distributed systems about the limits of finality (FLP, CAP, BFT lower bounds) would then be theorems about physical record formation under specific collapse conditions.

## Setup

1. State safety finality, liveness finality, and economic finality precisely as they appear in the consensus literature (Nakamoto, BFT, Avalanche).
2. For each definition, identify which D1 dimensions (accessible support, distinct-holder redundancy, causal branch support, graph reversal count) it depends on, and which it ignores or collapses.
3. Show the collapse map explicitly: "safety finality = D1 restricted to [dimensions X, Y] with [dimensions Z, W] set to trivial."
4. Check whether D1 with those collapses reproduces the original definition exactly, approximately, or not at all.
5. Identify any finality situation captured by D1 that is not captured by any of the three standard definitions — that gap is the theoretical contribution.

## Success Criteria

- All three standard definitions are special cases of D1 under explicitly stated collapse conditions.
- At least one finality situation is constructible in D1 that no standard definition captures.
- The partial order over finality definitions is well-formed (antisymmetric, transitive, non-trivial).

## Failure Criteria

- One of the three standard definitions is not a special case of D1 under any collapse — identify the counterexample and determine whether D1 needs a new dimension or whether the standard definition is richer than D1.
- D1 and the three standard definitions are mutually incommensurable — no clean inclusion or generalization relationship exists.

## Publication Target

PODC, DISC, or a distributed systems theory journal. This test requires no physics machinery and the contribution is formal and self-contained.

## Contribution Needed

Write the formal collapse maps and check each direction of the generalization claim. A crosswalk table is a minimum deliverable; a partial-order theorem over finality definitions is the full result.
