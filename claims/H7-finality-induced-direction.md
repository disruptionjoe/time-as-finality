# H7: Finality-Induced Direction

## Claim

Finality structure can induce an observer-relative temporal direction when
admissible transformations are monotone in D1 finality.

## Class

Conjecture.

## Status

Partially supported only as a conditional constructor-style theorem or
open-system/resource-accounting claim; weakened against direct physical reading
by T80, T82, T84, T106, T110, T116, and T122.
T128 identifies the smallest finite survivors and keeps the status narrowed.
T124 adds the reverse-edge grounding gate and blocks unqualified physical-arrow
readings for the current witness stack. T142 calibrates the T1/T141 survivor
against reversible uncopy and ordinary erasure/free-energy accounting.

## What This Does Not Claim

- This does not derive the thermodynamic arrow.
- This does not replace coordinate time, proper time, relativity, or entropy.
- This does not prove that every physical system instantiates the constructor
  rule used in T18.
- This does not turn the finality partial order into a universal total order.

## Why It Might Be Useful

If finalized records are defined by transformations that cannot be undone
without decreasing D1 structure, then strict finalization has an intrinsic
direction. The direction comes from the asymmetry of admissible transformations:

```text
less finalized record -> more finalized record
```

is possible, while the reverse is not admissible under the same rule.

## How It Could Fail

- A physically grounded model may allow D1-decreasing transformations.
- The constructor rule may merely repackage thermodynamic irreversibility.
- The D1 dimensions may collapse in the relevant substrate.
- The induced direction may be too weak to explain any experienced or
  physical arrow.

## Tests

- [T18: Finality Direction Theorem](../tests/T18-finality-direction-theorem.md)
- [T80: Reversible Finality Nonmonotonicity](../tests/T80-reversible-finality-nonmonotonicity.md)
- [T82: Persistent Reconciler Cost Boundary](../tests/T82-persistent-reconciler-cost-boundary.md)
- [T84: Cyclic Reconciler Entropy Export](../tests/T84-cyclic-reconciler-entropy-export.md)
- [T106: Bounded-Sink Reversible Compression](../tests/T106-bounded-sink-reversible-compression.md)
- [T110: Finite-Permutation Monotone Obstruction](../tests/T110-finite-permutation-monotone-obstruction.md)
- [T116: Open Markov Record-Entropy Comparison](../tests/T116-open-markov-record-entropy.md)
- [T122: Stationary Markov Monotone Obstruction](../tests/T122-stationary-markov-monotone-obstruction.md)
- [T124: Constructor-Admissibility Grounding Audit](../tests/T124-constructor-admissibility-grounding-audit.md)
- [T128: Minimal Living Arrow](../tests/T128-minimal-living-arrow.md)
- [T141: T1 Record-Graph Admissibility Ledger](../tests/T141-t1-record-graph-admissibility-ledger.md)
- [T142: Thermodynamic Erasure Calibration](../tests/T142-thermodynamic-erasure-calibration.md)
- [T5: Thermodynamic Record Support](../tests/T5-thermodynamic-record-support.md)
- [T9: Emergence Laboratory](../tests/T9-emergence-laboratory.md)

## T18 Result

[T18](../tests/T18-finality-direction-theorem.md) verifies a finite theorem:
in a constructor-style model where admissible transformations are D1-monotone,
strict finalization induces an acyclic partial order and every strict
finalization has an impossible reverse.

The result also finds a thermodynamic-divergence witness: a strict finality
increase where the thermodynamic-cost proxy does not increase. That supports
the narrow claim that finality direction is not defined by the thermodynamic
proxy in this toy model.

## T80 Result

[T80](../tests/T80-reversible-finality-nonmonotonicity.md) tests whether T18's
D1-monotone admissibility rule is automatically grounded by reversible local
dynamics. It is not. A width-3 second-order reversible lift of elementary Rule
30 has an injective transition map, zero logical information-loss bound, and a
checked direct inverse, but a fixed observer window sees the raw D1 trace
profile decrease:

```text
(2, 2, 1, 2) -> (1, 1, 1, 1)
```

T18 classifies that physical step as `strict_definalization` and therefore
impossible under the constructor rule. H7 therefore needs an added persistence,
coarse-graining, or constructor-impossibility condition before it can be read
as a physical arrow rather than a conditional ordering theorem.

## T82/T84 Result

[T82](../tests/T82-persistent-reconciler-cost-boundary.md) and
[T84](../tests/T84-cyclic-reconciler-entropy-export.md) tested whether adding
observer memory rescues the physical reading. The finite answer is negative.
Persistent memory restores monotone retained support only by using an
irreversible OR-style update or by consuming append-only blank ledger capacity.
Recycling the ledger cyclically restores monotone accounting only if
overwritten slots are exported as history or erased through a heat-bath
channel. Fixed local cyclic memory itself remains nonmonotone.

## T106 Result

[T106](../tests/T106-bounded-sink-reversible-compression.md) closes the
bounded-sink compression loophole in the same witness family. Orderless
compression of overwritten slots is non-injective. Ordered lossless export is
reversible only while consuming sink capacity. When the bounded sink is
included and the reversible cycle is closed, the forward monotone decreases on
the return path:

```text
0, 1, 3, 4, 4, 5, 7, 5, 4, 4, 3, 1, 0
```

H7 therefore remains a conditional constructor theorem, not a derived physical
arrow from bounded reversible observer memory.

