"""Tests for T392: Fixed-SBS-Key Reversal Divergence Witness.

Asserts, to numerical precision, the six items of the witness:

1. Full ordinary event-level record identical between preparations A and B.
2. SBS-importable closure keys (repo's T162 definition) identical between A/B.
3. Reversal divergence: A restores X-visibility after undo, B does not.
4. Typed axis H (reversal cost) finite for A, infinite for B; verdict split,
   both classes populated (T150 support).
5. Screening-off failure certificate: positive Bayes-risk lift from the
   auxiliary channel over the full ordinary record, across a finite loss
   family (T155), plus conditional mutual information I(V ; aux | R) > 0.
6. Null controls: a downstream-transform auxiliary channel gives zero lift
   (T137 null class), and preparation B' (A0 copies nothing) shows zero
   divergence from A on every metric (T198-style).
"""

from __future__ import annotations

import math

import numpy as np

from models.fixed_sbs_key_reversal_divergence import (
    FRAGMENT_QUBITS,
    V_STAR,
    d1_finalized_from_key,
    declared_conditional_state,
    dominant_meter_outcome,
    ordinary_record_distribution,
    prepare,
    reversal_cost,
    reversal_report,
    run_analysis,
    sbs_closure_key,
    screening_certificate,
    typed_axis_H,
    verdict_map,
    visibility_after_undo,
)

TOL = 1e-12


# --------------------------------------------------------------------------- #
# (1) Ordinary-record equality
# --------------------------------------------------------------------------- #

def test_ordinary_event_level_record_identical():
    psi_a = prepare("A")
    psi_b = prepare("B")
    rec_a = ordinary_record_distribution(psi_a)
    rec_b = ordinary_record_distribution(psi_b)
    keys = set(rec_a) | set(rec_b)
    assert keys, "record must be nonempty"
    for key in keys:
        assert abs(rec_a.get(key, 0.0) - rec_b.get(key, 0.0)) <= TOL


def test_ordinary_record_is_a_normalized_distribution():
    for kind in ("A", "B"):
        dist = ordinary_record_distribution(prepare(kind))
        assert abs(sum(dist.values()) - 1.0) <= TOL


# --------------------------------------------------------------------------- #
# (2) SBS closure-key equality (repo's T162 definition)
# --------------------------------------------------------------------------- #

def test_sbs_closure_keys_identical():
    key_a = sbs_closure_key(prepare("A"))
    key_b = sbs_closure_key(prepare("B"))
    assert key_a.as_tuple() == key_b.as_tuple()


def test_sbs_key_is_finalized_and_uses_repo_threshold():
    # Both preparations must present a genuinely finalized objective record,
    # so the reversal split is not smuggled in via a non-finalized key.
    for kind in ("A", "B"):
        key = sbs_closure_key(prepare(kind))
        assert key.objectivity_status == "sbs_objective"
        assert key.partition_visible is True
        assert key.support_count == 4  # R_delta over four independent fragments
        assert d1_finalized_from_key(key) is True


# --------------------------------------------------------------------------- #
# (3) Reversal divergence
# --------------------------------------------------------------------------- #

def test_reversal_restores_visibility_for_A_not_for_B():
    rep_a = reversal_report(prepare("A"), "A")
    rep_b = reversal_report(prepare("B"), "B")
    assert rep_a.best_branch_visibility >= V_STAR
    assert rep_b.best_branch_visibility <= TOL
    assert rep_a.best_branch_visibility - rep_b.best_branch_visibility > 0.5


def test_undo_needs_the_full_accessible_set_in_A():
    # On the dominant branch, no proper accessible subset restores visibility;
    # every one of the four fragments individually holds a full Z-copy.
    psi_a = prepare("A")
    m = dominant_meter_outcome(psi_a)
    _, full = visibility_after_undo(psi_a, m, FRAGMENT_QUBITS)
    assert full >= V_STAR
    # any strict subset (size 3) must fall short
    for drop in FRAGMENT_QUBITS:
        subset = tuple(f for f in FRAGMENT_QUBITS if f != drop)
        _, vis = visibility_after_undo(psi_a, m, subset)
        assert vis < V_STAR


def test_reversal_gap_matches_analytic_value():
    # Analytic A-branch visibility = 2 cos(t/2) / (1 + cos(t/2)**2), t = pi/3.
    t = math.pi / 3.0
    c = math.cos(t / 2.0)
    expected = 2.0 * c / (1.0 + c * c)
    rep_a = reversal_report(prepare("A"), "A")
    assert abs(rep_a.best_branch_visibility - expected) <= 1e-9


# --------------------------------------------------------------------------- #
# (4) Typed axis H and verdict map
# --------------------------------------------------------------------------- #

def test_typed_axis_H_finite_for_A_infinite_for_B():
    h_a = typed_axis_H(prepare("A"))
    h_b = typed_axis_H(prepare("B"))
    assert math.isfinite(h_a)
    assert h_a == 4.0  # must undo all four accessible fragments
    assert math.isinf(h_b)


