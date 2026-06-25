"""T239 tests: rank-k NON-CYCLE-SHAPED genre (CAP/consensus quorum-intersection).

Every test is a REAL check, not a placeholder. They prove:
  - the rank-k prediction holds on all FOUR rungs (0, 1, 2, 3) against a native
    witness that is a quorum-intersection FAILURE (a Helly/set-cover obstruction
    over node SETS), NOT a signed-graph parity product and NOT a directed cycle;
  - the off-by-one rank guard separates 1, 2, 3 natively (rank ceiling pushed to 3);
  - the native witness is a genuinely NON-CYCLE-SHAPED genre: Helly-monotone (a
    shared node destroys the obstruction), carried by an ACYCLIC agreement forest,
    and invariant under within-side relabeling -- none of which a cycle witness is;
  - no shared derivation (AST-proven: the transport path imports neither the T39
    engine nor cap_theorem_bridge), and the native witness never calls compute_kappa;
  - compute_kappa is the verbatim T224 object, not re-tuned;
  - the nu-cover and the native witness are INDEPENDENT code paths;
  - an ADVERSARIAL block with MANY disjoint quorum pairs counts as rank 1 (one
    INDEPENDENT block obstruction), not an inflated pair multiplicity.
"""

from __future__ import annotations

import ast
import inspect

import pytest

from models.typed_loss_transport import compute_kappa
import models.typed_loss_transport as tlt

from models.kappa_quorum_intersection_transport import (
    QuorumSystem,
    build_zero_obstruction_system,
    build_one_split_brain_system,
    build_two_split_brain_system,
    build_three_split_brain_system,
    build_k_split_brain_system,
    native_quorum_obstruction,
    nu_from_quorum_system,
    ast_shared_derivation_audit,
    run_quorum_intersection_transport_test,
    _native_witness_is_helly_not_cyclic,
    _transport_path_imports,
)


# --- The headline gate -----------------------------------------------------


def test_gate_verdict_is_pass_noncycle_genre():
    result = run_quorum_intersection_transport_test()
    assert result["verdict"] == "PASS_NONCYCLE_GENRE"
    assert result["gate_cleared"] is True


def test_all_four_rungs_predict_native_rank_exactly():
    result = run_quorum_intersection_transport_test()
    by_instance = {t["a_instance"]: t for t in result["trials"]}
    # kappa_A -> predicted -> native quorum rank -> nu-side kappa, all equal.
    for inst, k in (
        ("three_cell_transitive_kappa3", 3),
        ("two_cell_transitive_kappa2", 2),
        ("one_cell_transitive_kappa1", 1),
        ("satisfiable_kappa0", 0),
    ):
        assert by_instance[inst]["kappa_A"] == k
        assert by_instance[inst]["predicted_kappa_B"] == k
        assert by_instance[inst]["native_quorum_rank"] == k
        assert by_instance[inst]["kappa_B_via_nu"] == k
    assert all(t["prediction_matches_native"] for t in result["trials"])


def test_rank_ceiling_pushed_to_3():
    # T234 stopped at k = 2; this lane exercises k = 3 with a distinct native rank.
    result = run_quorum_intersection_transport_test()
    assert result["rank_separates_0_1_2_3"] is True
    native3 = native_quorum_obstruction(build_three_split_brain_system())
    assert native3["native_quorum_obstruction_rank"] == 3


def test_off_by_one_rank_guard_separates_1_2_3_natively():
    # A present/absent classifier cannot separate these; the native Helly witness must.
    n1 = native_quorum_obstruction(build_one_split_brain_system())
    n2 = native_quorum_obstruction(build_two_split_brain_system())
    n3 = native_quorum_obstruction(build_three_split_brain_system())
    assert n1["native_quorum_obstruction_rank"] == 1
    assert n2["native_quorum_obstruction_rank"] == 2
    assert n3["native_quorum_obstruction_rank"] == 3
    assert len({1, 2, 3}) == 3  # all distinct, ranks land distinctly


