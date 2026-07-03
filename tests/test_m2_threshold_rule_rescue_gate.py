from functools import lru_cache

from models import m2_threshold_rule_rescue_gate as t426


@lru_cache(maxsize=1)
def artifact():
    return t426.run()


def cell(rule, n):
    return artifact()["rule_reports"][rule][str(n)]


def test_strict_majority_regression_matches_t425():
    assert artifact()["overall_verdict"]["strict_majority_regression_ok"] is True

    assert cell("strict_majority", 3)["verdict_distribution"] == {
        "no-separation": 58,
        "SURVIVES-R1": 6,
    }
    assert cell("strict_majority", 4)["verdict_distribution"] == {
        "no-separation": 196,
        "ABSORBED": 60,
    }
    assert cell("strict_majority", 5)["verdict_distribution"] == {
        "no-separation": 634,
        "ABSORBED": 390,
    }


def test_weak_half_absorbs_every_nonzero_gap():
    for n in (3, 4, 5):
        report = cell("weak_half", n)
        assert report["separator_profiles"] == 0
        assert report["absorbed_profiles"] == report["nonzero_gap_profiles"]
        assert set(report["min_sep_size_distribution"]) <= {"none", "2"}


def test_size_matched_high_quotas_create_grand_targets():
    q34_n4 = cell("three_quarters", 4)
    q45_n5 = cell("four_fifths", 5)

    assert q34_n4["separator_profiles"] == 12
    assert q34_n4["min_sep_size_distribution"] == {"none": 244, "4": 12}
    assert q34_n4["size_matched_high_quota_shape"] is True

    assert q45_n5["separator_profiles"] == 20
    assert q45_n5["min_sep_size_distribution"] == {"none": 1004, "5": 20}
    assert q45_n5["size_matched_high_quota_shape"] is True


def test_no_fixed_quota_is_stable_across_n4_and_n5():
    verdict = artifact()["overall_verdict"]

    assert verdict["stable_fixed_quota_rules"] == []
    assert cell("three_quarters", 5)["separator_profiles"] == 0
    assert cell("four_fifths", 4)["separator_profiles"] == 0


def test_overall_verdict_is_size_matched_threshold_only():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == "RECHECK_SIZE_MATCHED_THRESHOLD_ONLY"
    assert verdict["survivor_cells"] == [
        {
            "rule": "three_quarters",
            "label": "3/4 quota",
            "n": 4,
            "separator_profiles": 12,
            "min_sep_size_distribution": {"none": 244, "4": 12},
            "size_matched_high_quota_shape": True,
        },
        {
            "rule": "four_fifths",
            "label": "4/5 quota",
            "n": 5,
            "separator_profiles": 20,
            "min_sep_size_distribution": {"none": 1004, "5": 20},
            "size_matched_high_quota_shape": True,
        },
    ]
