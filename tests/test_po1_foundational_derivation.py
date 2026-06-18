"""Tests for T33: PO1 foundational derivation."""

from __future__ import annotations

from models.po1_foundational_derivation import (
    T33Result,
    _ac5_naming_independence_counterexample,
    _ipt_derivation_attempts,
    _ipt_insufficient_for_ac6_counterexample,
    _rmt_derivation_attempts,
    _rmt_insufficient_for_ac3_counterexample,
    _t31_resource_monotones,
    all_derivation_attempts,
    classify_obstruction,
    compute_projection_action,
    compute_resource_monotone,
    extract_invariant_profile,
    extract_resource_state,
    run_t33_analysis,
    t33_result_to_dict,
)


# Module-level cache so run_t33_analysis() runs once per test session.
_RESULT: T33Result | None = None


def _r() -> T33Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t33_analysis()
    return _RESULT


# ---------------------------------------------------------------------------
# Resource extraction
# ---------------------------------------------------------------------------


class TestResourceExtraction:

    def test_four_positive_cases_extracted(self):
        assert len(_t31_resource_monotones()) == 4

    def test_all_positive_cases_are_strictly_decreasing(self):
        for rm in _t31_resource_monotones():
            assert rm.is_strictly_decreasing, f"Expected strict decrease for {rm.name}"

    def test_all_positive_cases_are_non_increasing(self):
        for rm in _t31_resource_monotones():
            assert rm.is_non_increasing, f"Expected non-increasing for {rm.name}"

    def test_positive_cases_have_richer_resource_positive(self):
        result = _r()
        for rm in result.resource_monotones:
            assert rm.richer_value == 1, (
                f"Expected richer_value=1 for {rm.name}, got {rm.richer_value}"
            )

    def test_positive_cases_have_restricted_resource_zero(self):
        result = _r()
        for rm in result.resource_monotones:
            assert rm.restricted_value == 0, (
                f"Expected restricted_value=0 for {rm.name}, got {rm.restricted_value}"
            )


# ---------------------------------------------------------------------------
# Invariant profile classification
# ---------------------------------------------------------------------------


class TestInvariantProfiles:

    def test_unobstructed_system_class_none(self):
        from models.multiscale_observer_field import D1Profile
        from models.po1_foundational_derivation import _build_rich
        rich = _build_rich("inv_test", "T33", D1Profile(2, 2, 1, 2))
        profile = extract_invariant_profile(rich)
        assert profile.obstruction_class == "none"
        assert profile.invariant_level == 0
        assert profile.global_satisfiable

    def test_obstructed_system_class_h1(self):
        from models.multiscale_observer_field import D1Profile
        from models.po1_foundational_derivation import _build_restricted
        restricted = _build_restricted("inv_h1", "T33", D1Profile(1, 1, 0, 1), obstructed=True)
        profile = extract_invariant_profile(restricted)
        assert profile.obstruction_class == "H1_cohomological"
        assert profile.invariant_level == 1
        assert not profile.global_satisfiable

    def test_obstruction_certificate_h1(self):
        from models.multiscale_observer_field import D1Profile
        from models.po1_foundational_derivation import _build_restricted
        restricted = _build_restricted("cert_h1", "T33", D1Profile(1, 1, 0, 1), obstructed=True)
        cert = classify_obstruction(restricted)
        assert cert.certificate_type == "H1_finite_gluing"
        assert cert.local_patches_satisfiable
        assert not cert.global_assignment_exists

    def test_obstruction_certificate_none(self):
        from models.multiscale_observer_field import D1Profile
        from models.po1_foundational_derivation import _build_rich
        rich = _build_rich("cert_none", "T33", D1Profile(2, 2, 1, 2))
        cert = classify_obstruction(rich)
        assert cert.certificate_type == "no_obstruction"


# ---------------------------------------------------------------------------
# Derivation attempt coverage
# ---------------------------------------------------------------------------


