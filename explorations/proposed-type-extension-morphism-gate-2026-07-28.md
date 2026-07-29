# Proposed Gate (Un-Numbered): Type-Extension Morphism Class and Forecasting-Capacity on the T583/T584 Contract — T587-Compliant Reopening Packet

**Status:** reopening packet and proposed gate spec. **No T-number is minted
here; the owner mints the number if the reopening is accepted.** Landed under
`explorations/` deliberately, to avoid numbering collisions and because
minting a T-scaffold is exactly what T587's stop forbids doing unilaterally.
The packet's cheap ε-witness has been executed as an un-T-numbered
exploration companion per the composition precedent's fallback path; the run
is attached in the final section. Everything else — adoption, numbering, any
`tests/` promotion — is a separate owner decision.
**Date:** 2026-07-28
**Reopening target:** the type-extension morphism packet *named, not built*,
in [commit-module-s6-series-conclusion-2026-07-28.md](commit-module-s6-series-conclusion-2026-07-28.md)
§7 item 1 — "T584's morphism classes contain no type-extension class — the
cheapest formal object, same T587-compliant packet discipline as the
composition gate" — and in the ROADMAP commit-module entry's next objects.
**Builds on:** [T583](../tests/T583-capability-contract-v1.md) (the contract
being extended), [T584](../tests/T584-capability-invariance-morphism-gate.md)
(the invariance classes the extension must respect, and whose named gap this
packet closes), [T585](../tests/T585-landauer-physical-capability-gate.md)
(the physical fixture class),
[T586](../tests/T586-record-capability-order-gate.md) (the unique-producer
record mechanism the consumption discipline reuses),
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md) (the stop this
packet argues compliance against),
[T588](../tests/T588-record-issuance-contract-fork-gate.md) (the issuance
contract whose consumption rules bind new tasks),
[proposed-composition-extensivity-gate-2026-07-28.md](proposed-composition-extensivity-gate-2026-07-28.md)
+ [composition-extensivity-execution-2026-07-28.md](composition-extensivity-execution-2026-07-28.md)
(the ⊗/ι/ρ machinery and the structural precedent this packet follows
clause by clause),
[commit-module-s3-capability-graded-finality-2026-07-28.md](commit-module-s3-capability-graded-finality-2026-07-28.md)
(the finality grades whose extension-sensitivity is this packet's separation
witness), and
[covariant-formulability-capability-rate-2026-07-28.md](covariant-formulability-capability-rate-2026-07-28.md)
(the covariant-scope condition named, not tested, in the boundary sentences).
**Registered motivation:** Q-0066 — the two-stroke ratchet: prediction =
capability within a fixed type space; forecasting = capability under
type-space growth. Registered wiki-first 2026-07-28 on the private
thinking-wiki surface (Q-0066; pointer only, per public-repo hygiene;
ownership per the registration — TI owns the fork, TaF the currency, DU
seam-only). No private content beyond the registration's existence,
ownership, and the in-repo phrasing already public in S6 §7 is imported.
**Tags:** `reopening_packet` · `finite_witness` (execution attached; the
spec stands on its own if the owner discounts the run)

---

## Why This Packet Satisfies T587's Reopening Conditions

T587 closed Lane 1's record-capability line with an explicit stop, quoted
verbatim from its results:

> Do not continue producing T-number scaffolds from T586 alone. Reopen Lane 1
> only for a provenance-valid physical source packet, a frozen capability
> witness, or a sharper counterexample that changes the record-issuance
> contract.

T588 reopened on the third condition (the undeclared ledger question); the
composition packet reopened on the third condition one level up (the
undeclared composition question). This packet invokes the **third condition**
at the same contract layer, for the last undeclared constructor the S6
conclusion names, and argues compliance clause by clause:

1. **Not a T-number scaffold from T586 alone.** The stop targets comparators
   overlaid on the frozen T586 event system — the move T587 proved sterile.
   This packet performs no comparison on that frozen system. It operates at
   the **T583/T584 contract layer**: it adds a declared extension structure —
   a new morphism class ε and a new context constructor C ↦ C⁺ — that no gate
   T583–T588 declares. The contract currently knows three envelope-
   *preserving* equivalence classes (T584: representation, gauge, declared
   coarse-graining) and, per the composition packet + its Exit-A execution,
   one composition operation ⊗ with embeddings ι and a declared consumption
   rule ρ. **Nobody has defined admissible extension of the task family.**
   New contract structure is not another comparator; it changes what the
   contract can express.

