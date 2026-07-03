from functools import lru_cache

from models import m2_separator_object_support_gate as t429


@lru_cache(maxsize=1)
def artifact():
    return t429.run()


def family(name):
    return next(
        report for report in artifact()["object_family_reports"]
        if report["family"]["name"] == name
    )


def cell(name, n):
    return family(name)["size_reports"][str(n)]


def test_predeclared_separator_object_family_is_fixed():
    names = {report["family"]["name"] for report in artifact()["object_family_reports"]}

    assert names == {
        "full_support_seen",
        "both_cross_diagonals_seen",
        "compatibility_cycle_positive",
        "signed_frustration_positive",
        "crossing_count_exactly_one",
        "support_two_two",
        "support_2111",
        "ambient_even_support_shape",
    }


def test_full_support_separator_is_size_local_then_absorbed():
    assert cell("full_support_seen", 4)["separator_profiles"] == 24
    assert cell("full_support_seen", 5)["separator_profiles"] == 0
    assert cell("full_support_seen", 5)["absorbed_profiles"] == 240


def test_graph_style_separator_objects_do_not_give_stable_larger_target():
    assert cell("compatibility_cycle_positive", 4)["separator_profiles"] == 24
    assert cell("compatibility_cycle_positive", 5)["separator_profiles"] == 0
    assert cell("compatibility_cycle_positive", 5)["absorbed_profiles"] == 1024

    assert cell("signed_frustration_positive", 4)["separator_profiles"] == 0
    assert cell("crossing_count_exactly_one", 4)["separator_profiles"] == 0


def test_only_ambient_even_support_shape_is_stable_across_larger_sizes():
    verdict = artifact()["overall_verdict"]

    assert verdict["stable_larger_families"] == [
        {
            "family": "ambient_even_support_shape",
            "object_class": "ambient_size_support_predicate",
            "uses_ambient_size": True,
            "n4_separator_profiles": 24,
            "n5_separator_profiles": 240,
            "support_fiber_mixed_separator_count": 0,
        }
    ]
    assert family("ambient_even_support_shape")["ambient_even_shape_by_size"] == {
        "3": [0, 1, 1, 1],
        "4": [1, 1, 1, 1],
        "5": [1, 1, 1, 2],
    }


def test_every_tested_separator_is_support_determined():
    for report in artifact()["object_family_reports"]:
        for size_report in report["size_reports"].values():
            assert size_report["support_fiber_mixed_separator_count"] == 0
            assert size_report["support_fiber_mixed_examples"] == []


def test_overall_verdict_blocks_separator_object_branch():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == "REDESIGN_SEPARATOR_SUPPORT_COMPLETION"
    assert verdict["clean_stable_families"] == []
    assert verdict["any_support_mixed"] is False
    assert "support/ambient-size completion artifacts" in verdict["reading"]
