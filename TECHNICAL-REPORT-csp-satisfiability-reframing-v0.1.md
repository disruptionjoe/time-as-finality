# Technical Report: CSP / Satisfiability Reframing (T39) v0.1

**Status:** implemented  
**Tests:** 65/65 pass  
**Best-supported hypothesis:** H_B  
**Model:** `models/csp_satisfiability_reframing.py`

---

## 1. Motivation and Central Question

The D1RestrictionSystem patch language, introduced in T26 and used throughout
T27-T38, is a binary constraint system: each patch imposes "same" or "different"
relations on named variables, and a global section requires a joint satisfying
assignment. This is structurally identical to a binary CSP over a two-value domain.

The central question of T39 is:

> Is PO1 best understood as a finite CSP theorem — satisfiability loss under
> typed projection?

Specifically: does the patch language reduce to known CSP theory so completely
that PO1 adds no new mathematical content, or does PO1 add structure beyond
what CSP satisfiability can express?

---

## 2. Setup

### 2.1 Binary CSP representation

The D1RestrictionSystem patch language maps directly to a binary {-1, 1} CSP:

| D1RestrictionSystem | Binary CSP |
| --- | --- |
| Named variable in patch | Variable |
| Domain: finality / non-finality | {-1, 1} |
| `PatchConstraint(left, right, "same")` | Edge labeled +1 |
| `PatchConstraint(left, right, "different")` | Edge labeled -1 |
| Local patch satisfiability | Local constraint satisfiability |
| Global section | Globally satisfying assignment |
| Gluing obstruction | No joint satisfying assignment |

### 2.2 Witnesses

Four scenarios establish the theorem witnesses:

1. **Minimum direct conflict** (`min_direct_conflict`): 2 variables, 2 patches —
   one "same" and one "different" on the same pair. Minimum D1 obstruction.

2. **Minimum transitive conflict** (`min_transitive_conflict`): 3 variables,
   3 patches — A=B, B=C, A≠C. This is the T26 3-site case. Minimum transitive
   obstruction.

3. **Tree-structured CSP** (`tree_structured`): 4 variables, 3 patches, no
   cycles in the constraint graph. Globally satisfiable.

4. **Satisfiable all-same CSP** (`satisfiable_all_same`): 3 variables, 2 patches,
   all "same" constraints. Globally satisfiable.

Four PO1 bridge cases (from T27, T29, T30) map PO1 to CSP language:
- `witten_1981`, `nielsen_ninomiya`, `synthetic_lossy_no_obstruction`,
  `synthetic_shared_obstruction`.

---

## 3. Theorems

### Theorem 1 — Arc-Consistency Triviality

> Every binary same/different constraint over {-1, 1} is arc-consistent.

**Proof sketch:** The "same" relation contains (left=1, right=1). The "different"
relation contains (left=1, right=-1). Both have a supporting value for every
variable value in {-1, 1}, so every constraint is arc-consistent by definition.

**Implication:** Arc consistency is universally true for our constraint language.
It cannot distinguish obstructed from unobstructed D1 systems. Standard arc
consistency propagation algorithms (AC-3, etc.) provide no information beyond
what is already known from the domain alone.

Verified: all four scenario CSPs are arc-consistent regardless of global
satisfiability.

### Theorem 2 — Signed-Graph Parity

> A binary {-1, 1} CSP with same/different constraints is globally satisfiable
> iff its signed constraint graph contains no negative cycle.

**Setup:** Construct the signed graph G where vertices are variables and each
constraint is an edge labeled +1 (same) or -1 (different). A negative cycle is
a cycle whose edge-label product is -1 (equivalently: odd number of "different"
edges around the cycle).

**Proof sketch:** Assign colors from {-1, 1} to variables via BFS 2-coloring:
start any vertex at color 1; propagate color(neighbor) = color(current) * sign.
A globally satisfying assignment exists iff this coloring is consistent, iff
no two paths between any pair of vertices assign different expected colors.
This occurs iff the graph has no negative cycle. The equivalence follows from
the standard signed-graph 2-colorability theorem (a special case of Harary's
balance theorem for signed graphs).

**Two obstruction subtypes:**
- **direct_parity_conflict**: same pair of variables appears in both a "same"
  and a "different" constraint. Minimum: 2 variables, 2 patches.
- **transitive_parity_conflict**: a cycle of length ≥ 3 with an odd number of
  "different" edges. Minimum: 3 variables, 3 patches (T26 3-site case).

**Verified:**
- `min_direct_conflict`: 2 vars, globally_satisfiable=False, type=direct_parity_conflict.
- `min_transitive_conflict`: 3 vars, globally_satisfiable=False, type=transitive_parity_conflict.
- `tree_structured`: 4 vars, globally_satisfiable=True (no cycles).
- `satisfiable_all_same`: 3 vars, globally_satisfiable=True (all same = no negative cycle).

### Theorem 3 — D1-CSP Equivalence

> `D1RestrictionSystem.global_section().obstruction_detected` equals
> `NOT globally_satisfiable` for the corresponding binary CSP.

This theorem shows that the D1 gluing obstruction and the CSP parity conflict
are the same mathematical object. The D1 machinery (local values, transport
edges, profile checks) wraps the same underlying satisfiability condition.

**Verified on all four scenarios:**

| Scenario | D1 obstructed | CSP obstructed | Equivalent |
| --- | --- | --- | --- |
| min_direct_conflict | True | True | ✓ |
| min_transitive_conflict | True | True | ✓ |
| tree_structured | False | False | ✓ |
| satisfiable_all_same | False | False | ✓ |

