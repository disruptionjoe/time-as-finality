"""T248 tests: the in-repo WBE/Moses coverage-axiom citation certificate (MTI sub-obj 2).

Real checks, no placeholders. The headline checks:
  - the cited quotes are LITERALLY present in the source file (a true citation,
    not a fabricated axiom) -- this is the binding honesty guard;
  - the cited axiom is stated INDEPENDENTLY of the separation it licenses;
  - the cited axiom IS the T238 terminal-reachability constraint on the finite
    fixture;
  - the falsification control is DECISIVE: drop the coverage axiom and the
    separation reverts to T227's objective-DEPENDENT verdict;
  - the certificate has the SAME structural audit shape as T243's area-preserving one;
  - the harness is NON-VACUOUS (it catches a fabricated quote and a circular
    axiom);
  - the imported T238 / T243 / T233 suites stay GREEN.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from models.mti_coverage_axiom_certificate import (
    CITATION_SOURCE,
    CITED_QUOTES,
    CoverageAxiom,
    axiom_matches_t238_constraint,
    axiom_stated_independently_of_separation,
    build_certificate,
    falsification_drop_coverage,
    feasibility_guards,
    non_vacuity_injector,
    same_shape_as_t243_audit,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def _source_text() -> str:
    src = REPO_ROOT / CITATION_SOURCE
    assert src.exists(), f"citation source missing: {src}"
    return src.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# PART A. The citation is REAL (the binding honesty guard).
# ---------------------------------------------------------------------------

def test_cited_quotes_are_literally_present_in_source():
    """Every CITED_QUOTES string must appear verbatim in the source file.
    This is what makes the axiom CITED rather than fabricated.
    """
    text = _source_text()
    for q in CITED_QUOTES:
        assert q in text, f"cited quote NOT found in source (fabricated?): {q!r}"


def test_citation_includes_the_subject_to_constraint_clause():
    """The load-bearing quote: coverage is in the WBE optimization's
    `subject to:` CONSTRAINT clause, not its objective -- i.e. constitutive.
    """
    text = _source_text()
    assert "subject to: network fills volume V" in text
    # and the repo's own equation of space-filling with terminal coverage:
    assert "Coverage requirement (all sites accessible)" in text


# ---------------------------------------------------------------------------
# PART B. The axiom is stated independently of what it licenses (non-circular).
# ---------------------------------------------------------------------------

def test_axiom_stated_independently_of_separation():
    assert axiom_stated_independently_of_separation(CoverageAxiom())


def test_circular_axiom_is_rejected():
    circular = CoverageAxiom(
        statement="coverage means the minimax objective separates Alpha and Beta"
    )
    assert not axiom_stated_independently_of_separation(circular)


# ---------------------------------------------------------------------------
# PART C. The cited axiom IS the T238 constraint on the finite fixture.
# ---------------------------------------------------------------------------

def test_cited_axiom_is_the_t238_constraint():
    m = axiom_matches_t238_constraint()
    assert m.full_coverage_is_reachable
    assert m.abandoning_a_terminal_violates
    assert m.t238_constraint_is_cov_axiom


# ---------------------------------------------------------------------------
# PART D. Falsification control -- the cited axiom is LOAD-BEARING.
# ---------------------------------------------------------------------------

def test_falsification_control_is_decisive():
    """WITH the cited coverage axiom: minimax AND total-cost separate
    (objective-invariant). WITHOUT it: only total-cost separates (T227's
    objective-DEPENDENT horn). The cited axiom is the only thing that flips
    minimax from non-separating to separating.
    """
    f = falsification_drop_coverage()
    # WITH axiom -> invariant
    assert f.with_axiom_minimax_separates
    assert f.with_axiom_totalcost_separates
    assert f.with_axiom_objective_invariant
    # WITHOUT axiom -> objective-dependent (T227 horn)
    assert f.without_axiom_totalcost_separates
    assert not f.without_axiom_minimax_separates
    assert f.without_axiom_objective_dependent
    # decisive
    assert f.control_is_decisive


def test_dropping_coverage_reverts_to_t227_minimax_horn():
    """Specifically: removing coverage makes minimax NON-separating (it zeroes
    the slow branch), which is exactly the T227 horn T238 escaped."""
    f = falsification_drop_coverage()
    assert not f.without_axiom_minimax_separates


# ---------------------------------------------------------------------------
# PART E. Same structural shape as T243.
# ---------------------------------------------------------------------------

def test_same_shape_as_t243():
    s = same_shape_as_t243_audit()
    assert s.cov_is_constitutive_constraint
    assert s.cov_stated_independently
    assert s.cov_falsification_decisive
    assert s.coverage_is_wbe_moses_premise
    assert s.both_independent_of_conclusion
    assert s.both_have_decisive_control
    assert s.same_shape_as_t243


# ---------------------------------------------------------------------------
# PART F. Non-vacuity -- the harness CAN report NOT-EARNED.
# ---------------------------------------------------------------------------

def test_non_vacuity_injector():
    nv = non_vacuity_injector()
    assert nv.fabricated_axiom_fails_citation
    assert nv.circular_axiom_fails_independence
    assert nv.harness_can_report_not_earned


def test_fabricated_quote_is_actually_absent_from_source():
    """The non-vacuity injector's fabricated quote must really NOT be in the
    source file -- otherwise the citation guard would be untestable."""
    text = _source_text()
    fabricated = "THIS EXACT STRING IS NOT IN ANY REPO FILE -- fabricated"
    assert fabricated not in text


def test_certificate_fails_when_quotes_absent():
    """If the file-read citation check fails (quotes_present_in_source=False),
    the certificate must NOT hold -- the citation is load-bearing, not cosmetic.
    """
    bad = build_certificate(quotes_present_in_source=False)
    assert not bad.certificate_holds


# ---------------------------------------------------------------------------
# PART G. Feasibility / quantum->0 guards.
# ---------------------------------------------------------------------------

def test_feasibility_guards():
    g = feasibility_guards()
    assert g.quantum_is_positive
    assert g.quantum_shrinks_toward_zero_with_fraction
    assert g.bound_below_threshold_infeasible
    assert g.bound_above_threshold_feasible


# ---------------------------------------------------------------------------
# Combined verdict.
# ---------------------------------------------------------------------------

def test_certificate_holds_with_real_citation():
    text = _source_text()
    present = all(q in text for q in CITED_QUOTES)
    cert = build_certificate(quotes_present_in_source=present)
    assert cert.quotes_present_in_source
    assert cert.axiom_stated_independently
    assert cert.axiom_is_t238_constraint
    assert cert.falsification_decisive
    assert cert.same_shape_as_t243
    assert cert.non_vacuity_ok
    assert cert.feasibility_ok
    assert cert.certificate_holds


# ---------------------------------------------------------------------------
# Imported sibling suites stay GREEN (import-only discipline).
# ---------------------------------------------------------------------------

def test_imported_t238_t243_t233_suites_stay_green():
    """The siblings this lane imports must keep passing -- we modified none of
    them. Runs their suites in a subprocess and asserts a clean exit.
    """
    res = subprocess.run(
        [
            sys.executable, "-m", "pytest", "-q",
            "tests/test_wbe_coverage_constrained.py",       # T238
            "tests/test_mti_area_preserving_exponent.py",   # T243
            "tests/test_wbe_objective_selection.py",        # T233
        ],
        cwd=str(REPO_ROOT),
        capture_output=True, text=True,
    )
    assert res.returncode == 0, (
        "imported sibling suites must stay green:\n"
        + res.stdout[-3000:] + "\n" + res.stderr[-2000:]
    )


# ---------------------------------------------------------------------------
# Emit the results JSON.
# ---------------------------------------------------------------------------

def test_emit_results_json():
    text = _source_text()
    present = all(q in text for q in CITED_QUOTES)
    cert = build_certificate(quotes_present_in_source=present)
    f = falsification_drop_coverage()
    s = same_shape_as_t243_audit()
    nv = non_vacuity_injector()
    g = feasibility_guards()
    m = axiom_matches_t238_constraint()

    out = {
        "test": "T248-mti-coverage-axiom-certificate",
        "verdict": "conditional",
        "promotes_mti": False,
        "citation": {
            "source": CITATION_SOURCE,
            "quotes_present_in_source": present,
            "quotes": list(CITED_QUOTES),
        },
        "axiom_stated_independently": cert.axiom_stated_independently,
        "axiom_is_t238_constraint": {
            "full_coverage_reachable": m.full_coverage_is_reachable,
            "abandoning_terminal_violates": m.abandoning_a_terminal_violates,
            "match": m.t238_constraint_is_cov_axiom,
        },
        "falsification_control": {
            "with_axiom_minimax_separates": f.with_axiom_minimax_separates,
            "with_axiom_totalcost_separates": f.with_axiom_totalcost_separates,
            "with_axiom_objective_invariant": f.with_axiom_objective_invariant,
            "without_axiom_totalcost_separates": f.without_axiom_totalcost_separates,
            "without_axiom_minimax_separates": f.without_axiom_minimax_separates,
            "without_axiom_objective_dependent": f.without_axiom_objective_dependent,
            "decisive": f.control_is_decisive,
        },
        "same_shape_as_t243": s.same_shape_as_t243,
        "non_vacuity": {
            "fabricated_axiom_fails_citation": nv.fabricated_axiom_fails_citation,
            "circular_axiom_fails_independence": nv.circular_axiom_fails_independence,
            "harness_can_report_not_earned": nv.harness_can_report_not_earned,
        },
        "feasibility_guards": {
            "quantum_positive": g.quantum_is_positive,
            "quantum_shrinks_with_fraction": g.quantum_shrinks_toward_zero_with_fraction,
            "below_threshold_infeasible": g.bound_below_threshold_infeasible,
            "above_threshold_feasible": g.bound_above_threshold_feasible,
        },
        "certificate_holds": cert.certificate_holds,
        "tags": ["finite_witness", "poly_decider"],
    }

    out_dir = REPO_ROOT / "results" / "mti-coverage-axiom"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "T248-results.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8"
    )
    assert out["certificate_holds"]


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
