# Cap_TI: Temporal Issuance Capability Object Specification

## Status

Open formal target. This is not H7 evidence, not a claim promotion, and not
a source-arrow derivation. It is the missing third leg of the Temporal
Issuance reopen burden: before a hostile same-neighbor-data split can be
constructed for any mu candidate (including mu_M), a task-natural capability
object must be declared.

## Why This Exists

The five-run metabolic-issuance persona panel (2026-06-22) converged on a
single bottleneck: neither the metabolic scaling exploration (mu_M candidate)
nor the optimal issuance rate exploration (lambda*(s) candidate) names what
capability a system with a Temporal Issuance source measure has that a system
without it cannot have. Without Cap_TI, the reopen burden items 3 and 5 of
the source-object spec remain unaddressed, and no hostile split can be
constructed.

Reference: `open-problems/temporal-issuance-source-object-spec.md`,
reopen burden items 3 and 5.

## The Gap

The source-object spec requires:

```text
Cap_TI : Y_TI -> K_TI
R_K_TI  native comparison on K_TI
```

"Recovering the hidden issuance variable" is explicitly excluded as a
capability. The capability must be task-natural: something an external agent
could observe, measure, or use to make better decisions, not just the internal
accounting identity of mu itself.

The metabolic scaling exploration names mu_M (structurally-motivated
hierarchical branching measure) but stops there. It does not ask: what can a
system do with mu_M as its source measure that it cannot do with entropy or
causal order as its source measure?

## Three Cap_TI Candidate Classes

The following candidates are ranked by how likely they are to survive the
same-neighbor-data freeze. Each candidate is stated, then assessed against
known absorbers.

### Candidate A: Scale-Sensitive Source-Order Certification

**Capability statement**: Given a set of observer records and declared
branching topology, certify the source precedence order at scale with fewer
record queries than a system using only causal order and entropy.

**What this would mean**: A system with mu_M as its source measure can
determine which source events came before which other source events using
fewer observations, because the branching exponent encodes structural
information about the order that entropy does not. At scale, the branching
hierarchy constrains the number of distinct orderings compatible with any
given entropy value -- fewer orderings need to be ruled out.

**Absorber risk**: High. Causal order already certifies precedence without
entropy. The branching topology, if it is the same as the transport graph
structure already encoded in D1RestrictionSystem's gluing data G, does not
add independent certification power. Surviving this candidate requires
showing that mu_M certifies order at a scale where both causal order and
G-encoded topology are ambiguous.

**Formal target**: For two D1RestrictionSystems (R_1, G_1) and (R_2, G_2)
with identical causal order and entropy but different branching exponents
beta_1 ≠ beta_2, show that the number of minimal record queries needed to
certify source precedence at scale n differs by a function of
|beta_1 - beta_2|. If this function is nonzero and not reproduced by
any quantity fixed in the same-neighbor-data freeze, Candidate A survives.

**Demotion condition**: If the query-count difference is zero when G is
matched (because G already encodes branching), Candidate A is absorbed by
G and closes.

### Candidate B: Reconstruction Reliability Under Access Loss With
Branching-Topology Dependence

**Capability statement**: Under degraded observer access (partial record
loss, channel noise, or access boundary shrinkage), a system with mu_M as
its source measure can bound reconstruction reliability with tighter or
qualitatively different guarantees than a system using entropy-alone or
causal-order-alone, and the bound depends on the branching exponent.

**What this would mean**: The 3/4 branching exponent is not just a scaling
law; it is a redundancy-encoding structure. In hierarchically-branched
systems, local record loss is partially compensated by the branching
structure -- the same event leaves traces at multiple scales. A system that
knows mu_M knows how much redundancy exists at each scale and can compute
reconstruction reliability as a function of access loss more precisely than a
system that only knows total entropy.

**Absorber risk**: Medium. Quantum Darwinism and provenance-aware redundancy
(Q1A territory) already deal with redundant multi-branch records. The
question is whether the metabolic scaling branching structure introduces
redundancy that is not already captured by the SBS (Spectrum Broadcast
Structure) framework. This is a non-trivial question because metabolic
branching is hierarchical (nested levels) while quantum redundancy is
parallel (same-level copies in environment fragments).

