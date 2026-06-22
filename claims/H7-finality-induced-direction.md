# H7: Finality-Induced Direction

## Claim

Finality structure can induce an observer-relative temporal direction when
admissible transformations are monotone in D1 finality.

## Class

Conjecture.

## Status

Paper-facing physical-arrow reading demoted. H7 is partially supported only as
a conditional constructor-style theorem and resource/reverse-edge audit
discipline; weakened against direct physical reading by T80, T82, T84, T106,
T110, T116, and T122. T128 identifies the smallest finite survivors and keeps
the status narrowed. T124 adds the reverse-edge grounding gate and blocks
unqualified physical-arrow readings for the current witness stack. T142
calibrates the T1/T141 survivor against reversible uncopy and ordinary
erasure/free-energy accounting. T144 requires future witnesses to declare the
reverse-edge class, T145 shows that fixed-accounting D1 topology splits are
capability residue rather than arrow evidence unless physical deletion remains
impossible after full absorber accounting, and T148 makes the paper-facing
demotion explicit. T152 screens metastable records and finds that finite
barriers are kinetic/resource absorbers, while infinite barriers or denied
controls are constructor or boundary stipulations rather than physical-arrow
evidence. T160 extends that intake screen across the most natural remaining
substrate families: protected memories, driven dissipation, exact sector
restrictions, and horizon-style inaccessibility are all null by default unless
they still show finite constructor-impossible physical deletion after matched
accounting. N8 maps the broader stochastic-thermodynamic absorber stack that
any future physical-arrow witness must survive. N11 and N12 then ground two of
those family screens in the external literature: protected-memory and
driven-dissipative successes remain neighboring stability programs unless they
freeze a true physical-deletion reverse and still survive matched accounting.

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
- [T144: Definalization Reverse-Edge Taxonomy](../tests/T144-definalization-reverse-edge-taxonomy.md)
- [T145: Physical Record Deletion Fixed-Accounting Screen](../tests/T145-physical-record-deletion-fixed-accounting.md)
- [T148: H7 Paper-Facing Demotion Gate](../tests/T148-h7-paper-facing-demotion-gate.md)
- [T152: Metastable-Record Deletion Screen](../tests/T152-metastable-record-deletion-screen.md)
- [T160: H7 Substrate-Family Screen](../tests/T160-h7-substrate-family-screen.md)
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

## T144 Result

[T144](../tests/T144-definalization-reverse-edge-taxonomy.md) adds a sharper
typing rule to the H7 blocker. "Definalization" now splits into four
reverse-edge classes:

- observer-boundary access loss;
- support-copy removal;
- physical record deletion; and
- authority/provenance loss.

This narrows H7 again. Boundary access loss is not physical record deletion.
Support-copy removal is absorbed by reversible uncopy or ordinary
erasure/free-energy accounting under T142. Authority/provenance loss may matter
for admissibility and future capability, but it is not thermodynamic
irreversibility. Only physically typed record deletion remains a plausible
future physical-arrow class, and no current witness clears that bar.

## T145 Result

[T145](../tests/T145-physical-record-deletion-fixed-accounting.md) screens that
remaining physical-deletion class under matched absorber data: free-energy
floor, capacity, sink/export state, observer boundary, provenance, source-copy
status, and reversible-control access.

The only fixed-accounting split currently present is the T142 same-chain versus
branch-spread topology split. It can change future operation availability for a
branch-failure task, but the deletion reverse remains ordinary one-bit erasure
accounting. That is capability/topology residue, not thermodynamic-arrow
evidence. The other deletion-shaped cases change erasure work, reversible
control, sink state, access boundary, or provenance class.

H7's remaining upgrade target is therefore very narrow: a physically typed
record substrate where a `physical_record_deletion` reverse remains
constructor-impossible after all of those absorber variables are matched.

## T148 Result

[T148](../tests/T148-h7-paper-facing-demotion-gate.md) turns the H7 status into
a paper-facing gate. The allowed claims are now the conditional D1-monotone
constructor theorem, reverse-edge/resource-accounting audit discipline, and
the T145 future-operation/topology residue. The rejected claims are a
thermodynamic-arrow derivation from finality alone, physical-arrow support from
the current record-graph/deletion fixtures, and promotion of fixed-erasure D1
topology to arrow evidence.

