# Geometric Unity — Time as Finality Integration Roadmap v0.1

**Status:** Research proposal  
**Date:** 2026-06-19  
**Scope:** Mathematical integration analysis; no physics claims; no GU validation claims  
**Dependencies:** T48–T56 (record-dependency order, FinaliEvent, finite descent, conflict, sheaf cohomology)

---

## Governing Principles

1. **Import mathematics before interpretations.** Fiber bundles, pullback maps, connections, affine spaces, and cohomology are established mathematics. TaF-specific interpretations of those tools are original and must be clearly labeled.

2. **Preserve TaF's central claim.** The claim being developed is: the temporal order of events is determined by the stabilization structure of records, not presupposed. No imported GU structure may depend on a pre-given temporal arrow.

3. **Avoid overclaiming.** GU and TaF share mathematical language in several places. Shared language is not shared physics. Similar formal constructions are noted as *structural analogies*, not as evidence that TaF validates GU or vice versa.

4. **Maintain mathematical independence.** Every TaF result must remain provable without reference to GU. GU is a source of mathematical inspiration and language, not a foundation.

5. **Label everything.** Each item in the roadmap is tagged: **[EST-MATH]** (established mathematics), **[TaF-ORIG]** (original TaF mathematics), **[CONJECTURE]** (not yet proved), or **[SPECULATIVE]** (long-term research direction).

---

## Concept Classification

### Level 1 — Mathematical Language (Established Mathematics)

Tools from GU that TaF can import without originality claims:

| Concept | GU Source | Established Reference |
|---------|-----------|----------------------|
| Fiber bundles and local sections | §3, §4 | Kobayashi–Nomizu |
| Pullback of bundles via embedding | §4–§6 | Spivak, Differential Geometry |
| Short exact sequences and splitting | §4 | Homological algebra (standard) |
| Affine spaces modeled on a vector space | §6, §12.8 | Linear algebra (standard) |
| Connections on principal bundles | §6 | Kobayashi–Nomizu |
| Augmented/displaced torsion tensor | §7 | GU §7 (original to Weinstein) |
| Čech cohomology of a presheaf | §9, §10 | Godement, Bredon |
| Deformation complex and moduli | §10 | Atiyah–Hitchin |
| Z/2Z Gaussian elimination for H¹ | standard | Linear algebra (standard) |
| Shiab-style contraction operators | §8 | GU §8 (original to Weinstein) |
| Inhomogeneous gauge group G = H ⋉ N | §6 | GU §6 (structure used there) |
| Semi-direct product of groups | §6 | Group theory (standard) |
| Rarita–Schwinger representations | §11 | Representation theory (standard) |

### Level 2 — Structural Framework (GU Structures Applied to TaF)

Analogies where a GU structural object maps naturally onto a TaF structural object. These require original work to formalize but the structural pattern is imported.

| GU Object | TaF Analog | Status |
|-----------|-----------|--------|
| Observerse triple (X, Y, {ι}) | Record-Space Triple (Σ, Π, {ι_α}) | [CONJECTURE] — requires definition |
| Einsteinian case: Y = Met(X) | Record-space Π = accessibility space over Σ | [CONJECTURE] |
| Native fields (Hebrew letters, X-native) | Global colimit order: A(U) = ρ_U(S_global) | [TaF-ORIG] — established in T56 |
| Invasive fields (pullbacks from Y) | Apparent-finality order: F(U) = S_local(U) | [TaF-ORIG] — established in T56 |
| Normal bundle N_ι | Hidden-intermediary bundle: events visible globally but not locally | [CONJECTURE] |
| Zorro construction | Colimit-determines-connection: global order → finality connection | [CONJECTURE] |
| Augmented torsion T_g = ω − ε⁻¹(d_{A₀}ε) | Finality torsion τ_F(U) = A(U) \ F(U) (gap presheaf) | [CONJECTURE] — T56 has H⁰(G) |
| Distinguished connection A₀ | Colimit as distinguished finality connection | [CONJECTURE] |
| Affine space of connections A | Affine space of finality orders (colimit is origin) | [CONJECTURE] |
| Inhomogeneous gauge group G = H ⋉ N | Inhomogeneous Finality Group G_F = H_F ⋉ N_F | [CONJECTURE] |
| Deformation complex (∂₁, ∂₂) | Phantom deformation complex | [SPECULATIVE] |
| Arrow of time (§12.2: only ℝ¹ is naturally ordered) | Record-dependency order as the unique 1D ordering | [SPECULATIVE] |

### Level 3 — New Definitions (Original TaF Mathematics Required)

Objects that do not yet exist in TaF and must be defined from scratch, informed by GU analogy but proven on TaF's own terms:

1. **Record Bundle** R(Σ) — fiber bundle over state space Σ whose fibers are record collections
2. **Observer Embedding** ι_α: U_α → Π — accessibility map formalized as a bundle section
3. **Record-Space Triple** (Σ, Π, {ι_α}) — TaF analog of the Observerse
4. **Finality Connection** ∇_F — connection on the observer bundle encoding how finality order varies across observers
5. **Finality Torsion** τ_F(U) = A(U) \ F(U) — the phantom gap at observer U (already named in T56 as gap presheaf G; this reframes it as a torsion tensor)
6. **Inhomogeneous Finality Group** G_F = H_F ⋉ N_F — symmetry group of finality structure
7. **Record Translation Group** N_F — analog of GU's ad-valued 1-forms; the "translations" in the finality affine space
8. **Finality Gauge Group** H_F — automorphisms of the record bundle that preserve finality structure
9. **Shiab-Analog Operator** C_F — contraction operator incorporating observer symmetry for counting phantom pairs

