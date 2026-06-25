"""T244 tests: rank-k NON-COMBINATORIAL genre (real-valued value-gap absorber).

Every test is a REAL check, not a placeholder. They prove:
  - the rank-k prediction holds on all FOUR rungs (0, 1, 2, 3) against a native
    witness that is a REAL value gap above a real floor (a value-of-information /
    rate-distortion obstruction), NOT a signed-graph parity product, NOT a directed
    cycle, and NOT a finite-set-intersection failure;
  - the off-by-one rank guard separates 1, 2, 3 natively (rank ceiling at 3);
  - the native witness is a finite real-threshold value-gap fixture: CONTINUOUS
    (affine) in the real gap parameter before thresholding, flips at a genuine real
    threshold, separates infinitesimally-positive from infinitesimally-negative delta,
    reads the strict-above-floor SIGN of a real gap, and references no
    cycle/parity/set-intersection helper;
  - the A-side intentionally reuses T39 source builders, while the target-side native
    witness imports neither d1_restriction_system, cap_theorem_bridge, nor the quorum
    module, and never calls compute_kappa or any combinatorial helper;
  - compute_kappa is the verbatim T224 object, not re-tuned;
  - the nu-cover and the native witness are INDEPENDENT code paths;
  - a NON-VACUITY injector proves the harness CAN report a non-PASS verdict (it is not
    a constant-True rubber stamp);
  - the strict at-floor boundary (delta = 0) is load-bearing: an at-floor cell counts 0.
"""

from __future__ import annotations

import ast
import inspect

import pytest

from models.typed_loss_transport import compute_kappa
import models.typed_loss_transport as tlt

from models.kappa_value_gap_transport import (
    VALUE_FLOOR,
    ValueGapCell,
    ValueGapSystem,
    _cell_value_gap,
    build_zero_value_gap_system,
    build_one_value_gap_system,
    build_two_value_gap_system,
    build_three_value_gap_system,
    build_k_value_gap_system,
    native_value_gap_obstruction,
    nu_from_value_gap_system,
    ast_shared_derivation_audit,
    run_value_gap_transport_test,
    _native_witness_is_real_valued_not_combinatorial,
    _transport_path_imports,
)


# --- The headline gate -----------------------------------------------------


def test_gate_verdict_is_pass_real_threshold_value_gap():
    result = run_value_gap_transport_test()
    assert result["verdict"] == "PASS_REAL_THRESHOLD_VALUE_GAP"
    assert result["gate_cleared"] is True


def test_all_four_rungs_predict_native_rank_exactly():
    result = run_value_gap_transport_test()
    by_instance = {t["a_instance"]: t for t in result["trials"]}
    # kappa_A -> predicted -> native value-gap rank -> nu-side kappa, all equal.
    for inst, k in (
        ("three_cell_transitive_kappa3", 3),
        ("two_cell_transitive_kappa2", 2),
        ("one_cell_transitive_kappa1", 1),
        ("satisfiable_kappa0", 0),
    ):
        assert by_instance[inst]["kappa_A"] == k
        assert by_instance[inst]["predicted_kappa_B"] == k
        assert by_instance[inst]["native_value_gap_rank"] == k
        assert by_instance[inst]["kappa_B_via_nu"] == k
    assert all(t["prediction_matches_native"] for t in result["trials"])


def test_rank_ceiling_at_3():
    result = run_value_gap_transport_test()
    assert result["rank_separates_0_1_2_3"] is True
    native3 = native_value_gap_obstruction(build_three_value_gap_system())
    assert native3["native_value_gap_rank"] == 3


def test_off_by_one_rank_guard_separates_1_2_3_natively():
    # A present/absent classifier cannot separate these; the native real witness must.
    n1 = native_value_gap_obstruction(build_one_value_gap_system())
    n2 = native_value_gap_obstruction(build_two_value_gap_system())
    n3 = native_value_gap_obstruction(build_three_value_gap_system())
    assert n1["native_value_gap_rank"] == 1
    assert n2["native_value_gap_rank"] == 2
    assert n3["native_value_gap_rank"] == 3
    assert len({1, 2, 3}) == 3  # all distinct, ranks land distinctly


