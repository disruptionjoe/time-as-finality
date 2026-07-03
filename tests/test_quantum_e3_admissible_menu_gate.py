"""Tests for T435: quantum E3 admissible-menu gate."""

import json

from models import quantum_e3_admissible_menu_gate as t435


def artifact():
    return t435.run()


def candidate(candidate_id):
    return next(
        item for item in artifact()["candidate_audits"] if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_and_scope():
    result = artifact()

    assert result["artifact"] == t435.ARTIFACT
    assert result["source_taxonomy"].endswith("capability-boundary-mode-taxonomy-REFERENCE.md")
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "not a WAY theorem" in result["honest_ceiling"]
    assert "not a GU/TaF adapter" in result["honest_ceiling"]


def test_main_phase_pair_is_e3_relative_to_a1_without_reference():
    main = candidate("z2_phase_pair_a1_no_reference")

    assert main["a1_shadow_left"] == [0.5, 0.5]
    assert main["a1_shadow_right"] == [0.5, 0.5]
    assert main["a1_statistics_equal"] is True
    assert main["separator_gap"] == 2.0
    assert main["separator_commutes_with_symmetry"] is False
    assert main["separator_commutator_norm"] == 2.0
    assert main["admitted_e3_relative_to_a1"] is True
    assert main["residue_label"] == "E3_STRUCTURAL_SYMMETRY_RELATIVE_TO_A1_NO_REFERENCE"


def test_a2_reference_resource_demotes_same_pair_to_e0_declared():
    a2 = candidate("z2_phase_pair_a2_reference")

    assert a2["a1_statistics_equal"] is True
    assert a2["separator_commutes_with_symmetry"] is False
    assert a2["packet"]["admissible_class"] == "A2"
    assert a2["packet"]["reference_resource_admitted"] is True
    assert a2["admitted_e3_relative_to_a1"] is False
    assert a2["residue_label"] == "E0_DECLARED_RELATIVE_TO_A2_REFERENCE_RESOURCE"


def test_a1_visible_charge_population_is_not_boundary():
    visible = candidate("charge_population_visible_control")

    assert visible["a1_statistics_equal"] is False
    assert visible["separator_commutes_with_symmetry"] is True
    assert visible["admitted_e3_relative_to_a1"] is False
    assert visible["residue_label"] == "no_boundary_a1_already_distinguishes"


def test_classical_full_code_control_does_not_pass_quantum_e3_gate():
    control = candidate("classical_full_code_control")

    assert control["packet"]["regime"] == "classical_finite"
    assert control["admitted_e3_relative_to_a1"] is False
    assert control["residue_label"] == "control_not_quantum_e3_regime"


def test_post_hoc_hidden_label_and_missing_symmetry_are_rejected():
    post_hoc = candidate("post_hoc_symmetry_selector")
    assert post_hoc["admitted_e3_relative_to_a1"] is False
    assert post_hoc["residue_label"] == "not_admitted_post_hoc_symmetry_or_separator"

    hidden = candidate("hidden_label_phase_oracle")
    assert hidden["admitted_e3_relative_to_a1"] is False
    assert hidden["residue_label"] == "blocked_hidden_label_oracle"

    missing = candidate("no_symmetry_packet")
    assert missing["admitted_e3_relative_to_a1"] is False
    assert missing["residue_label"] == "not_admitted_no_predeclared_symmetry"


def test_dephased_mixture_control_uses_same_a_class_gate():
    mixed = candidate("symmetric_mixed_state_control")

    assert mixed["a1_statistics_equal"] is True
    assert mixed["separator_gap"] == 1.0
    assert mixed["separator_commutes_with_symmetry"] is False
    assert mixed["admitted_e3_relative_to_a1"] is True
    assert mixed["residue_label"] == "E3_STRUCTURAL_SYMMETRY_RELATIVE_TO_A1_NO_REFERENCE"


def test_overall_verdict_keeps_scope_narrow():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t435.VERDICT
    assert verdict["main_pair_admitted_e3_relative_to_A1"] is True
    assert verdict["same_pair_A2_declared"] is True
    assert verdict["admitted_e3_candidate_ids"] == [
        "z2_phase_pair_a1_no_reference",
        "symmetric_mixed_state_control",
    ]
    assert "not a physics theorem" in verdict["reading"]


def test_result_is_json_serializable_and_avoids_promotion_language():
    result = artifact()

    json.dumps(result, sort_keys=True)
    combined = json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "WAY theorem proved",
        "GU adapter revived",
        "quantum physics claim proved",
    )
    assert all(term not in combined for term in banned)
