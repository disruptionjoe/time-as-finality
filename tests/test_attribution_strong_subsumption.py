"""Tests for T247 attribution strong-subsumption packet."""

import json

from models.attribution_strong_subsumption import (
    analyze,
    build_family,
    imported_objects_are_canonical,
    injector_clears,
    result_to_dict,
    structural_fingerprint,
    trichotomy_is_exhaustive_on_family,
)
from models.attribution_invariant_separation import _freeze, nu


def test_family_is_one_nu_fiber_with_three_off_nu_strata():
    family = build_family()

    assert len(family) == 8
    assert len({nu(case) for case in family}) == 1
    assert len({_freeze(structural_fingerprint(case)) for case in family}) == 8
    assert trichotomy_is_exhaustive_on_family(family) is True


def test_every_separating_pattern_is_absorbed_by_join():
    result = analyze()

    assert result.total_separation_patterns_enumerated == 4140
    assert result.separating_patterns == 4139
    assert result.route_b_clears_found == 0
    assert result.separating_patterns_all_absorbed_by_nu_join is True
    assert result.general_factorization_holds is True
    assert result.verdict == "closed"


def test_per_stratum_absorber_census_names_the_three_predecessor_gates():
    result = analyze()

    assert result.per_stratum_absorber_census == {
        "nu_prime": 16,
        "nu_struct": 8,
        "nu_cocycle": 4,
        "none": 0,
    }
    assert result.refinement_chain_holds is True


def test_nonvacuity_and_import_identity_guards_hold():
    result = analyze()

    assert injector_clears() is True
    assert result.nonvacuity_injector_clears is True
    assert all(imported_objects_are_canonical().values())
    assert all(result.object_identity_guards.values())


def test_serialized_payload_has_no_promotion_or_absolute_path_fields():
    payload = result_to_dict(analyze())
    encoded = json.dumps(payload, sort_keys=True)

    assert payload["test"] == "T247-attribution-strong-subsumption-theorem"
    assert payload["verdict"] == "closed"
    assert "criterion_6_earned" not in payload
    assert "independence_earned" not in payload
    assert "C:\\Users\\" not in encoded
    assert "/Users/" not in encoded
