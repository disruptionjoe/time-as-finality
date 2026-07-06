"""Tests for T462: H7 physical-deletion overread absorber."""

import json

from models import h7_physical_deletion_overread_absorber as t462


def artifact():
    return t462.run()


def classification(packet_id):
    return next(
        item
        for item in artifact()["classifications"]
        if item["packet"]["packet_id"] == packet_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t462.ARTIFACT
    assert result["sources"]["h7_handoff"].endswith(
        "h7-physical-deletion-substrate-handoff.md"
    )
    assert result["sources"]["t461_locality_control"].endswith(
        "T461-e1-local-recovery-family-audition-v0.1-results.md"
    )
    assert "Recorded-tier absorber audit only" in result["honest_ceiling"]


def test_minimum_h7_object_lists_required_gates():
    minimum = artifact()["minimum_h7_object"]

    assert "reverse edge typed as physical_record_deletion" in minimum
    assert "full H7 absorber vector declared and matched" in minimum
    assert "allowed control class declared" in minimum
    assert "finite operational substrate supplied" in minimum
    assert "reverse remains constructor-impossible after full accounting" in minimum
    assert "negative controls declared" in minimum


def test_t461_locality_depth_overread_is_absorbed_not_h7():
    item = classification("t461_local_recovery_depth_overread")

    assert item["label"] == "ABSORBED_BY_T461_LOCALITY_DEPTH_NOT_DELETION"
    assert item["route"] == "absorbed_by_e1_locality_control"
    assert item["admitted_for_future_h7_review"] is False
    assert item["h7_reopened"] is False
    assert item["minimum_h7_commitment_met"] is False


def test_non_deletion_reverse_edges_are_rejected():
    expected = {
        "observer_access_revocation": "NON_DELETION_ACCESS_LOSS",
        "provenance_authority_revocation": "NON_DELETION_PROVENANCE_LOSS",
        "support_copy_removal": "NON_DELETION_SUPPORT_COPY_REMOVAL",
        "gauge_relabeling_record_loss": "NON_DELETION_GAUGE_RELABELING",
    }

    for packet_id, label in expected.items():
        item = classification(packet_id)
        assert item["label"] == label
        assert item["admitted_for_future_h7_review"] is False
        assert item["h7_reopened"] is False


def test_absorber_stack_blocks_common_physical_deletion_overreads():
    expected = {
        "finite_barrier_metastable_delete": "ABSORBED_BY_T439_FINITE_KINETICS",
        "hidden_sink_export_delete": "ABSORBED_BY_T145_HIDDEN_SINK_EXPORT",
        "changed_blind_reset_ledger": "ABSORBED_BY_CHANGED_LEDGER_ACCOUNTING",
        "source_copy_reversible_control_missing": (
            "ABSORBED_BY_SOURCE_COPY_OR_REVERSIBLE_CONTROL"
        ),
        "ideal_sector_lock_delete": "ROUTE_TO_T440_T168_IDEAL_OR_SECTOR_ABSORBER",
    }

    for packet_id, label in expected.items():
        item = classification(packet_id)
        assert item["label"] == label
        assert item["admitted_for_future_h7_review"] is False
        assert item["h7_reopened"] is False


def test_minimum_commitment_and_control_failures_do_not_admit():
    incomplete = classification("substrate_incomplete_delete_claim")
    possible = classification("control_possible_after_accounting")
    vanished = classification("matched_split_vanishes")

    assert incomplete["label"] == "REJECTED_NO_NAMED_PHYSICAL_SUBSTRATE"
    assert incomplete["absorber_vector_matched"] is False
    assert incomplete["minimum_h7_commitment_met"] is False

    assert possible["label"] == "REJECTED_DELETION_STILL_CONTROL_POSSIBLE"
    assert possible["absorber_vector_matched"] is True
    assert possible["minimum_h7_commitment_met"] is True

    assert vanished["label"] == "ABSORBED_SPLIT_VANISHES_AFTER_MATCHING"
    assert vanished["route"] == "absorbed_by_matched_accounting"
    assert vanished["minimum_h7_commitment_met"] is True

    assert all(
        item["admitted_for_future_h7_review"] is False
        for item in (incomplete, possible, vanished)
    )


def test_only_synthetic_full_burden_packet_is_admitted_for_review():
    item = classification("synthetic_full_burden_physical_deletion_packet")
    verdict = artifact()["overall_verdict"]

    assert item["label"] == "ADMITTED_H7_PHYSICAL_DELETION_REVIEW_TARGET_NO_PROMOTION"
    assert item["route"] == "admitted_as_synthetic_h7_review_target"
    assert item["absorber_vector_matched"] is True
    assert item["minimum_h7_commitment_met"] is True
    assert item["admitted_for_future_h7_review"] is True
    assert item["h7_reopened"] is False

    assert verdict["admitted_review_target_ids"] == [
        "synthetic_full_burden_physical_deletion_packet"
    ]
    assert verdict["synthetic_positive_controls_only"] is True


def test_overall_verdict_records_no_claim_or_h7_movement():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t462.VERDICT
    assert verdict["all_h7_reopened_flags_false"] is True
    assert verdict["h7_promotion"].startswith("none")
    assert verdict["physical_deletion_evidence"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion or demotion"


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "H7 promoted",
        "physical deletion proved",
        "thermodynamic arrow proved",
        "E1 theorem proved",
        "E3 theorem proved",
        "public posture authorized",
        "claim promotion follows",
    )
    assert all(term not in combined for term in banned)
