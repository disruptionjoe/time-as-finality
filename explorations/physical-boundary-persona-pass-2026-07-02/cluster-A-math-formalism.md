---
document_type: persona_panel_exploration
primary_reader: agents
read_pattern: current_state
write_pattern: append_only
authority: exploratory
status: exploratory
created: 2026-07-02
cluster: A-math-formalism
personas: [2, 5, 6, 10, 11, 14, 15, 23, 24, 26, 37, 47, 52]
---

# Cluster A — Math / Formalism Persona Pass (Physical-Boundary Discriminator)

Method, not evidence. Convergence here is one process wearing masks; it generates
targets, never support. Physics/math attributions from memory are flagged. No
claim moves. Shrinkage and EMPTY syntheses are recorded as the method working.

Structure per persona: for each of U1–U4, a compact Phase-1 steelman (statement /
support / hidden assumptions / vindication / kill / confidence 1–10), then a
Phase-2 Hegelian pass (thesis / antithesis / synthesis). U1 antitheses face the
finite-closed-model objection; U2 antitheses face joint-record completion.

---

## 2. Category Theorist

### U1 — meaning of "physical rather than declared"
- **Steelman.** A boundary is physical iff it is the carrier of a *universal
  construction* over the dynamics — e.g. the coequalizer/quotient forced by the
  interaction morphisms — rather than an arbitrarily chosen subobject (mono) of
  the state object. "Declared subset" is precisely a non-canonical mono; a
  physical boundary must be determined up to unique iso by a universal property,
  hence agent-independent.
- **Support.** Universal constructions are stable under equivalence of
  categories; a subset that only exists because someone picked an inclusion is
  not. The kill history is exactly "we keep finding chosen monos."
- **Hidden assumptions.** That the model organizes into a category whose
  morphisms are the *only* admissible operations; that a relevant universal
  construction exists and is non-degenerate.
- **Vindication.** Exhibit the R→R+ cut as a colimit/coequalizer of the coupling
  diagram, invariant under the automorphisms of that diagram.
- **Kill.** Show the construction has a terminal object (the full closed state)
  through which every cut factors, collapsing universality to "pick a mono."
- **Confidence.** 4.
- **Thesis.** Physical = universal, not chosen.
- **Antithesis (finite closed model).** A finite closed unitary model is a
  category with a terminal/zero object: the whole state is co-present and every
  proper region is a chosen mono into it. Unitarity makes the dynamics an
  automorphism, so any "quotient" is reversible and the coequalizer is trivial.
  The universal object is the whole — the boundary is a non-canonical inclusion,
  the declared subset the kill already named.
- **Synthesis (SHRINKS).** Universality does not survive as a *sufficient*
  criterion in a closed unitary category. What survives is a weaker hygiene
  condition: **naturality/functoriality** — a candidate boundary that is not
  natural under the dynamics-morphisms is *definitely* declared. Necessary, not
  sufficient. Use it as a filter, not a certificate.

### U2 — transport rung as next fixture
- **Steelman.** Model reach as the image of a composite of coupling morphisms;
  "reach derived from the interaction graph" = the subobject *generated* by the
  span of couplings, which is canonical given the graph.
- **Support.** A generated subobject is functorial in the graph; changing the
  clock/relabeling acts by natural transformation, so the frontier is covariant.
- **Hidden assumptions.** Couplings compose cleanly; no hidden global morphism
  re-linking regions.
- **Vindication.** Frontier r(n) equals the rank/image of the composite span,
  computed identically under every automorphism.
- **Kill.** A retained back-morphism (copy) means the "generated" subobject is a
  proper part of a larger canonical co-present object.
- **Confidence.** 4.
- **Thesis.** Reach = canonical generated subobject.
- **Antithesis (joint-record completion).** If any carrier is copied and
  retained, the co-present object is the *product* of reached and retained
  factors; the generated subobject is again a chosen mono into that product, and
  a projection onto the retained factor separates the states. Joint-record
  completion re-instates the terminal-object collapse.
- **Synthesis.** Survives ONLY if transport is a *move* (iso relocating the
  factor) not a *copy* (diagonal) — i.e. no retained clone, enforced
  categorically by absence of a diagonal (no natural Δ). Verdict: **REDESIGN**
  around move-not-copy; without it, EMPTY.

### U3 — literature adjacency
- **Steelman.** Recovery is a right-adjoint/section to the coarse-graining
  functor; Hayden-Preskill/Petz recovery is the categorical section problem
  "when does the restriction functor admit a section on this object."
- **Support.** Recoverability = existence of a section; failure = obstruction to
  a section — clean, composable framing.
- **Hidden assumptions.** The recovery map is a morphism in the same category.
- **Vindication.** Cast Petz recovery as the adjoint and show the frontier is the
  point where the adjunction counit stops being iso.
- **Kill.** The adjoint always exists (approximately), making the boundary a
  quantitative not structural fact.
- **Confidence.** 5.
- **Thesis/Antithesis/Synthesis.** Thesis: boundary = failure of a section.
  Antithesis: approximate sections always exist (Petz is universal), so the cut
  is graded, not binary. **Synthesis:** keep "obstruction-to-section" as the
  right language for U3, but it delivers a *graded* frontier, reinforcing
  threshold-not-wall.

### U4 — fallback
- **Steelman.** Even absent a physical boundary, the surviving asset is a
  *natural transformation that has no local components* — the global correlation
  living in no proper subobject is a non-representable functor, a real invariant
  worth publishing as "a separator with no local section."
- **Support.** Non-representability is basis/relabel independent; it is exactly
  what the Lieb-Robinson relabel cannot express.
- **Hidden assumptions.** The correlation is genuinely global, not an artifact of
  a chosen product decomposition.
- **Vindication.** Prove the separator functor has no local representation across
  all admissible decompositions.
- **Kill.** A decomposition in which it localizes.
- **Confidence.** 6.
- **Synthesis.** Fallback (iii) reframed categorically survives and is clean.

---

## 5. Algebraic Topologist

### U1 — meaning of "physical rather than declared"
- **Steelman.** A boundary is physical iff it carries a **nonzero obstruction
  class** — a relative/Čech cohomology class that no choice of local trivialization
  (declaration/gauge) can kill. "Declared subset" is a coboundary: removable by a
  local section. Physical = a nontrivial class with no global section.
- **Support.** The T411 surviving residue — a discriminating datum present in NO
  proper subset of the reach — is literally "no local section, nonzero global
  class." Cohomology is the native language of local-to-global obstruction.
- **Hidden assumptions.** The data organize as a (pre)sheaf with a well-defined
  cohomology; the class is computed over the *physical* cover, not a declared one.
- **Vindication.** Compute a nonzero H^1 (or gerbe/H^2) for the correlation over
  the reach-cover, invariant under refinement.
- **Kill.** Show the class is a coboundary once the retained carriers are added to
  the cover — i.e. trivial on the true co-present cover.
- **Confidence.** 6.
- **Thesis.** Physical = nonzero obstruction class, no global section.
- **Antithesis (finite closed model).** Over a finite closed model the "full"
  cover is contractible/acyclic: unitarity means the global state is a section
  through everything, so H^* over the co-present cover vanishes and the class you
  computed was an artifact of an incomplete (declared) cover. The kill —
  "equality region is a declared subset of the co-present set" — is exactly
  "your cover omitted the retained carriers, faking a nonzero class."
- **Synthesis (SURVIVES, conditional).** The obstruction survives as physical
  ONLY if the cover is *forced by the dynamics* (open cover = actually reachable
  patches), not stipulated. Then a nonzero class over the reachable cover is
  meaningful even though the full cover is acyclic — the point is that the agent
  cannot access a trivializing section. This is the **best-formalized U1 repair
  in the cluster**: physical boundary = obstruction relative to the
  dynamics-forced cover. It converts "declared subset" into a testable
  cohomological triviality check.

### U2 — transport rung
- **Steelman.** Transport gives a genuinely dynamics-forced open cover (patches =
  causally-reachable sets), so the obstruction class of U1 becomes computable and
  non-artifactual.
- **Support.** The cover is now derived, killing the "you chose the cover"
  objection at the source.
- **Hidden assumptions.** Reachable patches form a good cover; no retained clones
  re-acyclify it.
- **Vindication.** Nonzero class over the reachable cover that becomes a
  coboundary the moment retained carriers are re-included — and the retained
  carriers are provably *not* reachable.
- **Kill.** Retained carriers are reachable (copies), trivializing the class.
- **Confidence.** 6.
- **Thesis.** Transport → honest cover → real obstruction.
- **Antithesis (joint-record completion).** A retained copy adds a patch to the
  *co-present* cover; the class becomes a coboundary there. Joint-record
  completion = "your good cover wasn't the whole space." The separating
  Z-measurement is a section over the retained patch.
- **Synthesis.** Survives iff transport is move-not-copy so the retained patch is
  genuinely absent from the co-present cover. Verdict **GO-conditional /
  REDESIGN**: the transport rung is the *right* fixture to make the cover honest,
  but only pays off under strict no-retained-clone dynamics. Strongest GO voice
  in the cluster, still conditional.