### Level 4 — Candidate Theorems (Original TaF Mathematics, Potentially Provable)

Statements that appear reachable given TaF's existing structure plus the imported framework:

1. **Phantom Incomparability Theorem** (extends T56): (e_j, e_i) is a phantom pair at observer U iff τ_F(U) contains (e_j, e_i). Equivalently: F(U) ≠ A(U) iff finality torsion is non-zero at U.
2. **Gap Presheaf Theorem** (conjectured in T56 Q1): H⁰(G) ≅ the set of phantom incomparability witnesses from T51–T52.
3. **Sheafification Theorem** (conjectured in T56 Q2): the sheafification of the apparent-finality pre-presheaf F equals the ambient presheaf A.
4. **Colimit as Torsion-Free Connection**: the colimit is the unique finality connection with vanishing torsion (τ_F = 0).
5. **Observer Embedding Determines Finality**: given a record-space triple (Σ, Π, {ι_α}), the observer embeddings uniquely determine both the apparent order and the phantom gap.
6. **G_F-Invariance**: the colimit connection is the unique G_F-invariant element of the affine space of finality connections.

### Level 5 — Long-term Research Directions (Speculative)

1. Gauge theory of finality evolution: curvature of the finality connection as a measure of irreversibility
2. Arrow of time recovery: whether TaF's record-dependency order can be recovered from a pre-metric structure analogous to GU's Observerse
3. Effective chirality analog: phantom incomparability as an observer's "effective" incomparability in a globally non-chiral finality structure
4. Dirac-pair analog: whether first-order finality equations (phantom detection) imply second-order finality equations (information flow conservation)
5. Categorical reformulation: TaF as a (∞,1)-categorical structure with finality connections as higher morphisms
6. Information geometry link: Riemannian metric on the space of finality connections

---

## 8-Stage Sequential Integration Roadmap

Each stage is designed to be self-contained and independently publishable. A stage can be reviewed and accepted before the next stage begins. Dependency arrows are one-directional: Stage N depends on Stages 1…N-1.

---

### Stage 1: Bundle Language for Records and Observers

**Objective:** Establish a bundle-theoretic vocabulary for TaF's existing structures. Translate records, events, and accessibility maps into the language of sections and fiber bundles. This stage imports language only — no new TaF results.

**Imported Mathematics:** [EST-MATH]
- Fiber bundle (E, B, π, F): total space, base, projection, fiber
- Local section s: U → E with π ∘ s = id_U
- Restriction of a section to a subspace
- Pullback bundle f*E along a map f: X → B
- Short exact sequence of bundles: 0 → A → B → C → 0

**TaF Concepts Affected:**
- Records r ∈ R: reframed as elements of fibers of a Record Bundle R(Σ) over state space Σ
- FinaliEvents (from T48): reframed as bundle morphisms between fibers
- Observer patches U_α (from T56): reframed as open subsets of Σ with a local section ι_α: U_α → Π
- Record-dependency order: becomes a partial order structure on the total space of R(Σ)
- Accessible records at patch U: the image of ι_α in Π

**New Definitions:** [TaF-ORIG]
- *Record Bundle* R(Σ): a fiber bundle over state space Σ where each fiber R_x contains the records accessible from state x
- *Accessibility Section* ι_α: U_α → Π: the map from a patch to the record-space
- *Record-Dependency Fiber Order*: the partial order on each fiber induced by source/target record overlap (from T48)

**Proofs Required:**
1. [EST-MATH] The record-dependency order is a valid partial order on fibers (reflexivity, transitivity, antisymmetry) — already established in T48; re-express in bundle language
2. [TaF-ORIG] The accessibility section ι_α determines a well-defined pullback of the global record-dependency order to U_α — this is the apparent-finality order of T56
3. [TaF-ORIG] The section decomposition is compatible with the existing colimit construction of T53

**Dependencies:** T48 (FinaliEvent, record-dependency order), T56 (observer patches, accessibility)

**Estimated Mathematical Difficulty:** 2/5 — standard differential geometry repackaging; no new mathematical content, only reframing

**Publication Readiness:** Publishable as a methods/foundations paper immediately. Target: a short note (4–8 pages) titled "Fiber Bundle Language for Time as Finality: Records, Observers, and Accessibility."

---

### Stage 2: The Record-Space Triple

**Objective:** Define the TaF analog of GU's Observerse — a triple (Σ, Π, {ι_α}) where Σ is the state space, Π is the record-space, and {ι_α} are observer embeddings. Show that TaF's existing observer patches are special cases.

**Imported Mathematics:** [EST-MATH]
- GU Observerse (X^n, Y^d, {ι}): base space, auxiliary space, observer embeddings [from GU §3–§5]
- Three Observerse cases: Trivial (Y=X), Einsteinian (Y=Met(X)), Ambient (Y unconstrained)
- Observer embedding ι: U_x → Y acting simultaneously as: (a) section of Met(X), (b) pullback generator, (c) ambient embedding with normal bundle N_ι, (d) connection splitting

**Structural Analogy:** [CONJECTURE — requires proof that the analogy is exact, not just suggestive]

| GU | TaF |
|----|-----|
| Base space X | State space Σ |
| Auxiliary space Y = Met(X) | Record-space Π = accessibility space over Σ |
| Observer embedding ι: U_x → Met(X) | Accessibility map ι_α: U_α → Π |
| Riemannian metric on X as section of Met(X) | Colimit order as section of finality-order space |
| Normal bundle N_ι (events invisible to ι) | Hidden-intermediary set H_α (intermediaries not in ι_α(U_α)) |