2. **The sharper counterexample, and why it changes the record-issuance
   contract.** Fully specified in the Setup and constructible from
   already-frozen fixtures: a declared context C (T585's one-bit Landauer
   context, verbatim) and an extended context C⁺ = C + one new task type τ
   (`audit_standard_record`, consuming the existing record
   `r_erased_standard` in a new way, issuing a fresh record). Under
   extension, three measured objects all change: the **capability envelope**
   (gains exactly the τ frontier point), the **T586 record order** (gains
   the edge erase < audit), and the **S3 finality grades of old records**
   (`r_erased_standard`'s un-commit closure grows; its price rises from
   20.197730572 to 30.296595859 kBT ln 2 units and its grade for a declared
   class flips reversible → final). Yet the current contract **cannot
   express C → C⁺ as a morphism at all**: T584's classes are envelope-
   preserving, so an envelope-growing arrow is inexpressible; and T583's own
   assessor, run on the raw pair, absorbs it as
   `TASK_REDEFINITION_COMPLETION` — the same undifferentiated verdict it
   gives a mutation of an existing task and a replay of T584's rejected
   vocabulary merge. The contract is silent on which task-family changes are
   ADMISSIBLE extensions and which are new-context-entirely, and different
   answers change measured capability — the same operative sharpness as the
   composition packet's ρ₁ witness. A counterexample that forces an
   admissibility clause for task-space growth into the contract — including
   into the issuance contract's consumption rules (which records may a *new*
   task consume, and what may it issue?) — is one "that changes the
   record-issuance contract."

3. **The contract has already used the missing operation once, without a
   law.** The Exit-A composition execution licensed
   `certify_cross_record_stability` in ns2 — a task neither component
   declared — via a declared ρ edge. That is a type extension performed
   avant la lettre, legitimized locally by the composition clause but
   governed by no general law. Declaring the law that move instantiated is
   overdue contract hygiene, not novelty for its own sake.

4. **Lineage with the T588/composition precedent.** Same shape: not a
   comparator; a structural question T583–T588 leave undeclared (admissible
   task-space growth); a decisive fork with both exits consequential (the
   class is definable and forecasting separates from prediction, or the
   formal separation dies at contract level — see The Two Exits); at least
   one candidate refutable (the deflationary collapse is a registered live
   exit, and it in fact half-fires — see the execution section).

5. **The stop's procedural content is honored.** No T-number is minted; the
   spec lands in `explorations/`; the owner decides the reopening. The
   composition precedent's fallback — execute the cheap witness as an
   un-T-numbered companion and attach the run — has been followed directly,
   since the ε-witness is cheap (stdlib + in-repo models, deterministic,
   runs in seconds).

Stated honestly, what this packet does **not** invoke: no provenance-valid
physical source packet (no literature import happens here), and no frozen
capability witness beyond the already-frozen T585/T586 fixtures and S3's
declared ω-ledger rows, reused verbatim as declared fixture data.

## Construction Fork Declaration

Per the repository's construction-fork discipline, the forks are identified
and named, not defaulted:

- **Extension as declared contract structure vs physical type growth.** This
  gate uses the *declared* construction: ε is a new contract clause on
  declared contexts, in the same sense that T583's context and the
  composition packet's ⊗ are declared. Whether any lawful C → C⁺ in nature
  is genuine issuance (type creation) or disclosure of a larger fixed space
  is **not adjudicated** — that is TI's PP-3/D-FORK, routed by pointer in
  the boundary sentences.
- **Addition-only v1.** ε adds task types and only adds. Deletion, mutation
  of existing tasks, task-vocabulary merges, and re-typings are *different
  operations*, named out of scope for v1 — and rejected fail-closed when
  disguised as extension (the controls).
