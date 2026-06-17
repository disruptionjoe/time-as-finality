# Repo Audit And Research Map — 2026-06-10

Scope: full read of README, CLAIM-LEDGER, HYPOTHESES, TESTS, ROADMAP, GLOSSARY, ESSAY, CONTRIBUTING, and all files in `claims/`, `tests/`, `literature/`, `open-problems/`, `guardrails/`, `explorations/`, `personas/`.

Method: audit against the repo's stated purpose (claim-led formalization, explicit failure conditions, stable IDs, claim-class separation, movement toward formal definitions and toy models), then a worth-ranking of next directions scored on novelty, profundity, publishability, and tractability (1–5 each).

Citations named below are candidate prior art from memory. None should enter `literature/` without primary-source verification, per the repo's own no-fake-citations rule.

---

## 1. Repo Purpose Alignment

**Verdict: structurally aligned, substantively incomplete.** The repo behaves like a claim-led formalization project in form — stable IDs, claim classes, guardrails, failure conditions, test specs, a glossary. That discipline is real and unusual for this genre. Five gaps keep it from behaving like one in substance:

1. **No formal artifact exists.** Every file is prose. T1 is named as the central test by C1, D1, D2, A1, and the roadmap, yet no graph, no preorder, no code, no worked example exists anywhere. The toy formalization in ESSAY §8 is the closest thing and it is a sketch. The repo is currently all scaffolding; "formalization project" is aspirational until one model runs.
2. **Promotion discipline was broken.** README says explorations are "kept separate from core claims," but H-Domain and H-Soft-Boundary sit in CLAIM-LEDGER as `conjecture` and `potential_byproduct` while living only in `explorations/`. Either promote them through proper `claims/` files or pull them from the ledger.
3. **Literature is two files, and one is Hoffman.** For a project whose nearest neighbors are Zurek, Rovelli, Halliwell, and Lamport, having interface-theory/trace-logic as the only worked literature note inverts the credibility ordering a technical reader expects.
4. **ESSAY contains unanchored core claims.** Several `[CORE CLAIM]` tags link to C1, but others have no ledger ID at all — notably "Classical objectivity is the high-finality limit of record redundancy" (§4), which is close to quantum Darwinism's central thesis and is presented as this project's claim.
5. **Front-door dilution.** README's Start Here list includes `personas/INDEX.md` (GEB-themed persona dialectics) ahead of any literature, and `personas/INDEX.md` cross-references a `../gu-formalization` repo. Both read as method theater to a hostile technical reviewer and dilute the serious surface.

It is not a manifesto. The guardrails, failure conditions, and "What This Does Not Claim" sections are consistently load-bearing. The fix is not tone; it is producing the first formal object and rebalancing literature.

---

## 2. Claim Integrity

| ID | Clearly stated | Properly classified | Linked to tests/failure | Separated from stronger versions | Guarded | Notes |
|---|---|---|---|---|---|---|
| C1 | Yes | Yes (core) | T1, T5; failure conditions present | Yes | Yes | Failure condition "cannot be reconstructed without primitive time" is not operational — no definition of what counts as smuggled time. See §3. |
| D1 | Yes as prose | Yes (definition) | T1, T5 | Yes | Yes | Four dimensions named, none typed. "Robust under **later** compatible observations" uses temporal language inside the definition the project wants to derive time from. Circularity risk acknowledged for reversal cost only; it applies to robustness too. |
| D2 | Yes | Yes (definition) | T1 | Yes | Yes | Known breadth problem (self-flagged). Near-duplicate of Gell-Mann–Hartle's IGUS concept — currently uncited, which is a prior-art exposure, not just a gap. |
| A1 | Yes | Yes (analogy) | T1, T3, T6 | Yes — strong "How It Could Mislead" | Yes | Best-maintained file in the repo. Open question it doesn't ask: whether Snowball-style metastable convergence is isomorphic to standard statistical-mechanics metastability, which would make the crypto branding removable. |
| Q1 | Yes | Yes (conjecture) | T2, T6 | Mostly | Yes | The proof-carrying paragraph drifts open-problem material into a conjecture file. The decisive failure condition ("adds no clarity beyond decoherence/quantum Darwinism") has no test procedure — the requested comparison note is the test and doesn't exist. |
| R1 | Yes | Yes (conjecture) | T1, T3, T7 | Yes | Yes | Honest. Risk is not overclaim but vacuity: the "claim" may reduce to restating relativity of simultaneity in new vocabulary. T3's job should be stated as deciding exactly that. |
| B1 | Yes | Yes (potential byproduct) | T4, T7 | Yes — extensive non-claims | Yes | Now carries the permeability-spectrum extension imported from explorations, which front-loads heliosphere material into a claim file before D1 exists formally. Dependency inversion. |
| S1 | Yes | Yes (speculative) | T7, open problem | Yes | Yes | Contains its own kill criterion ("turn into a precise proposal or mark rhetorical and remove"). Good. Should be exercised, not just stated — see Track B. |
| H-Domain / H-Soft-Boundary | Yes | **No** — ledger class conflicts with explorations location | T7/T4 nominally | Partially | Yes | Ledger rows without claim files. Also substantively weak: "the record-forming substrate differs across the heliopause" risks being trivially true, and its density-normalization failure condition cannot even be evaluated until D1 is formal. |
| G1–G3 | Yes | Yes | n/a | n/a | n/a | Strong. G3's existence signals how much renderer vocabulary needs guarding — see §6. |
| N1 | Yes | Yes | n/a | n/a | n/a | A list, not a note. Zero citations. |