**New Definitions:** [TaF-ORIG]
- *Record-Space Triple* (Σ, Π, {ι_α}): the fundamental TaF structure analogous to the Observerse
- *Einsteinian Record Case*: Π = FinOrder(Σ) = the space of finality orders over Σ; observer ι_α selects a finality order on U_α
- *Observer Normal Bundle* N_α: the set of events globally ordered relative to accessible events but not themselves accessible; this is the hidden-intermediary set of T56

**Proofs Required:**
1. [TaF-ORIG] The Record-Space Triple (Σ, Π, {ι_α}) is well-defined: Σ carries a record-dependency order; Π is a valid space of finality orders; ι_α are well-defined maps
2. [TaF-ORIG] The existing T56 observer cover {U_P, U_A, U_B} is a valid Record-Space Triple with the hidden-intermediary cover as its canonical instance
3. [CONJECTURE] The Observer Normal Bundle N_α encodes exactly the phantom pairs: (e_j, e_i) is a phantom pair at α iff e_k ∈ N_α for some intermediary e_k

**Dependencies:** Stage 1; T56 (observer cover, phantom pairs, accessible events)

**Estimated Mathematical Difficulty:** 3/5 — requires careful formalization of the analogy and proof that the normal bundle captures phantom pairs precisely

**Publication Readiness:** Publishable as an independent paper after proofs 1–2 are complete. Proof 3 can be listed as a conjecture/open problem. Target: "A Record-Space Triple for Time as Finality."

---

### Stage 3: Native vs Invasive Finality Orders

**Objective:** Formalize the distinction between F(U) (locally computed — "invasive") and A(U) (globally restricted — "native") as the TaF analog of GU's native/invasive field distinction. This stage upgrades the T56 finding from an informal observation to a formal theorem.

**Imported Mathematics:** [EST-MATH]
- GU native fields: defined intrinsically on X (Hebrew letters: ג = metric, ℵ = Levi-Civita connection) [GU §4]
- GU invasive fields: defined on Y but pulled back to X via ι* (Greek letters: θ, ψ, φ, etc.) [GU §4]
- Pullback of bundles and sections: ι*(χ) = χ ∘ ι for a Y-native field χ
- The pullback preserves the order of the field structure

**Structural Analogy:** [TaF-ORIG — the distinction is original to T56, here formally labeled]

| GU | TaF |
|----|-----|
| Native to X: ג (metric), ℵ (Levi-Civita) | Native-global: A(U) = ρ_U(S_global) — the global colimit restricted to U |
| Invasive: ι*(χ) pulled back from Y to X | Apparent-local: F(U) = S_local(U) — computed using only ι_α-accessible events |
| Native ≠ Invasive in general | A(U) ≠ F(U) when phantom pairs exist (T56) |

**New Definitions:** [TaF-ORIG]
- *Native Finality Order* at U: A(U) = restrict_order(S_global, acc(U)) — the global finality restricted to U-accessible events
- *Invasive Finality Order* at U: F(U) = S_local(U) — computed locally using only records accessible at U
- *Finality Gap* at U: G(U) = A(U) \ F(U) — the phantom pairs; measures the shortfall of the invasive order
- *Gap Presheaf* G: U ↦ G(U) — requires the Finality Reflection Property (below) to be a presheaf

**Warning: G(U) = A(U) \ F(U) is not automatically a presheaf.** The general result from abstract presheaf theory is: the complement of a subpresheaf F ⊆ A need NOT be a presheaf. The restriction map ρ^A_{UV}: A(U) → A(V) sends G(U) into G(V) only if it satisfies:

  ρ^A_{UV}(a) ∈ F(V)  ⇒  a ∈ F(U)

i.e., non-finality must be stable under restriction (non-finalized things cannot appear finalized at a more restricted observer). This is not entailed by F being a subpresheaf, which only gives the reverse: a ∈ F(U) ⇒ ρ^A_{UV}(a) ∈ F(V). In principle, a global object that looks unresolved could appear resolved after restriction.

**Finality Reflection Property (FRP):** [TaF-ORIG THEOREM — not an additional axiom]

In TaF's specific record model, FRP holds as a provable theorem:

  For any pair of observer patches V ⊆ U (i.e., acc(V) ⊆ acc(U)):  F(V) ⊆ F(U)|_{acc(V)}

Proof: Suppose (a, b) ∈ F(V). Then there is a witnessing chain a = e_0, e_1, ..., e_n = b where each consecutive pair has a direct record dependency (target_records(e_i) ∩ source_records(e_{i+1}) ≠ ∅) and each e_i ∈ acc(V). Since acc(V) ⊆ acc(U), all e_i ∈ acc(U). The same record dependencies hold in U's model (record dependencies are facts about actual records, not observer-relative). Therefore (a, b) ∈ F(U). ∎

Contrapositive: (a, b) ∉ F(U) and both a, b ∈ acc(V)  ⇒  (a, b) ∉ F(V).

This is exactly the condition needed for G to be a presheaf. FRP is a theorem because F(U) is computed from actual record dependencies, and any local witnessing chain at V is automatically a valid chain at U.

**Corollary (G is a presheaf — [TaF-ORIG]):** Under FRP, for V ⊆ U and (a, b) ∈ G(U) with a, b ∈ acc(V): (i) (a, b) ∈ A(V) since the global order is still accessible at V; (ii) (a, b) ∉ F(V) by FRP contrapositive. Therefore (a, b) ∈ G(V). ∎

