# T417 — Computational Finality Boundary (spec, frozen)

**Status:** exploratory big-swing on the R2 question — Door C (complexity-forced
recovery). Provisional T-number (**TESTS.md NOT edited**; noted here only;
registration pauses for Joe / numbering automation). No claim promotion; no
CLAIM-LEDGER entry. Cross-domain material (cryptography / complexity) is the
**object of study**, never evidence. Spec frozen before the model file.

## The R2 question and Door C

R2 (the persona pass + T412/T414/T415/T416): make the capability boundary
**physically forced, not declared**. T416 sharpened it: the boundary needs
**independent operation/coupling evidence** — the separator cannot self-certify
its own factorization. Every prior attempt died to the **reservoir-idealization**
killer (departure is a stipulated partial trace, "adopted not derived").

**Door C forces the boundary with computation instead of energy or a trace.** The
model is **closed and deterministic** — there is no reservoir and no partial
trace, so the reservoir-idealization killer **structurally cannot apply**. The
datum is information-theoretically **co-present**, but recovery is
**computationally hard**, reducing to a standard assumption. Reach = the
**feasible (poly-time) operations** — the canonical, externally-motivated resource
bound, which is exactly the *independent* operational structure T416 says R2
needs (it is not chosen to protect the separator).

## Construction (Goldwasser–Micali / quadratic residuosity)

Fix `N = p·q`, `p,q` odd primes (the reach holds `N`, **not** `p,q`). Two data:

- **A:** `x_A` a quadratic residue mod `N` (Legendre `(x_A/p)=(x_A/q)=+1`).
- **B:** `x_B` a quadratic non-residue mod `N` with **Jacobi symbol +1**
  (`(x_B/p)=(x_B/q)=−1`).

The **datum** = QR-ness of `x` mod `N`. It is **determined** by `(x, N)`
(co-present). The **poly-time reach predicate without the trapdoor** is the Jacobi
symbol, which is **+1 for both** (blind). Distinguishing A from B ≡ the
**Quadratic Residuosity Problem**, assumed hard (**QRA**; reduces to factoring
`N`). The **boundary-crossing menu** = the trapdoor (the factorization `p,q`),
which lives outside the reach; with it, the Legendre symbol mod `p` separates them.

## Fixed constants (predeclared)

`N = 77 = 7·11`; `x_A = 58` (`58≡2 mod 7`, `≡3 mod 11`: QR both); `x_B = 24`
(`24≡3 mod 7`, `≡2 mod 11`: non-QR both). Both Jacobi `(·/77) = +1`.
Cost-growth family of semiprimes: `[15, 77, 143, 899, 3599]`
(`=3·5, 7·11, 11·13, 29·31, 59·61`).

## Predeclared legs (verdicts fixed before running)

1. **Co-presence.** With the factorization: `x_A` is a QR, `x_B` is a non-QR mod
   `N` (they **differ**). QR-ness is a well-defined function of `(x,N)` — the
   datum is present in the reach's data.
2. **Reach-blindness (the equality).** The poly-time predicate available to the
   reach without the trapdoor — the Jacobi symbol — is `+1` for **both** A and B
   (identical). No feasible reach operation distinguishes them; distinguishing ≡
   QRA (cited assumption, not proven here). This is the computational analog of
   T411's "equal under all R-supported statistics."
3. **Boundary crossing = the trapdoor.** With `p,q` (outside the reach), the
   Legendre symbol `(x/p)` is `+1` for A and `−1` for B — the datum separates.
   The trapdoor is genuinely absent from the reach.
4. **Killer premortem (computed where possible).**
   - *Reservoir-idealization* → **dodged structurally**: the model is closed and
     deterministic; there is no partial trace, no reservoir, nothing adopted.
   - *Joint-record completion* → **conceded-then-denied**: brute-force factoring
     of `N` **does** recover the datum (co-presence confirmed executably), so
     completion wins information-theoretically — but only at a **cost** (trial-
     division step count), so feasible recovery is denied.
   - *Wait-longer / asymptotic gap* → the trial-division cost is monotonically
     **increasing** across the semiprime family (the honest core: the boundary is
     a *growing cost*, physical only in the family/asymptotic sense, conditional
     on factoring hardness). Predeclared: step counts strictly increasing.
   - *Lieb-Robinson* → **N/A** (no spatial/light-cone structure).
5. **Honest verdict.** Door C = an **asymptotic computational gap** — a refinement
   of Door B (asymptotic) with computation as the scaling resource. It **supplies
   T416's independent operational evidence** (reach = poly-time, an external
   bound). The boundary is **physical conditional on QRA/factoring hardness and
   only at the family/asymptotic level**; for any single fixed instance the datum
   is brute-force recoverable (finite work), so a single-instance boundary is
   still declared/crackable. **R2 is NOT unconditionally discharged.**

## Success / honesty criteria

Succeeds as exploration if it exhibits, executably, a closed-model boundary that
(a) dodges the reservoir killer, (b) concedes co-presence yet denies feasible
recovery, (c) supplies independent operational evidence (poly-time reach), and
(d) is honestly bounded: conditional on QRA and asymptotic (single instances
crackable), converging with Door B. Predeclared honest outcome: **the first
closed-model R2 door that the recurring reservoir killer cannot touch — at the
price of a computational-hardness assumption and a family-level (not
single-instance) boundary.** No physics/crypto claim beyond cited standard
assumptions; no promotion; pauses for Joe.
