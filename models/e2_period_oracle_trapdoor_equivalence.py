"""T450 - E2 period-oracle trapdoor equivalence audit.

T449 sharpened the remaining D2 route to hidden-order / cycle-length hardness.
This artifact stress-tests whether that route is independent of T417/Rabin.

For BBS-style public squaring on QR_N:

* if the cycle period L of a target y is known, the predecessor is F^(L-1)(y);
* a predecessor oracle on QR_N is the principal square-root oracle;
* Rabin's square-root oracle reduction factors N.

So an all-target period oracle is trapdoor-strength in the same sense as T417.
The temporal route has no independent finite-witness residue in this packet.

Run:

    python -m models.e2_period_oracle_trapdoor_equivalence --write-results
    python -m pytest tests/test_e2_period_oracle_trapdoor_equivalence.py -q
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from models import e2_period_hardness_packet_audit as t449
from models.computational_arrow_of_time import forward, rabin_reduction


ARTIFACT = "T450-e2-period-oracle-trapdoor-equivalence-v0.1"
SOURCE_D2 = "open-problems/computational-finality-arrow.md"
SOURCE_T417 = "results/T417-computational-finality-boundary-v0.1-results.md"
SOURCE_T438 = "results/T438-e2-period-hardness-admission-gate-v0.1-results.md"
SOURCE_T449 = "results/T449-e2-period-hardness-packet-audit-v0.1-results.md"

VERDICT = (
    "PERIOD_ORACLE_COLLAPSES_TO_RABIN_TRAPDOOR_NO_INDEPENDENT_D2_ROUTE"
)

HONEST_CEILING = (
    "Recorded-tier trapdoor-equivalence audit only. T450 does not redesign or "
    "abandon D2, does not prove period hardness, does not prove factoring "
    "hardness, does not promote a claim, does not make a physics claim, and "
    "does not authorize public posture."
)


def period_oracle(seed: int, modulus: t449.BlumModulus) -> int:
    """Trapdoor-backed toy period oracle, exposing only the period value."""

    return t449.period_witness_for_seed(modulus, seed).period_formula


def predecessor_from_period_oracle(target: int, modulus: t449.BlumModulus) -> dict[str, Any]:
    period = period_oracle(target, modulus)
    predecessor = t449.predecessor_from_known_period(target, modulus.n, period)
    return {
        "modulus": t449._modulus_to_dict(modulus),
        "target": target,
        "period_oracle_value": period,
        "predecessor": predecessor,
        "forward_of_predecessor_matches_target": forward(predecessor, modulus.n) == target,
    }


def period_oracle_to_predecessor_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for family_row in t449.family_period_audit()["rows"]:
        modulus = t449.BlumModulus(
            family_row["modulus"]["label"],
            family_row["modulus"]["p"],
            family_row["modulus"]["q"],
        )
        rows.append(predecessor_from_period_oracle(family_row["target_state"], modulus))
    return rows


def period_oracle_factorization_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for modulus in t449.candidate_family():
        def sqrt_oracle(a: int, current: t449.BlumModulus = modulus) -> int:
            return predecessor_from_period_oracle(a, current)["predecessor"]

        reduction = rabin_reduction(modulus.n, sqrt_oracle)
        rows.append(
            {
                "modulus": t449._modulus_to_dict(modulus),
                "rabin_reduction_exhibited": reduction,
                "period_oracle_yields_factor": (
                    reduction is not None
                    and reduction["nontrivial_factor"] in (modulus.p, modulus.q)
                    and reduction["nontrivial_factor"] * reduction["cofactor"]
                    == modulus.n
                ),
                "reading": (
                    "An all-target period oracle gives the unique QR predecessor, "
                    "which is a principal square-root oracle. Rabin reduction then "
                    "factors N in the toy audit."
                ),
            }
        )
    return rows


def trapdoor_to_period_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for family_row in t449.family_period_audit()["rows"]:
        modulus = t449.BlumModulus(
            family_row["modulus"]["label"],
            family_row["modulus"]["p"],
            family_row["modulus"]["q"],
        )
        order = t449.order_mod_n_from_group_order(
            family_row["seed"],
            modulus.n,
            modulus.qr_size,
        )
        period = t449.squaring_period_from_order(order)
        recovered_factors = t449.factor_from_qr_group_order(modulus.n, modulus.qr_size)
        rows.append(
            {
                "modulus": t449._modulus_to_dict(modulus),
                "seed": family_row["seed"],
                "group_order_used": modulus.qr_size,
                "order_from_group_order": order,
                "period_from_group_order": period,
                "matches_t449_period": period == family_row["period_formula"],
                "group_order_recovers_factors": recovered_factors
                == tuple(sorted((modulus.p, modulus.q))),
                "recovered_factors": list(recovered_factors),
            }
        )
    return rows


def oracle_scope_classifier() -> list[dict[str, Any]]:
    return [
        {
            "scope": "single_seed_period_value",
            "can_reverse_arbitrary_target": False,
            "can_factor_by_rabin_reduction": False,
            "status": "insufficient_for_d2_packet",
            "reading": (
                "A period value for one preselected seed does not invert arbitrary "
                "targets and does not supply the D2 predecessor capability."
            ),
        },
        {
            "scope": "challenge_target_period_value",
            "can_reverse_arbitrary_target": False,
            "can_factor_by_rabin_reduction": False,
            "status": "single_challenge_predecessor_only",
            "reading": (
                "A period value for the current target gives that target's "
                "predecessor, but does not by itself define a family oracle."
            ),
        },
        {
            "scope": "all_qr_targets_period_oracle",
            "can_reverse_arbitrary_target": True,
            "can_factor_by_rabin_reduction": True,
            "status": "trapdoor_strength",
            "reading": (
                "A period oracle over arbitrary QR targets supplies a predecessor "
                "oracle and factors N via Rabin reduction."
            ),
        },
        {
            "scope": "group_order_or_factorization_completion",
            "can_reverse_arbitrary_target": True,
            "can_factor_by_rabin_reduction": True,
            "status": "native_trapdoor_completion",
            "reading": (
                "Group-order or factorization data computes periods and is ordinary "
                "trapdoor completion, not new temporal residue."
            ),
        },
    ]


def absorber_screen(
    predecessor_rows: list[dict[str, Any]],
    factor_rows: list[dict[str, Any]],
    trapdoor_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {
            "id": "period_oracle_gives_predecessor",
            "status": "temporal_capability_reduced_to_period_value",
            "passed": all(
                row["forward_of_predecessor_matches_target"] for row in predecessor_rows
            ),
            "reading": (
                "For closed public squaring, target-period knowledge is enough to "
                "recover the predecessor by public forward iteration."
            ),
        },
        {
            "id": "predecessor_oracle_factors_n",
            "status": "rabin_trapdoor_equivalence_exhibited",
            "passed": all(row["period_oracle_yields_factor"] for row in factor_rows),
            "reading": (
                "An all-target period oracle becomes a principal square-root oracle; "
                "Rabin reduction factors N."
            ),
        },
        {
            "id": "trapdoor_completion_computes_periods",
            "status": "completion_absorbs_period_object",
            "passed": all(
                row["matches_t449_period"] and row["group_order_recovers_factors"]
                for row in trapdoor_rows
            ),
            "reading": (
                "The semiprime toy's group-order/factorization completion computes "
                "periods and recovers the ordinary trapdoor."
            ),
        },
        {
            "id": "oracle_scope_controls",
            "status": "scope_guardrail_recorded",
            "passed": True,
            "reading": (
                "Single-seed period values are too weak; all-target period oracles "
                "are trapdoor-strength. Future theorem targets must declare scope."
            ),
        },
        {
            "id": "independent_d2_residue",
            "status": "not_found_for_current_route",
            "passed": True,
            "reading": (
                "T450 finds no independent temporal theorem shape beyond the "
                "Rabin/factoring trapdoor for this closed public-squaring route."
            ),
        },
    ]


def run() -> dict[str, Any]:
    predecessor_rows = period_oracle_to_predecessor_rows()
    factor_rows = period_oracle_factorization_rows()
    trapdoor_rows = trapdoor_to_period_rows()
    scope_rows = oracle_scope_classifier()
    screen = absorber_screen(predecessor_rows, factor_rows, trapdoor_rows)
    passed = all(item["passed"] for item in screen)

    return {
        "artifact": ARTIFACT,
        "sources": {
            "d2_open_problem": SOURCE_D2,
            "t417": SOURCE_T417,
            "t438": SOURCE_T438,
            "t449": SOURCE_T449,
        },
        "purpose": (
            "Stress-test T449's hidden-order period target by checking whether "
            "a useful period oracle is independent of the Rabin/factoring trapdoor."
        ),
        "period_oracle_to_predecessor": predecessor_rows,
        "period_oracle_to_factorization": factor_rows,
        "trapdoor_to_period": trapdoor_rows,
        "oracle_scope_classifier": scope_rows,
        "absorber_screen": screen,
        "overall_verdict": {
            "verdict": VERDICT if passed else "PERIOD_ORACLE_TRAPDOOR_AUDIT_BLOCKED",
            "screen_passed": passed,
            "d2_decision": "none; redesign/abandon remains separately gated",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "For the current closed public-squaring route, an all-target period "
                "oracle is trapdoor-strength: it gives unique predecessors, and "
                "Rabin's reduction factors N from such a predecessor oracle. "
                "Conversely, group-order/factorization completion computes periods. "
                "The remaining D2 route therefore has no independent finite-witness "
                "residue beyond the standard Rabin/factoring boundary unless a "
                "future theorem target changes the oracle scope or assumption."
            ),
        },
        "recommended_next": [
            "Treat the current closed public-squaring period route as absorbed by Rabin/factoring trapdoor equivalence.",
            "Only continue D2 if a nonstandard period assumption is specified with scope that avoids both single-seed weakness and all-target trapdoor equivalence.",
            "Otherwise demote the temporal D2 route to T417's static E2 boundary in a separate governed decision packet.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    pred_rows = [
        "| {label} | {n} | {target} | {period} | {pred} | {ok} |".format(
            label=row["modulus"]["label"],
            n=row["modulus"]["n"],
            target=row["target"],
            period=row["period_oracle_value"],
            pred=row["predecessor"],
            ok="yes" if row["forward_of_predecessor_matches_target"] else "no",
        )
        for row in result["period_oracle_to_predecessor"]
    ]
    factor_rows = [
        "| {label} | {n} | {factor} | {cofactor} | {ok} |".format(
            label=row["modulus"]["label"],
            n=row["modulus"]["n"],
            factor=row["rabin_reduction_exhibited"]["nontrivial_factor"],
            cofactor=row["rabin_reduction_exhibited"]["cofactor"],
            ok="yes" if row["period_oracle_yields_factor"] else "no",
        )
        for row in result["period_oracle_to_factorization"]
    ]
    scope_rows = [
        "| {scope} | {reverse} | {factor} | {status} |".format(
            scope=row["scope"],
            reverse="yes" if row["can_reverse_arbitrary_target"] else "no",
            factor="yes" if row["can_factor_by_rabin_reduction"] else "no",
            status=row["status"],
        )
        for row in result["oracle_scope_classifier"]
    ]
    screen_rows = [
        "| {id} | {status} | {passed} |".format(
            id=item["id"],
            status=item["status"],
            passed="yes" if item["passed"] else "no",
        )
        for item in result["absorber_screen"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T450 - E2 Period-Oracle Trapdoor Equivalence - v0.1 results",
            "",
            "> Recorded-tier trapdoor-equivalence audit. `TESTS.md`, `ROADMAP.md`, "
            "and `CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, "
            "no claim promotion, no public posture.",
            "",
            "- Spec: `tests/T450-e2-period-oracle-trapdoor-equivalence.md`",
            "- Model: `models/e2_period_oracle_trapdoor_equivalence.py`",
            "- Tests: `tests/test_e2_period_oracle_trapdoor_equivalence.py`",
            "- Artifact JSON: `results/T450-e2-period-oracle-trapdoor-equivalence-v0.1.json`",
            "- Sources: T417, T438, T449, and the D2 open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Period Oracle To Predecessor",
            "",
            "| modulus | N | target | period | predecessor | verifies? |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
            *pred_rows,
            "",
            "## Period Oracle To Factorization",
            "",
            "| modulus | N | factor | cofactor | factors? |",
            "| --- | ---: | ---: | ---: | --- |",
            *factor_rows,
            "",
            "## Oracle Scope Classifier",
            "",
            "| scope | reverses arbitrary target? | factors by Rabin? | status |",
            "| --- | --- | --- | --- |",
            *scope_rows,
            "",
            "## Absorber Screen",
            "",
            "| check | status | passed? |",
            "| --- | --- | --- |",
            *screen_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a runnable collapse audit for the current closed public-squaring "
            "period route. The all-target period oracle is trapdoor-strength, and "
            "trapdoor completion computes periods.",
            "",
            "Does not earn: D2 redesign, D2 abandonment, a computational-arrow "
            "theorem, a period-hardness theorem, a crypto theorem, a physics claim, "
            "claim-ledger movement, or public posture.",
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
        json_path = results_dir / "T450-e2-period-oracle-trapdoor-equivalence-v0.1.json"
        md_path = results_dir / "T450-e2-period-oracle-trapdoor-equivalence-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