**Where FRP could fail in TaF extensions:** FRP uses that acc(V) ⊆ acc(U) and that F is computed purely from locally accessible record dependencies. If TaF were extended so that observers had additional local information not represented in the global record structure (e.g., private local clocks, local stabilization signals not encoded in records), a locally observed order pair could appear in F(V) without being witnessed in F(U). Any such extension must verify FRP independently before treating G as a presheaf.

**Proofs Required:**
1. [TaF-ORIG, already in T56] A(U) is a presheaf (functorial under restriction): proven in T56
2. [TaF-ORIG, already in T56] F(U) is not a presheaf in the presence of phantom pairs: proven in T56
3. [TaF-ORIG THEOREM] FRP holds in TaF's record model: proof given above; formalizing this as a standalone lemma is the concrete first obligation before Stages 4–8 proceed
4. [TaF-ORIG COROLLARY] G is a presheaf: follows immediately from proof 3 via the corollary above
5. [CONJECTURE] H⁰(G) ≅ set of phantom witnesses: T56 Q1; requires that global sections of G classify exactly the phantom incomparability witnesses from T51–T52
6. [CONJECTURE] Sheafification of F equals A: T56 Q2; requires constructing the sheafification and verifying it produces A

**Dependencies:** Stage 2; T56 (gap presheaf, H⁰(G), sheafification conjecture)

**Estimated Mathematical Difficulty:** 3.5/5 — proofs 3–4 are now theorems with known proofs; proofs 5–6 remain open sheaf-theoretic problems

**Publication Readiness:** Proofs 1–4 are publishable as a single note establishing FRP and the Gap Presheaf Theorem. Proofs 5–6 are open problems for a follow-up paper "The Gap Presheaf and H⁰ Classification of Phantom Incomparability."

---

### Stage 4: The Finality Connection and Zorro Analog

**Objective:** Define a "Finality Connection" as the TaF analog of GU's Zorro construction — the chain: observer embedding → local finality order → global colimit connection. Show the colimit is the canonical "torsion-free" finality connection.

**Imported Mathematics:** [EST-MATH]
- GU Zorro construction: metric g on X → Levi-Civita ℵ on TX → induced metric g_ℵ on TY → Levi-Civita A₀ on Y [GU §4, §6]
- Connection on a principal bundle: ∇ is a splitting of the Atiyah sequence 0 → ad P → TP/G → TX → 0
- Distinguished connection A₀: the canonical choice parameterized by the observer embedding; acts as reference point for the affine space of connections
- Affine space of connections: A is an affine space modeled on Ω¹(Y, ad(P)); choice of A₀ gives A ≅ N = Ω¹(Y, ad) [GU §6]

**Structural Analogy:** [CONJECTURE — requires proof of each step]

| GU Zorro | TaF Analog |
|----------|-----------|
| Metric g on X | Observer embedding {ι_α}: each α sees partial records |
| Levi-Civita ℵ: unique torsion-free connection for g | Colimit S_global: unique "torsion-free" finality order |
| Metric g_ℵ on TY induced by ℵ | Global ambient presheaf A induced by the colimit |
| Distinguished connection A₀ on Y | Colimit as distinguished finality connection ∇_F |
| Affine space A ≅ N (choice of A₀ gives isomorphism) | Affine space of finality orders; colimit is origin |

**New Definitions:** [TaF-ORIG]
- *Finality Connection* ∇_F: a connection on the observer bundle encoding how the finality order varies smoothly across observers; analogous to A₀ in GU
- *Distinguished Finality Connection*: the specific Finality Connection determined by the colimit S_global; this is the canonical origin of the affine space
- *Affine Space of Finality Orders* A_F: the space of all consistent finality assignments, with the colimit as distinguished origin; modeled on the Record Translation Group N_F (to be defined in Stage 6)
- *Finality Torsion* τ_F: for any finality connection ∇, τ_F(∇) measures deviation from the distinguished connection; τ_F(∇_F) = 0 by definition

**Proofs Required:**
1. [TaF-ORIG] The colimit S_global is a well-defined finality connection — i.e., it satisfies the compatibility axioms that make it a "connection" in this abstract sense; requires defining what "connection" means in the finality context precisely
2. [CONJECTURE] Uniqueness: the colimit is the unique finality assignment with vanishing torsion τ_F = 0; this is the "torsion-free" characterization of the colimit analogous to the Levi-Civita theorem
3. [CONJECTURE] The affine space A_F is well-defined and the colimit is its distinguished origin
4. [TaF-ORIG] Any observer's apparent order F(U) is a "section" of A_F restricted to U; the phantom gap G(U) measures the displacement from the distinguished section A(U)

**Dependencies:** Stages 1–3; T53 (canonical reconstruction failure), T54 (finite descent theorem — four cases of colimit behavior)

**Estimated Mathematical Difficulty:** 4/5 — requires defining "connection" abstractly for a non-smooth finality structure; the Levi-Civita uniqueness analog (proof 2) is the hardest step

**Publication Readiness:** Publishable as a research paper once proof 1 is complete and proof 2 is stated as a theorem with a clear conjecture note. Title: "The Colimit as Distinguished Finality Connection: A Zorro Analog in Time as Finality."

---

### Stage 5: Finality Torsion and the Phantom Incomparability Theorem

**Objective:** Prove that the finality torsion τ_F is the correct invariant for phantom incomparability. Phantom pairs are precisely the non-zero components of τ_F. This upgrades Stage 3's gap presheaf to a theorem about geometric structure.

