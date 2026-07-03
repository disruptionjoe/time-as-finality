from functools import lru_cache

from models import m2_independent_channel_admission_gate as t431


@lru_cache(maxsize=1)
def artifact():
    return t431.run()


def channel(name):
    return next(
        report for report in artifact()["channel_reports"]
        if report["name"] == name
    )


def test_source_artifacts_are_t424_and_t430_only():
    assert artifact()["source_artifacts"] == {
        "T424": "results/T424-m2-route-a-index-probe-v0.1-results.md",
        "T430": "results/T430-m2-support-completion-closure-gate-v0.1-results.md",
    }


def test_universe_declares_t430_no_completion_controls():
    universe = artifact()["universe"]

    assert universe["doctrine"] == "AND"
    assert universe["n_profiles"] == 64
    assert universe["t430_no_completion_controls"] == [
        "support_counts",
        "ambient_size",
        "quota_step",
        "selector_tie_completion",
        "deletion_critical_wording",
    ]


def test_t424_chi_escapes_vgap_but_fails_support_completion():
    report = channel("I_chi")

    assert report["class"] == "t424_candidate_index"
    assert report["vgap_independent"] is True
    assert report["feature_reports"]["vgap_reference"]["constant_on_all_fibers"] is False
    assert report["feature_reports"]["support_counts"]["constant_on_all_fibers"] is True
    assert report["admission_status"] == "rejected_completion_recoverable"
    assert "support_counts" in report["completion_leaks"]


def test_t424_frustration_escapes_vgap_but_fails_support_completion():
    report = channel("I_fr")

    assert report["class"] == "t424_candidate_index"
    assert report["vgap_independent"] is True
    assert report["feature_reports"]["vgap_reference"]["constant_on_all_fibers"] is False
    assert report["feature_reports"]["support_counts"]["constant_on_all_fibers"] is True
    assert report["admission_status"] == "rejected_completion_recoverable"
    assert "support_counts" in report["completion_leaks"]


def test_spectral_flow_channel_is_rejected_as_null():
    report = channel("I_sf")

    assert report["distinct_values"] == 1
    assert report["admission_status"] == "rejected_null_channel"


def test_finality_separator_is_rejected_by_selector_and_deletion_wording():
    report = channel("finality_separator")

    assert report["vgap_independent"] is False
    assert report["admission_status"] == "rejected_completion_recoverable"
    assert "selector_tie_completion" in report["completion_leaks"]
    assert "deletion_critical_wording" in report["completion_leaks"]


def test_leaky_support_and_quota_controls_are_rejected():
    support = channel("support_count_11")
    quota = channel("quota_margin_signature")

    assert support["admission_status"] == "rejected_completion_recoverable"
    assert "support_counts" in support["completion_leaks"]
    assert "quota_step" in support["completion_leaks"]

    assert quota["admission_status"] == "rejected_completion_recoverable"
    assert "quota_step" in quota["completion_leaks"]


def test_profile_serial_guard_proves_gate_can_see_independence():
    report = channel("profile_serial_guard")

    assert report["guard_only"] is True
    assert report["distinct_values"] == 64
    assert report["completion_leaks"] == []
    assert report["admission_status"] == "admitted_guard_only"
    assert report["feature_reports"]["support_counts"]["constant_on_all_fibers"] is False


def test_overall_verdict_blocks_current_domain_channels_only():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == "REDESIGN_M2_NO_CURRENT_INDEPENDENT_CHANNEL"
    assert verdict["admitted_domain_channels"] == []
    assert verdict["admitted_guard_channels"] == ["profile_serial_guard"]
    assert verdict["t424_candidate_status"] == {
        "I_chi": "rejected_completion_recoverable",
        "I_fr": "rejected_completion_recoverable",
        "I_sf": "rejected_null_channel",
    }
    assert "no-completion controls" in verdict["next_gate"]
    assert "not a universal no-go theorem" in artifact()["honest_ceiling"]
