from functools import lru_cache

from models import classical_finite_boundary_declarability_gate as t432


@lru_cache(maxsize=1)
def artifact():
    return t432.run()


def named(name):
    return next(
        certificate for certificate in artifact()["named_certificates"]
        if certificate["name"] == name
    )


def test_hidden_complement_bit_is_declared_relative_to_a1():
    cert = named("hidden_complement_bit")

    assert cert["a0_region_measurable"] is False
    assert cert["a1_full_code_measurable"] is True
    assert cert["has_boundary_pair"] is True
    assert cert["minimal_coordinate_support_labels"] == ["{x1}"]
    assert cert["verdict"] == "E0_DECLARED_RELATIVE_TO_A1_FULL_CODE"
    assert cert["single_instance_physical_boundary_relative_to_A1"] is False


def test_region_visible_control_has_no_boundary():
    cert = named("region_visible_control")

    assert cert["a0_region_measurable"] is True
    assert cert["has_boundary_pair"] is False
    assert cert["verdict"] == "NO_BOUNDARY_A0_REGION_DETERMINES_DATUM"


def test_full_support_parity_guard_has_no_proper_support_but_is_declared():
    cert = named("full_support_parity_separator")

    assert cert["a0_region_measurable"] is False
    assert cert["a1_full_code_measurable"] is True
    assert cert["has_boundary_pair"] is True
    assert cert["minimal_coordinate_support_labels"] == ["{x0,x1,x2}"]
    assert cert["has_no_proper_coordinate_support"] is True
    assert cert["single_instance_lookup_upper_bound"] == 8
    assert cert["verdict"] == "E0_DECLARED_RELATIVE_TO_A1_FULL_CODE"


def test_region_plus_complement_relation_records_mixed_support():
    cert = named("region_plus_complement_relation")

    assert cert["a0_region_measurable"] is False
    assert cert["a1_full_code_measurable"] is True
    assert cert["minimal_coordinate_support_labels"] == ["{x0,x1}"]
    assert cert["has_no_proper_coordinate_support"] is False
    assert cert["verdict"] == "E0_DECLARED_RELATIVE_TO_A1_FULL_CODE"


def test_exhaustive_small_boolean_sweep_finds_no_physical_candidates():
    sweep = artifact()["exhaustive_boolean_sweep"]

    assert [row["n_bits"] for row in sweep] == [1, 2, 3]
    assert all(row["boundary_functions"] > 0 for row in sweep)
    assert all(
        row["boundary_functions"] == row["a1_declared_boundaries"]
        for row in sweep
    )
    assert all(row["invalid_or_physical_candidates"] == 0 for row in sweep)
    assert any(row["no_proper_support_boundaries"] > 0 for row in sweep)


def test_overall_verdict_is_classical_fragment_only():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == "C_FRAGMENT_EXECUTABLE_E0_FOR_SINGLE_INSTANCE"
    assert verdict["no_physical_candidates_in_exhaustive_sweep"] is True
    assert artifact()["all_named_boundaries_declared_relative_to_A1"] is True
    assert "not a quantum statement" in artifact()["honest_ceiling"]
    assert "not cross-repo evidence" in artifact()["honest_ceiling"]