**Formal target**: For two source systems with the same causal order, entropy
production, event count, and SBS fragment count but different branching
exponents beta_1 ≠ beta_2, show that their reconstruction reliability under
k-fragment loss differs. This tests whether hierarchical branching adds
reconstruction reliability beyond what flat redundancy provides.

**Demotion condition**: If the reconstruction-reliability bound factors
through the SBS fragment count and causal order alone (making beta irrelevant
given those), Candidate B is absorbed by Q1A/Quantum Darwinism.

### Candidate C: Observer-Reconciliation Bound That Depends on Branching
Exponent

**Capability statement**: The minimum number of observer-pairwise
reconciliations needed to achieve global source-order agreement is bounded
above by a function that decreases with the branching exponent. A system
with mu_M as its source measure can predict this bound before reconciliation
begins; a system with entropy-as-mu cannot.

**What this would mean**: In a D1RestrictionSystem with multiple observers,
reconciliation cost (the number of disagreements that must be resolved) is
not just a function of how many records exist (entropy) or what order they
appear in (causal order). It is also a function of how hierarchically
organized the source events are. More hierarchical branching means fewer
independent chains of events that observers can disagree about -- disagreements
propagate upward to branch points and can be resolved there. The branching
exponent beta controls this propagation efficiency.

**Absorber risk**: Lower. This capability is not straightforwardly owned by
causal order (which doesn't predict reconciliation cost), entropy (which
doesn't encode the hierarchical structure), or Q1A (which is about redundant
copies of single events, not multi-event reconciliation chains). The closest
neighbor is TaF's own colimit/descent machinery (G), which handles
reconciliation. The key question is whether mu_M predicts the cost of that
machinery before it runs, which G does not by itself.

**Formal target**: For two D1RestrictionSystems with matching causal order,
event count, entropy, and gluing data structure type but different branching
exponents beta_1 < beta_2, show that the expected reconciliation rounds
R(beta_1) > R(beta_2) -- higher branching exponent means fewer required
reconciliation rounds. This would make Cap_TI = "predicted reconciliation
efficiency under declared branching topology."

**Demotion condition**: If the reconciliation bound is fully determined by G
(the gluing data), then Cap_TI is not independent of TaF's existing
formalism. If it is fully determined by causal order (topological sorting
suffices), Candidate C is absorbed by ordinary causal structure.

## Recommended Priority Order

Candidate C > Candidate B > Candidate A

Candidate C has the lowest absorber risk because it identifies a capability
(predicting multi-observer reconciliation cost before it happens) that is
not straightforwardly owned by causal order, entropy, SBS, or G taken
separately. It is also the most operationally testable: reconciliation rounds
are a countable quantity, not a continuous functional.

Candidate B is promising if metabolic hierarchical branching genuinely differs
from flat quantum redundancy in reconstruction-reliability guarantees. This
is a meaningful technical question that would engage the Q1A literature
productively.

Candidate A has the highest absorber risk: if G encodes branching topology
(which the D1RestrictionSystem formalism may already do through its gluing
data), then scale-sensitive certification is already available without mu_M.

## Required Before Any Hostile Split

Before constructing the hostile same-neighbor-data split (reopen burden item 5),
one of the three Cap_TI candidates above must be:

1. Chosen as the operative capability
2. Given units and a native comparison R_K_TI (e.g., for Candidate C:
   "expected reconciliation rounds, compared by >=")
3. Tested in a positive-control fixture where causal order is visible and
   mu_M's prediction is verified
4. Tested in the freeze fixture where causal order and entropy are matched
   and mu_M differs by the declared branching exponent

Only after steps 1-4 does the same-neighbor-data split become executable.

## What This File Does Not Claim

- This does not promote H7.
- This does not claim that mu_M has been shown to be a nonabsorbed source
  primitive.
- This does not propose a new source object for Temporal Issuance.
- This does not update CLAIM-LEDGER.md.

## Demotion Rule for All Three Candidates