- **Two extension axes, not one.** S3's extension order A ⊑ A′ grows the
  *un-committing agent class* (budgets, access, menu); ε grows the *graded
  context's task space* (the world of declared tasks and records). These
  are orthogonal axes and behave oppositely on finality (see Setup); the
  fork is named to prevent conflation. S3's check (ii) monotonicity lives
  on ⊑; nothing here touches it.
- **Attainable-envelope vs exercised-task indexing** (inherited open fork):
  this gate is stated on the *attainable* envelope, T583's native object.
- **Depth-1 closure fixture.** The grade leg's un-commit closures are
  depth-1 by declared fixture construction (nothing consumes the new
  records); transitive closure growth is a richer-fixture question, named
  open.
- **Inherited un-commit construction fork.** The settlement leg uses S3's
  closure-restoring un-commit convention: ε can change an old record's grade
  only because its new record enters that restoration closure.  Under the
  coherent closure-free convention executed in the
  [fork audit](causal-past-theorem-attempt-2026-07-28.md#1-step-1--the-undeclared-construction-fork-un-commit-closure-vs-closure-free),
  the ε settlement separation collapses and forecasting equals prediction at
  this layer.  Thus the executed split-by-layer result is convention-conditional,
  not a convention-neutral result about extension or physical issuance.

## Target Claims

- T583's CapabilityContract admits a declared type-extension morphism class
  ε compatible with T584's invariance classes and the composition clause.
- Extension admissibility (conservativity, budget discipline, record-
  interface discipline, T584/⊗ commutation) is decidable and executable on
  the T585 fixture class.
- The extension-sensitivity of settlement objects (T586 order, S3 grades)
  is well-defined and lawful — the forecasting/prediction layer analysis.
- The `CAPABILITY-TO-TEMPORAL-ORDER` lane's contract hygiene, and the
  TAF3/TAF8 boundary discipline, exactly as in T583–T588.

## Setup

### The extension morphism class ε (the packet's core)

Given a T583 context C (fields as implemented in
`models/t583_capability_contract_v1.py`), an **extension datum** τ declares:
a new task identifier not in C's task family; its declared performance
point(s); an operation-menu addition; a declared consumption edge to an
existing record with a declared unique producer (T586 discipline); and, for
any record τ issues, a fresh record identifier plus declared stabilization
data (ω) if the context is graded. Then:

> **ε_τ : C → C⁺**, where C⁺ = C with task_family ∪ {τ} and menu ∪ {op_τ},
> and **every other declared field identical** — budget, horizon, access
> profile, source theory, region, quotients. ε adds task types and only adds
> (no deletion, no mutation — different operations, out of scope v1);
> existing structure maps identically (ε is the inclusion). Admissible iff
> conditions (i)–(iv) below hold.

**The admissibility conditions, each declared and tested:**

- **(i) Conservativity on the old envelope — the anti-revisionism law.**
  Env(C⁺) restricted to C's task family = Env(C), bitwise after
  canonicalization. An extension may not retroactively change what the old
  tasks could do. This is the law that separates lawful extension from
  mutation: a "new task" bundled with a cheapened or altered existing task
  fails (i) and is rejected, not absorbed.
- **(ii) Budget discipline.** C⁺ carries the **same declared budget**; new
  tasks draw on it. Silent budget growth is rejected
  (`SILENT_BUDGET_GROWTH`), and a pure budget change is what T583 already
  classifies it as — `RESOURCE_BUDGET_COMPLETION` — never extension. Without
  (ii), extension smuggles composition: adding a task *plus* resources is
  ⊗ with an undeclared second component, not ε.
- **(iii) Record-interface discipline.** τ may consume only records with
  declared unique attainable producers, per the issuance contract's
  consumption rules — the composition packet's namespace/ρ machinery reused
  intra-context. Issuance stays with the producer: τ may not re-issue an
  existing record id (`REISSUE_EXISTING_RECORD`), and consumption of an
  undeclared record fails closed (`UNKNOWN_RECORD_CONSUMED`). New records τ
  issues get fresh ids and enter the record graph downstream.
- **(iv) Interaction with T584's classes and with ⊗.** ε commutes with
  representation, gauge, and declared coarse-graining — the extension of a
  relabeled context is the relabeling of the extended context — and with
  the composition clause: extending one component then composing equals
  composing then extending in that namespace, with the other namespace's
  envelope untouched (conservativity on composites).

**Why ε is a genuinely new kind of arrow.** T584's three classes are
envelope-*preserving* equivalences; the composition packet's ι embeddings
never lose capability and are exact on independent composites. ε is the
first declared arrow that is deliberately envelope-*growing* while
envelope-*conservative* on the old family — a directed, non-invertible
morphism class. The current contract cannot express it: its assessor has
exactly one verdict for any task-family difference
(`TASK_REDEFINITION_COMPLETION`), which it assigns identically to lawful
extension, mutation, and merge. The gate replaces that single absorbing
verdict with one admissible class and typed rejections.

**Why extension is not T584's rejected merge.** T584's counterexample
merged *existing* certification and recovery vocabulary — identifying two
declared task ids — and was rejected because the identification changes the
native envelope while claiming to be a physical-equivalence morphism. ε is
disjoint from that move on every axis: it adds a *fresh* id (a collision
with an existing id is rejected, `TASK_ID_COLLISION_NOT_EXTENSION`); it
identifies nothing (an id-identification presents to the admissibility law
as deletion-plus-redefinition and is rejected,
`VOCABULARY_MERGE_OR_DELETION_NOT_EXTENSION`); it claims no equivalence
(ε is directed and envelope-growing by design); and it is conservative on
the old family, which the merge demonstrably is not (the merged envelope
differs from Env(C) — T584's own mechanism, re-exhibited in the run). The
merge stays rejected; extension is lawful; the gate distinguishes them
executably.

### Forecasting-capacity, the new object

For a declared family E of admissible extensions of C:

- **The attainability layer.** The forecasting envelope
  FEnv(C, E) := ⋂_{ε ∈ E} Env(ε(C)) restricted to C's tasks — the stable
  core of what remains attainable across all extensions in E. **Under
  admissibility this equals Env(C) identically**: conservativity (i) makes
  every restriction exact, and T583's task-gated native order (points
  compare only within a task id) means new tasks can never dominate old
  points. So at the attainable-envelope layer, *forecasting collapses to
  prediction by law*. This is a small theorem with two load-bearing
  declared premises — the anti-revisionism law and the task-gated order —
  and it is stated as such, not discovered: a future declared cross-task
  comparison would reopen this layer.
- **The settlement layer — the extension-sensitive boundary.** The objects
  ε lawfully changes: the new-task boundary Env(ε(C)) \ Env(C); the T586
  record order's new edges; and the **S3 finality grades of old records**.
  The last is the sharp one: un-commit(r) is priced over r's record-graph
  closure (S3 §1.2), and ε lawfully grows the graph, so W_rev(r) of an
  *old* record rises and FINAL(A, r) can flip reversible → final under
  extension — with zero envelope revision. No conservativity violation
  occurs: anti-revisionism freezes what the old tasks could do; it does not
  freeze functionals that quote the record graph. This is S3's own check
  (iv) ("adding a downstream consumer only raises ancestors' grades") made
  class-indexed: settlement prices are **monotone along ε** (they can only
  rise), the dual direction to S3 check (ii)'s monotonicity along ⊑
  (extending the *agent* only evaporates finality; extending the *world*
  only accretes it). At fixture level this is the two-stroke ratchet's
  formal trace: the capability stroke and the type stroke move finality in
  opposite directions.  This sentence is conditional on S3's
  closure-restoring un-commit convention; the closure-free fork removes the
  settlement movement while leaving the fixed-task attainability result
  unchanged.
- **Forecasting-robust vs prediction-optimal — the pre-registered
  question.** Is there a nontrivial separation on the frozen fixtures
  between prediction-side objects (fixed-C envelope and grade profile) and
  forecasting-side objects (their stability across E)? Registered
  could-fail commitment, per Q-0066's anti-accommodation rail: **if for
  every declared E all settlement objects are E-stable — or if ε cannot be
  defined compatibly with T584/conservativity at all — then forecasting
  collapses to prediction on this fixture class entirely, and the ratchet
  thesis's formal separation dies at contract level.** That deflationary
  exit is legitimate and is registered as evidence *against* Q-0066's
  thesis, not as a fixable inconvenience.

**Definition (fixture-level).** *Forecasting-capacity of C relative to a
declared admissible family E* = the pair (stable core, extension-sensitive
boundary): what remains attainable and settlement-stable across all of E,
together with the typed inventory of what E can lawfully move. A record
whose grade is invariant across E is forecasting-robust for the declared
class; a record whose grade some ε ∈ E flips is extension-exposed. No
scalar is introduced anywhere.

### The executable witness class (executed; run attached below)

Fixture: T585's declared context and biased one-bit cell (p_one = 0.10,
reset cost 0.468995594), verbatim; budget energy 0.75, time 5.0, error
0.01, horizon `single_reset_cycle`.

