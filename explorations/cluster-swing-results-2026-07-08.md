# Cluster-swing results: testing the six profound-possibility clusters

2026-07-08. Executes `explorations/starter-swing-orchestration-plan-2026-07-08.md` over the six clusters
from `explorations/nested-band-twenty-persona-profound-possibilities-2026-07-08.md`. Two-phase pipeline
(probe -> build) with the cross-modal rule: every verdict is backed by executed code, not argument. All
re-run by the orchestrator (exit 0 confirmed locally).

## Scorecard

| Cluster | Probe | Built | Result |
|---|---|---|---|
| A access structure | conditional | yes | **CONFIRMED, but localized** (double dissociation) |
| B copy law | **dead** | - | no-cloning set = unreadable band (a relabel); claimed conservation J+R non-conserved (1->6) |
| C inner-label | viable | yes | **CONFIRMED (partial), the standout** -- monogamy sharper than CHSH; wall corrected 1/2 -> 2/3 |
| D arrow / spacetime | **dead** | - | ABL statistic invariant under pre/post swap (0.000 over 2000 fixtures); only asymmetry is causal-escape, H7-absorbed |
| E graded interior | **dead** | - | under the fixed algebra, recovery is flat binary across band depths -- no intrinsic grading |
| F band relativity | **dead** | - | commutativity-onset is ANTI-correlated with band-exit -- falsifies CRDT #15 |

Models kept: `models/finality_swing_A_access_structure.py`, `models/finality_swing_C_inner_label.py`
(both exit 0). Four clusters killed at probe by executed checks.

## Survivor A -- access structure is intrinsic only at the inner corner

Model tries hard to lower the entangled recovering coalition below n (over all n! permutations x a 4^n
local-unitary grid) and fails: every proper coalition has reduced-state distance exactly 0 (no operation
recovers the value); only the full n-of-n set recovers. Invariant at n for n=2 (Bell) and n=3 (GHZ).

**Double dissociation (the sharpening):** the minimal-recovering-coalition order parameter is *intrinsic*
(invariant under all admissible re-arrangements) ONLY at the entanglement / CHSH>2 corner, where monogamy
forces n-of-n. At the encryption corner it is a *free relabel* -- re-keying resets the minimal coalition to
any size {1,2,3} while outsider information stays 0 and CHSH stays <=2. So "finality = access structure"
(#18) is **not a single monotone across the whole nested band**; it carries intrinsic content only at the
inner corner. #18's hope of one order parameter over the whole band is down; its content survives, localized.

## Survivor C -- monogamy is a sharper inner label than CHSH (and corrects a number)

The standout result, and it **replaces CHSH as the inner-band discriminator.**

- **k_max (shareability number)** is a single monotone order parameter: `inf` for in-the-clear and encrypted
  (OUTER, copyable), `finite` for the entangled INNER band. It brackets both bands with one number.
- **It comes apart from CHSH.** On the Werner band `2/3 < p <= 1/sqrt2` the state is un-2-shareable
  (monogamous -> INNER) yet CHSH <= 2. CHSH would misfile that window as OUTER. So monogamy is strictly
  sharper, not a relabel.
- **Correction to a quantitative claim.** The shareability wall is **2/3, not 1/2.** Derived from an
  explicit symmetric-extension SDP (S_3 twirl -> 6-dim group algebra; nullspace + min-eigenvalue), validated
  by an explicit PSD swap-symmetric 2-extension at p=0.60 whose both marginals equal Werner(0.60). `1/2` is
  the Werner *projective LHV* threshold (Werner 1989), a different label.
- **Corrected threshold ladder:** `1/3` (entanglement / negativity) < `2/3` (2-shareability / monogamy) <
  `1/sqrt2 ~ 0.707` (CHSH). The come-apart window `(2/3, 0.707]` is real but narrower than the note implied.

## The integrated finding (A + C)

Both survivors point the same way: **the deep, intrinsic invariants live at the inner (genuinely entangled)
corner; the outer band (encryption / classical inaccessibility) is a free relabel on those axes.** The sharp
object is the **shareability number k_max** -- monotone across clear / encrypted / entangled, finite only
inside -- and the access structure (n-of-n) is its combinatorial content at the entanglement corner.
Recommended: **retire CHSH>2 as the inner label in favour of k_max (finite <=> inner), wall at 2/3.**

## What the dead clusters taught (recorded, not dropped)

- **B (copy law):** the no-cloning set equals the unreadable band identically -- a relabel of
  `rec_individual == 0`, not a new object. The proposed copy-conservation law J+R is non-conserved
  (`[1,2,1,1,6]`, BAND->GLOBAL 1->6). What survives (monogamy, Landauer) is already-absorbed LOCC / H7
  content.
- **D (arrow / spacetime):** the Aharonov ABL intermediate-recovery statistic is exactly swap-invariant
  (max diff 0 over 2000 fixtures); the only time-asymmetry (T393 causal-escape) reduces to "the record left
  the accessible region," standard accounting. Confirms the high prior: H7 keeps absorbing arrows. The
  time-as-finality arrow will not come cheaply from this route.
- **E (graded interior):** holding the admissible algebra fixed at the standard algebra, recovery is
  identically 0 across every band depth -- **a flat binary; the interior has NO intrinsic grading.** The only
  continuum comes from *widening* the algebra (the F axis). **Consequence for the pullback:** its demanded
  "graded interior" is not an intrinsic property of the band; it is an artifact of algebra choice. This is a
  real negative against a load-bearing earlier assumption.
- **F (band relativity):** the local recovery algebra commutes everywhere *inside* the band; the operator
  you must add to *open* the band is non-commutative, with commutator norm rising as recovery increases. So
  band-exit makes recoveries *more* non-commutative -- the exact opposite of CRDT #15. The band-depends-on-
  algebra intuition (Bohr / Rovelli) is not refuted, but the CRDT commutativity mechanism for it is.

## Next

- **Adopt k_max as the inner-band order parameter** and correct the CHSH-based inner label wherever it
  appears (main note, band-edges model). Wall = 2/3.
- **P1 on the bounded band** can now use k_max (finite <=> inner) rather than CHSH as the entanglement label.
- **E's negative** should be carried back to the pullback discussion: "graded interior" may be unavailable
  intrinsically; if the interior grades only via algebra-widening, the graded-band claim is
  observer-relative, not a state property.
