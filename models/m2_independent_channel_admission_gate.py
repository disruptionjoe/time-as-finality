"""T431 - M2 Independent-Channel Admission Gate.

T430 closed the bounded M2 support-family branch and named the next gate:
future M2 work must either move off that universe or predeclare an independent
measurement channel with no-completion controls. This artifact makes that gate
executable over the current T424 Route-A channel candidates.

Recorded-tier only. No claim promotion. Cross-domain social-choice / index
language is object of study, never evidence for physics or a sibling repository.

Run:

    python -m models.m2_independent_channel_admission_gate --write-results
    python -m pytest tests/test_m2_independent_channel_admission_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from models import m2_route_a_index_probe as t424


SOURCE_ARTIFACTS = {
    "T424": "results/T424-m2-route-a-index-probe-v0.1-results.md",
    "T430": "results/T430-m2-support-completion-closure-gate-v0.1-results.md",
}

STATES = ((0, 0), (0, 1), (1, 0), (1, 1))
PROPER_COALITIONS = tuple(
    coalition for coalition in t424.CANON_COALITIONS
    if 0 < len(coalition) < len(t424.JUDGES)
)
GRAND = tuple(t424.JUDGES)


def support_counts(profile):
    counts = Counter(profile)
    return tuple(counts[state] for state in STATES)


def majority_counts(profile):
    p, q, r = t424.columns(profile, t424.DOCTRINES["AND"])
    return (
        sum(p.values()),
        sum(q.values()),
        sum(r.values()),
    )


def selector_tie_completion(profile):
    p, q, r = t424.columns(profile, t424.DOCTRINES["AND"])
    return (
        t424.smaj(p, t424.JUDGES),
        t424.smaj(q, t424.JUDGES),
        t424.smaj(r, t424.JUDGES),
        t424.premise_verdict(t424.JUDGES, p, q, t424.DOCTRINES["AND"]),
        t424.conclusion_verdict(t424.JUDGES, r),
    )


def deletion_critical_wording(profile):
    p, q, r = t424.columns(profile, t424.DOCTRINES["AND"])
    proper_gap_values = tuple(
        int(t424.gap_value(frozenset(coalition), p, q, r, t424.DOCTRINES["AND"]))
        for coalition in PROPER_COALITIONS
    )
    grand_gap = int(t424.gap_value(frozenset(GRAND), p, q, r, t424.DOCTRINES["AND"]))
    any_proper_gap = int(any(proper_gap_values))
    return (
        grand_gap,
        any_proper_gap,
        proper_gap_values,
    )


def vgap_reference(profile):
    return t424.vgap_vector(profile, t424.DOCTRINES["AND"])


def ambient_size(profile):
    return len(profile)


def profile_serial_lookup(profiles):
    return {profile: serial for serial, profile in enumerate(profiles)}


def build_profiles():
    return tuple(t424.enumerate_profiles())


def feature_functions(profiles):
    return {
        "vgap_reference": {
            "class": "old_reference_primitive",
            "description": "T424 majority-gap set-function fiber.",
            "value": vgap_reference,
        },
        "support_counts": {
            "class": "t430_no_completion_control",
            "description": "Full counts over judgment states (00, 01, 10, 11).",
            "value": support_counts,
        },
        "ambient_size": {
            "class": "t430_no_completion_control",
            "description": "Number of judges in the finite profile.",
            "value": ambient_size,
        },
        "quota_step": {
            "class": "t430_no_completion_control",
            "description": "Majority-threshold support counts for p, q, and r.",
            "value": majority_counts,
        },
        "selector_tie_completion": {
            "class": "t430_no_completion_control",
            "description": "Strict-majority premise/conclusion selector output.",
            "value": selector_tie_completion,
        },
        "deletion_critical_wording": {
            "class": "t430_no_completion_control",
            "description": "Grand-gap plus proper-subset gap wording.",
            "value": deletion_critical_wording,
        },
    }


def channel_functions(profiles):
    serials = profile_serial_lookup(profiles)
    return {
        "finality_separator": {
            "class": "current_target",
            "guard_only": False,
            "description": "T413/T423 SURVIVES-R1 finality separator.",
            "value": lambda profile: t424.finality_separator(profile, t424.DOCTRINES["AND"]),
        },
        "I_chi": {
            "class": "t424_candidate_index",
            "guard_only": False,
            "description": "T424 compatibility-complex Euler characteristic.",
            "value": lambda profile: t424.i_chi(profile)["value"],
        },
        "I_fr": {
            "class": "t424_candidate_index",
            "guard_only": False,
            "description": "T424 signed-graph frustration index.",
            "value": lambda profile: t424.i_fr(profile)["value"],
        },
        "I_sf": {
            "class": "t424_candidate_index",
            "guard_only": False,
            "description": "T424 regularized spectral-flow channel.",
            "value": lambda profile: t424.i_sf(profile)["value"],
        },
        "support_count_11": {
            "class": "leaky_negative_control",
            "guard_only": False,
            "description": "Direct support-count readout for state (1, 1).",
            "value": lambda profile: support_counts(profile)[3],
        },
        "quota_margin_signature": {
            "class": "leaky_negative_control",
            "guard_only": False,
            "description": "Direct majority-count readout.",
            "value": majority_counts,
        },
        "profile_serial_guard": {
            "class": "positive_control_not_domain_channel",
            "guard_only": True,
            "description": "Guard-only ordered profile id; proves the gate can see independence.",
            "value": lambda profile: serials[profile],
        },
    }


def partition_report(values_by_serial, features_by_serial):
    fibers = {}
    for serial, feature in features_by_serial.items():
        fibers.setdefault(feature, []).append(serial)

    mixed = []
    for feature, serials in fibers.items():
        values = sorted({values_by_serial[serial] for serial in serials}, key=repr)
        if len(values) > 1:
            mixed.append(
                {
                    "feature": feature,
                    "serials": serials[:6],
                    "channel_values": values[:8],
                    "fiber_size": len(serials),
                }
            )

    return {
        "n_fibers": len(fibers),
        "n_mixed_fibers": len(mixed),
        "constant_on_all_fibers": len(mixed) == 0,
        "mixed_examples": mixed[:4],
    }


def evaluate_channel(name, channel, profiles, features):
    values_by_serial = {
        serial: channel["value"](profile)
        for serial, profile in enumerate(profiles)
    }
    value_distribution = {
        repr(value): count
        for value, count in sorted(
            Counter(values_by_serial.values()).items(),
            key=lambda item: repr(item[0]),
        )
    }
    feature_reports = {}
    for feature_name, feature in features.items():
        feature_values = {
            serial: feature["value"](profile)
            for serial, profile in enumerate(profiles)
        }
        feature_reports[feature_name] = partition_report(values_by_serial, feature_values)

    completion_leaks = [
        feature_name for feature_name, report in feature_reports.items()
        if (
            features[feature_name]["class"] == "t430_no_completion_control"
            and report["constant_on_all_fibers"]
        )
    ]
    vgap_independent = not feature_reports["vgap_reference"]["constant_on_all_fibers"]
    distinct_values = len(set(values_by_serial.values()))
    null_channel = distinct_values <= 1

    if null_channel:
        status = "rejected_null_channel"
    elif completion_leaks:
        status = "rejected_completion_recoverable"
    elif channel["guard_only"]:
        status = "admitted_guard_only"
    else:
        status = "admitted_domain_candidate"

    return {
        "name": name,
        "class": channel["class"],
        "guard_only": channel["guard_only"],
        "description": channel["description"],
        "distinct_values": distinct_values,
        "value_distribution": value_distribution,
        "vgap_independent": vgap_independent,
        "completion_leaks": completion_leaks,
        "admission_status": status,
        "feature_reports": feature_reports,
    }


def overall_verdict(channel_reports):
    domain_admitted = [
        report["name"] for report in channel_reports
        if report["admission_status"] == "admitted_domain_candidate"
    ]
    guard_admitted = [
        report["name"] for report in channel_reports
        if report["admission_status"] == "admitted_guard_only"
    ]
    t424_candidates = [
        report for report in channel_reports
        if report["class"] == "t424_candidate_index"
    ]
    t424_candidate_status = {
        report["name"]: report["admission_status"] for report in t424_candidates
    }

    if domain_admitted:
        verdict = "RECHECK_M2_CHANNEL_ADMISSION"
        reading = (
            "At least one non-guard domain channel cleared the no-completion gate. "
            "Inspect it before any M2 swing."
        )
    else:
        verdict = "REDESIGN_M2_NO_CURRENT_INDEPENDENT_CHANNEL"
        reading = (
            "The current T424 Route-A channel candidates do not clear T430's "
            "independent-channel admission bar. I_chi and I_fr are independent of "
            "the old v_gap primitive but are recoverable from full support counts; "
            "I_sf is null at this witness size. A future M2 swing needs a newly "
            "predeclared domain channel that survives these no-completion controls."
        )

    return {
        "verdict": verdict,
        "admitted_domain_channels": domain_admitted,
        "admitted_guard_channels": guard_admitted,
        "t424_candidate_status": t424_candidate_status,
        "reading": reading,
        "next_gate": (
            "Do not reopen support, quota, selector, tie-completion, ambient-size, "
            "or deletion-critical variants until a candidate channel passes these "
            "no-completion controls as a domain channel rather than a guard label."
        ),
    }


def run():
    profiles = build_profiles()
    features = feature_functions(profiles)
    channels = channel_functions(profiles)
    channel_reports = [
        evaluate_channel(name, channel, profiles, features)
        for name, channel in channels.items()
    ]
    return {
        "artifact": "T431-m2-independent-channel-admission-gate-v0.1",
        "scope": (
            "Recorded-tier admission gate for candidate M2 measurement channels "
            "after T430's bounded support-family closure."
        ),
        "source_artifacts": SOURCE_ARTIFACTS,
        "universe": {
            "doctrine": "AND",
            "n_profiles": len(profiles),
            "states": [list(state) for state in STATES],
            "t430_no_completion_controls": [
                name for name, feature in features.items()
                if feature["class"] == "t430_no_completion_control"
            ],
        },
        "channel_reports": channel_reports,
        "overall_verdict": overall_verdict(channel_reports),
        "honest_ceiling": (
            "This is not a universal no-go theorem, not a claim-ledger movement, "
            "and not evidence for physics or a sibling repo. It is an executable "
            "admission/control gate for future M2 attempts in the current finite "
            "AND-doctrine universe."
        ),
    }


def render_markdown(result):
    verdict = result["overall_verdict"]
    rows = []
    for report in result["channel_reports"]:
        rows.append(
            "| {name} | {klass} | {vgap} | {leaks} | {status} |".format(
                name=report["name"],
                klass=report["class"],
                vgap="yes" if report["vgap_independent"] else "no",
                leaks=", ".join(report["completion_leaks"]) or "none",
                status=report["admission_status"],
            )
        )

    source_lines = "\n".join(
        f"- {name}: `{path}`" for name, path in result["source_artifacts"].items()
    )

    return "\n".join(
        [
            "# T431 - M2 Independent-Channel Admission Gate - v0.1 results",
            "",
            "> Recorded-tier exploratory admission artifact. `TESTS.md`, `ROADMAP.md`, "
            "and `CLAIM-LEDGER.md` are UNTOUCHED; the T-number lives only in this "
            "header / the spec header. NO claim promotion; ledger actions pause for "
            "Joe. Cross-domain social-choice / index language is the OBJECT OF STUDY, "
            "never evidence for physics or a sibling repo.",
            "",
            "- Spec (frozen first): `tests/T431-m2-independent-channel-admission-gate.md`",
            "- Model: `models/m2_independent_channel_admission_gate.py`",
            "- Tests: `tests/test_m2_independent_channel_admission_gate.py`",
            "- Artifact JSON: `results/T431-m2-independent-channel-admission-gate-v0.1.json`",
            "- Run: `python -m pytest tests/test_m2_independent_channel_admission_gate.py -q`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Admission Table",
            "",
            "| channel | class | vgap independent? | completion leaks | status |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Source Artifacts",
            "",
            source_lines,
            "",
            "## What this says about M2",
            "",
            "T424's `I_chi` and `I_fr` were real improvements over Route B because "
            "they are not functions of the old `v_gap` primitive. T431 shows why "
            "that is still not enough after T430: both channels are fully recovered "
            "by support-count completion over the four judgment states. The spectral "
            "flow channel remains null at this finite witness size.",
            "",
            verdict["next_gate"],
            "",
            "## What this earns / does not earn",
            "",
            "Earns: an executable admission gate for future M2 independent-channel "
            "attempts, plus a bounded negative result for the current T424 channel "
            "candidates.",
            "",
            "Does not earn: a universal no-go theorem, a closed M2 program, a stable "
            "M2 rescue, a canonical separator object, any claim-ledger movement, any "
            "physics-facing claim, or any cross-repo evidential use.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
            "",
        ]
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T431-m2-independent-channel-admission-gate-v0.1.json"
        md_path = results_dir / "T431-m2-independent-channel-admission-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
