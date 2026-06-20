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

**TaF-specific claim:** D1's holder-redundancy dimension can be compared with a
Quantum-Darwinism-style redundancy ratio `R_delta` after a pointer basis,
fragment partition, observer access boundary, and information threshold are
declared. D1 is still a preorder over all four dimensions jointly, not a
single redundancy count. A state can have high environmental redundancy while
remaining low on branch support or reversal cost.

**Distinguishing criterion:** `[PARTIAL]`
T22 implements the first executable comparison. In a binary pointer-state
environment, raw accessible `R_delta` counts `3` informative fragments, while
the independence-corrected accessible value is `2`, matching D1 holder
redundancy. The divergence occurs because `E3` is a correlated duplicate of
`E1` under the declared independence class.

T2 implements the dynamical version with a system qubit, apparatus pointer,
and three environment fragments. Environmental `R_delta` grows from `0` to
`3`, but an outside observer with no access has D1 profile `(0, 0, 0, 0)`.
This is the current distinguishing case: high environmental redundancy does
not imply observer-relative finality for every observer.

The next extension is noisy scattering and partial decoherence. Check whether
the redundancy coordinate tracks `R_delta` monotonically, or whether states
exist with high `R_delta` but low D1 due to inaccessible fragments, branch
dependence, or reversal cost.

T62 implements the first noisy channel-level audit. It separates total raw
`R_delta`, accessible raw `R_delta`, and independence-corrected accessible
`R_delta`. The key boundary case is `raw_duplicate_boundary`: raw accessible
redundancy is `3`, but independence-corrected D1 holder redundancy is `2`
because one record is a correlated duplicate. This does not refute Quantum
Darwinism; it forces TaF to inherit Quantum Darwinism's fragment-partition
discipline.

T64 moves this into a Stern-Gerlach detector proxy with transient screen,
electronics, local-log, archive, and weak-bath fragments. The positive
distinction survives only after the access window and independence partition
are declared: `redundant_but_before_access` has total `R_delta=3` but D1
profile `(0, 0, 0, 0)`, while `duplicate_archive_boundary` has accessible raw
`R_delta=3` but independence-corrected `R_delta=2`. The threshold sweep
weakens Q1 because the same detector window can be finalized at threshold
`0.75` and not finalized at `0.9`.

T66-T72 narrow this further. Calibrated POVM response matrices do not determine
D1 detector finality, passive pairwise correlations do not recover provenance
classes, and intervention-sensitive provenance works only when trusted metadata
are available before scoring. The robustness result is mixed: T70 survives
moderate single-channel degradation when redundant authenticated channels
remain, but withholds D1 when clock, tag, intervention, and DAG evidence are
jointly missing, forgeable, thresholded, or back-action contaminated. T72 then
replaces the Boolean degradation flags with physical protocol parameters and
adds two unsafe regimes: forged tags can create false independence, and
perturbation back-action can create false dependence.

T74-T75 sharpen the instrumentation boundary. T74 shows robust provenance
recovery is confined to an engineered region under stress priors. T75 then maps
one source-anchored, posterior-modeled photon time-tagging stack into that
region: HydraHarp-class picosecond time tags, White Rabbit synchronization, and
a hash-chained RFC-3161-style signed archive. The unsigned-control variant keeps
timing hardware but mostly withholds D1, so the differentiator is authenticated
provenance infrastructure, not detector timing alone.

T83 compresses the whole branch into a null criterion. At present, the detector
route does not yet distinguish TaF from Quantum Darwinism at the level of new
measurement dynamics. It distinguishes only a stricter admissibility rule for
which already formed detector records may count as evidence. The branch becomes
non-null only if a pre-registered event-level raw-log protocol yields a verdict
that cannot be reduced to passive statistics, dashboard summaries, or post hoc
provenance declarations.

**Falsification condition for TaF:** If D1-redundancy and R_delta are numerically identical for
all separable system-environment states under every admissible access boundary
and independence criterion, D1 adds nothing over quantum Darwinism's existing
account for this dimension.

---

### 2. Decoherence (Zurek, Joos, Zeh)

**Shared claim:** Quantum states become classical through interaction with the environment. Records
of outcomes form in the environment. Superpositions are suppressed for practical observers.

**TaF-specific claim:** Decoherence explains *how* classical records form dynamically. TaF's D1
asks *which* records count as finalized relative to an observer, and whether finalized records
can be globally consistent. The H1 sheaf obstruction is TaF-native: pairwise-compatible finality
assignments can fail to extend globally. Decoherence has no corresponding global-consistency check.

**Distinguishing criterion:** `[PARTIAL]`
T2 constructs the first dynamical decoherence distinction. After environment
copying, pointer coherence is `0.0` and environmental `R_delta` is `3`, but an
outside observer with no access has D1 `(0, 0, 0, 0)`. Decoherence can say a
pointer basis has been environmentally recorded; TaF adds that finality is
still observer-access indexed.