Ledger mechanics: status values (`revised`, `weakened`, `rejected`) are defined but unused, and there are no dates or change history. A claim ledger that can only ever say "open" doesn't demonstrate the revision behavior it promises. ESSAY's ledger adds a Confidence column (Medium/High) with no stated basis — harmless internally, unjustified quantification to outside readers.

---

## 3. Formalization Gaps

**The root gap: no declared primitive inventory.** The project never states which structures it takes as given and which it derives. Everything below inherits this. The needed statement is roughly: *primitives = a finite set of events/systems, a causal partial order (or record-transfer DAG), and record states; explicitly not primitive = metric time, global simultaneity, experienced temporal order.* Without this, "reconstructed without smuggling primitive time" (H1, T1) is unfalsifiable, because no one can check what was smuggled.

Per concept:

- **Physical finality (D1).** Needs to commit to a mathematical type. ROADMAP says "relation or preorder"; ESSAY §8 says scalar score F_O(p). Pick the preorder: finality as a preorder ⪯_O over (proposition, observer) pairs, with the four dimensions as monotonicity axioms rather than summed components. Each dimension needs a graph-native definition: redundancy = number of edge-disjoint (or node-disjoint) record paths to O; causal accessibility = membership in O's causal past within the DAG; robustness = stability under extension of the graph by records in the causal future of p (causal order, not "later"); reversal cost = minimum number of record deletions/edits that make p non-reconstructible from O's accessible subgraph. All four are definable without time. That single move dissolves most of the circularity worry.
- **Observer as record-bearing system (D2).** The four-condition definition admits nearly every physical system; the file knows it. Fix is a taxonomy with parameters, not a sharper essence: record capacity, trace lifetime, propagation ability. Levels: trace-bearer → recorder → reconciler (can compare records) → conscious observer (out of scope). T1 only needs "recorder" and "reconciler."
- **Record stability.** GLOSSARY defines finality in terms of robustness and defines robustness nowhere. "Stability under later compatible observations" needs "compatible" defined (consistent with p? non-disturbing of p's records?) and "later" replaced with causal-future.
- **Causal accessibility.** Used throughout, defined relative to nothing. In the toy model it is reachability in the record DAG; in physics-facing prose it is the past light cone. Say both, and say which is in force in which file.
- **Reversal cost.** Currently the most hand-waved dimension and the most physical one. Two candidate formalizations, which disagree: (a) graph-theoretic erasure count (above); (b) thermodynamic — Landauer cost of resetting the correlated records. T5 should be reframed as deciding the relationship between (a) and (b); if they diverge, that divergence is informative content the project can own.
- **Temporal reconstruction (H1c/T1).** The deepest unsolved formal problem: what is the *target* of reconstruction? In a toy model the "experienced temporal order" is whatever the modeler built in, so success risks triviality. The non-trivial theorem shape: *the stabilization order of F_O is a linear extension of the causal partial order restricted to O's accessible record events, invariant under [class of graph perturbations], and not assumed in the construction of F_O.* State the theorem target before building the model, or the model proves nothing.
- **Partial order vs preorder language.** The repo uses "partial order" for causal structure (correct) and floats "preorder" for finality (correct instinct: distinct propositions can be finality-equivalent, so antisymmetry should not be assumed). Fix the vocabulary in GLOSSARY: causal structure = partial order on events; finality = preorder on propositions indexed by observer. One glossary entry each, used consistently.

---

## 4. Testability Gaps

Status: 8 test specs, 0 tests. All are well-formed as specs (target claims, success/failure criteria). What's missing per roadmap priority:

- **T1 (finite causal record graph) — highest priority, fully tractable now.** Needs: declared primitives (§3), the theorem target above, and ~100 lines of code. A 6–10 node DAG with two observers, one spacelike-independent record pair, one access-loss event, and one erasure event would exercise every success and failure criterion already written. Until T1 exists, C1, D1, and D2 have no real failure exposure — their failure conditions are listed but nothing can currently trigger them.
- **T2 (quantum measurement record finality) — tractable with effort.** Concrete path: a system + apparatus + N environment-fragment qubit model (standard quantum Darwinism setup, simulable in QuTiP), compute fragment–system mutual information, then show what F_O adds beyond Zurek's redundancy measure. Honest possible outcome: nothing — which triggers Q1's stated failure condition. The test should say that outcome is acceptable and would downgrade Q1 to `weakened`.
- **T3 (spacelike ordering / no global commit order) — tractable now, mostly a discipline exercise.** Two inertial observers, one Minkowski diagram, a table of which orderings are frame-dependent vs invariant, and an explicit verdict on whether finality language adds anything beyond relativity of simultaneity. The likely verdict ("it is interpretive vocabulary, not new structure") should be written down as the success outcome, not avoided.
- **T4 (black-hole causal access boundary) — not tractable beyond careful prose; correctly sequenced last by ESSAY §12.** Deliverable when reached: a Penrose-diagram-based classification of record classes (exterior-accessible, boundary-encoded, interior-local) reviewed by someone with GR competence. No code path exists.
- **T5 — under-specified but critical.** Currently framed as support; should be framed as a kill-test: *does D1-finality reduce to entropy production + decoherence + Landauer erasure?* If yes, D1 is renaming. This is the project's most important single question and no file states it that bluntly.
- **T6 — tractable; fine as written.** Should be sequenced after T1 since it presupposes the record-graph substrate.
- **T7 — the Voyager worked example is real content, but it currently tests H-Domain (an improperly promoted claim) more than R1/B1/S1.** Re-scope or re-target.
- **T8 — weakest test.** Its own failure criterion ("adds no clarity beyond ordinary cognitive-science language") is probably already met by predictive-processing and world-model literature. Candidate for deferral (Track B).

Claims with no real failure exposure today: **C1, D1, D2** (waiting on T1), **S1** (waiting on a decision, not a test), **H-Domain/H-Soft-Boundary** (failure condition unevaluable until D1 is formal).

---

## 5. Literature / Prior-Art Risk

Ordered by exposure. All citations below are from memory and must be verified before entering `literature/`.

1. **D2 vs Gell-Mann & Hartle's IGUS (information gathering and utilizing system) — highest collision risk.** "Observer = record-bearing system, consciousness is a special case" is nearly the IGUS definition from the decoherent-histories program (Gell-Mann & Hartle, early 1990s; Hartle's "The Physics of Now," Am. J. Phys. 2005). Uncited, D2 looks like reinvention.
2. **C1/T1 vs records theory in decoherent histories.** Halliwell has a body of work on records and reconstructing histories from records (e.g., PRD 1999, "Somewhere in the universe: where is the information stored when histories decohere?"). This is the closest technical neighbor to the T1 program itself. N1 names "records theory in quantum gravity" as a bullet; it needs a real note before T1 is built, to know what would be new.
3. **D1-redundancy vs quantum Darwinism.** "Classical objectivity is the high-finality limit of record redundancy" (ESSAY §4, tagged CORE CLAIM) is close to Zurek's thesis (RMP 2003; Nature Physics 2009; Ollivier–Poulin–Zurek PRL 2004). Either tag it `[KNOWN NEIGHBOR]` or write the note that says precisely what D1 adds (candidate answer: the other three dimensions, the observer-indexing, and the preorder packaging).
4. **A1/R1 vs Lamport.** Lamport's "Time, Clocks, and the Ordering of Events in a Distributed System" (CACM 1978) explicitly built the happened-before partial order on the analogy with special relativity. The bridge the repo treats as its novel contribution has run in the *other direction* for ~48 years. Citing Lamport converts A1 from possible reinvention into a deliberate round trip: physics → distributed systems (1978) → back to physics with finality vocabulary (this project). That is a genuinely good story, but only if claimed knowingly. Vector clocks and CRDT literature are secondary anchors.
5. **C1 vs the records-based arrow in philosophy of physics.** Reichenbach (*The Direction of Time*, 1956) and Albert (*Time and Chance*, 2000) ground the epistemic arrow in records and the past hypothesis; Mlodinow & Brun (PRD 2014) connect the psychological arrow to records thermodynamically. C1's "experienced time tracks record accumulation" needs positioning against these or it reads as unread.
6. **Relational time.** Rovelli's relational QM (1996) and Connes–Rovelli thermal time (1994); Page–Wootters (1983) for time-from-correlations. Named in N1's list, no notes.
7. **Causal structure.** Causal set theory (Bombelli–Lee–Meyer–Sorkin 1987) for order-theoretic spacetime. The project's "causal partial order as primitive" choice is causal-set-adjacent and should say so.
8. **Cognitive renderer vs predictive processing.** The entire renderer layer (T8, open problem, exploration Layer 1) has an unnamed mainstream neighbor: generative world models / predictive processing (Friston et al.). Currently the only named neighbor for this layer is Hoffman, which is the least mainstream available anchor — the worst ratio in the repo.
9. **S1 vs emergent-spacetime programs.** Wheeler's "it from bit," and the broad emergent-spacetime literature. S1 doesn't claim novelty, but its non-novelty is a reason to demote rather than develop it.

