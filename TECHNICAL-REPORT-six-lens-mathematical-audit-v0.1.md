# Technical Report: Six-Lens Mathematical Audit v0.1

## Purpose

T36 asks whether the T26-T35 framework is converging on a real mathematical
architecture or merely connecting attractive analogies. Six independent
mathematical lenses audited the same repo evidence:

- [Fiber Bundle / Differential Geometry](explorations/T36-fiber-bundle-audit.md)
- [Spin Geometry / Index Theory](explorations/T36-spin-index-audit.md)
- [Sheaf / Cohomology / Local-to-Global](explorations/T36-sheaf-cohomology-audit.md)
- [Category Theory / Functorial Semantics](explorations/T36-category-audit.md)
- [Resource Theory / Monotones](explorations/T36-resource-theory-audit.md)
- [Rich Object -> Observer Shadow Architecture](explorations/T36-rich-object-observer-shadow-audit.md)

The lenses were run independently before synthesis. This report compares them.
It does not average them.

## Executive Verdict

The strongest surviving structure is:

```text
finite rich local system
  -> typed lossy projection / restriction
  -> observer-accessible or restricted shadow
  -> local satisfiability can remain while global assignment disappears
```

This is more than a loose analogy inside the T26-T35 finite framework. It is
not yet a full sheaf theory, category theory, resource theory, index theorem,
fiber bundle theory, or universal theory of observation.

Best current name:

```text
finite projection-created satisfiability-loss schema
```

PO1 remains meaningful, but its strongest honest interpretation is narrower
than some current language suggests. It is a finite local-to-global obstruction
schema under typed lossy projection, with a Boolean global-assignment resource
and explicit boundary cases.

## Convergences From Three Or More Lenses

### 1. Current Core Is Finite CSP / Local-to-Global, Not Full Higher Machinery

All six lenses independently converged on the same base reading:

```text
D1RestrictionSystem = finite sites + local data + patch constraints
PO1 obstruction = locally satisfiable, globally unsatisfiable target
```

The closest existing mathematics is finite CSP, finite relational consistency,
and sheaf/contextuality-style local-to-global obstruction. Sheaf, category,
bundle, resource, and index languages are promising upgrades, not current
theorems.

This is the unexpected convergence of T36: even the differential-geometry,
index-theory, category-theory, and observer-shadow lenses all returned to the
same finite local-to-global core.

### 2. `global_section` Is Future-Right But Presently Overnamed

Fiber, sheaf, category, resource, and architecture lenses all warned that
`global_section()` currently behaves as a global assignment or joint solution.
It can become a sheaf global section only after the repo defines a base
category, section presheaf, restriction maps, and an equivalence theorem.

Recommended current language in prose:

```text
global assignment
joint solution
finite gluing obstruction
```

Recommended future theorem:

```text
T26 global_assignment exists iff a defined finite support presheaf has a
global section.
```

### 3. AC5 Is The Weak Link And Must Become First-Class

Every lens flagged `forgotten_structure` as underdeveloped. Current AC5 depends
on `ProjectionCase` metadata plus measurable profile loss. That is useful as a
guardrail, but not yet intrinsic mathematics.

Different lenses named the same missing object differently:

| Lens | Missing AC5 object |
| --- | --- |
| fiber | projection kernel / lost patch-transport data |
| index | kernel/cokernel or exact-sequence component |
| sheaf | support-presheaf kernel or quotient |
| category | first-class arrow label with composition law |
| resource | typed resource-loss mechanism, not metadata |
| architecture | lost-structure ledger / shadow kernel |

T36 therefore recommends elevating AC5/P5 from metadata to a formal component
of projection arrows.

### 4. Category And Composition Are The Next Bottleneck

Four lenses explicitly called for a category or preorder of finite restriction
systems. The category lens sharpened the issue: current
`D1RestrictionMorphism` preservation arrows and PO1 lossy projections cannot be
the same arrow class.

PO1 needs lossy projection arrows:

```text
objects = valid finite D1RestrictionSystems
arrows = total site maps + declared lost structure + preserved invariants
identity = identity site map + empty loss
composition = composed site maps + accumulated loss data
```

