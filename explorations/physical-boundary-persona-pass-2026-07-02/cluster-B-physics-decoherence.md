---
document_type: persona_panel_cluster_working_file
cluster: B-physics-decoherence
primary_reader: agents
read_pattern: current_state
write_pattern: append_only
authority: exploratory
created: 2026-07-02
status: exploratory
personas: [1-mathematical-physicist, 7-quantum-foundations, 8-quantum-information, 25-philosopher-of-physics, 54-experimentalist]
note: persona output is METHOD not evidence; single-process ceiling applies; no claim moves
---

# Cluster B — Physics / Decoherence

Steelmen (Phase 1) + Hegelian pass (Phase 2) for U1–U4, five personas, each
voice cold and independent. This cluster sits on the wound: the equality region
keeps turning out to be a declared subset of the co-present set. All physics
attributions flagged from memory, unverified. Terse.

---

## Persona 1 — Mathematical Physicist

### U1 — meaning of "physical rather than declared"

**Steelman.** "Physically forced" is a well-posed predicate ONLY as a statement
about a *net* of algebras and a *limit*, not about one finite density matrix. In
a finite-dimensional closed unitary model every partial trace is a chosen
coarse-graining; there is no algebraically distinguished factorization, so
"forced" cannot be intrinsic. The repair that survives is (b)+(c) fused:
entropy-priced permanence indexed to a causal-past exclusion, promoted to a
*limit statement* — the boundary is physical iff the recovery obstruction
survives the thermodynamic (or continuum/Reeh-Schlieder type-III) limit where
the commutant genuinely loses the recovering operation. Finite fixtures can only
*calibrate* the approach to that limit.

**Strongest supporting argument.** Genuine irreversibility is a limit
phenomenon: a finite closed unitary system is quasi-periodic (Poincaré
recurrence, reversible spectrum), so any "finality" it exhibits is stipulated by
the trace, exactly as the kill history found. Type-III₁ factors (Reeh-Schlieder)
have NO pure normal states and no trace — localization tails are forced, not
chosen. That is the only setting where "no localized record" is a theorem rather
than a bookkeeping convention.

**Hidden assumptions.** That the continuum/thermodynamic limit is the RIGHT
idealization for a *capability* claim (it imports infinite resources on both
sides); that a finite witness can certify a limit property at all; that
type-III structure is reachable in finite-witness house style (it is not — the
brief concedes the repo does not model type-III algebras).

**Vindicating theorem.** A finite-N family whose recovery-obstruction functional
has a certified monotone gap that provably DIVERGES (recovery cost → ∞) as
N→∞ at fixed agent budget, with the gap absent at every finite N under
enlargement — i.e. the boundary appears only in the limit, and the finite
fixtures track its onset.

**Killing finding.** A single finite closed unitary dilation in which the
"forced" recovery obstruction is discharged by a unitary on the declared reach
plus ancilla (Stinespring) — showing the obstruction was the trace, not the
dynamics. (This is what the artifacts' own dilation lemma already does for
work.)

**Confidence.** 4/10 that a finite fixture can carry U1 at all; 7/10 that the
limit reframing is the correct diagnosis.

**Phase 2.**
- *Thesis.* "Physical" = recovery obstruction that survives a genuine limit;
  finite fixtures calibrate.
- *Antithesis (must face finite-closed-model objection).* A finite CLOSED
  unitary model cannot *contain* an irreversibility; it can only stipulate one
  by partial trace. So U1 as posed — a physically-forced boundary certified
  *inside a finite fixture* — is ill-posed on its face: the fixture must either
  (i) stay closed and finite, in which case the boundary is always a chosen
  factorization (the T401 kill), or (ii) invoke a limit/open dynamics, in which
  case the "physical forcing" lives in the idealization (the reservoir kill),
  not in anything the finite witness computes. Every attempt so far chose (ii)
  and adopted the idealization.
- *Synthesis.* SHRINKS. What survives: "physically forced" is not a property of
  a finite closed model at all — it is a property of a *sequence* of models and
  their limit. The honest finite deliverable is not a forced boundary but a
  certified *rate of onset* of the obstruction along a family. The unconditional
  physical-boundary claim does not survive; the calibration-of-onset claim does.

### U2 — transport rung as next fixture

**Steelman.** Replace the stipulated `prepare_retained` trace with a genuine
Lieb-Robinson-bounded lattice dynamics: couplings local, agent's operations
supported on a fixed region, reach = the LR causal cone at the time budget. Then
"outside reach" is a proven operator-norm statement (the LR bound), not a
declaration. GO — but only to test whether the obstruction survives the closed
model, expecting it to fail.

**Strongest supporting argument.** LR gives an *approximate* factorization with a
rigorous, dynamics-derived error tail — the first candidate in this program
where "outside reach" has a theorem behind it (‖[A_R(t), B_S]‖ ≤ C e^{-(d-vt)/ξ}).

**Hidden assumptions.** That an *exponentially small* tail counts as a physical
boundary (it is a soft wall, not a wall); that the agent cannot wait longer
(v·t reaches everything); that a global correlation survives outside every LR
subcone — which LR itself does not forbid.

**Vindicating theorem.** A dynamics-derived reach set R(t) and a global
correlation certifiably absent from every LR-subcone marginal yet present in the
full-reach joint, with recovery cost lower-bounded by the LR tail — the T411
residue made dynamics-forced.

**Killing finding.** Wait-longer: for any fixed correlation, ∃ t with v·t ≥ d
recovering it, so the boundary is a time-budget threshold (resource), not a wall.

**Confidence.** 5/10.

**Phase 2.**
- *Thesis.* LR-derived reach makes "outside" a theorem; build the transport rung.
- *Antithesis (must face joint-record completion).* The LR tail is exponentially
  small but NONZERO at finite time. So the carrier outside the light cone is
  still co-present in the global state; joint-record completion re-enters exactly
  as "inside the light cone = co-present" — the brief's own worry. Worse, LR
  gives a *soft* boundary: the recovering operation exists with an
  exponentially-small-but-nonzero overlap, so "final" degrades to
  "exponentially-hard-to-recover," which is a resource threshold (wait-longer),
  precisely the resource-theory absorber the program already conceded.
- *Synthesis.* SHRINKS to a rate. What survives: LR converts the boundary from
  *declared* to *asymptotically forced with an explicit exponential rate*. It
  does not produce a sharp physical wall in finite time. The rung is worth
  building ONLY as the U1 onset-calibrator, not as a discriminator that beats
  joint-record completion at finite budget. Verdict: GO-as-calibration, not
  GO-as-discriminator.

### U3 — literature adjacency

**Steelman.** The natural mathematical home is the modular theory of the
recovery obstruction: Petz recovery + Tomita-Takesaki, where the failure of the
Petz map is quantified by relative entropy (Fawzi-Renner). The transport rung
BORROWS the decoupling/Petz machinery to *quantify* the obstruction, and
collides only if it claims a sharp boundary Petz already softens.