The Voyager citations in T7/heliosphere are marked `[citations verified]` and the crossing dates/distances are consistent with the public record. Not re-verified in this audit pass.

**Net judgment:** the project's actual novel surface, after honest literature positioning, is narrower than the repo implies but nonzero — see Track A, Path 1. The fastest credibility gain available is writing three literature notes (Darwinism/records, IGUS/arrow, Lamport), because each converts a reinvention exposure into a stated relationship.

---

## 6. Speculation Control

Flagged, in descending severity:

1. **`../gu-formalization` cross-references (personas/INDEX.md).** Associating with a Geometric Unity formalization repo is the single largest crackpot-adjacency signal in the repo for a physics-literate reader, regardless of that repo's content. Remove the references from public-facing files or fence them in a private process note.
2. **Renderer/simulation vocabulary in core surfaces.** "Rendered world," "body-interface," "cognitive renderer," "render gates" (even when denied) appear in GLOSSARY, TESTS' minimum constraints, README's start-here flow via personas, T8, and G3. The guardrails are well-written, but the vocabulary's *presence in core files* imports simulation-hypothesis framing wholesale. The denial of a frame still installs the frame. Recommendation: quarantine renderer vocabulary entirely to `explorations/` and the open problems; in GLOSSARY and tests, use "world model" / "accessible record set." G3 stays (guardrails can name what they guard against).
3. **Hoffman as the sole developed literature anchor.** N2 itself is careful — credibility boundaries are explicit and the "nine conjectures" honesty note is good practice. The problem is proportion: one of two literature files, plus roadmap items 5 and 11, plus glossary-adjacent influence. Hoffman is a pop-science-adjacent association; mainstream notes must outweigh it before the repo is shared with technical readers.
4. **Blockchain vocabulary density.** "Commit order," "consensus envelope," Avalanche/Snowball parameters, quorums, proof-carrying records, metastable consensus. A1 guards each use, but the aggregate reads as a crypto-native lens seeking physics applications. Two cheap mitigations: cite Lamport (makes the bridge scholarly), and run the Track B check on whether Snowball-specific machinery reduces to standard metastability — if it does, the abstract version is strictly safer and the protocol branding can be dropped from everything except A1.
5. **GEB persona dialectics in the front door.** Gödel/Escher/Bach lenses as method scaffolding are harmless internally; linked from README "Start Here" they read as mysticism-adjacent flavor. Demote to a process directory; remove from Start Here.
6. **ESSAY closing register.** "The universe is becoming accountable to itself" — fine for the essay's genre, but it is the line most likely to be quoted against the project. Consider letting §13 end one paragraph earlier, or accept the cost knowingly.
7. **Already well-controlled:** consciousness-creates-matter (G1/G3 + repeated non-claims), replacement-theory ambitions (G2 + per-claim non-claims), black-hole-travel (multiply guarded in B1/T7/rendered-interface), decoherence-renaming (named as failure condition in Q1/T2/H-failure-5). The G-series plus per-claim "What This Does Not Claim" sections are the repo's strongest feature. No claim file asserts anything in the forbidden list.

