# Landauer-Bounded Record Rate: Null Refinement of the Record Order, and the Matter-vs-Capability-Indexed Rate Discriminator (Spec)

**Status:** Part 1 executed — null refinement, confirming the pre-registered
prediction (the expected successful outcome). Part 2 is a paper spec only —
no fixture, no run, no new T-number (T587's stop on new T-scaffolds from T586
alone is respected; this note is an exploration companion)
**Date:** 2026-07-27
**Executes:** the queued Swing 6B spec, routed 2026-07-27 from Joe direct chat
(system-runtime mailbox,
`mailboxes/time-as-finality/20260727-landauer-derived-record-rate-in-t585.md`),
whose pre-registered prediction is restated verbatim below so the
pre-registration is on record in this repository
**Builds on:** [T583](../tests/T583-capability-contract-v1.md) and
[T584](../tests/T584-capability-invariance-morphism-gate.md) (the capability
contract and its invariance quotient), [T585](../tests/T585-landauer-physical-capability-gate.md)
(the Landauer fixture whose declared budgets supply the rate),
[T586](../tests/T586-record-capability-order-gate.md) (the record-capability
order under test), [T587](../tests/T587-t586-causal-collapse-boundary-attack.md)
(boundary typing and the stop condition this note operates under)
**Model:** [../models/landauer_rate_t585_overlay.py](../models/landauer_rate_t585_overlay.py)
(exploration companion, deliberately un-T-numbered; re-executes T585 and T586
as source-owned inputs rather than consuming cached results; exit 0, all 12
checks pass)
**Tags:** `finite_witness` (Part 1) · `spec_only` (Part 2)

---

## Verdict

- **Part 1 — NULL, as pre-registered.** The Landauer-bounded record rate,
  derived strictly as a ratio of T585's *declared* work and time budgets,
  neither refines nor changes T586's record-capability partial order. The
  closure after rate annotation is bitwise the baseline closure; zero
  record-backed edges are added; the order's axioms are untouched. Per the
  charter ("a precise failure is a successful outcome") and the swing spec,
  this null is the expected successful outcome, and it partially answers
  Goal 3 for the rate branch: **whatever an observer-indexed universal rate
  buys, it is not temporal order.**
