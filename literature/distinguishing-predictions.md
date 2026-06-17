# Distinguishing Predictions

**Purpose:** For each named neighbor of Time as Finality, state: (1) what TaF and the neighbor share,
(2) what TaF claims that the neighbor does not, and (3) the minimum model or experiment that could
distinguish them. This table is required before any external communication — without it, TaF cannot
defend against the charge that it is an elaborate restatement of existing frameworks in new vocabulary.

**Status:** Draft. Entries marked `[OPEN]` need a formal distinguishing criterion. Entries marked
`[PARTIAL]` have a sketch. Entries marked `[READY]` have an explicit criterion ready to test.

---

## Neighbor Map

### 1. Quantum Darwinism (Zurek et al.)

**Shared claim:** Classical records emerge from quantum states through redundant environment encodings.
Observer-accessible facts require environmental fragment sampling.

**TaF-specific claim:** D1's distinct-holder redundancy dimension is the same object as Zurek's
redundancy ratio R_delta (number of independent environment fragments needed to infer system state).
But D1 is a preorder over all four dimensions jointly, not a single redundancy count. A state can
have high R_delta while having low graph-reversal-count finality — these two directions are
orthogonal in D1 but not distinguished in quantum Darwinism.

**Distinguishing criterion:** `[PARTIAL]`
T22 implements the first finite comparison. In a small system-environment toy
model, D1 holder redundancy matches the count of independent informative
environment fragments, while raw informative fragment count diverges because a
readable copy can be correlated with an existing fragment. This makes D1
redundancy closer to independent environmental witness count than raw copy
count.

The remaining T2 extension is a spin-1/2 system plus N-qubit environment. At
each decoherence step, compute both R_delta and D1's four dimension values.
Check whether the redundancy coordinate tracks R_delta monotonically, or
whether states exist with high R_delta but low D1 due to inaccessible fragments,
branch dependence, or reversal cost. A divergence at any point is a genuine
distinguishing case.

**Falsification condition for TaF:** If D1-redundancy and R_delta are numerically identical for
all separable system-environment states, D1 adds nothing over quantum Darwinism's existing account.

---

### 2. Decoherence (Zurek, Joos, Zeh)

**Shared claim:** Quantum states become classical through interaction with the environment. Records
of outcomes form in the environment. Superpositions are suppressed for practical observers.

**TaF-specific claim:** Decoherence explains *how* classical records form dynamically. TaF's D1
asks *which* records count as finalized relative to an observer, and whether finalized records
can be globally consistent. The H1 sheaf obstruction is TaF-native: pairwise-compatible finality
assignments can fail to extend globally. Decoherence has no corresponding global-consistency check.

**Distinguishing criterion:** `[PARTIAL]`
T21 constructs the finite CHSH version of this distinction. Each local measurement context
has valid finality sections and compatible named overlaps, but no global assignment exists.
The probability extension compares classical score `2`, quantum Tsirelson score `2*sqrt(2)`,
and PR-box no-signalling score `4`. Decoherence can say each local context has a classical
record; TaF adds the global-section and CHSH-regime check. The remaining work is a detector-level
or experimental mapping.

**Falsification condition for TaF:** If the H1 sheaf obstruction vanishes whenever all pairwise
decoherence records are formed, TaF's global-consistency check reduces to local decoherence.

---

### 3. Relational Time (Barbour, Page-Wootters)

**Shared claim:** Time has no absolute existence; it is relational — defined by correlations between
physical subsystems. There is no external clock; duration is record-internal.

**TaF-specific claim:** Relational time recovers a total order for clocks in appropriate quantum
states but does not address the question of when a relational record becomes finalized. D1's
graph-reversal-count dimension is not the same as a correlation count — it tracks the cost of
undoing a committed record, not merely the existence of a correlation. High correlation with low
reversal cost is not finalized; high reversal cost with low correlation is finalized but inaccessible.

**Distinguishing criterion:** `[OPEN]`
Construct a Page-Wootters model where the clock-system correlation is well-defined but the record
is physically reversible (e.g., in a coherent trapped-ion system where the entanglement can be
unwound). TaF says this state is not finalized; relational time says it already defines a temporal
fact. Find an observable difference.

**Falsification condition for TaF:** If D1-finality is always equivalent to Page-Wootters
correlation strength, the finalization concept adds nothing beyond relational timing.

---

### 4. Causal Set Theory (Sorkin, Dowker, Henson)

**Shared claim:** Spacetime is a partial order of events, not a smooth manifold at the fundamental
level. Causal structure is the primitive; metric information is derived.

**TaF-specific claim:** T1's causal record graph may satisfy causal set axioms (T15 is the check).
If it does, TaF imports all causal set results. But TaF adds an observer-indexed finality preorder
on top of the causal order — D1 is not identical to the causal partial order because D1 is
observer-relative while causal sets are objective. Two events that are causally ordered in the
causal set may have different D1-finality values for different observers.

**Distinguishing criterion:** `[PARTIAL]`
Run T15: check T1's record graph against causal set axioms (irreflexivity, asymmetry, transitivity,
local finiteness). If it passes, map D1's graph-reversal-count dimension onto the causal set's
irreversibility. Look for an observer where the D1 preorder and the causal partial order diverge.
The divergence is TaF's claim beyond causal set theory.

