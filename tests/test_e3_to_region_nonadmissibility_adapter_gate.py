"""Tests for T453: E3 to region nonadmissibility adapter gate."""

import json

from models import e3_to_region_nonadmissibility_adapter_gate as t453


def artifact():
    return t453.run()


def evaluation(candidate_id):
    return next(
        item
        for item in artifact()["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_and_recorded_scope():
    result = artifact()

    assert result["artifact"] == t453.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t447"].endswith(
        "T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"
    )
    assert result["sources"]["t452"].endswith(
        "T452-law-sector-nonadmissibility-gate-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Recorded-tier adapter gate only" in result["honest_ceiling"]
    assert "not a GU/TaF adapter" in result["honest_ceiling"]


def test_bare_t447_has_exact_witness_but_no_region_packet():
    bare = evaluation("bare_t447_exact_no_go")

    assert bare["admitted"] is False
    assert bare["adapter_label"] == "NOT_REGION_INDEXED_BASE_PACKET_MISSING"
    assert bare["candidate"]["has_t447_exact_no_go_witness"] is True
    assert bare["candidate"]["t447_survives_declared_finite_a2"] is True
    assert bare["candidate"]["clears_t434_law_admission"] is False
    assert bare["candidate"]["r_statistics_and_interventions_matched"] is False
    assert "does not supply the T434/T445 region equality certificates" in bare["reason"]


def test_citation_only_t445_plus_t447_still_hits_t452_absorber():
    citation = evaluation("citation_only_t445_plus_t447")

    assert citation["admitted"] is False
    assert citation["adapter_label"] == "NOT_ADMITTED_T452_ABSORBER_STILL_FIRES"
    assert citation["candidate"]["clears_t434_law_admission"] is True
    assert citation["candidate"]["r_statistics_and_interventions_matched"] is True
    assert citation["candidate"]["boundary_menu_splits_capability"] is True
    assert citation["candidate"]["completion_merely_hidden_from_r"] is True
    assert citation["candidate"]["exact_witness_targets_named_completion"] is False
    assert "Adding a T447 citation" in citation["reason"]


def test_reference_policy_pair_is_e0_declared_completion():
    policy_pair = evaluation("reference_policy_pair")

    assert policy_pair["admitted"] is False
    assert (
        policy_pair["adapter_label"]
        == "E0_DECLARED_BY_ADMITTED_REFERENCE_OR_POLICY_COMPLETION"
    )
    assert policy_pair["candidate"]["completion_factors_through_admitted_policy"] is True
    assert policy_pair["candidate"]["exact_witness_targets_named_completion"] is True


def test_generic_sector_gauge_claim_routes_to_n14_absorber():
    generic = evaluation("generic_sector_gauge_claim")

    assert generic["admitted"] is False
    assert generic["adapter_label"] == "ROUTES_TO_N14_SECTOR_GAUGE_ABSORBER"
    assert generic["candidate"]["sector_gauge_generic_claim"] is True
    assert "reservoir, reference, boundary, and gauge data" in generic["reason"]


def test_exact_witness_and_negative_control_requirements():
    missing_control = evaluation("synthetic_missing_negative_control")

    assert missing_control["admitted"] is False
    assert missing_control["adapter_label"] == "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
    assert missing_control["candidate"]["negative_control_present"] is False


def test_only_synthetic_integrated_packet_is_admitted_as_future_target():
    result = artifact()
    synthetic = evaluation("synthetic_integrated_e3_region_packet")

    assert synthetic["admitted"] is True
    assert synthetic["adapter_label"] == (
        "ADMITTED_E3_REGION_ADAPTER_REVIEW_TARGET_NO_PROMOTION"
    )
    assert synthetic["candidate"]["synthetic_control_only"] is True
    assert result["overall_verdict"]["admitted_candidate_ids"] == [
        "synthetic_integrated_e3_region_packet"
    ]
    assert result["overall_verdict"]["admitted_candidates_are_synthetic_only"] is True


def test_overall_verdict_is_conservative():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t453.VERDICT
    assert verdict["bare_t447_label"] == "NOT_REGION_INDEXED_BASE_PACKET_MISSING"
    assert verdict["citation_only_t445_plus_t447_label"] == (
        "NOT_ADMITTED_T452_ABSORBER_STILL_FIRES"
    )
    assert verdict["current_artifacts_discharge_region_burden"] is False
    assert verdict["claim_ledger_update"] == "none; no claim promotion"
    assert "Only a synthetic integrated packet" in verdict["reading"]


def test_result_is_json_serializable_and_avoids_promotion_language():
    result = artifact()

    json.dumps(result, sort_keys=True)
    combined = json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "region-indexed discriminator success proved",
        "WAY theorem proved",
        "quantum physics theorem proved",
        "GU adapter revived",
        "public posture authorized",
    )
    assert all(term not in combined for term in banned)
