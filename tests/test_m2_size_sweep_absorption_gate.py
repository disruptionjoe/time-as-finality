"""Tests for T425 - M2 Size-Sweep Absorption Gate.

Recorded-tier; no claim promotion.

    python -m pytest tests/test_m2_size_sweep_absorption_gate.py -q
"""

import ast
import json
import sys
from pathlib import Path

from models.m2_size_sweep_absorption_gate import (
    compatibility_graph_cycle_rank,
    enumerate_profiles,
    run,
    run_size,
)


def test_import_audit_only_taf_native():
    src = Path("models/m2_size_sweep_absorption_gate.py").read_text(encoding="utf-8")
    tree = ast.parse(src)
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name.split(".")[0])

    allowed = {"__future__", "collections", "itertools", "json", "models"}
    assert imported <= allowed, imported - allowed

    forbidden = (
        "gu",
        "gu_formalization",
        "temporal_issuance",
        "ai_epistemology",
        "architecture_of_legitimacy",
    )
    for name in list(sys.modules):
        assert not any(name == f or name.startswith(f + ".") for f in forbidden), name


def test_n3_reference_matches_t424_global_no_local_datum():
    report = run_size(3)
    assert report["n_profiles"] == 64
    assert report["separator_profiles"] == 6
    assert report["verdict_distribution"]["SURVIVES-R1"] == 6
    assert report["verdict_distribution"]["no-separation"] == 58
    assert report["fiber_mixed_separator_count"] == 0
    assert report["separator_fiber_sizes"] == [6]


def test_n4_larger_size_absorbs_every_nonzero_gap():
    report = run_size(4)
    assert report["n_profiles"] == 256
    assert report["separator_profiles"] == 0
    assert report["nonzero_gap_profiles"] == 60
    assert report["verdict_distribution"]["ABSORBED"] == 60
    assert report["min_sep_size_distribution"]["3"] == 60
    assert report["larger_absorption_complete"] is True
    assert report["fiber_mixed_separator_count"] == 0


def test_n5_larger_size_absorbs_every_nonzero_gap():
    report = run_size(5)
    assert report["n_profiles"] == 1024
    assert report["separator_profiles"] == 0
    assert report["nonzero_gap_profiles"] == 390
    assert report["verdict_distribution"]["ABSORBED"] == 390
    assert report["min_sep_size_distribution"]["3"] == 390
    assert report["larger_absorption_complete"] is True
    assert report["fiber_mixed_separator_count"] == 0


def test_larger_profiles_have_cycle_structure_but_no_separator_target():
    n4 = run_size(4)
    n5 = run_size(5)
    assert n4["cycle_diagnostic"]["positive_cycle_profiles"] == 244
    assert n4["cycle_diagnostic"]["positive_cycle_profiles_without_separator"] == 244
    assert n5["cycle_diagnostic"]["positive_cycle_profiles"] == 1024
    assert n5["cycle_diagnostic"]["positive_cycle_profiles_without_separator"] == 1024

    assert compatibility_graph_cycle_rank(((0, 0), (0, 1), (1, 0), (1, 1))) >= 1


def test_overall_verdict_blocks_direct_route_a_continuation():
    out = run()
    assert out["overall_verdict"]["verdict"] == "REDESIGN"
    assert "blocked before separator-agreement" in out["overall_verdict"]["reading"]
    assert "not a direct Route-A continuation" in out["overall_verdict"]["next_gate"]


def test_run_is_deterministic_and_json_serializable():
    a = run()
    b = run()
    assert a == b
    json.dumps(a)


def test_profile_enumeration_sizes():
    assert len(enumerate_profiles(3)) == 64
    assert len(enumerate_profiles(4)) == 256
    assert len(enumerate_profiles(5)) == 1024
