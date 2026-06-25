"""Tests for T228: D1Cat transfinite colimit decision.

These are real assertion checks of the categorical mechanics that decide the
T222 contribution-needed edge. No placeholders.
"""

from models.d1_restriction_system import D1_DIMENSIONS
from models.d1cat_transfinite_colimit import (
    build_descending_chain,
    chain_saturates_empty,
    composite_preserved_dims,
    empty_preserved_morphism_is_legal,
    object_varying_chain_has_no_uniform_colimit_object,
    run_decision,
    sequential_colimit_of_constant_object_chain,
)


def test_descending_chain_strictly_decreases_then_saturates():
    chain = build_descending_chain(6)
    sizes = [len(step.composite_preserved) for step in chain]
    # Strictly decreasing until it hits 0, then constant at 0.
    assert sizes == [4, 3, 2, 1, 0, 0]


def test_descent_saturates_at_empty_in_at_most_four_steps():
    chain = build_descending_chain(6)
    # The fixed 4-element universe forces saturation by step 4: 'transfinite'
    # is a red herring at the level of morphism dimension data.
    assert chain_saturates_empty(chain)
    saturation_step = next(
        i for i, s in enumerate(chain) if s.composite_preserved == ()
    )
    assert saturation_step == 4
    assert saturation_step < len(D1_DIMENSIONS) + 1


def test_composite_preserved_dims_is_intersection():
    chain = build_descending_chain(3)
    # After 3 steps: keep first 4, then 3, then 2 -> intersection = first 2.
    assert composite_preserved_dims(chain) == D1_DIMENSIONS[:2]


def test_empty_preserved_morphism_is_a_legal_d1cat_morphism():
    # The honesty check: the empty-intersection limit does NOT exit D1Cat at the
    # morphism level. preserved_dimensions ranges over ALL subsets of the
    # 4-element universe, and () is one of them.
    assert empty_preserved_morphism_is_legal()


def test_constant_object_chain_has_a_colimit_object():
    out = sequential_colimit_of_constant_object_chain()
    assert out["colimit_object_valid"] is True
    assert out["colimit_leg_legal"] is True
    assert out["colimit_leg_preserved"] == ()
    assert out["saturated_empty"] is True


def test_object_varying_chain_obstruction_mechanism():
    out = object_varying_chain_has_no_uniform_colimit_object()
    # Disagreeing-profile objects ARE connectable by an empty-preserved morphism,
    # and that morphism is 'reached' (legal). This is exactly why the colimit
    # object carrying surviving dimension data is underdetermined.
    assert out["disagreeing_profiles"] is True
    assert out["empty_preserved_morphism_reached"] is True
    assert out["preserved_dims"] == ()


def test_run_decision_payload_is_consistent():
    payload = run_decision()
    assert payload["chain_saturates_empty"] is True
    assert payload["saturation_step"] == 4
    assert payload["empty_preserved_morphism_is_legal"] is True
    assert payload["composite_preserved_dims"] == ()