---

## 7. Recommended Work Cards

### Critical — before sharing with technical readers

**WC-1: Declare the primitive inventory**
- Files: HYPOTHESES.md (new top section), GLOSSARY.md, tests/T1
- Problem: "without smuggling primitive time" is unfalsifiable because the allowed primitives are never stated.
- Change: add a Primitives section: given = finite event/system set, causal partial order, record states; derived = experienced temporal order, finality; forbidden as input = metric time, global simultaneity. Reference it from T1's failure criteria.
- Why: every formalization and every failure condition depends on it; it is one page of work.
- Acceptance: T1 failure criterion "requires primitive time in disguise" can be checked mechanically against the declared list.

**WC-2: Formalize D1 as a finality preorder (v0.1)**
- Files: claims/D1, GLOSSARY.md, tests/T1
- Problem: four dimensions named, none typed; "later compatible observations" smuggles temporal language; score-vs-preorder ambiguity.
- Change: define ⪯_O on propositions over a finite record DAG; per-dimension graph-native definitions (redundancy = disjoint record paths; accessibility = causal-past membership; robustness = stability under causal-future graph extension; reversal cost = min record deletions breaking reconstructibility). Replace "later" with causal-future throughout D1 and GLOSSARY.
- Why: this is the repo's stated Phase 1 item and removes the central circularity objection.
- Acceptance: D1 contains formal definitions usable by T1 without interpretation; the word "later" no longer appears in the definition.

**WC-3: Build T1 (first runnable artifact)**
- Files: tests/T1, new `models/T1/` directory
- Problem: the central test of C1/D1/D2 exists only as a spec; the repo has zero formal artifacts.
- Change: small DAG model (6–10 nodes, two observers, one spacelike-independent pair, one access-loss event, one erasure event), implementing WC-2's definitions. State the theorem target first: stabilization order is a linear extension of causal order restricted to accessible records, not assumed in F_O's construction.
- Why: converts the project from scaffolding to formalization; gives C1/D1/D2 their first real failure exposure.
- Acceptance: code runs; output exercises every T1 success and failure criterion; the access-loss vs physical-reversal distinction is demonstrated, not asserted.

