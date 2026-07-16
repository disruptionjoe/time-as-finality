# TAF-002: Capability Adjudication of the Frozen P2C-W1 Witness (source-issued, v0.1)

Issued by the Time as Finality steward on 2026-07-16, on the mailbox proposal
`CapacityOS/system/mailboxes/time-as-finality/20260716-p2cw1-superconducting-ring-witness-capability-adjudication.md`.
This packet is TaF's sovereign return on the capability-adjudication question routed to it by the
possibility-to-capability (P2C) repository. Exploration tier; no TaF claim status changes;
`authority_transfer = false`. Whether anything in this return discharges, kills, or advances any
P2C object is entirely P2C's determination.

## 1. The adjudicated bundle (identified by hash manifest, per the combinability rule)

Bundle: `possibility-to-capability/exports/witness/P2C-W1-superconducting-ring-v0.1/`
(`witness_id: P2C-W1`, `bundle_status: WITNESS_FROZEN`), freezing commit
`4c9c28bbad0bdca45377dd2265b28b1fec3cc9ef`, blob content revision
`850521c2fc07b277734e293cd68c0928bb0cb6de`, sha256 manifest:

- `blobs/WITNESS-FREEZE.md` — `694443cacddfcd784a81e01a6e059557b5b1e6aaeea8c0a7616a4f0ac6b71b51` (19964 bytes)
- `blobs/REFEREE-REPORT.md` — `dfd966259d9e8e2f58bc3725f53f5751c08e0f6b4015c01c333548e09eca0113` (9188 bytes)
- `blobs/physical_witness_discriminator.py` — `42f647eb7a1f6533e26ae9f6f321824693a77517540259fe505ce968d59ea9eb` (16916 bytes)
- `blobs/discriminator_output.txt` — `b917f59b2e5f6ee3221a08260ce3f22043c7b843c89343a0fe7e778eb84db45f` (2550 bytes)

TaF-side verification before adjudication (2026-07-16): all four blob sha256s and byte lengths
re-hashed and confirmed against `witness.json`; the freezing commit and content revision confirmed
to exist in the P2C repository, with all three originating artifacts byte-identical at the content
revision (git-show re-hash); the witness discriminator re-run from the frozen blob (exit 0, stdout
byte-identical to `blobs/discriminator_output.txt`). The bundle was treated as stable input only
after these checks. This return adjudicates THIS bundle, unchanged; per P2C's own rule it is
combinable only with returns tested on the same manifest.

## 2. Exact question adjudicated

As posed by the proposal (quoted, not reworded):

> Given the declared budget-matched counterfactual pair, is the N-to-S pair a capability change
> under TaF's invariant standards — i.e., does the task "hold a quantized, locally-invariant,
> zero-maintenance-cost persistent record" constitute a change in achievability that survives
> TaF's admissible reformulations — or does it factor through TaF's own machinery: a change in
> record formation, holder access, or resource/erasure structure that TaF's record/access
> analysis (in the spirit of the TAF-001 ALPHA/BETA intervention separation) already accounts
> for without a capability-level change?

`question.decision_type: other` (a capability adjudication in TaF's native semantics; not an
independence or forcing claim).

## 3. Semantics used (all TaF-owned, none imported from P2C)

- **T1/FORMALISM record model** (`blobs/FORMALISM.md`, byte-identical to the copy frozen in
  TAF-001): causal record graph, record token `(id, proposition, value, event, holder,
  erasure_cost)`, causal-availability conditions 1–2, reconstruction rule (fixed threshold plus
  no-competing-value clause), D1 profile `F_O,e(x) = (A, R, B, C)` with `C_therm` reported
  separately, componentwise preorder, no scalarization.
- **Task achievability = reconstructibility** under the reconstruction rule — TaF's native task
  semantics (TAF-001 premise A5, reused verbatim). No other task semantics is used or endorsed.
- **CapabilityContract v1 discipline** (T583, frozen as `blobs/T583-capability-contract-v1.md`):
  capability is a region-indexed attainable envelope over a declared context (region,
  observer/access profile, task family, operation menu, resources, budget, horizon, quotient);
  a changed task, menu, access profile, resource, budget, horizon, or region is never a matched
  intrinsic-capability comparison; completions fail closed.
