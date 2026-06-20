# Skeptical Diligence Review of Typed Forgetting and Local-to-Global Obstruction in Finite Record Systems

## Executive verdict

The draft is candid about what is already known: it explicitly concedes that the gluing obstruction is known, that signed-graph parity CSP is known, that sheaf/contextuality obstruction is known, and that the possible contribution is instead a “typed attribution calculus” around finite satisfiability loss; it also says the note is not yet mature and that `LossKernel` still has to be turned from metadata into a first-class mathematical object. fileciteturn0file0

On a standalone mathematical reading, this is **not yet an independently publishable research program**. The core obstruction phenomenon already sits in well-developed prior art: finite CSP/homomorphism theory, relational database projection-join theory, sheaf-theoretic global-section obstruction, and signed-graph parity/balance. The draft’s category claim is routine once the definitions are chosen. The only genuine opening is a formal theory of **typed blame/provenance for obstruction under lossy maps**. But that exact area is already surrounded by provenance, why-not provenance, causal explanation, lenses, abstract interpretation, and declassification/effect systems, all of which study structured information loss, explanation, or path-sensitive behavior. As written, the draft has not yet shown a canonical mathematical object, a separation theorem, or an unavoidable obstruction to functorial/compositional attribution that would distinguish it sharply from those literatures. citeturn10academia8turn10academia3turn27search7turn28search0turn21academia0turn13search0turn22academia0turn11academia0turn23academia2turn26search1turn14academia3

## Closest prior art

The strongest hidden prior-art overlap is **not** category theory first; it is **relational database theory plus CSP plus sheaf/global-section formulations**. The draft’s “finite sites, local values, patch constraints, compatibility predicate, global-assignment predicate” are structurally much closer to finite relational structures, database instances under projection/join, and presheaves of local sections than to the technical notion of a restriction category. Abramsky explicitly drew a direct formal bridge between relational databases and Bell/contextuality, while the Sheaf-Theoretic Structure paper made “local compatibility without global section” the central obstruction pattern. Meanwhile, finite-structure/CSP literature treats these questions as homomorphism/existence problems. fileciteturn0file0 citeturn10academia3turn10academia8turn27search7turn24search0

A second strong overlap is with **provenance and explanation theories**. Database provenance distinguishes why-, where-, and how-provenance; why-not provenance asks why an expected answer does not appear; causal explanation frameworks rank responsibility; provenance graphs explicitly track which parts of an input and which operations are relevant to an output or non-output. The draft’s “typed attribution layer” is closest to this cluster, not to a new obstruction theory in the classical sense. citeturn22academia0turn11academia0turn23academia2turn23academia1

A third major overlap is with **typed forgetting and path-sensitive analysis** in programming-languages theory. Abstract interpretation formalizes systematic loss of distinctions under abstraction; information-flow security and declassification are already organized around typed control of what may be forgotten or revealed; effect systems and path-sensitive analyses treat behavior as depending on execution/path history rather than endpoints alone. This does not make the draft identical to that literature, but it means that “typed loss” and “path dependence” are not fresh ideas by themselves. citeturn14search4turn26academia2turn17search4turn26search1turn14academia3

The prior-art overlap is best summarized this way:

