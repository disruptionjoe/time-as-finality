# T65: Causal Reduction of CHSH Holonomy

## Target Claims

- [C1: Experienced Time as Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [H6: Phenomenal Bridge Formal-Gap Conjecture](../claims/H6-phenomenal-bridge.md)
- (depends on T63: CHSH Holonomy via Cech H1, and T19: Phenomenal Bridge Separation)

## Origin

Proposed 2026-06-19 in the v2 idea sprint session as the unification step: if T19 shows that
the phenomenal bridge gap is a temporal causal-boundary obstruction and T63 shows that CHSH
non-locality has holonomy = -1 in H^1(CHSH cover, Z/2Z), then a single formal principle should
cover both. T65 asks: is the CHSH holonomy obstruction also a causal-boundary obstruction, and
if so, are T19 and T65 both instances of the same abstract principle?

## Hypothesis

The CHSH holonomy = -1 established in T63 is not merely a topological invariant; it is a
causal-boundary obstruction of the same formal type as T19's phenomenal bridge separation.

Specifically:

- **T19 (temporal):** A bounded observer R cannot verify its own finalization because the
  witnessing records are in R's causal future -- outside R's accessible subgraph A*(R).
- **T65 (spatial):** A locally causal hidden-variable model cannot reproduce quantum CHSH
  correlations because the required joint information P(a,b|x,y) is outside BOTH Alice's and
  Bob's spacelike-separated causal regions.

Both obstructions should be instances of the general principle:
`H^1(cover, Z/2Z) != 0 when globally consistent assignment requires evidence inaccessible from
any bounded causal region in the cover.`

## Decision Problem Formulation

**Input:** The CHSH context cover {U_{A0B0}, U_{A0B1}, U_{A1B1}, U_{A1B0}} arranged in a
4-cycle. A deterministic section s assigning outcome pairs (a, b) to each context.

**Locally causal:** s is locally causal if Alice's outcome for setting A_i is the same in every
context where A_i appears (regardless of Bob's setting), and vice versa for Bob.

**Holonomy:** Product of the four transition functions around the context cycle. Each transition
function = +1 if the shared party's outcome is the same in both adjacent contexts, -1 otherwise.

**Query 1:** Does locally_causal(s) imply holonomy(s) = +1? [Answered: YES]

**Query 2:** Does holonomy(s) = +1 imply locally_causal(s)? [Answered: NO]

**Query 3:** What holonomy do quantum majority-outcome sections have? [Answered: -1]

**Causal reduction:** holonomy(s) = -1 implies NOT locally_causal(s) (contrapositive of Query 1).
Combined with Query 3: quantum sections are not locally causal. This is Bell's theorem as a
holonomy statement.

## Connection to T19, T63, T64

- **T63:** Proved H^1(4-cycle, Z/2Z) = Z/2Z via simplicial cohomology. Computed quantum
  holonomy = -1 for the CHSH context cover. Identified the -1 transition at the
  (A0B1 -> A1B1) edge (Bob_B1 outcome changes when Alice's setting changes).
- **T19:** Proved that a bounded observer R cannot verify its own finalization; the gap is a
  causal-boundary obstruction (temporal: witnesses are in R's causal future).
- **T65:** Reduces CHSH holonomy to a causal-boundary obstruction (spatial: joint information
  is in neither party's region) and establishes the formal parallel between T19 and T65.
- **T64:** (Stern-Gerlach proxy) Does not depend on T65 but provides an explicit physical
  measurement model for the CHSH scenario.

## Setup

1. Enumerate all 16 locally causal sections (a0, a1, b0, b1 in {+1, -1}^4).
2. Compute holonomy for each LC section. Verify all = +1.
3. Compute CHSH value for each LC section. Verify max |CHSH| <= 2.
4. Compute quantum majority-outcome sections at the standard angles
   (theta_A0=0, theta_A1=pi/2, theta_B0=pi/4, theta_B1=-pi/4).
5. Compute holonomy for quantum sections. Verify = -1.
6. Verify |CHSH_quantum| = 2*sqrt(2) (Tsirelson bound).
7. Enumerate all 256 sections (2^8 outcome combinations across 4 contexts).
   Count how many have holonomy = +1. Compare to 16 (number of LC sections).
   This tests whether the biconditional holds.
8. Analyze the -1 transition: identify which edge, which party's outcome changes,
   and what causal region the changing setting belongs to.
9. Construct the formal parallel table with T19.

## Success Criteria

- All 16 LC sections give holonomy = +1.
- Quantum majority-outcome sections give holonomy = -1.
- The -1 transition is at a spatial causal boundary (one party's outcome changes
  when the other party's setting changes, but that setting is outside the first
  party's causal region).
- The formal parallel with T19 is exhibited in a comparison table.
- The causal reduction theorem is stated precisely.

## Failure Criteria

- Any LC section gives holonomy = -1: would contradict the one-direction implication.
- Quantum sections give holonomy = +1: would mean quantum correlations are not in the
  non-trivial H^1 class.
- The -1 transition cannot be identified as a causal-boundary violation.

---

## Step 1 Results -- Causal Reduction Implementation

*Executed 2026-06-19. Code at `models/t65_causal_reduction.py`*

### Run summary

```
PART 1: All 16 locally causal sections have holonomy = +1: True
  CHSH values over LC sections: {-2, +2}
  Max |CHSH| = 2 <= 2 (Bell bound): True

PART 2: Quantum majority-outcome sections have holonomy = -1
  |CHSH_quantum| = 2.828427 = 2*sqrt(2): True (Tsirelson bound)

PART 3: Causal-boundary analysis
  -1 transition at edge (A0B1 -> A1B1)
  Shared setting: Bob_B1 (in Bob's causal region)
  Bob's outcome for Bob_B1: -1 in A0B1, +1 in A1B1
  These two contexts differ only in Alice's setting
  Alice's setting is outside Bob's causal region => CAUSAL VIOLATION

PART 4: Biconditional check (all 256 sections)
  Sections with holonomy = +1: 128
  Locally causal sections:     16
  LC => holonomy = +1: True (one direction verified)
  Biconditional (holonomy = +1 <=> LC): False
  [Holonomy = +1 is necessary but NOT sufficient for LC]

(6) CAUSAL REDUCTION THEOREM: ESTABLISHED
  LC => holonomy = +1 (proved). Quantum => holonomy = -1 (verified).
  Contrapositive: holonomy = -1 => NOT LC. Bell's theorem as holonomy.
```

### What was proved

**One-direction implication (proved exhaustively):**
`locally_causal(s) => holonomy(s) = +1`

Proof structure: an LC section assigns each party's outcome for their setting independently of
the other party's setting. Every transition function compares a shared party's outcome across
two adjacent contexts where only the other party's setting changes. Since the first party's
outcome is context-independent by LC, the shared outcome is the same in both contexts =>
transition = +1. All 4 transitions = +1 => holonomy = (+1)^4 = +1. QED.

**Contrapositive (Bell's theorem in holonomy language):**
`holonomy(s) = -1 => NOT locally_causal(s)`

Quantum majority-outcome sections have holonomy = -1 (verified numerically and structurally
from T63). Therefore: quantum correlations cannot be reproduced by any locally causal mechanism.

### What was disproved (biconditional too strong)

The originally conjectured biconditional `locally_causal(s) <=> holonomy(s) = +1` is FALSE.

The holonomy (product of 4 binary transition functions) equals +1 when 0, 2, or 4 transitions
are -1 (even parity). A section with 2 sign-flips -- e.g., Alice's A0 outcome is inconsistent
across A0B0 and A0B1, AND Bob's B1 outcome is inconsistent across A0B1 and A1B1 -- has
holonomy = (-1)(-1)(+1)(+1) = +1 but is NOT locally causal (neither party's outcomes are
context-independent).

Exhaustive count: 128 of 256 sections have holonomy = +1, but only 16 are locally causal.

### Relationship to T63's coboundary theorem

T63 proved H^1(4-cycle, Z/2Z) = Z/2Z. The abstract coboundary theorem for this computation
says: a 1-cochain on the 4-cycle (with Z/2Z coefficients) is a coboundary iff its holonomy
(product of edge values) equals +1.

A "coboundary" in the abstract topological sense is not the same as a "globally consistent
physical section." A coboundary requires there exist vertex assignments f such that each edge
value = f(target)/f(source) -- this allows edge values of -1 (when the two vertex values
differ). A globally consistent physical section requires ALL edges to be +1 (each party's
outcome is context-independent). So there exist non-LC sections that are abstract coboundaries.

What the coboundary theorem DOES give: sections with holonomy = -1 are in the non-trivial H^1
class, which is incompatible with local causality (by the one-direction implication). This is
the physically meaningful statement. The full biconditional would require sheaf cohomology
with the outcome sheaf, not just abstract Z/2Z coefficients.

### Causal-boundary analysis

The -1 transition is at edge (A0B1 -> A1B1), where the shared setting is Bob_B1. Bob's outcome
for Bob_B1 is -1 in context A0B1 and +1 in context A1B1. These two contexts differ only in
Alice's setting (A0 vs A1). So Bob's outcome for his own setting changes when Alice's setting
changes -- a setting that is spacelike separated from Bob's region.

This is the SPATIAL causal-boundary obstruction: the joint information P(a,b|x,y) needed to
produce a globally consistent assignment is not accessible from Alice's causal region (she lacks
Bob's outcome at measurement time) nor from Bob's (he lacks Alice's outcome and cannot condition
on her setting). The required evidence lives outside both bounded causal regions.

### Formal parallel with T19

```
+-----------------------+--------------------------------+-------------------------------+
| Aspect                | T19 (Phenomenal Bridge)        | T65 (CHSH Holonomy)           |
+-----------------------+--------------------------------+-------------------------------+
| Bounded region(s)     | A*(R) = R's causal past        | U_Alice, U_Bob (spacelike     |
|                       |                                | separated regions)            |
| Evidence inside       | R_obs records                  | a_i (Alice's outcome),        |
|                       |                                | b_j (Bob's outcome)           |
| Evidence outside      | R_self_finality                | P(a,b|x,y): joint             |
|                       | (in R's causal future)         | distribution (neither region) |
| Formal test           | accessible_support = 0         | max CHSH under LHV = 2        |
|                       | for R_self_finality            | < 2*sqrt(2)                   |
| Obstruction           | H^1(self-ref cover) != 0       | H^1(CHSH cover, Z/2Z) = Z/2Z  |
| Gap type              | TEMPORAL: witnesses in         | SPATIAL: joint info in        |
|                       | R's causal future              | neither party's region        |
| What can't be done    | R cannot self-verify           | LHV cannot reproduce          |
|                       | its own finalization           | quantum correlations          |
| Result                | First-person finality          | Bell inequality violated       |
|                       | not computable from A*(R)      | by quantum mechanics          |
+-----------------------+--------------------------------+-------------------------------+
```

### General principle (stated, not yet fully proved)

`H^1(cover, Z/2Z) != 0 when the globally consistent assignment requires evidence inaccessible
from any bounded causal region in the cover.`

The forward direction (causal inaccessibility => non-trivial H^1) is supported by both T19 and
T65. The converse (non-trivial H^1 => causal inaccessibility) requires a more general argument
and remains an open conjecture.

### Status: `partial_success`

- All success criteria met for the core causal reduction claim.
- Biconditional disproved by exhaustive check; corrected to one-direction implication + contrapositive.
- Formal parallel with T19 exhibited.
- General principle stated as a conjecture (forward direction supported, converse open).
- T65 establishes Bell's theorem as a holonomy statement and reduces it to the same formal
  type as the phenomenal bridge separation (T19).