**Imported Mathematics:** [EST-MATH]
- GU Augmented/Displaced Torsion: T_g = ω − ε⁻¹(d_{A₀}ε) where ε ∈ H, ω ∈ N [GU §7]
- T_g measures the deviation of the group element g ∈ G from the subgroup H_{τ_{A₀}} that stabilizes A₀
- Two connections A and B arise from one group element g via the bi-connection map μ_{A₀}: G → A × A; torsion = their difference
- Torsion as a gauge-covariant object: T_g transforms correctly under H_{τ_{A₀}}

**Structural Analogy:** [CONJECTURE]

| GU Torsion | TaF Finality Torsion |
|-----------|---------------------|
| T_g = ω − ε⁻¹(d_{A₀}ε): deviation from A₀ | τ_F(U) = A(U) \ F(U): deviation of F(U) from A(U) |
| T_g = 0 iff g ∈ H_{τ_{A₀}}: stabilizer of A₀ | τ_F(U) = ∅ iff U has no phantom pairs |
| Two connections A, B from one group element | F(U) and A(U) as two finality orders from one observer |
| Torsion as obstruction to gauge coherence | Phantom gap as obstruction to presheaf coherence |

**New Definitions:** [TaF-ORIG — refining Stage 3]
- *Finality Torsion Tensor* τ_F(U): the formal torsion object at observer U; equals G(U) = A(U) \ F(U) as sets; the theorem characterizes it as a torsion in the geometric sense
- *Torsion-Free Observer*: an observer U where τ_F(U) = ∅, i.e., F(U) = A(U); no phantom pairs
- *Phantom Torsion*: non-zero finality torsion arising specifically from hidden intermediaries (as distinct from other possible sources of A(U) ≠ F(U))

**Proofs Required:**
1. [TaF-ORIG] **Phantom Incomparability Theorem**: (e_j, e_i) is a phantom pair at observer U if and only if (e_j, e_i) ∈ τ_F(U). Proof: direct verification using the definitions of phantom pair (T51), apparent order F(U) (T56), and ambient order A(U) (T56). This proof is likely already implicit in T56 and requires only formalization.
2. [CONJECTURE] The Finality Torsion satisfies gauge covariance under H_F: τ_F(g·U) = Ad(g)τ_F(U) for g ∈ H_F. This requires defining the H_F action on observer patches (Stage 6 dependency).
3. [TaF-ORIG, depends on Stage 3 FRP] G is a presheaf (Finality Reflection Property): established by Stage 3 proof 3. Stage 5 proof 3 should verify FRP holds in the specific cover construction used for the torsion definition — namely that the cover satisfies acc(V) ⊆ acc(U) for all patch-to-overlap restrictions.
4. [CONJECTURE] H⁰(G) = ker(δ⁰: C⁰ → C¹) in a to-be-defined finality cochain complex; the global phantom torsion is the zeroth cohomology of the gap presheaf. This presupposes proof 3 above (G is a presheaf). It connects Stage 3's H⁰(G) conjecture to the torsion language.
5. [CONJECTURE] The Phantom Torsion Theorem: if the hidden-intermediary set H_α is non-empty then τ_F(U_α) ≠ ∅, and conversely. This strengthens proof 1 to a structural statement about the observer normal bundle.

**Dependencies:** Stages 1–4; T51/T52 (phantom incomparability); T56 (gap presheaf H⁰ conjecture); Stage 3 FRP theorem

**Estimated Mathematical Difficulty:** 3.5/5 for proof 1 (verification); 4.5/5 for proofs 2–4 (require Stages 6 definitions)

**Publication Readiness:** Proof 1 is publishable immediately as a formal theorem accompanying T56. Proofs 2–4 are suitable for a follow-up paper once Stage 6 is complete. Title: "Finality Torsion and the Phantom Incomparability Theorem."

---

### Stage 6: The Inhomogeneous Finality Group

**Objective:** Define the symmetry group of TaF's finality structure — the analog of GU's Inhomogeneous Gauge Group G = H ⋉ N. Characterize which transformations preserve the colimit, which ones shift the apparent order, and which ones create or destroy phantom pairs.

**Imported Mathematics:** [EST-MATH]
- GU Inhomogeneous Gauge Group: G = H ⋉ N where H = gauge group (automorphisms of P_H), N = Ω¹(Y, ad(P_H)) = "translations" [GU §6]
- Group law: (ε₁, ω₁)·(ε₂, ω₂) = (ε₁ε₂, Ad(ε₂⁻¹)ω₁ + ω₂)
- G acts on the affine space of connections A: g·A = ε(A − A₀) + A₀ + ω (using distinguished A₀)
- Tilted homomorphism τ_{A₀}: H → G; H embeds in G as the stabilizer of A₀
- G/H_{τ_{A₀}} ≅ N as a principal H-bundle

**Structural Analogy:** [CONJECTURE — requires proof that the semi-direct product structure is valid]

| GU | TaF |
|----|-----|
| H = gauge group Aut(P_H) | H_F = finality gauge group: record-level automorphisms preserving accessibility structure |
| N = Ω¹(Y, ad): ad-valued 1-forms = "translations" | N_F = record-translation group: shifts of the apparent finality order |
| G = H ⋉ N: inhomogeneous gauge group | G_F = H_F ⋉ N_F: inhomogeneous finality group |
| G acts on A: connections are the configuration space | G_F acts on A_F: finality orders are the configuration space |
| Colimit = A₀ is G_F-invariant | Colimit connection is the unique G_F-invariant element |
| G/H_{τ_{A₀}} ≅ N: translations factor out | G_F/H_{F,col} ≅ N_F: phantom-generating translations |