| Area | Core references | Finite local systems | Typed preserved or forgotten morphisms | Loss kernels or mathematically meaningful information loss | Obstruction attribution | Path dependence | Non-functorial attribution | Bottom-line |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Relational databases and CSP | Abramsky on databases and Bell; CSP/homomorphism literature. citeturn10academia3turn27search7 | Yes | Partial | Partial | Partial | Partial | No | **Closest structural prior art**. Your objects already live here. |
| Sheaf-theoretic contextuality | Abramsky–Brandenburger; cohomological follow-ups. citeturn10academia8turn0academia1 | Yes | Partial | No | Partial | Partial | No | Covers the obstruction itself almost exactly. |
| Signed graphs and parity CSP | Harary balance; parity/XOR formulations. citeturn28search0turn28search8 | Yes, for parity cases | No | No | Weak | Yes | No | Covers parity obstruction and path-sign phenomena, not typed blame. |
| Restriction categories | Cockett–Lack tradition. citeturn25academia0turn25academia1 | No, not as drafted | Partial | Partial in other senses | No | No | No | Name collision matters: your “restriction system” is **not** this notion. |
| Lenses and bidirectional transformations | Lens/bx literature; generalized lenses. citeturn13search0turn12academia0 | No | Yes | Partial | No | Partial | No | Already formalizes view/projection plus discarded information. |
| Provenance, why-not provenance, causality | Cheney; Meliou et al.; PUG. citeturn22academia0turn11academia0turn23academia2 | No | Partial | Partial | Yes | Yes | Partial | **Closest conceptual prior art** for the attribution layer. |
| Abstract interpretation, info-flow, effect systems | Cousot–Cousot tradition; abstract non-interference; declassification dimensions; path-sensitive AI. citeturn14search4turn26academia2turn26search1turn14academia3 | No | Yes | Yes | Partial | Yes | Partial | Strong prior art for typed forgetting and path sensitivity. |
| Classical obstruction theory | Standard extension/section obstruction tradition. citeturn15search2 | Partial | No | No | No | Weak | No | Same word “obstruction,” but not the same problem. |

The most important skeptical conclusion from that table is simple: **the draft’s closest neighbors already cover either the obstruction or the attribution machinery.** What is not yet established is that the draft’s combination yields a mathematically indispensable new object or theorem.

## Audit of the candidate theorem units

| Candidate theorem unit | Current status | Strongest existing framework that may subsume it | What would need to be proved to make it publishable |
|---|---|---|---|
| **CSP equivalence with typed attribution** | **Known for the equivalence part; unclear for the attribution part.** The reduction of local-to-global obstruction to CSP/homomorphism/global-section failure is classical. The claim that ordinary CSP lacks the typed attribution layer is true in a loose sense, but provenance and explanation frameworks already add structured metadata to CSP-like reasoning. citeturn10academia8turn10academia3turn27search7turn22academia0turn11academia0 | CSP/homomorphism theory; relational database projection-join theory; sheaf contextuality; provenance and why-not explanation. citeturn10academia8turn10academia3turn27search7turn22academia0turn23academia2 | A real representation theorem: define a typed system and an attribution semantics, show the obstruction part reduces to standard CSP, then prove that the attribution part **cannot** be reconstructed from ordinary CSP data or standard provenance alone. Without that separation theorem, this is mostly repackaging. |
| **Typed transport category** | **Trivial once definitions are chosen.** Any class of systems with designated identities and associative composition of morphisms forms a category if composition is defined that way. Existing literatures already build categories of partial maps, schema mappings, and lenses. citeturn25academia0turn21academia0turn13search0 | Restriction categories, functorial data migration, lenses/optics. citeturn25academia0turn21academia0turn12academia0 | Something beyond “it is a category”: a universal property, a factorization system, an enriched/fibred structure, or a theorem linking categorical structure to obstruction behavior. As stated, this is not publishable by itself. |
| **Non-functorial obstruction admissibility** | **Not yet well-posed.** A claim about a “Boolean functor” needs a specified target category or monoid structure on truth values; the draft does not supply one. If the intended claim is merely that admissibility is not endpoint-determined or not stable under composition, that must be stated precisely. fileciteturn0file0 | Provenance semantics and equivalence-invariant provenance; path-sensitive analyses; blame calculi. Provenance work is especially relevant because it studies when annotation semantics are or are not invariant under equivalent derivations. citeturn8academia3turn22academia0turn14academia3turn19academia0 | First, define the target notion precisely. Then prove a sharp impossibility theorem: for example, no endpoint-only or composition-only attribution semantics can satisfy your axioms. Without that, “non-functoriality” looks like a byproduct of unclear definitions. |
| **Path-dependent admissibility** | **Probably known in spirit; currently trivial as stated.** If the semantics explicitly accumulates forgotten labels along a path, then different paths can obviously produce different verdicts. That is definition-driven, not theorem-driven. Path sensitivity is already standard in program analysis and provenance graphs. citeturn14academia3turn23academia2turn28search0 | Path-sensitive abstract interpretation; provenance graphs; signed-graph path-sign phenomena; declassification histories. citeturn14academia3turn23academia2turn28search0turn26search1 | You need a **nontrivial quotient test**: prove that two paths with the same endpoints and the same composite map, or at least the same net forgotten-coordinate set, can still differ. Otherwise this is just “different paths have different labels.” |
| **Loss kernel attribution lemma** | **Plausible contribution, but currently unclear and not yet mathematical enough.** The draft itself says `LossKernel` may still be only metadata. If so, any lemma using it risks becoming definitional or tautological. fileciteturn0file0 | Abstract interpretation’s abstraction/concretization, provenance semirings, why-not provenance, causal responsibility, and possibly categorical kernel-like constructions if formalized. citeturn14search4turn26academia2turn22academia0turn11academia0turn19academia4 | Define `LossKernel` canonically and compositionally. Then prove necessity and sufficiency: not just “typed loss is recorded,” but that the kernel determines when obstruction attribution is legitimate, and that without it attribution fails or becomes non-unique. A counterexample boundary is essential. |