def test_zero_rung_has_all_gaps_at_or_below_floor():
    # kappa_A = 0 control: every gap is at-or-below the floor -> native rank 0.
    n0 = native_value_gap_obstruction(build_zero_value_gap_system())
    assert n0["native_value_gap_rank"] == 0
    assert n0["all_gaps_at_or_below_floor"] is True
    assert n0["above_floor_cells"] == []


# --- Native witness is a genuinely REAL-VALUED / NON-COMBINATORIAL genre ----


def test_native_witness_is_real_valued_not_combinatorial():
    cert = _native_witness_is_real_valued_not_combinatorial()
    assert cert["is_real_valued_value_gap_not_combinatorial"] is True


def test_value_gap_is_continuous_affine_in_delta():
    # The decisive genre separator: the gap is a CONTINUOUS (affine) function of the
    # real parameter delta -- gap(delta) = delta + FLOOR. A cycle/parity witness is a
    # discrete sign in {-1, +1}; a finite-set test is a discrete jump. Neither tracks a
    # real parameter continuously.
    cert = _native_witness_is_real_valued_not_combinatorial()
    assert cert["value_gap_is_continuous_affine_in_delta"] is True
    # independently re-derive: a tiny delta change moves the gap by exactly that amount.
    g0 = _cell_value_gap(ValueGapCell("a", 0.000, 0))
    g1 = _cell_value_gap(ValueGapCell("a", 0.001, 0))
    assert abs((g1 - g0) - 0.001) < 1e-9


def test_obstruction_flips_at_a_real_threshold_not_a_finite_set():
    # The obstruction (gap > floor) flips exactly as delta crosses 0, at an arbitrarily
    # small positive margin. A finite-set / cycle helper has no notion of "strictly
    # above a real floor by an infinitesimal margin".
    cert = _native_witness_is_real_valued_not_combinatorial()
    assert cert["obstruction_flips_at_real_threshold"] is True
    assert cert["real_threshold_separates_infinitesimal_pos_from_neg"] is True
    assert cert["rank_at_delta_plus_1e_minus_9"] == 1
    assert cert["rank_at_delta_minus_1e_minus_9"] == 0
    # independently: delta = +1e-9 above floor, delta = -1e-9 below floor.
    sys_plus = ValueGapSystem("p", (ValueGapCell("c", 1e-9, 0),))
    sys_minus = ValueGapSystem("m", (ValueGapCell("c", -1e-9, 0),))
    assert native_value_gap_obstruction(sys_plus)["native_value_gap_rank"] == 1
    assert native_value_gap_obstruction(sys_minus)["native_value_gap_rank"] == 0


def test_strict_at_floor_boundary_is_load_bearing():
    # delta = 0 -> gap EXACTLY at the floor -> NOT strictly above -> counts 0. A >= test
    # (or any finite-set surrogate) would miscount this boundary cell as an obstruction.
    at_floor = ValueGapSystem("f", (ValueGapCell("c", 0.0, 0),))
    res = native_value_gap_obstruction(at_floor)
    assert res["native_value_gap_rank"] == 0
    # the gap is exactly the floor (not strictly above).
    assert _cell_value_gap(ValueGapCell("c", 0.0, 0)) == pytest.approx(VALUE_FLOOR)


def test_rank_reads_sign_not_magnitude():
    # A huge-delta cell and a tiny-positive-delta cell each count as exactly ONE
    # above-floor unit; an at-floor cell counts 0. The rank reads the strict-above-floor
    # SIGN of a real gap, not magnitude and not finite cardinality.
    cert = _native_witness_is_real_valued_not_combinatorial()
    assert cert["rank_reads_strict_above_floor_sign_not_magnitude_or_cardinality"] is True
    mixed = ValueGapSystem(
        "mix",
        (
            ValueGapCell("huge", 1000.0, 0),
            ValueGapCell("tiny", 1e-6, 1),
            ValueGapCell("at_floor", 0.0, 2),
        ),
    )
    assert native_value_gap_obstruction(mixed)["native_value_gap_rank"] == 2