**WC-4: Literature note — decoherence and quantum Darwinism**
- Files: new literature/N3, claims/Q1, claims/D1, ESSAY §4
- Problem: D1-redundancy and ESSAY §4's "classical objectivity = high-finality limit of redundancy" collide with Zurek/Ollivier–Poulin–Zurek uncited.
- Change: verified-citation note stating what Darwinism says, what D1 borrows, what D1 adds (observer-indexing, the other three dimensions, the preorder), where it breaks. Retag the ESSAY §4 line `[KNOWN NEIGHBOR]` or anchor it to a new ID.
- Why: this is the prior-art collision most likely to be spotted first by a physicist.
- Acceptance: a reader can state in one sentence what D1 claims beyond redundancy-implies-objectivity.

**WC-5: Literature note — records, IGUS, and the experienced arrow**
- Files: new literature/N4, claims/C1, claims/D2
- Problem: D2 ≈ IGUS (Gell-Mann–Hartle) and C1 overlaps Reichenbach/Albert/Mlodinow–Brun and Halliwell's records work, all uncited.
- Change: verified-citation note covering IGUS, decoherent-histories records theory, and the records-based epistemic arrow; position C1/D2 explicitly against each.
- Why: D2 currently looks like reinvention of a 30-year-old concept; this is the second-most-likely spotted collision.
- Acceptance: D2 cites IGUS and states its delta; C1 states its delta from the records-arrow literature.

**WC-6: Fix ledger promotion discipline**
- Files: CLAIM-LEDGER.md, explorations/heliosphere-as-finality-domain.md
- Problem: H-Domain and H-Soft-Boundary are ledger rows without claim files, violating the explorations/core separation the README promises.
- Change: remove both rows from the ledger (recommended; see Track B) or write proper claims/ files with full structure. Add a dated changelog section to the ledger so `revised`/`weakened`/`rejected` become usable.
- Why: the ledger is the repo's integrity instrument; one inconsistency undermines the whole device.
- Acceptance: every ledger row points to a claims/, guardrails/, or literature/ file; ledger has a changelog with at least this audit's changes dated.

**WC-7: Clean the public-facing surface**
- Files: README.md, personas/INDEX.md, GLOSSARY.md, TESTS.md
- Problem: GU-repo cross-references, personas in Start Here, and renderer vocabulary in core files create crackpot-adjacency signals that guardrails alone cannot offset.
- Change: remove `gu-formalization` references from public files; drop personas from Start Here; move Cognitive Renderer / Body-Interface glossary entries into the exploration docs; reword TESTS' renderer-related minimum constraint in record-access terms.
- Why: cheapest reputational-risk reduction available; zero substantive loss.
- Acceptance: grep for "render" returns hits only in explorations/, open-problems/, G3, and T8; no public file references gu-formalization.

### High — important for credibility

**WC-8: Literature note — Lamport and the distributed-systems bridge**
- Files: new literature/N5, claims/A1, claims/R1
- Problem: the happened-before partial order was built on relativity (Lamport 1978); A1/R1 risk presenting a 48-year-old bridge as new.
- Change: verified-citation note; reframe A1 as a deliberate round trip (relativity → distributed systems → back, carrying finality vocabulary).
- Why: converts the project's most distinctive analogy from exposure into provenance, and it is the project's best story.
- Acceptance: A1 and R1 cite Lamport; the round-trip framing appears in A1.

**WC-9: Anchor all ESSAY claim tags to ledger IDs**
- Files: ESSAY.md, CLAIM-LEDGER.md
- Problem: several `[CORE CLAIM]` tags have no ID, so the essay asserts more than the ledger tracks.
- Change: every CORE CLAIM / CONJECTURE / SPECULATIVE tag links to an ID; new IDs or KNOWN NEIGHBOR retags where needed.
- Acceptance: zero unanchored claim tags in ESSAY.

**WC-10: Reframe T5 as the reduction kill-test**
- Files: tests/T5, claims/D1
- Problem: the project's most important question — does finality reduce to entropy + decoherence + Landauer? — is framed as "support" rather than as the test that could kill D1.
- Change: restate T5's purpose as the reduction attempt; specify that a successful reduction downgrades D1 to `weakened` (a useful synthesis vocabulary, not a new relation). Connect to WC-2's two candidate reversal-cost definitions (graph-theoretic vs thermodynamic) — their relationship is T5's concrete object.
- Acceptance: T5 names the reduction targets and the downgrade consequence explicitly.

**WC-11: T3 relativity sanity check**
- Files: tests/T3, claims/R1
- Problem: R1's vacuity risk is undecided.
- Change: one worked Minkowski example; a table of frame-dependent vs invariant orderings; an explicit verdict on what finality vocabulary adds (acceptable verdict: interpretive only).
- Acceptance: R1 status updated based on the verdict; "safe vs misleading" wording list produced as the claim file already requests.

### Medium — useful next improvements

**WC-12: T2 quantum Darwinism toy model** — system + apparatus + N-fragment qubit model; map F_O to fragment mutual information; honest comparison per Q1's contribution-needed. Files: tests/T2, models/, claims/Q1. Acceptance: the "adds no clarity beyond decoherence" failure condition gets a real evaluation.

