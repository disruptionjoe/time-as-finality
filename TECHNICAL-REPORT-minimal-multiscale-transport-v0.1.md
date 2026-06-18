# Technical Report: Minimal Multiscale Transport Formalization

**T38 — v0.1**

---

## Summary

T38 asks what the smallest mathematical object is that can express ten core
transport questions. It evaluates five competing hypotheses (H0-H4) against
four executable scenarios and produces a recommendation with a clear boundary.

**Result:** H1+ — TypedTransportNetwork extended with two annotation objects
(CompressionRecord, EmergenceRecord) — is the minimal justified formalism.

H0 (D1RestrictionSystem alone) covers three of ten questions. H1 covers eight.
The remaining two gaps (compression ratio and emergent structure) close with
annotation objects that introduce no new axioms. H2 (graph-of-graphs) and H3
(bundle/presheaf/category) are not yet required by the evidence.

---

## Background

T26 established D1RestrictionSystem as the minimal object for local D1 profile
assignment with trusted transport edges and gluing patch constraints.

T29-T31 established Projection-Obstruction Schema (PO1): a definable projection
from a globally satisfiable richer system to an obstructed restricted system is
a finite Projection-Obstruction instance. Seven admissibility conditions (AC1-AC7)
classify cases.

T34 proved the PO1 Chain Theorem: endpoint admissibility is independent of
whether any source-to-intermediate prefix is admissible.

T37 introduced TypedTransportNetwork and proved the Path-Dependent Admissibility
Theorem: two simple paths between the same endpoints yield different PO1 verdicts
when they accumulate different forgotten_structure. AC5 is the only path-varying
admissibility condition.

T38 is the first attempt to determine whether the transport intuitions that have
accumulated across T26-T37 reflect a genuinely new mathematical object or a
better interpretation of existing structures.

---

## The Ten Core Questions

| Q  | Question |
|----|----------|
| Q1 | What information is transported? |
| Q2 | What information is preserved? |
| Q3 | What information is forgotten? |
| Q4 | What information is compressed? |
| Q5 | What information only exists after transport? |
| Q6 | Can transport skip intermediate organizational levels? |
| Q7 | Can multiple transport channels coexist? |
| Q8 | Are different transport channels composable? |
| Q9 | When do paths produce equivalent observable outcomes? |
| Q10 | When do paths produce fundamentally different structures? |

---

## H0: D1RestrictionSystem Is Sufficient

**Verdict: Rejected (covers Q1-Q3 only).**

D1RestrictionSystem answers Q1 (D1 dimensions are the transported information),
Q2 (preserved_dimensions on D1RestrictionMorphism declares what is retained),
and Q3 (forgotten_structure on ProjectionCase declares what is lost).

It cannot express Q4: a many-to-one morphism from a 4-site source to a 2-site
target can be built, but there is no object to record the compression ratio
(0.5) or that the aggregate accessible_support was retained across the collapse.
forgotten_structure names what was lost; it says nothing about what aggregate
survives.

It cannot express Q5: a target system can be built with globally satisfiable
patches that the source lacked, but there is no object that names this as
emergence — structure created at the target that did not exist at the source.

It has no path concept, so Q6 (level-skip comparison), Q7 (simultaneous
channels), Q8 (path-level composition), Q9-Q10 (path equivalence and
difference) are not expressible.

---

## H1: TypedTransportNetwork Is Sufficient

**Verdict: Best supported with extension (covers Q1-Q3, Q6-Q10; lacks Q4, Q5).**

TypedTransportNetwork (T37) adds path-level tracking. Each NetworkTransport
carries explicit `forgotten_structure` and `preserved_structure`; accumulated
forgotten_structure across a path is the union of individual transport
declarations.

**Q6 (level-skip):** The spectre_network stepwise path (SRC→MID→TGT) and a
direct 2-layer path (SRC→TGT with composed morphism) produce the same PO1
verdict (both admissible). The paths are verdict-equivalent. They are
information-equivalent in this case because MID→TGT forgets nothing; in
general, when an intermediate transport forgets additional structure, the
stepwise and direct paths accumulate different forgotten_structure even with
the same PO1 verdict. TypedTransportNetwork detects this distinction; H0 cannot.

**Q7 (simultaneous channels):** The diamond_network (T37) witnesses two
channels from SRC to TGT producing different PO1 verdicts — the first
positive executable demonstration that simultaneous channels can be expressed
and distinguished.