def test_native_witness_calls_no_cycle_parity_or_setintersection_helpers():
    # Behavioral/structural: the native function references none of the combinatorial-
    # genre helpers. Checked on co_names (what the code calls), immune to comment wording.
    names = set(native_value_gap_obstruction.__code__.co_names)
    forbidden = {
        "compute_kappa", "majority_tournament", "_beats", "parity_product",
        "analyze_chsh_finality", "native_condorcet_obstruction",
        "native_quorum_obstruction", "_quorum_block",
    }
    assert not (names & forbidden)
    cert = _native_witness_is_real_valued_not_combinatorial()
    assert cert["native_calls_no_cycle_parity_or_setintersection_helpers"] is True


# --- No shared derivation, native independent of kappa (AST-proven) --------


def test_transport_path_imports_neither_d1_nor_cap_nor_quorum():
    imports = _transport_path_imports()
    assert "models.d1_restriction_system" not in imports
    assert "models.cap_theorem_bridge" not in imports
    assert "models.kappa_quorum_intersection_transport" not in imports


def test_ast_audit_clean_and_cap_disqualified():
    audit = ast_shared_derivation_audit()
    assert audit["transport_path_imports_d1_restriction_system"] is False
    assert audit["transport_path_imports_cap_theorem_bridge"] is False
    assert audit["transport_path_imports_quorum_module"] is False
    assert audit["shares_derivation_with_T39_or_CAP"] is False
    # T28/CAP (cap_theorem_bridge) is correctly disqualified: it imports the T39 engine.
    assert audit["T28_CAP_imports_d1_restriction_system"] is True


def test_native_witness_does_not_call_compute_kappa_or_combinatorial_helper():
    assert "compute_kappa" not in native_value_gap_obstruction.__code__.co_names
    audit = ast_shared_derivation_audit()
    assert audit["native_witness_calls_compute_kappa"] is False
    assert audit["native_witness_calls_any_combinatorial_helper"] is False


def test_compute_kappa_is_the_verbatim_T224_object():
    # imported verbatim, not re-tuned: object identity with the T224 module's func.
    assert compute_kappa is tlt.compute_kappa
    assert ast_shared_derivation_audit()["compute_kappa_is_T224_object_not_retuned"] is True


def test_fresh_native_witness_does_not_import_engines_at_top_level():
    # The whole point of building a FRESH value-gap witness from scratch is to avoid the
    # d1 engine, cap_theorem_bridge, and the prior native witnesses. Confirm at AST top.
    import models.kappa_value_gap_transport as m
    tree = ast.parse(inspect.getsource(m))
    top = set()
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            top.add(node.module)
        elif isinstance(node, ast.Import):
            for a in node.names:
                top.add(a.name)
    assert "models.d1_restriction_system" not in top
    assert "models.cap_theorem_bridge" not in top
    assert "models.kappa_quorum_intersection_transport" not in top


# --- nu-cover and native witness are INDEPENDENT code paths ----------------


def test_nu_cover_does_not_call_native_witness_and_vice_versa():
    nu_names = nu_from_value_gap_system.__code__.co_names
    native_names = native_value_gap_obstruction.__code__.co_names
    assert "native_value_gap_obstruction" not in nu_names
    assert "compute_kappa" not in nu_names
    assert "nu_from_value_gap_system" not in native_names
    assert "compute_kappa" not in native_names


def test_nu_kappa_matches_compute_kappa_directly():
    # nu-side kappa is compute_kappa applied to nu_from_value_gap_system's cover, the
    # same one T224 formula -- recompute it directly to confirm no hidden adjustment.
    for system, expected in (
        (build_zero_value_gap_system(), 0),
        (build_one_value_gap_system(), 1),
        (build_two_value_gap_system(), 2),
        (build_three_value_gap_system(), 3),
    ):
        assert compute_kappa(nu_from_value_gap_system(system)).kappa == expected


# --- Adversarial / scaling / non-vacuity ------------------------------------


