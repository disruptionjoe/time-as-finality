# Computational Status Ledger

## Status

Governance ledger for computational-status language. This file does not
promote any claim. It records what the current executable artifacts honestly
earn about scale, search, and hardness.

Use this ledger before saying that a branch is brute-force, polynomial,
theorem-backed, NP-hard, CSP-complete, or scalable.

## Coverage / Staleness

As of 2026-07-22, the test registry in `TESTS.md` reaches T587, while this
ledger has explicit computational-status placements only through T162. T163-T587
are not computational-status ratified here unless named elsewhere in this file.
Do not infer `finite_witness`, `poly_decider`, `theorem_backed`, `open_hardness`,
or scalable-algorithm status from silence in this ledger.

Mechanical frontier note: the claim ledger is current through T587 except for
its explicitly deferred T408-T409 adjudication, but claim-ledger placement does
not assign computational status. Post-T138 artifacts may use finite executable
gates and passing tests, but this ledger does not promote any of them to
`finite_witness`, `poly_decider`, `theorem_backed`, or a hardness/scalability
class until a dedicated computational-status reconciliation pass reviews the
relevant artifact and input encoding. The first bounded post-T138 slice,
T139-T162, is now reconciled below.

This note is mechanical frontier hygiene. It creates no claim-status movement,
Canon Index tier movement, theorem claim, hardness claim, public-posture
movement, or external-publication implication. A dedicated complexity-ledger
reconciliation pass remains due for the post-T138 frontier.

## Status Labels

| Label | Meaning |
| --- | --- |
| `finite_witness` | Current support is a finite executable fixture or finite-family check. It may use efficient operations internally, but no general scalable theorem has been earned. |
| `poly_decider` | The implemented decision surface is a finite polynomial-style classifier over declared inputs, not a hidden search over completions. |
| `theorem_backed` | The main claim has an explicit scalable proof argument, with finite code used only for sanity checks or examples. |
| `open_hardness` | Hardness is only an open question. Do not use NP-hard or CSP-complete language. |
| `non_computational` | The artifact is a prose taxonomy, conditional obstruction, or governance boundary and makes no algorithmic, scaling, or hardness claim to classify. |

## Current Ledger