**Q8 (composability):** `_compose_morphisms(f, g)` chains morphisms by
composing site maps and intersecting preserved_dimensions. Path-level
accumulated forgotten_structure is the union across transports. Composition
associativity remains an open formal obligation.

**Q9-Q10 (path equivalence and difference):** The Path-Dependent Admissibility
Theorem (T37) establishes when paths agree (AC1-AC4, AC6-AC7 are endpoint-
determined) and when they differ (AC5 varies when accumulated forgotten_structure
differs).

**Remaining gap:** H1 has no primitive for compression ratio (Q4) or emergent
structure (Q5). These require annotation objects.

---

## Executable Scenarios

### Compression (Q4): 4-site → 2-site

Source: 4-site system, D1Profile(2,2,2,2) per site, no patches.
Target: 2-site system, D1Profile(4,2,2,2) per site, obstructed (patches requiring
same and different simultaneously — locally satisfiable, globally not).
Morphism: many-to-one — sites {0,1} map to tgt_A; sites {2,3} map to tgt_B.
All four D1 dimensions declared in preserved_dimensions; accessible_support
(2 vs. 4) fails the profile check, so local_profiles_preserved=False.

AC5 = bool(forgotten) AND NOT local_profiles_preserved = True AND True = **True**.

All seven conditions pass: the compression morphism is a **positive PO1 instance**.

CompressionRecord captures: ratio=0.5, retained_invariants=("total_accessible_support",),
lost_detail=("individual_site_profiles", "source_spatial_resolution"),
aggregate_rule="sum_per_merged_pair".

The key observation: the PO1 check fires, but it does not say *why* the
profile changed or *what was retained*. Without CompressionRecord, a compression
that preserves aggregate accessible_support (8 total at source, 8 total at target)
looks identical to a compression that discards it entirely. CompressionRecord is
the minimal object that makes this distinction legible.

### Emergence (Q5): no patches → satisfiable patches

Source: 3-site system, no patches (source has no forced global structure).
Target: 3-site system, patches (A=B, B=C) — globally satisfiable: A=B=C=1 is
a valid global assignment.
Morphism: identity site map, all dims preserved.
Forgotten structure: ("source_unconstrained_freedom",).

AC6 = restricted_gs.obstruction_detected = **False** (target patches are satisfiable).
PO1 = **No**.

This is by design. PO1 requires that the target *loses* a global section the
source had. Emergence is the complementary phenomenon: the target *gains* a
global section the source lacked (source had no patches, hence no forced
coherence). PO1 and emergence are orthogonal.

EmergenceRecord captures: source_patch_count=0, target_patch_count=2,
is_genuine_emergence=True, emergence_kind="coherence_emergence".

Without EmergenceRecord, both "target obstructed (PO1)" and "target gained
coherence (emergence)" are represented by the same D1RestrictionSystem pair.
The distinction is invisible without explicit annotation.

### Level-Skip (Q6): stepwise vs. direct

The spectre_network stepwise path (SRC→MID→TGT) is PO1-admissible.
The direct path (SRC→TGT, composed morphism) is also PO1-admissible.
Verdict-equivalent: **True**.

Both paths accumulate forgotten_structure=("type_guarantee",). The intermediate
MID→TGT transport declares empty forgotten_structure, so stepwise and direct
paths accumulate the same forgotten_structure.
Information-equivalent: **True** in this case.

General principle: when an intermediate transport forgets additional structure,
stepwise and direct paths accumulate different forgotten_structure even though
their PO1 verdicts agree. TypedTransportNetwork detects this. D1RestrictionSystem
alone cannot, because it has no path concept.

### Simultaneous Channels (Q7)

Reuses diamond_network from T37. path_dependent=True. Two paths from SRC to TGT
produce different PO1 verdicts. Confirmed.

---

## Why H2 Is Not Required

H2 would be needed if transport itself had to be transported — if the rules
governing transport between levels were themselves subject to transport between
meta-levels. No current scenario demonstrates this requirement.

Morphism composition already telescopes multi-level transport: a path through
three layers composes the two edge morphisms, producing a single endpoint
morphism. This handles level-spanning without recursive nesting.

The level-skip test shows direct and stepwise transport are verdict-equivalent.
No scenario requires a graph-of-graphs to express any of the ten questions.

H2 remains a legitimate future hypothesis if a scenario requiring transport-of-
transport is ever constructed.

---

## Why H3 Is Not Yet Required

H3 would be needed if identity morphisms, natural transformations, or continuous
fiber structures were required to express the ten questions. No current scenario
demands them.

