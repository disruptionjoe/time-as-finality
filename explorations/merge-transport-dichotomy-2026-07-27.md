# Connection-Based Route to Finality Gauge Theory: Closed for Merge Transport

**Status:** negative result (no-go), symbolic proof + exhaustive finite corroboration —
the merge-transport sector of the finality-gauge-theory open problem is closed;
the lax-functor route is the surviving formalization
**Date:** 2026-07-27
**Updates:** [../open-problems/finality-gauge-theory-and-gravity.md](../open-problems/finality-gauge-theory-and-gravity.md)
(First Steps 3–4)
**Builds on:** [T111](../tests/T111-d1-gauge-invariance-audit.md) and
[T125](../tests/T125-d1-boundary-connection-transport.md) (entry conditions for the
connection branch); [T242](../tests/T242-compose-meet-total-functor.md) and
[T245](../tests/T245-d1filtered-gr-lax-coherence.md) (the surviving lax route);
`temporal-issuance/absorbers/distributed-systems.md` Absorber 3 (standing
CRDT-merge verdict); verdict-form precedent:
`possibility-to-capability/explorations/2026-07-16-big-swing/lane-B-gate1-functor.md`
**Model:** [../models/merge_transport_dichotomy.py](../models/merge_transport_dichotomy.py)
(exhaustive finite check; exit 0; adversarially re-run before landing)
**Tags:** `finite_witness` · `poly_decider` (the lemmas and the theorem are
general symbolic proofs; the enumeration corroborates them on declared small
universes — it is not the source of the generality, and no hardness or
continuum claim is made)

---

## Verdict

**SPLIT, both horns closed against the connection reading** — the same
adjudicated shape as the P2C Gate #1 precedent (value-blind IMPOSSIBLE /
field-valued constructible-but-underdetermined):

- **Invertible-transport reading of merge transport: CLOSED-TRIVIAL.** If
  parallel transport is instantiated by merge, the invertible sector of the
  transport monoid is exactly `{id}`. A principal/Ehresmann connection exists
  only where no merge ever does anything, and every group-valued holonomy is
  the identity — identically, over every semilattice, graph, and labeling, not
  merely flat for particular connection data (a flat connection can still carry
  nontrivial monodromy; here even that is excluded).
- **Non-invertible reading: OPEN and already under construction.** Merge
  transports are perfectly good non-invertible morphisms; the directed
  comparison-cell formalization (T242's totality-forces-laxity, T245's
  pentagon battery) is the surviving route, untouched and now pointed at.

The open problem's First Steps item 3 (flatness or holonomy audit) therefore
has a forced negative answer **in the merge-transport sector**: no nontrivial
group-valued loop invariant over merge transport can exist, for structural
reasons, before any fixture is built. This is a scope theorem, not an
empirical finding: its content is that the geometric dressing is empty in the
merge sector.

## The dichotomy theorem

**Setup.** A record graph `G` (any finite directed multigraph), a fiber `V` of
states over each node, each edge `e` carrying a merge label `s_e` acting by a
transport map `T_{s_e}: V -> V`; path transport is the composite. The
connection-based reading in the open problem's Working Claim requires path
transports to be fiber isomorphisms — parallel transport in a
principal/Ehresmann connection is invertible by definition — with holonomy the
loop transport, valued in the structure group.

**Lemma 1 (folklore: units of an idempotent monoid are trivial).** Let `M` be a
monoid with identity `e` in which every element is idempotent. If `x` is
invertible, then

```text
x = x·e = x·(x·x⁻¹) = (x·x)·x⁻¹ = x·x⁻¹ = e.
```

So the group of units is `{e}`. Only associativity and idempotence are used;
commutativity is not required, so the lemma covers non-commutative bands.

**Lemma 2 (idempotent endofunctions).** An idempotent `f: V -> V` that is
injective is the identity (cancel the outer `f` in `f∘f = f`); an idempotent
`f` that is surjective is the identity (any `y = f(x)` gives
`f(y) = f²(x) = f(x) = y`). Hence an idempotent is the identity or is neither
injective nor surjective onto its fixed set's complement — in particular,
every non-identity idempotent is non-injective. **No finiteness of `V` is
used.**

**Theorem (merge-transport dichotomy).**

*(i) CRDT horn.* If `(L, ∨)` is a join-semilattice and `T_s(x) = x ∨ s`, then
`T_s ∘ T_t = T_{s∨t}` and `T_s ∘ T_s = T_s`, so `{T_s} ∪ {id}` is a commutative
idempotent monoid and every path composite is a single merge
`T_{join of edge labels}`. By Lemma 1 every invertible transport — single edge
or loop composite — is the identity (and its label is a bottom element); by
Lemma 2 every non-identity transport is non-injective. Under the Ehresmann
demand (all path transports invertible), every edge label acts as the
identity; under the weaker holonomy-only demand (loop composites invertible),
every holonomy element is the identity. By order duality the same holds for
meet-semilattices (`T_s(x) = x ∧ s`), the codomain T242 built.

