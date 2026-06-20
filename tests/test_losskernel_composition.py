"""Tests for T73: LossKernel composition law.

Verifies H1–H4 on T34/T37 paths.
"""

import pytest

from models.losskernel_composition import (
    compose_loss_chain,
    compose_loss_network,
    run_t73_analysis,
    verify_h1,
    verify_h2,
    verify_h3,
    verify_h4,
)
from models.po1_chained_projection import run_t34_analysis
from models.transport_network import run_t37_analysis


@pytest.fixture(scope="module")
def t37():
    return run_t37_analysis()


@pytest.fixture(scope="module")
def t34():
    return run_t34_analysis()


@pytest.fixture(scope="module")
def t73():
    return run_t73_analysis()


# ---------------------------------------------------------------------------
# H1: Composition law = union of per-step LossKernels
# ---------------------------------------------------------------------------


def test_h1_composition_law_holds(t37, t34):
    result = verify_h1(t37, t34)
    assert result["h1_passes"], (
        f"H1 composition law failed on some paths: "
        f"{[(k, v) for k, v in result['checks'].items() if not v['composition_law_holds']]}"
    )


def test_h1_t37_diamond_path_a(t37):
    """Path A (SRC->L_A->TGT): LossKernel should be {'type_guarantee'}."""
    diamond = t37.diamond_network_analysis
    path_a = next(
        pa.path for pa in diamond.path_admissibilities
        if "L_A" in pa.path.layer_names or "A" in pa.path_label.upper()
    )
    lk = compose_loss_network(path_a)
    assert len(lk) > 0, "Path A should have non-empty LossKernel"
    assert "type_guarantee" in lk, f"Expected type_guarantee in Path A LossKernel, got {lk}"


def test_h1_t37_diamond_path_b(t37):
    """Path B (SRC->L_B->TGT): LossKernel should be empty."""
    diamond = t37.diamond_network_analysis
    path_b = next(
        pa.path for pa in diamond.path_admissibilities
        if "L_B" in pa.path.layer_names or "B" in pa.path_label.upper()
    )
    lk = compose_loss_network(path_b)
    assert len(lk) == 0, f"Path B should have empty LossKernel, got {lk}"


def test_h1_t34_spectre_losskernel_nonempty(t34):
    """Spectre chain: composed LossKernel should be non-empty (all 4 forgotten structures)."""
    lk = compose_loss_chain(t34.spectre_chain.chain)
    assert len(lk) > 0
    assert "type_safety_guarantee" in lk


def test_h1_t34_absorbed_losskernel_nonempty(t34):
    """Absorbed chain: LossKernel non-empty despite endpoint not being PO1."""
    lk = compose_loss_chain(t34.absorbed_chain.chain)
    assert len(lk) > 0


# ---------------------------------------------------------------------------
# H2: Lax-functorial (monotone)
# ---------------------------------------------------------------------------


def test_h2_lax_functorial(t37, t34):
    result = verify_h2(t37, t34)
    assert result["h2_passes"], (
        f"H2 monotonicity failed: "
        f"{[(k, v) for k, v in result['checks'].items() if not v['monotone']]}"
    )


def test_h2_identity_losskernel_empty():
    """Identity morphism (empty path) has LossKernel = frozenset()."""
    from models.transport_network import NetworkPath
    empty_path = NetworkPath(
        layer_names=("A",),
        transports=(),
        source_name="A",
        target_name="A",
    )
    lk = compose_loss_network(empty_path)
    assert lk == frozenset(), f"Identity path should have empty LossKernel, got {lk}"


def test_h2_monotone_prefix_growth(t37):
    """Each prefix of a multi-step path has LossKernel ⊆ full LossKernel."""
    for pa in t37.spectre_network_analysis.path_admissibilities:
        full_lk = compose_loss_network(pa.path)
        acc: frozenset[str] = frozenset()
        for t in pa.path.transports:
            acc = acc | frozenset(t.forgotten_structure)
            assert acc <= full_lk, (
                f"Prefix LossKernel {acc} should be subset of full LossKernel {full_lk}"
            )


# ---------------------------------------------------------------------------
# H3: Path-dependence biconditional
# ---------------------------------------------------------------------------


def test_h3_biconditional_holds(t37):
    result = verify_h3(t37)
    assert result["h3_passes"], (
        f"H3 biconditional failed: {result}"
    )


def test_h3_po1_paths_have_nonempty_losskernel(t37):
    result = verify_h3(t37)
    assert result["po1_paths_all_have_nonempty_losskernel"], (
        "All PO1-admissible paths must have non-empty LossKernel"
    )


def test_h3_non_po1_paths_have_empty_losskernel(t37):
    result = verify_h3(t37)
    assert result["non_po1_paths_all_have_empty_losskernel"], (
        "All non-PO1 paths (for fixed endpoints) must have empty LossKernel"
    )


# ---------------------------------------------------------------------------
# H4: T34 chain shapes as LossKernel patterns
# ---------------------------------------------------------------------------


def test_h4_chain_shapes(t34):
    result = verify_h4(t34)
    assert result["h4_passes"], (
        f"H4 chain shapes failed: {result}"
    )


def test_h4_emergent_nonempty_losskernel_with_ac5(t34):
    result = verify_h4(t34)
    emergent = result["emergent"]
    assert emergent["losskernel_nonempty"], "Emergent chain must have non-empty LossKernel"
    assert emergent["ac5_passes_at_endpoint"], "Emergent chain must have AC5=True at endpoint"
    assert emergent["ac6_passes_at_endpoint"], "Emergent chain must have AC6=True (obstructed target)"


def test_h4_absorbed_nonempty_losskernel_but_ac6_fails(t34):
    """Absorbed: non-empty LossKernel but AC6=False (target unobstructed) => not PO1."""
    result = verify_h4(t34)
    absorbed = result["absorbed"]
    assert absorbed["losskernel_nonempty"], "Absorbed chain has non-empty LossKernel"
    assert not absorbed["ac6_passes_at_endpoint"], (
        "Absorbed chain endpoint AC6 should FAIL (target unobstructed)"
    )
    assert absorbed["absorbed_obstruction"], "Absorbed obstruction must be confirmed"


def test_h4_stepwise_each_step_nonempty(t34):
    """Stepwise: each obstructed step contributes to LossKernel."""
    result = verify_h4(t34)
    stepwise = result["stepwise"]
    assert stepwise["losskernel_nonempty"], "Stepwise chain must have non-empty LossKernel"
    assert stepwise["stepwise_propagation"], "Stepwise propagation must be confirmed"


# ---------------------------------------------------------------------------
# Main theorem
# ---------------------------------------------------------------------------


def test_main_theorem_established(t73):
    assert t73.all_pass, (
        f"T73 main theorem not established: "
        f"H1={t73.h1['h1_passes']}, H2={t73.h2['h2_passes']}, "
        f"H3={t73.h3['h3_passes']}, H4={t73.h4['h4_passes']}"
    )


def test_losskernel_is_organizing_object(t37):
    """LossKernel determines PO1 for T37 diamond — it is the sole discriminating object."""
    diamond = t37.diamond_network_analysis
    for pa in diamond.path_admissibilities:
        lk = compose_loss_network(pa.path)
        lk_nonempty = len(lk) > 0
        # AC5 = LossKernel non-empty
        assert pa.admissibility.ac5_structure_forgotten == lk_nonempty, (
            f"Path {pa.path_label}: AC5={pa.admissibility.ac5_structure_forgotten} "
            f"but LossKernel non-empty={lk_nonempty}. These must agree."
        )