- **ε₁:** τ = `audit_standard_record`, consuming `r_erased_standard`
  (unique producer: the erase event), issuing fresh `r_audit_certificate`,
  declared ω = 7.0, point (success 0.99, energy 0.10, time 0.5, comm 0.2,
  memory 0.1, error 0.003) — feasible inside the *unchanged* budget.
- **ε₂:** τ = `audit_light_standard_record`, same consumption, fresh
  issue, declared ω = 1.0 — the family E = {ε₁, ε₂}.
- **Grade leg (mini-S3):** S3's declared ledger rows reused verbatim
  (erase ω = 9.0, certify ω = 5.0, prepare ω = 3.0; floors 0.0 / 0.0 /
  0.468995594), so W_rev(`r_erased_standard`) in C is S3's own table value
  20.197730572 and W_rev(`r_biased_reference`) is S3's 4.797080717.
  Declared class A_mid: energy 25.0. Predicted: ε₁ raises the standard
  record's price to (9+5+7)/ln 2 = 30.296595859 → grade flips
  reversible → final; ε₂ raises it only to 21.640425613 → no flip
  (sensitivity is ε-dependent, not automatic); the biased reference's
  closure is untouched by E → E-stable.
- **Order leg:** the record order gains exactly erase < audit; its
  restriction to old events equals the C order.