**Falsification condition for TaF:** If D1 collapses to the causal partial order for any inertial
observer, TaF is a restatement of causal set theory with extra notation.

---

### 5. Thermodynamic Arrow of Time (Boltzmann, Penrose, Carroll)

**Shared claim:** The direction of time is associated with entropy increase. The past is the
low-entropy direction; the future is the high-entropy direction.

**TaF-specific claim:** H7 claims that D1-monotone admissibility induces a temporal direction
without requiring entropy. T9's reversible CA lifts are the test: in zero-entropy substrates,
does finality-induced direction survive? If it does, H7 gives a temporal arrow that is not
thermodynamic. If it doesn't, H7 collapses to thermodynamics.

**Distinguishing criterion:** `[PARTIAL]`
Use T9's reversible-lift results to check whether any reversible CA rule generates a nontrivial
finality direction under D1-monotone admissibility. A reversible CA has zero thermodynamic entropy
production by construction. If H7 assigns a direction in that setting, the direction is not
thermodynamic. T18's constructor model is the finite check; T9's CA family is the next test.

**Falsification condition for TaF:** If D1-monotone admissibility is always equivalent to
entropy non-decrease in physically grounded models, H7 adds no new content.

---

### 6. FLP / CAP Impossibility (Fischer-Lynch-Paterson, Brewer)

**Shared claim:** Distributed systems face fundamental tradeoffs between consistency, availability,
and partition tolerance (CAP) and cannot achieve consensus in fully asynchronous settings with
one faulty process (FLP).

**TaF-specific claim:** T17's D1/progress impossibility result is structurally analogous to FLP/CAP
but is stated in D1 language, not distributed-systems language. The claim is that no D1-admissible
physical process can simultaneously maximize all four D1 dimensions under bounded resource budgets.
This should be provable from D1 axioms alone, not derived by mapping onto FLP.

**Distinguishing criterion:** `[PARTIAL]`
T20 performs the first theorem-transfer check. Quorum-intersection safety transfers from
distributed consensus into physical-record finality without changing proof structure:
`2q > n` plus local consistency blocks incompatible final certificates on both sides.
This is a partial positive result, not yet a TaF-native impossibility floor.

The remaining test is stronger: prove (or disprove) the TaF impossibility theorem in
T17/T19 language without invoking FLP. Construct the minimal D1-model where simultaneous
D1-dimension maximization requires a resource budget exceeding any bound. If the proof
structure does not reference FLP, the result is TaF-native. If it requires FLP as a lemma,
TaF is borrowing rather than deriving.

**Falsification condition for TaF:** If every TaF impossibility result requires importing FLP
or CAP as premises, TaF has no native impossibility floor.

---

### 7. Relational Quantum Mechanics (Rovelli)

**Shared claim:** Quantum states and their values are relative to observing systems. There are no
observer-independent facts about quantum outcomes. Consistency of observations is a derived result,
not a primitive.

**TaF-specific claim:** TaF's H1 sheaf obstruction makes the relativity of facts computable and
topological rather than interpretive. RQM says facts are relative to observers; TaF says the
incompatibility of relative facts is detectable via Cech cohomology and has a topological invariant
(the H1 class). This is a structure that RQM currently lacks — RQM is a framework for when to
apply facts, not a tool for detecting when local facts cannot be globally assembled.

**Distinguishing criterion:** `[OPEN]`
Construct an RQM scenario where two observers have consistent local facts (each correct relative
to themselves) but T13's Cech H1 is nontrivial. RQM says this is fine (no global facts required);
TaF says the obstruction is a detectable topological feature with a physical interpretation.
Find what, if anything, the H1 class predicts that RQM does not.

**Falsification condition for TaF:** If the H1 obstruction is always trivial in situations where
RQM predicts consistent local facts, TaF's cohomology adds nothing over RQM's consistency argument.

---

## Priority Ordering for Formal Development

| priority | neighbor | distinguishing criterion | status |
|---|---|---|---|
| 1 | Decoherence | CHSH contextuality and score comparison | `[PARTIAL]` -> T21 implemented; detector mapping open |
| 2 | Quantum Darwinism | independent fragment count vs D1 holder redundancy | `[PARTIAL]` -> T22 implemented; full T2 dynamics open |
| 3 | Thermodynamic Arrow | T9 reversible CA + H7 check | `[PARTIAL]` → use existing T9 results |
| 4 | Causal Set Theory | T15 axiom check + D1 divergence point | `[PARTIAL]` → implement T15 |
| 5 | FLP/CAP | theorem transfer positive; TaF-native impossibility still open | `[PARTIAL]` -> T20 plus T17/T19 extension |
| 6 | Relational Quantum Mechanics | H1 in RQM scenario | `[OPEN]` → requires new test |
| 7 | Relational Time | Page-Wootters vs D1 reversal cost | `[OPEN]` → requires new test |

---

*Authored 2026-06-17 based on v2 idea sprint convergence analysis.*
*See [explorations/all-persona-idea-sprint-2026-06-16-v2.md](../explorations/all-persona-idea-sprint-2026-06-16-v2.md) for the convergence cluster that identified this as the repo's highest-priority documentation gap.*
