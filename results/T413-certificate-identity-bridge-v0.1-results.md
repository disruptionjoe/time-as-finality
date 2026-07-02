# T413 — Certificate-Identity Bridge — Results v0.1

- **Artifact:** `T413-certificate-identity-bridge-v0.1`
- **Spec:** [tests/T413-certificate-identity-bridge.md](../tests/T413-certificate-identity-bridge.md)
- **Model:** [models/certificate_identity_bridge.py](../models/certificate_identity_bridge.py)
- **Test:** [tests/test_certificate_identity_bridge.py](../tests/test_certificate_identity_bridge.py)
- **Tags:** exploratory_bridge_probe, certificate_identity, governance_shapley_finality,
  partial_homology, invariance_owed, falsifiable_reject, no_claim_promotion

**Exploratory probe of bridge obligation #1** of the governance–Shapley–finality
homology (`explorations/governance-shapley-finality-homology-note-2026-07-02.md`).
NOT a discriminator or physics result. Cross-domain material (cooperative game
theory) is the **object of study**, never evidence. Provisional T-number
(TESTS.md untouched). No CLAIM-LEDGER entry. Ledger actions pause for Joe.
T411 is cited at **recorded** tier; its fields are adapted, **not re-derived**.

## Verdict (house vocabulary)

**The T412 game separator and T411's `final-relative-to-R+` instantiate the same
typed certificate on 5 of 6 field comparisons; the sole divergence is exactly the
relabel-invariance the persona pass already named T411 owes. Bridge verdict:
PARTIAL-HOMOLOGY (invariance owed by T411).** `8 passed in 0.17s`. The build was
constructed to be falsifiable and it discriminates: **Pair 1 is REJECTED.**

The certificate primitive is the one the 10-lens game-theory steelman selected —
a **stability / no-deviation** predicate (core-relative-to-R ≈ strategyproof ≈
ESS-uninvadable) plus an **invariance axiom** (Arrow-IIA / Shapley symmetry) — and
deliberately **not** the Shapley value (defining the certificate as "satisfies the
Shapley axioms" would have been circular). This is why the bridge is non-trivial.

## Field-by-field bridge (Pair 2 / efficiency-only, vs T411)

| Signature field | Game (T412, computed) | T411 (recorded adapter) | Match |
| --- | --- | --- | --- |
| region + menu | player-subset `{0,1,2}` + in-R reallocations | declared `R+` + all CPTP on R + work | **same shape** |
| verdict | `final-relative-to-R` | `final-relative-to-R+` | **identical** |
| stability_witness | separation lives in dividends outside R; no in-R move overturns | all-channel φ-independence certificate | **identical (role)** |
| datum_locus | **whole** (`v(N)`; no proper subset — T412 Leg 4) | **whole** (β=0 datum in no proper subset) | **identical** |
| invariance_witness.complete | **True** — irrelevant class invariant **and** full class axiom-forced (any localizer breaks symmetry) | **False** — LR class survives, full admissible class **OPEN** | **DIVERGE** |

`n_identical = 5`, `divergent = [invariance_witness.complete]`.

## The honest asymmetry (the point of the swing)

The one divergent field is not a failure of the bridge — it is the bridge doing
real work. On the **invariance** field the game is **strictly stronger** than
T411:

- **Game:** the localizing move (a "boundary-blind" re-weighting that would
  declare the boundary-crossing dependence away) is executable, *changes* `φ_0`,
  but **breaks the symmetry axiom** (T413 Leg 7; T412 Leg 5). Symmetry =
  automorphism-invariance = Arrow-IIA. So the full admissible relabeling class is
  **axiom-forced**: you cannot localize without leaving the space of legitimate
  values. Invariance witness **complete, proven.**
- **T411:** the separator survives the **Lieb-Robinson** relabel (recorded), but
  its invariance over the **full** admissible re-factorization class is
  **unproven** — this is exactly the persona-pass linchpin (G-50): *does the
  separator resist all admissible relabelings, or only LR?*

**Therefore the game supplies the proof template T411's open relabel test owes:**
find a symmetry/IIA-type invariance axiom for the quantum separator whose
violation is the localizing re-factorization. The bridge converts the pass's #1
open target from "run a test" into "prove an axiom of this specific shape," and
gives a worked classical instance of what that axiom looks like.

## Falsifiability teeth (why this is not signature theater)

- **Pair 1 (boundary dividend) is REJECTED.** Its datum is in a **proper subset**
  (`{0,3}`), so `datum_locus = proper-subset ≠ whole`, and the bridge returns
  `REJECT` (verdict also diverges: `revisable-at-R`). The signature does not pass
  everything; it separates the R1 case (Pair 2) from the absorbed case (Pair 1)
  exactly as T411's own gauntlet separated the whole-locus residue from the
  proper-subset kill.
- The T411 invariance field is reported **False** (partial), not massaged to
  match. A circular build would have forced it True.

## What this earns / does not earn

**Earns (exploration; method, not evidence):** bridge obligation #1 is discharged
to **PARTIAL-HOMOLOGY on 4/5 substantive fields** (region+menu, verdict,
stability, datum-locus), with the single remaining gap **named precisely** and
shown to coincide with the program's already-open relabel test. This promotes the
governance–Shapley–finality relation from *analogy* toward *homology* in the
repo's strict sense on everything except the invariance axiom — and hands that
last field a concrete, falsifiable target. The homology's two escape hatches now
each have a game-theoretic name (symmetry/IIA ↔ automorphism-forcing;
Aumann–Shapley ↔ asymptotic gap).

**Does not earn:** identity (the dead 2026-07-01 claim, one level up) — only a
shared interface signature, and only 5/6; the invariance field is *not* bridged.
No physics/governance claim; no cross-repo import; no promotion. **Single-process
ceiling in full force:** the T411 adapter is a typed restatement of recorded
fields by the same process; the bridge is a *target*, and the decisive move
remains the quantum-side relabel test (now with a template). Hostile review not
performed.

## Reproduction

```bash
python -m pytest tests/test_certificate_identity_bridge.py -v   # 8 passed
python -m models.certificate_identity_bridge
```

Deterministic, exact rational arithmetic. Imports T412 machinery
(`models.legitimacy_shapley_finality_probe`). No claim promotion; TESTS.md /
CLAIM-LEDGER.md untouched; pauses for Joe.