### U3 — literature adjacency
- **Steelman.** Anomaly-inflow / bulk-boundary is a cohomological
  statement; scrambling-recovery obstructions are computable as the failure of a
  decoupling cochain. The horizon literature is where "boundary term forced by
  bulk class" already lives.
- **Support.** Index/anomaly language (shared with persona 47) gives a
  bulk-forced, not declared, boundary quantity.
- **Hidden assumptions.** The finite model admits a meaningful discrete analog of
  the inflow.
- **Vindication.** A discrete bulk invariant that forces the boundary correlation.
- **Kill.** No stable discrete analog; inflow needs the continuum.
- **Confidence.** 5.
- **Synthesis.** Adjacency real; borrow the *language* (obstruction/inflow),
  flag GU firewall resonance as stress-test only.

### U4 — fallback
- **Steelman.** The anti-relabel result *is* "a nonzero global class with no
  local representative" — a topological invariant of the correlation. Publish it
  as such: the separator is a cohomological obstruction a light-cone bound cannot
  express.
- **Support.** Relabel-invariant by construction; that is the whole point.
- **Vindication/Kill.** As U1. **Confidence.** 7.
- **Synthesis.** Fallback (iii) is the cluster's strongest survivor and this
  persona gives it its cleanest statement.

---

## 6. Representation Theorist

### U1 — meaning of "physical rather than declared"
- **Steelman.** A physical boundary is a **superselection boundary**: a charge /
  symmetry sector that no admissible (local, symmetric) operation can cross.
  "Declared subset" carries no conserved charge; a physical cut separates
  inequivalent irreps that local operations cannot interconvert. The T411
  U(1)-asymmetry relabel is a *feature*: asymmetry charge is exactly the
  candidate physical invariant.
- **Support.** Superselection is the textbook notion of a boundary that is not a
  matter of bookkeeping — you genuinely cannot rotate between sectors with the
  allowed operations.
- **Hidden assumptions.** A genuine symmetry with a conserved charge exists and
  is not just an emergent/approximate one.
- **Vindication.** Exhibit a conserved charge whose value differs across R→R+ and
  cannot be changed by any R-supported symmetric operation, even with work.
- **Kill.** Show the "charge" is changeable by an allowed operation (no true
  superselection) — i.e. it's an approximate/emergent asymmetry.
- **Confidence.** 4.
- **Thesis.** Physical boundary = superselection sector.
- **Antithesis (finite closed model).** Finite-dimensional closed systems have
  **no true superselection rules** — they are emergent only in the
  thermodynamic/infinite limit (from memory, standard folklore: superselection is
  exact only for infinite systems / type-III algebras). In finite dimensions any
  sector boundary is broken by a suitable (possibly work-costly) unitary, so the
  charge is convertible and the boundary is again declared.
- **Synthesis (SHRINKS toward EMPTY).** No exact superselection in finite closed
  models. What survives: *approximate* asymmetry monotones whose interconversion
  cost grows with system size — a resource-monotone reading, not a physical wall.
  This collapses into the resource-theory absorber (persona 23). Physical-boundary
  synthesis here is **near-EMPTY**; only a size-scaling cost survives.

### U2 — transport rung
- **Steelman.** Transport under a symmetric interaction preserves the charge; the
  reachable set is a union of orbits, canonically defined by the symmetry.
- **Support.** Orbit structure is invariant, not chosen.
- **Hidden assumptions.** The dynamics is genuinely symmetric; charge is exactly
  conserved along transport.
- **Vindication.** A conserved charge that separates A/B and is carried away by
  transport beyond R.
- **Kill.** Retained charged carrier inside the co-present set.
- **Confidence.** 4.
- **Thesis.** Reach = symmetry orbit.
- **Antithesis (joint-record completion).** The retained tier-1 carrier still
  holds the charge; a symmetric measurement on it separates A/B. Orbits do not
  help if a charged copy stays co-present.
- **Synthesis.** Same as U1: survives only under move-not-copy so no charged
  clone is retained; otherwise EMPTY.

### U3 — literature adjacency
- **Steelman.** Scrambling delocalizes charge across many modes; recovery
  requires a symmetric decoder acting on the full orbit — natural home is
  symmetry-resolved scrambling / charged Hayden-Preskill (from memory).
- **Confidence.** 4.
- **Synthesis.** Adjacency plausible but thin; representation theory contributes
  the *charge-resolved* refinement, not a boundary.

### U4 — fallback
- **Steelman.** The honest deliverable is an **asymmetry-monotone frontier**:
  work (symmetric free ancillas) cannot buy reach because reach carries an
  asymmetry charge work cannot supply — a clean resource-theoretic statement.
- **Confidence.** 6.
- **Synthesis.** Feeds fallback (ii); real but is the absorber, not an escape.

---

## 10. Formal Methods Researcher

### U1 — meaning of "physical rather than declared"
- **Steelman.** Operationalize the distinction exactly: **physical = derivable in
  the operational semantics** of the closed model (a theorem of the transition
  relation); **declared = an axiom/annotation added on top** (e.g. the
  `prepare_retained` partial trace keyed on a stipulated set). A boundary is
  physical iff "no R-supported protocol realizes the task" is a *derivation* in
  the model, not a side condition. This is repair (d), protocol-impossibility,
  made machine-checkable.
- **Support.** Removes hand-waving: you either have a proof of impossibility from
  the transition rules or you have an annotation. The decoherence-bookkeeping kill
  is precisely "the cut is an annotation, not a derived step."
- **Hidden assumptions.** The operational semantics faithfully captures all
  admissible operations (the ALL quantifier); the menu M is complete.
- **Vindication.** A mechanized proof that no trace in the semantics, over the
  full R-menu, realizes the separation — with the reach set itself *derived* from
  the transition relation.
- **Kill.** The impossibility proof requires an extra axiom (the retained-set
  stipulation) to go through — then it's declared.
- **Confidence.** 6.
- **Thesis.** Physical = derivable impossibility; declared = required axiom.
- **Antithesis (finite closed model).** In a finite closed reversible semantics,
  *every* state is reachable from every other by some trace (unitarity =
  invertible transition relation). So "no protocol realizes the task" is FALSE
  unless you restrict the trace alphabet to R-only operations — and that
  restriction is the declaration. The impossibility is relative to a
  stipulated sub-alphabet, exactly the "declared subset" wound.
- **Synthesis (SHRINKS).** Protocol-impossibility is well-posed and checkable, but
  it is *always relative to a declared operation alphabet* in a closed model. It
  cannot make the alphabet itself physical. Survives as: **"physical = derivable
  impossibility relative to the dynamics-forced alphabet"** — pushing the burden
  onto U2 (does transport *derive* the alphabet from couplings?). Non-empty but
  dependent on U2.

### U2 — transport rung
- **Steelman.** The transport rung *derives the operation alphabet from the
  interaction graph*: available couplings = graph edges, time budget = trace
  length. This is the move that makes the sub-alphabet physical rather than
  stipulated — the alphabet is now a theorem of the model's wiring.
- **Support.** Directly answers the U1 antithesis: the restriction stops being an
  annotation and becomes a structural fact of the transition system.
- **Hidden assumptions.** The interaction graph is itself not a declaration
  (why these edges and not others?); the time budget bound is principled.
- **Vindication.** Mechanized reachability over the graph-derived transition
  system showing separation is underivable within budget, with reach = the
  graph's forward closure.
- **Kill.** A retained self-loop/copy edge keeps the separating carrier inside the
  forward closure.
- **Confidence.** 6.
- **Thesis.** Reach = graph-derived forward closure; alphabet now physical.
- **Antithesis (joint-record completion).** Model-checking the FULL co-present
  state: if the dynamics copied the record (retained tier-1), the separating
  carrier is inside the forward closure at time 0 and stays reachable — a
  one-qubit measurement (the derived Z-check) separates A/B. Reachable set is
  still a declared subset of co-present unless the graph *forbids* retention.
  Joint-record completion becomes "your transition system retained a copy."
- **Synthesis.** GO **only** with a verified no-retained-copy invariant on the
  transition system (linear/affine discipline, persona 37). Then reach ⊊
  co-present is a *derived* fact, not a declaration. Verdict: **REDESIGN → GO**
  contingent on a machine-checkable "record is moved not copied" invariant. This
  persona gives the sharpest actionable spec.

### U3 — literature adjacency
- **Steelman.** Recovery maps are decoders; Hayden-Preskill is a decodability
  theorem. Import it as a *soundness/completeness* pair: complete = recovery
  exists (Petz), sound = no R-decoder exists. The frontier is where completeness
  fails for R but holds for R+.
- **Confidence.** 5.
- **Synthesis.** Borrowable as decidability of decoding; delivers a graded/
  resource-indexed frontier, consistent with threshold-not-wall.

### U4 — fallback
- **Steelman.** Ship the **certificate toolkit as verified calibration
  machinery** (fallback i): the φ-independence certificate, the channel lemma
  `B=(id⊗Λ)(A)`, and the ALL-quantifier discharge are reusable, mechanized
  artifacts independent of the physical-boundary framing.