**WC-13: D2 taxonomy** — trace-bearer → recorder → reconciler → conscious observer, with parameters (capacity, lifetime, propagation). Files: claims/D2, GLOSSARY.md. Acceptance: T1 specifies which level each node needs.

**WC-14: A1 metastability comparison** — check Snowball-style confidence accumulation against statistical-mechanics metastability (basin escape, nucleation). If isomorphic, generalize A1's abstraction and confine protocol branding to one subsection. Files: claims/A1, tests/T6. Acceptance: a stated verdict either way.

**WC-15: Q1 interpretation comparison table** — the compact comparison vs decoherence, Darwinism, RQM, consistent histories, MWI, QBism that Q1 already requests. Files: claims/Q1, literature/. Acceptance: table exists with verified anchors.

### Later — after core formalization improves

**WC-16: S1 decision point** — exercise S1's own criterion: formalize the source/protocol/record map or demote S1 to explorations and mark the phrase rhetorical. Default: demote (see Track B). Files: claims/S1, CLAIM-LEDGER, ESSAY §10.

**WC-17: T8 / consciousness-renderer deferral** — mark T8 and the cognitive-renderer open problem as deferred until T1 exists; add predictive-processing as the named mainstream neighbor when resumed. Files: tests/T8, open-problems/consciousness-as-record-renderer.md.

**WC-18: B1/T4 specialist pass** — only after T1 and T3 are clean, per ESSAY §12's own sequencing. Files: claims/B1, tests/T4.

---

# Operating Frame: Worth-Ranking Of Next Directions

Criteria, scored 1–5: **N**ovelty (meaningfully new vs reframing), **Pr**ofundity (would it matter if formalized), **Pu**blishability (credible artifact for a real audience), **T**ractability (progress possible now).

| Path | N | Pr | Pu | T | Σ | Verdict |
|---|---|---|---|---|---|---|
| 1. Finality preorder + reconstruction theorem (D1+C1+T1) | 3 | 4 | 4 | 5 | 16 | **Pursue first** |
| 2. Lamport round-trip bridge note (A1+R1) | 3 | 3 | 4 | 5 | 15 | **Pursue** |
| 3. Under-finalization vs decoherence positioning (Q1+T2) | 2 | 3 | 4 | 4 | 13 | **Pursue (defensive)** |
| 4. Social finality / cognitive renderer | 2 | 2 | 3 | 3 | 10 | Separate project; defer |
| 5. Proof-carrying record finality | 3 | 2 | 2 | 2 | 9 | Defer |
| 6. Black-hole finality boundaries (B1+T4) | 2 | 3 | 2 | 2 | 9 | Defer per own sequencing |
| 7. Spacetime consensus envelope (S1) | 2 | 5 | 1 | 1 | 9 | Demote to exploration |
| 8. Heliosphere finality domain (H-*) | 2 | 1 | 1 | 3 | 7 | Close from ledger |

## Track A: Highest-Worth Research Paths

