"""Tests for T441: E1 family-limit packet gate."""

import json

from models import e1_family_limit_packet_gate as t441


def artifact():
    return t441.run()


def classification(packet_id):
    return next(
        item for item in artifact()["classifications"] if item["packet"]["packet_id"] == packet_id
    )


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t441.ARTIFACT
    assert result["sources"]["t440_e1_route"].endswith(
        "T440-ideal-limit-sector-lock-routing-gate-v0.1-results.md"
    )
    assert result["sources"]["t439_thermo_gate"].endswith(
        "T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md"
    )
    assert result["sources"]["h7_handoff"].endswith("h7-physical-deletion-substrate-handoff.md")
    assert "admission gate only" in result["honest_ceiling"]


def test_single_instance_and_finite_barriers_are_not_e1():
    ideal = classification("single_instance_infinite_barrier")
    barrier = classification("finite_barrier_metastable_family")
    finite_gap = classification("finite_positive_gap_only")

    assert ideal["label"] == "H7_NULL_SINGLE_INSTANCE_IDEALIZATION"
    assert ideal["route"] == "h7_null_or_idealization"
    assert barrier["label"] == "ABSORBED_BY_FINITE_KINETICS"
    assert finite_gap["label"] == "ABSORBED_BY_FINITE_GAP_NO_LIMIT_FORCING"
    assert all(
        not item["admitted_for_future_e1_review"] for item in (ideal, barrier, finite_gap)
    )


def test_post_hoc_hidden_resource_and_family_drift_are_rejected():
    selector = classification("post_hoc_limit_selector")
    hidden = classification("hidden_reservoir_boundary_drift")
    drift = classification("family_reencoding_drift")

    assert selector["label"] == "REJECTED_POST_HOC_LIMIT_SELECTOR"
    assert hidden["label"] == "REJECTED_CHANGED_RESOURCE_OR_BOUNDARY"
    assert drift["label"] == "REJECTED_FAMILY_DRIFT_OR_REENCODING"


def test_finite_approximants_task_and_invariant_are_required():
    approximants = classification("missing_finite_approximants")
    changed_task = classification("changed_task_operation_class")
    invariant = classification("no_predeclared_limit_invariant")
    anchored = classification("invariant_not_observable_on_approximants")

    assert approximants["label"] == "REJECTED_NO_FINITE_APPROXIMANT_MAP"
    assert changed_task["label"] == "REJECTED_UNSTABLE_TASK_OPERATION_OR_ACCOUNTING"
    assert invariant["label"] == "REJECTED_NO_PREDECLARED_LIMIT_INVARIANT"
    assert anchored["label"] == "REJECTED_INVARIANT_NOT_ANCHORED_TO_APPROXIMANTS"


def test_convergence_controls_and_divergence_are_required():
    controls = classification("missing_convergence_controls")
    bounded = classification("bounded_cost_sequence")

    assert controls["label"] == "REJECTED_NO_CONVERGENCE_OR_NEGATIVE_CONTROLS"
    assert bounded["label"] == "REJECTED_NO_DIVERGING_COST_OR_NONLOCALITY"
    assert bounded["admitted_for_future_e1_review"] is False


def test_e2_and_e3_packets_route_to_their_own_gates():
    e2 = classification("e2_period_hardness_packet")
    e3 = classification("e3_exact_sector_no_go_packet")

    assert e2["route"] == "route_to_e2_gate"
    assert e2["label"] == "ROUTE_TO_E2_HARDNESS_GATE"
    assert e3["route"] == "route_to_e3_gate"
    assert e3["label"] == "ROUTE_TO_E3_EXACT_NO_GO_GATE"


def test_synthetic_e1_family_packet_is_future_review_only():
    item = classification("e1_family_limit_synthetic_control")

    assert item["admitted_for_future_e1_review"] is True
    assert item["route"] == "admitted_as_future_e1_review"
    assert item["label"] == "ADMITTED_E1_FAMILY_LIMIT_REVIEW_NO_PROMOTION"
    assert item["packet"]["synthetic_positive_control"] is True
    assert "future review" in item["reason"]


def test_overall_verdict_keeps_e1_h7_claims_and_public_posture_gated():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t441.VERDICT
    assert verdict["admitted_packet_ids"] == ["e1_family_limit_synthetic_control"]
    assert verdict["synthetic_positive_controls_only"] is True
    assert verdict["e1_theorem"].startswith("none")
    assert verdict["h7_promotion"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion"


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "H7 promoted",
        "E1 theorem proved",
        "thermodynamic arrow proved",
        "physics claim proved",
        "public posture authorized",
        "claim promotion follows",
    )
    assert all(term not in combined for term in banned)