### Theorem 4 — PO1-as-CSP

> PO1 is a CSP theorem at the obstruction level. The PO1 gluing obstruction
> maps exactly to a parity-conflicting binary CSP. However, PO1 adds three
> layers not present in standard CSP theory.

**What CSP captures:** The presence or absence of a gluing obstruction.

**What CSP cannot express:**

**(A) Typed source (AC7):**  
PO1 requires the source (richer) system to be globally satisfiable. This
captures the idea that the projection created the obstruction — it was not
already present in the source. Standard CSP has no notion of a "source"
system that was satisfiable prior to the constraint transformation.

**(B) Typed forgotten structure (AC5):**  
PO1 requires the morphism to annotate which structure was forgotten. A
`D1RestrictionMorphism` carries `forgotten_dimensions: tuple[str, ...]`.
This annotation is causally significant: PO1 is admissible only when the
obstruction was *caused by forgetting named structure*, not when the target
was already obstructed independently. Standard CSP has no notion of constraints
being "forgotten with a named annotation."

**(C) Admissibility classification (AC1-AC7):**  
PO1 classifies satisfiability-loss events into:
- Fully admissible (PO1=True): meaningful obstruction created by typed projection.
- Non-admissible: shared obstruction (AC7 fails), no new obstruction (AC6 fails),
  trivial obstruction (AC3/AC4 fail), invalidity (AC1/AC2 fail).

Standard CSP is binary: satisfiable or not. It cannot express whether a
satisfiability change is "meaningful" under a typed morphism.

**Bridge case results:**

| Case | PO1 | Source sat. | Target obstruction | CSP detects | AC5 in CSP | AC7 in CSP |
| --- | --- | --- | --- | --- | --- | --- |
| witten_1981 | True | True | transitive | True | False | False |
| nielsen_ninomiya | True | True | transitive | True | False | False |
| synthetic_lossy_no_obstruction | False | True | none | True | False | False |
| synthetic_shared_obstruction | False | False | transitive | True | False | False |

Note: `synthetic_shared_obstruction` illustrates the AC7 gap precisely — CSP
detects an obstruction in the target, but the source was already obstructed,
so AC7 fails and PO1=False. CSP alone cannot make this distinction.

---

## 4. Hypothesis Verdicts

### H_A — PO1 is entirely reducible to known CSP results

**Verdict: rejected.**

The gluing obstruction is a parity-conflict CSP — a known phenomenon equivalent
to signed-graph 2-colorability / odd-cycle detection (Harary balance theorem).
This part of PO1 is not new mathematics.

However, PO1 adds typed source (AC7), typed forgotten structure (AC5), and
admissibility classification (AC1-AC7) that have no direct CSP analogues. H_A
is rejected because these additions are mathematically substantive: they change
what the framework can express and distinguish.

### H_B — PO1 obstruction = CSP; typed projection and admissibility are new

**Verdict: best supported.**

Theorem 3 establishes the exact equivalence at the obstruction level. Theorem 4
identifies the three gaps (AC5, AC7, classification) and verifies on bridge cases
that CSP alone cannot distinguish PO1-admissible from non-admissible events.

H_B is precise: it credits CSP for what it explains (the obstruction mechanism)
and identifies the genuine new contribution (the classification scheme built on top).

### H_C — admissibility classification is the primary new contribution

**Verdict: partially supported.**

Admissibility classification (AC1-AC7) is part of the new contribution, and
AC5 specifically has no CSP analogue. However, H_C undersells the typed source
(AC7): the requirement that the source system was satisfiable is equally central
to the definition and equally absent from CSP. H_C is correct but incomplete.

---

## 5. Boundary Conditions

The equivalence holds for:
- Binary {-1, 1} domains.
- Constraints limited to "same" / "different" (equality / disequality).

The equivalence may not extend to:
- **Valued CSP (VCSP):** soft constraints with costs. AC5's "named forgotten
  structure" might map to a constraint-violation cost — if forgetting named
  dimensions increases the penalty, VCSP might partially capture AC5. Not yet tested.
- **Algebraic CSP:** polymorphism-based tractability classes. The signed-graph
  parity condition corresponds to the "affine" polymorphism (Schaefer's theorem
  class); it is unknown whether PO1's admissibility conditions correspond to
  additional algebraic structure.
- **N-ary constraints:** D1 profiles could in principle support richer constraint
  types. The current binary framework is both sufficient and maximal for the
  same/different language.

---

## 6. Relation to Prior Work

The signed-graph 2-colorability result is classical (Harary, 1953; Zaslavsky,
1982). The parity-conflict characterization of binary Boolean CSPs is standard
knowledge. T39's contribution is not the parity theorem itself, but the
identification that:

1. The D1RestrictionSystem obstruction is exactly this known structure.
2. PO1 adds a typed classification layer (AC5, AC7, AC1-AC7) on top that has
   no CSP analogue and is the framework's genuine new content.
3. Arc consistency is vacuous for this constraint language (Theorem 1) — a
   result useful for ruling out arc-consistency-based proof strategies.

---

## 7. Next Steps

1. **Valued CSP comparison**: test whether AC5 (named forgotten structure) maps
   to a constraint-violation cost function in VCSP. If so, VCSP partially
   captures PO1's typed projection and the connection strengthens.
2. **Composition law**: verify that PO1-as-CSP is preserved under morphism
   composition. If `f: A→B` and `g: B→C` are both PO1-admissible, is `g∘f`?
3. **Algebraic CSP**: check whether the admissibility conditions (AC1-AC7)
   correspond to known polymorphism classes in the CSP dichotomy theorem context.