class TestDerivationAttempts:

    def test_ipt_attempts_count(self):
        assert len(_ipt_derivation_attempts()) == 8

    def test_rmt_attempts_count(self):
        assert len(_rmt_derivation_attempts()) == 8

    def test_all_attempts_count(self):
        assert len(all_derivation_attempts()) == 16

    def test_ac1_derived_from_ipt(self):
        ac1 = next(a for a in _ipt_derivation_attempts() if a.condition_id == "AC1")
        assert ac1.derivation_status == "derived"

    def test_ac2_derived_from_ipt(self):
        ac2 = next(a for a in _ipt_derivation_attempts() if a.condition_id == "AC2")
        assert ac2.derivation_status == "derived"

    def test_ac3_derived_from_ipt(self):
        ac3 = next(a for a in _ipt_derivation_attempts() if a.condition_id == "AC3")
        assert ac3.derivation_status == "derived"

    def test_ac4_derived_from_ipt(self):
        ac4 = next(a for a in _ipt_derivation_attempts() if a.condition_id == "AC4")
        assert ac4.derivation_status == "derived"

    def test_ac5_naming_independent_from_ipt(self):
        ac5n = next(a for a in _ipt_derivation_attempts() if a.condition_id == "AC5_naming")
        assert ac5n.derivation_status == "independent"

    def test_ac5_naming_independent_from_rmt(self):
        ac5n = next(a for a in _rmt_derivation_attempts() if a.condition_id == "AC5_naming")
        assert ac5n.derivation_status == "independent"

    def test_ac6_derived_from_rmt(self):
        ac6 = next(a for a in _rmt_derivation_attempts() if a.condition_id == "AC6")
        assert ac6.derivation_status == "derived"

    def test_ac7_derived_from_rmt(self):
        ac7 = next(a for a in _rmt_derivation_attempts() if a.condition_id == "AC7")
        assert ac7.derivation_status == "derived"

    def test_ac5_measurable_derived_from_rmt(self):
        ac5m = next(a for a in _rmt_derivation_attempts() if a.condition_id == "AC5_measurable")
        assert ac5m.derivation_status == "derived"

    def test_ac3_not_applicable_to_rmt(self):
        ac3 = next(a for a in _rmt_derivation_attempts() if a.condition_id == "AC3")
        assert ac3.derivation_status == "not_applicable"


# ---------------------------------------------------------------------------
# Hypothesis verdicts
# ---------------------------------------------------------------------------


class TestHypothesisVerdicts:

    def test_six_hypotheses_evaluated(self):
        assert len(_r().hypothesis_verdicts) == 6

    def test_h0_rejected(self):
        h0 = next(hv for hv in _r().hypothesis_verdicts if hv.hypothesis_id == "H0")
        assert h0.verdict == "rejected"

    def test_h1_partially_supported(self):
        h1 = next(hv for hv in _r().hypothesis_verdicts if hv.hypothesis_id == "H1")
        assert h1.verdict == "partially_supported"

    def test_h2_partially_supported(self):
        h2 = next(hv for hv in _r().hypothesis_verdicts if hv.hypothesis_id == "H2")
        assert h2.verdict == "partially_supported"

    def test_h3_supported(self):
        h3 = next(hv for hv in _r().hypothesis_verdicts if hv.hypothesis_id == "H3")
        assert h3.verdict == "supported"

    def test_h4_boundary(self):
        h4 = next(hv for hv in _r().hypothesis_verdicts if hv.hypothesis_id == "H4")
        assert h4.verdict == "boundary"

    def test_h5_rejected(self):
        h5 = next(hv for hv in _r().hypothesis_verdicts if hv.hypothesis_id == "H5")
        assert h5.verdict == "rejected"

    def test_best_hypothesis_is_h3(self):
        assert _r().best_hypothesis == "H3"

    def test_h3_covers_at_least_as_many_as_h1(self):
        hvs = {hv.hypothesis_id: hv for hv in _r().hypothesis_verdicts}
        assert len(hvs["H3"].conditions_covered) >= len(hvs["H1"].conditions_covered)

    def test_h3_covers_at_least_as_many_as_h2(self):
        hvs = {hv.hypothesis_id: hv for hv in _r().hypothesis_verdicts}
        assert len(hvs["H3"].conditions_covered) >= len(hvs["H2"].conditions_covered)