**New Definitions:** [TaF-ORIG]
- *Finality Gauge Group* H_F: the group of bijections on records that preserve the record-dependency partial order and the accessibility structure; the "rigid" symmetries of TaF
- *Record Translation Group* N_F: the group of "shifts" in the apparent finality order — maps that add phantom pairs to F(U) without changing the global colimit S_global
- *Inhomogeneous Finality Group* G_F = H_F ⋉ N_F: group law (h₁, n₁)·(h₂, n₂) = (h₁h₂, Ad(h₂⁻¹)n₁ + n₂) [EST-MATH structure, [TaF-ORIG] content]
- *Colimit Stabilizer* H_{F,col}: the subgroup of G_F that fixes the colimit connection; elements that preserve both the global order and the apparent orders at every observer

**Proofs Required:**
1. [TaF-ORIG] H_F is a well-defined group (closure, associativity, identity, inverses) and acts on the set of finality orders
2. [CONJECTURE] N_F is a well-defined group that acts on the affine space A_F by "translation" (shifting apparent orders without changing the colimit)
3. [CONJECTURE] G_F = H_F ⋉ N_F with the given group law is a valid semi-direct product; this requires proving Ad(h₂⁻¹)n₁ ∈ N_F for h₂ ∈ H_F, n₁ ∈ N_F
4. [CONJECTURE] The colimit is the unique G_F-invariant element of A_F: invariant under H_F (symmetries) and fixed point of N_F (no phantom-generating translations preserve the colimit)
5. [CONJECTURE] G_F acts on phantom pairs: an element n ∈ N_F can create a phantom pair (e_j, e_i) at observer U by adding it to F(U); the torsion τ_F(U) measures this action

**Dependencies:** Stages 1–5; T48 (FinaliEvent, record-dependency order automorphisms)

**Estimated Mathematical Difficulty:** 4.5/5 — the semi-direct product structure must be proven from TaF axioms; the colimit invariance theorem (proof 4) is likely the hardest result in this roadmap

**Publication Readiness:** This stage should begin as a research proposal paper. Proofs 1–2 may be accessible; proofs 3–5 are likely multi-month efforts. A paper could present H_F and N_F as definitions with clear open conjectures. Title: "Symmetries of the Finality Structure: Toward an Inhomogeneous Finality Group."

---

### Stage 7: Shiab-Analog Operators and the Finality Deformation Complex

**Objective:** Construct a TaF analog of GU's Shiab operators and deformation complex. Define operators that count or classify phantom pairs in a gauge-covariant way. Use the deformation complex structure to show that phantom pairs are a cohomological obstruction.

**Imported Mathematics:** [EST-MATH]
- GU Shiab Operators: contraction operators that incorporate the gauge group to overcome the gauge-covariance/contraction incompatibility problem [GU §8]
  - Form: C_φ(ω) = Σᵢ [(Γᵢ⁻¹φᵣ) ⌟ (φₘ ω)] where Γᵢ are Spin(7,7)-invariant elements
  - "Ship in a Bottle" construction: gauge group rotates the bundle-valued part to compensate for asymmetry in form contraction
  - Invariant subspaces {Γᵢ}ᵢ₌₀¹⁴ from Spin(7,7) representation theory (Definition 8.1 in GU)
- GU Deformation Complex [GU §10]: two-step complex
  - ∂₁: Ω⁰(ad) → Ω¹(ad) ⊕ Ω⁰(ad) (linearized gauge action)
  - ∂₂: Ω¹(ad) ⊕ Ω⁰(ad) → Ω^{d-1}(ad) (linearized equations of motion)
  - ∂₂ ∘ ∂₁ = 0 (complex condition); H¹ of this complex classifies infinitesimal deformations of solutions

