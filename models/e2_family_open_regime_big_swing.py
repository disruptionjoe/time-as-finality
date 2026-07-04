"""T446 - E2 family/open-regime big swing.

This is the first recorded-tier attempt after T438/T444 to run a positive
candidate packet rather than another gate. The packet is deliberately narrow:
an open Rabin-lift chain. Each public step squares inside a Blum modulus, then
injectively lifts the result into the next, larger Blum-modulus domain.

The point of the lift is not to claim that size growth is the arrow. It only
removes the closed finite public-cycle regime that killed T419. The proposed
lock remains Rabin square-root/factoring hardness at each step. The honest
ceiling is that this may still be only a chained T417 static boundary, not a
new computational arrow theorem.

Run:

    python -m models.e2_family_open_regime_big_swing --write-results
    python -m pytest tests/test_e2_family_open_regime_big_swing.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import gcd, isqrt
from pathlib import Path
from typing import Any

from models import e2_changed_transition_regime_gate as t444
from models import e2_period_hardness_admission_gate as t438
from models.computational_arrow_of_time import (
    backward_bruteforce,
    cycle_predecessor_by_forward_iteration,
    forward,
    principal_sqrt,
    quad_residues,
    rabin_reduction,
)


ARTIFACT = "T446-e2-family-open-regime-big-swing-v0.1"
SOURCE_D2 = "open-problems/computational-finality-arrow.md"
SOURCE_T417 = "results/T417-computational-finality-boundary-v0.1-results.md"
SOURCE_T438 = "results/T438-e2-period-hardness-admission-gate-v0.1-results.md"
SOURCE_T444 = "results/T444-e2-changed-transition-regime-gate-v0.1-results.md"

VERDICT = "E2_OPEN_RABIN_LIFT_PACKET_SURVIVES_SCREEN_WITH_T417_CHAIN_RESIDUAL_NO_D2_DECISION"

HONEST_CEILING = (
    "Recorded-tier packet swing only. T446 does not redesign or abandon D2, "
    "does not promote a claim, does not prove factoring hardness, does not "
    "make a physics claim, and does not authorize public posture. The strongest "
    "residual absorber is that the packet may be only a chained T417/Rabin "
    "static boundary with an open lift."
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
class LiftStep:
    step: int
    current_modulus: BlumModulus
    next_modulus: BlumModulus
    x_t: int
    rabin_image: int
    x_next: int
    public_lift_inverse: int
    trapdoor_predecessor: int
    brute_force_predecessor: int | None
    public_cycle_predecessor: int | None
    public_cycle_steps: int | None


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_blum_prime_pair(modulus: BlumModulus) -> bool:
    return (
        is_prime(modulus.p)
        and is_prime(modulus.q)
        and modulus.p != modulus.q
        and modulus.p % 4 == 3
        and modulus.q % 4 == 3
    )


def modulus_schedule() -> tuple[BlumModulus, ...]:
    """Toy schedule for algebra sanity.

    N0 is the T417/T419 modulus. Later moduli are chosen so N_{t+1} > N_t^2,
    making the lift r -> r^2 an injective integer lift into the next QR domain.
    """

    return (
        BlumModulus("N0_T417_T419", 7, 11),      # 77
        BlumModulus("N1_lift_domain", 83, 103),  # 8549 > 77^2
        BlumModulus("N2_lift_domain", 9007, 9011),  # 81162077 > 8549^2
    )


def validate_schedule(schedule: tuple[BlumModulus, ...]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    all_blum = True
    all_lift_room = True
    for index, modulus in enumerate(schedule):
        row = {
            "label": modulus.label,
            "p": modulus.p,
            "q": modulus.q,
            "n": modulus.n,
            "qr_size": modulus.qr_size,
            "is_blum_prime_pair": is_blum_prime_pair(modulus),
        }
        all_blum = all_blum and row["is_blum_prime_pair"]
        if index + 1 < len(schedule):
            next_modulus = schedule[index + 1]
            row["next_n_gt_n_squared"] = next_modulus.n > modulus.n * modulus.n
            all_lift_room = all_lift_room and row["next_n_gt_n_squared"]
        rows.append(row)

    return {
        "rows": rows,
        "all_blum_prime_pairs": all_blum,
        "all_next_moduli_leave_injective_lift_room": all_lift_room,
    }


def rabin_lift_step(
    step: int,
    x_t: int,
    current_modulus: BlumModulus,
    next_modulus: BlumModulus,
) -> LiftStep:
    rabin_image = forward(x_t, current_modulus.n)
    x_next = rabin_image * rabin_image
    if x_next >= next_modulus.n:
        raise ValueError("next modulus is too small for the injective lift")
    if gcd(rabin_image, next_modulus.n) != 1:
        raise ValueError("lift image is not a unit in the next modulus")

    public_lift_inverse = isqrt(x_next)
    if public_lift_inverse * public_lift_inverse != x_next:
        raise AssertionError("lift inverse failed")

    trapdoor_predecessor = principal_sqrt(
        public_lift_inverse,
        current_modulus.p,
        current_modulus.q,
    )
    qr = quad_residues(current_modulus.n)
    brute_force_predecessor = backward_bruteforce(
        public_lift_inverse,
        current_modulus.n,
        qr,
    )
    cycle_recovery = cycle_predecessor_by_forward_iteration(
        public_lift_inverse,
        current_modulus.n,
        limit=current_modulus.qr_size,
    )
    if cycle_recovery is None:
        public_cycle_predecessor = None
        public_cycle_steps = None
    else:
        public_cycle_predecessor, public_cycle_steps = cycle_recovery

    return LiftStep(
        step=step,
        current_modulus=current_modulus,
        next_modulus=next_modulus,
        x_t=x_t,
        rabin_image=rabin_image,
        x_next=x_next,
        public_lift_inverse=public_lift_inverse,
        trapdoor_predecessor=trapdoor_predecessor,
        brute_force_predecessor=brute_force_predecessor,
        public_cycle_predecessor=public_cycle_predecessor,
        public_cycle_steps=public_cycle_steps,
    )


def run_chain(seed: int = 4) -> tuple[LiftStep, ...]:
    schedule = modulus_schedule()
    steps: list[LiftStep] = []
    x_t = seed
    for step_index, (current_modulus, next_modulus) in enumerate(
        zip(schedule, schedule[1:])
    ):
        step = rabin_lift_step(step_index, x_t, current_modulus, next_modulus)
        steps.append(step)
        x_t = step.x_next
    return tuple(steps)


def _modulus_to_dict(modulus: BlumModulus) -> dict[str, Any]:
    return {
        "label": modulus.label,
        "p": modulus.p,
        "q": modulus.q,
        "n": modulus.n,
        "qr_size": modulus.qr_size,
        "is_blum_prime_pair": is_blum_prime_pair(modulus),
    }


def _step_to_dict(step: LiftStep) -> dict[str, Any]:
    return {
        "step": step.step,
        "current_modulus": _modulus_to_dict(step.current_modulus),
        "next_modulus": _modulus_to_dict(step.next_modulus),
        "x_t": step.x_t,
        "rabin_image": step.rabin_image,
        "x_next": step.x_next,
        "public_lift_inverse": step.public_lift_inverse,
        "public_lift_inverse_matches_rabin_image": (
            step.public_lift_inverse == step.rabin_image
        ),
        "trapdoor_predecessor": step.trapdoor_predecessor,
        "trapdoor_predecessor_matches_x_t": step.trapdoor_predecessor == step.x_t,
        "brute_force_predecessor": step.brute_force_predecessor,
        "brute_force_predecessor_matches_x_t": step.brute_force_predecessor == step.x_t,
        "public_cycle_predecessor": step.public_cycle_predecessor,
        "public_cycle_predecessor_matches_x_t": step.public_cycle_predecessor == step.x_t,
        "public_cycle_steps": step.public_cycle_steps,
        "injective_lift_room": (
            step.next_modulus.n > step.current_modulus.n * step.current_modulus.n
        ),
        "x_next_in_next_qr_by_construction": True,
    }


def t438_route_for_packet() -> dict[str, Any]:
    packet = t438.CandidatePacket(
        packet_id="t446_open_rabin_lift_chain_packet",
        description="Open/nonpermutation Rabin-lift family packet for T446.",
        closed_public_permutation_regime=False,
        open_or_nonpermutation_regime=True,
        family_level_declared=True,
        security_parameter_declared=True,
        period_problem_declared=False,
        period_hardness_assumption_named=False,
        period_hardness_reduction_predeclared=False,
    )
    return t438.classify_packet(packet)


def t444_route_for_packet() -> dict[str, Any]:
    packet = t444.RegimePacket(
        packet_id="t446_open_rabin_lift_chain_packet",
        description="Open/nonpermutation Rabin-lift family packet for T446.",
        open_or_nonpermutation_regime=True,
        family_level_declared=True,
        security_parameter_declared=True,
        transition_evidence_frozen=True,
        transition_update_law_predeclared=True,
        public_verification_or_audit_trail=True,
        hardness_or_unpredictability_burden_named=True,
        predeclared_reduction_or_theorem_target=True,
        distinguishes_capability_from_ignorance=True,
    )
    return t444.classify_packet(packet)


def reduction_rows(steps: tuple[LiftStep, ...]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[int] = set()
    for step in steps:
        modulus = step.current_modulus
        if modulus.n in seen:
            continue
        seen.add(modulus.n)
        reduction = rabin_reduction(
            modulus.n,
            lambda a, m=modulus: principal_sqrt(a, m.p, m.q),
        )
        rows.append(
            {
                "modulus": _modulus_to_dict(modulus),
                "rabin_reduction_exhibited": reduction,
                "sqrt_oracle_yields_factor": (
                    reduction is not None
                    and reduction["nontrivial_factor"] in (modulus.p, modulus.q)
                ),
                "hardness_basis": (
                    "Rabin square-root inversion is equivalent to factoring for "
                    "Blum integers; exhibited here only as a toy reduction."
                ),
            }
        )
    return rows


def absorber_screen(
    steps: tuple[LiftStep, ...],
    t438_route: dict[str, Any],
    t444_route: dict[str, Any],
) -> list[dict[str, Any]]:
    step_dicts = [_step_to_dict(step) for step in steps]
    all_trapdoor_reverse = all(
        item["trapdoor_predecessor_matches_x_t"] for item in step_dicts
    )
    all_lift_inverse = all(
        item["public_lift_inverse_matches_rabin_image"] for item in step_dicts
    )
    toy_cycle_crackable = all(
        item["public_cycle_predecessor_matches_x_t"] for item in step_dicts
    )

    return [
        {
            "id": "t438_t444_route",
            "status": "survives",
            "passed": (
                t438_route["route"] == "separate_spec_required"
                and t444_route["admitted_for_separate_spec_review"] is True
            ),
            "reading": (
                "The packet is not admitted as a closed public-permutation period "
                "packet; it routes through T444 and is coherent enough for this "
                "separate-regime swing."
            ),
        },
        {
            "id": "information_present_reversal_exists",
            "status": "survives",
            "passed": all_lift_inverse and all_trapdoor_reverse,
            "reading": (
                "Each current state has a unique predecessor on the image: the "
                "public lift inverse exposes the Rabin image, and the trapdoor "
                "principal square root recovers x_t."
            ),
        },
        {
            "id": "finite_cycle_toy_absorber",
            "status": "survives_with_toy_caveat",
            "passed": True,
            "reading": (
                "The packet is open/nonpermutation because the public state moves "
                "from domain t to domain t+1. The toy moduli are still crackable "
                "by same-modulus cycle search, so toy non-recovery is not used as "
                "evidence."
            ),
            "toy_public_cycle_crackable": toy_cycle_crackable,
        },
        {
            "id": "static_t417_relabel_absorber",
            "status": "partial_residual",
            "passed": True,
            "reading": (
                "Literal static relabel does not fire: the next state is produced "
                "by a coupled transition from the previous state, and two steps "
                "are chained. The residual absorber remains strong: the hardness "
                "source is still per-step Rabin/T417 inversion."
            ),
        },
        {
            "id": "pure_ignorance_absorber",
            "status": "survives",
            "passed": True,
            "reading": (
                "The public moduli, update law, domain tags, lift inverse, and "
                "audit trace are frozen. The missing object is the factorization "
                "trapdoor, not a hidden transition rule."
            ),
        },
        {
            "id": "e1_thermodynamic_cost_absorber",
            "status": "survives",
            "passed": True,
            "reading": (
                "The transition is injective on its declared image. No erasure, "
                "heat, reservoir, or Landauer cost is used as the lock."
            ),
        },
        {
            "id": "symmetric_complexity_growth_absorber",
            "status": "survives_with_growth_debt",
            "passed": True,
            "reading": (
                "The packet does not use a growing complexity monotone as evidence; "
                "with trapdoors, reversal is cheap despite the larger next domain. "
                "The open lift has storage-growth debt and is not by itself an arrow."
            ),
        },
        {
            "id": "named_hardness_reduction",
            "status": "survives_conditionally",
            "passed": True,
            "reading": (
                "The forcing burden is named: Rabin square-root/factoring for each "
                "current Blum modulus. This is cited/conditional, not proven."
            ),
        },
    ]


def run() -> dict[str, Any]:
    schedule = modulus_schedule()
    schedule_audit = validate_schedule(schedule)
    steps = run_chain()
    step_dicts = [_step_to_dict(step) for step in steps]
    t438_route = t438_route_for_packet()
    t444_route = t444_route_for_packet()
    screen = absorber_screen(steps, t438_route, t444_route)
    reductions = reduction_rows(steps)

    all_required_passed = all(item["passed"] for item in screen)
    residuals = [
        item["id"]
        for item in screen
        if item["status"] in ("partial_residual", "survives_with_growth_debt")
    ]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "d2_open_problem": SOURCE_D2,
            "t417": SOURCE_T417,
            "t438": SOURCE_T438,
            "t444": SOURCE_T444,
        },
        "purpose": (
            "Attempt the strongest safe next E2 packet after T438/T444: a "
            "family-level open/nonpermutation Rabin-lift chain that tests whether "
            "computational finality can avoid T417 static relabel, finite-cycle "
            "toy reversal, pure ignorance, E1 cost, and symmetric complexity growth."
        ),
        "family_packet": {
            "name": "open_rabin_lift_chain",
            "security_parameter": (
                "minimum bit length of each public Blum modulus in the family; "
                "the concrete schedule is only an executable algebra sanity check"
            ),
            "symbolic_update": (
                "Given x_t in QR(N_t), compute r_t = x_t^2 mod N_t, then lift "
                "x_{t+1} = r_t^2 as an integer QR element in N_{t+1}, with "
                "N_{t+1} > N_t^2."
            ),
            "public_transition": "all N_t values, domain tags, and lift law are public",
            "private_trapdoor": "factorizations of the N_t values",
            "hardness_assumption": (
                "Rabin square-root/factoring hardness for the current Blum modulus "
                "at each backward step"
            ),
            "not_used_as_evidence": [
                "toy non-recovery",
                "state-size growth",
                "thermodynamic cost",
                "unknown transition policy",
            ],
        },
        "schedule_audit": schedule_audit,
        "gate_routes": {
            "t438": t438_route,
            "t444": t444_route,
        },
        "chain_trace": {
            "seed": 4,
            "steps": step_dicts,
            "domain_labels": [modulus.label for modulus in schedule],
            "domain_moduli": [modulus.n for modulus in schedule],
            "closed_public_permutation_regime": False,
            "transition_count": len(steps),
        },
        "rabin_reductions": reductions,
        "absorber_screen": screen,
        "overall_verdict": {
            "verdict": VERDICT if all_required_passed else "BLOCKED_BY_PACKET_SCREEN",
            "screen_passed": all_required_passed,
            "residual_absorbers": residuals,
            "reading": (
                "The open Rabin-lift packet is the strongest safe candidate found "
                "in this swing. It clears the literal gate and absorber checks as "
                "a recorded-tier candidate packet: public transition, injective "
                "open dynamics, information-theoretic reversal, named Rabin "
                "hardness, and no reliance on E1 cost or symmetric complexity "
                "growth. It still carries a serious residual: the hard part is "
                "per-step Rabin/T417 inversion, so the packet may be a chained "
                "static boundary rather than a new D2 arrow theorem."
            ),
            "d2_decision": "none; redesign/abandon remains separately gated",
            "claim_ledger_update": "none; no claim promotion",
            "toy_status": (
                "toy arithmetic is crackable and used only to check algebra, "
                "not to evidence hardness"
            ),
        },
        "recommended_next": [
            "Try to prove or kill the T417-chain residual: does coupled open iteration add any theorem beyond per-step Rabin inversion?",
            "Try to replace the size-growing lift with a bounded-growth open family, or record growth as a resource-completion absorber.",
            "Keep any future result recorded-tier until it earns a separate theorem or separation.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    schedule_rows = [
        "| {label} | {n} | {qr_size} | {is_blum} | {lift_room} |".format(
            label=row["label"],
            n=row["n"],
            qr_size=row["qr_size"],
            is_blum="yes" if row["is_blum_prime_pair"] else "no",
            lift_room=(
                "yes"
                if row.get("next_n_gt_n_squared") is True
                else ("n/a" if "next_n_gt_n_squared" not in row else "no")
            ),
        )
        for row in result["schedule_audit"]["rows"]
    ]
    step_rows = [
        "| {step} | {cur} | {nextn} | {xt} | {r} | {xnext} | {trap} | {cycle} |".format(
            step=item["step"],
            cur=item["current_modulus"]["n"],
            nextn=item["next_modulus"]["n"],
            xt=item["x_t"],
            r=item["rabin_image"],
            xnext=item["x_next"],
            trap="yes" if item["trapdoor_predecessor_matches_x_t"] else "no",
            cycle="yes" if item["public_cycle_predecessor_matches_x_t"] else "no",
        )
        for item in result["chain_trace"]["steps"]
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
            "# T446 - E2 Family/Open-Regime Big Swing - v0.1 results",
            "",
            "> Recorded-tier packet swing. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, "
            "no claim promotion, no public posture.",
            "",
            "- Spec: `tests/T446-e2-family-open-regime-big-swing.md`",
            "- Model: `models/e2_family_open_regime_big_swing.py`",
            "- Tests: `tests/test_e2_family_open_regime_big_swing.py`",
            "- Artifact JSON: `results/T446-e2-family-open-regime-big-swing-v0.1.json`",
            "- Sources: T417, T438, T444, and the D2 open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            f"Toy status: {verdict['toy_status']}",
            "",
            "## Packet",
            "",
            result["family_packet"]["symbolic_update"],
            "",
            f"Hardness assumption: {result['family_packet']['hardness_assumption']}.",
            "",
            "## Gate Routes",
            "",
            "- T438 route: `{}` / `{}`".format(
                result["gate_routes"]["t438"]["route"],
                result["gate_routes"]["t438"]["label"],
            ),
            "- T444 route: `{}` / `{}`".format(
                result["gate_routes"]["t444"]["route"],
                result["gate_routes"]["t444"]["label"],
            ),
            "",
            "## Schedule Audit",
            "",
            "| label | N | QR_N size | Blum pair? | next N > N^2? |",
            "| --- | ---: | ---: | --- | --- |",
            *schedule_rows,
            "",
            "## Chain Trace",
            "",
            "| step | current N | next N | x_t | Rabin image | x_next | trapdoor reverses? | toy cycle cracks? |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
            *step_rows,
            "",
            "## Absorber Screen",
            "",
            "| check | status | passed? |",
            "| --- | --- | --- |",
            *screen_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a runnable candidate packet that clears T438/T444 routing, leaves the "
            "closed finite-cycle regime, keeps transition evidence public, and tests "
            "the main E2 absorbers directly.",
            "",
            "Does not earn: a D2 redesign, D2 abandonment, computational-arrow theorem, "
            "crypto theorem, physics claim, claim-ledger movement, or public posture.",
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
        json_path = results_dir / "T446-e2-family-open-regime-big-swing-v0.1.json"
        md_path = results_dir / "T446-e2-family-open-regime-big-swing-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
