"""T451 - D2 temporal route demotion packet.

T450 recommended a separate governed decision packet for the D2 temporal
computational-arrow route. This artifact executes that packet for the current
route only.

The decision is deliberately narrow:

* finite public-cycle evidence is absorbed by T420/T438;
* the open Rabin-lift chain is absorbed by T448;
* the closed public-squaring period route is absorbed by T450 as
  Rabin/factoring trapdoor equivalence;
* future D2 work is not banned, but it must change the assumption or scope
  rather than rebuild the absorbed route.

Run:

    python -m models.d2_temporal_route_demotion_packet --write-results
    python -m pytest tests/test_d2_temporal_route_demotion_packet.py -q
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from models import e2_changed_transition_regime_gate as t444
from models import e2_chain_residual_factorization as t448
from models import e2_period_hardness_admission_gate as t438
from models import e2_period_hardness_packet_audit as t449
from models import e2_period_oracle_trapdoor_equivalence as t450


ARTIFACT = "T451-d2-temporal-route-demotion-packet-v0.1"
SOURCE_D2 = "open-problems/computational-finality-arrow.md"
SOURCE_T417 = "results/T417-computational-finality-boundary-v0.1-results.md"
SOURCE_T438 = "results/T438-e2-period-hardness-admission-gate-v0.1-results.md"
SOURCE_T444 = "results/T444-e2-changed-transition-regime-gate-v0.1-results.md"
SOURCE_T448 = "results/T448-e2-chain-residual-factorization-v0.1-results.md"
SOURCE_T449 = "results/T449-e2-period-hardness-packet-audit-v0.1-results.md"
SOURCE_T450 = "results/T450-e2-period-oracle-trapdoor-equivalence-v0.1-results.md"

VERDICT = "CURRENT_D2_TEMPORAL_ROUTE_DEMOTED_TO_T417_STATIC_E2_BOUNDARY"

HONEST_CEILING = (
    "Route-demotion packet only. T451 closes the current temporal D2 route back "
    "to T417's static E2 boundary; it does not demote the whole D2 definition, "
    "does not promote a claim, does not prove or refute factoring hardness, does "
    "not make a physics claim, and does not authorize public posture."
)

FUTURE_EXCEPTION = (
    "Future D2 work remains admissible only if it supplies a changed assumption "
    "or scope: for example, a nonstandard period assumption avoiding both "
    "single-seed weakness and all-target trapdoor equivalence, or a separate "
    "changed-transition/open-regime packet that does not factor through per-step "
    "T417/Rabin inversion."
)


def imported_evidence() -> dict[str, Any]:
    return {
        "t438": t438.run()["overall_verdict"],
        "t444": t444.run()["overall_verdict"],
        "t448": t448.run()["overall_verdict"],
        "t449": t449.run()["overall_verdict"],
        "t450": t450.run()["overall_verdict"],
    }


def route_matrix(evidence: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "route": "finite_public_cycle_or_bounded_nonrecovery",
            "source": "T420/T438",
            "status": "absorbed",
            "reason": (
                "Closed finite public cycles recover predecessors by public "
                "forward iteration once the period is traversable; bounded "
                "non-recovery is not evidence without a family assumption."
            ),
            "decision_effect": "cannot carry D2 temporal-arrow novelty",
        },
        {
            "route": "open_rabin_lift_chain",
            "source": "T446/T448",
            "status": "absorbed",
            "reason": evidence["t448"]["reading"],
            "decision_effect": "collapses to chained T417/Rabin inversion",
        },
        {
            "route": "closed_public_squaring_period_oracle",
            "source": "T449/T450",
            "status": "absorbed",
            "reason": evidence["t450"]["reading"],
            "decision_effect": "no independent finite-witness temporal residue",
        },
        {
            "route": "changed_transition_or_open_nonpermutation",
            "source": "T444 plus T448 tested packet",
            "status": "future_exception_only",
            "reason": (
                "T444 admits this only as a separate-regime review target. The "
                "tested open Rabin-lift packet was then absorbed by T448."
            ),
            "decision_effect": (
                "future work must supply a different packet, not reuse the T446 "
                "chain shape"
            ),
        },
        {
            "route": "nonstandard_period_assumption",
            "source": "T449/T450",
            "status": "future_exception_only",
            "reason": (
                "T449 named hidden-order cycle length as the theorem burden, "
                "but T450 showed the current useful all-target period oracle is "
                "trapdoor-strength. No nonstandard replacement assumption is "
                "supplied by the current route."
            ),
            "decision_effect": "only remaining admissible D2 continuation shape",
        },
    ]


def decision_screen(matrix: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": "finite_cycle_route_closed",
            "passed": any(
                item["route"] == "finite_public_cycle_or_bounded_nonrecovery"
                and item["status"] == "absorbed"
                for item in matrix
            ),
            "status": "closed_by_t420_t438",
            "reading": "Finite public-cycle and bounded-search variants cannot carry D2.",
        },
        {
            "id": "open_chain_route_closed",
            "passed": any(
                item["route"] == "open_rabin_lift_chain"
                and item["status"] == "absorbed"
                for item in matrix
            ),
            "status": "closed_by_t448",
            "reading": "The tested open-chain route is product-decomposable into T417 steps.",
        },
        {
            "id": "closed_period_route_closed",
            "passed": any(
                item["route"] == "closed_public_squaring_period_oracle"
                and item["status"] == "absorbed"
                for item in matrix
            ),
            "status": "closed_by_t450",
            "reading": "The current period-oracle route is trapdoor-strength.",
        },
        {
            "id": "future_exception_preserved",
            "passed": all(
                item["status"] in {"absorbed", "future_exception_only"}
                for item in matrix
            ),
            "status": "future_changed_assumption_only",
            "reading": FUTURE_EXCEPTION,
        },
        {
            "id": "protected_surfaces_unchanged",
            "passed": True,
            "status": "no_claim_or_public_posture_move",
            "reading": (
                "This packet updates route standing only. CLAIM-LEDGER, TESTS, "
                "ROADMAP, README, and North Star files are not required for the "
                "decision."
            ),
        },
    ]


def run() -> dict[str, Any]:
    evidence = imported_evidence()
    matrix = route_matrix(evidence)
    screen = decision_screen(matrix)
    passed = all(item["passed"] for item in screen)

    return {
        "artifact": ARTIFACT,
        "sources": {
            "d2_open_problem": SOURCE_D2,
            "t417_static_boundary": SOURCE_T417,
            "t438": SOURCE_T438,
            "t444": SOURCE_T444,
            "t448": SOURCE_T448,
            "t449": SOURCE_T449,
            "t450": SOURCE_T450,
        },
        "purpose": (
            "Execute the separate governed decision packet recommended by T450 "
            "for the current temporal D2 computational-arrow route."
        ),
        "imported_evidence": evidence,
        "route_matrix": matrix,
        "decision_screen": screen,
        "overall_verdict": {
            "verdict": VERDICT if passed else "D2_TEMPORAL_ROUTE_DECISION_BLOCKED",
            "screen_passed": passed,
            "current_route_decision": (
                "demote current temporal D2 route to T417 static E2 boundary"
            ),
            "future_exception": FUTURE_EXCEPTION,
            "claim_ledger_update": "none; no claim status change",
            "public_posture_update": "none",
            "reading": (
                "The current D2 temporal computational-arrow route has exhausted "
                "its tested continuations. Finite public cycles are absorbed by "
                "public period traversal, the tested open chain factors through "
                "per-step Rabin/T417 inversion, and the closed public-squaring "
                "period route collapses to Rabin/factoring trapdoor equivalence. "
                "The route is therefore demoted to T417's static E2 boundary, "
                "with future D2 work reserved for a genuinely changed assumption "
                "or scope."
            ),
        },
        "recommended_next": [
            "Stop rebuilding the current public-squaring temporal D2 route.",
            "Keep T417 as the static E2 computational-finality boundary.",
            "Only reopen temporal D2 with a changed assumption or packet that clears T438/T444 and avoids T448/T450 absorbers.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    matrix_rows = [
        "| {route} | {source} | {status} | {effect} |".format(
            route=item["route"],
            source=item["source"],
            status=item["status"],
            effect=item["decision_effect"],
        )
        for item in result["route_matrix"]
    ]
    screen_rows = [
        "| {id} | {status} | {passed} |".format(
            id=item["id"],
            status=item["status"],
            passed="yes" if item["passed"] else "no",
        )
        for item in result["decision_screen"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T451 - D2 Temporal Route Demotion Packet - v0.1 results",
            "",
            "> Route-demotion packet. `CLAIM-LEDGER.md`, `ROADMAP.md`, `TESTS.md`, "
            "README, and North Star files are untouched. No claim promotion, no "
            "crypto theorem, no physics claim, no public posture.",
            "",
            "- Spec: `tests/T451-d2-temporal-route-demotion-packet.md`",
            "- Model: `models/d2_temporal_route_demotion_packet.py`",
            "- Tests: `tests/test_d2_temporal_route_demotion_packet.py`",
            "- Artifact JSON: `results/T451-d2-temporal-route-demotion-packet-v0.1.json`",
            "- Sources: T417, T438, T444, T448, T449, T450, and the D2 open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Route Matrix",
            "",
            "| route | source | status | decision effect |",
            "| --- | --- | --- | --- |",
            *matrix_rows,
            "",
            "## Decision Screen",
            "",
            "| check | status | passed? |",
            "| --- | --- | --- |",
            *screen_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: closure of the current temporal D2 route as a route-level "
            "decision. T417 remains as the static E2 computational-finality "
            "boundary.",
            "",
            "Does not earn: claim promotion, claim-ledger movement, a "
            "computational-arrow theorem, a crypto theorem, a physics claim, "
            "North Star movement, or public posture.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_steps,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T451-d2-temporal-route-demotion-packet-v0.1.json"
        md_path = (
            results_dir / "T451-d2-temporal-route-demotion-packet-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
