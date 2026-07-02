"""Tests for T418: Schwarzschild horizon access-profile screen."""

from models.schwarzschild_horizon_access_profile_screen import (
    RadialEvent,
    access_profile_alignment_audit,
    horizon_geometry_audit,
    outgoing_radial_null_slope,
    outside_signal_positive_control,
    run_schwarzschild_horizon_access_profile_screen,
    trace_outgoing_radial_null,
)


def test_radial_null_slope_marks_horizon_boundary():
    assert outgoing_radial_null_slope(1.5) < 0.0
    assert outgoing_radial_null_slope(2.0) == 0.0
    assert outgoing_radial_null_slope(3.0) > 0.0


def test_inside_horizon_signal_does_not_escape_outward():
    trace = trace_outgoing_radial_null(RadialEvent("inside", 0.0, 1.5, "bit"))

    assert trace.escaped_to_exterior_cutoff is False
    assert trace.crossed_outward_through_horizon is False
    assert trace.classification in {
        "hits_singularity_before_escape",
        "trapped_inside_horizon",
    }


def test_outside_horizon_signal_reaches_exterior_cutoff():
    trace = trace_outgoing_radial_null(RadialEvent("outside", 0.0, 3.0, "pulse"))

    assert trace.escaped_to_exterior_cutoff is True
    assert trace.classification == "reaches_exterior_cutoff"


def test_access_aligned_exterior_capability_does_not_split():
    audit = access_profile_alignment_audit()

    assert audit["exterior_projection_equal"] is True
    assert audit["aligned_exterior_capability_equal"] is True
    assert audit["alignment_gate_verdict"] == "no_same_profile_projection_failure"


def test_cross_profile_split_is_classified_as_mismatch():
    audit = access_profile_alignment_audit()

    assert audit["cross_profile_capability_split"] is True
    assert (
        audit["mismatch_verdict"]
        == "cross_profile_mismatch_absorbed_by_horizon_access_profile"
    )
    assert (
        audit["residue_label"]
        == "absorbed_by_schwarzschild_causal_access_and_profile_alignment"
    )


def test_positive_control_has_teeth_for_exterior_records():
    control = outside_signal_positive_control()

    assert control["same_geometry"] is True
    assert control["both_reach_exterior"] is True
    assert control["records_distinguished_by_exterior_profile"] is True
    assert control["residue_label"] == "ordinary_exterior_causal_record_access"


def test_aggregate_result_keeps_claims_unmoved():
    result = run_schwarzschild_horizon_access_profile_screen()

    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert result["north_star_or_public_posture_update"] == "none"
    assert result["absorber_audit"]["schwarzschild_event_horizon"]["status"] == "absorbs"
    assert result["absorber_audit"]["black_hole_information_claim"]["status"] == "not_attempted"
    assert "cross-profile mismatch" in result["verdict"]


def test_horizon_geometry_summary_includes_inside_horizon_absorber():
    geometry = horizon_geometry_audit()

    assert geometry["slope_inside"] < 0.0
    assert geometry["slope_on_horizon"] == 0.0
    assert geometry["slope_outside"] > 0.0
    assert geometry["inside_trace"]["escaped_to_exterior_cutoff"] is False
    assert geometry["outside_trace"]["escaped_to_exterior_cutoff"] is True