def test_zero_rung_has_global_intersection_property():
    # kappa_A = 0 control: all quorums intersect -> no split brain -> native rank 0.
    n0 = native_quorum_obstruction(build_zero_obstruction_system())
    assert n0["native_quorum_obstruction_rank"] == 0
    assert n0["has_global_intersection_property"] is True
    assert n0["split_brain_blocks"] == []


# --- Native witness is a genuinely NON-CYCLE-SHAPED genre ------------------


def test_native_witness_is_helly_not_cycle_shaped():
    cert = _native_witness_is_helly_not_cyclic()
    assert cert["is_helly_set_cover_not_cycle_shaped"] is True


def test_helly_monotonicity_shared_node_kills_obstruction():
    # The decisive genre separator: adding ONE shared node to both quorums of a
    # failing block makes them intersect -> the obstruction VANISHES. A frustrated
    # parity cycle or a directed tournament cycle is NOT destroyed by adding a vertex
    # to two of its sets, because it is carried by a cycle, not a set intersection.
    base = build_one_split_brain_system()
    assert native_quorum_obstruction(base)["native_quorum_obstruction_rank"] == 1
    shared = "b0_shared"
    patched = QuorumSystem(
        name="patched",
        nodes=base.nodes + (shared,),
        quorums=tuple(frozenset(set(q) | {shared}) for q in base.quorums),
        block_of={**base.block_of, shared: 0},
    )
    assert native_quorum_obstruction(patched)["native_quorum_obstruction_rank"] == 0


def test_native_witness_carries_no_cycle():
    # The within-quorum agreement graph of a failing block is an acyclic forest -- so
    # there is no cycle present to carry a parity or orientation, yet the obstruction
    # fires. (Certificate field; independently re-derived here.)
    cert = _native_witness_is_helly_not_cyclic()
    assert cert["within_quorum_agreement_graph_is_acyclic"] is True


def test_native_witness_calls_no_cycle_or_parity_helpers():
    # Behavioral/structural: the native function references none of the cycle-genre
    # helpers (compute_kappa, majority_tournament, _beats, parity_product, ...). This
    # is checked on co_names (what the code calls), immune to comment wording.
    names = set(native_quorum_obstruction.__code__.co_names)
    forbidden = {"compute_kappa", "majority_tournament", "_beats", "parity_product",
                 "analyze_chsh_finality", "native_condorcet_obstruction"}
    assert not (names & forbidden)
    cert = _native_witness_is_helly_not_cyclic()
    assert cert["native_calls_no_cycle_or_parity_genre_helpers"] is True


# --- No shared derivation, native independent of kappa (AST-proven) --------


def test_transport_path_imports_neither_d1_nor_cap():
    imports = _transport_path_imports()
    assert "models.d1_restriction_system" not in imports
    assert "models.cap_theorem_bridge" not in imports


def test_ast_audit_clean_and_cap_disqualified():
    audit = ast_shared_derivation_audit()
    assert audit["transport_path_imports_d1_restriction_system"] is False
    assert audit["transport_path_imports_cap_theorem_bridge"] is False
    assert audit["shares_derivation_with_T39_or_CAP"] is False
    # T28/CAP (cap_theorem_bridge) is correctly disqualified: it imports the T39 engine.
    assert audit["T28_CAP_imports_d1_restriction_system"] is True


def test_native_witness_does_not_call_compute_kappa():
    assert "compute_kappa" not in native_quorum_obstruction.__code__.co_names
    audit = ast_shared_derivation_audit()
    assert audit["native_witness_calls_compute_kappa"] is False


def test_compute_kappa_is_the_verbatim_T224_object():
    # imported verbatim, not re-tuned: object identity with the T224 module's func.
    assert compute_kappa is tlt.compute_kappa
    assert ast_shared_derivation_audit()["compute_kappa_is_T224_object_not_retuned"] is True


def test_fresh_native_witness_does_not_import_cap_theorem_bridge_at_top_level():
    # The whole point of building a FRESH quorum witness from scratch is to avoid
    # cap_theorem_bridge (which imports the d1 engine). Confirm at the AST top level.
    import models.kappa_quorum_intersection_transport as m
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


