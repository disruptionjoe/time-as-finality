from functools import lru_cache

from models import classical_declarability_proof_certificate as t433


@lru_cache(maxsize=1)
def artifact():
    return t433.run()


def named(name):
    return next(case for case in artifact()["named_cases"] if case["name"] == name)


def test_proof_certificate_states_the_classical_a1_lemma():
    proof = artifact()["proof_certificate"]

    assert proof["verdict"] == "CLASSICAL_DECLARABILITY_PROOF_CERTIFIED"
    assert "finite classical product code" in proof["statement"]
    assert "A1 contains the full co-present code" in proof["statement"]
    assert len(proof["proof_steps"]) == 5
    assert "not a quantum theorem" in proof["honest_scope"]


def test_region_visible_control_has_no_boundary():
    case = named("region_visible_control")

    assert case["a0_region_measurable"] is True
    assert case["has_boundary_pair"] is False
    assert case["verdict"] == "NO_BOUNDARY_A0_REGION_DETERMINES_DATUM"


def test_hidden_complement_bit_is_constructively_a1_declared():
    case = named("hidden_complement_bit")

    assert case["a0_region_measurable"] is False
    assert case["a1_full_code_measurable"] is True
    assert case["has_boundary_pair"] is True
    assert case["minimal_coordinate_support_labels"] == ["{x1}"]
    assert case["single_instance_physical_candidate_relative_to_A1"] is False
    assert case["verdict"] == "E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP"


def test_full_support_guard_prevents_complement_only_reading():
    case = named("full_support_parity_guard")

    assert case["a0_region_measurable"] is False
    assert case["a1_full_code_measurable"] is True
    assert case["has_no_proper_coordinate_support"] is True
    assert case["minimal_coordinate_support_labels"] == ["{x0,x1,x2}"]
    assert case["a1_lookup_upper_bound"] == 8
    assert case["verdict"] == "E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP"


def test_nonbinary_product_case_is_inside_the_same_classical_proof():
    case = named("nonbinary_region_complement_relation")

    assert case["domain_sizes"] == [3, 2]
    assert case["a0_region_measurable"] is False
    assert case["a1_full_code_measurable"] is True
    assert case["has_boundary_pair"] is True
    assert case["a1_lookup_upper_bound"] == 6
    assert case["verdict"] == "E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP"


def test_mixed_finite_sweep_finds_no_a1_physical_candidates():
    sweep = artifact()["exhaustive_mixed_sweep"]

    assert [row["domain_shape"] for row in sweep] == [
        [2],
        [2, 2],
        [2, 3],
        [3, 2],
        [2, 2, 2],
    ]
    assert all(row["boundary_functions"] > 0 for row in sweep)
    assert all(
        row["boundary_functions"] == row["a1_declared_boundaries"]
        for row in sweep
    )
    assert all(
        row["single_instance_physical_candidates_relative_to_A1"] == 0
        for row in sweep
    )


def test_overall_verdict_keeps_the_scope_narrow():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == "CLASSICAL_DECLARABILITY_PROOF_CERTIFIED"
    assert verdict["all_named_boundary_cases_declared_relative_to_A1"] is True
    assert verdict["no_physical_candidates_in_mixed_sweep"] is True
    assert "not an E3/WAY statement" in artifact()["honest_ceiling"]
    assert "not cross-repo evidence" in artifact()["honest_ceiling"]