**Strongest supporting argument.** Fawzi-Renner: recoverability is controlled by
conditional mutual information — a continuous knob, not a wall. This is the
rigorous version of "every equality region is a declared subset": CMI > 0 means
recoverable-in-principle. Borrowing it tells you the honest currency is a
recovery *cost*, not a binary.

**Hidden assumptions.** That the repo's exact certificates (φ-independence,
machine-floor) are the CMI=0 corner (they are — B's retained joint is an exact
product, I(R:E1)=0); that Hayden-Preskill's prior-entanglement premise is
absent here (it is — no reference system is pre-shared).

**Vindicating theorem.** Show the repo's φ-independence certificate is exactly
the Petz-perfect-recovery (CMI=0) condition, and the R++ enlargement is the Petz
map — unifying the fixture with a known theorem and pricing the boundary as CMI.

**Killing finding.** If Hayden-Preskill applies (some pre-shared reference makes
the departed record recoverable at O(log) scrambling depth from *inside* reach),
the boundary is not even asymptotically forced.

**Confidence.** 7/10 that Petz/Fawzi-Renner is the correct adjacency; borrow,
mostly.

**Phase 2.**
- *Thesis.* Borrow Petz/Fawzi-Renner; the obstruction IS a CMI recovery cost.
- *Antithesis.* Borrowing Fawzi-Renner concedes the boundary is continuous
  (CMI), which is the resource-theory absorber in information-theoretic
  clothing. The GU firewall resonance (a sharp one-way boundary) is the OPPOSITE
  of what the borrowed theorem says — flag, do not lean.
- *Synthesis.* Survives as ADJACENCY, not support. What holds: the program's
  exact separator is the CMI=0 corner of Fawzi-Renner, and its enlargement
  control is the Petz map. Honest, unifying, publishable as a *calibration*
  statement. It kills the sharp-boundary ambition (that is the GU resonance the
  one-way rule forbids citing) and confirms the currency is recovery cost.

### U4 — strongest fallback

**Steelman.** (iii) sharpened: the global-correlation separator is a genuine
result — a certified example where the discriminating datum is a correlation
present in NO proper subset of a dynamics-defined region, hence *not* expressible
by any Lieb-Robinson / light-cone / local-marginal functional. That is a
positive structural fact about where capability information can hide.

**Strongest supporting argument.** T411 leg 6: all 200 proper-subset marginals
identical, full joint differs at TD=0.494872, verdicts flip. LR-irreducibility
is real content and survived the one absorber it faced.

**Hidden assumptions.** That "no proper subset" is robust to enlarging the reach
definition; that the reader accepts a finite exact witness as a theorem-shaped
object.

**Vindicating.** A no-go: no LR-local functional family can separate the two
capability states, proven, not just exhibited on one fixture.

**Killing.** Joint-record completion again — if the "no proper subset" region is
itself a declared subset of the co-present retained set, the separator is a
bookkeeping artifact of where you drew R.

**Confidence.** 6/10 as a paper; 8/10 that it is the strongest honest residue.

**Phase 2.**
- *Thesis.* Global-correlation / LR-irreducible separator is the paper.
- *Antithesis.* Surviving the LR absorber does not rescue the physical boundary
  (the brief says so explicitly); and the co-presence of the retained tier means
  the "no proper subset" is over a *declared* reach.
- *Synthesis.* Survives, scoped. The result is: *given* a declared reach, the
  separator is LR-irreducible — a real anti-relabel fact worth a short paper,
  provided it is stated as a property of the toolkit on a QD family, not as a
  physical boundary. Confidence the residue is real: high; that it is a
  physical-boundary result: nil.

---

## Persona 7 — Quantum Foundations Researcher

### U1 — meaning of "physical rather than declared"

**Steelman.** Quantum Darwinism already supplies the operationally correct sense
of "physical": a record is objectively present when it is *redundantly*
proliferated into many fragments so that many independent observers agree
without disturbing the system. "Physically forced" boundary = the record has
been redundantly broadcast into fragments the agent's reach does NOT include,
and redundancy makes single-fragment recovery impossible for the agent while
keeping the datum objective. Repair (a): agent-relative + dynamics-derived +
permanent-within-budget, cashed out as *redundancy the agent cannot collect*.

**Strongest supporting argument.** Redundancy r(n) is dynamics-produced and
observer-agnostic — the SBS (spectrum-broadcast-structure) state is a derived
attractor of decoherence, not a stipulation. If the discriminating datum lives
only in the *mutual* correlation across fragments none of which the agent holds,
that is a physical fact about proliferation.

**Hidden assumptions.** That the agent genuinely cannot access the redundant
fragments (else redundancy HELPS recovery — the objectivity that makes it
physical also makes it easy to find); that SBS is reached, not idealized; that
`r(n)=n` here is redundancy and not, as the decoherence absorber says, just
counting.

**Vindicating.** A fixture where redundancy is high (many agreeing fragments)
yet the agent's reach provably collects none, and the capability datum is the
cross-fragment correlation — objective AND out of reach.

**Killing finding.** Objectivity cuts the other way: if the record is redundant,
SOME fragment is almost surely in reach (that is the whole point of Darwinism),
so "out of reach" and "redundant" are in tension — the T401 kill in QD dress.

**Confidence.** 4/10.

**Phase 2.**
- *Thesis.* Physical boundary = redundant proliferation the agent cannot collect.
- *Antithesis (finite-closed-model).* In a finite closed model the "fragments"
  are just factors you chose; redundancy is computed after a stipulated
  system/environment cut. The SBS attractor is an open-system, large-environment
  idealization — reintroduce the reservoir kill. And Darwinism's own thesis
  (objectivity via redundancy) says a redundant record is EASY to access, so
  making it "out of reach" requires stipulating the agent away from the
  fragments — declared again.
- *Synthesis.* SHRINKS. Redundancy gives objectivity, not inaccessibility; the
  two pull opposite ways. What survives: the datum being a *cross-fragment*
  (global) correlation is the honest content (→ U4), but "physically forced
  boundary" does not survive — QD explains why records are objective, not why
  they are unreachable.

### U2 — transport rung

**Steelman.** Build it as a *scrambling* rung, not a ballistic-transport rung.
The record should not merely propagate outside a light cone (recoverable by
waiting) but be *scrambled* — spread across global degrees of freedom so no
local sub-region carries it. Then reach-as-subregion genuinely fails to
complete the joint record because the datum is nonlocal by dynamics. GO, framed
as scrambling.

**Strongest supporting argument.** Scrambling (OTOC decay, Hayden-Preskill) is
exactly "information present globally, in no small subsystem" — the operational
twin of T411's surviving residue, but *dynamically produced* rather than
stipulated by broadcast+trace.