My blunt read is that **only the fifth unit has serious novelty potential**, and only if it becomes a real mathematical object rather than an annotation convention.

## The typed attribution layer

The draft is right to focus attention here, because the obstruction itself is plainly not new. fileciteturn0file0

Is “typed attribution of obstruction under lossy morphisms” already a recognizable problem? **Partly, but not under that exact name.** The closest existing names are:

- **Why-not provenance** or **explanations for non-answers** on the database side, where the goal is to explain why a desired global/query result fails to appear. citeturn23academia2turn11academia4
- **Causal explanation / responsibility** for outputs and non-outputs, where one identifies which inputs or transformations are relevant to the failure or success of a result. citeturn11academia0turn5academia0turn19academia4
- **Typed declassification / abstract non-interference** on the programming-languages side, where “what is forgotten or allowed to flow” is a typed, structured notion rather than an untyped loss. citeturn26search1turn26academia2turn17search4
- **Lenses / bidirectional transformations**, where a view function deliberately discards information and one studies what consistency information is needed to recover or update the source. citeturn13search0turn12academia0

What is **not** already a standard named problem is the exact synthesis: “Given a local-to-global satisfiability obstruction, and a lossy morphism between finite local systems, when is it mathematically legitimate to attribute the target obstruction to named forgotten source structure?” I do not know a canonical established label for that exact formulation, and that is the draft’s narrow novelty window. But that does **not** yet make it a publishable contribution. To rise above “metadata added to known machinery,” the paper would need to show at least one of the following:

First, a **canonical semantics** for forgotten structure, not user-chosen tags. Second, a **separation theorem** proving ordinary provenance/why-not/projection semantics cannot recover the same attribution judgments. Third, an **invariance or impossibility theorem** showing why no functorial or endpoint-only attribution can work under natural axioms. Without one of those, the typed layer looks like an explanatory wrapper around known CSP/sheaf/database constructions rather than a new mathematical program. citeturn22academia0turn23academia2turn8academia3turn26academia2

## Fatal weaknesses

The first fatal weakness is definitional: **“forgotten structure” is not yet a mathematical invariant.** The draft uses the language of named preserved versus forgotten structure, but unless those are tied to a formal semantics, they are just labels attached to morphisms. Existing fields already have mathematically meaningful notions of loss of distinction: abstraction/concretization in abstract interpretation, declassification dimensions in information-flow theory, view complements in lens theory, and provenance polynomials/graphs in provenance theory. The draft has not yet shown that its `forgotten_structure` is comparably rigid rather than ad hoc. fileciteturn0file0 citeturn14search4turn26search1turn13search0turn22academia0