T21 constructs the finite CHSH version of the global-consistency distinction. Each local measurement context
has valid finality sections and compatible named overlaps, but no global assignment exists.
The probability extension compares classical score `2`, quantum Tsirelson score `2*sqrt(2)`,
and PR-box no-signalling score `4`. Decoherence can say each local context has a classical
record; TaF adds the global-section and CHSH-regime check. The remaining work is a detector-level
or experimental mapping.

T62 adds a noisy threshold witness: `decohered_not_darwinist` suppresses the
pointer-coherence proxy below threshold while no individual fragment crosses
the information threshold. This is not uniquely TaF; standard decoherence
versus Quantum-Darwinism language already describes it. TaF's additional
content appears only in the access-boundary and independence-filter witnesses.

T64 adds a detector-shaped version of the same boundary and a no-signalling
guardrail. In the entangled-pair audit, remote setting changes leave the local
noisy detector marginal unchanged. This preserves a necessary physics
constraint, but it is not a novel prediction; it is a failure condition for any
future finality rule.

T83 makes the current comparison more honest. Unless the detector branch beats
its passive-statistics, dashboard, and post hoc partition nulls, TaF is not
competing with decoherence on dynamics. It is only adding a conservative
record-admissibility discipline over detector evidence.

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

T80 performs the first direct bridge between T9 and T18 and weakens the
criterion. A width-3 reversible Rule 30 lift has an injective transition map
and zero logical information-loss bound, but its raw observer-window D1 trace
profile decreases under the physical dynamics. T18 classifies that step as
`strict_definalization`, so D1-monotone admissibility is not automatically
grounded by reversible local dynamics. The remaining discriminator is not
"reversible trace exists"; it is whether an endogenous persistent reconciler
can make retained-record D1 monotone without reducing the effect to
thermodynamic erasure.

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

### 8. Category Theory / Structure-Preserving Maps

**Shared claim:** Many mathematical domains are organized by transformations
that preserve selected structure. Functors, natural transformations, quotient
maps, and homomorphisms already provide general languages for transport.

**TaF-specific claim:** T23 is not claiming novelty for "structure-preserving
maps" in general. The specific claim is that observer access restriction,
consensus-record theorem transfer, and quantum measurement redundancy
extraction can be expressed through one finite typed interface that declares
preserved invariants, allowed losses, and obstruction conditions. The
obstruction field is load-bearing: the weak-quorum boundary must fail rather
than be absorbed as another loose analogy.

**Distinguishing criterion:** `[PARTIAL]`
T23 implements a finite IPT kernel and verifies one positive composition and
one obstruction. The next distinguishing test is a representation theorem:
show that a nontrivial class of admissible TaF transformations must factor
through the IPT interface, or produce a counterexample transformation that
preserves meaningful structure but cannot be represented by the interface.

**Falsification condition for TaF:** If IPT is just an arbitrary restatement
of ordinary structure-preserving maps with no additional obstruction,
allowed-loss, or observer-indexing content, then the IPT layer adds no
mathematical independence.

---

## Priority Ordering for Formal Development

After T23, the top meta-priority is the IPT representation theorem or a
counterexample. The table below preserves the older domain-neighbor ordering.

| priority | neighbor | distinguishing criterion | status |
|---|---|---|---|
| 1 | Decoherence | decohered-but-inaccessible witness plus CHSH contextuality | `[PARTIAL]` -> T2/T21/T62/T64/T66-T81 implemented; real raw-log detector audit still open, and the current detector audit is narrower than its full schema claims |
| 2 | Quantum Darwinism | independent fragment count and observer access vs D1 profile | `[PARTIAL]` -> T22/T62/T64/T66-T81 implemented; signed provenance instrumentation survives only as a pre-registered raw-log route, with trust/pre-registration currently more load-bearing than the rest of the measured schema |
| 3 | Thermodynamic Arrow | T9 reversible CA + H7 check | `[PARTIAL]` → use existing T9 results |
| 4 | Causal Set Theory | T15 axiom check + D1 divergence point | `[PARTIAL]` → implement T15 |
| 5 | FLP/CAP | theorem transfer positive; TaF-native impossibility still open | `[PARTIAL]` -> T20 plus T17/T19 extension |
| 6 | Relational Quantum Mechanics | H1 in RQM scenario | `[OPEN]` → requires new test |
| 7 | Relational Time | Page-Wootters vs D1 reversal cost | `[OPEN]` → requires new test |

---

*Authored 2026-06-17 based on v2 idea sprint convergence analysis.*
*See [explorations/all-persona-idea-sprint-2026-06-16-v2.md](../explorations/all-persona-idea-sprint-2026-06-16-v2.md) for the convergence cluster that identified this as the repo's highest-priority documentation gap.*