- **Commutation legs:** gauge swap (p → 1−p), joule representation, and
  declared coarse-graining each commute with ε at envelope level; the
  ⊕-composition leg checks extend-then-compose = compose-then-extend with
  the other namespace untouched.

## Success Criteria

- ε is defined on the T585 fixture class with every admissibility condition
  enforced fail-closed and every rejection typed.
- **Conservativity holds on the lawful witness:** Env(C⁺) restricted to old
  tasks equals Env(C) bitwise, for every member of E; the envelope grows by
  exactly the declared τ point.
- The raw (C, C⁺) pair is absorbed by the *current* contract as
  `TASK_REDEFINITION_COMPLETION` — the executed exhibit of the gap this
  gate closes.
- All three T584 commutation legs pass, and the ⊕-composition leg passes
  with conservativity on composites (the other namespace's envelope
  untouched).
- The record order is conservative on old events and strictly grows.
- The grade leg separates: an old record's grade flips under some ε ∈ E
  with the old envelope untouched; another record is E-stable; the
  agent-class axis (S3 check (ii) direction) is never violated.
- **Controls that must fail (teeth) — at least three, all executed:**
  - *mutation disguised as extension:* a new task bundled with a cheapened
    existing-task point → rejected `EXISTING_TASK_MUTATION` by the
    conservativity law;
  - *budget-growing extension:* a new task whose point exceeds the declared
    budget, "fixed" by raising the budget → rejected
    `SILENT_BUDGET_GROWTH`; and the pure budget change, assessed by T583
    itself, reclassified `RESOURCE_BUDGET_COMPLETION` — never extension;
  - *vocabulary-merge replay of T584's rejected counterexample:* the
    certification-vocabulary identification presented as extension →
    rejected `VOCABULARY_MERGE_OR_DELETION_NOT_EXTENSION` (and its
    collision face `TASK_ID_COLLISION_NOT_EXTENSION`), with the
    envelope-change mechanism of T584 re-exhibited;
  - plus record-interface teeth: `UNKNOWN_RECORD_CONSUMED` and
    `REISSUE_EXISTING_RECORD` fail closed.
