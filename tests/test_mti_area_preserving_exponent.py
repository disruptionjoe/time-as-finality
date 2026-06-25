"""T243 tests: WBE-native area-preserving justification of the 3/4 exponent.

Real checks (no placeholders) of the claim that a domain-native pulsatile
impedance-matching (reflectionless / area-preserving) premise singles out the
area-preserving n^{-1/2} ratio (giving a=3/4), with a decisive falsification
control and a circularity audit. All checks are finite_witness + poly_decider.
"""

from math import isclose

import pytest

from models.mti_area_preserving_exponent import (
    additive_blend_is_an_exponent_dial,
    area_mismatch,
    check_constrained_optimum,
    check_dissipation_optimum,
    check_reflection_optimum,
    circularity_audit,
    falsification_remove_constraint,
    is_reflectionless,
    junction_reflection,
    reflectionless_convergence,
    rerun_gate1,
)
from models.wbe_objective_selection import (
    area_increasing_beta_r,
    area_preserving_beta_r,
)

NS = (4, 8, 16, 27)


# --- the reflection functional itself ---------------------------------------

def test_reflection_zero_exactly_at_area_preserving():
    """R = 0 iff n*beta_r^2 = 1, i.e. exactly at the area-preserving n^{-1/2}."""
    for n in NS:
        ap = area_preserving_beta_r(n)
        assert isclose(junction_reflection(n, ap), 0.0, abs_tol=1e-12)
        assert isclose(area_mismatch(n, ap), 0.0, abs_tol=1e-12)


def test_reflection_positive_at_area_increasing():
    """The area-increasing n^{-1/3} (T233's dissipation optimum) is NOT
    reflectionless -- it carries strictly positive reflected power."""
    for n in NS:
        ai = area_increasing_beta_r(n)
        assert junction_reflection(n, ai) > 1e-3


def test_reflection_rises_on_both_sides_of_area_preserving():
    """No special treatment of 0.75: R is a clean convex-like well around
    n^{-1/2}, rising on both sides (the functional has no exponent baked in)."""
    for n in NS:
        ap = area_preserving_beta_r(n)
        r0 = junction_reflection(n, ap)
        assert junction_reflection(n, ap * 0.95) > r0
        assert junction_reflection(n, min(ap * 1.05, 0.999)) > r0


def test_is_reflectionless_predicate():
    for n in NS:
        assert is_reflectionless(n, area_preserving_beta_r(n))
        assert not is_reflectionless(n, area_increasing_beta_r(n))


# --- Part 1: reflection optimum singles out n^{-1/2} (a=3/4) -----------------

def test_reflection_optimum_is_area_preserving_and_three_quarter():
    for n in NS:
        r = check_reflection_optimum(n=n)
        assert r.argmin_is_area_preserving
        assert isclose(r.reflection_at_argmin, 0.0, abs_tol=1e-6)
        assert isclose(r.exponent_at_argmin, 0.75, abs_tol=0.01)


# --- T233 baseline reproduced: dissipation alone gives n^{-1/3} (a=1) --------

def test_t233_baseline_unchanged_dissipation_gives_area_increasing():
    """We must NOT have perturbed T233's result: pure constrained dissipation
    still lands on the area-INCREASING n^{-1/3} with a=1."""
    for n in NS:
        base = check_dissipation_optimum(n=n)
        assert base.argmin_is_area_increasing
        assert not base.recovers_three_quarter
        assert isclose(base.exponent_at_optimum, 1.0, abs_tol=0.01)


# --- Part 2a: the additive blend is a forbidden exponent dial (rejected) -----

def test_additive_blend_is_rejected_as_exponent_dial():
    """The weighted blend slides continuously and never lands on n^{-1/2} at any
    finite lam -> it is an exponent dial -> rejected. This guards against
    hand-tuning the exponent into existence via a tunable weight."""
    for n in NS:
        d = additive_blend_is_an_exponent_dial(n=n)
        assert d.slides_continuously
        assert not d.lands_on_area_preserving_at_finite_lam


# --- Part 2b: hard reflectionless constraint singles out n^{-1/2} ------------

def test_hard_constraint_selects_area_preserving():
    for n in NS:
        c = check_constrained_optimum(n=n, reflectionless=True)
        assert c.selects_area_preserving
        assert c.recovers_three_quarter
        assert not c.selects_area_increasing


def test_hard_constraint_converges_to_three_quarter_as_tol_shrinks():
    """The reflectionless set is a single POINT; on a finite grid a loose
    tolerance over-reports a>3/4, but argmin -> n^{-1/2} and a -> 3/4
    MONOTONICALLY as refl_tol -> 0. This is the proof there is no free
    coefficient -- the band is a grid concession, not a tuned weight."""
    for n in NS:
        cv = reflectionless_convergence(n=n)
        assert cv.argmin_monotone_to_area_preserving
        assert cv.exponent_converges_to_three_quarter
        # tightest tolerance is within 0.01 of 3/4
        assert isclose(cv.exponents[-1], 0.75, abs_tol=0.01)
        # and strictly closer than the loosest tolerance (real convergence)
        assert abs(cv.exponents[-1] - 0.75) < abs(cv.exponents[0] - 0.75)


# --- Part 3: falsification control is decisive -------------------------------

def test_falsification_control_is_decisive():
    """Removing the reflectionless premise reverts the optimum to the
    area-INCREASING n^{-1/3} (a=1). So the constraint does real, separable
    work; the 3/4 is not smuggled in."""
    for n in NS:
        f = falsification_remove_constraint(n=n)
        assert f.with_constraint_selects_area_preserving
        assert f.without_constraint_selects_area_increasing
        assert f.control_is_decisive
        assert isclose(f.with_constraint_exponent, 0.75, abs_tol=0.02)
        assert isclose(f.without_constraint_exponent, 1.0, abs_tol=0.02)


# --- Part 4: circularity audit ----------------------------------------------

def test_circularity_audit_all_guards_pass():
    for n in NS:
        a = circularity_audit(n=n)
        assert a.reflection_zero_is_area_preserving
        assert a.premise_stated_without_exponent
        assert a.exponent_is_downstream
        assert a.additive_blend_rejected
        assert a.falsification_decisive
        assert a.not_circular


# --- the headline Gate-1 re-run verdict --------------------------------------

def test_gate1_rerun_singles_out_three_quarter():
    for n in NS:
        v = rerun_gate1(n=n)
        assert v.dissipation_only_selects_area_increasing
        assert v.with_reflection_selects_area_preserving
        assert v.falsification_decisive
        assert v.not_circular
        assert v.gate1_now_singles_out_three_quarter


# --- guards / domain sanity --------------------------------------------------

def test_reflection_input_validation():
    with pytest.raises(ValueError):
        junction_reflection(1, 0.5)   # n < 2
    with pytest.raises(ValueError):
        junction_reflection(8, 1.5)   # beta_r out of (0,1)
    with pytest.raises(ValueError):
        junction_reflection(8, 0.0)


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-q"]))