- **Part 2 — SPEC ONLY.** Matter-indexed and capability-indexed universal
  rates predict different scalings of the spontaneous-heating/radiation
  signature, so a discriminator exists on paper. Its load-bearing requirement
  is that the T583 capability measure admit an extensive ("capability
  density") form — and the preliminary assessment against T583/T584's actual
  properties is that **naive extensivity is blocked**; survival requires a
  new composition/extensivity gate that is named here but not opened.

## Part 1 — the derivation, done compliantly

### The rate is a ratio of given budgets, not a derived temporal quantity

T585's failure criteria reject any use of the fixture "to claim time,
temporal order, issuance, a new source law, or a claim-ledger movement."
This swing does not need to trip that gate, because T585's fixed context
already *declares* both budgets as inputs: a work budget of 0.75 (normalized
`kBT ln 2` units) and a time budget of 5.0 (declared units). The source law
gives the per-record reset cost as the binary entropy of the memory state in
the same normalized units. So:

- **records affordable** = declared work budget ÷ per-record reset cost;
- **bounded record rate** = records affordable ÷ declared time budget.

Both denominators are quantities the fixture was already given. No time and
no temporal order are derived from the fixture anywhere in this swing; the
overlay script asserts this in its output (`compliance_statement`) and reads
both budgets from T585's declared context object, re-executed at run time.

Construction fork, named per the repo discipline: the compliant construction
reads the rate as *ratio of declared budgets*; the rejected construction
would read it as *derived temporal structure*. The fork is settled by T585's
own failure criteria, not by preference.

For scale, outside the fixture's normalized units: `kB·T·ln 2` ≈ 2.87 × 10⁻²¹ J
at 300 K (the run computes 2.870979 × 10⁻²¹ J), so one watt supports
~3.5 × 10²⁰ record resets per second (run value 3.4831 × 10²⁰). The bound is
astronomically loose for anything that would count as an observer.

### Fixture numbers

| event (T586) | reset-cost basis (T585 state) | cost (`kBT ln 2` units) | records affordable | bounded rate (per declared time unit) |
| --- | --- | ---: | ---: | ---: |
| `seed_known_record` | `known_zero_record` | 0.0 | unbounded | unbounded |
| `copy_known_record` | `known_zero_record` | 0.0 | unbounded | unbounded |
| `erase_standard_record` | `known_zero_record` | 0.0 | unbounded | unbounded |
| `certify_erased_record` | `known_zero_record` | 0.0 | unbounded | unbounded |
| `prepare_biased_reference` | `biased_record` | 0.468995594 | 1.599162 | 0.319832 |

The state basis is a declared annotation mirroring T586's own event
construction (main chain on the known-zero lineage; the reference event is
the biased state). A consistency check confirms the ratio reading adds no
feasibility content: `floor(records_affordable) ≥ 1` exactly where T585's
audited envelope already makes erasure feasible (known/biased yes,
max-entropy no under the 0.75 budget).

### The refinement test

Baseline: T586 re-executed; its closure has six pairs (seed → copy → erase →
certify, transitively closed) with `prepare_biased_reference` incomparable to
the main chain. Four channels by which rate/capacity data could conceivably
order events were made executable:

| channel | closure pairs reproduced | closure pairs contradicted | non-closure pairs asserted | record-backed new edges | classification |
| --- | ---: | ---: | ---: | ---: | --- |
| rate as scalar, declared basis | 0 / 6 | 0 | 4 | 0 | `RATE_SCALAR_OVERREAD` |
| rate as scalar, uniform (max-entropy) stress basis | 0 / 6 | 0 | 0 | 0 | `RATE_SCALAR_OVERREAD` |
| rate-scaled clock labels (`t_i = clock_i / r`) | 4 / 6 | 2 | 6 | 0 | `CLOCK_PARAMETERIZED_OVERREAD` |
| rate-feasibility pruning | — | — | 0 removed/added | 0 | `NO_CHANGE_BOUND_DOES_NOT_BIND` |

Findings, in order of force:

1. **The scalar channels carry zero ordering information about the record
   chain.** Under the declared basis the entire ordered main chain shares one
   rate value (the known-zero lineage has zero reset cost), so the scalar
   comparison orders *nothing inside the chain* and relates only the pairs
   T586 proves incomparable — it inverts the incomparability structure
   rather than refining the order. Under the adversarial uniform basis the
   rate is constant everywhere and induces the empty order. Both extremes
   reproduce 0 of 6 record-order pairs.
2. **The clock channel is provably redundant.** Dividing clock labels by any
   finite positive rate is strictly monotone, so every rate-scaled clock
   order is *identical* to the clock-label order for every tested rate — and
   T586's clock-label control already showed that order is not the record
   order (here it also reverses two of its six pairs: clock puts copy before
   seed and certify before erase). Permuting presentation clock labels flips
   the rate-scaled order while the record closure is unchanged — re-verified
   in this run with rate annotations attached. A rate adds exactly zero
   ordering information beyond clock labels, and clock labels were already
   excluded. (With the declared main-chain rate, which is unbounded, the
   rate-time labels all degenerate to zero and induce no order at all.)
3. **The bound never binds.** Every per-event reset cost and the fixture
   total (0.469 of 0.75) sit inside the declared work budget, so feasibility
   pruning removes no event and no edge — consistent with the SI-scale
   looseness (~3.5 × 10²⁰ resets/s/W). An annotation aggressive enough to
   make events infeasible would be a changed budget/accounting, which T585
   itself classifies as a resource/access *completion*, not fixture truth.
4. **No rate-derived record edge is possible by type.** T586 admits an order
   edge only through a record whose unique producer is another event. Rate
   annotations issue no records; converting a per-unit-time quantity into a
   record issuance is precisely the overread T585's failure criteria and
   T587's boundary typing (capability deltas by themselves are not
   record-order edges) are written to catch.

