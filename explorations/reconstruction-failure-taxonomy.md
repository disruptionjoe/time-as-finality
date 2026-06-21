# Reconstruction Failure Taxonomy

**Status:** investigation complete
**Date:** 2026-06-19
**Depends on:** T19, T56, T58 (gap-phantom + Bell-H¹), T63, T64, T65, T66, T67, T34, T37, T39, T40
**Prior investigation:** [Boundary Duality and H¹ Reconstruction Failure](boundary-duality-h1-reconstruction-failure.md)
**Question:** Is the repository discovering one obstruction or a hierarchy of reconstruction failures?

---

## Assessment (Lead)

**Answer: a small family of four distinct failure types**, not a single obstruction, not a strict
hierarchy. The four types have specific relationships — two are complementary (A and B), one is
pre-theoretic (C), one is meta-level (D) — but none reduces to another. The structure is a
2+2 arrangement, not a linear ordering.

The proposed hierarchy
```
Visibility → Provenance → Attribution → Cohomological Obstruction
```
does not hold. Types A and B are at the SAME level of fundamentality (one says the
global section doesn't exist; the other says it exists but is inaccessible). Type C
occurs before you even ask whether a global section exists. Type D occurs after you
know an obstruction is present but ask what caused it.

---

## Part A: Reconstruction Failure Table

```
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| Test   | Failure   | Global  | Observer     | Provenance     | H^0  | H^1  | Access | Provenance | Attribution | Notes      |
|        | type(s)   | section | access       | ambiguity      | role | role | role   | role       | role        |            |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T19    | B         | EXISTS  | BLOCKED      | N/A            | FAIL | 0    | PRIMARY| NONE       | NONE        | Temporal   |
|        | (access)  | (ext.)  | (temporal)   |                |      |      |        |            |             | causal     |
|        |           |         |              |                |      |      |        |            |             | boundary   |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T51-T54| B         | EXISTS  | PARTIAL      | N/A            | FAIL | 0    | PRIMARY| NONE       | NONE        | Observer   |
|        | (access)  | (colim.)| (phantom)    |                |      |      |        |            |             | misses     |
|        |           |         |              |                |      |      |        |            |             | intermediary|
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T56/T58| B         | EXISTS  | PARTIAL      | N/A            | FAIL | 0    | PRIMARY| NONE       | NONE        | Gap        |
| (gap)  | (access)  | (global)| (apparent F) |                | H0(G)| vac. |        |            |             | presheaf   |
|        |           |         |              |                |      |      |        |            |             | G = A - F  |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T63    | A         | NO      | N/A          | N/A            | N/A  | !=0  | NONE   | NONE       | NONE        | H1(4-cycle |
|        | (H1)      | (no LC  |              |                |      |      |        |            |             | Z/2Z)=Z/2Z |
|        |           |  assign)|              |                |      |      |        |            |             | computed   |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T65    | A         | NO      | N/A          | N/A            | N/A  | !=0  | NONE   | NONE       | NONE        | Causal     |
|        | (H1)      | (no LC  |              |                |      |      |        |            |             | reduction  |
|        |           |  assign)|              |                |      |      |        |            |             | T63 +      |
|        |           |         |              |                |      |      |        |            |             | spatial    |
|        |           |         |              |                |      |      |        |            |             | boundary   |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T58    | A         | NO      | N/A          | N/A            | N/A  | !=0  | NONE   | NONE       | NONE        | A-B sheaf- |
| (Bell) | (H1,      | (no     |              |                |      | (set)| (direct|            |             | of-sets;   |
|        |  sheaf-   | global  |              |                |      |      | result)|            |             | CHSH > 2   |
|        |  of-sets) | HV)     |              |                |      |      |        |            |             |            |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| PO1    | A         | NO      | N/A          | N/A            | N/A  | !=0  | NONE   | NONE       | SECONDARY   | Gluing     |
| T29-T35| (H1,      | (after  |              |                |      | (CSP)|        |            | (which      | obstruction|
|        |  CSP      | projec. |              |                |      |      |        |            | step lost   | from       |
|        |  equiv.)  |         |              |                |      |      |        |            | AC5?)       | structural |
|        |           |         |              |                |      |      |        |            |             | info loss  |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T34/T37| A+D       | NO      | N/A          | N/A            | N/A  | !=0  | NONE   | NONE       | PRIMARY     | Path-      |
| T39/T40| (H1 +     | (after  |              |                |      |      |        |            | (AC5        | dependent  |
|        |  attrib.  | projec. |              |                |      |      |        |            | path-dep.)  | PO1;       |
|        |  underdet)|         |              |                |      |      |        |            |             | T37 clearest|
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T64    | C         | DEPENDS | YES (direct) | YES (threshold | N/A  | N/A  | CONTEXT| PRIMARY    | NONE        | Threshold  |
|        | (provenace|  on     |              | + independence |      |      | (access|            |             | sensitivity;|
|        |  underdet)| calibr. |              | partition)     |      |      | window)|            |             | T22 audit  |
|        |           |         |              |                |      |      |        |            |             | formal only|
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T66    | C         | DEPENDS | YES (direct) | YES (same      | N/A  | N/A  | CONTEXT| PRIMARY    | NONE        | POVM       |
|        | (provenace|  on     |              | POVM, diff.    |      |      |        |            |             | calibration|
|        |  underdet)| calibr. |              | provenance     |      |      |        |            |             | obstruction|
|        |           |         |              | → diff. D1)    |      |      |        |            |             |            |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T67    | C         | DEPENDS | YES (direct) | YES (identical | N/A  | N/A  | CONTEXT| PRIMARY    | NONE        | Passive    |
|        | (prov.    |  on     |              | agreement but  |      |      |        |            |             | correlation|
|        |  underdet)| prov.   |              | opposite class)|      |      |        |            |             | does NOT   |
|        |           |         |              |                |      |      |        |            |             | recover    |
|        |           |         |              |                |      |      |        |            |             | prov. class|
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
| T59    | A*        | NO      | N/A          | N/A            | N/A  | !=0  | NONE   | NONE       | NONE        | Coeff.     |
|        | (coeff.   | (with   |              |                |      | (Z/2Z|        |            |             | sensitivity:|
|        |  sensitive| correct |              |                |      | only)|        |            |             | scalar     |
|        |  H1)      | coeff.) |              |                |      |      |        |            |             | encoding   |
|        |           |         |              |                |      |      |        |            |             | gives H1=0 |
+--------+-----------+---------+--------------+----------------+------+------+--------+------------+-------------+------------+
```

*N/A = not applicable to this failure type. "DEPENDS" = verdict depends on calibration/provenance choice.*

---

## Part B: Taxonomy Proposal

### Type A — Existence Obstruction (H¹ Failure)

**What fails:** No globally consistent assignment exists. Local sections on each patch are
individually valid but cannot be patched into a global section.

**Preconditions:**
- Cover must have cycle topology (cycle in the nerve graph generates H¹)
- Correct coefficient group required (Z/2Z for binary outcomes; R-modules are too flasque)
- Local sections must exist (Type A is not about accessibility)

**Formal invariant:** H¹(cover, G) ≠ 0 where G = Z/2Z (discrete, sheaf-of-sets) or the
Abramsky-Brandenburger sheaf-of-sets H¹. Equivalently: holonomy of the section around
the cover cycle is non-trivial.

**Characterization:** "The answer cannot exist in this framework."

**Examples in TaF:**
- T63: H¹(4-cycle, Z/2Z) = Z/2Z (direct simplicial computation)
- T65: quantum sections in non-trivial H¹ class; spatial causal-boundary obstruction
- T131 Bell-H¹: H¹ ≠ 0 in sheaf-of-sets; classical bound 2 emerges
- T131 Distributed Contextuality: combined cover H¹ ≠ 0 (Alice and Bob sub-covers H¹ = 0)
- PO1 (T29-T35): gluing obstruction = parity-conflicting binary CSP; H¹-type
- T16: spacetime aggregation gluing obstruction (H¹-type on finality sections)

**Causal explanation:** Some Type A failures have a causal-boundary explanation (T63/T65:
spacelike separation enforces the cycle topology). Others arise from structural information
loss (PO1: projection forgets AC5). The H¹ invariant is the fingerprint; the causal or
structural mechanism is the explanation. Both generate the same obstruction type.

---

### Type B — Accessibility Failure (H⁰ / Gap)

**What fails:** The global section exists. The bounded observer cannot access the witnesses
required to verify it.

**Preconditions:**
- Global section exists (in some ambient sheaf or external record structure)
- Observer's accessible subgraph is a proper subset of the full record graph
- Witnesses for the relevant proposition lie outside the observer's accessible region

**Formal invariant:** H⁰(observer's region, gap presheaf G) ≠ 0 where G = A - F
(ambient minus apparent finality). Equivalently: accessible_support(R, P) = 0 for some
proposition P whose witnesses are outside R's causal past.

**Characterization:** "The answer is there — I just can't reach it."

**Examples in TaF:**
- T19: R cannot self-certify finalization; witnesses in R's causal future
- T51-T54: phantom incomparability; observer misses intermediary event e_k
- T56/T58 (gap-phantom): H⁰(G) = phantom incomparability witnesses; confirmed exhaustively

**Cover topology:** Linear (A*(R) ⊂ G). Mayer-Vietoris: H¹ = 0 for two-element nested cover.

**Causal explanation:** Always temporal or access-boundary. Witnesses exist globally but
are in the observer's causal future (T19) or in a portion of the record graph outside the
observer's access window (T51-T54).

---

### Type C — Provenance Underdetermination

**What fails:** Records exist and are accessible. The reconstruction verdict (D1 finality
score) depends on HOW the records are partitioned into independent witnesses. Physical data
plus causal graph do not canonically determine the provenance partition.

**Preconditions:**
- Records are physically present and accessible (Type B does not apply)
- Two distinct provenance partitions are consistent with the accessible data
- The two partitions give different D1 scores (at least one finality dimension changes)

**Formal invariant:** |{valid provenance partitions giving distinct D1 scores}| > 1.
No scalar observable (correlation, agreement rate, mutual information) computed from
accessible records can discriminate between valid partitions.

**Characterization:** "The answer depends on what we agree to count."

**Examples in TaF:**
- T64: Same detector fragment set gives D1 finalized at threshold 0.75, not at 0.9
- T66: Same calibrated POVM response; local-copy vs independent-readout archives give
  different D1 scores; threshold and provenance are both underdetermined
- T67: Definitive fingerprint — dependent_transport_noisy and independent_exact_overlap
  have identical agreement (0.92) and phi correlation (0.84) but opposite provenance class.
  Passive correlation cannot recover independence partition.

**Why this is distinct from Type B:** The records ARE accessible. The issue is not
visibility but interpretation: two observers with identical data can make incompatible
but equally valid finality assignments depending on how they declare provenance. No
additional record access resolves the ambiguity — only external labeling or intervention.

**Physical consequence:** Q1 has no calibration-free measurement predictions as long as
Type C remains unresolved. A physical theory of provenance classification is needed
before D1 evaluations at the detector level can be grounded.

---

### Type D — Attribution Underdetermination (over Type A)

**What fails:** A Type A obstruction (H¹-type, no global section) exists. The
CAUSE of the obstruction — specifically which projection step lost which structure,
and why that loss generated the obstruction — is not determined by the projection
endpoints alone. Different paths through the same network give different attributions.

**Preconditions:**
- A Type A obstruction is already present (required)
- The projection network has multiple paths between source and target
- Different paths accumulate different forgotten structure (AC5)
- Paths with different AC5 profiles give different PO1 verdicts

**Formal invariant:** For a TypedTransportNetwork with source S and target T:
|{paths P(S→T) with distinct PO1 verdicts}| > 1. Equivalently: AC5 is path-dependent.
(T37 proved: AC1-AC4, AC6-AC7 are endpoint-determined; only AC5 varies by path.)

**Characterization:** "There IS an obstruction — but which step caused it?"

**Examples in TaF:**
- T37: Same source/target node pair; two paths give different PO1 verdicts because AC5
  accumulates differently along the paths
- T34: Chained projection shapes (emergent, stepwise, absorbed) give different obstruction
  signatures for the same base D1RestrictionSystem
- T39: PO1 obstruction = parity-conflicting binary CSP; typed projection (AC5, AC7) is
  the layer that makes attribution possible; without AC5 declaration, cause is unknown
- T40: Holonic obstruction arises from cross-level AC5 in HolonicNetwork; same micro-level
  D1 profile, different holonic PO1 depending on cross-level constraint declaration

**Why this is distinct from Type A:** Type A says an obstruction exists. Type D says the
explanation (which forgotten structure generated it) is underdetermined without AC5 typing.
Type D is a meta-level attribution problem on top of an existing Type A obstruction.
Resolving Type D does not remove the obstruction — it names its cause.

---

### Type A* — Coefficient Sensitivity (Subtype of A)

**What fails:** Type A setup, but the H¹ computation gives trivial or non-trivial results
depending on the coefficient group. The obstruction appears to be present under one encoding
but absent under another.

**Example:**
- T59 (Finite-to-Infinite boundary): Z2 parity coefficient correctly detects the Mobius
  orientation; scalar coefficient encoding produces a false global section (H¹ = 0 spuriously)
- T58 Boolean variant: CHSH parity constraint has holonomy = 0 in Z/2Z under one encoding
  (coboundary); switching to the outcome-comparison encoding gives holonomy = 1 (non-trivial)
- T58 distribution presheaf: H¹ = 0 (sheaf of R-modules is too flasque); H¹ ≠ 0 in
  sheaf-of-sets

**Status:** This is best treated as a methodological risk within Type A rather than a
distinct obstruction type. The correct invariant requires the right coefficient group.
An apparent failure to find H¹ ≠ 0 may be coefficient blindness, not absence of obstruction.

**Warning sign:** When the same cover and local sections give different H¹ under different
encodings, suspect coefficient sensitivity before concluding the obstruction is absent.

---

## Part C: Reduction Analysis

### Does Type B reduce to Type A?

**No.** They are complementary: Type A says the global section does not exist; Type B says
it exists but is inaccessible. You cannot have both simultaneously for the same proposition
and observer. Type B is not a special case of Type A. They require different invariants
(H⁰ of gap presheaf vs H¹ of cover), different cover topologies (linear vs cyclic), and
have different physical implications (accessibility problem vs existence problem).

### Does Type A reduce to Type B?

**No.** In Type A, no external observer can see the global section either — it doesn't
exist. In Type B, the global section exists and is visible externally (just not from the
bounded region). Distinct mechanisms and distinct invariants.

### Does Type C reduce to Type A or B?

**No.** Type C is pre-sheaf-level. The ambiguity is not about whether a global section
exists (Type A) or is accessible (Type B), but about which SHEAF we are computing sections
of. The provenance partition determines which records count as independent witnesses, which
determines D1's value, which determines what "global section" even means in this context.

Type C must be resolved BEFORE the sheaf can be properly defined, and hence before asking
whether a Type A or B failure applies. Type C is logically prior to both A and B.

### Does Type D reduce to Type A?

**Partially.** Type D requires Type A (you need an obstruction before you can ask about
its attribution). But Type D adds genuine new content: the path-dependence of AC5 is not
derivable from the existence of an obstruction alone. Knowing that H¹ ≠ 0 for a projected
system does not tell you which projection step caused it. Type D is Type A plus
underdetermined causal attribution.

Type D does NOT reduce to Type A alone, but it presupposes Type A.

### Does Type D reduce to Type C?

**No.** Type C is about provenance of records (which ones are independent). Type D is
about attribution of obstructions (which projection step lost which structure). They
involve different objects (records in Type C vs projection morphisms in Type D) and
different invariants (partition multiplicity in Type C vs path-dependent AC5 in Type D).

### Summary of reduction results

```
A <--> B: COMPLEMENTARY, neither reduces to the other
A, B --> C: INDEPENDENT of C (C is logically prior)
A --> D: D PRESUPPOSES A but does not reduce to it
B, C, D: NO mutual reductions
```

---

## Part D: Assessment — One Obstruction or a Hierarchy?

### The proposed hierarchy does not hold

```
Visibility → Provenance → Attribution → Cohomological Obstruction
```

This ordering fails for two reasons:
1. Types A and B are at the same logical level (complementary, not ordered)
2. Type C is logically PRIOR to both (affects what the sheaf is), not posterior

### The correct structure: a 2+2 arrangement

```
[Physical data + causal graph]
        |
        | Type C: Provenance partition choice
        | (pre-sheaf: what counts as an independent record?)
        |
[Well-defined finality sheaf on observable record graph]
        |
   _____|______
  |           |
  |           |
Type B:    Type A:
Global     No global
section    section
EXISTS     exists
  |           |
  |           |
Accessible  Inaccessible
locally     from any
(except     bounded
phantom     region
pairs)
  |           |
  |___________|
        |
        | Type D: Attribution (over Type A)
        | (post-obstruction: which step caused this?)
        |
[Obstruction attributed to specific projection step or causal structure]
```

**Two fundamental types (A, B):** complementary existence vs accessibility failures.
Which one applies depends on whether the global section exists (Type A: no) or
exists but is inaccessible (Type B: yes).

**One pre-theoretic type (C):** affects which sheaf we're working with. Must be
resolved before A or B is even applicable. Governs D1 evaluation in detector settings.

**One meta-level type (D):** given Type A, the explanation is underdetermined. AC5
path-dependence adds information about WHERE the obstruction came from.

### Final answer: small family of four reconstruction failure types

The repository is discovering **four distinct reconstruction failure modes**, not a
single obstruction and not a strict linear hierarchy.

The evidence that they are genuinely distinct (not reducible to each other):
1. Type A and B have mutually exclusive global-section status
2. Type C is logically prior to both (affects the sheaf definition)
3. Type D adds content to Type A (attribution) not contained in the obstruction itself
4. Different formal invariants: H¹ (A), H⁰(G) (B), partition multiplicity (C), path-AC5 (D)
5. Different physical implications:
   - Type A: quantum correlations impossible to reproduce by local mechanisms; proof
   - Type B: observer can't self-certify finalization; phenomenal bridge gap (T60+T19)
   - Type C: no calibration-free D1 measurement prediction at detector level
   - Type D: obstruction cause underdetermined without typed network structure

---

## Implications for the Research Program

### For H¹ branch (Type A)

The organizing principle is correct: **cycle topology + right coefficient group = H¹ obstruction**.
Causal boundaries can create cycle topologies (T65: spacelike separation); so can structural
information loss (PO1). Both are Type A. The medium-form theorem target
("causal boundary + cyclic cover → H¹") is a sub-case worth promoting.

The Tsirelson bound (2√2) does NOT emerge from Type A structure alone — it requires QM
amplitude structure, which is outside TaF's finality-presheaf language. The classical
bound (2) does emerge as the global-section threshold.

### For gap-presheaf branch (Type B)

The H⁰(G) = phantom incomparability equivalence is confirmed as the correct invariant.
The T56/T57/T58 gap-phantom program is the formal home of Type B failures. The Finality
Reflection Property (T57) provides the restriction-closure theorem needed for G to be
well-defined as a presheaf.

The next target: connect the T19 temporal-boundary obstruction (accessible_support = 0)
to the gap-presheaf language of T56-T58. Both are Type B; they should unify under
H⁰(bounded region, G).

### For detector branch (Type C)

The clear finding: provenance classification requires **intervention or signed provenance
metadata** (T67 H4 supported). Passive correlation data is insufficient. This is not a
solvable limitation — it is a fundamental ambiguity in what "independent witness" means
without external causal intervention.

This permanently weakens Q1's measurement predictions at the detector level. Q1 can claim
an access-boundary DISTINCTION (Type B: finalized vs inaccessible-but-decoherent) but not
a calibration-free VERDICT (Type C: which records count as independent).

### For typed network branch (Type D)

The attribution problem is real and has a known solution: declaring AC5 (named forgotten
structure) at each projection step. Without AC5, the explanation for an obstruction is
path-dependent and underdetermined. T37 is the clearest witness.

The recommendation is Principle P5 (T33): always name the forgotten structure when
claiming a PO1 obstruction. This converts a Type D situation (obstruction without
attribution) into a Type A situation (obstruction with explicit source).

---

## Open Questions

1. **Does Type C have a formal invariant beyond "partition multiplicity > 1"?**
   Can the underdetermination be measured as, e.g., the dimension of an "equivalence
   class" of valid provenance partitions? A topological or algebraic structure on
   the space of valid partitions would be a Type C invariant.

2. **Is there a long exact sequence connecting Type A and Type B?**
   In sheaf cohomology, H⁰ and H¹ are connected by the long exact sequence
   ... → H⁰ → H⁰ → H¹ → ... for a short exact sequence of sheaves. Could the
   T19/T19-type gap presheaf and the T63/T65-type cycle obstruction be connected
   via such a sequence?

3. **Is Type D purely a naming/typing problem?**
   If we always require AC5 declaration (Principle P5), Type D disappears by
   construction. Does the underdetermination persist under ANY computable projection,
   or is it entirely a consequence of underdeclared structure?

4. **Are there Type A obstructions with no cyclic cover?**
   PO1's CSP structure is cycle-dependent (parity conflict on cycles). Is there a
   Type A obstruction in TaF without a cycle in the constraint or cover structure?

5. **Can Type C be pre-empted by a physical theory of causal independence?**
   If causal graph structure (not just record correlation) determines the independence
   partition, Type C might be resolvable from within TaF. The blocking result (T67)
   shows passive correlation fails. But does the causal structure of the detector chain
   (not correlation, but graph topology) uniquely determine independence class?