**Hidden assumptions.** That the agent's reach is a *small* subsystem relative to
the scrambled whole; that scrambling in a finite closed model is not just a basis
rotation the agent can invert; that "no local subsystem" is stable, not an
artifact of the time slice.

**Vindicating.** Post-scrambling-time state where every reach-subregion marginal
is (near-)maximally mixed and identical between A and B, while the global joint
separates — the T411 leg-6 phenomenon, dynamics-forced.

**Killing finding.** Hayden-Preskill recovery: with pre-shared entanglement the
scrambled record is recoverable from a *small* fragment after scrambling — so
"scrambled = out of reach" is false given a reference. And wait-longer /
recurrence: closed finite scrambling un-scrambles (Poincaré).

**Confidence.** 5/10.

**Phase 2.**
- *Thesis.* Scrambling rung: the datum is dynamically nonlocal, reach-subregions
  fail to complete the joint record.
- *Antithesis (must face joint-record completion).* Scrambling does not remove
  the record from the GLOBAL state — it is unitary. Joint-record completion says:
  admit the whole scrambled system and the datum is right there; excluding it
  from R is declaration. "Inside the light cone = co-present" becomes "inside the
  scrambled whole = co-present." Hayden-Preskill makes it worse: it exhibits a
  *small* recovering fragment, so even the subregion story leaks. The reach stays
  a declared subset of the co-present scrambled register.
- *Synthesis.* SHRINKS. Scrambling upgrades the residue from stipulated-nonlocal
  to dynamics-nonlocal (genuine gain for U4) but does NOT defeat joint-record
  completion — the global unitary keeps everything co-present. Verdict: REDESIGN
  the rung's *claim* to "dynamically LR/scramble-irreducible separator," drop the
  "completes the joint record is blocked" ambition. The blockage is never
  physical in a closed model.

### U3 — literature adjacency

**Steelman.** This IS Hayden-Preskill / scrambling territory and the transport
rung should engage it directly. Borrow: the Hayden-Preskill decoding criterion
and scrambling time t\*∼log S give the exact conditions under which a departed
record is recoverable-in-principle and the cost/time to do it. The rung's
"final-relative-to-R" is the pre-decoding-threshold regime.

**Strongest supporting argument.** HP precisely characterizes "info dropped into
a fast scrambler is recoverable after t\* given a reference" — the quantitative
grammar for "when and at what cost is recovery possible," which is U3's exact
question. It collides productively: it tells you your boundary is temporary and
reference-dependent.

**Hidden assumptions.** That a reference system exists (HP requires prior
entanglement with the infalling info); absent a reference, HP recovery does not
apply and the boundary could be sharper — this is a load-bearing branch.

**Vindicating.** Map the fixture's recovery-at-R++ onto an HP/Yoshida-Kitaev
decoder and show R+ finality = pre-scrambling-time (no decoder succeeds).

**Killing finding.** The GU firewall resonance is a trap: HP/ER=EPR says the
horizon boundary is NOT a firewall (smooth), i.e. the info is recoverable — so
leaning on the horizon as a "physically forced one-way boundary" contradicts the
very literature. FLAG: GU firewall-boundary hypothesis resonates with the
*sharp* boundary ambition, but HP says the boundary is soft. Do not treat as
support (one-way rule).

**Confidence.** 7/10.

**Phase 2.**
- *Thesis.* Borrow HP/scrambling; it is the natural home.
- *Antithesis.* HP is a *recoverability* result — its whole force is that the
  boundary is crossable given a reference and enough time. Borrowing it imports
  the conclusion that there is no permanent physical wall, which is the
  wait-longer + resource absorber. The horizon "home" comes with the firewall
  controversy, not a clean physical boundary.
- *Synthesis.* Survives as adjacency + borrowing, kills the sharp-boundary
  dream. What holds: the fixture's finality is the *no-reference, pre-scrambling*
  corner of HP; the honest statement is a recovery-threshold, cost-priced. The
  firewall resonance is logged as stress-test input only. Adjacency: HP + Yoshida-
  Kitaev decoding; borrow, do not collide destructively.

### U4 — fallback

**Steelman.** (iii): the global-correlation separator is the anti-Darwinism
result — a capability datum that is *objectively real* (present in the joint)
yet carried by NO fragment, the exact inverse of a Darwinist redundant record.
That is a foundationally interesting object: a "record" that fails objectivity-
by-redundancy yet still gates capability.

**Strongest supporting argument.** At β=0 the record is entirely in joint
coherences spanning the departure boundary; every single-fragment Holevo is
exactly 0 (T410 leg 6). This is a clean, computed anti-SBS state.

**Hidden assumptions.** That "gates capability" survives without the departed
tier being called physical; that anti-objectivity is interesting rather than
just "the record was destroyed."

**Vindicating.** A witness distinguishing "capability datum in global coherence,
zero in every fragment" from "datum simply erased" — an operational separator.

**Killing.** If zero-in-every-fragment is indistinguishable from erased for the
agent, there is no capability difference to gate — collapse to nothing.

**Confidence.** 6/10.

**Phase 2.**
- *Thesis.* Anti-Darwinist global-coherence separator is the fallback paper.
- *Antithesis.* Joint-record completion: the global coherence is co-present;
  refusing to read it is declaration. And "gates capability" leans on the R+/R++
  reach split which is the declared cut.
- *Synthesis.* Survives, scoped to the toolkit-on-QD-family framing: a computed
  anti-SBS capability separator, foundationally cute, LR-irreducible. Worth a
  section, maybe a short paper jointly with the QI framing. Not a physical
  boundary.

---

## Persona 8 — Quantum Information Theorist

### U1 — meaning of "physical rather than declared"

**Steelman.** Drop "physical" as a substance predicate; define it operationally
via decoupling. A boundary is physically forced (not declared) iff the reach
subsystem is *decoupled* from the discriminating reference — I(R:Ref)=0 as a
DERIVED consequence of the dynamics on a fixed factorization, with the
factorization itself fixed by the interaction graph, not chosen post hoc. The
survivor among repairs is (c)+(d): causal-past exclusion realized as a decoupling
theorem, plus protocol-impossibility as the converse (no channel on R recovers).

**Strongest supporting argument.** Decoupling is the workhorse of modern quantum
Shannon theory: if R decouples from the reference, no operation on R recovers the
info, PROVABLY (converse). That is protocol-impossibility with a theorem, and it
is dynamics-derived once the factorization is dynamics-fixed.

**Hidden assumptions.** That the factorization is dynamics-fixed and not chosen
— the entire kill history says it is chosen (`prepare_retained` on a stipulated
set). Decoupling on a *declared* bipartition is still declared.

**Vindicating.** A decoupling statement I(R:Ref)→0 where R is defined by the
interaction graph's causal past and the reference by the task, with no free
partition choice.

