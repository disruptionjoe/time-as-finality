"""T418: Schwarzschild horizon access-profile screen.

This is a conservative GR causal-accessibility witness for the capability
projection method. It uses the radial null structure of Schwarzschild geometry
only as an absorber gate: exterior recovery across an event horizon is not a
same-profile capability split, and comparing an exterior projection to an
infalling/full-slice capability is an access-profile mismatch unless declared.

No black-hole information theorem, QFT, holography, semiclassical gravity, or
new physics claim is asserted here.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Any


ARTIFACT = "T418-schwarzschild-horizon-access-profile-screen-v0.1"
SCHWARZSCHILD_RADIUS = 2.0
EPSILON = 1e-9


@dataclass(frozen=True)
class RadialEvent:
    event_id: str
    advanced_time: float
    radius: float
    record: str

    def __post_init__(self) -> None:
        if not self.event_id:
            raise ValueError("event_id cannot be empty")
        if self.radius <= 0:
            raise ValueError("radius must be positive")


@dataclass(frozen=True)
class SchwarzschildState:
    state_id: str
    mass: float
    exterior_log: tuple[str, ...]
    interior_event: RadialEvent

    def __post_init__(self) -> None:
        if self.mass <= 0:
            raise ValueError("mass must be positive")

    @property
    def horizon_radius(self) -> float:
        return 2.0 * self.mass


@dataclass(frozen=True)
class NullRayTrace:
    start_radius: float
    final_radius: float
    steps: int
    escaped_to_exterior_cutoff: bool
    crossed_outward_through_horizon: bool
    hit_singularity: bool
    classification: str


@dataclass(frozen=True)
class ExteriorProjection:
    profile_id: str
    mass: float
    horizon_radius: float
    exterior_log: tuple[str, ...]
    received_interior_record: str | None


@dataclass(frozen=True)
class CapabilityReadout:
    profile_id: str
    can_recover_record: bool
    recovered_record: str | None
    reason: str

    def comparison_key(self) -> tuple[bool, str | None]:
        return (self.can_recover_record, self.recovered_record)


def outgoing_radial_null_slope(radius: float, horizon_radius: float = SCHWARZSCHILD_RADIUS) -> float:
    """Return dr/dv for an outgoing radial null ray in ingoing EF coordinates."""

    if radius <= 0:
        raise ValueError("radius must be positive")
    return 0.5 * (1.0 - horizon_radius / radius)


def radial_region(radius: float, horizon_radius: float = SCHWARZSCHILD_RADIUS) -> str:
    if radius > horizon_radius + EPSILON:
        return "outside_horizon"
    if radius < horizon_radius - EPSILON:
        return "inside_horizon"
    return "on_horizon"


def trace_outgoing_radial_null(
    event: RadialEvent,
    *,
    horizon_radius: float = SCHWARZSCHILD_RADIUS,
    exterior_cutoff: float = 6.0,
    dv: float = 0.05,
    max_steps: int = 20_000,
) -> NullRayTrace:
    """Numerically trace whether an outgoing null signal reaches a finite exterior cutoff.

    The screen only needs the qualitative absorber:
    outside r_s, outgoing radial null rays move outward; at r_s they generate
    the horizon; inside r_s even the outgoing null direction moves to smaller r.
    """

    radius = event.radius
    crossed_outward = False
    previous_region = radial_region(radius, horizon_radius)

    for step in range(max_steps + 1):
        if radius >= exterior_cutoff:
            return NullRayTrace(
                start_radius=event.radius,
                final_radius=round(radius, 12),
                steps=step,
                escaped_to_exterior_cutoff=True,
                crossed_outward_through_horizon=crossed_outward,
                hit_singularity=False,
                classification="reaches_exterior_cutoff",
            )
        if radius <= EPSILON:
            return NullRayTrace(
                start_radius=event.radius,
                final_radius=0.0,
                steps=step,
                escaped_to_exterior_cutoff=False,
                crossed_outward_through_horizon=crossed_outward,
                hit_singularity=True,
                classification="hits_singularity_before_escape",
            )

        slope = outgoing_radial_null_slope(radius, horizon_radius)
        next_radius = radius + slope * dv
        next_region = radial_region(next_radius, horizon_radius)
        if previous_region == "inside_horizon" and next_region in {
            "on_horizon",
            "outside_horizon",
        }:
            crossed_outward = True
        radius = max(next_radius, 0.0)
        previous_region = next_region

    if abs(radius - horizon_radius) <= 1e-6:
        classification = "horizon_generator_no_escape"
    elif event.radius < horizon_radius:
        classification = "trapped_inside_horizon"
    else:
        classification = "outside_ray_not_resolved"
    return NullRayTrace(
        start_radius=event.radius,
        final_radius=round(radius, 12),
        steps=max_steps,
        escaped_to_exterior_cutoff=False,
        crossed_outward_through_horizon=crossed_outward,
        hit_singularity=False,
        classification=classification,
    )


def interior_pair() -> tuple[SchwarzschildState, SchwarzschildState]:
    common_event = RadialEvent(
        event_id="interior_memory_cell",
        advanced_time=10.0,
        radius=1.5,
        record="placeholder",
    )
    return (
        SchwarzschildState(
            state_id="BH0",
            mass=1.0,
            exterior_log=("collapse_mass_1", "horizon_radius_2"),
            interior_event=RadialEvent(
                common_event.event_id,
                common_event.advanced_time,
                common_event.radius,
                "interior_bit_0",
            ),
        ),
        SchwarzschildState(
            state_id="BH1",
            mass=1.0,
            exterior_log=("collapse_mass_1", "horizon_radius_2"),
            interior_event=RadialEvent(
                common_event.event_id,
                common_event.advanced_time,
                common_event.radius,
                "interior_bit_1",
            ),
        ),
    )


def exterior_projection(state: SchwarzschildState) -> ExteriorProjection:
    trace = trace_outgoing_radial_null(
        state.interior_event,
        horizon_radius=state.horizon_radius,
    )
    return ExteriorProjection(
        profile_id="stationary_exterior_observer",
        mass=state.mass,
        horizon_radius=state.horizon_radius,
        exterior_log=state.exterior_log,
        received_interior_record=(
            state.interior_event.record if trace.escaped_to_exterior_cutoff else None
        ),
    )


def exterior_capability(state: SchwarzschildState) -> CapabilityReadout:
    trace = trace_outgoing_radial_null(
        state.interior_event,
        horizon_radius=state.horizon_radius,
    )
    if trace.escaped_to_exterior_cutoff:
        return CapabilityReadout(
            profile_id="stationary_exterior_observer",
            can_recover_record=True,
            recovered_record=state.interior_event.record,
            reason="interior event emitted a signal that reached exterior cutoff",
        )
    return CapabilityReadout(
        profile_id="stationary_exterior_observer",
        can_recover_record=False,
        recovered_record=None,
        reason=(
            "event lies inside the Schwarzschild horizon; outgoing null trace "
            f"classified as {trace.classification}"
        ),
    )


def infalling_or_full_slice_capability(state: SchwarzschildState) -> CapabilityReadout:
    return CapabilityReadout(
        profile_id="infalling_or_full_slice_profile",
        can_recover_record=True,
        recovered_record=state.interior_event.record,
        reason=(
            "this profile is not the exterior observer: it is granted interior "
            "or full-slice access by definition"
        ),
    )


def horizon_geometry_audit() -> dict[str, Any]:
    inside = RadialEvent("inside_probe", 0.0, 1.5, "inside")
    horizon = RadialEvent("horizon_probe", 0.0, SCHWARZSCHILD_RADIUS, "horizon")
    outside = RadialEvent("outside_probe", 0.0, 3.0, "outside")
    return {
        "slope_inside": outgoing_radial_null_slope(inside.radius),
        "slope_on_horizon": outgoing_radial_null_slope(horizon.radius),
        "slope_outside": outgoing_radial_null_slope(outside.radius),
        "inside_trace": asdict(trace_outgoing_radial_null(inside)),
        "horizon_trace": asdict(trace_outgoing_radial_null(horizon)),
        "outside_trace": asdict(trace_outgoing_radial_null(outside)),
    }


def outside_signal_positive_control() -> dict[str, Any]:
    left = RadialEvent("outside_signal_A", 0.0, 3.0, "pulse_A")
    right = RadialEvent("outside_signal_B", 0.0, 3.0, "pulse_B")
    left_trace = trace_outgoing_radial_null(left)
    right_trace = trace_outgoing_radial_null(right)
    return {
        "case_id": "outside_signal_positive_control",
        "same_geometry": left.radius == right.radius,
        "both_reach_exterior": (
            left_trace.escaped_to_exterior_cutoff
            and right_trace.escaped_to_exterior_cutoff
        ),
        "records_distinguished_by_exterior_profile": (
            left.record != right.record
            and left_trace.escaped_to_exterior_cutoff
            and right_trace.escaped_to_exterior_cutoff
        ),
        "residue_label": "ordinary_exterior_causal_record_access",
        "reason": (
            "The guard has teeth: records emitted outside the horizon can reach "
            "the exterior cutoff and are ordinary causal record access."
        ),
    }


def access_profile_alignment_audit() -> dict[str, Any]:
    left, right = interior_pair()
    left_projection = exterior_projection(left)
    right_projection = exterior_projection(right)
    left_exterior_cap = exterior_capability(left)
    right_exterior_cap = exterior_capability(right)
    left_infalling_cap = infalling_or_full_slice_capability(left)
    right_infalling_cap = infalling_or_full_slice_capability(right)

    exterior_projection_equal = left_projection == right_projection
    aligned_exterior_capability_equal = (
        left_exterior_cap.comparison_key() == right_exterior_cap.comparison_key()
    )
    cross_profile_capability_split = (
        left_infalling_cap.comparison_key() != right_infalling_cap.comparison_key()
    )

    return {
        "case_id": "same_exterior_shadow_different_interior_record",
        "states": [left.state_id, right.state_id],
        "exterior_projection_left": asdict(left_projection),
        "exterior_projection_right": asdict(right_projection),
        "exterior_projection_equal": exterior_projection_equal,
        "aligned_exterior_capability_left": asdict(left_exterior_cap),
        "aligned_exterior_capability_right": asdict(right_exterior_cap),
        "aligned_exterior_capability_equal": aligned_exterior_capability_equal,
        "cross_profile_capability_left": asdict(left_infalling_cap),
        "cross_profile_capability_right": asdict(right_infalling_cap),
        "cross_profile_capability_split": cross_profile_capability_split,
        "alignment_gate_verdict": (
            "no_same_profile_projection_failure"
            if exterior_projection_equal and aligned_exterior_capability_equal
            else "fixture_failed"
        ),
        "mismatch_verdict": (
            "cross_profile_mismatch_absorbed_by_horizon_access_profile"
            if exterior_projection_equal and cross_profile_capability_split
            else "no_cross_profile_split"
        ),
        "residue_label": "absorbed_by_schwarzschild_causal_access_and_profile_alignment",
    }


def run_schwarzschild_horizon_access_profile_screen() -> dict[str, Any]:
    geometry = horizon_geometry_audit()
    alignment = access_profile_alignment_audit()
    positive = outside_signal_positive_control()
    return {
        "artifact": ARTIFACT,
        "status": "implemented_guardrail_no_claim_promotion",
        "source_method_action": (
            "Method next action: run a GR causal-accessibility witness using "
            "simple models first; access-profile alignment report named this "
            "as the safe follow-up."
        ),
        "model_scope": (
            "radial Schwarzschild causal-access screen in ingoing "
            "Eddington-Finkelstein coordinates; finite exterior cutoff, no QFT"
        ),
        "horizon_geometry_audit": geometry,
        "access_profile_alignment_audit": alignment,
        "positive_control": positive,
        "absorber_audit": {
            "schwarzschild_event_horizon": {
                "status": "absorbs",
                "reason": (
                    "Inside the horizon, outgoing radial null directions do not "
                    "increase through r_s. Exterior non-recovery is ordinary GR "
                    "causal-access structure in this model."
                ),
            },
            "access_profile_alignment": {
                "status": "absorbs",
                "reason": (
                    "Exterior projection compared to exterior capability does "
                    "not split. The split appears only when the capability is "
                    "silently moved to an infalling/full-slice profile."
                ),
            },
            "black_hole_information_claim": {
                "status": "not_attempted",
                "reason": (
                    "The artifact does not model Hawking radiation, QFT "
                    "algebras, Page curves, holography, or evaporation."
                ),
            },
        },
        "verdict": (
            "T418 supplies a GR causal-accessibility absorber screen: same "
            "exterior Schwarzschild shadow plus different interior records does "
            "not create an exterior capability split; comparing to an infalling "
            "or full-slice capability is a cross-profile mismatch unless "
            "declared."
        ),
        "claim_ledger_update": "none; no claim promotion",
        "north_star_or_public_posture_update": "none",
        "recommended_next": [
            "Use T418 as a horizon/access-profile guardrail for future B1/S1/R1 screens.",
            "Do not cite interior-record recovery by a non-exterior profile as exterior projection residue.",
            "A stronger GR-facing artifact would need matched access profiles plus a native black-hole information or algebraic-QFT capability object declared up front.",
        ],
        "falsification_condition": (
            "The screen would fail in TaF's favor only if two states matched the "
            "Schwarzschild exterior geometry, observer access profile, received "
            "record algebra, and task boundary, yet split an exterior-native "
            "capability not expressible as standard horizon causal access."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run_schwarzschild_horizon_access_profile_screen(), indent=2))