- **T584 admissible morphism classes** (frozen as `blobs/T584-capability-invariance-morphism-gate.md`):
  substantive representation changes, gauge changes inside the declared quotient, and declared
  irrelevant coarse-graining preserve the native envelope; task-vocabulary merges are the caught
  inadmissible class. These are "TaF's admissible reformulations" for this adjudication.
- **TAF-001 ALPHA/BETA separation** (`time-as-finality/exports/packets/TAF-001-paired-record-intervention-v0.1/`,
  `bundle_digest 0b0085419670a619c9574cd2accf1c4347e68ab6f249762372d8626bd8256a94`): access-side
  edits (condition-2 membership) versus record-formation-side edits (token inventory and graph)
  are distinct intervention classes in the T1 model, and both can change task achievability.
- **Observer level:** reconciler. No conscious-observer claim.

The witness's physics (integer fluxoid lattice, DEFORM/gauge invariance of the winding, zero
ongoing maintenance with a macroscopic phase-slip erasure barrier in S; continuous, non-invariant,
decaying-or-maintained current in N) is consumed as STIPULATED structure at literature grade from
the frozen bundle. TaF does not re-derive, upgrade, or vouch for the physics.

## 4. The TaF-native model of the declared frame

The witness's declared frame (referee correction R-D1, load-bearing) is the budget-matched
counterfactual pair. TaF models it as **two region-indexed contexts** in the T583 sense, sharing
byte-identical task family, operation menu `{COOL, THREAD, PROBE_READ, DEFORM}`, observer access
set, residual budget, horizon, and quotient, and differing only in region physics:

- **Context S:** ring in the superconducting branch at `T_f`. Record formation at cool-through
  yields a token with value on the integer lattice, DEFORM-invariant, `maintenance_draw = 0`,
  unmaintained lifetime at the literature metastability cap, `erasure_cost` macroscopic.
- **Context N:** matched reference normal conductor at the same `T_f` and the same spent
  COOL+THREAD budget. Any formed token has continuous value, is not DEFORM-invariant, requires
  strictly positive per-epoch maintenance draw to survive at all, and has `erasure_cost ≈ 0`.

Task family TV (reconstruction-rule sense, mirroring the witness's native signatures):
`tau_Q` (reconstructed value lies on the integer lattice across the declared flux sweep),
`tau_I` (reconstructed value identical with and without DEFORM), and
`tau_P` (reconstructible at the declared horizon with total maintenance spent exactly zero).

The computation is the frozen blob `blobs/taf002_p2cw1_adjudication.py` (pure Python 3, stdlib
only, deterministic; sha256 `1c75eec784687b14d965f95665f0e52a25b5a250381e62b40d061cbd54ffcfcd`,
18891 bytes). Its captured output is `blobs/taf002_output.txt` (sha256
`aba2329f9539b5f7641391a56e1a418334a04ec2d3e9b94f860d154afd483789`, 3832 bytes). Verification:
re-run the script, byte-compare stdout. Headline: 10 [E] + 3 [F] evidential checks, 1 [T]
theorem-consequence check; exit 0; deterministic (re-run diff empty at issuance).

Computed results consumed by the verdict:

1. **Pair delta (b1):** in the declared frame, S achieves `(tau_Q, tau_I, tau_P) = (1, 1, 1)` and
   N achieves `(0, 0, 0)` under the reconstruction rule at matched budget and horizon.
2. **Not access-side (c1):** enlarging N's observer access set to all holders leaves N at
   `(0, 0, 0)`. The delta is not an ALPHA edit — it does not factor through holder access.
3. **Not resource-side in the declared frame (c2):** multiplying N's residual budget by 10^6
   leaves N at `(0, 0, 0)`: `tau_Q`/`tau_I` fail at every budget, and `tau_P` fails because every
   N holding strategy has strictly positive draw (zero-maintenance is the task, not a budget line).
4. **Not hidden-state (c3):** latent auxiliary records in N manufacture none of the signatures.
5. **Survives TaF's admissible reformulations (c4, c5, guarded by c6):** unit-representation,
   holder-gauge, and declared irrelevant-coarse-graining morphisms preserve both envelopes; the
   inadmissible task-vocabulary merge is detected and rejected (it collapses distinct native
   envelopes to one merged value).
6. **Neutrality (c7, guarded by c8):** the verdict tracks the physics under branch-label swap; a
   label-keyed scorer is exhibited failing.
7. **The carrier (c11):** with access sets and budgets byte-identical, the entire delta lives in
   record-formation/erasure structure — which tokens are formable, their lattice, invariance,
   draw, lifetime, and erasure cost. In TAF-001 vocabulary: a BETA-side object, not an ALPHA-side
   one.
8. **The absorber, exhibited (c9, guarded by c10):** a SINGLE declared context whose region
   contains both phases and whose menu crosses `Tc` already contains the task family in its
   envelope — under that declaration there is no pair and no delta. The absorption is caused
   specifically by admitting the target phase into the declared region; the same move without the
   target phase absorbs nothing.
9. **Persistence grading (c12):** beyond the literature metastability horizon the model does not
   assert `tau_P` for S. The invariant carriers at every horizon and budget are `tau_Q` and
   `tau_I`.

## 5. VERDICT (split; each clause scoped exactly)

**Clause 1 — capability change: AFFIRMED, frame-indexed to the declared budget-matched
counterfactual pair, at exploration tier.** Under TaF's invariant standards — task achievability
as reconstructibility, evaluated over two declared region-indexed contexts with matched task
family, menu, access, budget, horizon, and quotient — the N-to-S pair is a capability change:
the achievability delta `(1,1,1)` vs `(0,0,0)` survives TaF's admissible reformulations (T584
representation, gauge, and irrelevant-coarse-graining classes) and does not disappear under TaF's
admitted fail-closed controls (access enlargement, resource enlargement, hidden state). This is
the strongest sense of "capability change" TaF's current machinery can assert, and it is asserted
at that machinery's grade: a designed finite witness consuming literature-grade stipulated
physics, formal-only evidence, review-only standing.