- **Firebreak inherited from T587's boundary typing:** no capability delta,
  grade flip, or new record-order edge is counted as time, temporal
  issuance, or an arrow by itself.

## Failure Criteria

- ε cannot satisfy (i)–(iv) jointly on the fixture class (Exit B fires).
- Conservativity fails on a lawful witness, or holds only by exempting some
  declared old task.
- Any must-fail control passes (the gate has no teeth).
- A grade flip is booked as an envelope revision, or any settlement change
  is treated as a temporal, issuance, or arrow quantity.
- A scalarization is defaulted anywhere (T583's failure criterion binds;
  forecasting-capacity is a pair of typed sets, not a score).
- The gate is used to move claims, canon, Lane posture, public posture, or
  any cross-repo result.

## The Two Exits (stated in advance)

- **Exit A — the extension class is definable and forecasting separates
  from prediction on the fixtures.** The disclosure/issuance fork's
  issuance stroke gains its first executable instrument:
  **forecasting-capacity = capability robust under declared type
  extension** becomes a contract-native, executable object, and the
  two-stroke ratchet toy — the nucleation toy of the Q-0066 seed's next
  arm (S6 §7 item 1's second object, with commit(A, r) as the
  settlement-substrate grade) — becomes buildable: this gate supplies its
  type-space-growth stroke as a lawful operation. The boost-equivariance
  gate also gains a third instance of the new-morphism-class pattern
  (⊗, isometries-proposed, ε) to pattern-match against.
- **Exit B — the class cannot be defined compatibly with
  T584/conservativity, or forecasting collapses to prediction on every
  declared E.** The formal separation dies at contract level, and Q-0066's
  thesis loses its cheapest support — registered as such, per the
  registration's own anti-accommodation rail. The death would be recorded
  in the Q-0066 lineage and the ratchet-toy arm would not open on this
  route.
- **Executed outcome (run attached below): Exit A, with an honest
  narrowing — SPLIT BY LAYER.** The deflationary exit *half-fires, by
  law*: at the attainability layer prediction and forecasting provably
  coincide (conservativity + task-gated order force it), and the
  separation lives entirely at the settlement layer (grades and order).
  Q-0066's separation gets support of a specific, carried shape:
  forecasting ≠ prediction *because settlement prices are record-graph
  functionals and extension lawfully grows the graph* — not because
  attainability changes.

## Boundary Sentences (mandatory)

1. **The fork's metaphysics stays TI's.** Whether a lawful C → C⁺ is
   genuine issuance (type creation) or disclosure of a larger fixed space
   is PP-3/D-FORK (TI-C019, E026), owned by temporal-issuance and routed
   there by T588's fork handoff — pointer only, not rebuilt. This packet
   defines contract machinery; a settlement-layer separation is **not** an
   issuance verdict, and a well-defined ε does not assert that nature
   performs ε.
2. **DU seam-only; the DU STOP respected.** The record interface remains
   *supplied*, per dynamic-unity's banked no-go (HC-DU-063) and their
   autonomous-finality `NO_READY_MECHANISM` result (HC-DU-061), cited by
   pointer at their pins as in S2; nothing here derives record-ness, and
   no split-dependent quantity is passed off as representation-independent
   (the grade and envelope legs are checked on T584 orbits). Nothing here
   asserts or tests whether any foliation, update ordering, or beable
   exists.
3. **Covariant forward-compatibility — condition (v), named not tested.**
   The goal2 charter verdict §2b registers the covariant-formulability
   question, and the covariant note's alignment law (§2d) and proposed
   isometry class (§2e; the boost-equivariance gate, S6 §7 item 4) bind
   any covariant re-declaration. Extension must not silently break them:
   at covariant scope an admissible τ must be event-locally statable with
   records consumed only from the causal past J⁻(y), and ε must commute
   with the isometry class when that gate opens. A flat-contract-admissible
   extension that consumes outside the causal past is *not*
   covariant-scope admissible. Condition (v) is a declared burden on the
   boost-equivariance gate's opening, untested here.
4. The DU-side and TI-side ownership of the Q-0066 registration binds:
   TI owns the fork, TaF the currency (this packet), DU seam-only.