**Killing finding.** Complementary recovery: decoupling of R from Ref means the
COMPLEMENT recovers perfectly (information conservation) — so the datum is
maximally present just outside R, i.e. co-present, i.e. the T401 kill. Decoupling
is exactly the statement that the record is elsewhere, not gone.

**Confidence.** 4/10.

**Phase 2.**
- *Thesis.* Physical = derived decoupling on a dynamics-fixed factorization.
- *Antithesis (finite-closed-model).* In a finite closed unitary model,
  decoupling R from Ref is *equivalent* to the complement recovering Ref
  (Uhlmann/complementary-channel duality). The record is never destroyed, only
  relocated to R^c, which is co-present. So decoupling formalizes the kill
  rather than escaping it: "final relative to R" ⇔ "recoverable from R^c," and
  R^c is a declared subset of the closed whole. There is no decoupling without a
  complement, and the complement is always co-present in a closed model.
- *Synthesis.* SHRINKS to honesty. Decoupling is the right *language* but it
  encodes the wound: physicality-as-decoupling is always relative to a
  factorization, and in a closed model the complement co-presents the datum.
  Survivor: the boundary is a *relative* object (R vs R^c), never absolute — U1
  has no closed-model absolute repair. This matches the Mathematical Physicist's
  limit conclusion.

### U2 — transport rung

**Steelman.** Design the rung around approximate decoupling with a
dynamics-derived rate: as the interaction graph spreads the reference across the
system, I(R:Ref) decays at a computable rate for the FIXED reach R. Recovery
cost is lower-bounded by the decoupling error. GO — it is the cleanest place to
get a *derived* obstruction with a *rate*.

**Strongest supporting argument.** Decoupling theorems give explicit rates
(smooth-min-entropy); you get an honest "recovery-hard-by-this-much" number that
is dynamics-derived, not stipulated. That is strictly more than `prepare_retained`.

**Hidden assumptions.** That approximate (nonzero-error) decoupling is a
boundary and not a threshold; that scrambling helps rather than enabling
Hayden-Preskill small-fragment decoding.

**Vindicating.** Certified I(R:Ref) ≤ ε(t) decaying with graph spread, with a
matched recovery-cost lower bound, and a global separator surviving in R^c.

**Killing finding.** Hayden-Preskill: after scrambling time, a reference-holding
decoder recovers the datum from a fragment barely larger than the reference — so
approximate decoupling of a fixed small R does NOT block a clever joint decoder;
joint-record completion succeeds via the HP decoder.

**Confidence.** 6/10.

**Phase 2.**
- *Thesis.* Approximate-decoupling transport rung with a derived rate.
- *Antithesis (must face joint-record completion).* Decoupling R does not remove
  the datum from the global state; by complementary recovery it sits in R^c, and
  by Hayden-Preskill even a small out-of-reach fragment (+ reference) completes
  the joint record after t\*. So the reachable set stays a declared subset of the
  co-present set and, worse, HP gives a *constructive* completion. The rung
  cannot block joint-record completion; it can only price it.
- *Synthesis.* SHRINKS to a cost. Survivor: the transport rung delivers a
  *dynamics-derived recovery-cost lower bound* (decoupling rate) — genuinely
  more than the stipulated trace, and the correct anti-resource-theory move is to
  show this cost is not payable in the frame's currency (work) but only by reach.
  It does NOT deliver a joint-record-completion block. Verdict: GO to produce the
  priced obstruction; REDESIGN the claim to "reach-priced recovery cost, derived"
  and abandon "joint record blocked."

### U3 — literature adjacency

**Steelman.** Directly Hayden-Preskill + Petz + decoupling — and the fixture
should be stated in that language from the start. Borrow the whole apparatus:
the φ-independence certificate = perfect-decoupling / CMI=0 (Petz-perfect); the
R++ enlargement = the recovery map; the recovery cost = Fawzi-Renner
CMI-remainder. This is not a collision, it is a translation into a mature
theory, and that is a feature: it makes the result legible.

**Strongest supporting argument.** Every load-bearing object has an exact
counterpart: complementary-channel recoverability dichotomy (the A-vs-B split is
textbook eraser-accessible vs escaped), decoupling converse, Petz map. The
program is reconstructing quantum Shannon theory on a capability index — worth
saying cleanly.

**Hidden assumptions.** That translation-into-known-theory is publishable as
contribution (it is, as a *bridge*, not as new physics); that the capability
indexing adds something the plain channel statement lacks.

**Vindicating.** A theorem: capability-state separation ⇔ CMI/decoupling gap,
with the reach filtration as the resource order — a clean dictionary.

**Killing finding.** If the dictionary is exact and complete, there is NO residue
beyond known theory — the decoherence-bookkeeping absorber wins at the theorem
level (the program is Petz + decoupling with new labels).

**Confidence.** 8/10 that this is the home; 5/10 that anything beyond translation
survives.

**Phase 2.**
- *Thesis.* Borrow HP/Petz/decoupling wholesale; state the fixture in that
  language.
- *Antithesis.* Complete borrowing IS the absorber: if the object is exactly
  CMI/decoupling with a capability relabel, then "work cannot buy reach" is the
  data-processing/monotonicity axiom and the separator is complementary-channel
  recoverability — conceded in leg 7. GU firewall resonance is anti-support (HP
  says boundary soft).
- *Synthesis.* Survives as a bridge, not a discovery. What holds: a clean,
  correct dictionary between the capability program and Hayden-Preskill/Petz/
  decoupling, whose one non-standard axis is the *reach-indexing* of the recovery
  order (dynamical resource theory of the recovery superchannel) — that axis is
  the only candidate residue, and T404 already flagged it as demotable if
  dynamical-resource-theory of channels verifies. Adjacency confirmed; borrow;
  residue thin.

### U4 — fallback

**Steelman.** (i)+(iii): the certificate toolkit is calibrated recovery-map
machinery (exact CMI=0 witnesses + graded recovery-cost bands) on a QD family,
AND the LR/complementary-channel-irreducible separator is a concrete
anti-relabel exhibit. Packaged together: "certified recoverability geometry of a
thermal collision channel, with a separator no local functional expresses."

**Strongest supporting argument.** The certificates work (214 passing assertions,
machine-floor exactness, factor-2 band measured across four artifacts) — that is
real, reproducible calibration content independent of the boundary claim.

**Hidden assumptions.** That calibration of standard machinery is publishable
(marginal — needs a hook); that the LR-irreducibility adds the hook.

**Vindicating.** Show the toolkit computes a recoverability quantity (Petz
fidelity / CMI) that a standard method gets wrong or cannot band, on a nontrivial
family.

**Killing.** If the toolkit only re-derives known CMI/Petz numbers, it is a
re-implementation, not a contribution.

**Confidence.** 6/10.