This would turn T34's endpoint-chain behavior into a real composition theorem
instead of a sequence of endpoint checks.

### 5. Distler-Garibaldi Is An Informative Boundary

Index, category, fiber, and architecture lenses all agreed with the repo's
existing treatment: Distler-Garibaldi is not a failed positive PO1 instance.
It is not definable by the current total site-map projection machinery.

Best current language:

```text
not definable in the current T26 site-map formalism
```

Avoid:

```text
PO1 explains Distler-Garibaldi
category change, unless a category is actually defined
```

### 6. T35 Has Real Generative Value But Not Theorem-Discovery Status

Sheaf, category, resource, index, and architecture lenses all treated T35 as a
meaningful finite search over generated projection candidates. None treated it
as automated theorem discovery.

The T35 four-patch witness is especially useful because it is a positive
finite obstruction candidate with no natural spin/index content. That makes it
a hostile counterexample against overidentifying PO1 with index theory.

## Direct Disagreements

### Disagreement 1: Which Upgrade Should Be First?

| Lens | Preferred next upgrade |
| --- | --- |
| sheaf | binary parity / `Z2` obstruction theorem |
| category | lossy projection category and composition law |
| resource | section-availability monotone over a defined free map class |
| index | exact-sequence connecting obstruction, then spin/APS extension |
| fiber | curvature-separation counterexample before connection claims |
| architecture | observer-shadow non-faithfulness theorem |

These are not mutually exclusive, but they imply different next T-goals.

### Disagreement 2: Is "Rich Object -> Observer Shadow" Already Meaningful?

The architecture lens says yes, inside the finite TaF/PO1 framework. The
category lens warns that it is too broad unless typed maps and invariants are
fixed. The sheaf and resource lenses agree with the warning: without a defined
map class, almost any abstraction can be described as rich object to shadow.

Synthesis: meaningful as a finite typed architecture, not as a universal
observation theorem.

### Disagreement 3: How Strong Is The Resource Reading?

The resource lens treats `R(S) = [global_assignment_exists]` as the cleanest
current monotone. The sheaf and resource lenses both warn that T33 overstates
the claim that RMT derives AC5-measurable. A strict resource drop can occur
because patches changed while local profiles stayed identical.

Synthesis: the Boolean resource reading is valuable, but AC5 remains
independent until lost structure is first-class.

### Disagreement 4: How Much Index Meaning Should Witten/NN Carry?

The index lens says Witten and Nielsen-Ninomiya are index-shaped because their
source mathematics is index-relevant. The T35 generic witness shows PO1 itself
is not index theory.

Synthesis: PO1 can model finite shadows of index-relevant loss in specific
examples, but PO1 is not intrinsically index-theoretic.

## Shared Concepts Under Different Terminology

| Shared role | Fiber | Index | Sheaf | Category | Resource | Architecture |
| --- | --- | --- | --- | --- | --- | --- |
| local data | fiber value | local analytic/topological datum | local section/relation | object data | state/resource profile | rich object field |
| compatible whole | section | index-compatible extension | global assignment | limit/equalizer candidate | resource-positive state | coherent shadow |
| loss map | projection | quotient/forgetting | restriction of support | lossy arrow | free operation candidate | observation/shadow map |
| obstruction | patch incompatibility | index-shaped defect | no global assignment | predicate failure | resource drop | shadow non-faithfulness |
| forgotten structure | missing transport/patch | kernel/cokernel | kernel/support data | arrow metadata | mechanism of loss | shadow kernel |

## Repeated Warnings Against Overclaiming

1. Do not call D1RestrictionSystem a sheaf, bundle, category, or resource
   theory yet.
2. Do not call PO1 an index theorem.
3. Do not call trusted transport edges a connection.
4. Do not call projection-created obstruction curvature.
5. Do not call current projections functors.
6. Do not claim T35 discovers theorems.
7. Do not claim PO1 proves source physics, CAP, Git, Spectre, or GU results.
8. Do not claim the rich-object-to-shadow architecture is universal.
9. Do not treat Distler-Garibaldi as a PO1 positive case.
10. Do not treat AC5 as derived until forgotten structure is first-class.

## Structures To Strengthen

