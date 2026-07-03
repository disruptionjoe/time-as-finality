from functools import lru_cache

from models import m2_nonquota_aggregation_family_gate as t428


@lru_cache(maxsize=1)
def artifact():
    return t428.run()


def family(name):
    return next(
        report for report in artifact()["selector_family_reports"]
        if report["family"]["name"] == name
    )


def cell(name, n):
    return family(name)["size_reports"][str(n)]


def test_baseline_reproduces_inherited_m2_size_pattern():
    baseline = artifact()["baseline"]["size_reports"]

    assert baseline["3"]["separator_profiles"] == 6
    assert baseline["4"]["separator_profiles"] == 0
    assert baseline["5"]["separator_profiles"] == 0
    assert baseline["4"]["absorbed_profiles"] == 60
    assert baseline["5"]["absorbed_profiles"] == 390


def test_all_selected_families_are_nonquota_full_judgment_selectors():
    families = [report["family"] for report in artifact()["selector_family_reports"]]

    assert {family["name"] for family in families} == {
        "plurality_reject",
        "plurality_accept",
        "kemeny_reject",
        "kemeny_accept",
        "minimax_reject",
        "minimax_accept",
    }
    assert all(family["family_class"] == "full_judgment_selector" for family in families)
    assert all(family["issue_quota_rule"] is False for family in families)


def test_kemeny_reject_collapses_to_premise_completion():
    for n in (3, 4, 5):
        report = cell("kemeny_reject", n)
        assert report["separator_profiles"] == 0
        assert report["nonzero_gap_profiles"] == 0
        assert report["verdict_distribution"] == {"no-separation": 4 ** n}


def test_nonquota_larger_positives_are_size_local_only():
    verdict = artifact()["overall_verdict"]

    assert verdict["stable_larger_n_families"] == []
    assert verdict["larger_positive_cells"] == [
        {
            "family": "plurality_reject",
            "n": 4,
            "separator_profiles": 24,
            "support_fiber_mixed_separator_count": 0,
            "min_sep_size_distribution": {"none": 172, "3": 60, "4": 24},
        },
        {
            "family": "minimax_reject",
            "n": 4,
            "separator_profiles": 24,
            "support_fiber_mixed_separator_count": 0,
            "min_sep_size_distribution": {"none": 166, "3": 66, "4": 24},
        },
    ]
    assert cell("plurality_reject", 5)["separator_profiles"] == 0
    assert cell("minimax_reject", 5)["separator_profiles"] == 0


def test_every_selector_separator_is_full_support_determined():
    for report in artifact()["selector_family_reports"]:
        for size_report in report["size_reports"].values():
            assert size_report["support_fiber_mixed_separator_count"] == 0
            assert size_report["support_fiber_mixed_examples"] == []


def test_overall_verdict_blocks_nonquota_selector_rescue():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == "REDESIGN_NONQUOTA_SELECTOR_COMPLETION"
    assert verdict["support_leak_clean"] is True
    assert "selector/full-support completion" in verdict["reading"]
