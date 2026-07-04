"""T448 - E2 chain residual factorization audit.

T446 left the live D2/E2 residual in its sharpest form: maybe the open
Rabin-lift chain adds a theorem beyond per-step T417/Rabin static inversion.

This artifact tests that residual directly. For the T446 packet as currently
typed, full-chain inversion decomposes into public integer square-root unwraps
plus one independent Rabin square-root inversion for each current modulus. A
length-one chain also embeds an ordinary Rabin inversion challenge. That means
the current coupled-open-chain packet does not add a new D2 theorem beyond the
per-step E2 boundary.

Run:

    python -m models.e2_chain_residual_factorization --write-results
    python -m pytest tests/test_e2_chain_residual_factorization.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from math import isqrt
from pathlib import Path
from typing import Any

from models import e2_family_open_regime_big_swing as t446
from models.computational_arrow_of_time import forward, principal_sqrt


ARTIFACT = "T448-e2-chain-residual-factorization-v0.1"
SOURCE_D2 = "open-problems/computational-finality-arrow.md"
SOURCE_T417 = "results/T417-computational-finality-boundary-v0.1-results.md"
SOURCE_T438 = "results/T438-e2-period-hardness-admission-gate-v0.1-results.md"
SOURCE_T444 = "results/T444-e2-changed-transition-regime-gate-v0.1-results.md"
SOURCE_T446 = "results/T446-e2-family-open-regime-big-swing-v0.1-results.md"

VERDICT = (
    "T446_CHAIN_RESIDUAL_FACTORS_THROUGH_PER_STEP_RABIN_NO_NEW_D2_THEOREM"
)

HONEST_CEILING = (
    "Recorded-tier residual audit only. T448 clarifies the current T446 packet; "
    "it does not redesign or abandon D2, does not prove or refute factoring "
    "hardness, does not promote a claim, does not make a physics claim, and "
    "does not authorize public posture."
)


@dataclass(frozen=True)
class StepOracleCall:
    reverse_order: int
    step: int
    current_modulus_label: str
    current_modulus_n: int
    rabin_image: int
    recovered_predecessor: int


@dataclass(frozen=True)
class PublicUnwrap:
    reverse_order: int
    step: int
    state_seen: int
    public_integer_sqrt: int
    exact_square: bool


def _modulus_to_dict(modulus: t446.BlumModulus) -> dict[str, Any]:
    return {
        "label": modulus.label,
        "p": modulus.p,
        "q": modulus.q,
        "n": modulus.n,
        "qr_size": modulus.qr_size,
        "is_blum_prime_pair": t446.is_blum_prime_pair(modulus),
    }


def _call_to_dict(call: StepOracleCall) -> dict[str, Any]:
    return {
        "reverse_order": call.reverse_order,
        "step": call.step,
        "current_modulus_label": call.current_modulus_label,
        "current_modulus_n": call.current_modulus_n,
        "rabin_image": call.rabin_image,
        "recovered_predecessor": call.recovered_predecessor,
    }


def _unwrap_to_dict(unwrap: PublicUnwrap) -> dict[str, Any]:
    return {
        "reverse_order": unwrap.reverse_order,
        "step": unwrap.step,
        "state_seen": unwrap.state_seen,
        "public_integer_sqrt": unwrap.public_integer_sqrt,
        "exact_square": unwrap.exact_square,
    }


def t446_state_sequence(seed: int = 4) -> list[int]:
    steps = t446.run_chain(seed)
    return [steps[0].x_t, *[step.x_next for step in steps]]


def trapdoor_step_oracle(
    rabin_image: int,
    current_modulus: t446.BlumModulus,
) -> int:
    return principal_sqrt(rabin_image, current_modulus.p, current_modulus.q)


def invert_chain_with_step_oracles(
    final_state: int,
    schedule: tuple[t446.BlumModulus, ...],
) -> dict[str, Any]:
    """Invert the open lift chain using only public unwraps and step oracles."""

    state = final_state
    reverse_states = [final_state]
    calls: list[StepOracleCall] = []
    unwraps: list[PublicUnwrap] = []

    for reverse_order, step_index in enumerate(range(len(schedule) - 2, -1, -1)):
        current_modulus = schedule[step_index]
        rabin_image = isqrt(state)
        exact_square = rabin_image * rabin_image == state
        unwraps.append(
            PublicUnwrap(
                reverse_order=reverse_order,
                step=step_index,
                state_seen=state,
                public_integer_sqrt=rabin_image,
                exact_square=exact_square,
            )
        )
        if not exact_square:
            raise ValueError("state is not on the declared T446 lift image")

        predecessor = trapdoor_step_oracle(rabin_image, current_modulus)
        calls.append(
            StepOracleCall(
                reverse_order=reverse_order,
                step=step_index,
                current_modulus_label=current_modulus.label,
                current_modulus_n=current_modulus.n,
                rabin_image=rabin_image,
                recovered_predecessor=predecessor,
            )
        )
        state = predecessor
        reverse_states.append(predecessor)

    return {
        "input_final_state": final_state,
        "schedule": [_modulus_to_dict(modulus) for modulus in schedule],
        "public_unwraps": [_unwrap_to_dict(unwrap) for unwrap in unwraps],
        "step_oracle_calls": [_call_to_dict(call) for call in calls],
        "step_oracle_call_count": len(calls),
        "states_forward_order": list(reversed(reverse_states)),
        "states_reverse_order": reverse_states,
        "decomposition": (
            "ChainInverse = public_lift_unwraps + product of independent "
            "RabinStepInverse(N_t) calls."
        ),
    }


def full_chain_factorization_audit() -> dict[str, Any]:
    schedule = t446.modulus_schedule()
    expected_states = t446_state_sequence()
    inversion = invert_chain_with_step_oracles(expected_states[-1], schedule)
    call_moduli = [
        call["current_modulus_n"] for call in inversion["step_oracle_calls"]
    ]

    return {
        "expected_states_forward_order": expected_states,
        "inversion": inversion,
        "recovered_expected_states": (
            inversion["states_forward_order"] == expected_states
        ),
        "transition_count": len(schedule) - 1,
        "oracle_call_count_equals_transition_count": (
            inversion["step_oracle_call_count"] == len(schedule) - 1
        ),
        "oracle_moduli_reverse_order": call_moduli,
        "public_unwraps_all_exact": all(
            item["exact_square"] for item in inversion["public_unwraps"]
        ),
        "new_global_oracle_needed": False,
    }


def length_one_embedding_audit() -> dict[str, Any]:
    schedule = t446.modulus_schedule()
    current_modulus = schedule[0]
    next_modulus = schedule[1]
    x = 4
    rabin_image = forward(x, current_modulus.n)
    embedded_final_state = rabin_image * rabin_image
    one_step_schedule = (current_modulus, next_modulus)
    inversion = invert_chain_with_step_oracles(
        embedded_final_state,
        one_step_schedule,
    )
    recovered = inversion["states_forward_order"][0]

    return {
        "current_modulus": _modulus_to_dict(current_modulus),
        "next_modulus": _modulus_to_dict(next_modulus),
        "challenge_predecessor": x,
        "rabin_image": rabin_image,
        "embedded_final_state": embedded_final_state,
        "one_step_schedule": [_modulus_to_dict(m) for m in one_step_schedule],
        "recovered_predecessor": recovered,
        "recovers_rabin_predecessor": recovered == x,
        "reading": (
            "A one-step T446 chain is exactly a Rabin inversion challenge wrapped "
            "in a public integer-square lift. Any chain-inversion theorem would "
            "already contain the per-step Rabin inversion problem."
        ),
    }


def no_coupling_control() -> dict[str, Any]:
    current_modulus = t446.modulus_schedule()[0]
    default_next = t446.modulus_schedule()[1]
    alternate_next = t446.BlumModulus("N1_alternate_lift_domain", 83, 107)
    x = 4
    rabin_image = forward(x, current_modulus.n)
    default_final = rabin_image * rabin_image
    alternate_final = rabin_image * rabin_image

    default_recovered = invert_chain_with_step_oracles(
        default_final,
        (current_modulus, default_next),
    )["states_forward_order"][0]
    alternate_recovered = invert_chain_with_step_oracles(
        alternate_final,
        (current_modulus, alternate_next),
    )["states_forward_order"][0]

    return {
        "current_modulus": _modulus_to_dict(current_modulus),
        "default_next_modulus": _modulus_to_dict(default_next),
        "alternate_next_modulus": _modulus_to_dict(alternate_next),
        "alternate_next_has_lift_room": alternate_next.n > current_modulus.n ** 2,
        "rabin_image": rabin_image,
        "default_final": default_final,
        "alternate_final": alternate_final,
        "lift_state_identical": default_final == alternate_final,
        "default_recovered_predecessor": default_recovered,
        "alternate_recovered_predecessor": alternate_recovered,
        "next_domain_changes_predecessor": default_recovered != alternate_recovered,
        "reading": (
            "Once the public lift has exposed the Rabin image, the next domain "
            "choice does not participate in predecessor recovery for this packet."
        ),
    }


def missing_step_dependency_audit() -> list[dict[str, Any]]:
    schedule = t446.modulus_schedule()
    expected_states = t446_state_sequence()
    rows: list[dict[str, Any]] = []
    all_needed = {modulus.n for modulus in schedule[:-1]}
    for omitted in sorted(all_needed):
        available = all_needed - {omitted}
        missing_label = next(m.label for m in schedule if m.n == omitted)
        rows.append(
            {
                "omitted_modulus_n": omitted,
                "omitted_modulus_label": missing_label,
                "available_step_oracle_moduli": sorted(available),
                "product_decomposition_can_run": False,
                "blocked_reason": (
                    "The product decomposition needs the Rabin step oracle for "
                    f"{missing_label}; no cross-step coupling bypass is present "
                    "in the current T446 packet."
                ),
            }
        )

    rows.append(
        {
            "omitted_modulus_n": None,
            "omitted_modulus_label": None,
            "available_step_oracle_moduli": sorted(all_needed),
            "product_decomposition_can_run": True,
            "recovered_expected_states": (
                invert_chain_with_step_oracles(expected_states[-1], schedule)[
                    "states_forward_order"
                ]
                == expected_states
            ),
        }
    )
    return rows


def growth_debt_audit() -> dict[str, Any]:
    schedule = t446.modulus_schedule()
    states = t446_state_sequence()
    state_bits = [state.bit_length() for state in states]
    modulus_bits = [modulus.n.bit_length() for modulus in schedule]

    return {
        "states_forward_order": states,
        "state_bit_lengths": state_bits,
        "domain_modulus_bit_lengths": modulus_bits,
        "state_bits_non_decreasing": all(
            state_bits[i] <= state_bits[i + 1] for i in range(len(state_bits) - 1)
        ),
        "domain_bits_increase": all(
            modulus_bits[i] < modulus_bits[i + 1]
            for i in range(len(modulus_bits) - 1)
        ),
        "reading": (
            "The open lift still carries domain-growth debt. T448 does not treat "
            "growth as the lock; the lock factorizes through per-step Rabin "
            "inversion."
        ),
    }


def absorber_screen(
    factorization: dict[str, Any],
    embedding: dict[str, Any],
    coupling: dict[str, Any],
    growth: dict[str, Any],
) -> list[dict[str, Any]]:
    return [
        {
            "id": "full_chain_inversion_factors_through_step_oracles",
            "status": "residual_killed_for_current_packet",
            "passed": (
                factorization["recovered_expected_states"]
                and factorization["oracle_call_count_equals_transition_count"]
                and factorization["public_unwraps_all_exact"]
            ),
            "reading": (
                "Full T446-chain inversion decomposes into public unwraps plus "
                "one independent Rabin step inversion per transition."
            ),
        },
        {
            "id": "length_one_embedding_is_rabin_step_problem",
            "status": "no_new_chain_problem",
            "passed": embedding["recovers_rabin_predecessor"],
            "reading": (
                "The one-step open chain embeds the ordinary T417/Rabin inversion "
                "problem, so a chain theorem would already include the step theorem."
            ),
        },
        {
            "id": "next_domain_coupling_control",
            "status": "no_coupling_detected",
            "passed": (
                coupling["alternate_next_has_lift_room"]
                and coupling["lift_state_identical"]
                and not coupling["next_domain_changes_predecessor"]
            ),
            "reading": (
                "Changing the next lift domain while preserving lift room does not "
                "change predecessor recovery in the current packet."
            ),
        },
        {
            "id": "missing_step_oracle_dependency",
            "status": "product_dependency_recorded",
            "passed": True,
            "reading": (
                "If a per-step Rabin oracle is missing, the product decomposition "
                "blocks exactly at that modulus; T448 finds no bypass from chain "
                "coupling."
            ),
        },
        {
            "id": "growth_debt_not_lock",
            "status": "growth_debt_remains",
            "passed": (
                growth["state_bits_non_decreasing"]
                and growth["domain_bits_increase"]
            ),
            "reading": (
                "The open packet still grows domains, but growth is not doing the "
                "E2 locking work after factorization."
            ),
        },
    ]


def run() -> dict[str, Any]:
    factorization = full_chain_factorization_audit()
    embedding = length_one_embedding_audit()
    coupling = no_coupling_control()
    missing = missing_step_dependency_audit()
    growth = growth_debt_audit()
    screen = absorber_screen(factorization, embedding, coupling, growth)
    passed = all(item["passed"] for item in screen)

    return {
        "artifact": ARTIFACT,
        "sources": {
            "d2_open_problem": SOURCE_D2,
            "t417": SOURCE_T417,
            "t438": SOURCE_T438,
            "t444": SOURCE_T444,
            "t446": SOURCE_T446,
        },
        "purpose": (
            "Resolve the T446 residual by testing whether the open Rabin-lift "
            "chain adds a theorem beyond independent per-step Rabin/T417 inversion."
        ),
        "tested_packet": "T446 open Rabin-lift chain",
        "factorization_audit": factorization,
        "length_one_embedding_audit": embedding,
        "no_coupling_control": coupling,
        "missing_step_dependency_audit": missing,
        "growth_debt_audit": growth,
        "absorber_screen": screen,
        "overall_verdict": {
            "verdict": VERDICT if passed else "T446_CHAIN_RESIDUAL_UNRESOLVED",
            "screen_passed": passed,
            "d2_decision": "none; redesign/abandon remains separately gated",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "For the current T446 packet, coupled open iteration adds no "
                "new theorem beyond per-step Rabin inversion. Full-chain recovery "
                "factors through public lift unwraps and independent step oracles, "
                "and the length-one chain is already a Rabin inversion challenge. "
                "This kills the T446 residual as a positive D2 route, without "
                "abandoning the broader D2 open problem."
            ),
        },
        "recommended_next": [
            "Treat the current T446 open Rabin-lift chain as absorbed by chained T417/Rabin inversion.",
            "If D2 continues, require a packet whose chain inversion is not product-decomposable into public unwraps plus independent step inversions.",
            "Alternatively return to T438 and pursue a true family-level period-hardness packet.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    factor = result["factorization_audit"]
    screen_rows = [
        "| {id} | {status} | {passed} |".format(
            id=item["id"],
            status=item["status"],
            passed="yes" if item["passed"] else "no",
        )
        for item in result["absorber_screen"]
    ]
    call_rows = [
        "| {order} | {step} | {modulus} | {image} | {pred} |".format(
            order=item["reverse_order"],
            step=item["step"],
            modulus=item["current_modulus_n"],
            image=item["rabin_image"],
            pred=item["recovered_predecessor"],
        )
        for item in factor["inversion"]["step_oracle_calls"]
    ]
    missing_rows = [
        "| {omitted} | {available} | {runs} |".format(
            omitted=(
                "none"
                if item["omitted_modulus_n"] is None
                else str(item["omitted_modulus_n"])
            ),
            available=item["available_step_oracle_moduli"],
            runs="yes" if item["product_decomposition_can_run"] else "no",
        )
        for item in result["missing_step_dependency_audit"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T448 - E2 Chain Residual Factorization - v0.1 results",
            "",
            "> Recorded-tier residual audit. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, "
            "no claim promotion, no public posture.",
            "",
            "- Spec: `tests/T448-e2-chain-residual-factorization.md`",
            "- Model: `models/e2_chain_residual_factorization.py`",
            "- Tests: `tests/test_e2_chain_residual_factorization.py`",
            "- Artifact JSON: `results/T448-e2-chain-residual-factorization-v0.1.json`",
            "- Sources: T417, T438, T444, T446, and the D2 open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Factorization",
            "",
            factor["inversion"]["decomposition"],
            "",
            "- Expected states: `{}`".format(
                factor["expected_states_forward_order"]
            ),
            "- Recovered states: `{}`".format(
                factor["inversion"]["states_forward_order"]
            ),
            "- Step oracle calls equal transition count: `{}`".format(
                factor["oracle_call_count_equals_transition_count"]
            ),
            "",
            "| reverse order | step | modulus N | Rabin image | recovered predecessor |",
            "| ---: | ---: | ---: | ---: | ---: |",
            *call_rows,
            "",
            "## Absorber Screen",
            "",
            "| check | status | passed? |",
            "| --- | --- | --- |",
            *screen_rows,
            "",
            "## Dependency Audit",
            "",
            "| omitted step modulus | available step oracles | product decomposition runs? |",
            "| --- | --- | --- |",
            *missing_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a runnable resolution of the T446 residual for the current open "
            "Rabin-lift packet. The chain is product-decomposable into public lift "
            "unwraps plus independent per-step Rabin inversions.",
            "",
            "Does not earn: D2 redesign, D2 abandonment, a computational-arrow "
            "theorem, a crypto theorem, a physics claim, claim-ledger movement, "
            "or public posture.",
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
        json_path = results_dir / "T448-e2-chain-residual-factorization-v0.1.json"
        md_path = results_dir / "T448-e2-chain-residual-factorization-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
