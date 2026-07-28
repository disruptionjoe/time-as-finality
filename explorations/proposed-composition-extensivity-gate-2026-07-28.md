# Proposed Gate (Un-Numbered): Capability Composition and Extensivity on the T583 Contract — T587-Compliant Reopening Packet

**Status:** reopening packet and proposed gate spec only. **No T-number is
minted here; the owner mints the number if the reopening is accepted.** Landed
under `explorations/` deliberately, to avoid numbering collisions and because
minting a T-scaffold is exactly what T587's stop forbids doing unilaterally.
No fixture is built and no run is executed; execution is a separate owner
decision.
**Date:** 2026-07-28
**Reopening target:** the composition/extensivity gate *named, not opened* in
[landauer-rate-and-capability-indexed-discriminator-2026-07-27.md](landauer-rate-and-capability-indexed-discriminator-2026-07-27.md)
(Part 2 (ii) step 3 and "Constructive next object" 1) — the gate required
before any capability-indexed rate density can exist.
**Builds on:** [T583](../tests/T583-capability-contract-v1.md) (the contract
being extended), [T584](../tests/T584-capability-invariance-morphism-gate.md)
(the invariance classes the extension must respect),
[T585](../tests/T585-landauer-physical-capability-gate.md) (the physical
fixture class), [T586](../tests/T586-record-capability-order-gate.md) (the
record-dependence mechanism that sources the obstruction),
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md) (the stop this
packet answers), [T588](../tests/T588-record-issuance-contract-fork-gate.md)
(the reopening precedent and the issuance contract this packet extends)
**Tags:** `spec_only` · `reopening_packet`

---

## Why This Packet Satisfies T587's Reopening Conditions

T587 closed Lane 1's record-capability line with an explicit stop, quoted
verbatim from its results:

> Do not continue producing T-number scaffolds from T586 alone. Reopen Lane 1
> only for a provenance-valid physical source packet, a frozen capability
> witness, or a sharper counterexample that changes the record-issuance
> contract.

Three conditions. T588 reopened on the third by asking a question T586/T587
left undeclared (*into what does a record get issued?*). This packet invokes
the **third condition** again, one level up, and argues compliance against
T587's text clause by clause:

1. **Not a T-number scaffold from T586 alone.** The stop targets the move
   T587 proved sterile: overlaying another comparator on the frozen T586
   event system, where every candidate is absorbed by standard dependency and
   causal comparators. This packet performs no comparison on that frozen
   system at all. It operates at the **T583/T584 contract layer**: it adds a
   declared composition structure (a new morphism class and a new context
   constructor) that no gate T583–T588 declares. The wave-3 companion note
   established that without this structure, additivity of capability is *not
   even statable* in the contract. New contract structure is not another
   comparator; it changes what the contract can express.