**Phase 2.**
- *Thesis.* Toolkit-as-recovery-calibration + LR-irreducible separator.
- *Antithesis.* Calibration of standard theory is not a result unless it does
  something standard theory does not; and the separator survived only the wrong
  absorber.
- *Synthesis.* Survives as the honest fallback: a calibration + one genuine
  structural exhibit (LR/complementary-irreducible separator). Paper-worthy as a
  focused methods-plus-example note, NOT as a physical-boundary or
  quantum-foundations breakthrough. Confidence real content survives: high;
  physical-boundary: nil.

---

## Persona 25 — Philosopher of Physics

### U1 — meaning of "physical rather than declared"

**Steelman.** The distinction the program wants is the old one between a
*conventional* (coordinate/gauge) cut and an *invariant* one. "Physical rather
than declared" should mean: invariant under the redescription group of the model
— i.e. the boundary is physical iff every admissible re-factorization /
re-partition agrees it is there. Repair: none of (a)-(d) alone; the well-posed
criterion is *partition-invariance* of the recovery obstruction.

**Strongest supporting argument.** This is exactly how physics separates real
from bookkeeping everywhere else (gauge invariance, general covariance, frame-
independence). It gives a sharp test: is the obstruction invariant under the
symmetry that shuffles what counts as "retained"? If not, it is a coordinate
artifact — which is precisely the T401 diagnosis.

**Hidden assumptions.** That there is a well-defined redescription group for
subsystem factorizations (there is: the local-unitary / factorization-choice
group); that finite closed models have enough invariants to carry it (they may
not — this is the wound).

**Vindicating.** A recovery obstruction certified invariant under the full
factorization-redescription group — genuinely physical by the same standard as
any gauge-invariant quantity.

**Killing finding.** The factorization group acts transitively enough that ANY
finite-model obstruction can be redescribed away (tensor-factor ambiguity) —
then no finite closed model has a partition-invariant boundary, and U1 is
ill-posed exactly as posed.

**Confidence.** 5/10.

**Phase 2.**
- *Thesis.* Physical = partition/redescription-invariant obstruction.
- *Antithesis (finite-closed-model).* The subsystem-factorization ambiguity is
  notorious: in a finite closed system, "which tensor factors are the agent's
  reach" is a choice with no invariant fixture-internal ground. Every equality
  region has been a declared subset precisely BECAUSE the factorization is a
  convention. Partition-invariance, applied honestly, likely rules out EVERY
  finite-closed obstruction — so the criterion is well-posed but its extension is
  empty for the model class the house style permits. The invariant only appears
  once dynamics (locality of the Hamiltonian) *privileges* a factorization — and
  that is an open-system / continuum move again.
- *Synthesis.* SHRINKS, possibly to EMPTY for finite closed models. Survivor:
  U1 is well-posed as partition-invariance, and its verdict on the existing
  fixtures is *negative* — they are coordinate artifacts. A physical boundary
  requires a dynamics-privileged factorization (Hamiltonian locality), which is
  the transport rung's premise and lives at the edge of the house style. Honest
  synthesis: the criterion exists; the finite closed fixtures fail it; that
  failure is the correct, publishable finding.

### U2 — transport rung

**Steelman.** GO, because Hamiltonian locality is the ONE thing that privileges a
factorization non-conventionally — a local Hamiltonian makes "nearby" an
invariant fact, so a reach derived from it is not a mere choice. The transport
rung is the first design where "physical" has a fighting chance of meaning
partition-privileged rather than partition-declared.

**Strongest supporting argument.** Locality of interactions is a physical input
(you cannot gauge it away without changing the dynamics), so a reach built from
the interaction graph inherits that non-conventionality. This is philosophically
the right move.

**Hidden assumptions.** That inhabitants of the model agree the Hamiltonian's
locality structure is itself not a declaration (it is a modeling choice, but a
*dynamical* one, which is the relevant upgrade); that a privileged factorization
yields a SHARP boundary rather than a soft LR tail.

**Vindicating.** A recovery obstruction invariant under all factorizations that
preserve the Hamiltonian's locality structure — physical in the gauge sense.

**Killing finding.** Wait-longer shows the locality-privileged reach still grows
with the time budget, so the boundary is a threshold relative to a resource
(time), not an invariant wall — the philosopher's "real vs conventional"
collapses into "expensive vs cheap."

**Confidence.** 5/10.

**Phase 2.**
- *Thesis.* Local Hamiltonian privileges the factorization → a chance at a
  non-conventional boundary.
- *Antithesis (joint-record completion).* Even with a privileged factorization,
  the global state is closed and unitary: the datum is co-present in the full
  system, and admitting it (joint-record completion) is not a gauge violation —
  it is just using the whole state. Locality privileges *distance*, not
  *inaccessibility*; the agent who waits or who reads the global correlation
  completes the record. "Inside the light cone = co-present" is the exact
  restatement: the light cone is invariant, but everything inside it is still
  co-present, and it eventually contains everything.
- *Synthesis.* SHRINKS. Survivor: locality upgrades the boundary from *declared*
  to *convention-reduced* (partition-privileged), which is a real philosophical
  gain and defeats the "pure declaration" charge — but it does NOT defeat
  joint-record completion, because privilege≠inaccessibility in a closed model.
  Verdict: GO to earn "not merely declared," but the honest ceiling is a
  *soft, resource-indexed* boundary, not a wall.

### U3 — literature adjacency

**Steelman.** The natural home is the philosophy of black-hole information and
the horizon-as-boundary literature — where exactly this question (is the horizon
a *physical* one-way information boundary or an observer-relative one?) is live
and unresolved. The transport rung is a finite, controlled toy for that debate.
Borrow the framing; do not claim to resolve it.

**Strongest supporting argument.** The horizon literature has already spent
decades on "physically forced vs observer-relative information boundary," compl
with firewalls, complementarity, ER=EPR — a ready-made conceptual toolkit and
audience for a clean finite model.

**Hidden assumptions.** That a finite non-gravitational toy speaks to the
gravitational case (analogy, not derivation); that observer-relativity
(complementarity) is not itself the concession that the boundary is declared.

**Vindicating.** A finite model that instantiates black-hole complementarity's
"no observer sees a contradiction" structure with a computed capability index.

**Killing finding.** Black-hole complementarity's lesson is that the boundary IS
observer-relative (declared-per-observer) and no single physical wall exists —
which, imported honestly, CONFIRMS the kill rather than escaping it. And the GU
firewall resonance is the disputed, minority sharp-boundary position — flagging
it as resonance is correct; leaning on it would be adopting the least-supported
horizon view as if it were TaF support (one-way rule forbids).

**Confidence.** 6/10.

**Phase 2.**
- *Thesis.* Home = horizon-information philosophy; borrow the framing.
- *Antithesis.* The mainstream horizon lesson (complementarity, HP recovery) is
  that the boundary is observer-relative and soft — importing it imports the
  concession. The GU firewall resonance is exactly the contested sharp-boundary
  claim; treating the resonance as encouragement would be circular (GU is
  stress-test input, never evidence).
