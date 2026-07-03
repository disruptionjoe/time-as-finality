from functools import lru_cache

from models import m2_support_completion_closure_gate as t430


@lru_cache(maxsize=1)
def artifact():
    return t430.run()


def certificate(branch):
    return next(
        cert for cert in artifact()["certificates"]
        if cert["branch"] == branch
    )


def test_source_artifacts_are_t425_through_t429_only():
    assert artifact()["source_artifacts"] == {
        "T425": "results/T425-m2-size-sweep-absorption-gate-v0.1-results.md",
        "T426": "results/T426-m2-threshold-rule-rescue-gate-v0.1-results.md",
        "T427": "results/T427-m2-threshold-index-leakage-gate-v0.1-results.md",
        "T428": "results/T428-m2-nonquota-aggregation-family-gate-v0.1-results.md",
        "T429": "results/T429-m2-separator-object-support-gate-v0.1-results.md",
    }


def test_inherited_strict_majority_branch_closes_by_larger_absorption():
    cert = certificate("inherited_strict_majority_size_sweep")

    assert cert["closed"] is True
    assert cert["closure_status"] == "closed_no_larger_target"
    assert cert["evidence"]["n3_separator_profiles"] == 6
    assert cert["evidence"]["n4_separator_profiles"] == 0
    assert cert["evidence"]["n5_separator_profiles"] == 0
    assert cert["evidence"]["n4_larger_absorption_complete"] is True
    assert cert["evidence"]["n5_larger_absorption_complete"] is True


def test_threshold_branch_closes_by_support_and_quota_leakage():
    cert = certificate("threshold_rule_and_index_followup")

    assert cert["closed"] is True
    assert cert["closure_status"] == "closed_threshold_support_leakage"
    assert cert["evidence"]["stable_fixed_quota_rules"] == []
    assert cert["evidence"]["clean_candidate_channels"] == []
    assert cert["evidence"]["separator_profiles_in_index_universe"] == 32
    assert cert["evidence"]["leaking_perfect_channels"] == [
        "cell_local_support",
        "support_plus_quota_step",
        "quota_margin_signature",
    ]


def test_nonquota_selector_branch_closes_by_full_support_completion():
    cert = certificate("nonquota_full_judgment_selectors")

    assert cert["closed"] is True
    assert cert["closure_status"] == "closed_full_support_completion"
    assert cert["evidence"]["stable_larger_n_families"] == []
    assert cert["evidence"]["support_leak_clean"] is True
    assert [cell["family"] for cell in cert["evidence"]["larger_positive_cells"]] == [
        "plurality_reject",
        "minimax_reject",
    ]


def test_separator_object_branch_closes_by_ambient_support_completion():
    cert = certificate("separator_object_family")

    assert cert["closed"] is True
    assert cert["closure_status"] == "closed_ambient_support_completion"
    assert cert["evidence"]["clean_stable_families"] == []
    assert cert["evidence"]["any_support_mixed"] is False
    assert cert["evidence"]["stable_larger_families"] == [
        {
            "family": "ambient_even_support_shape",
            "object_class": "ambient_size_support_predicate",
            "uses_ambient_size": True,
            "n4_separator_profiles": 24,
            "n5_separator_profiles": 240,
            "support_fiber_mixed_separator_count": 0,
        }
    ]


def test_overall_verdict_closes_bounded_support_family_without_claim_promotion():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == "REDESIGN_M2_BOUNDED_SUPPORT_COMPLETION_CLOSURE"
    assert verdict["open_branches"] == []
    assert set(verdict["closed_branches"]) == {
        "inherited_strict_majority_size_sweep",
        "threshold_rule_and_index_followup",
        "nonquota_full_judgment_selectors",
        "separator_object_family",
    }
    assert "bounded AND-doctrine M2 universe" in verdict["reading"]
    assert "no-completion controls" in verdict["next_gate"]
    assert "not a universal no-go theorem" in artifact()["honest_ceiling"]
