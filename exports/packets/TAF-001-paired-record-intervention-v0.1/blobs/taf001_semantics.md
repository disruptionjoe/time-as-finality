# TAF-001: Paired Record-Access / Record-Formation Intervention Evidence Packet (source-issued, v0.1)

Issued by the Time as Finality steward on 2026-07-16. Semantics pinned at TaF revision
`8df3cf138855571538768d57e94ca36320f3830b` (the revision whose `FORMALISM.md` and
`tests/T46-open-causal-scarcity-synchronization-boundary.md` are frozen byte-identical in this
bundle as `blobs/FORMALISM.md` and `blobs/T46-open-causal-scarcity-synchronization-boundary.md`).
Drafted by a firewalled agent in the possibility-to-capability program; adopted by the TaF steward
with the corrections from the attached adversarial referee report (defects D1, D2, D5, and the
Section 9 grade note) applied, after independent TaF-side re-verification of the computation, the
blob hashes, and the correction-relevant probes. Exploration tier; no TaF claim status changes.

## 1. Exact question

Given one fixed finite baseline world W0 in the TaF T1/FORMALISM record model and one shared finite
task vocabulary TV, what are the exact task-achievability consequences, under TaF's own
reconstruction rule, of (ALPHA) enlarging one observer's bounded holder-access set with the causal
record graph held byte-identical, versus (BETA) adding record-formation events to the causal record
graph with the observer's access set held byte-identical?

`question.decision_type: other` (this packet decides a computed consequence, not an independence or
forcing claim).

## 2. Semantics used (all TaF-owned, none invented)

- **Causal record graph** `G = (E, A)`: finite DAG whose reachability induces `<_c` (FORMALISM,
  "Causal Record Graph").