- *Synthesis.* Survives as framing + honest audience, kills the escape. What
  holds: the transport rung is a legitimate finite toy for the
  physical-vs-observer-relative boundary debate, and its likely verdict
  (observer-relative / soft) aligns with mainstream horizon thinking. The GU
  firewall resonance is logged, quarantined, and explicitly NOT support. Publish
  as "a finite capability model of the observer-relative information boundary,"
  not as a resolution.

### U4 — fallback (SHARPEST HONEST VERDICT)

**Steelman.** The strongest honest fallback is (iii) stated as a *negative*
structural theorem with positive content: *the discriminating datum for a
capability difference can be a global correlation irreducible to any local
(Lieb-Robinson-expressible) functional* — a demonstrated dissociation between
"what a region can DO" and "what any local statistic of the region can SEE." That
dissociation is the actual philosophical thesis of the whole program (capability
≠ observability), and here it has a clean finite exhibit. THIS is worth a paper —
as a result about the epistemology of capability, not about physical boundaries.

**Strongest supporting argument.** The program's founding claim is that the
honest ledger is what a region can DO, not what it can SEE. The LR-irreducible
separator is the first concrete, computed, absorber-tested demonstration that
these come apart — the observational functionals (all R-supported statistics)
agree while the capability verdict differs. That is the thesis instantiated.

**Hidden assumptions.** That the DO/SEE gap here is not just "the datum left the
region" (trivial) but genuinely "present-globally-yet-locally-invisible"
(nontrivial — and leg 6 supports it: nonzero global TD, zero every proper subset);
that a reviewer values the dissociation over the deflation.

**Vindicating.** A no-go: no local/LR functional family separates the capability
states, proven for the family — turning the exhibit into a theorem.

**Killing.** If DO/SEE never actually come apart — if some admissible R-supported
operation (not just passive statistic) reveals the datum — then the dissociation
is illusory and only the trivial "it left" remains. (The T401 kill is exactly
the claim that a retained co-present register + one measurement DOES reveal it.)

**Confidence.** 6/10 that it is paper-worthy; 8/10 that it is the strongest
honest fallback available.

**Phase 2.**
- *Thesis.* The LR-irreducible DO/SEE dissociation is the real, paper-worthy
  result.
- *Antithesis.* Joint-record completion says the SEE side was under-counted: the
  retained tier-1 is co-present and a single Z-measurement (P=0.4286 vs 0) SEES
  the difference — so DO and SEE do NOT come apart once you admit everything
  co-present; the dissociation was an artifact of drawing R short of the retained
  set.
- *Synthesis.* Survives ONLY at β=0 and ONLY for the reach-relative reading. The
  honest verdict: at the β=0 corner the datum is provably in no proper subset
  (leg 6, 200 marginals, Holevo exactly 0) — there the DO/SEE dissociation is
  real and LR-irreducible, and that specific corner is worth a *short, sharply
  scoped* paper: "a capability separator carried by a global correlation local
  functionals cannot express, on a thermal QD family." At β=∞ the joint-record
  kill applies (retained record readable) and there is no dissociation. So the
  fallback is real but NARROW — a single-corner anti-relabel exhibit, not a
  general DO/SEE theorem. That narrowing is the method working.

---

## Persona 54 — Experimentalist

### U1 — meaning of "physical rather than declared"

**Steelman.** Operationalize "physical" as *protocol-impossibility with a
falsifiable witness*: the boundary is physical iff there is a concretely
specified in-reach protocol that the model FORBIDS (certificate) and whose
success would be an observable event. Declared boundaries have no falsifiable
witness — you cannot run an experiment that could have shown the boundary was
crossable. Repair (d), protocol-impossibility, is the only one an experimentalist
can hold.

**Strongest supporting argument.** Falsifiability is the demarcation: a physical
boundary must license a bet — "no in-reach protocol achieves X, and here is the
device that would catch you if it did." The φ-independence certificate against
all channels + unlimited work IS such a bet. Declaration cannot be caught.

**Hidden assumptions.** That "all in-reach protocols" is exhaustively certifiable
(the certificate claims it via the channel lemma — that is the load-bearing
assumption); that the reach itself is fixed non-circularly (it is not — reach is
declared).

**Vindicating.** An adversary given the state on R, unlimited work, and any CPTP
channel, provably cannot achieve the task — and a red-team fails to break it.

**Killing finding.** The red-team on the CO-PRESENT retained register: give the
adversary the retained tier-1 (which physically exists in both runs) and a single
Z-measurement breaks equality (P=0.4286 vs 0). The "impossibility" was only over
a declared-short reach; widen to the co-present set and the protocol succeeds.

**Confidence.** 4/10.

**Phase 2.**
- *Thesis.* Physical = falsifiable in-reach protocol-impossibility.
- *Antithesis (finite-closed-model).* In a finite closed model, "in-reach" is
  the only knob, and it is declared. The impossibility certificate is airtight
  *given* R — but the adversary who is handed the co-present retained register
  (which the closed model physically contains) wins immediately. So the
  falsifiable content is "no protocol on the DECLARED reach succeeds," which is
  true and uninteresting; the physical question "is R the right reach" has no
  in-model experiment. The witness exists but tests declaration-consistency, not
  physicality.
- *Synthesis.* SHRINKS. Survivor: protocol-impossibility gives a REAL,
  reproducible witness — but only certifies "final relative to the declared R,"
  not "physically final." The experiment that would distinguish physical from
  declared (vary R and show the boundary is invariant) is not available in a
  finite closed fixture. Honest: the toolkit produces genuine impossibility
  certificates; they do not reach "physical."

### U2 — transport rung (PREMORTEM)

**Steelman.** GO, because the transport rung is the FIRST design where reach is
an *measured output of the dynamics* rather than a dial: run the local dynamics
for time t, measure where correlations actually are, define reach = where the
agent's couplings physically touch within t. That makes `prepare_retained`
unnecessary — departure is a consequence you observe, not a trace you impose.
That is the single biggest experimental upgrade available.

**Strongest supporting argument.** It removes the one object every absorber
attacked: the hand-imposed partial trace on a stipulated set. If departure is
dynamically produced, the decoherence-bookkeeping and reservoir-idealization
kills lose their target.

**Hidden assumptions.** That the agent's couplings are *finitely* limited in a
way that does not itself smuggle in a declared reach (the coupling graph is a
modeling choice — but a dynamical one); that the observed departure is not
trivially reversible within budget.

**Vindicating.** A run where (i) reach is read off the dynamics, (ii) the
capability split appears at that dynamics-defined reach, (iii) no proper subset
holds the datum, (iv) recovery cost is dynamics-lower-bounded — all four in one
fixture with NO `prepare_retained`.