## Known Physics Constraints

None claimed. The only physical source input remains T585's bounded
Landauer-style erasure cost, re-executed as source-owned input at run time.
S3's ω rows enter as *declared fixture data* (their status in S3 —
declared, not derived — is inherited unchanged). No rate constant is
established or used; no collapse model is endorsed; nothing in the gate
derives time, temporal order, issuance, or a thermodynamic arrow; the
grade flip lives in S3's own honest category ("capability/topology
residue," not thermodynamic-arrow evidence).

## What This Does Not Claim

- **No T-number is minted and no reopening is performed.** The owner mints
  the number, decides adoption, and decides whether the attached run counts
  as the reopening's executed witness or merely as design verification.
- **No issuance verdict and no ratchet-thesis confirmation.** Exit A is
  fixture-level and layer-specific; the attainability-layer collapse is
  real, forced by declared law, and carried undiluted. Support for Q-0066
  is exactly as narrow as the SPLIT BY LAYER verdict states.
- **No claim movement.** No claim-ledger, Canon Index, hypothesis, Lane, or
  public-posture change; T583–T588, the composition artifacts, and the S3
  verdicts are untouched.
- **Capability remains T583's operational, executable-task measure and
  nothing else** — not consciousness, not cognition, not awareness, not
  agency. A grade flip is a repriced feasibility fact about a declared
  class, not a mind-adjacent quantity.
- **The witness is an existence witness, not a genericity claim.** The
  grade flip is realizable under the admissibility laws (that is what the
  separation question asks); it is engineered by declared ω and class
  budget, and nothing says extensions generically flip grades — ε₂'s
  non-flip is exhibited on purpose.
- **No bearing on the foliation branch.** ε extends declared task
  families, not spacetime slicings.

## Contribution Needed