- **Confidence.** 7.
- **Synthesis.** Fallback (i) is solid and this is its natural owner — real,
  publishable, honest about scope.

---

## 11. Programming Languages Theorist

### U1 — meaning of "physical rather than declared"
- **Steelman.** A physical boundary is a **parametricity barrier**: by a free
  theorem, any R-supported observer factors through an abstraction under which the
  two states are *observationally equivalent*, and this is forced by the type of
  the observer, not by a chosen hidden field. The channel lemma
  `B=(id_R⊗Λ_E)(A)` IS a parametricity/representation-independence statement.
  "Declared" = a phantom distinction the type system erases.
- **Support.** Observational equivalence under all contexts is the gold standard
  for "genuinely indistinguishable"; it is exactly what the ALL quantifier wants.
- **Hidden assumptions.** The observer's type really quantifies over *all* R
  contexts including interventions; the abstraction boundary isn't itself an
  arbitrary module signature.
- **Vindication.** A logical-relations proof that A ≃ B at type "R-observer" for
  every R-context, breaking only at an R+-typed context.
- **Kill.** A well-typed R-context that distinguishes them (a retained field the
  type didn't actually hide).
- **Confidence.** 5.
- **Thesis.** Physical = parametric indistinguishability; declared = phantom type.
- **Antithesis (finite closed model).** Abstraction boundaries are *declared* —
  a module signature is a choice. In a finite closed model the "hidden"
  representation is fully present in the global state; the retained tier-1 carrier
  is a public field the signature merely *pretended* to hide. Parametricity over a
  falsely-restricted signature is vacuous — the kill is "your abstraction leaked a
  retained field."
- **Synthesis (SHRINKS).** Observational equivalence survives as the correct
  *statement* of R-indistinguishability, but "physical" requires the signature
  (which fields are private) to be dynamics-enforced, not declared. Survives as a
  necessary condition + a demand that the abstraction boundary be backed by an
  operational no-access theorem (→ U2 transport, → linearity persona 37).

### U2 — transport rung
- **Steelman.** Transport enforces information hiding *operationally*: the record
  is passed by linear channel out of R, so no well-typed R-context can observe it
  — hiding backed by dynamics, not by a signature.
- **Support.** Turns a declared `private` into an operationally enforced one.
- **Hidden assumptions.** No aliasing/retained reference to the transported value.
- **Vindication.** Logical-relations proof of A ≃ B for all R-contexts where the
  hiding is a theorem about the transport channel.
- **Kill.** An alias (retained copy) — a live reference into the "hidden" value.
- **Confidence.** 5.
- **Thesis.** Transport = operationally enforced hiding.
- **Antithesis (joint-record completion).** A retained alias defeats information
  hiding: the joint record is a live reference, and a context reading it
  distinguishes A/B. Joint-record completion = "hidden value still aliased."
- **Synthesis.** Requires *linear/affine* discipline (no aliasing = no retained
  clone). Same convergence: move-not-copy. REDESIGN around linearity.

### U3 — literature adjacency
- **Steelman.** Recovery = a coercion/decoder; Hayden-Preskill = "the value is
  still typeable at R+ but the coercion needs the scrambled context." Natural
  framing: representation-independence that holds at R, fails at R+.
- **Confidence.** 4.
- **Synthesis.** Language framing is illustrative, not load-bearing here.

### U4 — fallback
- **Steelman.** The reusable deliverable is the **channel-lemma / logical-relations
  method** for discharging an ALL-quantifier over interventions — a
  parametricity technique for capability claims, valuable regardless of the
  physical-boundary verdict.
- **Confidence.** 6.
- **Synthesis.** Complements fallback (i); a methods contribution.

---

## 14. Complexity Theorist

### U1 — meaning of "physical rather than declared"
- **Steelman.** Recasting: a boundary is physical iff crossing it is not merely
  *possible-in-principle* but **resource-hard** — recovery exists (unitarity) yet
  demands super-polynomial time/work/ancilla in system size. Repair (b)
  entropy-priced permanence generalized to *complexity-priced* permanence. The
  distinction "declared vs physical" becomes "free vs
  computationally-infeasible-to-cross."
- **Support.** This is how black-hole information is actually rescued: the record
  is recoverable but only after scrambling time / with exponential resources
  (from memory, Hayden-Preskill + computational-complexity of recovery, Harlow-
  Hayden flavor). A complexity wall is a real, relabel-stable boundary.
- **Hidden assumptions.** A meaningful asymptotic family exists (n→∞); the cost
  measure is robust; "feasible" is well-defined for the agent.
- **Vindication.** A family where R-recovery cost grows super-polynomially in n
  while R+-recovery stays efficient — a provable complexity separation.
- **Kill.** Efficient R-recovery exists (the separation collapses), or the gap is
  an artifact of a single fixture with no asymptotics.
- **Confidence.** 5.
- **Thesis.** Physical = complexity-priced permanence.
- **Antithesis (finite closed model).** Complexity separations are *asymptotic*;
  a single finite fixture has no complexity content — every finite instance is
  O(1) to crack. The finite-witness house style is structurally unable to host a
  complexity wall, and a fixed r(n)=n frontier is a counting statement, not a
  hardness one. In-principle recoverability (unitarity) means the finite boundary
  is again bookkeeping.
- **Synthesis (SHRINKS, redirects).** The physical boundary is *not* well-posed
  as a binary in a finite closed model, but it MAY be well-posed as an
  **asymptotic complexity threshold**. This demands abandoning the single-fixture
  house style for a fixture *family*. Survives conditionally as a research
  redirection: "physical = a proven complexity/entropy scaling gap," not a
  one-shot certificate. Real but expensive; changes the program's shape.

### U2 — transport rung
- **Steelman.** Transport gives the missing asymptotic knob: reach vs time budget
  is a resource-parameterized family; the frontier r(n) can carry genuine
  complexity content (scrambling time ~ log n or poly n).
- **Support.** Converts "wait-longer" from an objection into the *independent
  variable* of a complexity statement.
- **Hidden assumptions.** The family is uniform; scrambling time is well-defined.
- **Vindication.** R-recovery cost super-poly until t ≥ t_scramble, efficient at
  R+ — a decoupling/complexity threshold.
- **Kill.** Reach grows so gently that no super-poly gap ever opens.
- **Confidence.** 5.
- **Thesis.** Transport frontier = complexity threshold.
- **Antithesis (joint-record completion).** If a copy is retained, R-recovery is
  *trivially efficient* (measure the retained carrier) — no hardness at all. The
  complexity wall requires the record to be genuinely scrambled beyond R with no
  cheap retained handle. Joint-record completion = "there's an efficient decoder
  you ignored."
- **Synthesis.** GO **as a family, not a fixture**, and only with no-retained-
  copy transport into a scrambling reservoir. Then wait-longer is the axis and
  the boundary is a hardness threshold. Verdict: **REDESIGN** toward an asymptotic
  family; ABANDON the single-witness framing for this purpose.

### U3 — literature adjacency
- **Steelman.** Direct hit: Hayden-Preskill + computational complexity of the
  recovery map (Harlow-Hayden-style hardness) is the exact home of a
  dynamically-forced, complexity-priced information boundary.
- **Support.** They already prove "recoverable but infeasible" — the precise shape
  of the repair.
- **Hidden assumptions.** Transferability of continuum/large-N results to finite
  discrete fixtures (from memory, unverified).
- **Vindication.** A finite-family analog of Harlow-Hayden hardness for R-recovery.
- **Kill.** No finite analog; the hardness is essentially large-N.
- **Confidence.** 6.
- **Synthesis.** Strongest adjacency in the cluster alongside persona 47/24:
  borrow decoupling + recovery-hardness. Flag GU firewall resonance, do NOT cite.

### U4 — fallback
- **Steelman.** If no hardness gap materializes, the honest fallback is that the
  boundary is a **resource threshold, explicitly named as such** — the
  work-does-not-buy-reach frontier (ii) is a monotone/cost statement, not a wall.
- **Confidence.** 6.
- **Synthesis.** Feeds fallback (ii). Also cautions: the whole physical-boundary
  claim may only ever be a complexity statement, which the finite house style
  cannot certify — a structural limit worth stating in the paper.

---

## 15. Infinite Models Theorist

### U1 — meaning of "physical rather than declared" (THE finite-closed-model seat)
- **Steelman.** The honest model-theoretic position: a genuinely non-declarable
  boundary — one not definable as a subset by the agent's parameters — is
  **well-posed only in an infinite model** (thermodynamic limit, type-III von
  Neumann algebra, Reeh-Schlieder). There, local algebras have no minimal
  projections and no perfectly localized records exist, so localization scales can
  be *forced* rather than declared. In any finite closed model, compactness of the
  state space + unitarity make every region a first-order-definable subset of a
  co-present whole. Physicality of the boundary = **failure of implicit
  definability** (Beth): the boundary is physical iff it is NOT implicitly
  definable from the agent's accessible relations.
- **Support.** The kill history is a theorem, not bad luck: "every equality region
  is a declared subset" is what Beth definability *predicts* for finite models —
  anything invariant is definable, anything non-definable is not invariant. The
  Reeh-Schlieder routed lead is the correct literature.
- **Hidden assumptions.** That the infinite structure is the *intended* model and
  the finite fixtures are approximations, not the ontology; that type-III behavior
  is physically operative at the agent's scale.
- **Vindication.** A limit in which the R-algebra has no minimal projection
  separating A/B while the R+-algebra does — a definability jump surviving the
  n→∞ limit and absent at every finite n.
- **Kill.** The definability gap closes in the limit too (the boundary stays
  declared even at infinity), OR the finite fixtures are shown to already capture
  it (no need for infinity).
- **Confidence.** 6.
- **Thesis.** Physical boundary is a non-definability fact, native to infinite
  models.
- **Antithesis (finite closed model).** House style *requires* finite witnesses.
  If the phenomenon only exists at infinity, then within the program's own rules
  the boundary is *unprovable* and every finite fixture will (correctly) show a
  declared subset. The three deaths are not accidents — they are the finite model
  telling the truth. One cannot smuggle a type-III fact into a finite Hilbert
  space; the "physical boundary" is then, in-house, bookkeeping all the way down.
- **Synthesis (HONEST, largely NEGATIVE).** The two are reconcilable only by
  admitting scope: **in finite closed models the physical-boundary criterion is
  NOT well-posed** (Beth: definable ⇒ declared). It becomes well-posed only in an
  infinite/limit model the house style forbids. Surviving positive content:
  reframe the target as a *definability jump across a limit*, or accept U4. This
  persona is the cluster's clearest voice that U1 has **no finite repair** — the
  physical claim shrinks to "well-posed only at infinity."

### U2 — transport rung
- **Steelman.** Transport with a time budget is a natural *directed family* whose
  limit (unbounded budget, n→∞) can host the definability jump finite fixtures
  cannot; the finite rungs approximate the limit and can *bracket* it.
- **Support.** Even if each finite rung shows a declared subset, a monotone trend
  in the definability gap across rungs is evidence about the limit.
- **Hidden assumptions.** The limit exists and is the intended object; the trend
  is not an artifact.
- **Vindication.** A definability gap that provably *does not close* as n→∞ along
  the transport family.
- **Kill.** The gap closes in the limit (wait-longer wins) — boundary is a
  resource threshold, not a wall.
- **Confidence.** 5.
- **Thesis.** Transport family brackets an infinite-model definability jump.
- **Antithesis (joint-record completion).** At every finite rung the retained
  carrier keeps the boundary a declared subset; joint-record completion holds at
  all finite n. The claim then rests entirely on an *unobserved* limit — exactly
  the extrapolation the house style distrusts.
- **Synthesis.** REDESIGN as a family with an explicit limit argument, or ABANDON
  the finite-witness ambition. Honestly: transport does not escape joint-record
  completion at any finite rung; it can only argue about the limit, which is
  out-of-house. Verdict leans **ABANDON-in-house / REDESIGN-as-limit-study**.

### U3 — literature adjacency
- **Steelman.** Reeh-Schlieder + type-III algebras + horizon thermodynamics are
  the correct home: no localized records, cyclic-separating vacuum, and a
  physically-forced localization scale. Hayden-Preskill lives on top of this.
- **Support.** This is where "no perfectly localized record" is a theorem, not a
  declaration.
- **Confidence.** 6.
- **Synthesis.** Strong literature adjacency; but it is *literature-shaped*, and
  finite house style cannot model type-III — cite as direction, not support.
  Flag GU firewall resonance as stress-test only.

### U4 — fallback
- **Steelman.** The honest fallback is to state the **scope limit as a result**:
  "within finite closed models the physical/declared boundary is provably a
  definability artifact; a non-declarable boundary requires infinite structure."
  That is a genuine no-go about the *program's own reach*, plus the calibration
  toolkit (i) and anti-relabel separator (iii) as finite deliverables.
- **Confidence.** 7.
- **Synthesis.** Fallbacks (i)+(iii) plus an explicit scope theorem. This persona
  argues the scope theorem is itself the most valuable honest output.

---

## 23. Resource Theory Researcher (the absorber's own seat)

### U1 — meaning of "physical rather than declared"
- **Steelman.** Give the strongest *constructive* resource-theoretic reading: a
  boundary is physical iff it is the **free/non-free cut of a resource theory
  whose free operations are themselves dynamically forced** — not chosen. If the
  free operations are exactly "what the couplings + budget permit" (not a
  stipulated menu), then the monotone structure is physical and the R→R+ cut is
  the boundary of free convertibility.
- **Support.** Resource theories already express "work cannot buy reach" as
  free-ancilla monotonicity; if the free set is derived, the monotone is a
  physical fact.
- **Hidden assumptions.** The free-operation set is dynamically forced, not
  declared — the crux the absorber exploits.
- **Vindication.** A monotone that separates A/B and is provably non-increasing
  under the dynamics-forced free operations, strictly increasing only across R+.
- **Kill.** The free-operation set is a choice; then the monotone gap is an
  artifact of that choice (the T398 kill).
- **Confidence.** 4.
- **Thesis.** Physical = free/non-free cut with dynamically-forced free set.
- **Antithesis (finite closed model).** The defining move of resource theory is
  to *declare* the free operations. That declaration IS the boundary — this is
  precisely the sole-survivor concession the artifacts already make ("adopted, not
  derived"). In a finite closed model every operation is unitarily invertible, so
  "free" cannot be forced by physics; it must be stipulated. Resource theory
  therefore *cannot* supply a physical boundary — it presupposes one.
- **Synthesis (EMPTY on the physical claim).** Honestly EMPTY. Resource theory
  formalizes the boundary beautifully but always *takes the cut as input*. It
  cannot derive physicality; it can only relabel a declared cut as a monotone.
  Recorded as the method working: the resource-theoretic U1 synthesis is empty by
  construction. The value of RT is entirely downstream (U4).

### U2 — transport rung
- **Steelman.** Transport is the one design where the free set could be *derived*:
  free ops = graph-local couplings within budget. This is the honest attempt to
  fix RT's declared-free-set problem by grounding it in dynamics.
- **Support.** If reach = graph closure, the free monotone is dynamics-forced, not
  chosen — the strongest possible answer to the T398 absorber.
- **Hidden assumptions.** Graph and budget are not themselves declarations.
- **Vindication.** A monotone non-increasing under graph-local free ops, gapped at
  R+, with the free set provably = the coupling structure.
- **Kill (joint-record completion).** Retained carrier ⇒ the "free" ops already
  include reading it ⇒ monotone gap vanishes. If any record is retained
  co-present, RT's free set silently contains the separating operation and the
  boundary evaporates.
- **Confidence.** 4.
- **Thesis.** Transport → dynamically-forced free set → physical monotone.
- **Antithesis (joint-record completion).** Same as kill: joint-record completion
  means the co-present retained carrier is *free to read*, so the monotone does
  not separate. The reachable set being a declared subset of co-present = the free
  set being a declared subset of what's actually free.
- **Synthesis.** Survives ONLY if transport provably retains no co-present copy —
  move-not-copy again. Even then RT gives a *monotone*, i.e. a resource threshold,
  not a wall (wait-longer raises reach). Verdict: **REDESIGN** for move-not-copy;
  expect the deliverable to be a frontier/threshold, not a physical boundary.
  Load-bearing honest read: RT will relabel any transport result as a monotone —
  the physical wall is not in RT's vocabulary.

### U3 — literature adjacency
- **Steelman.** Dynamical resource theories of channels (T404's named candidate)
  + resource theory of asymmetry/athermality are the home; Hayden-Preskill
  recovery is channel-resource non-freeness.
- **Confidence.** 5.
- **Synthesis.** Adjacency real and it is *absorptive*: the literature exists to
  relabel the result as a channel monotone. Borrowable, but it demotes the
  residue to translation (the T404 warning).

### U4 — fallback
- **Steelman.** The cluster's cleanest fallback owner: **"work does not substitute
  for reach" as a genuine resource-theory contribution (ii)** — a temperature-blind
  integer frontier r(n)=n where free work/ancillas cannot raise reach is a real
  monotone-separation result, publishable without any physical-boundary claim.
- **Support.** Survives every absorber because it *is* the absorbed form; it is
  true as stated.
- **Confidence.** 7.
- **Synthesis.** Fallback (ii) is solid and honest. RT's role: kill the physical
  boundary (U1 EMPTY), keep the frontier (U4 strong).

---

## 24. Constructor Theory Researcher

### U1 — meaning of "physical rather than declared"
- **Steelman.** Constructor theory is built to make this distinction: state
  physics as **which transformations are possible/impossible**, not as dynamics +
  initial conditions. A physical boundary = a genuine **impossibility** — no
  constructor with the R-repertoire can perform the R→R+ task — expressed
  substrate-independently and *counterfactually*, not as a chosen partition. "The
  task is impossible for any constructor confined to R" is not a declared subset
  if "confined to R" is itself given by an impossibility (a coupling no
  R-constructor can instantiate).
- **Support.** Counterfactual impossibility statements are relabel-proof by design
  and do not reference a chosen region — they reference what *cannot be built*.
  This is repair (d) in its most principled form.
- **Hidden assumptions.** "Confined to R" is itself a genuine impossibility, not a
  declaration; the task and substrates are well-specified counterfactually.
- **Vindication.** A proof that the R→R+ task is impossible for every constructor
  built from R-couplings, while possible with an R+-coupling — the confinement
  itself an impossibility.
- **Kill.** The confinement is a declaration (an R-constructor *could* be built to
  cross it with allowed resources), collapsing impossibility to choice.
- **Confidence.** 5.
- **Thesis.** Physical = counterfactual impossibility for a forced repertoire.
- **Antithesis (finite closed model).** In a finite closed *unitary* model every
  transformation is possible in principle (invertibility), so the only
  impossibilities are relative to a *stipulated* repertoire — and stipulating the
  repertoire is the declaration. Worse, the Hayden-Preskill adjacency says the
  task IS possible at R++ under an identical forward unitary; a transformation
  that is merely *costly/delayed* is **possible**, not impossible, so constructor
  theory classifies it as possible-with-resources — no physical boundary. The kill
  ("declared subset") reappears as "declared repertoire."
- **Synthesis (SHRINKS).** Constructor theory sharpens the target — "physical =
  impossible, not just costly" — and thereby *raises the bar the artifacts fail*:
  because recovery is possible at R++, the boundary is NOT a constructor-theoretic
  impossibility; it is a possible-but-priced task. Honest synthesis: constructor
  theory converts U1 into a demand for a *true* impossibility, which the finite
  closed model (unitary, hence everything-possible) cannot supply. Survives as a
  crisp negative diagnostic, not a repair.

### U2 — transport rung
- **Steelman.** Transport could manufacture a genuine impossibility: if the
  record is propagated into a region the R-constructor provably cannot couple to
  within budget, then "recover at R" is counterfactually impossible — not
  declared, because the confinement is a coupling the agent cannot build.
- **Support.** Turns confinement from a stipulation into an interaction-graph
  impossibility.
- **Hidden assumptions.** The agent genuinely *cannot* build the crossing coupling
  (not merely chooses not to); no retained handle.
- **Vindication.** Impossibility of R-recovery within budget that is invariant
  under all R-constructors, plus provable non-retention.
- **Kill (joint-record completion).** A retained co-present carrier means an
  R-constructor *can* recover by reading it — recovery is possible, so no
  impossibility. Joint-record completion directly refutes the impossibility claim.
- **Confidence.** 5.
- **Thesis.** Transport-forced confinement = genuine impossibility.
- **Antithesis (joint-record completion).** Retention makes the task possible at R;
  and even without retention, "wait longer / build a bigger constructor" makes it
  possible at R+, so the impossibility is budget-relative, i.e. a possibility with
  a resource cost — not a constructor-theoretic wall.
- **Synthesis.** Only a *budget-indexed* impossibility survives ("impossible
  within budget T"), which is a resource threshold, not an unconditional
  impossibility. Verdict: **REDESIGN** toward move-not-copy; but constructor
  theory's honest verdict is that a *strict* impossibility will not appear —
  expect "impossible-within-budget," which is possibility-with-cost. Leans
  REDESIGN with low expectation of a hard wall.

### U3 — literature adjacency
- **Steelman.** Constructor theory of information + Hayden-Preskill: recovery
  possibility/impossibility is exactly a constructor-theoretic (im)possibility
  statement; scrambling sets when recovery-constructors exist.
- **Confidence.** 5.
- **Synthesis.** Genuine conceptual adjacency (both traffic in possible/impossible
  transformations); borrow the framing. But the horizon result is
  recovery-*possible*-after-scrambling, which undercuts a strict boundary. Flag
  GU firewall resonance; do not cite.

### U4 — fallback
- **Steelman.** The honest constructor-theoretic fallback: report the
  **possibility/impossibility frontier as budget-indexed** — "the R→R+ task is
  impossible within budget T(n) and possible beyond," a substrate-independent
  counterfactual frontier (overlaps ii and the escape-velocity result T409).
- **Confidence.** 6.
- **Synthesis.** Feeds fallback (ii)/T409; a counterfactual-frontier contribution,
  not a physical wall.

---

## 26. Philosophy of Mathematics Researcher

### U1 — meaning of "physical rather than declared"
- **Steelman.** Structuralism gives the sharpest criterion: a property is
  *structural* iff invariant under all **isomorphisms/automorphisms** of the
  model; a "declared subset" is a non-structural add-on that a relabeling
  (automorphism) can move. So: **a boundary is physical iff it is fixed by the
  automorphism group of the model** (equivalently, definable without ad hoc
  parameters). This is the rigorous meaning of "not bookkeeping": bookkeeping =
  parameter-dependent = automorphism-movable.
- **Support.** It explains every death: a declared subset is exactly one an
  automorphism can shift, so it "turns out to be a declared subset of what's
  co-present" whenever the automorphism group is transitive on the co-present
  factors. The criterion is precise and testable.
- **Hidden assumptions.** The right automorphism group is the physical symmetry
  group (which operations count as "relabelings"); agent-relativity may need a
  *fixed* subgroup (automorphisms that also fix the agent).
- **Vindication.** A boundary invariant under Aut(model-with-agent-fixed) that
  separates A/B — a parameter-free definition.
- **Kill.** An automorphism (fixing the agent) that maps the boundary elsewhere or
  swaps A/B — proving it non-structural.
- **Confidence.** 6.
- **Thesis.** Physical = automorphism-invariant / parameter-free definable.
- **Antithesis (finite closed model).** In a finite closed model the automorphism
  group (the full unitary group modulo agent constraints) is typically large and
  transitive enough that the only invariant subsets are trivial (∅ / whole). So
  every nontrivial region is non-structural = declared. Convergent with persona 15
  (Beth definability): finite + closed ⇒ implicit-definable ⇒ declared. The
  criterion is well-posed but its verdict in finite closed models is *negative*.
- **Synthesis (SURVIVES as criterion, negative verdict).** The automorphism-
  invariance criterion is the **cluster's cleanest well-posedness answer to U1**,
  and it converges with 15 and 5. But applied to finite closed models it predicts
  the boundary is generically declared — vindicating the kill history as a
  theorem. Positive residue: a boundary invariant under the *agent-fixing
  subgroup* (not the full group) could still be structural relative to the agent
  — agent-relativity (repair a) reinstated as "structural w.r.t. the agent's
  stabilizer subgroup." Non-empty, precise, and the right frame for U1.

### U2 — transport rung
- **Steelman.** Transport fixes the agent's stabilizer subgroup concretely (the
  couplings the agent has); the boundary should be defined as invariant under that
  subgroup, and reach = the subgroup's orbit closure — a parameter-free definition
  relative to the agent.
- **Support.** Makes "agent-relative structural" operational.
- **Hidden assumptions.** The coupling-generated subgroup is the correct
  stabilizer; the graph is not itself a declaration.
- **Vindication.** A separator invariant under the coupling subgroup but not under
  the R+ subgroup.
- **Kill (joint-record completion).** The retained carrier is in the agent's
  stabilizer orbit (readable), so the separator is not invariant — it's movable by
  an operation the agent has. Joint-record completion = "the retained factor is
  inside the agent's own subgroup."
- **Confidence.** 5.
- **Thesis.** Reach = agent-subgroup orbit; boundary = subgroup-invariant.
- **Antithesis (joint-record completion).** If the retained carrier lies in the
  agent's reachable orbit, the boundary is not invariant under the agent subgroup
  either — declared even relative to the agent.
- **Synthesis.** Survives iff the retained carrier is provably *outside* the agent
  subgroup's orbit (move-not-copy, no reachable handle). Verdict: **REDESIGN** to
  make the stabilizer subgroup genuinely exclude the retained factor. Precise
  test: is the separator in the orbit of the coupling-generated subgroup?

### U3 — literature adjacency
- **Steelman.** The horizon/Reeh-Schlieder literature is where automorphism-
  invariant localization is discussed (modular automorphisms, Tomita-Takesaki);
  a philosophically robust notion of forced localization lives there.
- **Confidence.** 4.
- **Synthesis.** Conceptual home noted; out-of-house for finite fixtures.

### U4 — fallback
- **Steelman.** If no agent-relative structural boundary survives, the honest
  contribution is a **structuralist scope result**: "capability boundaries in
  finite closed models are non-structural (automorphism-movable) except relative
  to the agent's stabilizer subgroup" — a clarification of what the program can and
  cannot mean.
- **Confidence.** 6.
- **Synthesis.** Supports the persona-15 scope-theorem fallback + anti-relabel
  (iii). A definitional deliverable.

---

## 37. Type-System Designer

### U1 — meaning of "physical rather than declared"
- **Steelman.** A physical boundary must be **operationally load-bearing under
  subject reduction**: a typing distinction no well-typed reduction can erase.
  "Declared" = a *phantom type* / newtype wrapper with no runtime force (exactly
  `prepare_retained`'s trace flag). The candidate with real force is
  **linearity/affineness**: a linear type forbids duplication (no-cloning), so a
  record typed linear *cannot* be both retained and transported — the boundary is
  enforced by the type discipline, not annotated.
- **Support.** Linear types are the one place "you cannot copy this" is a theorem
  (progress + preservation), which is exactly the no-retained-clone condition
  every other persona keeps needing.
- **Hidden assumptions.** The physics genuinely enforces linearity (no-cloning at
  the record level); the menu M cannot silently duplicate.
- **Vindication.** A linear-typed record where well-typedness *proves* no retained
  copy co-exists with the transported one, so the R-marginal cannot separate A/B.
- **Kill.** A well-typed operation that duplicates the record (the type wasn't
  really linear) — retained + transported both live.
- **Confidence.** 5.
- **Thesis.** Physical = linearity-enforced non-duplication; declared = phantom
  type.
- **Antithesis (finite closed model).** The three deaths are all phantom-type
  bugs: the "boundary" was a wrapper the global state ignores; the retained tier-1
  carrier is precisely an *un-consumed copy*, i.e. the record was NOT treated
  linearly. In a finite closed model you can always inspect the global heap, so a
  phantom type erases — the kill is "your private field was public." Linearity
  helps only if the *whole* model, not just an annotation, is linear.
- **Synthesis (SURVIVES conditionally).** Linearity is a *genuine* mechanism to
  turn a declared boundary into an enforced one — it is the type-theoretic name for
  the move-not-copy condition every persona converges on. Survives as: "physical
  boundary requires a linear/affine discipline on the record such that retention
  and transport are mutually exclusive by type." Actionable and non-empty; it is
  the enforcement layer the cluster keeps demanding.

### U2 — transport rung
- **Steelman.** Transport under a linear discipline is exactly `move` semantics:
  the record is *consumed* at R and produced beyond R, so no retained copy is
  well-typed. This makes reach ⊊ co-present a *type theorem*, not a declaration —
  the direct fix for joint-record completion.
- **Support.** "Move not copy" is precisely linear/affine transport; type
  preservation guarantees no aliasing.
- **Hidden assumptions.** The physical SWAP is genuinely a move (no residual
  correlation left in R); tier-1 retention is disallowed by the model, not just
  unused.
- **Vindication.** Type-preservation proof that transported ⇒ not-retained, with
  the R-marginal provably A/B-blind.
- **Kill (joint-record completion).** The physics leaves a residual correlation in
  R (partial SWAP), i.e. an affine leak — then a copy is effectively retained and
  the separator returns. This is the T411 death: tier-1 was retained; the transport
  was not linear.
- **Confidence.** 6.
- **Thesis.** Linear transport = enforced reach ⊊ co-present.
- **Antithesis (joint-record completion).** Any residual R-correlation is a
  retained clone; joint-record completion is the statement "your move leaked."
  Real quantum SWAP that leaves *any* mutual information in R breaks linearity.
- **Synthesis.** GO **conditional on exact linearity of transport** (zero residual
  R-correlation, no tier-1 retention). This is the sharpest statement of the whole
  cluster's convergence: the transport rung is worth building iff it enforces exact
  move semantics; a partial/leaky move reproduces every prior death. Verdict:
  **REDESIGN → GO** with a linearity invariant as the acceptance test.

### U3 — literature adjacency
- **Steelman.** No-cloning + quantum linear typing (linear logic ↔ quantum
  channels) is the type-theoretic face of Hayden-Preskill: the record is a linear
  resource scrambled beyond R; recovery = a linear decoder existing only at R+.
- **Confidence.** 4.
- **Synthesis.** Clean conceptual bridge; borrow linear-logic framing for the
  ALL-quantifier and no-copy conditions.

### U4 — fallback
- **Steelman.** The reusable deliverable is a **typed acceptance criterion**: the
  linearity/no-retained-clone invariant as a *reusable well-formedness test* for
  any future capability fixture — the thing whose violation explains all three
  deaths.
- **Confidence.** 6.
- **Synthesis.** Complements fallback (i) as a design-rule contribution: "capability
  fixtures must pass a move-not-copy type check."

---

## 47. Index Theory Expert (load-bearing)

### U1 — meaning of "physical rather than declared" (index / anomaly-inflow angle)
- **Steelman.** The key structural move: replace "boundary = a chosen subset" with
  "boundary = an **integer invariant forced by the bulk** via a bulk-boundary
  correspondence." In index theory the boundary term is *not chosen* — it is
  determined by a bulk topological invariant (anomaly inflow: the boundary anomaly
  is fixed by the bulk index; from memory, Atiyah-Patodi-Singer / Callan-Harvey
  inflow). A capability boundary cast as an **index** (Fredholm index, spectral
  flow, winding number) is integer-valued, deformation/relabel-invariant, and is a
  *quantity*, **not a declared region**. The temperature-blind integer frontier
  r(n)=n is exactly the kind of object that could be an index/winding number rather
  than a partition.
- **Support.** This is the one framing that yields "a boundary quantity that is NOT
  a subset." Indices are invariant under continuous deformation and change only by
  integer jumps (spectral flow) — precisely what would resist the relabel/
  declared-subset absorbers. Anomaly inflow gives a boundary term you cannot remove
  by any local counterterm (declaration).
- **Hidden assumptions.** The capability data admit an elliptic-operator / Fredholm
  structure; a bulk invariant exists whose inflow forces the boundary quantity; the
  finite model has a stable discrete analog (from memory, unverified — index theory
  is native to infinite-dim/continuum).
- **Vindication.** Express the A/B separation as a **spectral flow / index jump**:
  an integer that is 0 at R, ±1 at R+, invariant under all R-supported deformations
  (the ALL quantifier as deformation-invariance), forced by a bulk quantity no
  local declaration can cancel.
- **Kill.** No Fredholm/elliptic structure survives discretization; the "integer"
  r(n)=n is mere counting (quantum-Darwinism redundancy) with no deformation-
  invariance — i.e. it is not an index, just a tally. (The decoherence-bookkeeping
  absorber already reads r(n)=n as redundancy counting.)
- **Confidence.** 5.
- **Thesis.** Physical boundary = a bulk-forced integer index, not a declared
  region.
- **Antithesis (finite closed model).** Index theory lives on infinite-dimensional
  spaces: the Fredholm index is dim ker − dim coker of an operator with infinite-dim
  domain; spectral flow needs a continuous spectrum; anomaly inflow needs a bulk
  field theory. A **finite closed model has no genuine index** — every operator is a
  finite matrix with equal ker/coker dimensions balancing (index of a square matrix
  is 0), and "boundary" here is a subsystem choice, not a manifold boundary. So the
  proposed invariant either lives at infinity (out-of-house, cf. persona 15) or
  degenerates to a counting number a declaration can reproduce. The finite-closed-
  model objection bites hard: no infinite-dim structure, no true index.
- **Synthesis (PARTIAL SURVIVE — most promising physical repair, but out-of-house).**
  What survives: index theory offers the *only* candidate in the cluster for a
  boundary quantity that is intrinsically **not a subset** — an integer invariant
  forced from the bulk and stable under deformation. That is genuinely orthogonal to
  the declared-subset kill (you cannot "declare" a winding number away). BUT it is
  well-posed only where an elliptic/Fredholm or anomaly-inflow structure exists —
  the thermodynamic/continuum limit, NOT a finite closed matrix model. Synthesis:
  **reframe the target as an index/spectral-flow invariant of a limiting family**
  (converges with 15's "well-posed only at infinity" and 14's "asymptotic family"),
  and *test whether r(n)=n has any deformation-invariance beyond counting*. If
  r(n)=n is only a tally, EMPTY; if it is a spectral-flow/winding invariant, this is
  the strongest physical-boundary repair the cluster produced. Confidence that it is
  more than counting: low-moderate. Honest status: **promising, unverified,
  out-of-house.**

### U2 — transport rung
- **Steelman.** Transport dynamics could supply the missing *operator with a
  spectrum*: propagation gives a one-parameter family (time/reach) whose spectral
  flow across the R→R+ threshold is an integer invariant — a dynamically-generated
  index, not a declared cut. The frontier r(n) = accumulated spectral flow.
- **Support.** Turns the static finite fixture into a parameterized family (the
  thing index theory needs) and makes the integer frontier a *flow*, not a count.
- **Hidden assumptions.** The transport generator has a spectral gap whose crossing
  is the boundary; discretization preserves the flow.
- **Vindication.** A spectral flow of the transport generator that jumps by 1
  exactly at the R→R+ threshold, invariant under R-deformations, and *not*
  reproducible by any retained-carrier count.
- **Kill (joint-record completion).** A retained carrier adds a co-present mode that
  contributes to the count and makes the "invariant" reproducible by a local
  measurement — the flow is then not bulk-forced but boundary-declared. Joint-record
  completion = "your spectral flow is carried by a retained mode you could just
  measure," collapsing index → tally.
- **Confidence.** 5.
- **Thesis.** Reach frontier = spectral flow of the transport generator.
- **Antithesis (joint-record completion).** If tier-1 is retained, the discriminating
  correlation is carried by a co-present mode; the "index" is then a property of a
  declared subsystem, and a Z-measurement (the T401 kill) reproduces it — no bulk
  forcing. The integer looks topological but is actually a retained-mode count.
- **Synthesis.** GO-**conditional**: the transport rung is the right vehicle to
  turn r(n) from a count into a possible spectral-flow invariant, but ONLY under
  move-not-copy so the flow is carried by *inaccessible bulk modes*, not a retained
  handle. Test to run: is the frontier deformation-invariant (index-like) or does a
  single retained-mode measurement reproduce it (tally)? Verdict: **REDESIGN toward
  a spectral-flow readout**; strongest reason in the cluster to build transport, and
  strongest risk (it may just be counting).

### U3 — literature adjacency
- **Steelman.** Anomaly inflow ↔ black-hole boundary terms, spectral flow ↔ level
  crossing at horizons, APS boundary index ↔ entanglement across a cut — the horizon
  literature *is* where bulk-forced boundary invariants live, and Hayden-Preskill
  recovery has an index-theoretic decoupling face (from memory, unverified).
- **Support.** This is the natural home for "a boundary quantity forced by the bulk,
  not declared," which is exactly the U1 repair.
- **Hidden assumptions.** Transfer of continuum index results to finite/discrete
  fixtures.
- **Vindication.** A discrete anomaly-inflow analog forcing the capability boundary.
- **Kill.** No discrete analog; inflow is essentially continuum.
- **Confidence.** 5.
- **Synthesis.** Strongest-adjacency vote with 14/24: the horizon/index literature
  is the right home for a dynamically-forced boundary. Borrow inflow + spectral
  flow. Flag GU firewall/boundary resonance as stress-test input ONLY — do not treat
  the index framing's fit with GU's firewall hypothesis as any support.

### U4 — fallback
- **Steelman.** If the physical boundary dies, the honest index-flavored fallback is
  that the **integer, deformation-covariant frontier r(n)=n** is itself a reportable
  invariant — a partition-covariant, dynamics-indexed integer (aligned with T409's
  partition-covariance) — even if it is "only" redundancy counting, its
  deformation behavior across the interaction family is content.
- **Confidence.** 6.
- **Synthesis.** Feeds a fourth fallback flavor: the integer frontier as a
  (weak) topological/covariance invariant, complementing (ii)/(iii). Honest caveat:
  if it is pure counting, this collapses into the resource-theory frontier (ii).

---

## 52. Mathematical Minimalist

### U1 — meaning of "physical rather than declared"
- **Steelman.** Ask the deflationary question: does "physical boundary" name any
  object smaller constructions do not already provide? The minimal honest content
  is a **tripartite state with vanishing bipartite-marginal distinguishability but
  nonzero global distinguishability** (the T411 residue: worst proper-subset diff
  0.0, full-joint diff 0.124). If that object exists, it is the whole result; the
  words "physical boundary" add nothing testable. So: "physical vs declared" should
  be *retired* in favor of the smallest object that does the work — a
  no-local-marginal separator.
- **Support.** Every death attached to the phrase "physical boundary," never to the
  minimal separator object. Occam: drop the phrase, keep the object.
- **Hidden assumptions.** The minimal object is genuinely basis/decomposition-
  independent (else it too is declared).
- **Vindication.** The minimal tripartite separator exists and is
  decomposition-invariant — no bipartite marginal separates, the global does.
- **Kill.** Some proper subset / decomposition *does* separate (the object isn't
  minimal-and-global) — which is exactly the joint-record kill.
- **Confidence.** 6.
- **Thesis.** Retire "physical boundary"; keep the minimal global separator.
- **Antithesis (finite closed model).** Even the minimal object faces the kill: the
  "proper subsets" over which no marginal separates were declared subsets of a
  larger co-present set; add the retained carrier and a subset marginal *does*
  separate. In a finite closed model the minimal separator may itself be an artifact
  of an incomplete factor list. Minimality does not by itself defeat joint-record
  completion.
- **Synthesis (SURVIVES, shrunk and honest).** The minimal object survives IFF the
  factor list is complete (no retained carrier omitted) — i.e. the "no proper subset
  separates" holds over the *full* co-present factorization, not a declared one.
  Then it is exactly the Lieb-Robinson-surviving residue and needs no "physical
  boundary" language. Minimalist verdict: **the smallest honest survivor is the
  global-in-no-proper-subset separator over a complete factorization; the phrase
  "physical boundary" is surplus and should be dropped.** Converges with 5 and 26.

### U2 — transport rung
- **Steelman.** The minimal question: does transport add any object the static
  tripartite separator lacks? If the only new content is "the factorization is now
  dynamics-forced (complete, no retained factor)," then transport is worth building
  *only* to certify completeness of the factor list — not to add new structure.
- **Support.** Focuses the build on the single thing that was missing (a complete,
  non-declared factorization), avoiding QD/thermal-substrate overkill.
- **Hidden assumptions.** Transport actually certifies completeness (no retained
  factor) — which requires move-not-copy.
- **Vindication.** A transport fixture where the factor list is provably complete
  and the minimal global separator survives.
- **Kill (joint-record completion).** Transport still retains a factor → the minimal
  separator localizes to it → nothing gained over the static case. If transport does
  not certify completeness, it adds only apparatus, not content.
- **Confidence.** 5.
- **Thesis.** Build transport only to certify a complete factorization.
- **Antithesis (joint-record completion).** If retention persists, the transport
  rung is a *larger* object reproducing the same death — strictly worse by
  minimalist lights (more machinery, same kill).
- **Synthesis.** Verdict leans **REDESIGN or ABANDON**: build transport ONLY if it
  demonstrably delivers a complete, non-declared factorization (move-not-copy);
  otherwise it is apparatus without new content and should be abandoned in favor of
  stating the minimal static separator honestly. Most skeptical GO-vote in the
  cluster.

### U3 — literature adjacency
- **Steelman.** Minimally, the adjacency is a liability: Hayden-Preskill embeds the
  result in a large-N literature that already *has* the recovery/scrambling
  frontier, risking "we reproduced a known theorem with more apparatus."
- **Confidence.** 5.
- **Synthesis.** Borrow the theorem, do not re-derive it; the minimal contribution
  must be *orthogonal* to Hayden-Preskill (the anti-relabel separator), else it is
  redundant.

### U4 — fallback
- **Steelman.** The strongest honest fallback is the smallest one: **the global-
  correlation separator as the anti-relabel result (iii)** — a minimal object that
  no light-cone/support functional can express, stated without any physical-boundary
  or resource claim. Everything else (toolkit, frontier) is secondary.
- **Support.** It is the unique surviving asset (Lieb-Robinson relabel survived) and
  the smallest object carrying it.
- **Confidence.** 7.
- **Synthesis.** Fallback (iii) is the minimalist's primary recommendation and the
  cluster's most-backed survivor. Drop "physical boundary"; publish the minimal
  anti-relabel separator.

---

## Cluster Synthesis

Reminder: this is one process wearing 13 masks. Convergence below is a **target
generator, not evidence** (single-process ceiling). Attributions from memory are
flagged in-line above.

### U1 — What must "physical rather than declared" mean? (finite-closed-model)

**Surviving syntheses (by strength):**
- **Automorphism-invariance / implicit-(non)definability** (26, 15, converges with
  5). Physical = fixed by the model's automorphism group / not implicitly definable
  from the agent's relations; declared = parameter-dependent / automorphism-movable.
  This is the cluster's cleanest *well-posedness* criterion — and it *explains the
  kill history as a theorem*: in finite closed models, definable ⇒ declared, so the
  three deaths were the model telling the truth. Positive residue only relative to
  the **agent's stabilizer subgroup** (agent-relativity, repair a).
- **Obstruction class / no-local-section** (5). Physical = nonzero cohomology
  relative to a *dynamics-forced* cover; survives conditionally and gives the
  cleanest formal statement of T411's surviving residue.
- **Index / spectral-flow / anomaly-inflow** (47) — the load-bearing candidate for
  a boundary quantity that is **NOT a declared subset** (an integer invariant forced
  from the bulk, not a region). Genuinely orthogonal to the declared-subset kill
  (you cannot declare a winding number away). BUT well-posed only where an
  elliptic/Fredholm or inflow structure exists — the continuum/limit, not a finite
  closed matrix model (index of a square matrix is 0). Status: **promising,
  unverified, out-of-house.** Key test it hands the program: does r(n)=n have any
  deformation-invariance beyond quantum-Darwinism counting? If not, EMPTY.
- **Linearity / move-not-copy enforcement** (37). Not a definition of "physical" but
  the *mechanism* that would make a boundary enforced rather than declared;
  identified independently by nearly every persona as the missing ingredient.
- **Protocol-impossibility relative to a dynamics-forced alphabet** (10) and
  **counterfactual impossibility for a forced repertoire** (24) — well-posed and
  machine-checkable, but both reduce to "impossibility relative to a stipulated
  alphabet/repertoire" in a closed unitary model; they raise the bar and diagnose
  the failure rather than repairing it.

**EMPTY / near-empty syntheses (recorded honestly):**
- **Resource Theory (23): EMPTY by construction.** RT always *takes the free/non-free
  cut as input*; it can relabel a declared cut as a monotone but cannot derive
  physicality. This is the T398 concession restated from the inside.
- **Representation Theory (6): near-EMPTY.** No exact superselection in finite closed
  models; collapses to a size-scaling asymmetry cost (i.e. into RT).
- **Category Theory (2): SHRINKS** to functoriality/naturality as a necessary-not-
  sufficient hygiene filter (universal property collapses via the terminal full-state
  object).
- **Constructor Theory (24): SHRINKS** to a crisp negative diagnostic — because
  recovery is possible at R++, the boundary is possible-but-priced, NOT a
  constructor-theoretic impossibility.

**Convergence:** Strong, multi-discipline convergence (26, 15, 5, 6, 23, 24) that in
a **finite closed unitary model the strict physical/declared boundary is generically
NOT well-posed** — unitarity ⇒ everything co-present/recoverable ⇒ any nontrivial
region is a declared subset. **Split** on the escape route: (i) go infinite/limit
(15, 47, and 14's asymptotic family); (ii) go agent-relative-structural (26, and 5's
dynamics-forced cover); (iii) accept the negative and fall back (23, 52). The single
most novel *positive* U1 candidate is **47's index/spectral-flow invariant** (a
non-subset boundary quantity), explicitly out-of-house and unverified.

### U2 — Transport rung: GO / REDESIGN / ABANDON?

**Dominant verdict: REDESIGN (GO-conditional).** Near-unanimous convergence that the
transport rung is worth building **only if it enforces move-not-copy / exact
linearity** — i.e. the record is *transported with zero retained co-present clone and
zero residual R-correlation*. Under that single invariant, "reach ⊊ co-present"
becomes a *derived* fact (10: theorem of the transition system; 37: type-preservation
theorem; 26: outside the agent-subgroup orbit; 5: retained patch genuinely absent
from the cover) and joint-record completion is finally blocked at its source.

**Faced explicitly — joint-record completion:** every persona's antithesis shows that
*any* retained carrier or leaky (partial-SWAP) transport reproduces the T401/T411
kill (a Z-measurement on the retained mode separates A/B). The transport rung does NOT
automatically escape joint-record completion; it escapes *only* under a provable
no-retained-clone invariant. **37 gives the sharpest acceptance test** (linearity /
zero residual R mutual information); **10 gives the machine-checkable spec**
(reachable-set = graph forward closure with a verified no-copy invariant).

**Other killers:**
- *Wait-longer:* broad agreement (14, 24, 23, 15) that reach grows with budget ⇒ the
  boundary is a **resource/complexity threshold, not a wall.** Reframe the time budget
  as the independent variable (14: scrambling-time hardness; 24: budget-indexed
  impossibility; T409 escape-velocity).
- *Lieb-Robinson relabel:* the surviving residue (global correlation in no proper
  subset) is what a light cone cannot express (5, 52) — an asset, but surviving the
  wrong absorber doesn't rescue the boundary.
- *Reservoir idealization:* handled only by making departure dynamical (move-not-copy)
  rather than a declared partial trace.

**Splits:** 5 and 47 are the strongest GO-conditional voices (transport makes the
cover honest / turns r(n) into a possible spectral flow). 15, 52, and 23 lean
**ABANDON-in-house**: at every finite rung joint-record completion holds, so the claim
rests on an unobserved limit (15) or adds apparatus without new content over the
static minimal separator (52). **Net recommendation: REDESIGN** around an explicit
move-not-copy/linearity invariant AND a family/limit or complexity-threshold framing;
do not build a single leaky-transport fixture (it will die the same death).

### U3 — Literature adjacency (Hayden-Preskill / recovery)

**Strong, convergent adjacency** (14, 47, 24, 15, and secondarily 2/6/10/37): the
transport rung is a small Hayden-Preskill — a record dumped into a scrambling
reservoir, recoverable after a scrambling time with the right (Petz) recovery map.
Borrowable tools named (all **from memory, unverified**): the **decoupling theorem**
(a *derived* reach frontier: when the record is no longer recoverable from R), **Petz
recovery** (recovery = existence of a section/adjoint; 2), and **recovery-hardness /
Harlow-Hayden-style** results (14, 47: "recoverable but computationally infeasible" =
the complexity-priced repair).

**Two cautions the cluster raises:**
- The adjacency **reinforces threshold-not-wall**: Hayden-Preskill says the record IS
  recoverable after scrambling, which *undercuts* a strict impossibility (24, 2) and
  makes the boundary graded/time-indexed.
- It is **absorptive** (23): dynamical resource theories of channels + recovery maps
  are exactly the literature that would *relabel* the result as a channel monotone
  (the T404 demotion-to-translation risk). 52 warns of redundancy: contribute
  something *orthogonal* to Hayden-Preskill (the anti-relabel separator), don't
  re-derive a known theorem with more apparatus.
- Deeper home (15, 26, 47): Reeh-Schlieder / type-III algebras / anomaly inflow /
  horizon thermodynamics — where "no localized record" and "bulk-forced boundary
  term" are theorems. This is **literature-shaped and out-of-house** for finite
  fixtures. **GU firewall/boundary resonance FLAGGED (47, 15, 24, 5) as stress-test
  input ONLY — never support; the one-way rule stands.**

### U4 — Strongest honest fallback

**Most-backed survivor: (iii) the global-correlation / anti-relabel separator.**
Personas 52 (primary), 5 (cleanest statement: nonzero global class with no local
representative), and 2 (non-representable separator functor) converge on this as the
minimal, relabel-invariant object that survives every absorber including Lieb-Robinson
— publishable with NO physical-boundary or resource claim.

**Strong secondary: (ii) work-does-not-substitute-for-reach frontier**, owned by 23
(the temperature-blind integer monotone-separation result), backed by 6 (asymmetry
monotone) and 24 (budget-indexed impossibility / T409 escape-velocity). True as
stated because it *is* the absorbed form.

**Solid methods fallback: (i) the certificate toolkit as calibration machinery**,
owned by 10 (mechanized channel-lemma / ALL-quantifier discharge) and 37 (a reusable
move-not-copy type-check as a well-formedness rule for future fixtures), with 11's
parametricity/logical-relations technique.

**Additional honest deliverable — a scope theorem** (15, 26, 14): "within finite
closed models the physical/declared boundary is provably a definability/automorphism
artifact; a non-declarable boundary requires infinite structure (or an asymptotic
complexity gap)." Several personas argue this negative result is itself the most
valuable honest output — it converts three deaths into a theorem about the program's
reach.

**Fourth flavor (weak): 47's integer deformation-covariant frontier** as a
topological-flavored invariant — but collapses into (ii) if r(n)=n is pure
quantum-Darwinism counting.

**Verdict on "still worth a paper?":** Yes, on (iii)+(ii)+(i) plus the scope theorem —
but NOT as a physical-boundary result. The cluster's honest consensus: the
physical-boundary framing is unsupported at every tier and, in a finite closed model,
likely ill-posed; the surviving paper is the anti-relabel separator + the
work-≠-reach frontier + the calibration toolkit + an explicit scope/definability
theorem.

### Load-bearing-persona notes (as requested)
- **23 (Resource Theory):** U1 EMPTY by construction (RT presupposes the cut); owns
  U4-(ii). "Physically forced boundary" is **not in RT's vocabulary** — RT will
  relabel any transport result as a monotone/threshold.
- **24 (Constructor Theory):** raises the bar to *genuine impossibility*; because R++
  recovery exists, the boundary is possible-but-priced — a negative diagnostic, not a
  repair.
- **47 (Index Theory):** the only cluster candidate for a boundary quantity that is
  **NOT a declared subset** (bulk-forced integer index / spectral flow / anomaly
  inflow). Promising and orthogonal to the kill, but out-of-house (needs infinite-dim
  / continuum structure) and unverified; hands the program a concrete test — is
  r(n)=n deformation-invariant or just counting?
- **15 (Infinite Models):** clearest statement that U1 has **no finite repair**
  (Beth: definable ⇒ declared); the physical claim is well-posed only at infinity;
  recommends the scope theorem as primary deliverable.
- **52 (Minimalist):** retire "physical boundary"; the minimal honest survivor is the
  global-in-no-proper-subset separator over a *complete* factorization — most
  skeptical transport GO-vote (build only to certify completeness, else ABANDON).

### Whole-cluster honesty note
Shrinkage dominated this cluster: 4 syntheses came up EMPTY or near-EMPTY on the U1
physical claim (23 EMPTY, 6 near-EMPTY, 2 and 24 SHRUNK). The single positive,
genuinely non-subset U1 candidate (47's index framing) is explicitly out-of-house.
This is the method working: the finite-closed-model objection is not a hurdle the
cluster cleared — it is a result the cluster corroborated from six independent
directions. The durable output is the anti-relabel separator, the work-≠-reach
frontier, the calibration toolkit, and a scope theorem — not a physical boundary.