**Killing finding (four killers, head-on):**
- *Joint-record completion:* the propagated carrier is still in the global closed
  state; admit it and the record completes. Blocks the "physical block" claim.
- *Wait-longer:* reach = v·t grows; the boundary is a time-budget threshold, not
  a wall. Turns the boundary into a resource.
- *Lieb-Robinson relabel:* dynamics-derived reach IS a light cone — the very
  object T411 was proud to NOT be.
- *Reservoir idealization:* if you re-add a bath to get true departure, departure
  is adopted again.

**Confidence.** 5/10.

**Phase 2.**
- *Thesis.* Dynamics-measured reach eliminates the stipulated trace; build it.
- *Antithesis (must face joint-record completion).* The transport rung's carrier
  never leaves the closed global state — it propagates within it. Joint-record
  completion: admit the full propagated system and one measurement on the carrier
  (now at distance d, but co-present) separates A from B. The reachable set is
  still a DECLARED subset of the co-present (whole-system) set; "outside the
  light cone" is the new name for "excluded from R," and it is co-present. The
  rung trades `prepare_retained` for a light-cone declaration — and then faces
  the Lieb-Robinson relabel it was built to avoid. Worst case: it dies to TWO
  killers at once (joint-record completion + LR).
- *Synthesis.* SHRINKS to a conditional GO. Survivor: the rung is worth building
  ONLY IF it targets the *derived recovery-cost band* (dynamics-lower-bounded,
  reach-priced, work-can't-substitute) and the *global/LR-irreducible separator*
  — NOT a joint-record-completion block, which a closed model cannot deliver. If
  the design still centers "the boundary physically blocks completion," ABANDON
  that framing. Net premortem verdict: **REDESIGN → GO** as a recovery-cost /
  anti-relabel rung; **ABANDON** as a physical-completion-block rung. Highest-
  value single change: reach measured from dynamics, no `prepare_retained`.

### U3 — literature adjacency

**Steelman.** Engage Hayden-Preskill experimentally: the transport rung is a
small, exactly-simulable HP scrambling-and-decoding scenario. Borrow the
Yoshida-Kitaev decoder as the concrete "recovery protocol" whose success/failure
IS the boundary test. This gives the rung an executable, literature-anchored
falsification target.

**Strongest supporting argument.** HP decoding has explicit finite-size protocols
(traversable-wormhole / probabilistic decoders) already run on small quantum
simulators — a ready template for an executable capability-recovery witness.

**Hidden assumptions.** That the no-reference case (which sharpens the boundary)
is the relevant one, or that the reference-dependence is explicitly declared;
that finite-size HP is not dominated by recurrence.

**Vindicating.** A simulated decoder that succeeds exactly at R++ and provably
fails at R+, matching the certificate — the recovery threshold made executable.

**Killing finding.** The decoder succeeds from a small out-of-reach fragment
after scrambling (HP) — showing the boundary is crossable and the completion not
blocked. And the GU firewall resonance is not experimentally accessible — flag,
ignore as evidence.

**Confidence.** 6/10.

**Phase 2.**
- *Thesis.* Borrow HP + Yoshida-Kitaev as the executable recovery test.
- *Antithesis.* HP decoders are RECOVERY successes — their existence is the
  wait-longer/joint-completion killer made concrete. Borrowing the machinery
  imports a working completion protocol.
- *Synthesis.* Survives as an executable falsification harness, not as support.
  What holds: the rung can be stated as a finite HP-decoding experiment whose
  certificate predicts exactly when the decoder fails (R+) and succeeds (R++) —
  a clean, runnable, falsifiable claim. It will confirm the boundary is a
  recovery threshold (cost/time-priced), which is the honest content. GU
  firewall resonance flagged, non-evidential.

### U4 — fallback (SHARPEST HONEST VERDICT)

**Steelman.** Yes — worth a paper, as a METHODS + EXHIBIT result, not a physics
claim. The deliverable: (i) a reproducible certificate toolkit (all-channel
φ-independence, factor-2 bands, entropy ledger) validated across four artifacts
and 214 passing assertions, PLUS (iii) one clean executable exhibit — the
β=0 global-correlation separator where every one of 200 proper-subset marginals
is identical and only the full joint (TD=0.494872) and the capability verdict
differ. That pair — a validated tool and a striking, absorber-tested example —
clears the bar for a focused methods/quantum-information paper.

**Strongest supporting argument.** It is EXECUTABLE and REPRODUCED: deterministic,
machine-floor, 214 green assertions, closed-form corners hand-derived pre-run,
cross-pinned across T392/T409/T410/T411. That reproducibility is exactly what a
methods paper needs, and it does not depend on the physical-boundary claim that
died.

**Hidden assumptions.** That "global-correlation separator" survives a hostile
reviewer widening the region (the T401 kill); that the toolkit does something a
standard Petz/CMI computation does not (else it is a re-implementation).

**Vindicating.** External reproduction of the separator + a referee agreeing the
LR-irreducibility is non-trivial (no local functional expresses it).

**Killing.** A reviewer shows the separator is the R+ marginal of a co-present
retained register (joint-record completion) — then even the exhibit is a
bookkeeping artifact and only the toolkit (calibration) remains.

**Confidence.** 6/10 that the pair is paper-worthy; 8/10 that the toolkit alone
is a solid internal calibration asset; 2/10 that any physical-boundary claim
survives.

**Phase 2.**
- *Thesis.* Toolkit + β=0 separator = a real methods/QI paper.
- *Antithesis.* Joint-record completion threatens the separator (co-present
  retained register); calibration-of-standard-machinery alone is thin.
- *Synthesis.* Survives, scoped and narrowed. Honest fallback verdict: the
  **certificate/ledger toolkit is a genuine, reproducible calibration asset**
  (worth writing up regardless), and the **β=0 LR-irreducible separator is a
  worth-a-short-paper exhibit IF it survives region-widening** — which is exactly
  the open hostile-review question. Recommend: write the methods note now (safe);
  hold the separator-as-result until a hostile reviewer tries the joint-record
  completion on the β=0 corner specifically. Physical-boundary paper: no.

---

## Cluster Synthesis

Persona output is method, not evidence; the five voices are one process wearing
masks (single-process ceiling). Convergence below is a TARGET generator, not
support. Attributions (Reeh-Schlieder/type-III, Lieb-Robinson, Hayden-Preskill,
Petz/Fawzi-Renner, Yoshida-Kitaev, EGY, SBS/quantum-Darwinism) all from memory,
unverified.

### U1 — what "physical rather than declared" must mean

**Strongest surviving repair.** None survives as an ABSOLUTE, finite-closed-model
criterion. Five independent reframings converge on the SAME shrinkage: physical
forcing is not a property a finite closed unitary model can contain — it is a
property of a *limit/sequence* (Math-Phys: thermodynamic/type-III limit;
Phil-Phys: partition-invariance, likely empty for finite closed models;
QI: decoupling ⇔ complementary-recovery, so the datum is always co-present in the
complement; QF: redundancy gives objectivity not inaccessibility; Experimentalist:
protocol-impossibility only certifies "final relative to declared R").
- **Backing personas:** all five.
- **Best honest survivor:** "physical" = obstruction that survives a genuine
  limit / is partition-invariant / is a dynamics-derived *recovery cost* — none
  achievable as a sharp boundary in a finite closed fixture.
- **Confidence range:** 4–5/10 that any repair is finite-model-realizable; 7/10
  (Math-Phys, QI) that the limit/decoupling DIAGNOSIS is correct.
- **Dissent/empty:** Phil-Phys synthesis is potentially EMPTY (partition-
  invariance may rule out every finite-closed obstruction). QF's redundancy
  repair actively BACKFIRES (objectivity ⇒ accessibility). Recorded as shrinkage.

### U2 — transport rung premortem

**Strongest surviving verdict.** **REDESIGN → GO** as a recovery-cost /
anti-relabel rung; **ABANDON** the "physically blocks joint-record completion"
framing. Unanimous across the cluster that dynamics-derived reach does NOT block
joint-record completion in a closed model: "excluded from R" simply becomes
"outside the light cone / outside the decoupled region," and the datum stays
co-present (complementary recovery; Hayden-Preskill even gives a constructive
small-fragment completion). The rung faces joint-record completion AND the
Lieb-Robinson relabel simultaneously if framed as a wall.
- **Genuine gains the rung DOES deliver:** (1) eliminates the stipulated
  `prepare_retained` trace (Experimentalist — highest-value single change: reach
  measured from dynamics); (2) a *dynamics-derived recovery-cost lower bound*
  (QI decoupling rate; Math-Phys LR exponential tail) — strictly more than a
  stipulated trace and the correct anti-resource-theory target (cost payable only
  in reach, not work); (3) upgrades the residue from stipulated-nonlocal to
  *dynamics-nonlocal* (QF scrambling; global/LR-irreducible separator).
- **Backing personas:** all five converge on REDESIGN→GO-as-cost/anti-relabel,
  ABANDON-as-wall.
- **Confidence range:** 5–6/10.
- **Dissent/empty:** wait-longer is unrefuted — every persona concedes the
  boundary is a time/resource threshold, not a wall, at finite budget. No
  synthesis rescues a sharp physical wall; that ambition is recorded DEAD.

### U3 — literature adjacency

**Strongest surviving adjacency.** BORROW, do not collide. The natural home is
Hayden-Preskill / decoupling / Petz / Fawzi-Renner recoverability (QI, QF,
Experimentalist), with the modular-theory framing (Math-Phys) and the
horizon-information *philosophy* debate as conceptual home (Phil-Phys). Exact
correspondences: φ-independence certificate = perfect decoupling / CMI=0 /
Petz-perfect; R++ enlargement = the recovery (Petz) map; recovery cost =
Fawzi-Renner CMI remainder; A-vs-B = complementary-channel recoverability
dichotomy; executable test = Yoshida-Kitaev decoder.
- **Backing personas:** all five; QI (8) and QF (7) engaged Hayden-Preskill/
  scrambling directly as instructed.
- **Confidence range:** 7–8/10 that this is the correct home.
- **Key consequence:** borrowing IMPORTS the conclusion that the boundary is
  soft/recoverable/cost-priced (the resource absorber in information-theoretic
  dress). The only candidate residue beyond translation is the *reach-indexing*
  of the recovery order (dynamical resource theory of the recovery superchannel)
  — thin, and T404 already flagged it demotable.
- **GU firewall resonance:** FLAGGED by every persona, treated as anti-support —
  Hayden-Preskill/complementarity say the boundary is SOFT, the opposite of the
  GU sharp-boundary hypothesis; leaning on the resonance would be adopting the
  contested minority horizon view as if it were TaF support. One-way rule held.
- **Dissent/empty:** if the Petz/decoupling dictionary is exact and complete
  (QI's fear), there is NO residue beyond relabeling — the decoherence-bookkeeping
  absorber wins at theorem level. Recorded.

### U4 — strongest honest fallback

**Strongest surviving fallback.** A PAIR: **(i) the certificate/ledger toolkit as
a reproducible calibration asset** (all-channel φ-independence, factor-2 bands,
two-way entropy identity; 214 green assertions, machine-floor, cross-pinned four
artifacts) — worth writing up NOW, independent of the dead boundary claim; PLUS
**(iii) the β=0 global-correlation / Lieb-Robinson-irreducible separator** as a
sharply-scoped anti-relabel EXHIBIT (200 proper-subset marginals identical, full
joint TD=0.494872, every fragment Holevo exactly 0, verdicts flip).
- **Backing personas:** Experimentalist (54) and Phil-Phys (25) give the sharpest
  honest verdicts (as tasked): Phil-Phys frames it as the DO/SEE dissociation
  (capability ≠ observability) instantiated; Experimentalist frames it as a
  methods-note + executable exhibit. QI (8) and Math-Phys (1) concur, scoped to
  "toolkit + one structural exhibit."
- **Is it worth a paper?** Split verdict, honestly: the **toolkit/calibration
  note is paper-worthy and safe** (consensus, ~8/10). The **separator-as-result
  is worth a SHORT paper ONLY at the β=0 corner and ONLY if it survives
  region-widening** (the joint-record-completion / co-present-retained-register
  hostile test) — at β=∞ the T401 kill removes it (retained record readable,
  P=0.4286 vs 0). Net: 6/10 the pair clears the bar; 2/10 any physical-boundary
  claim survives.
- **Confidence range:** 6–8/10 (real content) / 2/10 (physical boundary).
- **Dissent/empty:** Phil-Phys explicitly NARROWS the DO/SEE dissociation to the
  single β=0 corner (empty at β=∞) — recorded as the method working. The
  general "capability ≠ observability" theorem did NOT survive; only the
  single-corner exhibit did.

### Empty / shrunk syntheses (recorded honestly)

- **U1 absolute physical-boundary criterion:** NO finite-closed-model repair
  survives (Phil-Phys synthesis potentially EMPTY; QF repair backfires).
- **U2 physical-completion-block:** DEAD — joint-record completion + wait-longer
  unrefuted in any closed model.
- **U3 residue beyond translation:** thin-to-empty if Petz/decoupling dictionary
  is complete.
- **U4 general DO/SEE theorem:** SHRANK to a single-corner (β=0) exhibit.
- **Sharp physical wall (all uncertainties):** DEAD across the cluster; the
  honest ceiling everywhere is a *soft, resource/cost-indexed, reach-priced*
  boundary — which is the resource-theory absorber the program already partially
  conceded.