**Result:** closure after = closure before (bitwise); no new relations
derivable; no existing relation changed; antisymmetry and transitivity
untouched (the spec's contradiction outcome did not trigger). Of the spec's
three outcomes — refine / change / leave unchanged — the answer is **leave
unchanged**.

### The pre-registered prediction, confirmed not adjusted

Restated verbatim from the swing spec, which was on record before this run:

> **The rate will not refine the order.** [...] T586 already established that
> **arbitrary clock-label permutation does not reproduce the
> record-capability order.** A rate is a clock-parameterized quantity. If the
> order is provably not clock-derived, a per-unit-time bound is the wrong
> type of object to refine it. Second reason: the Landauer bound is
> astronomically loose for any system that would count as an observer.

Both registered reasons are the ones the run exhibits: the clock channel
reduced exactly to the already-excluded clock order, and the bound never
bound. Prediction status: **CONFIRMED**. Had the result been positive, the
registered posture was suspicion that the time budget had been smuggled in as
an ordering parameter; that suspicion was not needed.

## Part 2 — discriminator spec: matter-indexed vs capability-indexed rates

*Spec only. No fixture is built, no experiment is proposed for execution, no
collapse model is endorsed, and no T-number is assigned.*

### The two indexings and the scaling signature

The universal-rate branch of the preferred-frame family (a rate, not a
foliation) needs an index: what does the rate couple to?

- **Matter-indexed (GRW/CSL/Diósi–Penrose class).** The spontaneous-process
  rate is per constituent: an N-particle system runs at ~N × the per-particle
  rate (mass-proportional amplification; GRW's historical per-particle rate
  is ~10⁻¹⁶ s⁻¹ — memory-cited, see Literature status). The collapse noise
  imparts momentum diffusion, predicting *spontaneous heating* of bulk matter
  and, for charged constituents, *spontaneous X-ray emission* — independent
  of how the matter is organized. This is exactly what underground
  bulk-matter searches bound: Donadi et al., Nat. Phys. 17, 74 (2021) used a
  radio-pure germanium detector at Gran Sasso to search for the predicted
  spontaneous X-rays, excluding the parameter-free Diósi–Penrose model and
  bounding its smearing length at the sub-angstrom scale; CSL heating and
  radiation bounds constrain the (rate, correlation-length) plane similarly.
- **Capability-indexed (the sharpening this program can state natively).**
  The rate couples to the T583 capability measure of a declared
  region-observer-task context — the task-indexed Pareto envelope of
  attainable performance-cost-error points — not to particle number. An
  undifferentiated crystal has enormous N but a minimal record-forming task
  envelope: **low capability per unit mass**, so it heats *less* than the
  matter-indexed prediction at equal mass. An organized record-forming
  system (an operating memory array; T585 is the one-cell instance) has a
  larger envelope at the same mass and heats *more* than an equal-mass
  crystal.

The discriminating signature is therefore **differential**: at matched mass,
composition, and temperature, matter-indexing predicts identical spontaneous
signal from a monolithic crystal and from the same matter fabricated into an
operating record-forming array; capability-indexing predicts an excess
scaling with the capability difference. Construction fork, named and left
open: does the rate read the *attainable* envelope (T583's object — in which
case powering the work store up and down modulates capability through the
declared budget, T585's own budget axis, without touching the matter) or the
*exercised* tasks (execution-indexed — in which case idle/operate modulation
does the work)? Either reading yields a modulation experiment; they differ
in what the idle condition measures. Any real design must also separate the
collapse channel from ordinary dissipation (an operating array emits vastly
more mundane heat than any collapse signal; the spectrum-resolved X-ray
channel, not bolometry, is the plausible handle) — noted as a design burden,
not solved here.

### (i) How a Ge-detector bound transfers

Under matter-indexing, the null result bounds the per-particle rate directly
(given the model's kernel): signal ∝ λ_matter × N × (channel factor), N and
the channel factor supplied by the model, so λ_matter is capped.

Under capability-indexing, the same null bounds only the **product**

> λ_cap × Cap(Ge crystal; declared context)

where `Cap` must be evaluated on a T583-valid declared context for the
crystal (region = the crystal; observer/access = the experiment's readout;
task family = whatever record-forming tasks the crystal genuinely supports;
budget = ambient conditions), invariantly under T584's quotient. The
coupling and the crystal's capability enter only as a product, so:

- the underground bound **cannot cap λ_cap alone** without an independent,
  contract-valid evaluation of the crystal's capability; and
- because capability-indexing assigns the crystal a small `Cap`, it predicts
  a *smaller* signal in precisely the organization-poor systems the searches
  use — the null is automatically absorbed at the cost of pushing the
  entire evidential burden onto the differential experiment above.

Stated as a constraint honestly: bulk-matter nulls alone cannot falsify the
capability-indexed sub-variant; only the differential (or modulated)
comparison can. A sub-variant that also declined the differential test would
be unfalsifiable by this class of experiment and would exit the physically
discriminable classification of Goal 1.

### (ii) The extensivity requirement — the pre-registered kill

For a rate to integrate over a detector — for "heating per gram" or "rate
per region" to mean anything — the coupling needs a **capability density**.
That requires, in order:

1. **Canonical contextualization.** T583 capability is indexed to a
   *declared* context (observer, access, task family, budget). A physical
   rate cannot depend on our declaration; the sub-variant must supply a
   canonical context assignment (e.g., a maximal or intrinsic envelope over
   admissible contexts) — currently undeclared anywhere in T583–T586.
2. **T584-invariant scalarization.** The native object is a task-indexed
   Pareto frontier with `native_structure = task_indexed_pareto_preorder`.
   T583 lists "capability defaults to one scalar" as a *failure criterion*,
   and its negative nonfactorization control certifies genuinely
   INCOMPARABLE envelopes — the native order is partial on purpose. A
   density needs a scalar, so a scalarization must be *explicitly declared*
   (never defaulted), and must be constant on T584's
   representation/gauge/coarse-graining orbits. The invariance half is
   plausible (the envelope itself is the invariant); the totalization half
   forces ties the native order refuses to break.
3. **Additivity under declared composition — the kill condition.**
   **Pre-registered:** if the T583 measure cannot be made extensive —
   additive over subsystems under a declared composition,
   `s(A ⊕ B) = s(A) + s(B)` — then no rate density exists and the
   capability-indexed sub-variant **dies at spec stage**.

Assessment against T583/T584's actual properties:

- Neither T583 nor T584 declares a composition operation. T584's admissible
  morphism classes are representation, gauge, and irrelevant
  coarse-graining — nothing composes two contexts. Additivity is currently
  **not even statable** in the contract; stating it requires a new declared
  morphism class.
- The program's own central mechanism cuts against additivity. T586's whole
  content is that an executable task of one event can require a record whose
  unique producer is another. Under any composition permitting
  cross-subsystem record dependence, the composite has executable tasks
  neither part has alone — capability is generically **superadditive**, not
  additive. Exact additivity can hold at best on record-noninteracting
  composition classes, and organized record-formers are precisely
  record-coupled internally: the density would fail exactly where the
  discriminator needs it.

**Preliminary verdict: naive extensivity is BLOCKED** (non-scalar native
object with declared anti-scalarization; no composition operation in the
contract; superadditivity forced by the record-dependence mechanism). This
is not yet a fired kill: a declared composition class with a declared
scalarization — for instance, an additive lower bound or a subadditive
envelope with controlled defect — has not been constructed *or* excluded.
Deciding it **needs a new gate** (a composition/extensivity gate on the
T583 contract). That gate is *named here, not opened*: per T587's next_work,
new T-number scaffolds from T586 alone are stopped, and opening it requires
a T587-compliant reopening — a provenance-valid physical source packet
(e.g., a properly imported underground-bound dataset under the literature
discipline) or a composition counterexample sharp enough to change the
record-issuance contract.

### (iii) Guard — what "capability" means here, verbatim level

**Capability in this spec is the operational, executable-task measure of
T583 and nothing else:** the task-indexed Pareto frontier of attainable
performance-cost-error points for a declared region, observer/access
profile, task family, operation menu, and budget. It is a third-person,
contract-declared, physically instantiable quantity (T585 instantiates it in
a one-bit memory with a thermal bath).

**Capability here is explicitly NOT consciousness, NOT cognition, NOT
awareness, NOT experience, NOT agency, and not any mind-adjacent notion.**
A thermostat-grade controller with a declared task family has capability; a
rock under a record-forming task family has essentially none; no term in
the measure refers to minds. **Any reading of this spec as a
consciousness-causes-collapse proposal is a misreading and is disclaimed.**
The discriminator is between two fully physical indexings of a rate —
particle number versus operational task capability — and would remain
exactly as stated in a universe containing no minds at all.

## Kill status — both kills

| kill | registered where | status |
| --- | --- | --- |
| "The rate will not refine the record order" (kills the rate-buys-temporal-order reading) | swing spec, before the run | **CONFIRMED / route dead** — executable null, exit 0; the rate branch contributes nothing to TaF's record order; positive and contradiction outcomes not triggered |
| Extensivity kill: no extensive capability measure ⇒ no rate density ⇒ sub-variant dies at spec stage | this note, Part 2 (ii), before any gate is built | **ARMED, NOT FIRED** — preliminary assessment: naive extensivity blocked; survival only through a not-yet-opened composition/extensivity gate |

## What This Does Not Claim

- **No rate constant is established.** The bounded rate is a ratio of
  declared fixture budgets; the SI numbers are scale statements about the
  Landauer bound's looseness, not measurements or model parameters.
- **No time, temporal order, or issuance is derived from T585.** Both
  budgets are declared inputs; deriving time from the fixture is a T585
  failure criterion and was not done.
- **No collapse model is endorsed.** GRW, CSL, and Diósi–Penrose appear as
  comparators for the matter-indexed scaling only; the capability-indexed
  sub-variant is a spec under assessment, currently wounded at the
  extensivity step, not a proposal the repository backs.
- **The discriminator is a spec, not a result.** No fixture, no run, no
  experiment design mature enough to execute, no sensitivity estimate.
- **No claim movement.** No claim-ledger, Canon Index, hypothesis, Lane, or
  public-posture change; T585/T586/T587 verdicts are untouched; no new
  T-number is created (T587's stop respected).
- **No bearing on the foliation branch.** A rate is a scalar; a foliation is
  a slicing; Part 1 tests only the former, exactly as the swing spec scoped.
- **Literature status.** The anchor citation (Donadi et al., Nature Physics
  17, 74 (2021), underground Ge test of gravity-related collapse) comes from
  the directing swing; the specific numeric values recalled around it (GRW
  per-particle rate ~10⁻¹⁶ s⁻¹; the DP smearing-length bound at the
  sub-angstrom scale) are **memory-cited in this offline run and are not
  source-verified here**. Under the repository's literature discipline they
  must be imported with sources before any use as evidence; nothing in
  Part 1's executable result depends on them.

## Constructive next object (named, not built)

1. **Composition/extensivity gate on the T583 contract** — declare a
   composition morphism class, then decide whether any T584-invariant,
   explicitly declared scalarization is additive on it (or additive up to a
   controlled superadditive defect sourced by cross-subsystem record edges).
   Opening it requires a T587-compliant reopening packet; if it fails, the
   Part 2 kill fires and the capability-indexed rate-density sub-variant is
   dead at spec stage.
2. **Differential-signature design study** (only if the gate survives):
   spectrum-resolved spontaneous-emission comparison at matched mass,
   composition, and temperature between low- and high-capability
   configurations, with the envelope-vs-execution coupling fork settled by
   budget-modulation (T583's declared budget axis) rather than by matter
   changes.