- A finite base category of sites, patches, overlaps, and contexts.
- A support presheaf or constrained assignment object.
- A lossy projection arrow with first-class forgotten structure.
- A composition law for loss accumulation across chains.
- A Boolean section-availability monotone over a defined operation class.
- A `Z2` parity obstruction theorem for `same`/`different` fragments.
- A first-class `ObserverShadow(S, O)` object.
- A separation theorem showing current PO1 obstruction is not curvature.

## Structures To Weaken Or Rename

| Current phrase | Recommended posture |
| --- | --- |
| `global_section` in prose | global assignment / joint solution until sheaf theorem |
| `H1_finite_gluing` | finite gluing obstruction unless cohomology is proved |
| `Resource-Monotonicity Theorem` | global-assignment resource principle |
| `Invariant-Preservation Theorem` | invariant-preservation framework |
| `*_functor` labels | informal projection labels |
| category change | not definable by current site-map formalism |
| finality resource | D1 preorder or section-availability resource, depending on context |

## Candidate New Mathematical Objects

1. `D1Proj`: a category or preorder of lossy finite D1 projections.
2. `D1LossyProjection`: total site map plus preserved invariants plus
   first-class forgotten structure.
3. `ProjectionKernel`: formal object replacing informal AC5 metadata.
4. `ObserverShadow(S, O)`: observer/access-dependent view of a rich system.
5. `D1SupportPresheaf`: finite presheaf of assignments satisfying local patch
   constraints.
6. `SectionAvailabilityResource`: Boolean resource
   `[global_assignment_exists]`.
7. `D1GraphConnection`: optional future object with edge transport maps,
   path composition, holonomy, and curvature.

## Candidate Future Theorem Directions

### T37 Candidate: Finite Lossy Projection Category

Define `D1Proj` with valid systems as objects and lossy projections as arrows.
Prove identity, composition, and cumulative P5/loss accumulation. Then restate
T34 as a real composition theorem.

### T38 Candidate: Binary Parity Obstruction Theorem

For binary `same`/`different` constraints, prove that a global assignment
exists iff every cycle has even parity. This would turn the common
three-patch and four-patch witnesses into real `Z2` obstruction cases.

### T39 Candidate: Observer Shadow Non-Faithfulness Theorem

Prove that two valid rich systems can share every scalar, vector, and one-site
observer shadow while differing in global assignment status. This would make
the observer-shadow architecture precise by proving what shadows lose.

### T40 Candidate: Projection Boundary Obstruction

Given a short exact sequence of finite presheaves

```text
0 -> K -> Rich -> Restricted -> 0
```

show when a richer global assignment whose image fails to glue determines a
connecting obstruction. This is the bridge toward sheaf and index theory.

## Candidate Hostile Tests

1. Same-profile resource-drop case: identity site map, identical profiles,
   target patches obstructed. Tests whether RMT really derives AC5-measurable.
2. Curvature separation: flat edge transports with obstructed patches. Tests
   whether PO1 obstruction is distinct from curvature.
3. T35 square witness as non-index case. Tests whether PO1 is broader than
   index theory.
4. Distler-Garibaldi replacement with a richer category-level bridge. Tests
   whether current "non-definable" is a real boundary or a missing arrow type.
5. Blinded Arrow run through T35 before domain interpretation.

## Concrete Audit Findings

Two implementation-facing findings surfaced during T36 verification:

1. T13's advertised nontrivial H1 scenario currently computes:

```text
is_cocycle True
is_coboundary True
h1_is_nontrivial False
```

The tests also assert nontriviality is false. This should be corrected or
renamed before the repo relies on T13 as a nontrivial cohomology witness.

2. T33's `classify_obstruction()` local-failure branch references
`gs.patch_count`, but `GlobalSectionResult` has no such field. A local-failure
probe raises `AttributeError`. This appears to be an unhit branch and does not
affect positive PO1 cases, but it should be fixed before hostile local-failure
classification is trusted.

## Required Final Verdicts

### V1: What Is D1RestrictionSystem?

`D1RestrictionSystem` is best understood as a finite approximation of existing
mathematics: finite CSP, finite relational consistency, and presheaf-ready
local-to-global data. It is not yet a genuinely new mathematical object in the
strong sense. Its novelty is the synthesis with D1 profiles, observer access,
transport metadata, and PO1-style projection auditing.

