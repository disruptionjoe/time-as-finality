"""T69: LossKernel Failure Type — automated test suite."""
import pytest
from models.losskernel_failure_type import (
    witness_1_h0_preservation,
    witness_2_h1_destruction,
    witness_3_h0_to_h1_impossible,
    witness_4_h1_introduction_on_cyclic_cover,
    run_all,
    Cover,
)


def test_w1_h0_preserved():
    r = witness_1_h0_preservation()
    assert r["h0_failure_before"], "H0 gap must be present before loss"
    assert r["h0_failure_after"], "H0 gap must be preserved after topology-preserving loss"
    assert not r["h1_possible_before"], "Source cover must be acyclic (no H1)"
    assert not r["h1_possible_after"], "Target cover must remain acyclic after loss"
    assert not r["h1_created"], "Topology-preserving loss must not create H1"
    assert r["global_section_survives_in_target"], "Global section must survive in target"


def test_w2_h1_destroyed():
    r = witness_2_h1_destruction()
    assert r["source_cover_cyclic"], "Source 4-cycle cover must be cyclic"
    assert r["h1_nontrivial_before"], "H1 must be non-trivial before sub-cover restriction"
    assert not r["target_cover_cyclic"], "Target sub-cover must be acyclic"
    assert not r["h1_nontrivial_after"], "H1 must be zero after cycle is destroyed"
    assert r["h1_destroyed"], "H1 must be destroyed by sub-cover restriction"
    assert r["global_sections_in_target"] > 0, "Global sections must exist in target"
    assert r["all_lc_holonomy_plus1"], "All LC sections must have holonomy +1 (T65 check)"


def test_w3_h0_to_h1_impossible():
    r = witness_3_h0_to_h1_impossible()
    assert r["counterexamples_found"] == 0, (
        f"Found unexpected counterexample to H0->H1 impossibility: {r['counterexamples']}"
    )


def test_w3_acyclic_sub_cover_stays_acyclic():
    """Verify algebraic claim: sub-cover of acyclic cover is acyclic."""
    from itertools import combinations

    chain = Cover({
        "U0": frozenset({"v0", "v1"}),
        "U1": frozenset({"v1", "v2"}),
        "U2": frozenset({"v2", "v3"}),
    })
    assert not chain.has_cycle_in_nerve(), "Chain cover must be acyclic"

    patches = list(chain.patches.keys())
    for dropped in patches:
        remaining = {p: chain.patches[p] for p in patches if p != dropped}
        sub = Cover(remaining)
        assert not sub.has_cycle_in_nerve(), (
            f"Sub-cover after dropping {dropped} must remain acyclic"
        )


def test_w4_cyclic_projection():
    r = witness_4_h1_introduction_on_cyclic_cover()
    assert r["source_cover_cyclic"], "Source CHSH cover must be cyclic"
    assert not r["target_cover_cyclic"], "Alice-projection target must be acyclic"
    assert r["global_sections_survive"], "Global (Bob-only) sections must survive"


def test_main_theorem():
    results = run_all()
    s = results["summary"]
    assert s["H1_topology_preserving_preserves_type"], "H1 must be supported"
    assert s["H2_sub_cover_restriction_destroys_h1"], "H2 must be supported"
    assert s["H3_h0_to_h1_impossible"], "H3 must be supported"
    assert s["main_theorem"], "Main failure-type monotonicity theorem must be established"


def test_failure_type_ordering():
    """The ordering H1 > H0 > none means loss can only go down or stay flat."""
    # W1: H0 -> H0 (stay flat)
    w1 = witness_1_h0_preservation()
    assert w1["h0_failure_before"] and w1["h0_failure_after"]  # H0 -> H0
    assert not w1["h1_created"]  # no increase

    # W2: H1 -> H0 (go down)
    w2 = witness_2_h1_destruction()
    assert w2["h1_nontrivial_before"] and not w2["h1_nontrivial_after"]  # H1 -> H0

    # W3: H0 -> H0 (never H0 -> H1)
    w3 = witness_3_h0_to_h1_impossible()
    assert w3["counterexamples_found"] == 0  # no H0 -> H1