The composition law (associativity of D1RestrictionMorphisms) is an open formal
obligation. If associativity holds, the existing objects form the morphism half
of a category, making H3 a consequence of H1+ rather than a competing hypothesis.
If associativity *fails*, that failure would be the first positive evidence for H3
— the current composition would not form a category, and a richer structure might
be needed.

Adopting H3 before testing associativity would be premature.

---

## Minimal Multiscale Transport Theorem

**Statement:** TypedTransportNetwork extended with CompressionRecord and
EmergenceRecord (H1+) is the smallest currently justified mathematical object
capable of expressing all ten core transport questions.

**Evidence:**
- H0 covers Q1-Q3 (3/10).
- H1 covers Q1-Q3 and Q6-Q10 (8/10).
- Two annotation objects close Q4 and Q5 without adding new axioms.
- H2 is not required: level-skip is verdict-equivalent; no scenario requires
  transport-of-transport.
- H3 is not required: associativity is open but its absence is a gap in H1, not
  evidence for H3.
- H4 is rejected: H1+ handles all ten questions.

**Boundary:**
- The result holds within the finite D1/T26/T31/T37 framework.
- CompressionRecord and EmergenceRecord are annotation objects; they do not change
  morphism composition or admissibility checking.
- Transport-of-transport (H2 evidence) has not been observed.
- Associativity (H3 prerequisite) has not been tested.
- The ten questions are finite and domain-neutral; continuous or covariant
  generalizations are not addressed.

---

## Recommendation

Adopt H1+ as the current minimal transport formalism.

Add CompressionRecord and EmergenceRecord to the formal object inventory in
FORMALISM.md and MATHEMATICAL-INDEPENDENCE-AUDIT.md.

The composition law (associativity) should be the next formal obligation:
- If it holds, H1+ becomes a proper category fragment (H3 is a consequence, not
  a competitor).
- If it fails, that failure is the first evidence for H3.

Neither H2 nor H3 should be adopted until the composition law is settled.

---

## Addendum: Network-Propagation Audit (Proposed)

Before building beyond T38, there is one audit that should precede any further
structural development: determining whether the typed multiscale transport
formalism developed here reduces to existing multilayer network mathematics, or
whether its added value is specifically the typed obstruction semantics.

**Why this matters:** Multilayer networks, hypergraphs, message-passing frameworks,
and graph-pooling methods are well-studied. If the T26-T38 mathematics is a
special case of one of them, the value of the work is its application to typed
obstruction semantics, not a new structural object. If it is not reducible, there
is a genuine structural contribution worth naming precisely.

**What the audit should compare:**

*Multilayer networks* (Kivelä et al., 2014): layers are graphs; inter-layer edges
connect copies of the same node across layers. The transport direction here is
not inter-layer edges between node copies — it is restriction maps that reduce
site counts and dimension profiles. The forgotten_structure and admissibility
conditions have no multilayer network analogue.

*Hypergraphs*: edges connect sets of nodes. The obstruction pattern (locally
satisfiable patches, globally obstructed) looks like a 2-coloring problem on
a hypergraph. Whether the PO1 admissibility conditions can be rephrased as
hypergraph-coloring constraints is worth checking.

*Message passing (GNNs, belief propagation)*: information propagated from
neighbors, aggregated, transformed. The compression scenario (many-to-one
site map) has surface similarity to graph pooling. The key distinction is that
message passing does not track what is *forgotten* during aggregation, nor does
it check whether the result is a gluing obstruction.

*Graph pooling*: coarsens a graph to a smaller one. Again, no obstruction
semantics, no admissibility conditions, no forgotten_structure tracking.

**Hypothesis to test:** The added value of the T26-T38 formalism over existing
network mathematics is specifically (a) typed forgotten_structure declarations,
(b) PO1 admissibility conditions, and (c) gluing obstruction detection. If this
hypothesis holds, the formalism is not a variant of multilayer networks — it is
a typed obstruction theory that uses graph structure as a substrate.

**Proposed future test (if the audit finds a real gap):** Build a minimal
translation of a known multilayer-network result into the T26/T38 framework and
check whether PO1 admissibility conditions fire or fail. If they fail uniformly,
the obstruction semantics is the distinguishing feature. If they fire on known
multilayer results, the formalism is identifying something the network literature
did not name.

**Action:** Add as a post-T38 research note, not a full test, unless the audit
finds that T38's abstraction is materially misframed by comparison to existing
multilayer mathematics.