- **Record token** `r = (id, proposition, value, event, holder, erasure_cost)`.
- **Causal availability**: a record is available to observer O at event e iff (1) its formation
  event is `<=_c e` and (2) its holder is in O's bounded access set. The model's structure separates
  access changes from record-formation changes: an access change edits condition-2 membership
  without creating or deleting records; record formation changes the token inventory and the graph.
  FORMALISM states the access-loss-vs-erasure case explicitly ("Local access loss changes condition
  2 without deleting the record. Physical reversal deactivates or deletes record tokens. The model
  treats these as different operations."); the access-gain and record-formation cases follow from
  the same primitives, not from that sentence.
- **Reconstruction rule**: (p, v) is reconstructible for O at e iff accessible support reaches the
  fixed threshold k and no competing value for p reaches k.
- **D1 profile** `F_O,e(x) = (A, R, B, C)`: accessible support; distinct accessible holders; causal
  antichain width of accessible supporting formation events; minimum accessible supporting erasures
  to drop below k. Reported per task; componentwise preorder, no scalarization.
- **Observer level**: reconciler (TaF observer taxonomy). No conscious-observer claim.
- **T46 `RecordAccessSystem` framing**: ALPHA acts on the observer-access side (who can inspect
  which holders); BETA acts on the generation/propagation side (which records form, where, on what
  causal paths). The packet uses T46's distinction only as vocabulary; it does not import T46's
  market/Spanner witnesses.

## 3. Shared baseline world W0 (exact, enumerable)

- Events: `src, a1, a2, b1, b2, c1, d1, d2, f1, f2, f3, f4, e_obs`; edges as in the computation
  (all formation events causally precede `e_obs`; `a1 <_c a2`; all others pairwise incomparable).
- Holders: `h1, h2, h3, h4`. Observer O access set `{h1, h2}`. Threshold `k = 2`, fixed before
  evaluation. Evaluation event `e_obs`. Uniform `erasure_cost = 1` (so `C_therm` coincides with
  `C`; divergence not exercised here).
- Record tokens r1–r11 exactly as in `blobs/taf001_paired_intervention.py` (p1=1 at h1,h2 chained;
  p2=1 at h1,h3; p3=1 at h4 only; p4 split 1@h1 / 0@h2; p5=1 at h1,h2 with p5=0 twice at h3).

## 4. Shared task vocabulary TV (finite, reconstruction-rule sense)

TV = { τ1:(p1,1), τ2:(p2,1), τ3:(p3,1), τ4:(p4,1), τ5:(p5,1) }. A task is achieved in a world iff
its pair is reconstructible for O at `e_obs` under k=2. TV is identical for both interventions;
that identity is load-bearing for the receiver's comparison and is guaranteed by construction
(same proposition-value pairs, same observer, same threshold, same evaluation event).

## 5. Intervention ALPHA — access structure changes, record inventory fixed

- **Before:** W0 with access set `{h1, h2}`.
- **After (W_A):** identical events, edges, and record tokens (byte-identical graph and inventory);
  access set enlarged to `{h1, h2, h3}`. In T46 terms: an observer-access-side change in
  `RecordAccessSystem`; in T1 terms: condition 2 of causal availability changes for records held at
  h3; nothing forms, propagates, or erases.

## 6. Intervention BETA — record formation changes, access fixed

- **Before:** W0 with access set `{h1, h2}`.
- **After (W_B):** access set held byte-identical at `{h1, h2}`; four new record-formation events
  `n1–n4` (causally after `src`, before `e_obs`) add tokens r12:(p3,1)@h1, r13:(p3,1)@h2,
  r14:(p4,1)@h2, r15:(p4,0)@h1. In T46 terms: a generation-side change in `RecordAccessSystem`;
  the causal record graph gains events and tokens at holders already inside the fixed access set.

## 7. Machine-checkable evidence

The computation is the frozen blob `blobs/taf001_paired_intervention.py` (pure Python 3, stdlib
only, deterministic; SHA-256 `e945cd89fc59e4ab644ec49d4513742ca17911edf760d239eabaebb2e1c8b34c`,
8181 bytes). Its captured output is the frozen blob `blobs/taf001_output.txt` (SHA-256
`c3ada0d8367f76638f1ffba7889a748bd355b8fcd4c67262236b08a496f060d0`, 2038 bytes). Verification:
re-run the script, byte-compare against the output blob. The TaF steward re-ran it at issuance:
exit 0, output byte-identical.

Result summary (full per-task D1 profiles and competing-support detail are in the output blob):

```text
W0  = (1, 0, 0, 0, 1)
W_A = (1, 1, 0, 0, 0)
W_B = (1, 0, 1, 0, 1)
ALPHA newly achievable: [tau2]   ALPHA newly unachievable: [tau5]
BETA  newly achievable: [tau3]   BETA  newly unachievable: []
```

**Computed facts the packet asserts (nothing more):**

1. ALPHA changes the achievability vector from (1,0,0,0,1) to (1,1,0,0,0) with zero change to the
   record inventory or causal graph: τ2 becomes achievable (previously-formed records at h3 become
   causally available), and τ5 becomes UNachievable (enlarged access makes a competing value reach
   threshold). Access enlargement is not monotone in task achievability under TaF's own
   reconstruction rule.
2. BETA changes the vector from (1,0,0,0,1) to (1,0,1,0,1) with the access set byte-identical:
   τ3 becomes achievable via new record-formation events at already-accessible holders; τ4 stays
   unachievable because the added formation events also raise a competing value to threshold (the
   no-competing-value clause binds).
3. The two specific interventions produce different deltas over the same TV ({τ2 on, τ5 off} vs
   {τ3 on}). The non-interchangeability is one-directional. Asymmetry: no access-set change of W0
   can produce BETA's delta (p3 has a single token in W0, held at h4, so its accessible support is
   ≤ 1 < k under every access set; verified exhaustively over all 16 access subsets of
   {h1,h2,h3,h4} at issuance), but a different formation-only intervention under the same fixed
   access set `{h1, h2}` reproduces ALPHA's delta exactly (add (p2,1)@h2, (p5,0)@h1, (p5,0)@h2;
   re-verified at issuance). Access-edits and formation-edits are not symmetric intervention
   classes in this world: formation subsumes this access delta; the converse fails.
