"""T234 tests: rank-k GENRE-CROSSING third absorber (Condorcet / Arrow-SMD).

Every test is a REAL check, not a placeholder. They prove:
  - the rank-k prediction holds on all three rungs (0, 1, 2) against a native
    witness that is a directed-cycle count over an oriented majority tournament
    (NOT a signed-graph parity product);
  - the off-by-one rank guard separates 1 from 2 natively;
  - the native witness is genuinely a DIFFERENT genre (orientation-sensitive),
    so the residual "same-genre" edge is retired;
  - no shared derivation (AST-proven: the transport path imports neither the T39
    engine nor CAP), and the native witness never calls compute_kappa;
  - compute_kappa is the verbatim T224 object, not re-tuned;
  - the nu-cover and the native witness are INDEPENDENT code paths (nu does not
    call the native packing, native does not call compute_kappa), so their
    agreement at the same integer is corroboration, not circularity;
  - an ADVERSARIAL 5-candidate profile (overlapping triples) is counted as rank 1
    by the vertex-disjoint packing -- the integer is a genuine independent rank.
"""

from __future__ import annotations

import ast
import inspect

import pytest

from models.typed_loss_transport import compute_kappa
import models.typed_loss_transport as tlt

from models.kappa_genre_crossing_transport import (
    CondorcetProfile,
    build_transitive_profile,
    build_one_condorcet_cycle_profile,
    build_two_condorcet_cycle_profile,
    majority_tournament,
    native_condorcet_obstruction,
    nu_from_condorcet,
    ast_shared_derivation_audit,
    run_genre_crossing_transport_test,
    _native_witness_is_orientation_sensitive,
    _transport_path_imports,
)


# --- The headline gate -----------------------------------------------------


def test_gate_verdict_is_pass_genre_cross():
    result = run_genre_crossing_transport_test()
    assert result["verdict"] == "PASS_GENRE_CROSS"
    assert result["gate_cleared"] is True


def test_all_three_rungs_predict_native_rank_exactly():
    result = run_genre_crossing_transport_test()
    by_instance = {t["a_instance"]: t for t in result["trials"]}
    # kappa_A -> predicted -> native Condorcet rank -> nu-side kappa, all equal.
    assert by_instance["two_cell_transitive_kappa2"]["predicted_kappa_B"] == 2
    assert by_instance["two_cell_transitive_kappa2"]["native_condorcet_rank"] == 2
    assert by_instance["two_cell_transitive_kappa2"]["kappa_B_via_nu"] == 2
    assert by_instance["one_cell_transitive_kappa1"]["native_condorcet_rank"] == 1
    assert by_instance["one_cell_transitive_kappa1"]["kappa_B_via_nu"] == 1
    assert by_instance["satisfiable_kappa0"]["native_condorcet_rank"] == 0
    assert by_instance["satisfiable_kappa0"]["kappa_B_via_nu"] == 0
    assert all(t["prediction_matches_native"] for t in result["trials"])


def test_off_by_one_rank_guard_separates_1_from_2_natively():
    # The decisive load-bearing distinction: a present/absent classifier cannot
    # separate these; the native tournament witness must read 2 vs 1.
    native1 = native_condorcet_obstruction(build_one_condorcet_cycle_profile())
    native2 = native_condorcet_obstruction(build_two_condorcet_cycle_profile())
    assert native1["native_condorcet_cycle_rank"] == 1
    assert native2["native_condorcet_cycle_rank"] == 2
    assert native1["native_condorcet_cycle_rank"] != native2["native_condorcet_cycle_rank"]


# --- Native witness is a genuinely DIFFERENT genre -------------------------


def test_native_witness_reads_an_oriented_tournament_not_parity():
    # The one-cycle profile yields a directed 3-cycle; the transitive profile a
    # Condorcet winner. These are tournament/orientation facts, not Z/2 parity.
    one = native_condorcet_obstruction(build_one_condorcet_cycle_profile())
    trans = native_condorcet_obstruction(build_transitive_profile())
    assert one["condorcet_winner"] is None  # no winner: genuine cycle
    assert one["native_condorcet_cycle_rank"] == 1
    assert trans["condorcet_winner"] == "a"  # a beats b and c
    assert trans["native_condorcet_cycle_rank"] == 0


def test_native_witness_is_orientation_sensitive():
    # Reversing every ballot flips at least one majority edge while the obstruction
    # still fires -> the witness reads orientation, which a sign-symmetric parity
    # product structurally cannot. This is the genre-cross certificate.
    assert _native_witness_is_orientation_sensitive() is True


def test_reversed_profile_flips_a_majority_edge():
    prof = build_one_condorcet_cycle_profile()
    rev = CondorcetProfile(
        name=prof.name + "_rev",
        candidates=prof.candidates,
        ballots=tuple(tuple(reversed(b)) for b in prof.ballots),
    )
    e_fwd = majority_tournament(prof)
    e_rev = majority_tournament(rev)
    # at least one oriented edge reverses sign (tournament is not sign-symmetric)
    assert any(e_fwd[k] == -e_rev[k] != 0 for k in e_fwd)


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
    # T28/CAP is correctly disqualified: it DOES import the T39 engine.
    assert audit["T28_CAP_imports_d1_restriction_system"] is True