**Clause 2 — the factor: NAMED, and non-deflationary in TaF semantics.** The delta factors
entirely through TaF's record-formation/erasure structure (the TAF-001 BETA side): with holder
access and resources byte-identical across the pair, what differs is which record tokens are
formable and their lattice, local-invariance, maintenance-draw, lifetime, and erasure-cost
structure. It does NOT factor through holder access (not ALPHA), and does NOT factor through
resource/erasure accounting within the declared frame. Critically, in TaF's own semantics this
factoring does not "account for the change without a capability-level change": record-formation
structure is precisely the mechanism by which task achievability changes (TAF-001, computed facts
1–3). The proposal's dichotomy — capability change XOR factors through TaF's record machinery —
is therefore NON-EXCLUSIVE under TaF's standards. The honest one-line answer to the exact
question is: **both — it is a capability change in the declared frame, and it is carried by
(reducible to) a record-formation/erasure-structure difference; the deflationary readings
(access, resource, hidden state) are each executably excluded.**

**Clause 3 — the boundary: the fixed-family absorber is NOT adjudicable by TaF's standards, and
this return does not discharge it.** TaF's capability object is region-indexed and frame-TAKING
by construction: the context (region, menu, budget, horizon) is declared input, fixed before
comparison, and T583 treats any changed context as an unmatched comparison in both directions.
Whether the two-context individuation (the declared counterfactual pair) or the one-context
whole-family reading (one region containing both phases, COOL in the menu — under which the task
family was always in the envelope and no change exists) is the LEGITIMATE description of the
physical situation is a context-individuation / completion-legitimacy question that TaF's
formalism consumes as a declaration rather than derives. The fixture exhibits both readings
executably (c9/c10) and endorses neither. That question remains with Temporal Issuance's
CompletionClass machinery per the witness's own routing, and P2C's falsifier F1 remains live and
untouched by this return.

**Grading riders:** (i) the persistence leg `tau_P` is affirmed only up to the literature-grade
metastability cap ("effectively infinite", never "provably infinite"); the quantization and
local-invariance legs are the carriers that survive at every horizon and budget. (ii) Within the
S context, the cool-through formation event is a strict-finalization-type event in T18's sense
(record formation with no D1 dimension decreased and `C_therm` raised from ~0 to macroscopic);
this is an intra-context observation, not a cross-context order, and no temporal-order,
issuance, or T586-style record-capability-order consequence is asserted over this witness.

