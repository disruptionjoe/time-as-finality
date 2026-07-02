# T417 — Computational Finality Boundary (R2, Door C) — Results v0.1

- **Artifact:** `T417-computational-finality-boundary-v0.1`
- **Spec:** [tests/T417-computational-finality-boundary.md](../tests/T417-computational-finality-boundary.md)
- **Model:** [models/computational_finality_boundary.py](../models/computational_finality_boundary.py)
- **Test:** [tests/test_computational_finality_boundary.py](../tests/test_computational_finality_boundary.py)
- **Tags:** exploratory_R2_swing, door_C_complexity_forced, closed_model,
  reservoir_killer_dodged, copresent_but_infeasible, asymptotic_computational_gap,
  QRA_conditional, no_claim_promotion

**Exploratory big-swing on the R2 question — Door C.** NOT a physics or crypto
result beyond cited standard assumptions. Cross-domain material (cryptography /
complexity) is the **object of study**, never evidence. Provisional T-number
(TESTS.md untouched; registration pauses for Joe / the numbering automation). No
CLAIM-LEDGER entry. Ledger actions pause for Joe.

## Verdict (house vocabulary)

**Door C is the first R2 door the reservoir-idealization killer cannot touch — at
the honest price of a computational-hardness assumption and a family-level (not
single-instance) boundary.** All five predeclared legs hold; `7 passed`. The
boundary is forced by **computation** in a **closed, deterministic** model (no
reservoir, no partial trace), it **concedes co-presence but denies feasible
recovery**, and it **supplies the independent operational evidence T416 demanded**
(reach = poly-time feasibility, an external bound). It does **not** discharge R2
unconditionally: it is conditional on QRA/factoring hardness and physical only at
the asymptotic/family level — which makes it a **refinement of Door B**, with
computation as the scaling resource.

## Construction

Goldwasser–Micali quadratic residuosity. `N = 77 = 7·11`; the reach holds `N`, not
`p,q`. `x_A = 58` is a QR mod `N`; `x_B = 24` is a non-QR mod `N` with Jacobi `+1`.
The **datum** = QR-ness of `x` mod `N`, determined by `(x, N)`. The trapdoor-free
poly-time predicate (the Jacobi symbol) is `+1` for both; distinguishing them ≡ the
**Quadratic Residuosity Problem** (assumed hard; reduces to factoring `N`). The
**boundary-crossing menu** = the factorization `p,q`, outside the reach.

## Leg-by-leg

**Leg 1 — co-presence.** With the trapdoor, `x_A` is a QR and `x_B` a non-QR mod
`N` (**differ**). QR-ness is a well-defined function of `(x,N)`: the datum is
present in the reach's data.

**Leg 2 — reach-blindness (the equality).** The poly-time predicate available
without the trapdoor — the Jacobi symbol — is `+1` for **both** (identical). No
feasible reach operation distinguishes A from B; distinguishing ≡ QRA (cited
assumption, **not** proven). Computational analog of T411's "equal under all
R-supported statistics."

**Leg 3 — boundary crossing = the trapdoor.** With `p,q`, the Legendre symbol
`(x/7)` is `+1` for A and `−1` for B — the datum separates. The trapdoor is
genuinely absent from the reach.

**Leg 4 — killer premortem.**
| Killer | Door C's answer |
| --- | --- |
| **Reservoir-idealization** | **Dodged structurally.** Closed, deterministic, number-theoretic; no partial trace, nothing adopted. The killer that killed every prior R2 attempt cannot even be stated here. |
| **Joint-record completion** | **Conceded, then denied.** Brute-force factoring of `N` **does** recover the datum (co-presence confirmed executably) — completion wins information-theoretically — but only at a **cost**, so *feasible* recovery is denied. |
| **Wait-longer / asymptotic** | Trial-division cost across the semiprime family `[15,77,143,899,3599]` is strictly increasing: **`[2, 6, 10, 28, 58]`**. The boundary is a *growing cost*, physical only at the family/asymptotic level (conditional on factoring hardness; trial division is illustrative, the basis is QRA). |
| **Lieb-Robinson** | **N/A** (no spatial / light-cone structure). |

**Leg 5 — honest verdict.** Door C = an **asymptotic computational gap**, a
refinement of Door B with computation as the scaling resource. It **supplies
T416's independent operational evidence** (reach = poly-time, not chosen to
protect the separator). The boundary is **physical conditional on QRA/factoring
hardness and only at the family/asymptotic level**; any single fixed instance is
brute-force recoverable (finite work), hence still declared/crackable. **R2 is not
unconditionally discharged.**

## What this earns / does not earn

**Earns (exploration; method, not evidence):** the first R2 construction the
recurring **reservoir-idealization** killer structurally cannot touch — because
there is no reservoir. It cleanly instantiates the "concede co-presence, deny
feasible recovery" defeat of joint-record completion, supplies the *independent*
operational structure T416 proved R2 requires (a poly-time feasibility bound that
is external, not separator-serving), and beats wait-longer via a growing
(assumed-superpolynomial) cost. It also **unifies Doors B and C**: the
computational boundary is an asymptotic gap, so the "physical" claim is honestly a
*family/limit* statement — the same shape as the Aumann–Shapley (T413) infinite-
layer escape.

**Does not earn:** an unconditional physical boundary. The wall rests on QRA /
factoring hardness (**unproven**), and it is **asymptotic** — for any single fixed
`N` the datum is finite-work recoverable, so a single-instance boundary is still
declared/crackable. "Computationally forced" means *forced relative to a hardness
assumption and in the family limit*, which is a coherent, defensible notion
(physical Church–Turing) but is **not** an unconditional discharge of R2. No
physics/crypto claim beyond cited standard assumptions; no cross-repo import; no
promotion. **Single-process ceiling** in full force. Hostile review not performed.

## Net for R2

The three doors now have a first executable datapoint each way:
- The recurring killer (reservoir-idealization) is **specific to the
  thermodynamic framing** — Door C shows a closed computational model sidesteps it
  entirely.
- But the boundary's *physicality* still bottoms out at the **same place** every
  other thread reached: it is **asymptotic and conditional** (here on factoring
  hardness; in Door B on the scaling limit; in the homology on "is the operational
  structure forced"). R2's honest current status: **a physical boundary is a
  family/limit + a forcing assumption, not a single-instance closed-model fact** —
  consistent with M1 (finite closed ⇒ declarable) from the persona pass.

## Reproduction

```bash
python -m pytest tests/test_computational_finality_boundary.py -v   # 7 passed
python -m models.computational_finality_boundary
```

Deterministic, exact integer arithmetic; closed model (no reservoir). No claim
promotion; TESTS.md / CLAIM-LEDGER.md untouched; pauses for Joe.