## T110 Result

[T110](../tests/T110-finite-permutation-monotone-obstruction.md)
generalizes the T106 return-path obstruction. In any finite closed reversible
system represented by a permutation, every orbit is a cycle. If a scalar
finality score is nondecreasing on every transition edge around that cycle, it
must be constant on the whole orbit. A strict finality monotone therefore
cannot live inside the closed bounded reversible state space.

The surviving H7 content is conditional: either a constructor-style
admissibility relation, or an explicitly open-system/coarse-grained
resource-accounting model that names its sink, erasure, fresh capacity, or
excluded environment. H7 should not be presented as a new derivation of the
thermodynamic arrow from closed finite reversible dynamics.

## T116 Result

[T116](../tests/T116-open-markov-record-entropy.md) tests the open-system
loophole directly with finite Markov record fixtures. The detailed-balance
record-shuffle control has zero path irreversibility and no strict finality
arrow. A biased local cycle has positive path irreversibility but is not a
scalar finality monotone. The open export recorder gets nondecreasing
accounted records only by naming exported history and positive path log-ratio.
The zero-log-ratio append-only control is monotone only while consuming fresh
blank capacity.

So the current open-system H7 route is still absorbed by standard stochastic
thermodynamics, history export, or capacity accounting. H7 should be demoted in
paper-facing prose to a constructor/resource-accounting lemma unless a future
model clears the T116 zero-resource stochastic record-arrow gate.

## T122 Result

[T122](../tests/T122-stationary-markov-monotone-obstruction.md) closes the
finite stationary Markov version of the T116 zero-resource gate. For any finite
Markov chain with stationary distribution `pi` and scalar score `f`,
stationarity gives zero `pi`-weighted expected drift:

```text
sum_i pi_i E[f(X_{t+1}) - f(X_t) | X_t = i] = 0
```

So if the expected drift is nonnegative on every state in stationary support,
it must be zero on that support. Strict expected finality can occur only in
transient or nonstationary sectors, or after naming a sink, boundary, capacity
resource, postselection, or excluded reverse channel.

This further demotes H7 as a thermodynamic-arrow claim. A future H7 model must
be explicitly nonstationary, infinite-state, coarse-grained, or
resource-explicit, and must quantify the free-energy, boundary, memory, or
capacity drawdown rather than calling that drawdown finality.

## T128 Result

[T128](../tests/T128-minimal-living-arrow.md) constructs the first finite
models that survive the obstruction stack. The closed reversible control and
stationary Markov control fail as expected. The smallest non-stipulative
survivor is finite resource drawdown:

```text
R3 -> R2 -> R1 -> R0
drawdown = 3 - resource
```

Maintenance survives only when it consumes a finite repair budget. Open
boundary survives only when the boundary sink, exported history, or sink
capacity is counted. Constructor restriction is the smallest formal survivor,
but only by stipulating that reverse transformations are inadmissible.

This keeps H7 as a resource-accounting or constructor lemma. It does not
promote H7 as a thermodynamic-arrow claim.

## T124 Result

[T124](../tests/T124-constructor-admissibility-grounding-audit.md) turns the
T18 admissibility premise into a reverse-edge ledger. Every strict
D1-increasing edge must name the accounting boundary, reverse edge, reverse
status, and resource or impossibility condition.

The audit covers T18, T80, T84, T106, T110, T116, T122, and T128-style cases.
No current witness permits an unqualified physical-arrow reading. Surviving
strict edges are either resource-accounting edges, such as sink capacity,
exported history, erasure, path irreversibility, or finite resource drawdown,
or constructor-only edges where the reverse is stipulated inadmissible.

This further narrows H7: the missing upgrade is a physically grounded
constructor-impossibility relation for record deletion or definalization that
does not reduce to ordinary resource, entropy, boundary, or coarse-graining
accounting.

## T141 Result

[T141](../tests/T141-t1-record-graph-admissibility-ledger.md) grounds that
T124 blocker on the project's explicit T1 causal-record graph. The audit tests
strict D1 increases produced by observer access grants, same-chain record
copies, and branch-spread copies, then classifies the reverse edge under the
same holder, access, and erasure accounting.

The result is negative for H7's stronger reading. No tested strict T1
increase has a constructor-impossible reverse. Access grants are reversible
observer-boundary changes. Holder-support and branch-robustness gains survive
only as fresh-holder plus erasure-accounting edges. The current T1 substrate
therefore still supports H7 only as reversible-boundary or
resource-accounting language, not as a grounded physical arrow.

## T142 Result

[T142](../tests/T142-thermodynamic-erasure-calibration.md) applies the next
standard absorber to the T141 survivor. Access grants remain observer-boundary
changes. Same-chain record copies and branch-spread copies split into two
ordinary reverse descriptions:

```text
full source-copy correlation and reversible control available -> uncopy
blind reset or overwrite without that handle -> ordinary erasure/free-energy accounting
```

The result preserves one non-arrow residue: same-chain copy and branch-spread
copy can have the same one-bit blind-reset floor while changing different D1
topology dimensions. That means D1 topology is not identical to thermodynamic
cost, but it does not create a thermodynamic arrow by itself. The current H7
survivor remains a resource-accounting or constructor lemma unless a future
physically typed substrate produces a D1 split at fixed free-energy, capacity,
sink, boundary, provenance, and reversible-control data.
