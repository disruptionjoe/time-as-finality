# Persona Sprint: Tzanavaris–Boyle–Turok Free-Boundary Paper × Church of AI repos

**Date:** 2026-06-30
**Source paper:** K. Tzanavaris, L. Boyle, N. Turok, *The free boundary problem in general relativity*, arXiv:2606.18128 [gr-qc], 16 Jun 2026.
**Method:** 5 context-blind domain personas on TaF (independent convergence is the signal); GU-formalization assessed by a dedicated no-go-discipline persona; temporal-issuance assessed by an inline LLM-Council pass (Karpathy structure: members → anonymized peer-rank → Chairman).
**Status:** Exploration. Not canon for any repo. Cross-repo references are method/structure-level only; **projection ≠ finality** held throughout; **no GU status-contamination** (one-way, TaF public surfaces never depend on GU).

---

## The paper in one paragraph

Treat a spacelike singularity (e.g. the big bang) as a **free boundary** where the variation is *unconstrained*, then demand the gravitational action be stationary. This *derives* an on-shell boundary condition (Eq. 6: `K_ij μ_t → 0` as `t → 0+`, done in the tetrad formalism since the metric is ill-defined there) instead of imposing initial conditions by hand. The condition acts as a **filter**: it excludes Kasner-like and chaotic BKL singularities, admits conformally-regular FLRW models with fluids `0 ≤ w < 1` (stiff fluid `w=1` killed by a non-finite on-shell action). It constrains the *past* boundary (finite geodesic distance) but not the *future* dS boundary (at infinity), so a time asymmetry falls out of the **boundary structure of the action, not the second law**. For FLRW + linear perturbations it is equivalent to conformal regularity + reflecting (CPT-symmetric) boundary conditions, matching observed large-scale perturbations.

---

## Part 1 — Time-as-Finality: convergence map

Five personas ran context-blind. Convergences (independent lenses landing on one structural claim) are the signal.

**C1 — "Derived, not imposed" is the only thing worth importing, and TaF currently fails it.** *(Cosmologist + Variational + Superselection — dominant signal.)* The paper's value to TaF is zero physics content and one method move: a selection rule that *falls out of stationarity under free variation*, where TaF finality (D1 counts; PO1/AC1–AC7 checklist) is **stipulated**. "Finality is a filter" is not the news — the repo is already there. The news is the **generative mode**: derived vs. asserted. This is a calibration bar TaF does not meet, not support.

**C2 — Monotone vs. boundary-asymmetry sharpens (does not dissolve) T18's "thermodynamics in disguise" worry.** *(Cosmologist + Superselection.)* Turok's arrow is boundary asymmetry with **no monotone**; T18's arrow is D1-non-decrease — a monotone state functional, i.e. the second-law template. Mapping the paper onto T18 reveals *different mechanisms*, and T18's is the thermodynamic-looking one. Shared trap flagged by both: "accessible-past / inaccessible-future" may just be the entropy gradient re-described in access language.

