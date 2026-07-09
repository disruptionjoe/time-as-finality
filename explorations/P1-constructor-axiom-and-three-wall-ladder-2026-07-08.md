# P1: the constructor axiom, and the between-band as a three-wall ladder

2026-07-08. Runs starter-swing P1 to completion on the shareability-bounded band. Model:
`models/finality_constructor_axiom_band.py` (exit 0, all checks pass). Carrier: the 2-qubit singlet Werner
family `rho_p = p |psi-><psi-| + (1-p) I/4`.

## The axiom, stated and settled

**Task T_reversible:** by a LOCAL UNITARY (reversible, deterministic, no measurement), map the shared state
to a PRODUCT state. Local unitaries preserve every entanglement monotone and a product target has negativity
0, so:

> T_reversible is **POSSIBLE** (severally) iff the state is separable, **IMPOSSIBLE** iff entangled.

That is the clean Deutsch-Marletto possible/impossible pair the swing asked for. Both of the swing's required
fixes are confirmed by the run:

- **(a) The reversible restriction is load-bearing.** An entangled state has negativity 0.425; applying an
  *irreversible* local op (Z-dephasing on B) drives negativity to exactly 0 -- so "remove the correlation"
  becomes possible once you allow measurement. The loose axiom is therefore false; the impossibility holds
  *only* for the reversible+deterministic+state-preserving task.
- **(b) QRT supplies the grading.** The constructor verdict is binary, but negativity (a QRT monotone) is
  continuous -- 65 distinct monotone-increasing values across the entangled region. Constructor theory gives
  the wall; QRT grades the interior.

**The flip coincides exactly with the QRT monotone crossing 0** at `p = 1/3` (measured flip at p=0.34 on a
0.01 grid). So the constructor task reproduces the entanglement boundary rather than contradicting it.

## The main finding: the band is a three-wall LADDER

The decisive placement result. On one Werner family, three distinct walls appear, each with its own
monotone -- and the constructor task pins the **outermost** one:

| wall | p | monotone | source |
|---|---|---|---|
| **entanglement** | **1/3** | **negativity** | **constructor task T_reversible (P1)** |
| shareability / monogamy | 2/3 | k_max (shareability number) | swing C |
| CHSH | 1/sqrt2 ~ 0.707 | CHSH_max | (demoted inner label) |

At `p = 0.50` the state is **entangled (constructor IMPOSSIBLE) yet 2-shareable and CHSH-local**
(CHSH_max = 1.414). That "entangled-but-shareable" window is exactly the gap between wall 1 and wall 2, and
it proves the three walls are genuinely distinct, not one wall relabelled.

So the "between-band" is not a single object with one boundary. It is a **nested ladder**:

- **outermost (p > 1/3):** entangled -- not reversibly disentanglable by any local unitary. Constructor
  wall, graded by negativity.
- **middle (p > 2/3):** monogamous -- not 2-shareable. Swing C's k_max wall.
- **innermost (p > 1/sqrt2):** CHSH-violating.

Each rung is a strictly stronger form of "final for the pair, inaccessible severally," with its own order
parameter. P1 supplies the outermost rung and its grading; swing C supplies the middle; CHSH (now demoted
from "the" inner label) marks only the innermost.

## How this integrates the session

- The nested-band finding (entanglement inside a broader unreadability band) sits ON TOP of this: the
  admissible-unreadability wall (rec_individual = 0) is the *outer* wall; within it, this ladder refines the
  entangled sub-region into three rungs.
- Swing C's correction (monogamy sharper than CHSH, wall 2/3) is rung 2; P1 adds rung 1 below it.
- The band is therefore characterised by a *stack of monotones*, not one -- consistent with T17's finding
  that finality is a multi-dimensional vector, not a scalar. The ladder is the concrete quantum instance of
  that.

## Honest limits / next

- The ladder is shown on the Werner family only. Whether the three walls stay ordered and distinct off the
  Werner line (general 2-qubit, then qudit) is unchecked; the ordering 1/3 < 2/3 < 1/sqrt2 is Werner-specific
  in its numbers though the *nesting* (separable < shareable-bound < CHSH-bound) is general.
- The 2/3 shareability wall is imported from swing C, not re-derived here.
- Natural next step: state each rung's constructor task explicitly (reversible-disentangle, reversible-
  unshare, reversible-de-nonlocalise) and check each flip tracks its own monotone -- turning the ladder into
  three stacked Deutsch-Marletto pairs.
