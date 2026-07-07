# Gorard's Multiway Rewriting: Knuth-Bendix Completion as a Candidate Finality Operator

Exploration-grade intake, 2026-07-07 (Joe-supplied video). **Pointer grade; primary sources unchecked.**
No claim movement in any repo. This EXTENDS the 2026-06-30 Wolfram reading set
(`wolfram-observer-theory-reading-set-2026-06-30.md`) rather than duplicating it: that set covered
Wolfram's two *popular* TOE interviews (Observer Theory, computational-universe/biology). This is the
**Gorard** episode -- the technically rigorous member of the program -- so it carries a sharper, named
mechanism the earlier set did not have. Manufactured-convergence risk is high (computation and finality
are both in the session vocabulary); the guards and the distinguishing-predictions obligation are
load-bearing, the resemblance is not.

## Source

Jonathan Gorard, *Quantum Gravity & the Wolfram Physics Project* (Theories of Everything / Curt
Jaimungal, YouTube `ioXwL-c1RXQ`, published ~2024-03-29). Gorard is the mathematician supplying the
formal spine of the Wolfram model. Anchors (cited from the video + Gorard's papers, **unchecked**):
- *Some Relativistic and Gravitational Properties of the Wolfram Model* (arXiv:2004.14810): causal
  invariance of the hypergraph rewriting -> discrete general + Lorentz covariance; a hypergraph
  curvature -> Ricci tensor / discrete Einstein field equations.
- *Algorithmic Causal Sets and the Wolfram Model* (arXiv:2011.12174): hypergraph rewriting as an
  algorithmic dynamics for causal-set evolution; causal invariance -> conformal invariance of the
  induced causal partial order.
- *A Functorial Perspective on (Multi)computational Irreducibility* (arXiv:2301.04690): computational
  irreducibility formalized as a symmetric-monoidal functor between a category of computations and a
  category of cobordisms; higher cobordism categories capture multiway (branch/merge) irreducibility.

## What is new here versus the 2026-06-30 reading set (the four Gorard-specific items)

1. **A NAMED finality mechanism: Knuth-Bendix completion.** The old set had "equivalencing /
   coarse-graining = record-finality" as an *abstract* correspondence. Gorard gives the actual algorithm:
   an observer imposes *effective* causal invariance by performing a **Knuth-Bendix completion** on the
   multiway evolution, collapsing distinct multiway branches into a single unambiguous thread of time --
   explicitly analogized to decoherence / wavefunction collapse. That is a concrete, named, terminating-or-not
   mathematical operation standing where TaF puts "finality."
2. **A slicing-independence reading of relativity.** "Relativity = the choice of how you slice the
   multiway system does not change the underlying causal structure." Causal invariance -> discrete
   Lorentz covariance; hypergraph curvature -> Einstein equations. A derivation-shaped claim about where
   geometry comes from.
3. **A categorical formalization of irreducibility.** Irreducibility as a (symmetric-monoidal) functor;
   multiway irreducibility via higher cobordism categories. Candidate machinery, not vocabulary.
4. **Multicomputational irreducibility as a specific wall.** Determining the branchial structure requires
   tracing *every* singleway path -- a named complexity wall, sharper than "bounded observers can't
   decrypt irreducible microdynamics."

## The sharpest yield: Knuth-Bendix completion as a candidate formal model of the finality operator

The 2026-06-30 set's sharpest importable lane was **valid coarse-graining = finality admissibility**
(`open-problems/valid-coarse-graining-as-finality-admissibility.md`): Wolfram *asks* "which
equivalencings are valid?"; TaF *answers* "the bounded-observer-certifiable ones." Gorard sharpens BOTH
sides of that lane:

- **The operation is now named.** The observer's branch-collapse is a **Knuth-Bendix completion** (a
  confluence-forcing rewrite of the multiway system). So TaF's finality operator has a concrete external
  candidate model to be compared against: *is TaF's record-finality a Knuth-Bendix-style completion of a
  branching process to a confluent (single-thread) one?*
- **The admissibility question gets a built-in success condition.** Knuth-Bendix completion is not always
  possible: it may fail to terminate, or no finite confluent system may exist. That failure structure is
  exactly the shape of "which coarse-grainings are admissible": the admissible finalizations are the ones
  whose completion *converges*. This is a candidate crisp restatement of the finality-admissibility filter
  (D1 accessible-records + reversal-cost; T10/T29 selection) in rewriting-theoretic terms.