The second fatal weakness is that **`LossKernel` currently does not do theorem-level work**. The draft explicitly says the “LossKernel phase asks whether `forgotten_structure` can be upgraded from metadata into a composable mathematical object.” That is an honest admission, but it also means the central candidate novelty is not yet there. Until `LossKernel` has either a universal property, a factorization role, a kernel/congruence interpretation, or a proven compositional law, any “loss kernel attribution lemma” is in danger of being tautological: “attribution is admissible when the attribution data says it is.” fileciteturn0file0

The third fatal weakness is with **admissibility**. Right now, admissibility looks dangerously close to a predicate designed to certify exactly the cases the author wants. The draft’s own gloss says attribution requires that the projection be definable, loss be named and typed, and loss be relevant to the target obstruction. Unless “relevant” is given an independent criterion and its computational or categorical behavior is analyzed, the theory risks circularity. Provenance and causal-explanation literatures already wrestle with this exact issue: explanation notions are cheap to define and hard to make canonical, invariant, and non-circular. fileciteturn0file0 citeturn11academia0turn22academia0turn23academia2

The fourth fatal weakness is that the **non-functoriality claim is currently not a theorem but a slogan**. As stated in the draft, “the predicate is not a Boolean functor”; but without a target category, this is simply not precise mathematics yet. And if the intended meaning is only that the property depends on intermediate morphisms or path annotations, then that is not surprising; it is the default behavior of many path-sensitive systems unless one proves an invariance theorem. In provenance theory, the genuinely interesting result is often the opposite one: proving equivalence invariance. So if this paper wants non-functoriality to matter, it has to prove that no natural invariant/compositional semantics can do the job. fileciteturn0file0 citeturn8academia3turn23academia2

The fifth fatal weakness is that **path dependence may be entirely definitional**. If a path carries the ordered list of discarded labels, then of course two different paths can have different admissibility verdicts. That does not yet say anything mathematically deep. The test is whether path dependence survives after quotienting by the obvious summary invariants: same composite map, same endpoint pair, same multiset or set of forgotten types, same induced coarse system. If not, the theorem collapses into bookkeeping. fileciteturn0file0 citeturn14academia3turn28search0

A smaller but still real issue is terminology. In category theory, **restriction categories** already have a standard meaning, namely categories of partial maps with a restriction operation. The draft’s “finite restriction systems” are not that notion; they are closer to presheaf/database/CSP systems. An expert category theorist will notice this immediately and may infer more novelty than is actually present, or simply view the terminology as confused. fileciteturn0file0 citeturn25academia0turn25academia1

## Diligence verdict

### Claim-by-claim status table

| Claim | Status | Reason |
|---|---|---|
| Finite local-to-global obstruction can be modeled as parity/CSP/global-section failure | **Known** | Classical in sheaf contextuality, relational databases, CSP/homomorphism, and signed-graph parity. citeturn10academia8turn10academia3turn27search7turn28search0 |
| “Typed transport category” | **Trivial** | Categoryhood is routine once morphisms and composition are definitionally chosen. Existing categorical frameworks already model similar maps. citeturn25academia0turn21academia0turn13search0 |
| “Non-functorial obstruction admissibility” | **Unclear** | Not well-posed as stated; likely either a restatement of path sensitivity or a consequence of unspecified semantics. |
| “Path-dependent admissibility” | **Trivial or probably known under another name** | Interesting only if it survives quotienting by obvious summaries. Path-sensitive analysis and provenance already normalize this phenomenon. citeturn14academia3turn23academia2 |
| “Loss kernel attribution lemma” | **Plausible contribution** | This is the one live novelty candidate, but only if `LossKernel` becomes a canonical mathematical object with a non-vacuous theorem. |
| “Typed attribution layer adds data not present in ordinary CSP” | **True but insufficient** | So do provenance, why-not explanations, causal responsibility, lenses, and declassification systems. The missing piece is a theorem of necessity or separation. citeturn22academia0turn11academia0turn13search0turn26search1 |