# ---------------------------------------------------------------------------
# Counterexamples
# ---------------------------------------------------------------------------


class TestCounterexamples:

    def test_ac5_naming_counterexample_fails_ac5(self):
        ce = _ac5_naming_independence_counterexample()
        assert not ce.admissibility_check.ac5_structure_forgotten

    def test_ac5_naming_counterexample_passes_ac6(self):
        ce = _ac5_naming_independence_counterexample()
        assert ce.admissibility_check.ac6_restricted_obstructed

    def test_ac5_naming_counterexample_passes_ac7(self):
        ce = _ac5_naming_independence_counterexample()
        assert ce.admissibility_check.ac7_richer_unobstructed

    def test_ac5_naming_counterexample_verdict(self):
        ce = _ac5_naming_independence_counterexample()
        assert ce.admissibility_check.verdict == "non_admissible_no_forgotten_structure"

    def test_ac3_rmt_counterexample_fails_ac3(self):
        ce = _rmt_insufficient_for_ac3_counterexample()
        assert not ce.admissibility_check.ac3_projection_definable

    def test_ac3_rmt_counterexample_restricted_obstructed(self):
        ce = _rmt_insufficient_for_ac3_counterexample()
        assert ce.admissibility_check.ac6_restricted_obstructed

    def test_ac6_ipt_counterexample_fails_ac6(self):
        ce = _ipt_insufficient_for_ac6_counterexample()
        assert not ce.admissibility_check.ac6_restricted_obstructed

    def test_ac6_ipt_counterexample_passes_ac1_ac2_ac3(self):
        ce = _ipt_insufficient_for_ac6_counterexample()
        assert ce.admissibility_check.ac1_richer_valid
        assert ce.admissibility_check.ac2_restricted_valid
        assert ce.admissibility_check.ac3_projection_definable

    def test_three_counterexamples_built(self):
        assert len(_r().counterexamples) == 3


# ---------------------------------------------------------------------------
# Resource monotone properties
# ---------------------------------------------------------------------------


class TestResourceMonotone:

    def test_monotone_strict_decrease(self):
        from models.multiscale_observer_field import D1Profile
        from models.po1_foundational_derivation import _build_rich, _build_restricted
        rich = _build_rich("mono_test", "T33", D1Profile(2, 2, 1, 2))
        restricted = _build_restricted("mono_test", "T33", D1Profile(1, 1, 0, 1), obstructed=True)
        rm = compute_resource_monotone("test_monotone", rich, restricted)
        assert rm.is_non_increasing
        assert rm.is_strictly_decreasing

    def test_identical_systems_non_increasing_not_strictly(self):
        from models.multiscale_observer_field import D1Profile
        from models.po1_foundational_derivation import _build_rich
        sys = _build_rich("idem", "T33", D1Profile(2, 2, 1, 2))
        rm = compute_resource_monotone("idem_monotone", sys, sys)
        assert rm.is_non_increasing
        assert not rm.is_strictly_decreasing


# ---------------------------------------------------------------------------
# T33Result structure
# ---------------------------------------------------------------------------


class TestT33ResultStructure:

    def test_result_type(self):
        assert isinstance(_r(), T33Result)

    def test_remaining_independence_is_ac5_naming(self):
        assert "AC5_naming" in _r().remaining_independence

    def test_smallest_theorem_candidate_present(self):
        assert "SMALLER THEOREM CANDIDATE" in _r().smallest_theorem_candidate

    def test_recommendation_mentions_p5(self):
        assert "P5" in _r().recommendation

    def test_negative_results_note_present(self):
        assert len(_r().negative_results_note) > 50

    def test_t32_basis_loaded(self):
        assert _r().t32_basis is not None
        assert len(_r().t32_basis.minimal_condition_basis) == 6

    def test_dict_serializable(self):
        d = t33_result_to_dict(_r())
        assert "hypothesis_verdicts" in d
        assert "counterexamples" in d
        assert "ac_derivation_attempts" in d
        assert "resource_monotones" in d
        assert "best_hypothesis" in d
        assert d["best_hypothesis"] == "H3"