*(ii) Non-confluent horn.* If merges are merely redelivery-idempotent
(`T_s ∘ T_s = T_s`) but order-dependent — e.g. per-key **arrival-order
override** (note: timestamped last-writer-wins with a total ID order is
confluent and falls under horn (i); the non-confluent case is override by
arrival order) — each transport is still an idempotent endofunction, so by
Lemma 2 it is the identity or non-injective: any edge that genuinely merges is
not a fiber isomorphism and the connection is undefined at that edge. The
holonomy-only fallback also collapses, **on fibers of any cardinality**: in a
bijective composite of idempotent transports the outermost factor is
surjective, hence the identity by Lemma 2; recursing, every factor is the
identity. Note the tempting reading runs exactly backwards: non-confluence is
order-dependence of values, which is what a curvature reading would want to
measure — but it cannot be curvature of a connection, because the comparison
object `T_Q⁻¹ ∘ T_P` does not exist (`T_Q` has no inverse). What survives of
the two-path discrepancy is a directed comparison cell (`x ≤ T(x)` on both
routes), the lax shape, not a group element.

*(iii) Information-destroying horn.* A merge that identifies two distinct
fiber states is non-injective by definition; no fiber isomorphism, no
connection.

**Conclusion.** The connection-based reading of the finality preorder,
instantiated with transports that are merges, hosts only the sector in which
nothing happens: the merge monoid and any structure group intersect only in
the identity.

## Machine check

`models/merge_transport_dichotomy.py` (pure Python, no dependencies, exit 0;
independently re-run in an adversarial pass before landing) checks:
(a) the transport monoid law, commutativity, idempotence, and inflationarity
exhaustively on ALL labeled join-semilattices on ≤ 5 elements — enumerated two
independent ways for n ≤ 4 (poset-with-all-joins and
commutative-idempotent-associative operation tables; counts agree: 1, 2, 9,
76; n = 5 yields 1065, with the poset enumeration guarded against the known
labeled-poset counts 1, 3, 19, 219, 4231) — plus powerset lattices `2^[n]`,
n ≤ 4, and the meet-dual on `2^[3]`; (b) Lemma 1 exhaustively on ALL unital
all-idempotent monoids on ≤ 4 elements including the non-commutative ones
(35 monoids at n = 4, 26 non-commutative; units trivial in all), and Lemma 2
on all endofunctions of sets of size ≤ 6; (c) per semilattice: bijective ⟺
identity ⟺ bottom label, non-identity ⟹ non-injective with an exhibited
collision (6055 transports at n ≤ 5: 425 identities, 5236 non-injective, zero
exceptions), plus a loop demo on `2^{a,h,b,r}` (the D1 dimension universe)
where all 16³ triangle labelings have bijective loop composite iff all labels
are bottom iff the composite is `id`; (d) the arrival-order override witness
(the script's `lww` fixture): redelivery-idempotent, non-confluent (explicit
witness pair), label monoid a non-commutative band with trivial units, every
non-identity transport non-injective, every invertible composite equal to
`id`. The symbolic proofs above carry the generality — including infinite
fibers via Lemma 2 — and the enumeration is corroboration in the
`finite_witness` discipline, not the theorem's source.

## Scope limits — what this does not kill

Stated generously, because the closure is narrow and exact:

1. **The finality preorder itself.** Nothing here touches D1, observer-indexed
   finality comparison, or the comparative structure in the open problem's
   Working Claim. Only one proposed geometric packaging of its transport is
   closed.
2. **Lax/oplax functors into categories with non-invertible morphisms.**
   Idempotents are ordinary morphisms there. This is the surviving
   formalization, and the repo has already built its first two floors: T242's
   total, genuinely lax `gr_semilattice` on `D1FilteredCat_meet`
   (totality forces laxity) and T245's pentagon battery with the named
   `mu_top` repair. Inflationarity (`x ≤ T_s(x)`, machine-checked) supplies
   the directed 2-cell for free. A "loop residue" for merge transport, if one
   exists, lives here — as a directed comparison cell, not a group element.