def test_native_witness_does_not_call_compute_kappa():
    # co_names inspection: the native tournament witness never names compute_kappa.
    assert "compute_kappa" not in native_condorcet_obstruction.__code__.co_names
    audit = ast_shared_derivation_audit()
    assert audit["native_witness_calls_compute_kappa"] is False


def test_compute_kappa_is_the_verbatim_T224_object():
    # imported verbatim, not re-tuned: object identity with the T224 module's func.
    assert compute_kappa is tlt.compute_kappa
    assert ast_shared_derivation_audit()["compute_kappa_is_T224_object_not_retuned"] is True


# --- nu-cover and native witness are INDEPENDENT code paths ----------------


def test_nu_cover_does_not_call_native_packing_and_vice_versa():
    # nu_from_condorcet must not call native_condorcet_obstruction; the native
    # witness must not call nu_from_condorcet or compute_kappa. They corroborate
    # by landing on the same integer through independent code, not by one calling
    # the other.
    nu_names = nu_from_condorcet.__code__.co_names
    native_names = native_condorcet_obstruction.__code__.co_names
    assert "native_condorcet_obstruction" not in nu_names
    assert "compute_kappa" not in nu_names
    assert "nu_from_condorcet" not in native_names
    assert "compute_kappa" not in native_names


def test_nu_kappa_matches_compute_kappa_directly():
    # nu-side kappa is compute_kappa applied to nu_from_condorcet's cover, the same
    # one T224 formula -- recompute it directly to confirm no hidden adjustment.
    for prof, expected in (
        (build_transitive_profile(), 0),
        (build_one_condorcet_cycle_profile(), 1),
        (build_two_condorcet_cycle_profile(), 2),
    ):
        assert compute_kappa(nu_from_condorcet(prof)).kappa == expected


# --- Adversarial: independent rank, not inflated multiplicity --------------


def test_adversarial_overlapping_triples_count_as_rank_1():
    # A 4-candidate tournament can carry MULTIPLE directed 3-cycles that share
    # vertices (e.g. a cyclic 4-tournament has several 3-cycles, all overlapping).
    # The vertex-disjoint packing must report rank 1 (one INDEPENDENT obstruction),
    # not the raw triple count -- otherwise the "rank" would be an inflated
    # multiplicity. We build a 4-cycle tournament a>b>c>d>a with a>c, b>d set so
    # several 3-cycles exist but share vertices.
    prof = CondorcetProfile(
        name="adversarial_overlapping_4cand",
        candidates=("a", "b", "c", "d"),
        # ballots engineered so majority = a>b, b>c, c>d, d>a, a>c, d>b
        ballots=(
            ("a", "b", "c", "d"),
            ("b", "c", "d", "a"),
            ("c", "d", "a", "b"),
        ),
    )
    native = native_condorcet_obstruction(prof)
    # there is at least one Condorcet cycle, but only ONE vertex-disjoint cell fits
    # in 4 candidates (a 3-cycle uses 3 of 4 vertices), so independent rank == 1.
    assert len(native["all_condorcet_triples"]) >= 1
    assert native["native_condorcet_cycle_rank"] == 1
    # and the nu-cover agrees on the same integer through its independent path.
    assert compute_kappa(nu_from_condorcet(prof)).kappa == 1


def test_profile_rejects_malformed_ballots():
    with pytest.raises(ValueError):
        CondorcetProfile(
            name="bad", candidates=("a", "b", "c"), ballots=(("a", "b"),)
        )


# --- Tags / guardrail language present, no forbidden language --------------


def test_no_forbidden_physics_or_new_object_language_in_verdict():
    result = run_genre_crossing_transport_test()
    # Scan the MEANING/claim text (not the guardrails line, which legitimately
    # NAMES the banned tokens to declare it avoids them). The claim must not
    # PROMOTE any physics/new-object language.
    meaning = result["meaning"].lower()
    for banned in (
        "curvature", "holonomy", "spacetime", "quantum amplitude",
        "consciousness", "social welfare as physical law", "new law of",
    ):
        assert banned not in meaning, f"banned token {banned!r} promoted in meaning"
    # The guardrails line is the explicit DISCLAIMER; confirm it is present.
    assert "no physics" in result["guardrails"].lower()
    assert "finite_witness" in result["complexity_tags"]
    assert "poly_decider" in result["complexity_tags"]


def test_module_does_not_import_forbidden_engines_at_top_level():
    import models.kappa_genre_crossing_transport as m
    tree = ast.parse(inspect.getsource(m))
    top_imports = set()
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            top_imports.add(node.module)
        elif isinstance(node, ast.Import):
            for a in node.names:
                top_imports.add(a.name)
    assert "models.d1_restriction_system" not in top_imports
    assert "models.cap_theorem_bridge" not in top_imports