4. Per-task D1 profiles (A,R,B,C) before/after are as printed in the output blob; the profile
   remains a componentwise preorder throughout (no scalarization was used to decide anything).
5. Reconstruction is computed from causal reachability alone; no topological ordering, timestamp,
   or clock is consumed anywhere in the implementation, so FORMALISM's topological-invariance
   requirement is satisfied by construction (verifiable by code inspection). The embedded assert
   in `evaluate` is a tautological guard (it compares a pure function of the edge set with itself)
   and carries no evidential weight.

## 8. Assumptions (all load-bearing, all explicit)

- A1 (definition): TaF T1/FORMALISM record model — causal record graph, record tokens,
  causal-availability conditions 1–2, reconstruction rule, D1 profile.
- A2 (construction_choice): threshold k=2, fixed before evaluation; evaluation event `e_obs`
  causally after all formation events; uniform erasure_cost=1.
- A3 (construction_choice): the specific finite worlds W0, W_A, W_B and TV above. These are
  designed witnesses, not sampled or physically measured systems.
- A4 (implementation): the frozen Python program correctly implements A1 over A3.
- A5 (definition): "task achievability" means reconstructibility under the reconstruction rule —
  TaF's native notion, chosen because it is the only task semantics TaF owns. If the receiver's
  normalization frame uses a different task semantics, mapping is the receiver's work.

## 9. Grades

- Overall packet: **exploration tier**; `source.evidence_grade = formal only` in TaF's T22
  confidence vocabulary (finite executable toy model; no physical substrate).
- Method M1 (ALPHA evaluation): computation grade — deterministic, stdlib-only, output frozen and
  hashed; verification = rerun script, byte-compare output.
