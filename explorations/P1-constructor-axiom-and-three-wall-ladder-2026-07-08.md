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

## Off-Werner generalization (2026-07-09) -- the ladder is NOT a one-family artifact

Model: `models/finality_ladder_off_werner.py` (exit 0). This attacked the load-bearing question: is the
three-wall nesting real, or a Werner-line artifact?

The two nesting implications are **theorems**, so the ORDER is general by proof:
- **I1** CHSH-violating => NOT 2-shareable (Toner-Verstraete monogamy of Bell correlations);
- **I2** NOT 2-shareable => entangled (separable states are infinitely shareable; and for two qubits
  PPT <=> separable <=> shareable, Horodecki).

Computational confirmation off the Werner line:
- **Calibration passed:** the symmetric-extension (2-shareability) test, implemented by projections onto
  PSD and the affine {symmetric, correct marginal} set, reproduces swing C's Werner wall at **0.665 ~= 2/3**
  -- so the tool is trustworthy off-Werner.
- **Nesting holds statewise:** on 400 random general 2-qubit states, zero CHSH-violating separable states;
  on the off-Werner sample, zero I1 violations (genuine POCS test) and zero I2 violations (theorem-enforced).
- **Both gaps stay non-empty off Werner:** 62 entangled-but-shareable states and 27 un-shareable-but-CHSH-
  local states -- the three walls remain genuinely DISTINCT, not coincident, beyond the Werner family.

One honest wrinkle handled correctly: an initial run flagged 6 "un-shareable separable" states (an I2
violation). Because I2 is a theorem, those were numerical false-negatives of the iterative extension test on
near-separable states, resolved by the 2-qubit PPT=separable short-circuit (PPT => shareable by theorem),
not by loosening a threshold.

**Verdict:** the ladder ORDER (separable < shareable-bound < CHSH-bound) is theorem-backed and confirmed
general; the Werner NUMBERS (1/3, 2/3, 1/sqrt2) are family-specific. The three-wall structure survives the
generalization attack.

## Honest limits / next

- Confirmed for general two-qubit states. Qudit (d>2) is still unchecked -- and note the PPT=separable
  short-circuit used above is two-qubit-specific (fails for d>2), so a qudit test needs a full extension SDP.
- The 2/3 shareability wall is imported from swing C, not re-derived here.
- Natural next step: state each rung's constructor task explicitly (reversible-disentangle, reversible-
  unshare, reversible-de-nonlocalise) and check each flip tracks its own monotone -- turning the ladder into
  three stacked Deutsch-Marletto pairs.
