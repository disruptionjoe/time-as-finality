"""T151: causal-access screen for finality-boundary claims.

This artifact tests whether black-hole/finality-boundary language adds
anything beyond ordinary causal record reachability. The conservative answer
is usually no: for direct classical records, the relevant capability factors
through a declared causal-access graph. The screen preserves a narrow B1 use:
horizons are useful stress tests for observer-indexed record access, not
evidence for a new information-loss or spacetime-reconstruction claim.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RecordEvent:
    event_id: str
    region: str
    records: frozenset[str]

    def __post_init__(self) -> None:
        if not self.event_id:
            raise ValueError("event_id cannot be empty")
        if not self.region:
            raise ValueError("region cannot be empty")


@dataclass(frozen=True)
class RecordChannel:
    channel_id: str
    source: str
    target: str
    channel_kind: str
    classical_export: bool
    boundary_id: str | None = None
    boundary_direction: str = "none"
    record_character: str = "preserved"

    def __post_init__(self) -> None:
        if not self.channel_id:
            raise ValueError("channel_id cannot be empty")
        if self.boundary_direction not in {"none", "inward", "outward"}:
            raise ValueError("boundary_direction must be none, inward, or outward")
        if self.record_character not in {"preserved", "transformed", "encoded"}:
            raise ValueError("record_character must be preserved, transformed, or encoded")


@dataclass(frozen=True)
class ObserverProfile:
    observer_id: str
    collection_events: frozenset[str]
    participation_events: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if not self.observer_id:
            raise ValueError("observer_id cannot be empty")


@dataclass(frozen=True)
class CausalRecordSystem:
    events: tuple[RecordEvent, ...]
    channels: tuple[RecordChannel, ...]

    def __post_init__(self) -> None:
        event_ids = [event.event_id for event in self.events]
        if len(set(event_ids)) != len(event_ids):
            raise ValueError("event ids must be unique")
        known = set(event_ids)
        missing = {
            endpoint
            for channel in self.channels
            for endpoint in (channel.source, channel.target)
            if endpoint not in known
        }
        if missing:
            raise ValueError(f"channel references unknown events: {sorted(missing)}")

    @property
    def event_map(self) -> dict[str, RecordEvent]:
        return {event.event_id: event for event in self.events}

    @property
    def outgoing(self) -> dict[str, tuple[RecordChannel, ...]]:
        out: dict[str, list[RecordChannel]] = {}
        for channel in self.channels:
            out.setdefault(channel.source, []).append(channel)
        return {event: tuple(channels) for event, channels in out.items()}


@dataclass(frozen=True)
class AccessResult:
    accessible: bool
    direct_participation: bool
    event_path: tuple[str, ...]
    channel_path: tuple[str, ...]
    channel_kinds: tuple[str, ...]
    crossed_boundaries: tuple[str, ...]
    transformed_record: bool


@dataclass(frozen=True)
class BoundaryProfile:
    boundary_id: str
    classical_directions: tuple[str, ...]
    has_outward_classical_export: bool
    has_inward_classical_import: bool
    transformed_classical_records: bool
    permeability_class: str


@dataclass(frozen=True)
class CausalAccessCase:
    name: str
    system: CausalRecordSystem
    source_event: str
    exterior_observer: ObserverProfile
    local_observer: ObserverProfile | None
    boundary_id: str | None
    claim_scope: str


@dataclass(frozen=True)
class CausalAccessAudit:
    name: str
    classification: str
    residue_label: str
    taf_adds_independent_content: bool
    exterior_classical_access: bool
    exterior_extended_access: bool
    exterior_direct_participation: bool
    local_classical_access: bool
    boundary_permeability: str
    reason: str
    weakened_claim: str
    required_next: str


@dataclass(frozen=True)
class T151Result:
    audits: tuple[CausalAccessAudit, ...]
    remote_observation_guardrail_passed: bool
    horizon_claim_absorbed_by_causal_reachability: bool
    encoded_channel_overclaim_rejected: bool
    soft_boundary_parameterized: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    b1_update: str
    s1_update: str
    r1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def access_path(
    system: CausalRecordSystem,
    source_event: str,
    observer: ObserverProfile,
    *,
    allowed_modes: frozenset[str] = frozenset({"classical"}),
) -> AccessResult:
    if source_event not in system.event_map:
        raise KeyError(f"unknown source event: {source_event}")
    unknown_collection = observer.collection_events - set(system.event_map)
    unknown_participation = observer.participation_events - set(system.event_map)
    if unknown_collection or unknown_participation:
        missing = sorted(unknown_collection | unknown_participation)
        raise ValueError(f"observer references unknown events: {missing}")

    if source_event in observer.participation_events:
        return AccessResult(
            accessible=True,
            direct_participation=True,
            event_path=(source_event,),
            channel_path=(),
            channel_kinds=(),
            crossed_boundaries=(),
            transformed_record=False,
        )
    if source_event in observer.collection_events:
        return AccessResult(
            accessible=True,
            direct_participation=False,
            event_path=(source_event,),
            channel_path=(),
            channel_kinds=(),
            crossed_boundaries=(),
            transformed_record=False,
        )

    queue: deque[tuple[str, tuple[str, ...], tuple[RecordChannel, ...]]] = deque(
        [(source_event, (source_event,), ())]
    )
    visited = {source_event}
    outgoing = system.outgoing

    while queue:
        current, event_path, channel_path = queue.popleft()
        for channel in outgoing.get(current, ()):
            if not _edge_allowed(channel, allowed_modes):
                continue
            next_event = channel.target
            if next_event in visited:
                continue
            next_event_path = event_path + (next_event,)
            next_channel_path = channel_path + (channel,)
            if next_event in observer.collection_events:
                return _access_from_path(
                    next_event_path,
                    next_channel_path,
                    direct_participation=False,
                )
            visited.add(next_event)
            queue.append((next_event, next_event_path, next_channel_path))

    return AccessResult(
        accessible=False,
        direct_participation=False,
        event_path=(),
        channel_path=(),
        channel_kinds=(),
        crossed_boundaries=(),
        transformed_record=False,
    )


def boundary_profile(
    system: CausalRecordSystem,
    boundary_id: str | None,
) -> BoundaryProfile:
    if boundary_id is None:
        return BoundaryProfile(
            boundary_id="none",
            classical_directions=(),
            has_outward_classical_export=False,
            has_inward_classical_import=False,
            transformed_classical_records=False,
            permeability_class="not_boundary_case",
        )

    classical_boundary_channels = tuple(
        channel
        for channel in system.channels
        if channel.boundary_id == boundary_id and channel.classical_export
    )
    directions = tuple(
        sorted(
            {
                channel.boundary_direction
                for channel in classical_boundary_channels
                if channel.boundary_direction != "none"
            }
        )
    )
    has_outward = "outward" in directions
    has_inward = "inward" in directions
    transformed = any(
        channel.record_character == "transformed"
        for channel in classical_boundary_channels
    )

    if has_outward and has_inward:
        permeability = "bidirectional_classical_exchange"
    elif has_inward and not has_outward:
        permeability = "one_way_inward_only"
    elif has_outward and not has_inward:
        permeability = "one_way_outward_only"
    elif classical_boundary_channels:
        permeability = "classical_boundary_declared_without_direction"
    else:
        permeability = "no_classical_boundary_export_declared"

    return BoundaryProfile(
        boundary_id=boundary_id,
        classical_directions=directions,
        has_outward_classical_export=has_outward,
        has_inward_classical_import=has_inward,
        transformed_classical_records=transformed,
        permeability_class=permeability,
    )


def classify_causal_access(case: CausalAccessCase) -> CausalAccessAudit:
    exterior_classical = access_path(
        case.system,
        case.source_event,
        case.exterior_observer,
        allowed_modes=frozenset({"classical"}),
    )
    exterior_extended = access_path(
        case.system,
        case.source_event,
        case.exterior_observer,
        allowed_modes=frozenset({"classical", "encoded_indirect"}),
    )
    local_classical = (
        access_path(
            case.system,
            case.source_event,
            case.local_observer,
            allowed_modes=frozenset({"classical"}),
        )
        if case.local_observer is not None
        else AccessResult(False, False, (), (), (), (), False)
    )
    profile = boundary_profile(case.system, case.boundary_id)

    if (
        case.claim_scope == "all_information"
        and not exterior_classical.accessible
        and exterior_extended.accessible
    ):
        return _audit(
            case,
            "overclaim_classical_screen_only",
            "absorber_guardrail",
            False,
            exterior_classical,
            exterior_extended,
            local_classical,
            profile,
            (
                "The direct classical record is not exterior-accessible, but an "
                "encoded or indirect channel was declared. The screen can block "
                "classical-export claims; it cannot adjudicate total information "
                "loss, holography, complementarity, or unitarity."
            ),
            "B1 may speak only about direct classical record export unless a richer physical channel is typed.",
            "Declare the native black-hole information framework before making all-information claims.",
        )

    if (
        exterior_classical.accessible
        and "remote_signal" in exterior_classical.channel_kinds
        and not exterior_classical.direct_participation
    ):
        return _audit(
            case,
            "remote_record_access_not_direct_participation",
            "translation_residue",
            False,
            exterior_classical,
            exterior_extended,
            local_classical,
            profile,
            (
                "The observer lacks direct local participation but receives a "
                "classical signal record. Remote observation is still causal "
                "record access, so absence-of-rendering language is rejected."
            ),
            "Remote sources are observer-accessible through received records without requiring direct participation.",
            "Keep direct participation and received-record access as separate fields in future S1/R1 models.",
        )

    if profile.permeability_class == "bidirectional_classical_exchange":
        return _audit(
            case,
            "permeable_interface_not_horizon",
            "parameterized_boundary",
            False,
            exterior_classical,
            exterior_extended,
            local_classical,
            profile,
            (
                "The boundary admits classical exchange in both directions, with "
                "record character changes. This is a permeability parameter, not "
                "a horizon-like export cap."
            ),
            "Soft finality-domain boundaries should be parameterized by exchange direction and record transformation.",
            "Bind permeability parameters to measured substrate changes before using them in S1.",
        )

    if (
        local_classical.accessible
        and not exterior_classical.accessible
        and not profile.has_outward_classical_export
    ):
        return _audit(
            case,
            "causal_reachability_absorbs_boundary",
            "translation_residue",
            False,
            exterior_classical,
            exterior_extended,
            local_classical,
            profile,
            (
                "The event is locally record-accessible but lacks an outward "
                "classical path to the exterior observer. That is ordinary causal "
                "reachability/domain-of-dependence bookkeeping."
            ),
            "A horizon is a causal-access boundary for direct classical records, not a new finality mechanism.",
            "Add extra physics only after naming a channel or capability not captured by causal reachability.",
        )

    if not local_classical.accessible and case.local_observer is not None:
        return _audit(
            case,
            "underdeclared_local_finality",
            "failed_fixture",
            False,
            exterior_classical,
            exterior_extended,
            local_classical,
            profile,
            "The source event is not even locally accessible to the declared local observer.",
            "Do not call an event locally final without a local record-access path or participation event.",
            "Fix the local observer/access profile before auditing exterior access.",
        )

    if exterior_classical.accessible:
        return _audit(
            case,
            "classical_access_available",
            "absorbed",
            False,
            exterior_classical,
            exterior_extended,
            local_classical,
            profile,
            "The declared exterior observer has a classical record path.",
            "No finality-boundary claim survives when the relevant classical record path is present.",
            "State the remaining capability object if reachability is not the intended distinction.",
        )

    return _audit(
        case,
        "unclassified_access_case",
        "open",
        False,
        exterior_classical,
        exterior_extended,
        local_classical,
        profile,
        "The finite screen did not classify this access pattern.",
        "No claim should be promoted from an unclassified causal-access fixture.",
        "Add a positive and negative control before using this case.",
    )


def canonical_causal_access_cases() -> tuple[CausalAccessCase, ...]:
    return (
        remote_signal_control_case(),
        horizon_classical_export_case(),
        encoded_indirect_horizon_case(),
        soft_boundary_permeability_case(),
    )


def remote_signal_control_case() -> CausalAccessCase:
    system = CausalRecordSystem(
        events=(
            RecordEvent("andromeda_emission", "remote_galaxy", frozenset({"photon_wavefront"})),
            RecordEvent("earth_telescope_log", "earth", frozenset({"ccd_record"})),
        ),
        channels=(
            RecordChannel(
                "starlight_to_telescope",
                "andromeda_emission",
                "earth_telescope_log",
                "remote_signal",
                classical_export=True,
            ),
        ),
    )
    return CausalAccessCase(
        name="remote_signal_control",
        system=system,
        source_event="andromeda_emission",
        exterior_observer=ObserverProfile("earth_observer", frozenset({"earth_telescope_log"})),
        local_observer=None,
        boundary_id=None,
        claim_scope="remote_record_access",
    )


def horizon_classical_export_case() -> CausalAccessCase:
    system = CausalRecordSystem(
        events=(
            RecordEvent("exterior_crossing_signal", "exterior", frozenset({"pre_horizon_beacon"})),
            RecordEvent("interior_measurement", "interior", frozenset({"interior_result"})),
            RecordEvent("infalling_memory", "interior", frozenset({"interior_memory"})),
            RecordEvent("exterior_archive", "exterior", frozenset({"outside_log"})),
        ),
        channels=(
            RecordChannel(
                "inward_horizon_crossing",
                "exterior_crossing_signal",
                "interior_measurement",
                "boundary_crossing",
                classical_export=True,
                boundary_id="event_horizon",
                boundary_direction="inward",
            ),
            RecordChannel(
                "interior_to_infalling_memory",
                "interior_measurement",
                "infalling_memory",
                "local_transfer",
                classical_export=True,
            ),
        ),
    )
    return CausalAccessCase(
        name="horizon_classical_export_cap",
        system=system,
        source_event="interior_measurement",
        exterior_observer=ObserverProfile("exterior_observer", frozenset({"exterior_archive"})),
        local_observer=ObserverProfile(
            "infalling_observer",
            frozenset({"infalling_memory"}),
            frozenset({"interior_measurement"}),
        ),
        boundary_id="event_horizon",
        claim_scope="direct_classical_export",
    )


def encoded_indirect_horizon_case() -> CausalAccessCase:
    base = horizon_classical_export_case()
    system = CausalRecordSystem(
        events=base.system.events
        + (
            RecordEvent("late_radiation_record", "exterior", frozenset({"encoded_exterior_record"})),
        ),
        channels=base.system.channels
        + (
            RecordChannel(
                "declared_encoded_indirect_channel",
                "interior_measurement",
                "late_radiation_record",
                "encoded_indirect",
                classical_export=False,
                boundary_id="event_horizon",
                boundary_direction="outward",
                record_character="encoded",
            ),
        ),
    )
    return CausalAccessCase(
        name="encoded_indirect_horizon_channel",
        system=system,
        source_event="interior_measurement",
        exterior_observer=ObserverProfile("exterior_observer", frozenset({"late_radiation_record"})),
        local_observer=base.local_observer,
        boundary_id="event_horizon",
        claim_scope="all_information",
    )


def soft_boundary_permeability_case() -> CausalAccessCase:
    system = CausalRecordSystem(
        events=(
            RecordEvent("solar_particle_event", "solar_domain", frozenset({"solar_particle_flux"})),
            RecordEvent(
                "interstellar_cosmic_ray_event",
                "interstellar_domain",
                frozenset({"galactic_cosmic_ray_flux"}),
            ),
            RecordEvent("voyager_boundary_log", "boundary_probe", frozenset({"changed_flux_log"})),
        ),
        channels=(
            RecordChannel(
                "solar_outward_boundary_record",
                "solar_particle_event",
                "voyager_boundary_log",
                "boundary_crossing",
                classical_export=True,
                boundary_id="heliopause",
                boundary_direction="outward",
                record_character="transformed",
            ),
            RecordChannel(
                "interstellar_inward_boundary_record",
                "interstellar_cosmic_ray_event",
                "voyager_boundary_log",
                "boundary_crossing",
                classical_export=True,
                boundary_id="heliopause",
                boundary_direction="inward",
                record_character="transformed",
            ),
        ),
    )
    return CausalAccessCase(
        name="soft_boundary_permeability",
        system=system,
        source_event="solar_particle_event",
        exterior_observer=ObserverProfile("boundary_probe", frozenset({"voyager_boundary_log"})),
        local_observer=None,
        boundary_id="heliopause",
        claim_scope="soft_boundary",
    )


def run_t151_analysis() -> T151Result:
    audits = tuple(classify_causal_access(case) for case in canonical_causal_access_cases())
    by_name = {audit.name: audit for audit in audits}

    remote_ok = (
        by_name["remote_signal_control"].classification
        == "remote_record_access_not_direct_participation"
    )
    horizon_absorbed = (
        by_name["horizon_classical_export_cap"].classification
        == "causal_reachability_absorbs_boundary"
    )
    encoded_rejected = (
        by_name["encoded_indirect_horizon_channel"].classification
        == "overclaim_classical_screen_only"
    )
    soft_parameterized = (
        by_name["soft_boundary_permeability"].classification
        == "permeable_interface_not_horizon"
    )

    return T151Result(
        audits=audits,
        remote_observation_guardrail_passed=remote_ok,
        horizon_claim_absorbed_by_causal_reachability=horizon_absorbed,
        encoded_channel_overclaim_rejected=encoded_rejected,
        soft_boundary_parameterized=soft_parameterized,
        strongest_claim=(
            "For direct classical records, B1 factors through ordinary causal "
            "reachability: an exterior observer can use only records connected "
            "to its access events by declared classical channels. Horizon "
            "language is safe only as causal-access bookkeeping."
        ),
        improved=(
            "T151 gives S1/B1/R1 a finite access screen that separates direct "
            "participation, received remote records, local interior records, "
            "soft boundary permeability, and nonclassical or encoded channels."
        ),
        weakened=(
            "B1 is weakened from an open black-hole byproduct to translation "
            "residue unless a future model names a capability not absorbed by "
            "causal reachability/domain-of-dependence accounting."
        ),
        falsification_condition=(
            "This screen fails if a direct-classical-record boundary claim "
            "changes verdict after the full causal-access graph is fixed, or "
            "if S1/B1 needs a native capability not representable as reachability "
            "through typed record channels."
        ),
        b1_update=(
            "B1 should say only that horizons cap direct classical record export "
            "for exterior observers. It should not infer unreality, information "
            "loss, or a new finality mechanism."
        ),
        s1_update=(
            "S1 aggregation must carry causal-access maps, not just compatible "
            "local orders. A consensus-envelope claim is underdeclared without "
            "reachability, channel type, and boundary permeability data."
        ),
        r1_update=(
            "R1 gains a guardrail: remote observation through received signals is "
            "ordinary causal record access, while direct local participation is a "
            "stronger relation."
        ),
        claim_ledger_update=(
            "Add T151 to B1/S1/R1. B1 status should be weakened: current horizon "
            "language is causal-access translation residue until a non-reachability "
            "capability is typed."
        ),
        open_blocker=(
            "No metric, Lorentzian, semiclassical-gravity, holographic, or quantum "
            "information structure is present in this finite screen."
        ),
        recommended_next=(
            "Try a Lorentzian causal-diamond version: define access by causal pasts "
            "and domains of dependence, then test whether any TaF residue survives."
        ),
    )


def t151_result_to_dict(result: T151Result) -> dict[str, Any]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "remote_observation_guardrail_passed": result.remote_observation_guardrail_passed,
        "horizon_claim_absorbed_by_causal_reachability": (
            result.horizon_claim_absorbed_by_causal_reachability
        ),
        "encoded_channel_overclaim_rejected": result.encoded_channel_overclaim_rejected,
        "soft_boundary_parameterized": result.soft_boundary_parameterized,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "b1_update": result.b1_update,
        "s1_update": result.s1_update,
        "r1_update": result.r1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _edge_allowed(channel: RecordChannel, allowed_modes: frozenset[str]) -> bool:
    if "classical" in allowed_modes and channel.classical_export:
        return True
    if "encoded_indirect" in allowed_modes and channel.channel_kind == "encoded_indirect":
        return True
    return False


def _access_from_path(
    event_path: tuple[str, ...],
    channel_path: tuple[RecordChannel, ...],
    *,
    direct_participation: bool,
) -> AccessResult:
    return AccessResult(
        accessible=True,
        direct_participation=direct_participation,
        event_path=event_path,
        channel_path=tuple(channel.channel_id for channel in channel_path),
        channel_kinds=tuple(channel.channel_kind for channel in channel_path),
        crossed_boundaries=tuple(
            channel.boundary_id
            for channel in channel_path
            if channel.boundary_id is not None
        ),
        transformed_record=any(
            channel.record_character != "preserved" for channel in channel_path
        ),
    )


def _audit(
    case: CausalAccessCase,
    classification: str,
    residue_label: str,
    taf_adds_independent_content: bool,
    exterior_classical: AccessResult,
    exterior_extended: AccessResult,
    local_classical: AccessResult,
    profile: BoundaryProfile,
    reason: str,
    weakened_claim: str,
    required_next: str,
) -> CausalAccessAudit:
    return CausalAccessAudit(
        name=case.name,
        classification=classification,
        residue_label=residue_label,
        taf_adds_independent_content=taf_adds_independent_content,
        exterior_classical_access=exterior_classical.accessible,
        exterior_extended_access=exterior_extended.accessible,
        exterior_direct_participation=exterior_classical.direct_participation,
        local_classical_access=local_classical.accessible,
        boundary_permeability=profile.permeability_class,
        reason=reason,
        weakened_claim=weakened_claim,
        required_next=required_next,
    )


def _audit_to_dict(audit: CausalAccessAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "classification": audit.classification,
        "residue_label": audit.residue_label,
        "taf_adds_independent_content": audit.taf_adds_independent_content,
        "exterior_classical_access": audit.exterior_classical_access,
        "exterior_extended_access": audit.exterior_extended_access,
        "exterior_direct_participation": audit.exterior_direct_participation,
        "local_classical_access": audit.local_classical_access,
        "boundary_permeability": audit.boundary_permeability,
        "reason": audit.reason,
        "weakened_claim": audit.weakened_claim,
        "required_next": audit.required_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t151_result_to_dict(run_t151_analysis()), indent=2))
