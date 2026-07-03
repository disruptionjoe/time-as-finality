"""Tests for T434: substrate-law admission gate."""

import json

from models import substrate_law_admission_gate as t434


def artifact():
    return t434.run()


def candidate(candidate_id):
    return next(
        item for item in artifact()["candidate_audits"] if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_and_scope():
    result = artifact()

    assert result["artifact"] == t434.ARTIFACT
    assert result["source_artifact"] == "T406-transition-system-operation-unavailability-gate-v0.1"
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Admission gate only" in result["honest_ceiling"]


def test_current_t406_main_pair_is_not_admitted():
    bare = candidate("bare_t406_main_pair")

    assert bare["capability_split"] is True
    assert bare["fixed_accounting_projection_equal"] is True
    assert bare["transition_system_completion_equal"] is False
    assert bare["admitted"] is False
    assert bare["residue_label"] == "not_admitted_no_independent_law_or_measurement"


def test_transition_table_restatement_is_rejected():
    restatement = candidate("transition_table_restatement")

    assert restatement["law_package"]["source_kind"] == "transition_table"
    assert restatement["law_package"]["reads_transition_relation"] is True
    assert restatement["admitted"] is False
    assert restatement["residue_label"] == "not_admitted_transition_table_restatement"


def test_post_hoc_pair_specific_hidden_and_non_native_laws_are_rejected():
    post_hoc = candidate("post_hoc_conservation_selector")
    assert post_hoc["admitted"] is False
    assert post_hoc["residue_label"] == "not_admitted_post_hoc_law"

    pair_specific = candidate("pair_specific_law")
    assert pair_specific["admitted"] is False
    assert pair_specific["residue_label"] == "not_admitted_pair_specific_law"

    hidden = candidate("hidden_label_law")
    assert hidden["admitted"] is False
    assert hidden["residue_label"] == "blocked_hidden_label_law"

    non_native = candidate("non_native_observable")
    assert non_native["admitted"] is False
    assert non_native["residue_label"] == "not_admitted_non_native_observable"


def test_measured_dynamics_needs_replicates_and_negative_control():
    weak = candidate("underpowered_measured_dynamics")

    assert weak["law_package"]["source_kind"] == "measured_dynamics"
    assert weak["law_package"]["measurement_replicates"] < t434.MIN_MEASURED_REPLICATES
    assert weak["law_package"]["has_negative_control"] is False
    assert weak["admitted"] is False
    assert weak["residue_label"] == "not_admitted_underpowered_measured_dynamics"


def test_fixed_accounting_mismatch_absorbs_before_law_verdict():
    control = candidate("fixed_accounting_change_control")

    assert control["capability_split"] is True
    assert control["fixed_accounting_projection_equal"] is False
    assert control["admitted"] is False
    assert control["residue_label"] == "absorbed_by_fixed_accounting_completion"


def test_synthetic_positive_controls_show_admitted_shape_only():
    conservation = candidate("conservation_law_positive_control")
    assert conservation["synthetic_positive_control"] is True
    assert conservation["admitted"] is True
    assert (
        conservation["residue_label"]
        == "admitted_conservation_law_forced_transition_candidate"
    )
    assert conservation["law_package"]["reads_transition_relation"] is False
    assert conservation["law_package"]["declared_before_pair"] is True

    measured = candidate("measured_dynamics_positive_control")
    assert measured["synthetic_positive_control"] is True
    assert measured["admitted"] is True
    assert (
        measured["residue_label"]
        == "admitted_measured_dynamics_forced_transition_candidate"
    )
    assert measured["law_package"]["measurement_replicates"] >= t434.MIN_MEASURED_REPLICATES
    assert measured["law_package"]["has_negative_control"] is True


def test_matched_transition_no_split_control_is_not_a_positive():
    matched = candidate("matched_transition_no_split_control")

    assert matched["capability_split"] is False
    assert matched["transition_system_completion_equal"] is True
    assert matched["admitted"] is False
    assert matched["residue_label"] == "not_needed_no_capability_split"


def test_overall_verdict_keeps_controls_synthetic():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t434.VERDICT
    assert verdict["current_t406_main_pair_admitted"] is False
    assert verdict["admitted_candidate_ids"] == [
        "conservation_law_positive_control",
        "measured_dynamics_positive_control",
    ]
    assert verdict["synthetic_positive_controls_only"] is True
    assert "do not supply real physics" in verdict["reading"]


def test_result_is_json_serializable_and_not_claim_language():
    result = artifact()

    json.dumps(result, sort_keys=True)
    banned = ("claim promotion follows", "theorem proved", "real substrate law proved")
    combined = json.dumps(result, sort_keys=True)
    assert all(term not in combined for term in banned)
