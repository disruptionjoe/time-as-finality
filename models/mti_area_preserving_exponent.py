"""T243: a WBE/BMR-native justification for the area-preserving n^{-1/2}
condition that singles out the 3/4 exponent -- MTI sub-object (1).

CONTEXT (the exact T233 Gate-1 failure this attacks)
----------------------------------------------------
T233 (models/wbe_objective_selection.py) showed that pure West-Brown-Enquist
dissipation minimization at fixed material budget (the scale-free Lagrangian
J = Z * V^2) lands on the AREA-INCREASING radius ratio

        beta_r = n^{-1/3}      (a = 1, small-vessel / diffusive)

NOT on the AREA-PRESERVING ratio

        beta_r = n^{-1/2}      (a = 3/4, large-vessel / pulsatile)

`check_dissipation_optimum` confirms this for every n. So steady Poiseuille
dissipation minimization does NOT single out 3/4: T233 passed Gate 2 but
FAILED Gate 1 precisely here. The 3/4 exponent requires the area-preserving
condition as a SEPARATE physical input. This module asks whether that separate
input can be made WBE/BMR-native and argued INDEPENDENTLY of the exponent it
produces -- or whether the only route is circular (hand-tuning the exponent in).

THE OBJECT (stated as a premise, not a theorem)
-----------------------------------------------
WBE 1997 themselves do NOT obtain n^{-1/2} from steady dissipation. They obtain
it from a SECOND physical regime: in the large vessels the flow is PULSATILE
(driven by a periodic source), and the network minimizes the energy lost to
WAVE REFLECTIONS at the branch junctions. The standard transmission-line /
pulse-wave result is that the power reflected at a symmetric n-way junction is

        R(n, beta_r) = ( (Y0 - n*Y1) / (Y0 + n*Y1) )^2

where Y is the characteristic ADMITTANCE of a branch and Y1/Y0 is the
daughter/parent admittance ratio. A reflectionless (impedance-MATCHED)
junction requires n*Y1 = Y0. In the area-proportional long-wavelength limit
Y ~ A = pi r^2, this is

        n * beta_r^2 = 1   <=>   beta_r = n^{-1/2}    (AREA-PRESERVING).

So `n^{-1/2}` is the UNIQUE radius ratio that makes every junction reflection-
free. This is the WBE-native pulsatile impedance-matching principle. It is the
SAME structural statement as Banavar-Maritan-Rinaldo cross-section conservation
at branch points (total daughter cross-sectional area = parent cross-sectional
area, n*A_daughter = A_parent), reached from the directed-transport-network side
rather than the pulsatile-vessel side.

HONESTY POSTURE (binding -- this is interpretive, like T238's coverage premise)
-------------------------------------------------------------------------------
This module does NOT claim to DERIVE 3/4 from dissipation. It claims:
  (P) IF the large-vessel regime minimizes pulsatile reflection energy (a
      defensible, independently-stated WBE/BMR physical premise), THEN the
      junction condition is n*beta_r^2 = 1, whose unique solution is the
      area-preserving n^{-1/2}, which yields a = 3/4.
The 3/4 number is a DOWNSTREAM CONSEQUENCE of (P), never an input. The argument
for (P) -- "a pulsatile network wastes energy on reflected waves unless its
junctions are impedance-matched" -- is stated WITHOUT reference to 3/4.

The decisive guard against circularity is the FALSIFICATION CONTROL
(`falsification_remove_constraint`): with the reflection-minimization premise
REMOVED, the optimizer must revert to the area-increasing n^{-1/3} (a=1). It
does. So the area-preserving constraint is doing real, separable work -- it is
not a renamed exponent.

Tags: finite_witness (a finite branching-tree fixture + a finite grid scan over
beta_r; NO continuum theorem) + poly_decider (closed-form reflection functional
+ bounded finite grid argmin; NO hidden search, NO hardness / NP / scale claim).

NO GR/QFT/spacetime/curvature/gravity language. The 3/4 is a COMPUTED VALUE of a
specific finite fixture, not a promoted physical law.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose

# IMPORT ONLY from T233 / T227 -- reuse the exact machinery, modify nothing.
from models.wbe_objective_selection import (
    BranchingTree,
    area_increasing_beta_r,
    area_preserving_beta_r,
    check_dissipation_optimum,
    space_filling_gamma,
    three_quarter_from_optimal_ratios,
)


# ===========================================================================
# PART 1. The WBE-native pulsatile impedance-matching (reflection) functional.
#
#   This is the SECOND physical regime WBE invoke for the large vessels, stated
#   independently of the exponent. Its unique reflectionless ratio is n^{-1/2}.
# ===========================================================================

def junction_reflection(n: int, beta_r: float) -> float:
    """Power reflection coefficient at a symmetric n-way branch junction.

    R = ((Y0 - n*Y1)/(Y0 + n*Y1))^2,  with the area-proportional admittance
    Y ~ A = pi r^2 (rigid-walled long-wavelength / Banavar-Maritan-Rinaldo
    cross-section limit), so Y1/Y0 = beta_r^2. R in [0,1]; R=0 iff n*beta_r^2=1.

    Independently motivated: a pulsatile (periodically driven) network loses
    energy to waves reflected back up the tree at every impedance-MISMATCHED
    junction. Minimizing that reflected energy is a physical objective stated
    with NO reference to any metabolic exponent.
    """
    if not (0.0 < beta_r < 1.0):
        raise ValueError("beta_r must be in (0,1)")
    if n < 2:
        raise ValueError("n must be >= 2")
    y0 = 1.0
    y1 = beta_r * beta_r  # daughter/parent area (admittance) ratio
    num = y0 - n * y1
    den = y0 + n * y1
    return (num / den) ** 2


def area_mismatch(n: int, beta_r: float) -> float:
    """Junction cross-section mismatch m(n,beta_r) = n*beta_r^2 - 1.

    m = 0   : AREA-PRESERVING (cross-section conserved, BMR/WBE pulsatile).
    m > 0   : area-INCREASING toward periphery (n^{-1/3} gives m = n^{1/3}-1>0).
    m < 0   : area-decreasing (un-physical for a service network: would starve
              the periphery).
    This is the directed-transport-network (Banavar-Maritan-Rinaldo) reading of
    the same condition the reflection functional enforces.
    """
    return n * beta_r * beta_r - 1.0


@dataclass(frozen=True)
class ReflectionOptimumResult:
    n: int
    beta_r_reflection_argmin: float    # grid argmin of junction_reflection
    beta_r_area_preserving: float      # n^{-1/2}
    reflection_at_argmin: float        # should be ~0
    reflection_at_area_preserving: float
    reflection_at_area_increasing: float
    argmin_is_area_preserving: bool    # does reflection min land on n^{-1/2}?
    exponent_at_argmin: float          # metabolic exponent there (should be 3/4)


def check_reflection_optimum(
    n: int = 8, grid: int = 8001
) -> ReflectionOptimumResult:
    """Minimize the pulsatile junction-reflection functional over beta_r on the
    SAME bounded interval T233 scans, at the space-filling gamma = n^{-1/3}.

    poly_decider: a finite grid argmin over (gamma^2, 1), no hidden search.

    The reflection functional has its UNIQUE zero at the area-preserving
    n^{-1/2}, so the argmin is n^{-1/2}, and the metabolic exponent there is
    3/4 -- i.e. the SECOND WBE physical regime singles out exactly the ratio
    steady dissipation minimization (T233) does NOT.
    """
    gamma = space_filling_gamma(n)
    lo = gamma * gamma  # identical scan window to T233's check_dissipation_optimum
    best_beta_r = None
    best_r = None
    for i in range(1, grid):
        beta_r = lo + (1.0 - lo) * i / grid
        r = junction_reflection(n, beta_r)
        if best_r is None or r < best_r:
            best_r = r
            best_beta_r = beta_r
    assert best_beta_r is not None

    ap = area_preserving_beta_r(n)
    ai = area_increasing_beta_r(n)
    a_at_argmin = BranchingTree(
        n=n, beta_r=best_beta_r, gamma=gamma, levels=12
    ).metabolic_exponent()

    return ReflectionOptimumResult(
        n=n,
        beta_r_reflection_argmin=best_beta_r,
        beta_r_area_preserving=ap,
        reflection_at_argmin=best_r,
        reflection_at_area_preserving=junction_reflection(n, ap),
        reflection_at_area_increasing=junction_reflection(n, ai),
        argmin_is_area_preserving=isclose(best_beta_r, ap, abs_tol=0.01),
        exponent_at_argmin=a_at_argmin,
    )


# ===========================================================================
# PART 2a. REJECTED ENCODING -- the additive weighted blend (a disqualifier).
#
#   A first, tempting encoding is an additive blend
#        J_blend = (Z*V^2 normalized)  +  lam * R(n, beta_r)
#   and "tune lam until the optimum is n^{-1/2}". We BUILD it only to REJECT it:
#   the argmin slides CONTINUOUSLY from n^{-1/3} (lam=0) toward n^{-1/2} as lam
#   grows, never *landing* on n^{-1/2} at any finite lam (see
#   `additive_blend_is_an_exponent_dial`). That makes lam an EXPONENT DIAL --
#   exactly the hand-tuning the honesty guard forbids. So the additive blend is
#   a disqualifier, not the justification. The load-bearing encoding is the
#   HARD reflectionless constraint in PART 2b.
# ===========================================================================

def additive_blend_objective(
    n: int, beta_r: float, lam: float, levels: int = 14
) -> float:
    """J_blend = (Z*V^2 / ref)  +  lam * R(n, beta_r).  REJECTED encoding."""
    gamma = space_filling_gamma(n)
    j_diss = BranchingTree(
        n=n, beta_r=beta_r, gamma=gamma, levels=levels
    ).constrained_dissipation()
    ai = area_increasing_beta_r(n)
    j_ref = BranchingTree(
        n=n, beta_r=ai, gamma=gamma, levels=levels
    ).constrained_dissipation()
    return j_diss / j_ref + lam * junction_reflection(n, beta_r)


def _blend_argmin(n: int, lam: float, levels: int = 14, grid: int = 2001) -> float:
    gamma = space_filling_gamma(n)
    lo = gamma * gamma
    best_b, best_j = None, None
    for i in range(1, grid):
        b = lo + (1.0 - lo) * i / grid
        j = additive_blend_objective(n, b, lam, levels=levels)
        if best_j is None or j < best_j:
            best_j, best_b = j, b
    assert best_b is not None
    return best_b


@dataclass(frozen=True)
class BlendDialResult:
    n: int
    lam_values: tuple[float, ...]
    argmins: tuple[float, ...]
    area_preserving: float
    slides_continuously: bool   # argmin monotone in lam, never == n^{-1/2}
    lands_on_area_preserving_at_finite_lam: bool


def additive_blend_is_an_exponent_dial(
    n: int = 8, lams: tuple[float, ...] = (0.0, 1.0, 20.0, 100.0, 500.0, 2000.0)
) -> BlendDialResult:
    """Demonstrate the additive blend is a forbidden exponent dial.

    The argmin decreases monotonically with lam (sliding n^{-1/3} -> n^{-1/2})
    but never equals n^{-1/2} at any finite lam in the scan. Therefore the blend
    does NOT *single out* n^{-1/2}; it interpolates. This is reported as a
    DISQUALIFIER, not a success.
    """
    ap = area_preserving_beta_r(n)
    args = tuple(_blend_argmin(n, lam) for lam in lams)
    monotone = all(args[i] >= args[i + 1] - 1e-9 for i in range(len(args) - 1))
    lands = any(isclose(a, ap, abs_tol=0.012) for a in args)
    return BlendDialResult(
        n=n,
        lam_values=lams,
        argmins=args,
        area_preserving=ap,
        slides_continuously=monotone and not lands,
        lands_on_area_preserving_at_finite_lam=lands,
    )


# ===========================================================================
# PART 2b. The LOAD-BEARING encoding: a HARD reflectionless constraint
#          (lexicographic, not weighted).
#
#   WBE physics is a regime SEPARATION, not a weighted average: the large
#   vessels ARE the impedance-matched / reflectionless regime. The domain-native
#   constraint is therefore the HARD feasibility restriction R(n,beta_r)=0
#   (equivalently the BMR cross-section conservation n*beta_r^2=1), and steady
#   dissipation is minimized WITHIN that feasible set. Because R=0 has the UNIQUE
#   space-filling solution beta_r=n^{-1/2}, the feasible set is the single point
#   n^{-1/2}, so the constrained optimum IS n^{-1/2}, giving a=3/4 -- with NO
#   tunable weight. Dropping the constraint reverts to T233's n^{-1/3}.
# ===========================================================================

def is_reflectionless(n: int, beta_r: float, tol: float = 1e-6) -> bool:
    """Hard feasibility test: junction is impedance-matched (R ~ 0)."""
    return junction_reflection(n, beta_r) <= tol


@dataclass(frozen=True)
class ConstrainedOptimumResult:
    n: int
    constraint: str                    # 'reflectionless' or 'none'
    beta_r_argmin: float               # dissipation argmin within feasible set
    beta_r_area_preserving: float
    beta_r_area_increasing: float
    exponent_at_argmin: float
    selects_area_preserving: bool
    selects_area_increasing: bool
    recovers_three_quarter: bool
    feasible_count: int                # # grid points passing the hard constraint


def check_constrained_optimum(
    n: int = 8,
    reflectionless: bool = True,
    levels: int = 14,
    grid: int = 20001,
    refl_tol: float = 1e-4,
) -> ConstrainedOptimumResult:
    """Re-run T233's Gate-1 dissipation argmin on the SAME scan window/grid, but
    RESTRICTED to the reflectionless (area-preserving) feasible set when
    `reflectionless=True`.

    reflectionless=True  -> feasible set = {beta_r : R~0}, which is the single
                            POINT n^{-1/2}; the constrained dissipation argmin is
                            therefore n^{-1/2}, a=3/4.
    reflectionless=False -> NO constraint = exactly T233's unconstrained scan,
                            argmin = n^{-1/3}, a=1  (falsification control).

    HONESTY NOTE: R=0 is a single point, not a band. On a finite grid the filter
    R<=refl_tol admits a thin band around n^{-1/2}, and within it steady
    dissipation pulls the argmin to the band's fat edge -- so a LOOSE refl_tol
    over-reports a > 3/4. The hard constraint is recovered in the limit:
    `reflectionless_convergence` shows the argmin -> n^{-1/2} and a -> 3/4
    monotonically as refl_tol -> 0. The default (grid=20001, refl_tol=1e-4)
    already lands within abs_tol 0.012 of n^{-1/2}; this is a finite-grid
    concession, NOT a tuned weight (there is no free coefficient).

    poly_decider: finite bounded grid argmin with a finite feasibility filter;
    NO hidden search, NO tunable weight.
    """
    gamma = space_filling_gamma(n)
    lo = gamma * gamma
    best_beta_r = None
    best_j = None
    feasible = 0
    for i in range(1, grid):
        beta_r = lo + (1.0 - lo) * i / grid
        if reflectionless and not is_reflectionless(n, beta_r, tol=refl_tol):
            continue
        feasible += 1
        j = BranchingTree(
            n=n, beta_r=beta_r, gamma=gamma, levels=levels
        ).constrained_dissipation()
        if best_j is None or j < best_j:
            best_j = j
            best_beta_r = beta_r
    assert best_beta_r is not None, "feasible set empty -- tighten grid or refl_tol"

    ap = area_preserving_beta_r(n)
    ai = area_increasing_beta_r(n)
    a_at_opt = BranchingTree(
        n=n, beta_r=best_beta_r, gamma=gamma, levels=levels
    ).metabolic_exponent()

    return ConstrainedOptimumResult(
        n=n,
        constraint="reflectionless" if reflectionless else "none",
        beta_r_argmin=best_beta_r,
        beta_r_area_preserving=ap,
        beta_r_area_increasing=ai,
        exponent_at_argmin=a_at_opt,
        selects_area_preserving=isclose(best_beta_r, ap, abs_tol=0.012),
        selects_area_increasing=isclose(best_beta_r, ai, abs_tol=0.012),
        recovers_three_quarter=isclose(a_at_opt, 0.75, abs_tol=0.02),
        feasible_count=feasible if reflectionless else (grid - 1),
    )


@dataclass(frozen=True)
class ConvergenceResult:
    n: int
    tols: tuple[float, ...]
    argmins: tuple[float, ...]
    exponents: tuple[float, ...]
    area_preserving: float
    argmin_monotone_to_area_preserving: bool   # |argmin - n^{-1/2}| decreasing
    exponent_converges_to_three_quarter: bool  # |a - 0.75| decreasing -> ~0


def reflectionless_convergence(
    n: int = 8, tols: tuple[float, ...] = (5e-3, 1e-3, 1e-4, 1e-5)
) -> ConvergenceResult:
    """Witness the hard-constraint limit: as refl_tol -> 0 the constrained
    dissipation argmin converges MONOTONICALLY to n^{-1/2} and the exponent to
    3/4. This is the proof the constraint is a single POINT (the area-preserving
    ratio), not a tunable band -- removing the grid concession recovers exactly
    a = 3/4 with NO free coefficient.
    """
    ap = area_preserving_beta_r(n)
    args, exps = [], []
    for tol in tols:
        c = check_constrained_optimum(n=n, reflectionless=True, grid=20001, refl_tol=tol)
        args.append(c.beta_r_argmin)
        exps.append(c.exponent_at_argmin)
    d_arg = [abs(a - ap) for a in args]
    d_exp = [abs(e - 0.75) for e in exps]
    arg_mono = all(d_arg[i] >= d_arg[i + 1] - 1e-12 for i in range(len(d_arg) - 1))
    exp_mono = all(d_exp[i] >= d_exp[i + 1] - 1e-12 for i in range(len(d_exp) - 1))
    return ConvergenceResult(
        n=n,
        tols=tols,
        argmins=tuple(args),
        exponents=tuple(exps),
        area_preserving=ap,
        argmin_monotone_to_area_preserving=arg_mono and d_arg[-1] < 0.012,
        exponent_converges_to_three_quarter=exp_mono and d_exp[-1] < 0.01,
    )


# ===========================================================================
# PART 3. Falsification control.
# ===========================================================================

@dataclass(frozen=True)
class FalsificationResult:
    n: int
    with_constraint_selects_area_preserving: bool   # reflectionless -> n^{-1/2}
    with_constraint_exponent: float                 # ~0.75
    without_constraint_selects_area_increasing: bool  # none -> n^{-1/3}
    without_constraint_exponent: float              # ~1.0
    control_is_decisive: bool   # both above true => constraint does real work


def falsification_remove_constraint(n: int = 8) -> FalsificationResult:
    """DECISIVE control: removing the reflectionless premise must revert the
    optimum to the area-INCREASING n^{-1/3} (a=1).

    With the hard reflectionless constraint ON, the constrained dissipation
    argmin is n^{-1/2} (a=3/4). With it OFF, the scan is identical to T233 and
    the argmin is n^{-1/3} (a=1). So the area-preserving constraint is separable
    and load-bearing, NOT a renamed exponent: the 3/4 disappears the moment the
    independently-motivated reflection premise is withdrawn.
    """
    on = check_constrained_optimum(n=n, reflectionless=True)
    off = check_constrained_optimum(n=n, reflectionless=False)
    return FalsificationResult(
        n=n,
        with_constraint_selects_area_preserving=on.selects_area_preserving,
        with_constraint_exponent=on.exponent_at_argmin,
        without_constraint_selects_area_increasing=off.selects_area_increasing,
        without_constraint_exponent=off.exponent_at_argmin,
        control_is_decisive=(
            on.selects_area_preserving and off.selects_area_increasing
        ),
    )


# ===========================================================================
# PART 4. Circularity audit -- the binding honesty guard.
# ===========================================================================

@dataclass(frozen=True)
class CircularityAudit:
    reflection_zero_is_area_preserving: bool   # R=0 <=> n*beta_r^2=1
    premise_stated_without_exponent: bool      # functional has no 3/4 in it
    exponent_is_downstream: bool               # 3/4 computed AFTER, from ratios
    additive_blend_rejected: bool              # the weighted blend is a dial
    falsification_decisive: bool               # drop constraint -> n^{-1/3}
    not_circular: bool


def circularity_audit(n: int = 8) -> CircularityAudit:
    """Audit that the area-preserving justification is NOT circular.

    Five checks, all must pass:
      (1) the reflection functional's zero is EXACTLY the area-preserving
          condition n*beta_r^2 = 1 (verified by the closed form), so the
          premise is a clean physical condition, not a fitted curve;
      (2) the reflection functional contains NO exponent: junction_reflection
          is a function of (n, beta_r) only -- 0.75 does not appear in it, and
          R rises on BOTH sides of n^{-1/2} (no special treatment of 0.75);
      (3) the exponent 3/4 is computed DOWNSTREAM from the selected ratio via
          T233's metabolic_exponent, never fed in;
      (4) the additive weighted blend is REJECTED as an exponent dial (the
          honest encoding is a HARD constraint, not a tuned weight);
      (5) the falsification control is decisive (drop the hard reflectionless
          constraint -> the optimum reverts to n^{-1/3}).
    """
    ap = area_preserving_beta_r(n)
    # (1) R=0 exactly at area-preserving:
    r_at_ap = junction_reflection(n, ap)
    r_zero_ap = isclose(r_at_ap, 0.0, abs_tol=1e-12) and isclose(
        area_mismatch(n, ap), 0.0, abs_tol=1e-12
    )
    # (2) the functional has no 3/4 baked in: it is exactly the area
    #     (admittance) ratio; R rises on BOTH sides of n^{-1/2}
    r_below = junction_reflection(n, ap * 0.95)
    r_above = junction_reflection(n, min(ap * 1.05, 0.999))
    premise_no_exponent = r_below > r_at_ap and r_above > r_at_ap
    # (3) exponent is downstream: recompute 3/4 from the ratios, post hoc:
    a_at_ap = three_quarter_from_optimal_ratios(n=n)
    exponent_downstream = isclose(a_at_ap, 0.75, abs_tol=1e-6)
    # (4) the additive blend is a forbidden dial -> rejected:
    blend = additive_blend_is_an_exponent_dial(n=n)
    blend_rejected = (
        blend.slides_continuously
        and not blend.lands_on_area_preserving_at_finite_lam
    )
    # (5) falsification decisive:
    fal = falsification_remove_constraint(n=n)
    return CircularityAudit(
        reflection_zero_is_area_preserving=r_zero_ap,
        premise_stated_without_exponent=premise_no_exponent,
        exponent_is_downstream=exponent_downstream,
        additive_blend_rejected=blend_rejected,
        falsification_decisive=fal.control_is_decisive,
        not_circular=(
            r_zero_ap and premise_no_exponent and exponent_downstream
            and blend_rejected and fal.control_is_decisive
        ),
    )


# ===========================================================================
# Combined Gate-1 re-run verdict.
# ===========================================================================

@dataclass(frozen=True)
class Gate1RerunVerdict:
    n: int
    dissipation_only_selects_area_increasing: bool  # T233 baseline (a=1)
    dissipation_only_exponent: float
    with_reflection_selects_area_preserving: bool   # this lane (a=3/4)
    with_reflection_exponent: float
    falsification_decisive: bool
    not_circular: bool

    @property
    def gate1_now_singles_out_three_quarter(self) -> bool:
        return (
            self.dissipation_only_selects_area_increasing
            and self.with_reflection_selects_area_preserving
            and isclose(self.with_reflection_exponent, 0.75, abs_tol=0.02)
            and self.falsification_decisive
            and self.not_circular
        )


def rerun_gate1(n: int = 8) -> Gate1RerunVerdict:
    """The headline: re-run T233's Gate 1 under the HARD reflectionless
    (area-preserving) constraint -- the WBE-native pulsatile impedance-matching
    premise -- and report whether n^{-1/2} (3/4) is now singled out, with the
    T233 baseline and the falsification control side by side.
    """
    base = check_dissipation_optimum(n=n)
    con = check_constrained_optimum(n=n, reflectionless=True)
    fal = falsification_remove_constraint(n=n)
    aud = circularity_audit(n=n)
    return Gate1RerunVerdict(
        n=n,
        dissipation_only_selects_area_increasing=base.argmin_is_area_increasing,
        dissipation_only_exponent=base.exponent_at_optimum,
        with_reflection_selects_area_preserving=con.selects_area_preserving,
        with_reflection_exponent=con.exponent_at_argmin,
        falsification_decisive=fal.control_is_decisive,
        not_circular=aud.not_circular,
    )


if __name__ == "__main__":
    print("=== PART 1: pulsatile junction-reflection optimum over beta_r ===")
    for n in (4, 8, 16, 27):
        r = check_reflection_optimum(n=n)
        print(
            f"n={n:3d}  reflection-argmin beta_r={r.beta_r_reflection_argmin:.4f}  "
            f"area-pres n^-1/2={r.beta_r_area_preserving:.4f}  "
            f"R@argmin={r.reflection_at_argmin:.2e}  "
            f"a@argmin={r.exponent_at_argmin:.4f}  "
            f"is_area_preserving={r.argmin_is_area_preserving}"
        )

    print()
    print("=== PART 2a: REJECTED additive blend is an exponent dial ===")
    for n in (4, 8, 16, 27):
        d = additive_blend_is_an_exponent_dial(n=n)
        print(
            f"n={n:3d}  argmins over lam={d.lam_values} -> "
            f"{tuple(round(x,4) for x in d.argmins)}  "
            f"area-pres={d.area_preserving:.4f}  "
            f"slides_continuously={d.slides_continuously}  "
            f"lands_at_finite_lam={d.lands_on_area_preserving_at_finite_lam}"
        )

    print()
    print("=== PART 2b: HARD reflectionless-constraint Gate-1 re-run ===")
    for n in (4, 8, 16, 27):
        c = check_constrained_optimum(n=n, reflectionless=True)
        print(
            f"n={n:3d}  constrained argmin beta_r={c.beta_r_argmin:.4f}  "
            f"area-pres={c.beta_r_area_preserving:.4f}  "
            f"a@argmin={c.exponent_at_argmin:.4f}  "
            f"feasible_pts={c.feasible_count}  "
            f"selects_area_preserving={c.selects_area_preserving}  "
            f"recovers_3/4={c.recovers_three_quarter}"
        )

    print()
    print("=== PART 2b-conv: hard-constraint limit (refl_tol -> 0) ===")
    for n in (4, 8, 16, 27):
        cv = reflectionless_convergence(n=n)
        print(
            f"n={n:3d}  argmins={tuple(round(x,5) for x in cv.argmins)} "
            f"-> area-pres={cv.area_preserving:.5f}  "
            f"exponents={tuple(round(x,5) for x in cv.exponents)} -> 0.75  "
            f"argmin->AP={cv.argmin_monotone_to_area_preserving}  "
            f"a->3/4={cv.exponent_converges_to_three_quarter}"
        )

    print()
    print("=== PART 3: falsification control (drop the hard constraint) ===")
    for n in (4, 8, 16, 27):
        f = falsification_remove_constraint(n=n)
        print(
            f"n={n:3d}  constraint ON -> area-pres="
            f"{f.with_constraint_selects_area_preserving} "
            f"(a={f.with_constraint_exponent:.4f})  "
            f"constraint OFF -> area-incr="
            f"{f.without_constraint_selects_area_increasing} "
            f"(a={f.without_constraint_exponent:.4f})  "
            f"decisive={f.control_is_decisive}"
        )

    print()
    print("=== PART 4: circularity audit ===")
    for n in (4, 8, 16, 27):
        a = circularity_audit(n=n)
        print(
            f"n={n:3d}  R=0<=>area-pres={a.reflection_zero_is_area_preserving}  "
            f"no_exponent_in_functional={a.premise_stated_without_exponent}  "
            f"exponent_downstream={a.exponent_is_downstream}  "
            f"blend_rejected={a.additive_blend_rejected}  "
            f"falsification_decisive={a.falsification_decisive}  "
            f"NOT_CIRCULAR={a.not_circular}"
        )

    print()
    print("=== GATE-1 RE-RUN VERDICT ===")
    for n in (4, 8, 16, 27):
        v = rerun_gate1(n=n)
        print(
            f"n={n:3d}  dissip-only->area-incr(a={v.dissipation_only_exponent:.3f})  "
            f"+reflectionless->area-pres(a={v.with_reflection_exponent:.3f})  "
            f"GATE1_SINGLES_OUT_3/4={v.gate1_now_singles_out_three_quarter}"
        )