2. **The sharper counterexample, and why it changes the record-issuance
   contract.** The packet carries a structural counterexample, fully
   specified in the Setup and constructible from already-frozen fixtures:
   two T585 one-bit Landauer cells composed side by side, where one
   composite task (`certify_cross_record_stability` in cell 2's namespace)
   requires the standard record whose **unique producer** is cell 1's erase
   event — T586's own admission mechanism run *across a composite boundary*.
   Neither component context has this task alone; the coupled composite
   does. The counterexample is sharper in the operative sense: it shows the
   current record-issuance contract is silent on a question whose answer
   changes measured capability. T588 adjudicated the ledger question (B
   refuted; per-observer A and regional-merge C both left standing);
   this counterexample forces the successor clause the contract does not
   have: **when declared contexts compose, into which namespace is a record
   issued, and which tasks may consume records across the composite
   boundary?** Different answers yield different capability envelopes
   (deviation Δ = ∅ versus Δ ≠ ∅ below). A counterexample that forces a new
   consumption clause into the issuance contract is precisely one "that
   changes the record-issuance contract."

3. **Lineage with the T588 precedent.** T588's reopening logic was: not a
   comparator on the frozen system; a structural question T586/T587 leave
   undeclared; at least one candidate answer refutable. This packet has the
   same shape: not a comparator; a structural question T583–T588 leave
   undeclared (composition and cross-namespace consumption); and a decisive
   fork (extensivity holds on independent composites, or it does not — each
   exit is consequential, see What The Gate Feeds).

4. **The stop's procedural content is honored.** No T-number is minted; the
   spec lands in `explorations/`; the owner decides the reopening — this
   packet argues admissibility only. The wave-3 note pre-registered exactly
   this requirement: "opening it requires a T587-compliant reopening
   packet."

Stated honestly, what this packet does **not** invoke: no provenance-valid
physical source packet is supplied (no literature import happens here), and
no frozen capability witness beyond the already-frozen T585/T586 fixtures is
claimed. If the owner reads "sharper counterexample" as requiring an
*executed* witness rather than a fully specified constructible one, the
minimal pre-step is to run the ρ₁ witness of the Setup as an un-T-numbered
exploration companion (same discipline as the wave-3 note's overlay model)
and re-submit this packet with the run attached.

## Construction Fork Declaration

Per the repository's construction-fork discipline, the forks are identified
and named, not defaulted:

- **Composition as declared contract structure vs emergent physical
  junction.** This gate uses the *declared* construction: ⊗ is a new
  contract clause on declared contexts, in the same sense that T583's
  context is itself declared. It does not claim physical systems compose
  this way; a physical-junction construction would need its own source
  packet. Chosen because the object under test is the contract.
- **Parallel vs serial composition.** v1 declares *parallel* composition
  (simultaneous operation under a shared time window). Serial composition
  (time budgets add, outputs feed forward) is a different declared
  operation, out of scope for v1; justification under the time-budget
  choice below.
- **Attainable-envelope vs exercised-task indexing** (inherited open fork
  from the wave-3 note): this gate is stated on the *attainable* envelope,
  T583's native object. The exercised-task reading composes differently and
  remains open.

## Target Claims

- T583's CapabilityContract admits a declared parallel composition C₁ ⊗ C₂
  compatible with T584's invariance classes.
- Envelope-level extensivity, Env(C₁⊗C₂) = Env(C₁) ⊕ Env(C₂), is decidable
  and executable on independent composites of the T585 fixture class.
- The record-coupled deviation Δ(ρ) is well-defined, T584-invariant, and
  monotone in coupling strength — a capability-synergy measure.
- The `CAPABILITY-TO-TEMPORAL-ORDER` lane's contract hygiene, and the
  TAF3/TAF8 boundary discipline, exactly as in T583–T585.

## Setup

### The composition clause (the packet's core)

Given two T583 contexts C₁, C₂ (fields as implemented in
`models/t583_capability_contract_v1.py`: region, observer, access profile,
task family, operation menu, provenance fields, Budget(energy, time,
communication, memory, error), horizon, physical equivalence, gauge
quotient, native comparison, irrelevant coarse-graining fields), the
parallel composite C₁ ⊗ C₂ is defined **only when the intensive restriction
holds**. The clause is organized by the thermodynamic extensive/intensive
split, because that is the split under which a density can exist at all:
extensive quantities add at fixed intensive conditions.

**Intensive fields — must be equal; composition fails closed otherwise:**

- `source_theory` (both components drawn from the same declared source law);
- bath temperature (the declared thermal access datum and the `kBT ln 2`
  unit normalization — see Known Physics Constraints for why this
  restriction is load-bearing, not cosmetic);
- **time budget — equal and shared.** This is the declared choice between
  equal/shared and max, and the justification is the gate's purpose: the
  discriminator's target quantity integrates capability over regions at a
  fixed observation window ("signal per gram per second"), so the physically
  meaningful composite is *simultaneous operation* and the window is one
  shared intensive datum, not an additive resource. Summing time budgets
  models serial scheduling and conflates rate with sequencing; taking an
  unequal max silently hands the shorter component undeclared slack — a
  changed budget, which T583/T585 already classify as a resource/budget
  completion, not capability. Equal-and-shared is the only reading under
  which a per-region rate can integrate. (Serial ⊗ is a different declared
  operation, out of scope v1.)
- error bound and horizon (one composite cycle).

**Extensive fields — add, carrying a declared partition; no pooling:**

- energy (work), memory, and communication budgets add:
  B(C₁⊗C₂) = B₁ + B₂, **carrying the partition** — each component's
  namespaced tasks are charged against that component's declared share.
  Budget pooling (reallocating shares across the boundary) makes
  performance points feasible that neither component affords alone; per
  T583's own discipline a changed budget is a `RESOURCE_COMPLETION`, so
  pooling is classified as completion, never as composite capability and
  never as synergy. The partition rule is load-bearing twice over: it keeps
  independent extensivity from being trivially broken by resource transfer,
  and it underwrites Δ-monotonicity below (existing points' feasibility
  never changes when coupling edges are added).

**Structural fields:**

- regions: disjoint union R₁ ⊔ R₂ with disjointness declared (no shared
  substrate); overlapping regions fail closed;
- observer/access: tagged disjoint union of access profiles; the composite
  observer is the pair;
- task families and operation menus: **tagged (namespaced) disjoint
  union** — every task identifier and every record identifier carries its
  component namespace; an untagged collision fails closed;
- physical equivalence / gauge quotient: componentwise product quotient
  (each component's gauge acts on its own namespace);
- native comparison: unchanged — task-indexed Pareto cover, now over the
  namespaced task union;
- irrelevant coarse-graining fields: tagged union.

**Independence vs record coupling — the fork the gate exists to measure:**

- **Independent composite C₁ ⊗ C₂:** no cross-namespace record consumption
  and no cross-namespace communication. Every executable task consumes only
  records issued in its own namespace.
- **Record-coupled composite C₁ ⊗_ρ C₂:** additionally declares a
  cross-consumption rule ρ — a finite set of edges
  (record issued in namespace i) → (task in namespace j ≠ i) admitted as
  prerequisites. ρ is declared, never inferred. Issuance stays namespaced:
  records are always issued into the producing component's namespace; ρ
  governs consumption only. This is the new record-issuance-contract clause
  the reopening argument names.

### Envelope composition and the extensivity question, formalized

Define ⊕ on envelopes as the **namespaced disjoint union of frontiers with
the product preorder**: Env(C₁) ⊕ Env(C₂) contains ι₁ of component 1's
canonical points and ι₂ of component 2's; points compare within a namespace
as in that component; there is no cross-namespace domination.

**Extensivity (envelope level, scalar-free — the primary statement).** For
independent composites:

> Env(C₁ ⊗ C₂) = Env(C₁) ⊕ Env(C₂)

— after canonicalization, the composite attainable frontier is exactly the
namespaced union: no new Pareto points, no new dominations, incomparability
preserved. The statement is deliberately order-theoretic: T583 lists
"capability defaults to one scalar" as a failure criterion, so this gate's
additivity claim never routes through a scalar.

**Scalar corollary (secondary, declared-only).** For any *explicitly
declared*, T584-invariant scalarization s that is ⊔-additive by
construction, envelope extensivity yields s(C₁⊗C₂) = s(C₁) + s(C₂). The
gate certifies the envelope statement; it neither supplies nor blesses any
scalarization — that remains the separate burden of the wave-3 note's
Part 2 (ii) step 2, untouched here.

**The known obstruction, recorded honestly (why the gate must fork).**
T586's entire content is that an executable task of one event can require a
record whose unique producer is another. Under any ρ ≠ ∅ the coupled
composite has executable tasks neither component has alone, so generically

> Env(C₁ ⊗_ρ C₂) ⊋ Env(C₁) ⊕ Env(C₂)

— **superadditivity is the expected behavior of record-coupled composition,
not a pathology.** The gate therefore does not deny the deviation; it makes
the deviation the measured object:

> Δ(ρ) := the set of canonical frontier points (and induced dominations) of
> Env(C₁ ⊗_ρ C₂) absent from Env(C₁) ⊕ Env(C₂),

with three requirements: Δ is well-defined on T584 orbits (invariant under
componentwise representation, gauge, and declared coarse-graining);
Δ(∅) = ∅ exactly when independent extensivity holds; and Δ is **monotone
under coupling strength**: ρ ⊆ ρ′ ⇒ Δ(ρ) ⊆ Δ(ρ′). Δ is a
capability-synergy measure, and arguably the more interesting quantity in
this program: it is what separates an organized record-former from an
undifferentiated crystal at matched mass — exactly the axis the wave-3
discriminator needs to couple to.

### Morphism extension (T584 compatibility)

- **Existing T584 classes extend componentwise.** Substantive
  representation changes (task interface, units, protocol labels,
  implementation traces), gauge changes (representatives inside each
  component's quotient), and declared irrelevant coarse-graining each act
  on their component's namespace and must preserve the composite envelope;
  composite gauge factors through the product quotient.
- **The new admissible class this packet introduces: the embeddings
  ι_i : C_i → C₁ ⊗ C₂,** with the interchange laws:
  - *restriction law:* Env(C₁⊗C₂) restricted to namespace i covers
    ι_i(Env(C_i)) always (embedding never loses capability), with
    per-namespace equality exactly on independent composites — that
    equality *is* extensivity stated locally;
  - *interchange square:* for admissible componentwise morphisms f₁, f₂,
    the map f₁ ⊗ f₂ is admissible on composites and
    (f₁ ⊗ f₂) ∘ ι_i = ι_i ∘ f_i;
  - *symmetry and associativity:* the swap C₁⊗C₂ → C₂⊗C₁ and reassociation
    are admissible and preserve the envelope;
  - *order-compatibility:* ⊗ is monotone in the native preorder (component
    covers imply composite cover) — required for any density to live on
    capability classes rather than on presentations.
- **Inadmissible by construction:** the untagged namespace merge —
  identifying task or record vocabulary across components — the composite
  descendant of T584's certification/recovery merge counterexample. It
  changes the native envelope and must be rejected.

### The executable witness class (specified here, not run)

Fixture class = T585's one-bit Landauer memory cell, unchanged. Two cells
at equal declared bath temperature, equal time budget 5.0, equal error
0.01, equal horizon `single_reset_cycle`; energy 0.75 + 0.75 under the
declared partition; task families {erase_to_standard_record,
certify_record_stability} × {namespace 1, namespace 2}.

- **Independence check:** the composite envelope must equal the ⊕ of the
  two T585 envelopes, by canonical (bitwise-after-canonicalization)
  comparison.
- **Coupling ρ₁** = {(standard record issued by erase in namespace 1) →
  (task `certify_cross_record_stability` in namespace 2)}: cell 2 gains an
  executable task requiring the record whose unique producer is cell 1's
  erase event — T586's seed → erase → certify mechanism run across the
  composite boundary. Predicted: Δ(ρ₁) ≠ ∅ (a frontier point of the coupled
  composite with no preimage in ⊕).
- **Coupling ρ₂ ⊋ ρ₁** adds the symmetric edge. Predicted:
  Δ(ρ₁) ⊆ Δ(ρ₂).

## Success Criteria

- ⊗ is defined on the T585 fixture class with every intensive restriction
  enforced fail-closed.
- **Envelope-level extensivity holds on independent composites:** canonical
  equality Env(C₁⊗C₂) = Env(C₁) ⊕ Env(C₂); incomparability preserved; no
  cross-namespace domination appears.
- All three T584 morphism classes extend componentwise and preserve the
  composite envelope; the interchange square, swap symmetry, and
  order-compatibility laws pass.
- Δ is well-defined: T584-invariant, Δ(∅) = ∅ on the independence check,
  nonempty on ρ₁, and monotone from ρ₁ to ρ₂.
- **Controls that must fail (teeth):**
  - *scalarized-capability control:* a default composite scalar (a summed
    "capability score") is rejected as a T583 failure-criterion violation.
    The control exhibits two independent composites with equal scalar
    totals and non-isomorphic composite envelopes, so the scalar
    demonstrably collapses distinctions the native order keeps; it must
    fail to stand in for the envelope verdict.
  - *namespace-collision control:* the untagged task/record-vocabulary
    merge changes the native envelope and is rejected as inadmissible.
  - *budget-pooling control:* reallocating shares across the declared
    partition makes a point feasible that neither component affords; it is
    classified `RESOURCE_COMPLETION`, never composite capability, never
    synergy.
  - *unequal-bath control:* composition at unequal declared temperatures
    fails closed — rejected, not silently unit-normalized away.
- **Firebreak inherited from T587's boundary typing:** Δ, like any
  capability delta, is never counted as a record-order edge, an issuance,
  or a temporal quantity by itself.

## Failure Criteria

- Envelope additivity fails on an independent composite of the fixture
  class (Exit B fires — see What The Gate Feeds).
- ⊗ cannot satisfy the T584 extension laws: componentwise preservation,
  the interchange square, swap symmetry, or order-compatibility fails
  (Exit B fires).
- A scalarization is defaulted anywhere in the gate.
- Cross-namespace record consumption occurs without a declared ρ, or
  issuance is silently re-namespaced across the boundary.
- Δ or any capability delta is treated as a record-order edge, issuance,
  temporal order, or time.
- The gate is used to move claims, canon, Lane posture, public posture, or
  any cross-repo result.

## What The Gate Feeds (both exits, stated in advance)

- **Exit A — extensivity holds on independent composites and Δ is
  well-behaved.** A capability rate *density* becomes definable on
  independent scaffolds, with Δ the candidate correction term sourced by
  cross-namespace record coupling. The wave-3 discriminator spec's
  pre-registered extensivity kill **un-arms** (does not fire). Un-armed is
  not alive: canonical contextualization (Part 2 (ii) step 1) and a
  declared T584-invariant scalarization (step 2) remain open burdens before
  any density is actually constructed, and the differential-signature
  design study remains a separate owner decision.
- **Exit B — additivity fails even on independent composites, or ⊗ is
  incompatible with T584's invariance classes.** The pre-registered kill
  **fires**: the capability-indexed rate-density sub-variant dies at the
  contract level, before any experiment is designed. Per the charter, this
  precise failure is a successful outcome; the death is recorded in the
  discriminator lineage and the design study never opens.
- **Secondary feed, hedged.** T588 left per-observer ledgers (A) and
  regional-merge ledgers (C) standing, unresolved by reunion counts. The
  composition clause is where A-like and C-like bookkeeping first diverge
  on the capability side (is cross-namespace consumption ever admissible,
  and when do namespaces reconcile?), so a well-defined Δ *may* give the
  A-versus-C residual a new observable. Named as a possible connection
  only; nothing in this gate adjudicates A versus C.

## Known Physics Constraints

- The only physical source input remains T585's bounded Landauer-style
  erasure cost. Nothing else physical enters the gate.
- The extensive/intensive organization mirrors ordinary thermodynamic
  extensivity — densities exist where extensive quantities add at fixed
  intensive conditions. That is an organizing analogy for the *contract*,
  not a derived physical law.
- The equal-bath-temperature restriction is load-bearing, not cosmetic:
  two baths at unequal temperatures admit a work-extraction (heat-engine)
  channel between components — composite tasks neither part has alone for
  reasons that have nothing to do with records. Unequal-T composition
  would source superadditivity through a non-record channel and
  contaminate Δ as a record-coupling measure. Equal temperature removes
  that channel by construction.
- No rate constant is established or used; no collapse model is endorsed;
  the GRW/CSL/Diósi–Penrose comparators of the wave-3 note do not appear
  in this gate.
- Nothing in the gate derives time, temporal order, or issuance; the
  entire construction lives at the declared-contract level.

## What This Does Not Claim

- **No T-number is minted.** The owner mints the number if and when the
  reopening is accepted. This packet argues admissibility; it does not
  perform the reopening, and it does not treat the reopening as granted.
- **No execution.** No fixture is built and no run is performed here; the
  witness class is specified so that execution, if the owner opens the
  gate, is mechanical. Execution is a separate owner decision.
- **No claim movement.** No claim-ledger, Canon Index, hypothesis, Lane,
  or public-posture change; the T585/T586/T587/T588 verdicts are
  untouched.
- **Superadditivity under record coupling is a design prediction, not a
  result;** independent-composite extensivity is a question, not an
  assumption. Both directions of the fork are live until the gate runs.
- **Capability remains T583's operational, executable-task measure and
  nothing else** — not consciousness, not cognition, not awareness, not
  agency. The wave-3 note's verbatim guard is inherited in full; Δ is a
  task-envelope difference, not a mind-adjacent quantity.
- **No bearing on the foliation branch.** ⊗ composes declared contexts,
  not spacetime slicings.

## Contribution Needed

Owner decision on this reopening packet. If accepted: mint the T-number,
move this spec into `tests/` under house numbering, build the two-cell
witness class of the Setup as the model, and run it with `--write-results`
plus a focused unit test before treating the gate as opened. If the owner
reads T587's third condition as requiring an executed counterexample first,
run the ρ₁ witness as an un-T-numbered exploration companion (the same
discipline as the wave-3 note's overlay model) and re-submit this packet
with the run attached.