- Method M2 (BETA evaluation): same grade, same verification.
- Grade for fact 3 (one-directional non-interchangeability): the deltas themselves are in the
  machine-checked output; the asymmetry is a finite argument (single-token bound for p3 under every
  access set; explicit alternative formation edit reproducing ALPHA's delta), independently
  confirmed at issuance by an exhaustive access-set sweep and a re-run of the alternative
  formation edit. It is a finite verified argument over W0, not a general theorem.
- Fact 5 is a by-construction property verifiable by code inspection, not a mechanized receipt.
- Nothing here is "physically supported" or "partially supported" in TaF's ledger sense, and this
  packet does not change the status of any TaF claim (R1, A1, PO1, CS1, D1, T46 verdicts all
  untouched).

## 10. Evidence structure (v0.2 dependency honesty)

- `method_ledger`: M1, M2. `raw_method_count = 2`; `raw_method_count_is_independence_count = false`.
- `premise_ledger`: A1–A5, with A1, A2, A3, A4, A5 load-bearing for BOTH methods.
- `shared_load_bearing_premise_ids = [A1, A2, A3, A4, A5]` — the two methods share their entire
  premise base and implementation; they are two evaluations of one model, not two independent
  evidential legs.
- `method_dependency_edges`: M1→M2 and M2→M1 `shares_implementation` and `shares_data` (same
  baseline W0).
- `claim.independence_scope` (source's exact wording, to be copied byte-for-byte by any receiving
  assessment): "The ALPHA and BETA evaluations share one implementation, one baseline world, and
  one task vocabulary; they are not evidentially independent methods, and this packet asserts no
  independence result of any type." `independence_type: not_applicable`.
  `convergence: not_applicable`.

## 11. Residuals

- R-1: Within W0 itself, formation-only edits can reproduce this access edit's task-delta while no
  access edit can reproduce the formation delta (fact 3). Whether this direction of simulability
  (formation subsumes access-deltas; converse fails) holds beyond this witness family is open; no
  general theorem is claimed in either direction.
- R-2: The τ5 non-monotonicity depends on the no-competing-value clause; under a task semantics
  without that clause the ALPHA delta would be monotone. Sensitivity to the clause is not swept
  here.
- R-3: `C_therm` vs `C` divergence is not exercised (uniform erasure costs). A receiver needing
  cost-ordering evidence needs a further packet.
- R-4: Interventions are evaluated separately from W0; the composite ALPHA∘BETA world is not
  computed.
- R-5: T46's open-causal vs closed-synchronization scarcity distinction is used as vocabulary only;
  neither witness models propagation delay or quorum rules.

## 12. Nonclaims (what TaF does NOT claim)

- TaF does not classify either intervention under any receiver taxonomy. In particular this packet
  deliberately assigns no diagnostic label of any kind to ALPHA or BETA; "changes the access
  structure" and "changes record formation under fixed access" are mechanical descriptions of which
  TaF object was edited, not classifications of what kind of change occurred. Labeling is the
  receiver's job; any label the receiver assigns is receiver-owned and must not be attributed to
  TaF.
- No claim that reconstructibility is the correct or unique normalization of "task capability" —
  only that it is TaF's native task semantics (A5).
- No physics: nothing here derives relativity, `c`, measurement, thermodynamic cost, or real
  market/consensus behavior (T46's own constraint list is inherited).
- No TaF claim status changes; no statement about GU, Temporal Issuance, or any other repository.
- Two methods are not two independent evidential units (Section 10).
- The designed witnesses do not establish that real systems exhibit these deltas.

## 13. Source-sovereignty statement

Time as Finality owns the semantics (record model, reconstruction rule, D1 profile, T46 access
vocabulary), the witness worlds, the computation, and every statement in this packet, at the pinned
revision. The receiving repository (`possibility-to-capability`) owns any classification,
normalization framing, gate verdict, or diagnosis built on this packet, and owns it separately —
nothing the receiver concludes upgrades, downgrades, or reinterprets any TaF claim, and TaF's
issuance of this packet endorses no receiver-side conclusion.
`ownership.authority_transfer = false`. The draft was authored without access to the receiver's
diagnostic frames, expectation matrices, or forecasts (firewalled lane; audited INDEPENDENT by the
receiver-side adversarial referee). Handling note for the receiver (referee advisory D6): the
section headers and fact glosses name which TaF object each intervention edited; a careful receiver
run should classify from the frozen computation blobs with this framing prose quarantined.

## 14. Interfaces

- `target_repository: possibility-to-capability`; `requested_datum:` classification of the
  ALPHA/BETA pair under the receiver's preregistered frames; `ownership_status: target_owned`.
- No datum is requested from GU or Temporal Issuance by this packet.

## 15. Issuance provenance

- Drafted 2026-07-16 by a firewalled lane-B agent in the possibility-to-capability program
  (draft: `possibility-to-capability/explorations/2026-07-16-northstar-unblock/lane-B-taf-source-packet.md`,
  which also carries the governing adversarial referee report: verdict SOUND-WITH-CORRECTIONS,
  firewall verdict INDEPENDENT).
- Adopted and issued 2026-07-16 by the Time as Finality steward with referee corrections D1
  (tautological invariance guard demoted to by-construction property), D2 (fact 3 narrowed to the
  one-directional asymmetry; R-1 rescoped), D5 (FORMALISM citation narrowed to its actual text),
  and the Section 9 grade note applied. D3 is discharged by this issuance itself; D4 is discharged
  by the complete `packet.json` in this bundle.
- TaF-side verification at issuance: blob hashes and byte lengths confirmed; computation re-run
  byte-identical (exit 0); referee probes P1 (formation-only edit reproduces ALPHA's delta), P1b
  (exhaustive 16-access-set sweep finds no access edit reproducing BETA's delta), and P2 (the
  invariance assert cannot fail) independently re-implemented and confirmed; semantics checked
  against the frozen `blobs/FORMALISM.md` and `blobs/T46-open-causal-scarcity-synchronization-boundary.md`.
- Issuing this packet commits TaF to nothing beyond the machine-checked computed facts 1–5 above,
  at exploration tier, formal-only grade, on designed finite witnesses.