If the chosen Cap_TI candidate's value is determined by some combination of
the same-neighbor-data freeze vector (causal order, volume/counting,
thermodynamic ledgers, information state, instrumentation, access, cadence,
record-generation rule, gluing data) without remainder, Cap_TI is absorbed,
the hostile split cannot be constructed, and the Temporal Issuance bridge
closes as translation residue for this capability class.

## Status Update — 2026-06-22

**Candidate C is now the operative capability.**

Steps 1-4 are complete for Candidate C:

1. **DONE** — Candidate C selected as operative capability: predicted reconciliation rounds R(beta)
2. **DONE** — Units and native comparison declared: R_continuous = n^(1-beta), R_K_TI = >= on rounds
3. **DONE** — Positive-control fixture PASSED: R(beta=0.85)=1.52 < R(beta=0.75)=1.68 for matched 20-event systems (cap-ti-candidate-c-positive-control-v0.1-results.md)
4. **DONE** — Hostile same-neighbor-data split COMPLETE (T188): G(Alpha)=G(Beta) (identical gluing topology) but beta(Alpha)≠beta(Beta) (different delivery-time metric). G encodes topology but not timing. Continuous R(Alpha) > R(Beta) at all n. At n=20 with CV-proxy betas: 7.03 vs 5.28 rounds (24.9% reduction). A system knowing mu_M predicts fewer rounds BEFORE reconciliation; causal order alone cannot.

**Cap_TI Candidate C advances to OPERATIVE CAPABILITY for physical-substrate systems.**

The ceiling-based R formula from step 3 is replaced by the continuous R = n^(1-beta) for step 4 verification (ceiling formula too coarse at small n for the beta differences produced by T186/T187).

**Remaining conditions before formal promotion:**
- FUNCTOR-OBL-TaF-001: RESOLVED 2026-06-24 by T221 (directional split). The
  covariant F: States(Ext_S) -> FinSets is NOT a functor; the contravariant
  F_op IS. The functorial direction is the opposite of the one the issuance
  dynamics need, so this is settled by refutation, not satisfaction.
- PO1-NCK-001: re-scoped by T221 to "PO1 types K, not lambda*(S)"; it cannot be
  promoted to a supported formal connection over covariant FinSets. Any
  promotion of lambda*(S) now requires F_partial over ParSets (open).
- The reconciliation protocol grounding the continuous R formula must be specified.

## Contribution Needed

All 4 steps are now completed for Candidate C. Later gates resolved or repriced
the remaining follow-up burdens:

1. FUNCTOR-OBL-TaF-001 is resolved by T221 as a directional refutation, not as
   the covariant functor the issuance dynamics wanted.
2. The continuous reconciliation cost formula is grounded only as review
   machinery by T513.
3. Promotion would still require a governed source-object contract and claim
   movement path; T513 does not supply either.
4. If demotion occurs (e.g., G is extended to include timing), record the
   demotion condition here.

No capability candidate from this file should be promoted to Cap_TI status
without steps 3 and 4 being executed on it. Candidate C has now cleared steps 1-4.

## Status Update - 2026-07-09: T513 Protocol-Grounding Gate

T513 makes the remaining protocol-grounding burden executable:
`tests/T513-cap-ti-reconciliation-protocol-gate.md`.

Verdict:
`CAP_TI_RECONCILIATION_PROTOCOL_GATE_BUILT_REVIEW_ONLY`. A future Cap_TI
reconciliation packet must predeclare beta, the timing metric beta reads, the
finite reconciliation unit, observer-pair schedule, hierarchy capacity
`ceil(n^beta)`, and integer round interpretation `ceil(n^(1 - beta))` before
using the continuous formula as review material. A synthetic high-beta packet
requires fewer rounds than the matched low-beta packet, same-beta null controls
match, and formula-only, topology-only, post-hoc beta, hidden-timing,
round-mismatch, claim/public-posture, external-publication, and cross-repo
shortcuts are rejected, absorbed, or blocked.

This grounds the formula as review machinery only. It does not promote Cap_TI,
H7, Temporal Issuance source truth, a physical-substrate theorem, source-object
contract completion, claim-ledger movement, roadmap movement, README movement,
North Star movement, public-posture movement, hard-policy movement, external
publication, or cross-repo truth movement.