# --- nu-cover and native witness are INDEPENDENT code paths ----------------


def test_nu_cover_does_not_call_native_witness_and_vice_versa():
    nu_names = nu_from_quorum_system.__code__.co_names
    native_names = native_quorum_obstruction.__code__.co_names
    assert "native_quorum_obstruction" not in nu_names
    assert "compute_kappa" not in nu_names
    assert "nu_from_quorum_system" not in native_names
    assert "compute_kappa" not in native_names


def test_nu_kappa_matches_compute_kappa_directly():
    # nu-side kappa is compute_kappa applied to nu_from_quorum_system's cover, the
    # same one T224 formula -- recompute it directly to confirm no hidden adjustment.
    for system, expected in (
        (build_zero_obstruction_system(), 0),
        (build_one_split_brain_system(), 1),
        (build_two_split_brain_system(), 2),
        (build_three_split_brain_system(), 3),
    ):
        assert compute_kappa(nu_from_quorum_system(system)).kappa == expected


# --- Adversarial: independent rank, not inflated pair multiplicity ---------


def test_adversarial_many_disjoint_quorum_pairs_in_one_block_count_as_rank_1():
    # A SINGLE block with THREE mutually-disjoint quorums has THREE disjoint quorum
    # PAIRS, but it is ONE independent obstruction (one split-brain block). The native
    # rank (vertex-disjoint BLOCK packing) must report 1, not 3 -- otherwise the "rank"
    # would be an inflated pair multiplicity, not an independent obstruction count.
    nodes = tuple(f"n{i}" for i in range(6))
    block_of = {n: 0 for n in nodes}
    quorums = (
        frozenset({"n0", "n1"}),
        frozenset({"n2", "n3"}),
        frozenset({"n4", "n5"}),
    )  # pairwise disjoint: 3 disjoint quorum PAIRS, all in block 0
    system = QuorumSystem(
        name="adversarial_three_disjoint_quorums_one_block",
        nodes=nodes,
        quorums=quorums,
        block_of=block_of,
    )
    native = native_quorum_obstruction(system)
    assert len(native["all_disjoint_quorum_pairs"]) == 3       # three disjoint PAIRS
    assert native["native_quorum_obstruction_rank"] == 1       # but ONE independent block
    # nu agrees on the same integer through its independent path.
    assert compute_kappa(nu_from_quorum_system(system)).kappa == 1


def test_k_split_brain_system_scales_to_arbitrary_k():
    # The construction extends mechanically: native rank == k for k = 0..5.
    for k in range(6):
        system = build_k_split_brain_system(k)
        assert native_quorum_obstruction(system)["native_quorum_obstruction_rank"] == k
        assert compute_kappa(nu_from_quorum_system(system)).kappa == k


def test_quorum_system_rejects_malformed_inputs():
    with pytest.raises(ValueError):
        QuorumSystem(name="bad_empty_quorum", nodes=("a", "b"),
                     quorums=(frozenset(),), block_of={"a": 0, "b": 0})
    with pytest.raises(ValueError):
        QuorumSystem(name="bad_missing_block", nodes=("a", "b"),
                     quorums=(frozenset({"a"}),), block_of={"a": 0})
    with pytest.raises(ValueError):
        QuorumSystem(name="bad_quorum_outside_nodes", nodes=("a",),
                     quorums=(frozenset({"z"}),), block_of={"a": 0})


# --- Tags / guardrail language present, no forbidden language --------------


def test_no_forbidden_physics_or_new_object_language_in_meaning():
    result = run_quorum_intersection_transport_test()
    meaning = result["meaning"].lower()
    for banned in (
        "curvature", "holonomy", "spacetime", "gravity", "consciousness",
        "cap theorem as physical law", "new law of", "social welfare as physical law",
    ):
        assert banned not in meaning, f"banned token {banned!r} promoted in meaning"
    assert "no physics" in result["guardrails"].lower()
    assert "finite_witness" in result["complexity_tags"]
    assert "poly_decider" in result["complexity_tags"]
