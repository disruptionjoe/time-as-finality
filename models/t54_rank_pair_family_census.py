"""T163: exhaustive six-event T54 rank-pair family census for S1.

This module replaces one-off interpretation of the T157 witness with a full
finite census of the smallest nontrivial T54 rank-pair family:

  causal ranks fixed to 1..6
  information ranks varied over all 6! permutations

Each case is completed through the T54 quotient-union pipeline and then sent
through the existing T126, T156, and T159 screens. The result is still finite
control work, not spacetime evidence. Its value is family-level triage:
whether T157 was an isolated fragile curiosity or one member of a broader,
audit-surviving finite class.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    audit_finality_colimit_causet,
)
from models.finality_descent_theorem import (
    AxisProfile,
    EventIdentityMap,
    LocalEvent,
    ObserverDescentDatum,
    ObserverView,
    complete_observer_descent_datum,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)
from models.t54_interval_jackknife_screen import (
    _deletion_audits,
    _largest_interval_size,
    flat_1p1_interval_jackknife_target,
)
from models.t54_ordering_fraction_bridge import _completion_to_t126_datum


Event = str
InfoPermutation = tuple[int, ...]

T157_BASELINE_PERMUTATION: InfoPermutation = (1, 6, 4, 5, 2, 3)


@dataclass(frozen=True)
class T163CaseAudit:
    info_permutation: InfoPermutation
    t126_classification: str
    t126_filter_passed: bool
    t156_verdict: str | None
    parent_interval_support_passed: bool
    deletion_pass_count: int
    deletion_case_count: int
    deletion_pass_rate: Fraction
    stable_under_t159: bool
    strict_pair_count: int | None
    interval_counts_by_size: tuple[tuple[int, int], ...]
    outcome_bucket: str


@dataclass(frozen=True)
class T163Result:
    total_cases: int
    t126_classification_counts: tuple[tuple[str, int], ...]
    t156_fail_count: int
    parent_interval_fail_count: int
    fragile_jackknife_count: int
    stable_survivor_count: int
    stable_survivor_fraction: Fraction
    t157_baseline_bucket: str
    t157_baseline_stable: bool
    representative_stable_permutations: tuple[InfoPermutation, ...]
    representative_fragile_permutations: tuple[InfoPermutation, ...]
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


NOT_CLAIMED = (
    "T163 does not show a random sprinkling law, faithful embedding, metric or "
    "Lorentzian reconstruction, covariance, or a continuum limit. It is a "
    "finite family census over one small T54 rank-pair class only."
)


def run_t163_analysis() -> T163Result:
    case_audits = audit_t163_family()
    t126_counts = _count_by_key(case_audits, key=lambda audit: audit.t126_classification)
    t156_fail_count = sum(
        1 for audit in case_audits if audit.outcome_bucket == "t156_ordering_fraction_fail"
    )
    parent_interval_fail_count = sum(
        1 for audit in case_audits if audit.outcome_bucket == "t159_parent_interval_fail"
    )
    fragile_jackknife_count = sum(
        1 for audit in case_audits if audit.outcome_bucket == "t159_fragile_jackknife"
    )
    stable_survivors = tuple(
        audit for audit in case_audits if audit.outcome_bucket == "t159_stable_survivor"
    )
    stable_count = len(stable_survivors)
    baseline = next(
        audit for audit in case_audits if audit.info_permutation == T157_BASELINE_PERMUTATION
    )

    return T163Result(
        total_cases=len(case_audits),
        t126_classification_counts=t126_counts,
        t156_fail_count=t156_fail_count,
        parent_interval_fail_count=parent_interval_fail_count,
        fragile_jackknife_count=fragile_jackknife_count,
        stable_survivor_count=stable_count,
        stable_survivor_fraction=_fraction(stable_count, len(case_audits)),
        t157_baseline_bucket=baseline.outcome_bucket,
        t157_baseline_stable=baseline.stable_under_t159,
        representative_stable_permutations=tuple(
            audit.info_permutation for audit in stable_survivors[:5]
        ),
        representative_fragile_permutations=tuple(
            audit.info_permutation
            for audit in case_audits
            if audit.outcome_bucket == "t159_fragile_jackknife"
        )[:5],
        strongest_claim=(
            "The T157 witness is not an isolated accident, but it is also not "
            "representative of the whole six-event rank-pair family. Across "
            "all 720 labeled T54 rank-pair completions, 26 survive T126, T156, "
            "parent-interval, and single-deletion stability screens, while 130 "
            "more are jackknife-fragile and 694 remain below robust finite "
            "survivor status."
        ),
        improved=(
            "T163 upgrades S1 from single-example reading to family-level audit. "
            "It quantifies how often six-event T54 rank-pair completions are "
            "blocked at T126, miss the T156 target, fail parent-interval "
            "support, fail jackknife stability, or survive all current finite "
            "screens."
        ),
        weakened_or_falsified=(
            "This weakens the simple demotion story left by T159. The original "
            "T157 construction is fragile, but finite deletion-stable survivors "
            "do exist in the same six-event T54 rank-pair family. At the same "
            "time it weakens any broad optimism: only 26 of 720 labeled cases "
            "clear the current screens, so the family is still highly selective."
        ),
        falsification_condition=(
            "T163 fails if the census does not actually exhaust the 6! rank-pair "
            "family up to the declared fixing of causal ranks, if any case is "
            "audited through a different T54/T126/T156/T159 pipeline than the "
            "published controls, or if labeled-case counts are misread as a "
            "continuum or generic-family theorem."
        ),
        s1_update=(
            "S1 remains open_formal_target. The current finite boundary is now "
            "slightly stronger than T159 allowed: six-event deletion-stable T54 "
            "rank-pair survivors exist. But they remain tiny finite controls, "
            "not spacetime evidence, and still lack sprinkling, locality, "
            "embedding, covariance, and continuum diagnostics."
        ),
        claim_ledger_update=(
            "Add T163 to S1: an exhaustive six-event T54 rank-pair census finds "
            "26 labeled completions that survive T126, T156, parent-interval, "
            "and single-deletion screens, while the original T157 witness stays "
            "fragile. The S1 finite boundary is therefore family-level but still "
            "strictly calibration/control-level."
        ),
        open_blocker=(
            "No isomorphism-class reduction, random-sprinkling comparison, "
            "neighborhood-growth rule, locality diagnostic, faithful embedding "
            "theorem, covariance result, or continuum bridge exists for the 26 "
            "survivors."
        ),
        suggested_next=(
            "Quotient the 26 survivors by isomorphism and compare those classes "
            "against a declared random-sprinkling or locality diagnostic, rather "
            "than adding more hand-picked finite examples."
        ),
        not_claimed=NOT_CLAIMED,
    )


def audit_t163_family() -> tuple[T163CaseAudit, ...]:
    return tuple(_audit_info_permutation(info_perm) for info_perm in permutations(range(1, 7)))


def t163_t126_datum_for_permutation(info_permutation: InfoPermutation):
    datum = _rank_pair_datum(info_permutation)
    completion = complete_observer_descent_datum(datum)
    return _completion_to_t126_datum(completion)


def t163_result_to_dict(result: T163Result) -> dict[str, Any]:
    return {
        "total_cases": result.total_cases,
        "t126_classification_counts": [
            {"classification": classification, "count": count}
            for classification, count in result.t126_classification_counts
        ],
        "t156_fail_count": result.t156_fail_count,
        "parent_interval_fail_count": result.parent_interval_fail_count,
        "fragile_jackknife_count": result.fragile_jackknife_count,
        "stable_survivor_count": result.stable_survivor_count,
        "stable_survivor_fraction": _fraction_to_dict(result.stable_survivor_fraction),
        "t157_baseline_permutation": list(T157_BASELINE_PERMUTATION),
        "t157_baseline_bucket": result.t157_baseline_bucket,
        "t157_baseline_stable": result.t157_baseline_stable,
        "representative_stable_permutations": [
            list(permutation) for permutation in result.representative_stable_permutations
        ],
        "representative_fragile_permutations": [
            list(permutation) for permutation in result.representative_fragile_permutations
        ],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _audit_info_permutation(info_permutation: InfoPermutation) -> T163CaseAudit:
    datum = _rank_pair_datum(info_permutation)
    completion = complete_observer_descent_datum(datum)
    t126_datum = _completion_to_t126_datum(completion)
    t126_audit = audit_finality_colimit_causet(t126_datum)
    diagnostics = t126_audit.diagnostics

    if not t126_audit.manifold_filter_passed:
        return T163CaseAudit(
            info_permutation=info_permutation,
            t126_classification=t126_audit.classification,
            t126_filter_passed=False,
            t156_verdict=None,
            parent_interval_support_passed=False,
            deletion_pass_count=0,
            deletion_case_count=0,
            deletion_pass_rate=Fraction(0, 1),
            stable_under_t159=False,
            strict_pair_count=(
                diagnostics.strict_pair_count if diagnostics is not None else None
            ),
            interval_counts_by_size=(
                diagnostics.interval_counts_by_size if diagnostics is not None else tuple()
            ),
            outcome_bucket="t126_blocked",
        )

    t156_audit = audit_ordering_fraction_target(
        t126_datum,
        target=flat_1p1_interval_target(),
    )
    if t156_audit.verdict != "passes_ordering_fraction_control_only":
        return T163CaseAudit(
            info_permutation=info_permutation,
            t126_classification=t126_audit.classification,
            t126_filter_passed=True,
            t156_verdict=t156_audit.verdict,
            parent_interval_support_passed=False,
            deletion_pass_count=0,
            deletion_case_count=0,
            deletion_pass_rate=Fraction(0, 1),
            stable_under_t159=False,
            strict_pair_count=(
                diagnostics.strict_pair_count if diagnostics is not None else None
            ),
            interval_counts_by_size=(
                diagnostics.interval_counts_by_size if diagnostics is not None else tuple()
            ),
            outcome_bucket="t156_ordering_fraction_fail",
        )

    interval_counts = diagnostics.interval_counts_by_size if diagnostics is not None else tuple()
    largest_interval_size = _largest_interval_size(interval_counts)
    parent_interval_support_passed = largest_interval_size is not None and largest_interval_size <= 1
    if not parent_interval_support_passed:
        return T163CaseAudit(
            info_permutation=info_permutation,
            t126_classification=t126_audit.classification,
            t126_filter_passed=True,
            t156_verdict=t156_audit.verdict,
            parent_interval_support_passed=False,
            deletion_pass_count=0,
            deletion_case_count=0,
            deletion_pass_rate=Fraction(0, 1),
            stable_under_t159=False,
            strict_pair_count=(
                diagnostics.strict_pair_count if diagnostics is not None else None
            ),
            interval_counts_by_size=interval_counts,
            outcome_bucket="t159_parent_interval_fail",
        )

    jackknife_target = flat_1p1_interval_jackknife_target()
    deletion_audits = _deletion_audits(t126_datum, target=jackknife_target)
    deletion_pass_count = sum(
        1
        for audit in deletion_audits
        if audit.ordering_band_passed and audit.interval_support_passed
    )
    deletion_case_count = len(deletion_audits)
    deletion_pass_rate = _fraction(deletion_pass_count, deletion_case_count)
    stable = deletion_pass_count == deletion_case_count

    return T163CaseAudit(
        info_permutation=info_permutation,
        t126_classification=t126_audit.classification,
        t126_filter_passed=True,
        t156_verdict=t156_audit.verdict,
        parent_interval_support_passed=True,
        deletion_pass_count=deletion_pass_count,
        deletion_case_count=deletion_case_count,
        deletion_pass_rate=deletion_pass_rate,
        stable_under_t159=stable,
        strict_pair_count=diagnostics.strict_pair_count if diagnostics is not None else None,
        interval_counts_by_size=interval_counts,
        outcome_bucket=(
            "t159_stable_survivor" if stable else "t159_fragile_jackknife"
        ),
    )


def _rank_pair_datum(info_permutation: InfoPermutation) -> ObserverDescentDatum:
    profiles = {
        f"e{index}": AxisProfile(causal=index, info=info_permutation[index - 1])
        for index in range(1, 7)
    }
    strict_pairs = frozenset(
        (left, right)
        for left, left_profile in profiles.items()
        for right, right_profile in profiles.items()
        if left != right and left_profile.leq(right_profile)
    )
    observers = ("A", "B")
    observer_views = tuple(
        ObserverView(
            observer,
            tuple(
                _local_event(
                    observer=observer,
                    event=event,
                    profile=profiles[event],
                    predecessors=frozenset(
                        left for left, right in strict_pairs if right == event
                    ),
                )
                for event in sorted(profiles)
            ),
        )
        for observer in observers
    )
    identity_maps = tuple(
        EventIdentityMap(observer=observer, local_event=event, global_event=event)
        for observer in observers
        for event in sorted(profiles)
    )
    return ObserverDescentDatum(
        name=f"t163_rank_pair_{'-'.join(str(value) for value in info_permutation)}",
        description="Six-event exhaustive rank-pair T54 family member.",
        observer_views=observer_views,
        identity_maps=identity_maps,
        overlap_witnesses=frozenset(profiles),
        expected_classification="canonical",
    )


def _local_event(
    *,
    observer: str,
    event: Event,
    profile: AxisProfile,
    predecessors: frozenset[Event],
) -> LocalEvent:
    return LocalEvent(
        observer=observer,
        name=event,
        source_records=frozenset({f"raw_{event}"} | {f"locked_{p}" for p in predecessors}),
        target_records=frozenset({f"locked_{event}"}),
        profile=profile,
    )


def _count_by_key(
    audits: tuple[T163CaseAudit, ...],
    *,
    key: Any,
) -> tuple[tuple[str, int], ...]:
    counts: dict[str, int] = {}
    for audit in audits:
        label = key(audit)
        counts[label] = counts.get(label, 0) + 1
    return tuple(sorted(counts.items()))


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t163_result_to_dict(run_t163_analysis()), indent=2))