Honest grade: this is a **candidate model to test, not an import.** Knuth-Bendix is a *rival* fully-worked
account of "how branches become one history"; if it reproduces TaF's finality typing it is a competitor to
out-distinguish, and if it does not, the mismatch is the TaF-specific content. Either way it makes the
distinguishing-predictions obligation (below) concrete rather than abstract.

## Bearing on the live GU dialectic: computation-first is a rival MONISM, not a confirmation

Relevant because a multi-persona Hegelian pass on **GU geometry-first vs entropic-gravity information-first**
is running in `gu-formalization` right now, synthesizing toward "geometry and information as two faces of
one boundary structure." Gorard/Wolfram is a *third* position in that exact dialectic, and its bite cuts
against the synthesis, not for it:

- In the Wolfram model, spacetime/geometry emerges from the **causal graph** and observer/measurement
  structure emerges from the **branchial graph** -- two projections of one **multiway (computational)
  substrate**. That looks superficially like the session's inside/outside two-faces synthesis, with the
  rewriting rules as the common root.
- But the honest reading is the opposite of a confirmation: computation-first **relocates the fundamental
  layer BELOW both** geometry and information. Wolfram would say neither is a "face" of a boundary -- both
  are *downstream* of rules + the observer's finalization. So an independent program (outside the tri-repo
  lineage) does NOT independently arrive at "geometry <-> information as co-equal faces"; it dissolves the
  pair into a third monism (rules). That is a genuine antithesis to the running synthesis, and it is the
  more valuable input precisely because it resists the manufactured convergence. **To be folded into the
  workflow's main-loop verifier note as the noted third pole + the "independent arrival vs relocation" test.**

## Other repos (proportionate; each keeps its own ledger)

- **temporal-issuance (candidate, not yet filed):** the multiway **branch** (a new admissible successor
  state is created) vs the observer's **confluence/collapse** (existing branches are read down to one) is a
  clean candidate image of TI's **D-FORK**: branching = *issuance* (new possibility minted), completion =
  *disclosure* (reading a fixed structure). This would sharpen the existing
  `absorbers/observer-equivalencing-ruliad-slice.md`. **Named here as a pointer; offer to file the absorber
  extension separately -- not filed unilaterally.**
- **gu-formalization (thin; standing refusal respected):** the existing
  `explorations/misc/wolfram-observer-theory-pointer-2026-06-30.md` correctly grades Wolfram
  *low-relevance to GU's specific obligations* (renormalizability, ghost/unitarity, generation count).
  Nothing here changes that. The one GU-adjacent use is the live-dialectic input above, which routes
  through the running workflow, not a new GU obligation.

## Distinguishing-predictions obligation (carried over, now concrete)

The 2026-06-30 set flagged that TaF, being a near-neighbor of Wolfram Observer Theory, *must* state a
difference or read as a relabeling. Gorard makes the target concrete: TaF must state what its
record-finality does that a **Knuth-Bendix completion of a multiway system does not** (candidate: TaF's
finality carries a record/causal *typing* and a sheaf-gluing obstruction that a bare confluence-forcing
rewrite does not; and TaF's admissibility is bounded-observer-*cost*-indexed, not just
termination-indexed). -> the row for `literature/distinguishing-predictions.md` when created; tracked here
meanwhile alongside the Observer-Theory row.

## Guards (standing, load-bearing)

- **Projection is not finality; coupling-flow is not record-flow.** Borrow the *shape* (a branching
  process finalized to one thread by an observer operation), never the ontology. TaF has no rewriting rules
  and asserts no substrate.
- **G1/G3 hold.** Observer-relative finality is access/rendering, not creation; Wolfram's "laws because we
  are observers like us" flirts with observer-creates-reality and TaF's discipline is exactly what keeps
  the mapping from collapsing into idealism.
- **Primary sources unchecked.** All Gorard/Wolfram claims are from the video + abstracts, from memory in
  places; verify arXiv:2004.14810 / 2011.12174 / 2301.04690 before any load-bearing use.
- **Manufactured convergence.** "Physics from computation, finalized by an observer" rhymes with the whole
  finality program because computation is in view this session; resemblance is a warning, not evidence. The
  cures are the distinguishing-predictions statement and treating Knuth-Bendix as a *rival* to test, not a
  confirmation to adopt.
- **Cross-repo material is stress-test input, never support.** Gorard's model does not validate TaF's
  finality language, and TaF does not move any Wolfram-model status. Single-process caution: this note and
  the dialectic it touches come from one process; independent arrival would be stronger, and the honest
  reading above is that Gorard does NOT independently arrive at the session's synthesis.