**Structural Analogy:** [SPECULATIVE — GU's deformation complex is highly specific to Yang-Mills type equations; the TaF analog requires significant original work]

| GU | TaF |
|----|-----|
| Shiab: contraction incorporating gauge group | Finality Contraction: counting operator incorporating H_F-action |
| Deformation complex (∂₁, ∂₂) | Finality Deformation Complex for phantom pairs |
| H¹(deformation complex): moduli of solutions | H¹(phantom complex): moduli of phantom configurations |
| ∂₂ ∘ ∂₁ = 0 (complex condition) | Analogous composition = 0 for phantom maps |

**New Definitions:** [TaF-ORIG]
- *Finality Contraction Operator* C_F: an operator on the finality cochain complex that contracts phantom pairs in an H_F-covariant way; the TaF Shiab analog
- *Phantom Deformation Complex*: 0 → C⁰_F → C¹_F → C²_F → 0 with coboundary maps ∂₁, ∂₂ satisfying ∂₂ ∘ ∂₁ = 0; H¹ of this complex classifies non-trivial phantom configurations
- *Finality Bianchi Identity*: the analog of ∂₂(∂₁(ε)) = 0 in GU; an automatic consequence of the record-dependency order axioms

**Proofs Required:**
1. [CONJECTURE] The phantom deformation complex (∂₁, ∂₂) is a valid cochain complex: ∂₂ ∘ ∂₁ = 0; this requires defining ∂₁ and ∂₂ in terms of TaF operations
2. [CONJECTURE] The Finality Contraction Operator C_F is H_F-covariant: C_F(h·τ) = h·C_F(τ) for h ∈ H_F
3. [SPECULATIVE] Phantom pairs are precisely the H¹ of the phantom deformation complex; this connects the sheaf-theoretic H⁰(G) of T56 to the deformation-complex H¹ — a potentially deep theorem
4. [SPECULATIVE] The Finality Bianchi Identity forces automatic satisfaction of some phantom equations once others are satisfied — the analog of Dirac-pair structure in GU

**Dependencies:** Stages 1–6; T56 (H⁰(G)); full Stage 6 definitions

**Estimated Mathematical Difficulty:** 5/5 — this stage requires both the GU deformation complex machinery and the full Stage 6 group definitions; it is the most technically demanding stage

**Publication Readiness:** Long-term (2–5 years). A research proposal paper can be written now identifying the open problems. First publishable results likely come from proof 1 alone, once ∂₁ and ∂₂ are defined. Title: "A Deformation Complex for Phantom Incomparability in Time as Finality."

---

### Stage 8: Arrow of Time and Pre-Metric Recovery

**Objective:** Investigate whether TaF's record-dependency order — the temporal arrow — can be *recovered* from a pre-metric structure, analogous to GU's claim that spacetime must be recovered from the Observerse rather than presupposed.

**Imported Mathematics:** [EST-MATH]
- GU arrow-of-time observation (§12.2): only in dimension n=1 is ℝⁿ naturally well-ordered. For n > 1, additional structure must be *chosen* to impose an ordering (e.g., indifference curves in consumer theory). GU interprets this as evidence that the temporal arrow is emergent, not fundamental.
- GU spacetime recovery: X^{1,3} must be recovered from the Observerse as an approximation; it is not the fundamental object
- Pull-back of Y-native fields to X via ι*: observation = pull-back; X "sees" Y through the embedding metric
- Metric data transfer as engine of observation (§12.6): the Observerse model as a phonograph/stylus picture — X samples Y, not Y that is derived from X

**Structural Analogy:** [SPECULATIVE]

| GU | TaF |
|----|-----|
| ℝ¹ uniquely well-ordered; higher dimensions need structure | Record-dependency order is unique in 1D; colimit gives the arrow |
| X^{1,3} recovered from Observerse as approximation | Temporal order recovered from record-stabilization structure (T48) |
| Metric on X = section of Y = Met(X) | Apparent order at U = section of the finality order space |
| Arrow of time: emergent from higher structure | Record-dependency order: emergent from accessibility structure, not presupposed |
| Metric data transfer as engine of observation | Accessible records as engine of finality determination |
| Chirality as effective (§12.9): globally non-chiral, locally chiral | Phantom incomparability as effective: globally ordered (e_j ≤ e_i), locally incomparable |

**Research Questions:** [SPECULATIVE]

1. Is TaF's record-dependency order the TaF analog of ℝ¹'s natural well-ordering — the unique order that emerges in the correct dimension from the Record-Space Triple?
2. Can the "arrow of time" in TaF be stated as: *the temporal arrow is the pull-back of the colimit order to each observer's patch, not a prior structure*? If so, this formalizes TaF's central claim in exactly the language GU uses for its own recovery of spacetime.
3. Is phantom incomparability the TaF analog of GU's "effective chirality" (§12.9)? In GU: a globally non-chiral Dirac operator on Y appears chiral on X in low-curvature regions. In TaF: a globally ordered pair (e_j ≤ e_i) appears incomparable (e_j || e_i) to a low-access observer. The formal structure is: a property true globally that is locally undetectable due to insufficient information.
4. Does the Finality Connection ∇_F (Stage 4) determine a natural well-ordering on the records, analogous to the way the Levi-Civita connection determines the metric's geodesics?
5. What is the TaF analog of GU's Dirac-pair structure (§12.5)? GU proposes: first-order equations (Einstein + Dirac) imply second-order equations (Yang-Mills + Klein-Gordon). TaF might have: first-order finality conditions (phantom detection) imply second-order conditions (information flow conservation)?

**New Definitions (if research questions resolve positively):** [SPECULATIVE]
- *Pre-Metric Record Structure*: a Record-Space Triple (Σ, Π, {ι_α}) before any finality order is chosen; the finality order is emergent
- *Finality Chirality*: the observer-relative incomparability of globally-ordered events; effective chirality in the TaF sense
- *Temporal Arrow as Section*: the colimit order as the canonical global section of the finality order bundle, determined by the Record-Space Triple

**Proofs Required:** None yet — this is a research direction. The immediate task is:
1. Formalize research question 1 precisely enough to be a theorem statement
2. Check whether the analogy in question 3 can be made exact (not merely suggestive)
3. Identify whether TaF's T53–T54 canonical reconstruction failure is the TaF analog of GU's "spacetime is not fundamental" claim

**Dependencies:** All Stages 1–7; T53 (canonical reconstruction); T54 (finite descent); T56 (gap presheaf)

**Estimated Mathematical Difficulty:** 5/5 — this is the deepest research direction; results here would be major original contributions

**Publication Readiness:** A position paper or research proposal can be written now, presenting the structural analogies and the five research questions. Publishable as: "Records, Observers, and the Arrow of Time: Toward a Pre-Metric Foundation for Temporal Order."

---

## Dependency Graph

```
Stage 1 (Bundle Language)
    |
Stage 2 (Record-Space Triple)
    |
Stage 3 (Native vs Invasive)
    |
Stage 4 (Finality Connection)
    |
Stage 5 (Finality Torsion)  ←── Stage 6 (Inhomogeneous Finality Group)
    |                              |
    └─────────────────────────────→ Stage 7 (Shiab + Deformation Complex)
                                         |
                                   Stage 8 (Arrow of Time)
```

Stages 4 and 6 can be developed in parallel. Stage 5 depends on both. Stage 7 requires all prior stages.

---

## Immediate Next Steps (Before Any Stage 1 Work)

The following conceptual clarifications are needed before Stage 1 code or proofs begin:

1. **Define "state space" Σ precisely.** In GU, X^n is a smooth Riemannian manifold. TaF's state space is currently implicit — it is the "space of observer situations" that generates different record-dependency orders. This must be formalized.

2. **Check the normal bundle claim.** Stage 2 claims that the hidden-intermediary set H_α ≅ Observer Normal Bundle N_α. This must be verified against the T56 definition of hidden_intermediaries before proceeding.

3. **Audit the circular risk.** Arrow_direction (MEDIUM circular risk in T56 assumption ledger) applies here: several definitions in this roadmap may quietly import temporal directionality. Each Stage 3–8 definition must be checked against the T56 circular risk framework.

4. **Prove the Finality Reflection Property (FRP) as a formal lemma.** G(U) = A(U) \ F(U) is NOT automatically a presheaf from abstract presheaf theory — the complement of a subpresheaf need not be a subpresheaf. The needed condition is: ρ^A_{UV}(a) ∈ F(V) ⇒ a ∈ F(U), i.e., non-finality is stable under restriction. In TaF's specific model this holds as a theorem: any witnessing chain for (a,b) ∈ F(V) uses events in acc(V) ⊆ acc(U), hence witnesses (a,b) ∈ F(U). Formalizing FRP as a standalone lemma is the first concrete mathematical task before Stages 4–8 proceed. The proof is given in Stage 3 above; what remains is stating it precisely and verifying the acc-monotonicity assumption holds in every cover construction used in Stages 4–8.

---

## What This Is Not

- This is not evidence that GU is physically correct
- This is not a claim that TaF provides a quantum gravity theory
- This is not a claim that the structural analogies between GU and TaF are anything other than mathematical analogies
- This roadmap does not import GU's physical interpretation of its mathematical structures; it imports only the mathematical structures themselves (bundles, connections, torsion, deformation complexes, gauge groups)

The value of this roadmap is: GU has developed sophisticated mathematical machinery for dealing with observer-relative measurements and the emergence of spacetime structure. That machinery is relevant to TaF's problem of reconstructing temporal order from stabilized records. The roadmap traces where this borrowing can be made precise.

---

## Appendix: Full GU Concept Inventory

All GU structures encountered in the manuscript (all 69 pages), tagged by TaF relevance:

| GU Concept | Pages | Relevance to TaF | Import Level |
|-----------|-------|-----------------|--------------|
| Observerse (X, Y, {ι}) | 3–10 | Record-Space Triple | Level 2 |
| Einsteinian case Y = Met(X) | 5–8 | Π = finality order space | Level 2 |
| Chimeric bundle C = V ⊕ H* | 4–5 | Local ⊕ global record structure | Level 2 |
| Native fields (Hebrew letters) | 4 | Global ambient order A(U) | Level 2 |
| Invasive fields (pullbacks) | 4–6 | Apparent local order F(U) | Level 2 |
| Normal bundle N_ι | 5, 11 | Hidden-intermediary set | Level 2 |
| Long exact sequence splitting | 4–5 | H⁰(G) decomposition | Level 1 |
| Zorro construction | 6 | Colimit as Levi-Civita analog | Level 2 |
| Observer ι as metric section | 5–6 | Colimit as canonical section | Level 2 |
| Inhomogeneous Gauge Group G = H ⋉ N | 6–7 | G_F = H_F ⋉ N_F | Level 2/3 |
| Distinguished connection A₀ | 6–7 | Colimit connection | Level 2 |
| Affine space of connections | 6, 12 | Space of finality orders | Level 1 |
| Augmented torsion T_g | 7 | Finality torsion τ_F(U) | Level 2/3 |
| Bi-connection map μ_{A₀} | 7 | F(U) vs A(U) from one observer | Level 2 |
| Tilted homomorphism τ_{A₀}: H → G | 6–7 | H_F embeds in G_F | Level 2 |
| Shiab operators | 8, 41–42 | Finality Contraction Operator | Level 3 |
| Ship in a Bottle construction | 8, 41 | H_F-covariant phantom counting | Level 3 |
| Spin(7,7) invariant subspaces {Γᵢ} | 8 | Observer symmetry elements | Level 1 |
| First-order bosonic Lagrangian IB₁ | 9, 43–44 | Phantom detection equations | Level 4/5 |
| Second-order Lagrangian IB₂ | 9, 45 | Information flow conservation | Level 5 |
| Dirac pair structure | 9, 57–58 | First-order → second-order finality | Level 5 |
| Deformation complex (∂₁, ∂₂) | 10, 47–48 | Phantom deformation complex | Level 4/5 |
| Swervature S = Shiab(F) − Displasion | 9, 45 | Gap curvature operator | Level 5 |
| Observed field content (pull-back) | 11, 49–53 | Finality fields on X from Π | Level 3 |
| Three-family problem / imposter gen. | 11, 50–52 | Phantom "impostor" orders | Level 5 |
| Bosonic decompositions (§11.4) | 53–54 | Force-carrying analogs in TaF | Level 5 |
| Arrow of time (§12.2) | 55–56 | TaF temporal arrow as emergent | Level 5 |
| Affine space shift to A (§12.8) | 60 | Connections over metrics for TaF | Level 2 |
| Chirality as effective (§12.9) | 60–62 | Phantom incomparability as effective | Level 5 |
| Imposter third generation (§12.10) | 62–63 | Imposter phantom pairs | Level 5 |
| Metric as engine of observation (§12.6) | 58–59 | Accessible records as engine | Level 2 |
| Spinors chimeric and topological (§12.7) | 59 | Pre-metric finality structure | Level 5 |
| Einstein-Dirac = sqrt(Yang-Mills-Higgs) | 12, 57–58 | Phantom detection = sqrt(info-flow) | Level 5 |