3. **Curvature-like invariants not built on invertible transport.**
   Simplicial/connectivity/cover-topology obstructions (the Čech-style
   machinery of T63/T65) are untouched. T63's flat-connection dictionary uses
   Z/2-valued transition functions — invertible and non-idempotent
   ((−1)² = +1 ≠ −1) — so that lane's nontrivial holonomy is fully consistent
   with this theorem: gauge structure lives in T111's invertible relabeling
   sector, merges in the idempotent sector, and the theorem says those sectors
   meet only at the identity.
4. **Naturality-based criteria.** Natural transformations require no
   invertibility; naturality squares with idempotent components are legal.
5. **Absorber 3's schema-expanding-merge boundary** (`temporal-issuance/
   absorbers/distributed-systems.md`). Untouched: a schema-expanding
   (D4-level) merge is not an endofunction of a fixed fiber — it leaves the
   lattice — so neither horn applies. The standing verdict "G_ij value-merge
   is absorbed by CRDT theory" is if anything reinforced from the geometry
   side: the CRDT laws that absorb value-merge are the same laws that
   trivialize any connection built on it, so no gauge-theoretic surplus can be
   recovered from the absorbed sector.
6. **T125's provenance-bearing transport object.** Its composition retains
   *ordered* provenance traces — append, not idempotent merge — so the theorem
   does not decide it. The theorem is consistent with T125's finding that
   access-boundary loops retain residual provenance rather than closing as
   identity, but that result is independently derived and not claimed here.
7. **Invertible non-idempotent transport in general.** Transport by genuine
   relabelings (T111's pure-gauge sector) can compose to whatever group it
   likes; ordinary gauge theory is untouched. The theorem only forbids the
   identification *transport = merge* from carrying any of it.

## Relation to the faithful-CRDT-functor question (Nielsen pilot)

The gu-formalization pilot (`gu-formalization/lab/active-research/
calm-gw-boundary/nielsen-protocol-analogy-pilot.md`, second-pass item 1) asks
whether a faithful functor exists between the category of CRDT-style protocols
with conserved observables and the category of lattice fermion algebras with
anomaly-inflow data. This result contributes a constraint, not an answer: any
functor preserves idempotence of endomorphisms, and an invertible idempotent
in any category is the identity (`id = e⁻¹∘(e∘e) = e`); so if the
fermion-algebra-side target supplies only invertible morphisms at the image
(unitaries, gauge transformations, invertible algebra maps), every merge lands
on an identity — the functor collapses all merge structure and cannot be
faithful on any protocol category with a single non-identity merge. A faithful
functor, if it exists, must land in a target with genuinely non-invertible
morphisms (projections, conditional expectations, completely positive maps, or
directed 2-cells). This narrows where the pilot's functor can live; it does
not decide whether it exists.

## Honest novelty framing

Lemma 1 and Lemma 2 are elementary folklore — "a band's group of units is
trivial" is a textbook semigroup exercise, and the transport monoid of a
semilattice acting on itself is its own well-studied object. No mathematical
novelty is claimed for either. The content of this note is the application:
the named open problem proposed a specific formalization target — finality
transport as a connection with curvature — and the folklore lemmas, applied to
the merge instantiation of that transport, close that target's merge sector
exactly and identify which neighboring formalizations survive.

## What This Does Not Claim

- No claim about gravity, curvature as a physical field, the Raychaudhuri
  analog, or any physical observable. Known Physics Constraints: none. No
  physics language is earned or promoted by this note.
- Not a closure of the finality-gauge-theory open problem. Only its
  connection/holonomy-shaped merge-transport sector is closed; the problem
  survives in non-merge (invertible relabeling) and non-invertible (lax,
  simplicial, naturality) forms.
- Not a kill of D1, the finality preorder, T63/T65's Z/2 holonomy lane, or
  T125's provenance transport (see scope limits 3 and 6).
- Not new mathematics. The lemmas are folklore; the contribution is the
  application and the sector boundary it draws.
- Not a general no-go for functors out of merge categories — only for
  functors into invertible-morphism targets. The lax route is explicitly the
  surviving formalization, not collateral damage.
- Not a continuum or scalability claim about the enumeration. The theorem and
  both lemmas are cardinality-free symbolic results; the machine check is
  `finite_witness` corroboration over declared small universes.

## Constructive next object (named, not built)

1. **Directed loop residue on the lax route:** define the loop invariant for
   merge transport as a comparison-cell composite in `D1FilteredCat_meet`
   (T242/T245 vocabulary), after the named `mu_top` repair; decide whether
   any loop's directed residue is non-degenerate where the group-valued
   holonomy provably cannot be.
2. **Sector-boundary audit for T125:** classify each component of the T125
   transport object as idempotent-merge / trace-append / invertible-relabel;
   this theorem then applies component-wise to exactly the first class.