| Surface | Primary status | Input size / scope | Current decision method | Scale / hardness guardrail |
| --- | --- | --- | --- | --- |
| [T26 D1 Restriction System](tests/T26-d1-restriction-system.md) | `finite_witness` | Number of patch variables and finite constraints in a `D1RestrictionSystem`. | `global_section()` checks the current finite witnesses by assignment enumeration over patch variables. | Do not call this a scalable obstruction algorithm; use T39 for the signed-graph tractable fragment. |
| [T39 CSP / Satisfiability Reframing](tests/T39-csp-satisfiability-reframing.md) | `poly_decider` | Binary same/different constraints over `{-1, 1}`. | Signed-graph parity / 2-coloring classifies the tested obstruction fragment. | This earns tractability for the declared binary parity fragment, not NP-hardness or general CSP-completeness. |
| [T45 Measurement Asymmetry — obstructed-source lemma](results/measurement-po1-asymmetry-v0.1-results.md) | `theorem_backed` | Any morphism between `D1RestrictionSystem`s under the PO1 AC1–AC7 checklist. | AC7 argument: no PO1-admissible morphism can originate from an obstructed system; the admissible relation lies inside (unobstructed × obstructed). Finite run is a control. | GENERAL but elementary: an order-property of the *partially-supported* PO1 schema, inheriting its ceiling. ZERO temporal/empirical content — it does NOT show measurement is physically irreversible, nor that time is finality. |
| [T47 PO1-DAG Theorem](results/po1-dag-theorem-v0.1-results.md) | `theorem_backed` | Admissible morphisms in `D1Cat` over arbitrary finite `D1RestrictionSystem`s. | AC6 (target obstructed) and AC7 (source unobstructed) are necessary and complementary, so the admissible relation ⊆ (unobstructed × obstructed) is trivially acyclic, bipartite, depth ≤ 1. The K_{2,3} run is a control. | Same guardrail as T45: a GENERAL but elementary structural lemma about the PO1 schema; inherits PO1's `partially_supported` ceiling; ZERO temporal/empirical content. |
| [T54 Finite Finality Descent Theorem](tests/T54-finite-finality-descent-theorem.md) | `poly_decider` | Finite observer-local events, identity maps, records, axis profiles, and overlap witnesses. | Quotient-union construction plus finite record/order/Axis-Monotonicity checks classify canonical, underdetermined, conflicting, nondefinable, and AM-invalid cases. | Keep the theorem finite. It does not prove infinite descent or sheaf/categorical descent machinery. |
| [T73 LossKernel Composition](tests/T73-losskernel-composition.md) | `finite_witness` | Declared T34/T37 finite morphism paths and their `forgotten_structure` annotations. | Set union computes the current LossKernel annotation and finite tests compare it to path-dependent PO1 admissibility. | State this as a powerset-union monoid-valued annotation law, not as a lax functor or new categorical object. Quotient/prior-art gates remain open. |
| [T110 Finite-Permutation Monotone Obstruction](tests/T110-finite-permutation-monotone-obstruction.md) | `theorem_backed` | Finite closed reversible dynamics, modeled as permutation orbits. | Orbit argument: edgewise nondecrease on a finite cycle forces constancy. Exhaustive finite cycle checks are controls. | This blocks strict scalar finality monotones in finite closed reversible systems only. Open-system, coarse-grained, resource, and constructor variants require their own assumptions. |
| [T132 Weak-Measurement Non-Null Criterion](tests/T132-weak-measurement-nonnull-criterion.md) | `poly_decider` | Declared protocol features for a weak-measurement candidate. | Fixed finite rule audit classifies same-record, post hoc, constant-branch, monotone-proxy, and independent-axis cases. | This is a gate, not a prediction. It does not make Q1C empirical or near-ready. |
| [T138 Detector Manifest Workflow Fit](tests/T138-detector-manifest-workflow-fit.md) | `poly_decider` | Declared T136 manifest fields and authority-domain workflow structure. | Finite field, authority, pre-data-boundary, and outcome-smuggling checks via the T136 validator. | Passing a scaffold is not detector evidence. Q1B remains externally blocked until real pre-event manifest and event-level packet exist. |
| [T139 Weak-Measurement Full-Record Sufficiency Boundary](tests/T139-weak-measurement-full-record-sufficiency-boundary.md) | `poly_decider` | Declared coarse-summary, full-record, and auxiliary-witness features. | A fixed finite rule classifies refinement-only, downstream-null, and full-record escape shapes. | This is a proposal/admissibility classifier, not a scalable physical inference or platform-independent no-go. |
| [T140 Q1 Frontier Escape Matrix](tests/T140-q1-frontier-escape-matrix.md) | `poly_decider` | Declared Q1A-Q1D packet and route features. | Fixed branch-specific Boolean gates classify bookkeeping, external-block, dormant/null, guardrail, and candidate-route states. | It selects routes; it does not establish detector evidence, a new theorem, or physical scalability. |
| [T141 T1 Record-Graph Admissibility Ledger](tests/T141-t1-record-graph-admissibility-ledger.md) | `finite_witness` | Four declared transformations on the explicit finite T1 record graph. | Direct finite graph/profile comparison and reverse-edge classification over the frozen cases. | Do not generalize the tested absence of constructor-impossible reverses to arbitrary substrates. |
| [T142 Thermodynamic Erasure Calibration](tests/T142-thermodynamic-erasure-calibration.md) | `finite_witness` | T141's finite cases plus declared uncopy and blind-reset modes. | Exact finite bookkeeping applies the dimensionless one-bit Landauer floor and named absorber classes. | This is calibration/accounting, not a thermodynamic theorem or general arrow result. |
| [T143 Weak-Measurement Instrument Sufficiency Obstruction](tests/T143-weak-measurement-instrument-sufficiency-obstruction.md) | `non_computational` | Conditional prose comparison of an ordinary monitored instrument and auxiliary channel. | No executable decision procedure or scale claim; the artifact names a conditional obstruction and escape classes. | Do not restate it as a universal dual-meter no-go theorem. |
| [T144 Definalization Reverse-Edge Taxonomy](tests/T144-definalization-reverse-edge-taxonomy.md) | `non_computational` | Four named reverse-edge classes for future record-finality audits. | Prose taxonomy and declaration requirement only. | Classification vocabulary does not prove thermodynamic irreversibility or constructor impossibility. |
| [T145 Physical Record Deletion Fixed-Accounting Screen](tests/T145-physical-record-deletion-fixed-accounting.md) | `poly_decider` | Declared absorber vectors and reverse-edge features for a finite fixture family or future packet. | A fixed finite gate compares accounting vectors and requires physical deletion, matched absorbers, a task-natural split, and constructor impossibility. | Passing the syntactic gate would create a review candidate, not itself prove a physical arrow. |
| [T146 Weak-Measurement Escape Architecture Gate](tests/T146-weak-measurement-escape-architecture-gate.md) | `poly_decider` | Declared full-record, screening, proxy, instrument, environment, comparison-target, and verdict features. | A fixed finite architecture classifier rejects null/underdeclared shapes and admits two review classes. | It is an intake gate, not evidence that either live architecture exists physically. |
| [T147 Q1A Current-Family Closure](tests/T147-q1a-current-family-closure.md) | `poly_decider` | Declared partition visibility, audited accessible provenance support, and current D1 proxy features. | A fixed closure-key calculation checks whether every current-family verdict factors through the declared quotient. | The closure is current-family only; it is not a theorem about arbitrary quantum measurements or future physical dimensions. |
| [T148 H7 Paper-Facing Demotion Gate](tests/T148-h7-paper-facing-demotion-gate.md) | `poly_decider` | Declared constructor theorem, obstruction, reverse-grounding, deletion, and capability-residue status flags. | A fixed finite status gate produces allowed claims, rejected claims, blockers, and reinstatement conditions. | This governs claim language; it neither proves a physical arrow nor deletes the conditional T18 theorem. |
| [T149 Weak-Measurement Conditional-Sufficiency Gate](tests/T149-weak-measurement-conditional-sufficiency-gate.md) | `poly_decider` | Finite declared joint distributions over full record, auxiliary output, and verdict plus architecture flags. | Exact finite Bayes-risk comparison and a fixed architecture gate classify zero-lift, underdeclared, and candidate shapes. | Positive lift is only an intake condition and does not establish a physical platform or scalable inference result. |
| [T150 Weak-Measurement Verdict-Admissibility Gate](tests/T150-weak-measurement-verdict-admissibility-gate.md) | `poly_decider` | T149 output plus declared hidden-axis typing, verdict map, support floor, and predeclaration status. | A fixed finite rule rejects auxiliary-defined, rare, and post-hoc verdict targets. | Passing creates a review candidate only; it does not validate the hidden axis or reinstate Q1C. |
| [T151 Causal-Access Screen](tests/T151-causal-access-screen.md) | `poly_decider` | Finite directed record-channel graph, observer profile, boundary direction, and channel type. | Graph reachability plus typed channel and boundary checks classify direct classical record access. | The screen is restricted to declared classical channels and cannot adjudicate encoded, holographic, or quantum information claims. |
| [T152 Metastable-Record Deletion Screen](tests/T152-metastable-record-deletion-screen.md) | `poly_decider` | Declared barrier, lifetime, absorber-vector, control, and reverse-status features. | A fixed finite gate separates kinetic/resource, boundary, idealization, topology-residue, and candidate classes. | Finite barriers and fixture passes do not prove constructor impossibility or a thermodynamic arrow. |
| [T153 Lorentzian Causal-Diamond Screen](tests/T153-lorentzian-causal-diamond-screen.md) | `finite_witness` | Five frozen fixtures in explicit 1+1 Minkowski coordinates. | Exact causal-order, diamond-membership, and interval domain-of-dependence calculations evaluate the declared cases. | Do not promote this finite 1+1 absorber check to a general spacetime-reconstruction or black-hole theorem. |
| [T154 T54/T58-to-T126 Bridge](tests/T154-t54-t58-t126-bridge.md) | `finite_witness` | The specific T51/T52 canonical completions and T53 underdetermined boundary. | Direct adaptation through the T58 exact-match gate into the finite T126 screen. | The tiny candidates are insufficient-scale controls; no continuum, dimension, locality, or embeddability result is earned. |
| [T155 Weak-Measurement Blackwell Boundary](tests/T155-weak-measurement-blackwell-boundary.md) | `poly_decider` | Declared finite joint distributions and a predeclared finite loss-table family. | Exact posterior equality and finite Bayes-risk minimization compare the ordinary record with the augmented record. | The result is restricted to the declared finite decision family, not all experiments or loss functions. |
| [T156 Myrheim-Meyer Ordering-Fraction Screen](tests/T156-myrheim-meyer-ordering-fraction-screen.md) | `poly_decider` | A finite strict relation plus the declared T126 gate, target fraction, and tolerance. | Pair counting computes ordering fraction and a fixed gate classifies blocked, in-band, and over-ordered candidates. | A band pass is calibration only, not a dimension estimate, sprinkling theorem, embedding, or spacetime derivation. |
| [T157 T54 Ordering-Fraction Bridge](tests/T157-t54-ordering-fraction-bridge.md) | `finite_witness` | Three frozen T54 descent datums, including one six-event flat-control construction. | Canonical quotient-union completion followed by the existing finite T126 and T156 screens. | The positive case is a constructed finite control; no locality, covariance, continuum, or metric claim is earned. |
| [T158 Weak-Measurement Preserved-Target Gate](tests/T158-weak-measurement-preserved-target-gate.md) | `poly_decider` | Finite standard and enlarged event records, a declared projection, target status, and lift status. | A fixed eventwise equality and admissibility classifier rejects coarse, drifting, underdeclared, and no-lift shapes. | Passing is an intake condition and does not validate an enlarged instrument or Q1C. |
| [T159 T54 Interval-Jackknife Screen](tests/T159-t54-interval-jackknife-screen.md) | `finite_witness` | The three frozen T157 candidates and every single-event deletion suborder. | Exact interval counts, ordering fractions, and exhaustive deletion checks test the declared finite controls. | Jackknife failure demotes one fixture; it is neither a continuum no-go nor a scalable robustness theorem. |
| [T160 H7 Substrate-Family Screen](tests/T160-h7-substrate-family-screen.md) | `non_computational` | Four prose-defined substrate families and the inherited H7 reinstatement burden. | Claim-triage synthesis over existing absorber results; no new executable procedure or scale claim. | The default-null taxonomy does not prove impossibility for every member of a substrate family. |
| [T161 Detector Control-Root Independence](tests/T161-detector-control-root-independence.md) | `poly_decider` | Finite nominal authority assignments and critical/noncritical control-root assignments. | Union/quotient of authority domains by shared critical roots followed by the existing finite authority audit. | This is infrastructure admissibility, not detector evidence, physics, or Q1B support. |
| [T162 Q1A SBS Factorization Obstruction](tests/T162-q1a-sbs-factorization-obstruction.md) | `finite_witness` | Enumerated finite SBS-style objectivity, access, provenance, and independence cases. | Exact closure-key comparison checks factorization of current-family D1 verdicts over the frozen cases. | This is a current-family obstruction, not a no-go theorem for quantum measurement or all SBS models. |

## Global Guardrail

Within the explicitly reconciled computational-status set through T162, no
surveyed core branch currently earns:

```text
NP-hard / CSP-complete core result
```

Hardness language is blocked until a branch proves a reduction or supplies an
accepted complexity-class placement under declared input encoding and
admissible transformations.

The honest current summary for the explicitly reconciled set is:

```text
mixed computational status: finite witnesses, several polynomial finite
classifiers, and three theorem-backed results — the T110 finite-permutation
obstruction (a NEGATIVE result, under the weakened H7) plus the T45/T47 elementary
order-properties of the partially-supported PO1 schema (no temporal or empirical
content). No top-line claim is a proven general theorem; no earned general
hardness rhetoric.
```
