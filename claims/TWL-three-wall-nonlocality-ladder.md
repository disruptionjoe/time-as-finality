# TWL: Three-Wall Nonlocality Ladder

## Claim

On the isotropic/Werner family of bipartite qudit states there are three distinct
nested thresholds -- **entanglement < 2-shareability < CGLMP nonlocality** -- each
with its own monotone, and this nested-ladder structure reconstructs identically
across d = 2, 3, 4 with both interior gaps populated on and off the isotropic line.
The three walls and their nesting are **established quantum-information results**;
what is earned here is a single executable object that reconstructs them with one
calibrated toolchain, verifies the gaps and the statewise implication
(CGLMP-violating => un-shareable) on genuine violators, and corrected a latent
operator bug in the process.

## Class

formal_scaffold (executable reconstruction of known QI; anchors the monogamy <->
secret-sharing strut).

## Status

active (verified scaffold; not a standalone novel claim). Canon-Index tier:
**finite-witness supported**.

## Current Strongest Form

```text
wall 1  entanglement      F = 1/d          monotone: negativity (NPT),
                                            upgraded to CCNR for bound entanglement
wall 2  2-shareability    F = (d+1)/(2d)    monotone: symmetric-extension SDP;
                                            closed form = Johnson & Viola (2013)
wall 3  CGLMP nonlocality F = F_CGLMP       monotone: fixed optimal CGLMP-d witness;
                                            threshold matches literature v_crit(d)
ordered 1/d < (d+1)/2d < F_CGLMP, both gaps non-empty, verified d = 2,3,4.
```

## Earned Content

- **d=3 (qutrit) ladder** (`explorations/qudit-three-wall-ladder-result-2026-07-09.md`):
  three ordered distinct walls (0.333 < 0.670 < 0.730); F_CGLMP maps to visibility
  0.696, matching the known CGLMP-3 noise threshold ~0.6961. Statewise I1
  (CGLMP-violating => un-shareable) holds with 0 violations on 49 genuine
  violators; both gaps populated off the isotropic line.
- **d=4 extension + bug-catch (T515).** The ladder extends to d=4
  (0.25 < 0.625 < 0.710). Building CGLMP-4 surfaced a latent sign bug in the
  `cglmp` operator (the k>=1 term, never fired at d<=3); the corrected operator
  matches standard CGLMP maxent values EXACTLY at d = 2,3,4,5. The d=3 result is
  unaffected (it only used k=0). This bug-catch is the one genuinely new datum.
- **Shareability closed form (T516).** F_share(d) = (d+1)/(2d) (Johnson & Viola PRA
  88 032323 (2013)); an independent symmetric-extension POCS brackets and contains
  the closed form at d = 2,3,4. F_share(3) = 2/3 discharges the earlier POCS value.
- **Bound-entanglement upgrade (T514).** A CCNR/realignment witness upgrades the
  outer wall from "NPT-entangled" to "entangled," catching the Tiles UPB
  bound-entangled state (negativity ~0, CCNR 1.087). On the isotropic line
  PPT<=>sep, so the ladder is unchanged there; the upgrade adds off-line detection.

## Known Neighbors (honesty scope -- this is reconstruction, not new physics)

- Monogamy of entanglement / nonlocality; "2-shareable => admits a local model =>
  no Bell violation" is a known theorem.
- Johnson & Viola (2013) supply the isotropic symmetric-extendibility closed form.
- CGLMP inequality and its noise-threshold visibilities are established.
- CCNR/realignment criterion and the symmetric-extension (Doherty-Parrilo-
  Spedalieri) SDP hierarchy are standard tools.

The nesting entanglement < shareability < nonlocality is therefore **known
structure**; the contribution is executable cross-d reconstruction with one
calibrated toolchain, non-vacuous gap/implication verification on genuine
violators, and the CGLMP-d operator correction.

## Honest Limits

- Shareability via POCS is a feasibility test, not a dual-witness certificate; the
  closed form is the certified value.
- The CGLMP wall uses a fixed-measurement witness: sufficient, not necessary
  (certifies violation for aligned states, can miss rotated ones). CGLMP
  non-violation here is not a certificate of locality.
- "Entangled" defaults to NPT/negativity on the isotropic line; bound entanglement
  is caught only by the CCNR upgrade and is measure-~0 in random sampling.
- Verified d = 2,3,4; higher d unchecked (symmetry-reduced calibration would make
  it cheap).

## Relation To Finality (what this does and does not support)

- **Supports:** the monogamy <-> quantum secret sharing strut (the one bridge that
  survived TaF's stress tests; arXiv 2605.26866) and the A1 distributed-systems
  finality analogy, by giving them a verified, cross-d nonlocality/shareability
  scaffold to build on.
- **Does NOT support:** any finality-core claim (C1/D1/H7), novel physics, a novel
  theorem, or Q1 reinstatement. Q1 stays demoted. TWL asserts no observer-relative
  finality content; it is neighbor structure made executable.

## Test Ledger

P1 two-qubit off-Werner generality -> d=3 qutrit result -> T514 (CCNR) -> T515
(d=4 + operator correction) -> T516 (shareability closed form). Adjacent DS-bridge
prospecting (T517 SHUT, T518/T519 structural-only) is tracked separately in the
lane-status ledger and does not feed TWL.

## No-Movement Boundary

Registering TWL at finite-witness supported moves no other claim, no
COMPLEXITY-LEDGER theorem, no ROADMAP target, no North Star, no public posture, and
nothing external or cross-repo. It is an honest tier placement of already-run,
already-green work.
