from functools import lru_cache

from models import m2_threshold_index_leakage_gate as t427


@lru_cache(maxsize=1)
def artifact():
    return t427.run()


def channel(name):
    return artifact()["universe"]["channel_reports"][name]


def test_t426_high_quota_positive_cells_are_reproduced():
    cells = {
        (cell["rule"], cell["n"]): cell
        for cell in artifact()["universe"]["cell_reports"]
    }

    assert artifact()["universe"]["n_profiles"] == 2560
    assert artifact()["universe"]["separator_profiles"] == 32

    assert cells[("three_quarters", 4)]["separator_profiles"] == 12
    assert cells[("four_fifths", 5)]["separator_profiles"] == 20
    assert cells[("three_quarters", 5)]["separator_profiles"] == 0
    assert cells[("four_fifths", 4)]["separator_profiles"] == 0


def test_support_alone_is_not_stable_across_adjacent_quota_controls():
    report = channel("support_only")

    assert report["perfectly_predicts_separator"] is False
    assert report["guardrail_verdict"] == "FAILS_SEPARATOR"
    assert report["n_collision_values"] == 2
    assert {tuple(example["value"]) for example in report["collision_examples"]} == {
        (0, 1, 1, 2),
        (0, 1, 1, 3),
    }


def test_only_quota_support_leaks_perfectly_predict_separator():
    leaking = artifact()["universe"]["leaking_perfect_channels"]

    assert leaking == [
        "cell_local_support",
        "support_plus_quota_step",
        "quota_margin_signature",
    ]
    assert channel("quota_margin_signature")["separator_only_values"] == [
        {
            "value": [0, 0, -1, 0],
            "separator_0": 0,
            "separator_1": 32,
        }
    ]


def test_graph_index_channels_collide_with_nonseparators():
    expected = {
        "crossing_count": 1,
        "compatibility_cycle_rank": 2,
        "signed_frustration_index": 1,
        "graph_index_triple": 2,
    }

    for name, collisions in expected.items():
        report = channel(name)
        assert report["channel_type"] == "candidate_index"
        assert report["perfectly_predicts_separator"] is False
        assert report["guardrail_verdict"] == "FAILS_SEPARATOR"
        assert report["n_collision_values"] == collisions


def test_overall_verdict_blocks_threshold_index_reading():
    verdict = artifact()["overall_verdict"]

    assert artifact()["universe"]["clean_candidate_channels"] == []
    assert verdict["verdict"] == "REDESIGN_THRESHOLD_INDEX_LEAKAGE"
    assert "finite threshold testbeds" in verdict["reading"]
