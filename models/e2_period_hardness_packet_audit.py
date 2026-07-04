"""T449 - E2 period-hardness packet audit.

T448 closed the current open-chain route by showing that T446 factors through
independent per-step Rabin inversions. The remaining T438 route is the closed
public-permutation period-hardness path: keep the public transition fixed, but
make predecessor recovery depend on knowing the cycle period in a hidden-order
family.

This artifact does not prove period hardness. It makes the burden exact:

* for BBS-style squaring on QR_N, F^t(x) = x^(2^t);
* the cycle period is ord_d(2), where d = ord_N(x);
* trapdoor/group-order data computes toy periods;
* once the period is known, predecessor recovery is public forward iteration;
* small-period seeds collapse the packet immediately.

Run:

    python -m models.e2_period_hardness_packet_audit --write-results
    python -m pytest tests/test_e2_period_hardness_packet_audit.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import gcd, isqrt
from pathlib import Path
from typing import Any

from models import e2_period_hardness_admission_gate as t438
from models.computational_arrow_of_time import forward, quad_residues


ARTIFACT = "T449-e2-period-hardness-packet-audit-v0.1"
SOURCE_D2 = "open-problems/computational-finality-arrow.md"
SOURCE_T420 = "results/T420-finite-cycle-anti-relabel-gate-v0.1-results.md"
SOURCE_T438 = "results/T438-e2-period-hardness-admission-gate-v0.1-results.md"
SOURCE_T448 = "results/T448-e2-chain-residual-factorization-v0.1-results.md"

VERDICT = (
    "E2_PERIOD_HARDNESS_PACKET_SHARPENED_TO_HIDDEN_ORDER_THEOREM_TARGET_NO_D2_DECISION"
)

HONEST_CEILING = (
    "Recorded-tier period-hardness packet audit only. T449 does not redesign or "
    "abandon D2, does not prove period hardness, does not prove factoring "
    "hardness, does not promote a claim, does not make a physics claim, and "
    "does not authorize public posture."
)


@dataclass(frozen=True)
class BlumModulus:
    label: str
    p: int
    q: int

    @property
    def n(self) -> int:
        return self.p * self.q

    @property
    def qr_size(self) -> int:
        return ((self.p - 1) * (self.q - 1)) // 4


@dataclass(frozen=True)
class PeriodWitness:
    modulus: BlumModulus
    seed: int
    order_of_seed: int
    period_formula: int
    period_by_public_iteration: int
    target_state: int
    predecessor_from_period: int
    period_known_reverses_target: bool


def gcd_lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


def divisors(n: int) -> list[int]:
    result: set[int] = set()
    for candidate in range(1, isqrt(n) + 1):
        if n % candidate == 0:
            result.add(candidate)
            result.add(n // candidate)
    return sorted(result)


def multiplicative_order_mod(a: int, modulus: int) -> int:
    if modulus == 1:
        return 1
    if gcd(a, modulus) != 1:
        raise ValueError("multiplicative order requires a unit")
    value = 1
    for exponent in range(1, modulus + 1):
        value = (value * a) % modulus
        if value == 1:
            return exponent
    raise ValueError("multiplicative order not found")


def order_mod_n_from_group_order(x: int, n: int, group_order: int) -> int:
    if gcd(x, n) != 1:
        raise ValueError("seed must be a unit")
    for divisor in divisors(group_order):
        if pow(x, divisor, n) == 1:
            return divisor
    raise ValueError("order not found")


def squaring_period_from_order(order_of_seed: int) -> int:
    if order_of_seed == 1:
        return 1
    return multiplicative_order_mod(2, order_of_seed)


def public_period_by_iteration(seed: int, n: int, limit: int) -> int | None:
    state = seed
    for steps in range(1, limit + 1):
        state = forward(state, n)
        if state == seed:
            return steps
    return None


def predecessor_from_known_period(target_state: int, n: int, period: int) -> int:
    state = target_state
    for _ in range(period - 1):
        state = forward(state, n)
    return state


def factor_from_qr_group_order(n: int, qr_size: int) -> tuple[int, int]:
    """Recover p,q from N and |QR_N| for a semiprime N=pq.

    |QR_N| = (p-1)(q-1)/4 = (N - (p+q) + 1)/4, so p+q is determined.
    """

    sum_pq = n + 1 - 4 * qr_size
    discriminant = sum_pq * sum_pq - 4 * n
    root = isqrt(discriminant)
    if root * root != discriminant:
        raise ValueError("not a semiprime QR-size packet")
    p = (sum_pq - root) // 2
    q = (sum_pq + root) // 2
    if p * q != n:
        raise ValueError("factor recovery failed")
    return tuple(sorted((p, q)))


def candidate_family() -> tuple[BlumModulus, ...]:
    return (
        BlumModulus("N0_T419_control", 7, 11),
        BlumModulus("N1_hidden_order_control", 11, 19),
        BlumModulus("N2_hidden_order_control", 23, 31),
        BlumModulus("N3_hidden_order_control", 83, 103),
        BlumModulus("N4_hidden_order_control", 131, 179),
    )


def period_witness_for_seed(modulus: BlumModulus, seed: int) -> PeriodWitness:
    order = order_mod_n_from_group_order(seed, modulus.n, modulus.qr_size)
    formula_period = squaring_period_from_order(order)
    iter_period = public_period_by_iteration(seed, modulus.n, modulus.qr_size)
    if iter_period is None:
        raise AssertionError("public iteration did not find the finite toy period")
    target = forward(seed, modulus.n)
    predecessor = predecessor_from_known_period(target, modulus.n, formula_period)
    return PeriodWitness(
        modulus=modulus,
        seed=seed,
        order_of_seed=order,
        period_formula=formula_period,
        period_by_public_iteration=iter_period,
        target_state=target,
        predecessor_from_period=predecessor,
        period_known_reverses_target=predecessor == seed,
    )


def best_seed_witness(modulus: BlumModulus) -> PeriodWitness:
    qr = quad_residues(modulus.n)
    candidates = [period_witness_for_seed(modulus, seed) for seed in qr]
    return max(
        candidates,
        key=lambda item: (item.period_formula, item.order_of_seed, -item.seed),
    )


def _modulus_to_dict(modulus: BlumModulus) -> dict[str, Any]:
    return {
        "label": modulus.label,
        "p": modulus.p,
        "q": modulus.q,
        "n": modulus.n,
        "qr_size": modulus.qr_size,
    }


def _witness_to_dict(witness: PeriodWitness) -> dict[str, Any]:
    return {
        "modulus": _modulus_to_dict(witness.modulus),
        "seed": witness.seed,
        "order_of_seed": witness.order_of_seed,
        "period_formula": witness.period_formula,
        "period_by_public_iteration": witness.period_by_public_iteration,
        "formula_matches_iteration": (
            witness.period_formula == witness.period_by_public_iteration
        ),
        "target_state": witness.target_state,
        "predecessor_from_period": witness.predecessor_from_period,
        "period_known_reverses_target": witness.period_known_reverses_target,
    }


def family_period_audit() -> dict[str, Any]:
    witnesses = [best_seed_witness(modulus) for modulus in candidate_family()]
    rows: list[dict[str, Any]] = []
    for witness in witnesses:
        recovered_factors = factor_from_qr_group_order(
            witness.modulus.n,
            witness.modulus.qr_size,
        )
        row = _witness_to_dict(witness)
        row["qr_group_order_recovers_factorization"] = recovered_factors == tuple(
            sorted((witness.modulus.p, witness.modulus.q))
        )
        row["recovered_factors_from_qr_size"] = list(recovered_factors)
        rows.append(row)

    return {
        "family": [_modulus_to_dict(modulus) for modulus in candidate_family()],
        "rows": rows,
        "all_formula_match_iteration": all(
            row["formula_matches_iteration"] for row in rows
        ),
        "all_period_known_reverses_target": all(
            row["period_known_reverses_target"] for row in rows
        ),
        "all_qr_group_orders_recover_factorization": all(
            row["qr_group_order_recovers_factorization"] for row in rows
        ),
        "max_periods": [row["period_formula"] for row in rows],
    }


def small_period_seed_controls() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for modulus in candidate_family():
        one = period_witness_for_seed(modulus, 1)
        rows.append(
            {
                "modulus": _modulus_to_dict(modulus),
                "seed": one.seed,
                "period_formula": one.period_formula,
                "period_by_public_iteration": one.period_by_public_iteration,
                "period_known_reverses_target": one.period_known_reverses_target,
                "admitted_as_period_hardness_evidence": False,
                "reason": (
                    "Seed 1 is a fixed point. A period-hardness packet must "
                    "declare the seed distribution or generator and reject "
                    "small-period controls."
                ),
            }
        )
    return rows


def t438_classification_for_period_packet() -> dict[str, Any]:
    packet = t438.CandidatePacket(
        packet_id="t449_bbs_hidden_order_period_packet",
        description=(
            "Closed public squaring family over QR_N; reversal is public once "
            "the orbit period is known; period hardness remains a theorem target."
        ),
        closed_public_permutation_regime=True,
        family_level_declared=True,
        security_parameter_declared=True,
        public_transition_known=True,
        period_problem_declared=True,
        period_hardness_assumption_named=True,
        period_hardness_reduction_predeclared=True,
    )
    return t438.classify_packet(packet)


def absorber_screen(
    family: dict[str, Any],
    controls: list[dict[str, Any]],
    route: dict[str, Any],
) -> list[dict[str, Any]]:
    return [
        {
            "id": "t438_admission",
            "status": "admitted_as_theorem_target",
            "passed": (
                route["label"]
                == "ADMITTED_E2_PERIOD_HARDNESS_REDESIGN_PACKET_NO_D2_DECISION"
            ),
            "reading": (
                "The packet clears T438 as a future target because it declares "
                "the family, security parameter, public transition, period "
                "problem, named hidden-order burden, and theorem target."
            ),
        },
        {
            "id": "period_formula_matches_public_cycle",
            "status": "toy_formula_verified",
            "passed": family["all_formula_match_iteration"],
            "reading": (
                "For the toy family, period = ord_{ord_N(x)}(2) matches public "
                "cycle discovery. This is algebra sanity, not hardness evidence."
            ),
        },
        {
            "id": "known_period_publicly_reverses",
            "status": "period_is_missing_capability_object",
            "passed": family["all_period_known_reverses_target"],
            "reading": (
                "Once the cycle period is known, predecessor recovery is just "
                "public forward iteration F^(L-1)."
            ),
        },
        {
            "id": "group_order_completion_absorbs",
            "status": "trapdoor_completion_recorded",
            "passed": family["all_qr_group_orders_recover_factorization"],
            "reading": (
                "Granting QR group order is essentially trapdoor completion in "
                "the semiprime toy: N and |QR_N| recover p,q."
            ),
        },
        {
            "id": "small_period_seed_controls",
            "status": "seed_distribution_required",
            "passed": all(
                row["admitted_as_period_hardness_evidence"] is False
                and row["period_formula"] == 1
                for row in controls
            ),
            "reading": (
                "The family alone is not enough. Small-period seeds collapse the "
                "period route, so future packets must declare a seed distribution "
                "or generator with small-period rejection controls."
            ),
        },
        {
            "id": "hardness_theorem_gap",
            "status": "open_theorem_obligation",
            "passed": True,
            "reading": (
                "T449 proves no period-hardness theorem. The live D2 burden is a "
                "hidden-order/cycle-length lower bound or reduction, not another "
                "finite witness."
            ),
        },
    ]


def run() -> dict[str, Any]:
    family = family_period_audit()
    controls = small_period_seed_controls()
    route = t438_classification_for_period_packet()
    screen = absorber_screen(family, controls, route)
    passed = all(item["passed"] for item in screen)

    return {
        "artifact": ARTIFACT,
        "sources": {
            "d2_open_problem": SOURCE_D2,
            "t420": SOURCE_T420,
            "t438": SOURCE_T438,
            "t448": SOURCE_T448,
        },
        "purpose": (
            "After T448 absorbed the open-chain route, sharpen T438's closed "
            "public-permutation period-hardness path into an exact hidden-order "
            "theorem target."
        ),
        "packet": {
            "name": "bbs_hidden_order_period_packet",
            "transition": "F_N(x) = x^2 mod N on QR_N",
            "security_parameter": "bit length of N in a Blum-integer family",
            "period_problem": (
                "Given public N, seed x in QR_N, and y = F_N(x), recover x by "
                "determining the orbit period L and computing F_N^(L-1)(y)."
            ),
            "named_burden": (
                "hidden-order/cycle-length hardness for public squaring in RSA/Blum "
                "groups; theorem target only in this repo artifact"
            ),
            "not_used_as_evidence": [
                "bounded toy non-recovery",
                "single fixed finite instance",
                "point square-root inversion alone",
                "thermodynamic cost",
                "symmetric complexity growth",
            ],
        },
        "t438_route": route,
        "family_period_audit": family,
        "small_period_seed_controls": controls,
        "absorber_screen": screen,
        "overall_verdict": {
            "verdict": VERDICT if passed else "E2_PERIOD_HARDNESS_PACKET_BLOCKED",
            "screen_passed": passed,
            "d2_decision": "none; redesign/abandon remains separately gated",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "The best remaining D2 route is now sharply typed: a closed public "
                "squaring family where the missing capability object is the orbit "
                "period. If the period is known, reversal is public; if group-order "
                "trapdoor data is admitted, the toy family is completed. What is "
                "not earned is the hardness theorem. Future progress needs a real "
                "hidden-order/cycle-length reduction or lower-bound target, plus "
                "seed-distribution controls."
            ),
        },
        "recommended_next": [
            "Do not build another finite D2 toy unless it changes the theorem obligation.",
            "If D2 continues, write a theorem-target note for hidden-order cycle length: exact assumption, seed distribution, and reduction/lower-bound burden.",
            "If no such theorem target is acceptable, demote the temporal route back to T417's static E2 boundary.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {label} | {n} | {seed} | {order} | {period} | {pred} | {group} |".format(
            label=row["modulus"]["label"],
            n=row["modulus"]["n"],
            seed=row["seed"],
            order=row["order_of_seed"],
            period=row["period_formula"],
            pred="yes" if row["period_known_reverses_target"] else "no",
            group="yes" if row["qr_group_order_recovers_factorization"] else "no",
        )
        for row in result["family_period_audit"]["rows"]
    ]
    screen_rows = [
        "| {id} | {status} | {passed} |".format(
            id=item["id"],
            status=item["status"],
            passed="yes" if item["passed"] else "no",
        )
        for item in result["absorber_screen"]
    ]
    controls = [
        "| {label} | {n} | {period} | {admitted} |".format(
            label=row["modulus"]["label"],
            n=row["modulus"]["n"],
            period=row["period_formula"],
            admitted="yes" if row["admitted_as_period_hardness_evidence"] else "no",
        )
        for row in result["small_period_seed_controls"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T449 - E2 Period-Hardness Packet Audit - v0.1 results",
            "",
            "> Recorded-tier period-hardness packet audit. `TESTS.md`, "
            "`ROADMAP.md`, and `CLAIM-LEDGER.md` are untouched. No D2 "
            "redesign/abandon decision, no claim promotion, no public posture.",
            "",
            "- Spec: `tests/T449-e2-period-hardness-packet-audit.md`",
            "- Model: `models/e2_period_hardness_packet_audit.py`",
            "- Tests: `tests/test_e2_period_hardness_packet_audit.py`",
            "- Artifact JSON: `results/T449-e2-period-hardness-packet-audit-v0.1.json`",
            "- Sources: T420, T438, T448, and the D2 open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Packet",
            "",
            "- Transition: `{}`".format(result["packet"]["transition"]),
            "- Period problem: {}".format(result["packet"]["period_problem"]),
            "- Named burden: {}".format(result["packet"]["named_burden"]),
            "- T438 route: `{}` / `{}`".format(
                result["t438_route"]["route"],
                result["t438_route"]["label"],
            ),
            "",
            "## Family Period Audit",
            "",
            "| modulus | N | selected seed | ord_N(seed) | period | period reverses? | QR order gives factors? |",
            "| --- | ---: | ---: | ---: | ---: | --- | --- |",
            *rows,
            "",
            "## Small-Period Controls",
            "",
            "| modulus | N | period | admitted as evidence? |",
            "| --- | ---: | ---: | --- |",
            *controls,
            "",
            "## Absorber Screen",
            "",
            "| check | status | passed? |",
            "| --- | --- | --- |",
            *screen_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a sharper D2 target. The live closed-regime packet is not point "
            "inversion or open-chain coupling; it is hidden-order cycle-length "
            "hardness for public squaring, with seed-distribution controls.",
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
        json_path = results_dir / "T449-e2-period-hardness-packet-audit-v0.1.json"
        md_path = results_dir / "T449-e2-period-hardness-packet-audit-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