## 6. Assumptions (all load-bearing, all explicit)

- A1 (definition): TaF T1/FORMALISM record model (as in TAF-001 A1), frozen in `blobs/FORMALISM.md`.
- A2 (definition): task achievability = reconstructibility (TAF-001 A5, reused verbatim).
- A3 (definition): "TaF's admissible reformulations" = the T584 morphism classes over the T583
  contract; "admitted controls" = the T583/T585 fail-closed completion classes (access, resource,
  hidden-state) as implemented in the fixture.
- A4 (external stipulation, literature grade, quarantined): the branch physics as frozen in
  P2C-W1 (`WITNESS-FREEZE.md` sections 0–1 under the R-D1 frame declaration). TaF asserts nothing
  about real superconductors beyond consuming this stipulation.
- A5 (construction_choice): the specific finite parameters — threshold k=1 fixed before
  evaluation, horizon 100 epochs, matched residual budget 50, flux sweep {1/5, 2/5, 3/5, 4/5,
  13/10}, DEFORM drift 3/100, metastability cap 10^12 epochs. Designed witness, not a measured
  system.
- A6 (implementation): the frozen Python program correctly implements A1–A3 over A4–A5.

## 7. Evidence structure (v0.2 dependency honesty)

- `method_ledger`: M1 (pair evaluation + controls, one deterministic computation).
  `raw_method_count = 1`; `raw_method_count_is_independence_count = false`.
- All assumptions A1–A6 are load-bearing for M1; there is one implementation, one designed frame,
  one task family. This packet asserts no independence result of any type.
  `independence_type: not_applicable`; `convergence: not_applicable`.
- The witness's own discriminator (P2C-owned) was re-run for bundle verification only; it is not
  counted as a TaF method and lends this packet no evidential weight.

## 8. Residuals

- R-1: The adjudication is existential over one designed finite frame implementing the declared
  counterfactual pair; no universal claim over frames, thresholds, horizons, or task semantics.
- R-2: `tau_P` beyond the metastability cap is unadjudicated by construction (c12); a receiver
  needing unbounded-horizon persistence has no TaF support here.
- R-3: The fixture consumes the witness's physics as stipulation; any error in the frozen
  bundle's literature-grade physics propagates to Clause 1 unchanged (corrections would produce a
  witness v0.2 and require re-adjudication).
- R-4: Whether formation-side simulability results (TAF-001 R-1) bear on the whole-family
  question is not explored; no bridge from Clause 2 to Clause 3 is claimed.
- R-5: The D1 profile is reported for the S record at k=1 single-holder only; redundancy (R),
  branch (B) structure with multiple holders/probes is not exercised.

## 9. Nonclaims

- No verdict on the fixed-family absorber / P2C falsifier F1, in either direction (Clause 3).
- No claim about capability "enlargement" versus "disclosure" — those are P2C hierarchy terms;
  TaF asserts only the frame-indexed achievability delta and its factor structure in TaF
  vocabulary. Any mapping of this return onto P2C's hierarchy grades is receiver-owned work.
- No claim that superconductivity "is" finality or any TaF object; no physics derived; no real
  superconductor measured; literature-grade stipulations are consumed, not endorsed.
- No temporal-order, issuance, or record-capability-order (T586) consequence over this witness.
- No TaF claim-status, Canon-Index, ledger, or public-posture movement; the TAF-001 packet and
  all TaF claims (R1, A1, PO1, CS1, D1, T46, T583–T586 verdicts) are untouched.
- No statement about Temporal Issuance's pending or future return; combinability of the two
  sovereign returns is P2C's determination under its own manifest rule.

## 10. Source-sovereignty statement

Time as Finality owns the semantics, the designed frame, the computation, and every statement in
this packet at the pinned revision. P2C owns the witness bundle, its hierarchy vocabulary, its
falsifiers, and any conclusion built on this return; nothing P2C concludes upgrades, downgrades,
or reinterprets any TaF claim. `ownership.authority_transfer = false`.

## 11. Interfaces

- `target_repository: possibility-to-capability`; `requested_datum:` none (this packet IS the
  return of the datum P2C requested); `ownership_status: target_owned` for all downstream use.