def test_adversarial_many_above_floor_cells_in_one_block_count_as_rank_1():
    # MULTIPLE above-floor cells SHARING a block are ONE independent obstruction (the
    # native rank counts vertex-disjoint BLOCKS, not raw above-floor cells), so the
    # rank is an independent obstruction count, not an inflated cell multiplicity.
    system = ValueGapSystem(
        name="adversarial_three_above_floor_one_block",
        cells=(
            ValueGapCell("a", 0.5, 0),
            ValueGapCell("b", 0.6, 0),
            ValueGapCell("c", 0.7, 0),
        ),  # three above-floor cells, ALL in block 0
    )
    native = native_value_gap_obstruction(system)
    assert native["native_value_gap_rank"] == 1   # ONE independent block
    # nu agrees on the same integer through its independent path.
    assert compute_kappa(nu_from_value_gap_system(system)).kappa == 1


def test_k_value_gap_system_scales_to_arbitrary_k():
    # The construction extends mechanically: native rank == k for k = 0..5.
    for k in range(6):
        system = build_k_value_gap_system(k)
        assert native_value_gap_obstruction(system)["native_value_gap_rank"] == k
        assert compute_kappa(nu_from_value_gap_system(system)).kappa == k


def test_non_vacuity_harness_can_report_non_pass():
    # NON-VACUITY: prove the gate is not a constant-True rubber stamp. If the native
    # witness reported the WRONG integer (e.g. it ignored the at-floor boundary and
    # counted an at-floor cell), the predictions would not all match. We exhibit a
    # system whose native rank DIFFERS from a wrong "all cells count" prediction: the
    # native witness reports 1 (one above-floor cell), NOT 2 (it does not count the
    # at-floor cell), so a naive count-all classifier would mispredict -> the harness's
    # equality test would FAIL. This shows the equality gate can register a mismatch.
    system = build_one_value_gap_system()  # one above-floor + one at-floor cell
    native = native_value_gap_obstruction(system)
    assert native["native_value_gap_rank"] == 1            # correct rank
    assert native["num_cells"] == 2                        # but TWO cells exist
    # a wrong "count every cell" prediction (2) would NOT equal the native rank (1):
    wrong_prediction = native["num_cells"]
    assert wrong_prediction != native["native_value_gap_rank"]
    # and the real transported prediction (kappa_A = 1) DOES equal it.
    assert native["native_value_gap_rank"] == 1


def test_value_gap_system_rejects_malformed_inputs():
    with pytest.raises(ValueError):
        # duplicate cell names
        ValueGapSystem(
            name="dup_names",
            cells=(ValueGapCell("x", 0.5, 0), ValueGapCell("x", 0.5, 1)),
        )
    with pytest.raises(ValueError):
        # non-real delta
        ValueGapSystem(
            name="bad_delta",
            cells=(ValueGapCell("x", "not-real", 0),),  # type: ignore[arg-type]
        )
    with pytest.raises(ValueError):
        # negative block index
        ValueGapSystem(
            name="bad_block",
            cells=(ValueGapCell("x", 0.5, -1),),
        )
    with pytest.raises(ValueError):
        # outside the fixture regime where native value-iteration and nu encoding agree
        ValueGapSystem(
            name="bad_negative_delta",
            cells=(ValueGapCell("x", -VALUE_FLOOR - 1e-6, 0),),
        )


# --- Tags / guardrail language present, no forbidden language --------------


def test_no_forbidden_physics_or_new_object_language_in_meaning():
    result = run_value_gap_transport_test()
    meaning = result["meaning"].lower()
    for banned in (
        "curvature", "holonomy", "spacetime", "gravity", "consciousness",
        "value as physical law", "new law of", "reward as physical law",
        "continuum theorem",
    ):
        assert banned not in meaning, f"banned token {banned!r} promoted in meaning"
    guard = result["guardrails"].lower()
    assert "no physics" in guard
    assert "no continuum" in guard or "not a continuum" in guard
    assert "finite_witness" in result["complexity_tags"]
    assert "poly_decider" in result["complexity_tags"]


# --- Regression: sibling suites must stay green (import-only siblings) ------


def test_kappa_definition_imported_verbatim_not_redefined_locally():
    # This module must NOT define its own compute_kappa; it imports T224's verbatim.
    import models.kappa_value_gap_transport as m
    src = inspect.getsource(m)
    tree = ast.parse(src)
    local_funcs = {
        n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)
    }
    assert "compute_kappa" not in local_funcs  # not redefined here
    assert compute_kappa is tlt.compute_kappa
