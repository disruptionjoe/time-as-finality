"""G8: reusable finite sheafification / descent engine for S6.

This replaces bespoke S6 descent code with a small generic finite-site engine.
It is not a general sheafification theorem. It is a finite associated-record
reflector:

  local records on contexts
  -> declared field policies and support thresholds
  -> globally supported record values
  -> unit non-isomorphism / loss profile

The fixture consumes G7 SBS fragment scores and checks that the generic engine
reproduces the S6 threshold without special-purpose gluing logic.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any

from models.s6_g7_sbs_approximation import sbs_level


CONTEXTS: tuple[str, ...] = tuple(f"E{i}" for i in range(5))
DESCENT_SUPPORT = 4
FIELDS: tuple[str, ...] = ("pointer", "prep_measure", "measure_record")
LOSS_FIELDS: tuple[str, ...] = ("phase_tag",)


@dataclass(frozen=True)
class FiniteSite:
    contexts: tuple[str, ...]
    overlaps: tuple[tuple[str, str], ...]
    cover: tuple[str, ...]


@dataclass(frozen=True)
class LocalRecord:
    context: str
    values: dict[str, object]
    capabilities: tuple[str, ...]


@dataclass(frozen=True)
class FieldPolicy:
    field: str
    support_threshold: int
    required_value: object | None = None


@dataclass(frozen=True)
class AssociatedRecord:
    values: dict[str, object]
    field_support: dict[str, int]
    stable: bool
    local_records_used: int
    separated_classes: int
    eta_loss: tuple[str, ...]
    final_capabilities: tuple[str, ...]


def run_g8_finite_sheaf_engine() -> dict[str, Any]:
    site = finite_site()
    policies = tuple(FieldPolicy(field, DESCENT_SUPPORT) for field in FIELDS)
    pre_records = records_from_sbs_strength(1.0)
    threshold_records = records_from_sbs_strength(1.2)
    pre = finite_associated_record(site, pre_records, policies)
    threshold = finite_associated_record(site, threshold_records, policies)
    checks = {
        "site_and_cover_declared": bool(site.contexts and site.cover and site.overlaps),
        "prethreshold_not_stable": not pre.stable,
        "threshold_stable": threshold.stable,
        "all_fields_supported_at_threshold": all(
            threshold.field_support.get(field, 0) >= DESCENT_SUPPORT
            for field in FIELDS
        ),
        "eta_loss_detected": "phase_sensitive_branch" in threshold.eta_loss,
    }
    return {
        "test": "s6-g8-finite-sheaf-engine-v0.1",
        "tag": ["finite_witness", "generic_descent_engine", "no_claim_promotion"],
        "guardrail": (
            "Reusable finite descent engine only: not a general sheafification "
            "theorem and not a proof that abstract sheafification creates time."
        ),
        "site": {
            "contexts": list(site.contexts),
            "cover": list(site.cover),
            "overlap_count": len(site.overlaps),
        },
        "policies": [
            {
                "field": policy.field,
                "support_threshold": policy.support_threshold,
                "required_value": policy.required_value,
            }
            for policy in policies
        ],
        "checks": checks,
        "all_checks_passed": all(checks.values()),
        "prethreshold": _record_to_dict(pre),
        "threshold": _record_to_dict(threshold),
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "strongest_result": (
            "The generic finite descent engine reproduces the S6 threshold at "
            "strength=1.2 from field support alone: pointer and both provenance "
            "edges have support 4, the associated record is stable, and phase "
            "capability is lost across eta_F."
        ),
        "first_obstruction": (
            "This is still a finite associated-record reflector over declared "
            "fields. It does not prove general sheafification or pick the site "
            "canonically."
        ),
        "next_step": (
            "Use this generic engine to build the G9 same-final-record / "
            "different-presheaf-capability pair."
        ),
    }


def finite_site() -> FiniteSite:
    return FiniteSite(
        contexts=CONTEXTS,
        cover=CONTEXTS,
        overlaps=tuple(combinations(CONTEXTS, 2)),
    )


def records_from_sbs_strength(strength: float) -> tuple[LocalRecord, ...]:
    level = sbs_level(strength)
    records: list[LocalRecord] = []
    for index, fragment in enumerate(level.fragment_scores):
        if fragment.objective_fragment:
            values: dict[str, object] = {
                "pointer": 1,
                "prep_measure": True,
                "measure_record": True,
                "phase_tag": "phase_plus" if index % 2 == 0 else "phase_minus",
            }
            capabilities = (
                "read_pointer",
                "reconstruct_provenance_order",
                "phase_sensitive_branch",
            )
        elif fragment.redundant:
            values = {
                "pointer": 1,
                "prep_measure": True,
                "measure_record": None,
                "phase_tag": "weak_phase",
            }
            capabilities = ("read_pointer", "phase_sensitive_branch")
        else:
            values = {
                "pointer": None,
                "prep_measure": None,
                "measure_record": None,
                "phase_tag": "unread_phase",
            }
            capabilities = ("phase_sensitive_branch",)
        records.append(
            LocalRecord(
                context=fragment.name,
                values=values,
                capabilities=capabilities,
            )
        )
    return tuple(records)


def finite_associated_record(
    site: FiniteSite,
    records: tuple[LocalRecord, ...],
    policies: tuple[FieldPolicy, ...],
) -> AssociatedRecord:
    if tuple(record.context for record in records) != site.contexts:
        raise ValueError("records must be ordered by site contexts")

    values: dict[str, object] = {}
    support: dict[str, int] = {}
    for policy in policies:
        chosen, count = _supported_value(records, policy)
        support[policy.field] = count
        if count >= policy.support_threshold:
            values[policy.field] = chosen

    stable = all(field in values for field in FIELDS)
    final_capabilities = _final_capabilities(values, stable)
    presheaf_capabilities = sorted(
        {capability for record in records for capability in record.capabilities}
    )
    eta_loss = tuple(
        capability
        for capability in presheaf_capabilities
        if capability not in final_capabilities
    )
    separated_classes = len(
        {
            tuple((field, record.values.get(field)) for field in FIELDS)
            for record in records
        }
    )
    return AssociatedRecord(
        values=values if stable else {},
        field_support=support,
        stable=stable,
        local_records_used=len(records),
        separated_classes=separated_classes,
        eta_loss=eta_loss,
        final_capabilities=final_capabilities,
    )


def _supported_value(
    records: tuple[LocalRecord, ...],
    policy: FieldPolicy,
) -> tuple[object | None, int]:
    counts: dict[object, int] = {}
    for record in records:
        value = record.values.get(policy.field)
        if value is None:
            continue
        if policy.required_value is not None and value != policy.required_value:
            continue
        counts[value] = counts.get(value, 0) + 1
    if not counts:
        return None, 0
    return max(counts.items(), key=lambda item: item[1])


def _final_capabilities(values: dict[str, object], stable: bool) -> tuple[str, ...]:
    if not stable:
        return ()
    capabilities = ["read_pointer"]
    if values.get("prep_measure") and values.get("measure_record"):
        capabilities.append("reconstruct_provenance_order")
    return tuple(capabilities)


def _record_to_dict(record: AssociatedRecord) -> dict[str, Any]:
    return {
        "values": record.values,
        "field_support": record.field_support,
        "stable": record.stable,
        "local_records_used": record.local_records_used,
        "separated_classes": record.separated_classes,
        "eta_loss": list(record.eta_loss),
        "final_capabilities": list(record.final_capabilities),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_g8_finite_sheaf_engine(), indent=2, sort_keys=True))