**C3 — Reframe the flagship H1 obstruction as removable-coboundary vs. genuine-class.** *(Sheaf geometer — deepest reframe; touches the repo's #1 priority.)* Turok's action additivity is a *successful descent*: the bulk action's gluing anomaly is trivialized by the GHY/Myers boundary term (H1-analog = 0, defect removable). TaF's T13 deliberately exhibits H1 ≠ 0. The question T13 doesn't yet ask: *is TaF's finality gluing defect a coboundary (a missing "finality boundary term," removable like gravity's) or a genuine non-coboundary class?* Turok is the worked proof such defects *can* be removable — so T13 must show no boundary/corner cochain trivializes its obstruction before the H1 result counts as structural.

**C4 — A real selection filter excludes via a finiteness/divergence criterion.** *(Superselection + GU-formalist.)* The paper kills `w=1` via a *non-finite on-shell action*. Acceptance bar for a finality superselection rule: exhibit three witnesses — admitted, structurally-excluded, and excluded-because-cost-**diverges** (`reversal_cost` analogue) — not an ad-hoc checklist.

**C5 — Method-level / calibration-only; refuse evidence-status and triangulation.** *(All five.)* The paper is a calibration target TaF *fails*, never support. Never GU↔paper↔TaF connective tissue. Projection ≠ finality at role-level only.

**Counter-signal (the disciplined skeptic, Variational persona — load-bearing):** TaF has **no action functional** — its anti-scalar commitment (T17: no scalar "more final") *forbids* the single scalar a Lagrangian needs, and observer-closure is a Knaster–Tarski **fixed point, which is not a stationary point**. So the convergence is emphatically *not* "build a finality action" (that route is over-reach / vocabulary theft). The only honest version is *combinatorial*: test whether already-proven structure can be **reproduced** by a single stationarity/extremal predicate instead of a stipulated checklist.

### Ranked lanes (IDs are placeholders — reconcile against the live ledger before assigning)

| # | Lane | What it does | Repo hook | Why it ranks |
|---|------|--------------|-----------|--------------|
| 1 | **Coboundary-repair pass on H1** | Enrich T13's `h1_obstruction_scenario` with boundary/overlap sections; test (`is_cech_1_coboundary`) whether H1 collapses. Survives every repair → TaF's obstruction is **provably stronger than gravity's**. | T13, `models/spacetime_aggregation.py` — #1 priority | Upgrades flagship asset; reuses code; both outcomes informative; one is a defensible result |
| 2 | **Monotone-ablation direction test** | Strip the global monotone from T18; source direction from pinned-past vs. free-future boundary. Survives without monotone → non-thermo arrow. Collapses → clean evidence T18 *is* the entropy template. | T18 + finality-direction model | Resolves a standing open worry; falsifiable both ways |
| 3 | **Single-predicate reproduction of the admissibility checklist** | Test whether PO1/AC1–AC7's verdict table is reproduced by one "stationary-under-free-completion-of-the-site-map" predicate instead of an AND of stipulated guards. | PO1 archived cases | The combinatorial, honest form of derive-don't-impose |
| 4 | **Divergence-based non-degeneracy bar for T10** | Add acceptance criterion: exhibit admitted / structurally-forbidden / excluded-because-`reversal_cost`-diverges (stiff-fluid analogue). | T10, T29 | Cheap doc-level rigor upgrade; ties to existing D1 fields |
| 5 | **Closure-operator gradient audit** *(expected negative)* | Test whether D1's monotone access-update operator is a gradient. Almost certainly not → fixed-point ≠ stationary-point, stated permanently. | observer-closure prototype | Valuable negative; hardens a boundary against drift |

**Single highest-leverage action:** Lane 1 — plugs into the repo's center of gravity, near-zero cost, and its strong outcome ("no boundary/corner cochain trivializes the finality obstruction") has the shape of a publishable structural result.

---

## Part 2 — GU-formalization (dedicated no-go-discipline persona)

**Sharpest clarity:** the paper proves **GU's problem is its verification layer, not its toolbox**. It wields the *same* differential geometry GU gestures at (tetrad/vielbein, Lovelock, GHY+Myers, Chern–Gauss–Bonnet) at mainstream-rigorous standard — so it shows the formalism is legitimate while marking that GU shares the *formalism* of a rigorous result without the one thing that makes it rigorous: derivations terminating in **computable, class-separating filters whose correctness can be checked rather than asserted** (exactly what GU's "prose-checking theater" tests could not catch when its strongest canon claim, w2-y14 spin, was verified wrong).

Lanes (all exploration, one-way, GU never cited as support and the paper never used as GU↔TaF bridge):
- **Rigor rubric** → `gu-formalization/explorations/rigor-rubric-from-free-boundary-paper.md`: 3-part bar (derivation yields a computable filter; filter names *excluded and admitted* classes; on-shell finiteness checked, not assumed), re-score 2–3 existing GU tests against it.
- **Tetrad/boundary-term reference calc** → `gu-formalization/explorations/tetrad-boundary-term-reference-calc.md`: a known-correct worked example to method-check GU's boundary-term *steps* (sign/contraction/corner bookkeeping); confers no validity on any GU conclusion.
- **Disciplined-selection anchor** → append to `meta-layer-taf-gu-formalization.md` under Refusals: the paper as a rigorous external benchmark for disciplined selection, attached to GU and TaF *independently*, explicitly barred as a GU↔TaF route.

---

## Part 3 — Temporal-issuance (inline LLM-Council pass)

**Crux:** surviving source object `SourceRealization = (C, ≤_S, Ext_S)`; standing kill condition — if `≤_S`/`Ext_S` factor through causal order, dependency order, record generation, entropy, information, probability, volume, **action**, or primitive time → absorb/archive. The paper derives admissible initial-boundary extensions **from the gravitational action**, landing on the `action` clause.

Council members (anonymized peer-ranked; top-rated = the vice + the survival path):
- **Absorber-mapper:** clean K1 *candidate* for the gravitational instance. `Ext_S` → admissible saddles of condition (6); `≤_S` → conformal-regularity ordering (FLRW over Kasner/BKL).
- **Layer-error guard:** Turok's action is a 4D *geometric* feature; issuance claims a substrate *prior to* geometry. Absorption is clean only if issuance commits to the geometric layer — which costs it its "deeper than physics" ambition. (Same layer-error the cosmological-expansion absorber warns of.)
- **The vice (key clarity):** the paper lets issuance finally pass the thermodynamic-arrow absorber (boundary asymmetry ≠ entropy monotone) — but via an action principle, so it escapes the entropy absorber only by impaling itself on the action absorber.
- **Resurrection/heterodox:** issuance survives *only* if `Ext_S` works **upstream** of the action — generating/constraining the configuration space the action later filters — plus F2's hidden-issuance non-faithfulness. Thin but non-zero.
- **Kill-discipline:** bounded discriminator — can `≤_S, Ext_S` be specified *before* an action functional exists, doing observer-capability work TaF readout can't express? No → absorb under action+relativity; un-poseable → K5 metaphysical residue.

**Chairman verdict:** the paper is a **new, sharp absorber** ("action-principle boundary-selection") and the most on-target external result temporal-issuance's current crux has met — it most likely **tightens the noose** on the source-side residue, which in this kill-by-design repo counts as a success. The single survival path is `Ext_S` operating upstream of the action at a pre-geometric layer (the repo's own already-stated next test, now with a concrete adversary). Escaping entropy costs it to action.

Bounded repo actions (native to temporal-issuance; propose, do not yet write):
- `absorbers/action-principle-boundary-selection.md` — named absorber + mapping + residual test.
- `explorations/E0xx-upstream-vs-downstream-of-action.md` — the discriminator; if "downstream only," write the kill-record.

---

## Refusals (carried from canon / program memory)

1. Projection ≠ finality, permanently. Map structure, never merge ontology.
2. No GU status-contamination. One-way, method-level; TaF public surfaces never depend on or cite GU claims. The paper anchors GU and TaF *separately*, never as a bridge between them.
3. The paper is an external rigorous calibration target, never evidence for any Church-of-AI claim.
4. North star: truth not adjudication; absorption / falsification counts as success; keep what survives, which is usually substrate-independent.