### V2: What Is PO1 Fundamentally?

PO1 is fundamentally a finite projection-created satisfiability-loss schema.
It has sheaf-obstruction, resource-monotone, and functorial shadows, but none
of those upgrades is fully earned yet. It is not an index theorem, not a
curvature theorem, and not a completed categorical theorem.

### V3: Are AC1-AC7 Natural Or Empirical?

They are partly natural and partly assembled:

- AC1, AC2: natural typing conditions.
- AC3: natural definability condition.
- AC4, AC6, AC7: natural local-to-global obstruction polarity.
- AC5: necessary guardrail, but currently methodological and metadata-based.

AC5 is the least intrinsic condition and should become first-class formal data.
The claim that RMT derives AC5-measurable should be weakened until a theorem
rules out same-profile resource-drop counterexamples.

### V4: Does T35 Explore A Genuine Mathematical Landscape?

Yes, but boundedly. T35 explores a genuine finite landscape of generated patch
systems and projection candidates. It is not a finite category and not
automated theorem discovery. Its scientific value is triage: it finds positive,
boundary, and counterexample structures without domain stories.

### V5: Strongest Next Mathematical Theorem

The strongest next direction is:

```text
Finite Lossy Projection Category + Cumulative P5 Theorem
```

Define a typed arrow class for lossy projections, make forgotten structure a
formal kernel/loss object, prove identities and composition, and then prove
that endpoint PO1 in a chain is controlled by endpoint obstruction polarity
plus accumulated P5.

This theorem is upstream of the other upgrades. It would support sheaf
realization, resource monotonicity, observer-shadow non-faithfulness, and
future index/bundle extensions.

### V6: Is Rich Object -> Observer Shadow Meaningful?

Yes, inside the finite TaF/PO1 framework. The meaningful current architecture
is:

```text
rich finite restriction system
  -> typed lossy projection or observer access map
  -> shadow with preserved invariants and forgotten structure
  -> possible loss of global assignment
```

It is not yet a universal mathematical architecture across GU, quantum theory,
spacetime, cognition, or social systems. It becomes more than analogy only when
the map class, invariants, forgotten structure, and obstruction test are all
typed.

### V7: What Would Falsify The Architectural Hypothesis?

The architectural hypothesis would be weakened or falsified if:

1. No nontrivial arrow class can be defined that composes.
2. AC5 cannot be made first-class without domain-specific storytelling.
3. Generated PO1 candidates reduce to ordinary manufactured CSP artifacts with
   no stable invariants under isomorphism/refinement.
4. Observer shadows cannot be defined without already including the entire
   rich object.
5. Hostile external domains require unrelated machinery each time.
6. The T35 blinded protocol fails to predict boundary/positive cases before
   domain interpretation.
7. Physical D1 observables remain too weak to support the intended observer
   semantics.

## Strongest Single Mathematical Insight

The core insight is not "D1 is a sheaf" or "PO1 is category theory." The core
insight is:

```text
Projection-created obstruction is finite satisfiability loss under typed
forgetting, and the forgotten structure is the missing mathematical object.
```

T36 therefore moves the repo's next frontier from adding more examples to
formalizing the arrow: what it preserves, what it forgets, how forgotten
structure composes, and when loss of that structure creates obstruction.

## Recommendation

Do not promote PO1 beyond `partially_supported`. Instead, narrow the claim:

```text
PO1 is a finite projection-created satisfiability-loss schema with promising
sheaf, category, resource, and observer-shadow extensions.
```

The next major research goal should not be another domain bridge. It should be
a mathematical foundation goal:

```text
T37 Finite Lossy Projection Category and Observer Shadow Kernel
```

Deliverables should include:

- `D1LossyProjection` with first-class loss kernel;
- identity and composition laws;
- cumulative P5 theorem;
- same-profile resource-drop counterexample;
- observer-shadow non-faithfulness witness;
- binary parity obstruction theorem if tractable.

Negative outcomes would be valuable. If no such arrow category exists, PO1
should remain a useful finite classifier rather than a deeper mathematical
architecture.