### Prior-art overlap table

| Prior-art cluster | Overlap verdict |
|---|---|
| Sheaf-theoretic contextuality | **Very high overlap** on the obstruction itself. |
| Signed graphs and parity CSP | **Very high overlap** on parity obstruction and path-sign logic. |
| Relational databases and projection-join theory | **Very high overlap** on local records, projections, joins, and consistency questions. |
| Finite CSP and homomorphism | **Very high overlap** on satisfiability/existence structure. |
| Restriction categories | **Low direct overlap**, but the chosen terminology collides with an established field. |
| Lenses and optics | **Moderate overlap** on explicit forgetting under compositional morphisms. |
| Provenance, why-not provenance, causal explanation | **High conceptual overlap** on attribution, relevance, and failure explanation. |
| Abstract interpretation, info-flow, effect systems | **High conceptual overlap** on typed forgetting, declassification, and path sensitivity. |

### The three strongest objections an expert reviewer would raise

The first objection is that **the mathematical content currently visible is almost entirely prior art**, and the draft itself admits as much. What remains is an attribution layer that has not yet been separated from established provenance/explanation/blame frameworks by theorem. fileciteturn0file0 citeturn10academia8turn10academia3turn22academia0turn11academia0

The second objection is that **the proposed novelty is not yet mathematical enough**. `LossKernel` is not yet defined as a canonical object; admissibility risks circularity; the non-functor claim is not formally stated in a category-theoretic sense; and path dependence currently looks annotation-driven rather than theorem-driven. fileciteturn0file0

The third objection is that **the draft may be rebranding known “explanation of failure under projection” ideas without acknowledging the database/provenance lineage strongly enough**. The surprise omission is not just one paper or two; it is an entire long-running body of work on projection, loss, provenance, non-answers, and causal explanation. citeturn10academia3turn22academia0turn11academia0turn23academia2

### The three best ways to strengthen the paper

The first and most important fix is to **define `LossKernel` canonically**. It should not be a bag of labels. It needs either a universal property, a factorization role, an induced equivalence/congruence, or a formally compositional semantics analogous to an abstract domain, provenance object, or kernel pair.

The second fix is to **prove a true separation theorem**. The strongest version would show that ordinary CSP/sheaf data plus standard provenance/why-not semantics are insufficient to recover the attribution judgments, while the proposed typed layer is sufficient. That would convert the paper from “new language” to “new theorem.”

The third fix is to **replace slogans with counterexamples**. In particular, the paper should have one minimal worked example proving that the same source and target, and ideally the same composite map, can yield different admissibility verdicts in a way that cannot be collapsed to simple endpoint predicates or naive loss-set bookkeeping.

### Best target venue type

**Not ready.** If the core formalization succeeds, the natural next stop would be a **theoretical CS workshop** or a short **category-theory / applied-category-theory note**. In its current state, even an arXiv note would read more like a research memorandum than a finished mathematical contribution. fileciteturn0file0

### Recommended next proof or counterexample to attempt

The best next move is a **minimal factorization counterexample**:

Construct finite systems \(A,B_1,B_2,C\) and maps
\[
A \xrightarrow{f_1} B_1 \xrightarrow{g_1} C,\qquad
A \xrightarrow{f_2} B_2 \xrightarrow{g_2} C
\]
such that:

- \(A\) is globally satisfiable,
- \(C\) is obstructed,
- the two composites \(g_1 f_1\) and \(g_2 f_2\) are the same underlying projection or induce the same endpoint behavior,
- the naive summary “set of forgotten labels” is also the same, but
- one path is admissible and the other is not.

If such an example exists, it would show that path dependence is not just bookkeeping. If it **cannot** exist under a reasonable definition of `LossKernel`, then the current program collapses toward standard provenance semantics, which is equally valuable information. Either outcome would materially sharpen the paper.