H7 should not be presented as a physical-arrow or thermodynamic-arrow claim
unless a future physically typed record substrate clears the fixed-accounting
physical deletion gate and survives hostile thermodynamic, stochastic, and
resource-accounting absorbers.

## T152 Result

[T152](../tests/T152-metastable-record-deletion-screen.md) tests the most
natural physical-deletion substrate left after T145/T148: finite metastable
records protected by barriers.

The result is another demotion. Finite barriers can make records long-lived and
support retention capabilities, but deletion remains finite-rate or
finite-control possible. Barrier height, reservoir state, control windows, and
task horizon are ordinary kinetic/resource data. Infinite barriers block
deletion only by ideal constructor stipulation or state-space split, and denied
controls block deletion only relative to an observer/control boundary.

The only matched finite-barrier split is the T145 branch-topology residue:
future operation availability changes, but reverse deletion remains possible.
So metastability does not reopen H7 as a physical-arrow or thermodynamic-arrow
claim.

## T160 Result

[T160](../tests/T160-h7-substrate-family-screen.md) turns the remaining H7
substrate burden into a family-level triage rule. The most likely reopeners are
now screened before detailed modeling:

- protected memories are null until code-distance, syndrome, bath/reset, and
  finite control data are frozen and still leave deletion impossible;
- driven dissipative records are null until pumping, bias, chemostat, work,
  and sink accounting are matched and the reverse still fails;
- exact sector or gauge restrictions are null until they admit a finite
  operational substrate reading rather than an ideal ban; and
- horizon-style proposals are non-deletion families unless they are recast as
  actual physical deletion with matched access/control data.

This weakens H7's remaining open-ended search space. Future work should not
reopen the physical-arrow route with generic "protected memory" or "hard to
erase" language alone.

## N8 Absorber Map

[N8](../literature/N8-h7-stochastic-thermodynamic-absorbers.md) records the
standard literature absorbers for any future H7 physical-arrow claim:
Landauer/Bennett information thermodynamics, Jarzynski/Crooks/Seifert
stochastic thermodynamics, feedback thermodynamics, nonequilibrium steady-state
accounting, and chemical-reaction-network thermodynamics.

The map does not change H7 status. It sharpens the reinstatement gate: a finite
record substrate must match thermodynamic and information-accounting variables
and still exhibit a constructor-impossible `physical_record_deletion` reverse
before H7 can be promoted beyond conditional constructor/resource-accounting
language. T160 adds the intake rule: the common substrate families most likely
to be proposed next are null by default until they clear that burden on a
finite operational reading.

## N11 Protected-Memory Absorber

[N11](../literature/N11-h7-protected-memory-absorber.md) tests the most
credible protected-memory neighbor family directly against the T160/N8 gate:
topological memories, self-correcting codes, engineered-dissipation memories,
and symmetry-protected proposals.

The result is negative for H7's current physical-arrow route. The protected
memory literature targets stored-logical-information lifetime under thermal
noise, often with active recovery assumptions, barrier scaling, engineered
baths, higher-dimensional constructions, or strong symmetry restrictions. That
is a serious neighboring physics program, but it is not yet the same object as
an H7 `physical_record_deletion` reverse that remains
constructor-impossible after matched thermodynamic, information, boundary, and
control accounting.

So protected memories stay in the absorber stack by default. A future H7
proposal may borrow this family only after it freezes the deletion task,
allowed controls, decoder/syndrome assumptions, bath/reset channels, symmetry
enforcement, and future-operation target, then still shows more than lifetime
or barrier protection.

## N12 Driven-Dissipative Absorber

[N12](../literature/N12-h7-driven-dissipative-absorber.md) grounds the other
high-risk T160 family directly: pumped, chemostatted, reservoir-engineered,
and autonomously stabilized records.

The result is again negative for H7's current physical-arrow route.
Driven-dissipative successes are typically target-state preparation,
nonequilibrium maintenance, logical-lifetime extension, autonomous reset, or
phase-selection results under explicit drive, bath, or chemostat resources.
Those are serious neighboring achievements, but they are not yet the same
object as an H7 `physical_record_deletion` reverse that remains
constructor-impossible after work, pump, bath, sink/export, source-copy, and
control data are matched.

So driven-dissipative proposals also stay in the absorber stack by default. A
future H7 proposal may borrow this family only after it freezes the deletion
task, allowed controls, pump/reset/decoder structure, nonequilibrium resource
ledger, and future-operation target, then still shows more than maintained
steady-state order or kinetic residence.
