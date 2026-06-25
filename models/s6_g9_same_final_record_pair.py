"""G9: same final record, different presheaf capability pair.

This is the clean S1/S6 non-factorization witness:

    aF_phase = aF_plain
    Cap(F_phase) != Cap(F_plain)

Both presheaves have the same pointer/provenance data, so the G8 generic finite
descent engine returns the same associated record. Only the phase-side local
capability differs, and that capability is not preserved in the final record.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.s6_g8_finite_sheaf_engine import (
    DESCENT_SUPPORT,
    FIELDS,
    FieldPolicy,
    LocalRecord,
    finite_associated_record,
    finite_site,
)


@dataclass(frozen=True)
class PresheafCase:
    name: str
    records: tuple[LocalRecord, ...]
    capabilities: tuple[str, ...]


def run_g9_same_final_record_pair() -> dict[str, Any]:
    phase_case = phase_sensitive_case()
    plain_case = plain_case_without_phase()
    site = finite_site()
    policies = tuple(FieldPolicy(field, DESCENT_SUPPORT) for field in FIELDS)
    phase_final = finite_associated_record(site, phase_case.records, policies)
    plain_final = finite_associated_record(site, plain_case.records, policies)
    same_final_record = (
        phase_final.values == plain_final.values
        and phase_final.final_capabilities == plain_final.final_capabilities
    )
    cap_diff = set(phase_case.capabilities) != set(plain_case.capabilities)
    checks = {
        "same_associated_record": same_final_record,
        "different_presheaf_capability": cap_diff,
        "phase_capability_lost": "phase_sensitive_branch" in phase_final.eta_loss,
        "plain_case_has_no_phase_loss": "phase_sensitive_branch"
        not in plain_final.eta_loss,
        "non_factorization_witness": same_final_record and cap_diff,
    }
    return {
        "test": "s6-g9-same-final-record-capability-pair-v0.1",
        "tag": ["finite_witness", "capability_non_factorization", "no_claim_promotion"],
        "guardrail": (
            "Finite same-final-record pair only: demonstrates capability loss "
            "across declared descent, not a new quantum separation theorem."
        ),
        "phase_case": _case_to_dict(phase_case),
        "plain_case": _case_to_dict(plain_case),
        "phase_final": _final_to_dict(phase_final),
        "plain_final": _final_to_dict(plain_final),
        "checks": checks,
        "all_checks_passed": all(checks.values()),
        "capability_equation": {
            "same_final_record": same_final_record,
            "phase_minus_plain": sorted(
                set(phase_case.capabilities) - set(plain_case.capabilities)
            ),
            "plain_minus_phase": sorted(
                set(plain_case.capabilities) - set(phase_case.capabilities)
            ),
        },
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "strongest_result": (
            "Two presheaf cases with the same pointer/provenance data sheafify to "
            "the same final record, but only the phase-sensitive case has the "
            "phase_sensitive_branch capability before eta_F. This is the cleanest "
            "finite S1/S6 non-factorization witness so far."
        ),
        "first_obstruction": (
            "The capability difference is intentionally finite and declared. A "
            "stronger witness should source the capability difference from a known "
            "quantum task or resource monotone."
        ),
        "next_step": (
            "Feed this pair into the G10 hostile absorber gauntlet and classify "
            "which neighbor owns the capability difference."
        ),
    }


def phase_sensitive_case() -> PresheafCase:
    records: list[LocalRecord] = []
    for index, context in enumerate(finite_site().contexts):
        records.append(
            LocalRecord(
                context=context,
                values={
                    "pointer": 1,
                    "prep_measure": True,
                    "measure_record": True,
                    "phase_tag": "phase_plus" if index % 2 == 0 else "phase_minus",
                },
                capabilities=(
                    "read_pointer",
                    "reconstruct_provenance_order",
                    "phase_sensitive_branch",
                ),
            )
        )
    return PresheafCase(
        name="F_phase_sensitive",
        records=tuple(records),
        capabilities=_capabilities(records),
    )


def plain_case_without_phase() -> PresheafCase:
    records: list[LocalRecord] = []
    for context in finite_site().contexts:
        records.append(
            LocalRecord(
                context=context,
                values={
                    "pointer": 1,
                    "prep_measure": True,
                    "measure_record": True,
                    "phase_tag": None,
                },
                capabilities=("read_pointer", "reconstruct_provenance_order"),
            )
        )
    return PresheafCase(
        name="F_plain_final_record_only",
        records=tuple(records),
        capabilities=_capabilities(records),
    )


def _capabilities(records: tuple[LocalRecord, ...]) -> tuple[str, ...]:
    return tuple(
        sorted({capability for record in records for capability in record.capabilities})
    )


def _case_to_dict(case: PresheafCase) -> dict[str, Any]:
    return {
        "name": case.name,
        "capabilities": list(case.capabilities),
        "records": [
            {
                "context": record.context,
                "values": record.values,
                "capabilities": list(record.capabilities),
            }
            for record in case.records
        ],
    }


def _final_to_dict(record: Any) -> dict[str, Any]:
    return {
        "values": record.values,
        "field_support": record.field_support,
        "stable": record.stable,
        "eta_loss": list(record.eta_loss),
        "final_capabilities": list(record.final_capabilities),
        "separated_classes": record.separated_classes,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_g9_same_final_record_pair(), indent=2, sort_keys=True))