### Path 1: The Finality Preorder And The Reconstruction Theorem
- **Core claim:** observer-relative temporal order is recoverable as the stabilization order of a finality preorder defined over a causal record graph, using only causal structure and record states as primitives.
- **Why it may be novel:** quantum Darwinism formalizes redundancy; Halliwell formalizes records within decoherent histories; Lamport formalizes causal order. Nobody appears to have packaged *finality as an observer-indexed preorder with redundancy, accessibility, robustness, and reversal cost as separate monotone dimensions*, with experienced temporal order as the reconstruction target. The novelty is the synthesis and the theorem shape, not any ingredient — which is an honest, defensible kind of novelty.
- **Why it may be profound:** if the theorem holds non-trivially, "experienced time" gets a substrate-independent formal definition that applies to any record-bearing system — detectors, organisms, distributed databases — and the quantum/classical and relativity-facing claims (Q1, R1) inherit a common formal backbone instead of being parallel analogies.
- **What would make it publishable:** a short technical note (arXiv: quant-ph or physics.hist-ph; venue class: *Foundations of Physics*, *BJPS*, or *Synthese*) containing the primitive inventory, the preorder definition, the toy model, the theorem or counterexample, and honest positioning against Darwinism/IGUS/Halliwell. Audience: foundations-of-physics and philosophy-of-physics readers; also legible to CS-theory readers via Lamport.
- **What would falsify or weaken it:** the reconstruction needs primitive time smuggled into robustness or reversal cost (kills H1); the stabilization order is trivially whatever the modeler built in (kills the theorem's content); T5's reduction succeeds completely (D1 is renaming; project becomes a vocabulary, which is survivable but lesser).
- **First concrete work product:** WC-1 + WC-2 + WC-3 — primitives page, D1 v0.1 preorder, runnable T1 model with theorem statement. Roughly the smallest unit that changes the repo's nature.
- **Files affected:** HYPOTHESES.md, GLOSSARY.md, claims/D1, claims/C1, claims/D2, tests/T1, new models/T1/.
- **Scores:** N 3, Pr 4, Pu 4, T 5.

### Path 2: The Lamport Round Trip
- **Core claim:** "finality" is a concept distributed systems built on relativity's causal structure (Lamport 1978), and it can be carried back into physics discourse as a disciplined vocabulary for record stabilization — with an explicit map of which protocol concepts transfer, which fail, and why.
- **Why it may be novel:** the direction physics→CS is famous; the disciplined return trip — finality, metastable consensus, and commit-order *non*-existence as physics-facing vocabulary with stated failure modes — has no canonical treatment. A1's "How It Could Mislead" section is already half the paper.
- **Why it may be profound:** modestly — it gives interdisciplinary readers a correct intuition pump for relativity of simultaneity and classical record formation, and inoculates against the blockchain-mysticism failure mode by doing the analogy properly once.
- **What would make it publishable:** an essay or interdisciplinary note (venue class: *Synthese*, interdisciplinary CS/physics workshops, or a high-quality long-form essay) — concept-transfer table, worked Minkowski example (WC-11), failure-mode catalog. This is also the path best matched to the author's existing credibility base (distributed systems / crypto governance), which matters for who can publish it credibly.
- **What would falsify or weaken it:** discovery of an existing thorough treatment (the fastest check is a literature pass on "finality" in philosophy-of-computing and relativity-pedagogy literature); or the T3 verdict showing the vocabulary actively misleads where it claims to clarify.
- **First concrete work product:** WC-8 (Lamport note) + WC-11 (T3 sanity check), which together are most of the artifact.
- **Files affected:** literature/N5 (new), claims/A1, claims/R1, tests/T3.
- **Scores:** N 3, Pr 3, Pu 4, T 5.

### Path 3: Under-Finalization Positioned Against Decoherence (defensive necessity)
- **Core claim:** "real but under-finalized" is a coherent intermediate status for quantum states, distinct from (not renaming) decoherence and Darwinism vocabulary.
- **Why it may be novel:** probably only mildly — the value is in the precise delta statement, which doesn't exist anywhere yet.
- **Why it may be profound:** the "stratified by finality regime, not real-vs-unreal" framing (ESSAY §5) is the project's best public-communication payoff; if the delta is real, it earns it.
- **What would make it publishable:** the comparison note Q1 already requests, upgraded with the WC-12 toy model. Audience: quantum-foundations-adjacent readers; also strengthens any Path 1 paper's related-work section.
- **What would falsify or weaken it:** the comparison shows zero delta beyond Zurek's existing language — in which case Q1 is downgraded to `weakened` and the project saves itself from a slow embarrassment. Either outcome is a win, which is why this path scores well on tractability despite low novelty.
- **First concrete work product:** WC-4 + WC-15 (literature note and comparison table), then WC-12 if the delta survives.
- **Files affected:** literature/N3 (new), claims/Q1, tests/T2, models/.
- **Scores:** N 2, Pr 3, Pu 4, T 4.

## Track B: Quick-Close Pathways

### QC-1: Heliosphere as finality domain (H-Domain, H-Soft-Boundary, H-Hierarchy)
- **Why tempting:** real spacecraft data, verified citations, a concrete worked example for T7, and a satisfying soft/hard boundary spectrum for B1.
- **Why weak:** "the record-forming substrate differs across the heliopause" is trivially true as plasma physics and does no work for D1 — heliophysics already owns every observable involved. The density-normalization failure condition cannot even be evaluated until D1 is formal, so the claims are unfalsifiable *in this repo's own terms* today. It also consumed disproportionate repo mass (the longest exploration, a ledger violation, an open problem, and a T7 section) for a peripheral illustration.
- **Fastest check:** ask one question of D1-v0.1 once it exists: does any of the four dimensions change across the heliopause in a way not captured by standard plasma parameters? No formalized D1, no evaluable claim — which settles the sequencing by itself.
- **Recommendation:** **Close from ledger, retain as exploration.** Remove H-Domain/H-Soft-Boundary ledger rows (WC-6); keep the exploration file and Voyager citations as a future worked example; keep the non-static-boundaries open problem (it raises a real D1 question). Do no further heliosphere work until after Path 1.
- **Files:** CLAIM-LEDGER.md, explorations/heliosphere-as-finality-domain.md, tests/T7.

### QC-2: Spacetime as consensus envelope (S1)
- **Why tempting:** it is the profound-sounding capstone; emergent spacetime is fashionable; it keeps the "wild idea alive."
- **Why weak:** by its own admission it has no source→protocol→record map, no mechanism, and no failure condition beyond "remains an evocative phrase." Emergent-spacetime territory (it-from-bit onward) is crowded with better-resourced programs; an unformalized entrant adds reputational risk and zero progress. It is also the claim most quotable against the project.
- **Fastest check:** apply the rendered-interface mechanism challenge (already written, in open-problems/rendered-interface-assumptions.md) as a pass/fail gate with a deadline: if no one can fill in "what is computed, by which systems, differing how from causal-access language" in one page, S1's own contribution-needed clause fires.
- **Recommendation:** **Demote to explorations now.** Keep ESSAY §10 (properly labeled there); remove S1 from claims/ and the ledger, or mark it `weakened` with the demotion dated. Revisit only if Path 1's formalism produces something that wants the extension.
- **Files:** claims/S1, CLAIM-LEDGER.md, open-problems/rendered-interface-assumptions.md.

### QC-3: Observer-renderer / consciousness layer (T8, cognitive-renderer open problem, Layer 1–2 of the layer-split exploration)
- **Why tempting:** it connects the physics to lived experience, which is the essay's emotional engine; the layer-split discipline is genuinely careful.
- **Why weak:** T8's own failure criterion — "adds no clarity beyond ordinary cognitive-science language" — is very likely already met: generative world models, predictive processing, and social-ontology literature (uncited) cover the candidate model's content. The renderer vocabulary is also the repo's main pop-science exposure (§6). The hard problem sits underneath and the repo rightly refuses it, which caps the payoff.
- **Fastest check:** one literature afternoon: put the Agent A = (M,P,I,H,S,C) → (W,B) model next to a standard predictive-processing formulation and list what differs. If the answer is "vocabulary," the failure criterion has fired.
- **Recommendation:** **Defer T8 and the open problem until T1 exists; quarantine vocabulary per WC-7.** Do not delete — the social-finality layer may become a legitimate application chapter later — but stop investing now.
- **Files:** tests/T8, open-problems/consciousness-as-record-renderer.md, explorations/cognitive-social-renderer-layer-split.md, GLOSSARY.md.

### QC-4: Proof-carrying record finality (ZK analogy)
- **Why tempting:** elegant, matches the author's crypto fluency, and the "finality = verifiable constraint under bounded access" slogan is the repo's best aphorism.
- **Why weak:** it is an analogy stacked on an analogy (ZK on top of distributed-systems finality) before the base formalism exists. Its quantum application (certifying nonclassical joint constraints) brushes against actual results in device-independent certification and self-testing — a literature the repo hasn't engaged, so the analogy may be either preempted or misleading.
- **Fastest check:** a literature pass on device-independent certification / self-testing (Bell-based certification of entanglement under bounded access). If that work already formalizes "verification under bounded access" for quantum records, the open problem should cite it and shrink to its delta.
- **Recommendation:** **Defer; keep as open problem; add the literature check as its first task.** Remove the proof-carrying paragraph from Q1 (claim files should not host speculative imports).
- **Files:** open-problems/proof-carrying-record-finality.md, claims/Q1.

### QC-5: Hoffman trace-logic reconstruction (roadmap item 11, parts of N2)
- **Why tempting:** N2's correspondences (observer window ↔ bounded record access) are suggestive, and reconstructing the "nine conjectures" feels like diligence.
- **Why weak:** reconstructing another program's unpublished conjectures from interviews is low-yield work that deepens the repo's most reputationally expensive association. N2's credibility-boundaries section already extracts the useful part.
- **Fastest check:** none needed — this is a priority call, not an empirical question.
- **Recommendation:** **Close roadmap item 11.** Keep N2 as-is; revisit only if Hoffman's group publishes the technical list, at which point reconstruction is unnecessary anyway.
- **Files:** ROADMAP.md.

### QC-6: Black-hole boundary development (B1 beyond current wording)
- **Why tempting:** highest-drama domain; the permeability-spectrum idea gives it apparent momentum.
- **Why weak:** ESSAY §12 already sequences it last ("test black-hole language only after the ordinary causal-access model is clean") and the repo then ignored its own sequencing by extending B1 with heliosphere material. Horizon territory has the field's highest specialist density and the lowest tolerance for vocabulary imports.
- **Fastest check:** none — enforce the existing sequencing rule.
- **Recommendation:** **Freeze B1 at current wording; revert or fence the permeability-spectrum section as exploration-linked; revisit at WC-18 time.**
- **Files:** claims/B1, tests/T4.

---

## Ranked Map (summary)

**Most worth pursuing:** Path 1 (preorder + T1 + reconstruction theorem) is the project's identity bet — everything else either feeds it or waits on it. Path 2 (Lamport round trip) is the best near-term *artifact* and matches the author's credibility base. Path 3 is the defensive note Path 1's related-work section needs anyway.

**Kill or narrow quickly:** heliosphere ledger rows (close), S1 (demote), renderer/Hoffman investment (defer + quarantine), proof-carrying (defer behind a literature check), roadmap item 11 (close), B1 extension (freeze).

**Concrete next work, in order:** WC-1 → WC-2 → WC-3 (one unit: primitives, preorder, runnable T1), then WC-4/WC-5/WC-8 (the three literature notes), then WC-6/WC-7 (ledger and surface hygiene — cheap, do alongside). After that, WC-10 (T5 as kill-test) and WC-11 (T3 verdict) decide whether D1 and R1 survive as more than vocabulary — which is exactly the question the repo was built to ask.