def test_verdict_map_splits_the_two_preparations():
    v_a = verdict_map(typed_axis_H(prepare("A")))
    v_b = verdict_map(typed_axis_H(prepare("B")))
    assert v_a == "recoverable-at-access-K"
    assert v_b == "final-relative-to-K"
    assert v_a != v_b


def test_reversal_cost_infinite_when_no_accessible_subset_reaches_vstar():
    psi_b = prepare("B")
    m = dominant_meter_outcome(psi_b)
    assert math.isinf(reversal_cost(psi_b, m, V_STAR))


def test_phi_independence_lemma_grounds_infinite_cost_in_B():
    # v0.1.1 lemma: the accessible conditional state rho_{S,F1..F4 | M=0} in
    # preparation B is EXACTLY independent of the initial S phase phi, while
    # in preparation A it is phi-dependent. Raw visibility 1.0 is achievable
    # in B by manufactured coherence (e.g. CNOT(F1->S) then H(S)), but
    # manufactured coherence carries no phi information and would trivialize
    # A equally; so H(B) = inf rests on this lemma, not on the
    # inverse-coupling protocol restriction.
    phis = (0.0, math.pi / 7.0, math.pi / 3.0, 2.0 * math.pi / 3.0, math.pi)

    def max_pairwise_diff(kind: str) -> float:
        rhos = [
            declared_conditional_state(prepare(kind, s_phase=phi), 0)
            for phi in phis
        ]
        diff = 0.0
        for i in range(len(rhos)):
            for j in range(i + 1, len(rhos)):
                diff = max(diff, float(np.max(np.abs(rhos[i] - rhos[j]))))
        return diff

    assert max_pairwise_diff("B") < 1e-12  # exact phi-independence in B
    assert max_pairwise_diff("A") > 0.1  # genuine phi-dependence in A


# --------------------------------------------------------------------------- #
# (5) Screening-off failure certificate
# --------------------------------------------------------------------------- #

def test_both_verdict_classes_populated_no_gerrymander():
    cert = screening_certificate()
    # T150: verdict is a fixed map from the typed axis, both classes have mass.
    assert cert.both_classes_populated is True
    assert len(cert.class_support) == 2
    for mass in cert.class_support.values():
        assert mass > 0.0


def test_auxiliary_channel_gives_positive_lift_across_loss_family():
    # T155: lift must hold across a finite decision family, not one loss rule.
    cert = screening_certificate()
    assert cert.all_losses_positive_lift is True
    assert len(cert.lift_by_loss) >= 3
    for name, vals in cert.lift_by_loss.items():
        assert vals["lift"] > 0.0, f"loss {name} showed no lift"


def test_conditional_mutual_information_strictly_positive():
    cert = screening_certificate()
    assert cert.cmi_positive is True
    assert cert.cmi_class1 > 0.0


# --------------------------------------------------------------------------- #
# (6) Null controls (T198-style)
# --------------------------------------------------------------------------- #

def test_downstream_transform_auxiliary_channel_has_zero_lift():
    # T137 null class: an auxiliary channel that is a downstream transform of
    # the ordinary record must add nothing.
    cert = screening_certificate()
    assert cert.null_all_zero_lift is True
    for name, vals in cert.null_lift_by_loss.items():
        assert abs(vals["lift"]) <= TOL, f"null loss {name} leaked lift"
    assert abs(cert.null_cmi) <= TOL


def test_bprime_shows_zero_divergence_from_A():
    psi_a = prepare("A")
    psi_bp = prepare("Bprime")
    assert np.allclose(psi_a, psi_bp, atol=TOL)
    from models.fixed_sbs_key_reversal_divergence import bprime_zero_divergence

    checks = bprime_zero_divergence()
    assert checks["statevector_identical"] is True
    assert checks["records_equal"] is True
    assert checks["sbs_keys_equal"] is True
    assert checks["reversal_equal"] is True
    assert checks["H_equal"] is True


# --------------------------------------------------------------------------- #
# Top-level verdict
# --------------------------------------------------------------------------- #

def test_witness_holds_end_to_end():
    result = run_analysis()
    assert result.ordinary_records_equal is True
    assert result.sbs_keys_equal is True
    assert result.visibility_gap > 0.5
    assert result.verdict_A != result.verdict_B
    assert result.screening.all_losses_positive_lift is True
    assert result.screening.cmi_positive is True
    assert result.screening.null_all_zero_lift is True
    assert result.bprime["statevector_identical"] is True
    assert result.witness_holds is True


def test_witness_language_is_restrained_house_vocabulary():
    result = run_analysis()
    text = result.verdict_language.lower()
    # House discipline: never "proves"; must say "finite" and scope to family.
    assert "prove" not in text
    assert "finite" in text