Owner decision on this reopening packet. If accepted: mint the T-number,
move the spec into `tests/` under house numbering with a focused unit test
over `models/type_extension_witness_probe.py`, and decide whether the
settlement-layer separation warrants opening the ratchet-toy arm (S6 §7
item 1's second object). If the owner discounts the attached run, the spec
stands alone as the packet and the run reverts to design verification.

---

## Execution attached (2026-07-28)

The composition precedent's fallback path has been followed: the ε-witness
ran as an un-T-numbered exploration companion with the full check slate —
admissibility on both members of E, conservativity, the raw-pair absorption
exhibit, three T584 commutation legs plus the ⊕-composition leg, the
record-order leg, the five-price grade leg, and all seven fail-closed
controls — deterministic, exit 0, output byte-identical across two
consecutive runs.

- Model: [../models/type_extension_witness_probe.py](../models/type_extension_witness_probe.py)
  (stdlib + in-repo models only; run with
  `python3 -B -m models.type_extension_witness_probe` from the repository
  root). 271 lines — over the pre-declared ~150-line cheapness target; the
  ε-core (constructor, admissibility law, conservativity and commutation
  legs) is within it, and the overage is the mandated control slate and
  grade leg. Reported, not smoothed.
- Verdict string emitted:
  `TYPE_EXTENSION_WITNESS_EXECUTED_EXIT_A_EXTENSION_CLASS_DEFINABLE_SPLIT_BY_LAYER_REVIEW_ONLY`.

### Pre-registered predictions vs outcomes

| # | prediction (registered above) | outcome | status |
| --- | --- | --- | --- |
| 1 | ε₁, ε₂ admissible; conservativity bitwise; envelope grows by exactly τ's point | both `ADMISSIBLE`; Env(C⁺)\|old = Env(C) bitwise for both; frontier 2 → 3 points, the new point is τ's | **CONFIRMED** |
| 2 | the current contract absorbs the raw pair as completion | `assess_pair(C, C⁺)` → relation `SUBSET`, verdict `TASK_REDEFINITION_COMPLETION` | **CONFIRMED** (the gap, exhibited) |
| 3 | ε commutes with gauge, representation, coarse-graining, and ⊕ (conservativity on composites) | 4/4 legs pass; other namespace untouched | **CONFIRMED** |
| 4 | record order conservative on old events, strictly grows by erase < audit | restriction equals the C order; exactly one new edge | **CONFIRMED** |
| 5 | grade flip under ε₁ (20.197730572 → 30.296595859 > 25.0), no flip under ε₂ (→ 21.640425613), `r_biased_reference` E-stable at 4.797080717 | all five prices land exactly as computed; flip and non-flip as predicted; class-axis monotonicity never violated | **CONFIRMED** |
| 6 | all controls fail closed with typed reasons | 7/7: `EXISTING_TASK_MUTATION`, `SILENT_BUDGET_GROWTH`, `RESOURCE_BUDGET_COMPLETION` (reclassification), `VOCABULARY_MERGE_OR_DELETION_NOT_EXTENSION` + envelope-change exhibit, `UNKNOWN_RECORD_CONSUMED`, `REISSUE_EXISTING_RECORD`, `TASK_ID_COLLISION_NOT_EXTENSION` | **CONFIRMED** |

### The witness table (the contract question, made concrete)

| candidate task-family change | current contract's verdict | this gate's verdict |
| --- | --- | --- |
| ε₁: fresh τ, same budget, declared consumption, conservative | `TASK_REDEFINITION_COMPLETION` | `ADMISSIBLE` |
| new task + cheapened existing task | `TASK_REDEFINITION_COMPLETION` | `EXISTING_TASK_MUTATION` |
| new task + grown budget | `TASK_REDEFINITION_COMPLETION` | `SILENT_BUDGET_GROWTH` |
| T584's vocabulary merge, replayed | `TASK_REDEFINITION_COMPLETION` | `VOCABULARY_MERGE_OR_DELETION_NOT_EXTENSION` |

One absorbing verdict versus one admissible class plus typed rejections —
the executed form of the sharper-counterexample claim. (Row 1's absorption
is executed by the run; rows 2–4's current-contract column follows from the
assessor's declared precedence — `task_family` is classified first — not
from separate executions. This gate's column is executed for all four.)

### Honest notes on strength of evidence

- **The attainability-layer collapse is by construction, and is the
  finding.** Conservativity plus the task-gated native order *force*
  prediction ≡ forecasting at the envelope layer; the run certifies
  coherence (an ε satisfying all four conditions exists on this fixture
  class), and the genuinely falsifiable legs were the commutation laws,
  the controls, and the grade leg's five prices.
- **Shallow embedding.** Commutation legs are executed at envelope level
  over morphed fixtures, not over an abstract morphism category; the
  ⊕-leg uses the composition clause's namespaced envelope form (licensed
  by the Exit-A execution's Env(⊗) = ⊕ on independent composites), not a
  re-run of ⊗ itself. Same caveat class as the composition run.
- **Depth-1 closures, declared.** Nothing consumes the new records, so
  un-commit closures grow by exactly one record; transitive growth (an
  extension whose new record is itself consumed downstream) is unexercised.
- **Fixture-class scope.** One cell, one state, two extensions, one
  declared class pair. All counts are fixture-specific; only the structure
  is claimed to be exercised.

## Provenance

- Writer lock checked before writing:
  `git rev-parse --git-path capacityos-writer.lock` →
  `.git/capacityos-writer.lock`, not present. Repository main at read and
  write time: `c2e6604`, working tree otherwise clean. This arm performs
  file writes only — no commit, no push; its writes are this packet and
  `models/type_extension_witness_probe.py`.
- Read in full before drafting: the composition packet and its execution
  note, T583–T588, S3 (grades and check slate), the covariant note §2,
  goal2 charter verdict §2b, S6 §7 and its Q-0066 registration provenance,
  the record-layer naturality spec's routing, and the tri-repo division of
  labor.
- Probe executed 2026-07-28 from the repository root with bytecode writes
  suppressed (`python3 -B`); exit 0; all 16 checks pass, all 7 controls
  fail closed; output verified byte-identical across two consecutive runs
  (no randomness, no wall-clock values).
- **Q-0066:** cited by pointer to the private thinking-wiki registration
  only; no private content beyond the registration's existence, ownership
  line, and the S6-public phrasing is imported.
- No fetches this run; no external physics enters beyond T585's source law
  and S3's declared rows, both in-repo.
