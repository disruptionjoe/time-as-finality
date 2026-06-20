"""T88: Pati-Salam typed-forgetting crosswalk.

This module imports no GU runtime code. It reimplements the finite
representation arithmetic needed for one narrow TaF question:

Does forgetting the SU(2)_R Cartan term T3R break reconstruction of the
Standard-Model hypercharge table, while the full Pati-Salam map recovers it?

The result is a typed-forgetting witness for TaF's LossKernel/TF1 work. It is
not evidence for GU physics or TaF physics.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Iterable


HALF = Fraction(1, 2)


@dataclass(frozen=True, order=True)
class Multiplet:
    su3: str
    su2_l_dim: int
    n: int
    dim: int

    def as_tuple(self) -> tuple[str, int, int, int]:
        return (self.su3, self.su2_l_dim, self.n, self.dim)


@dataclass(frozen=True)
class SpinorState:
    weight: tuple[Fraction, Fraction, Fraction, Fraction, Fraction]
    su3: str
    b_minus_l: Fraction
    t3l: Fraction
    t3r: Fraction
    y: Fraction
    q: Fraction
    n: int


@dataclass(frozen=True)
class TransportAudit:
    name: str
    hypercharge_rule: str
    used_structure: frozenset[str]
    losskernel: frozenset[str]
    multiplets: tuple[Multiplet, ...]
    n_values: tuple[int, ...]
    charge_values: tuple[str, ...]
    total_dimension: int
    exact_table_match: bool
    dimension_preserved: bool
    missing_paper_multiplets: tuple[Multiplet, ...]
    extra_multiplets: tuple[Multiplet, ...]
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T88Result:
    standard_audit: TransportAudit
    bl_only_audit: TransportAudit
    loss_attribution: str
    po1_status: str
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    taf_update: str
    recommended_next: str


PAPER_TABLE: tuple[Multiplet, ...] = (
    Multiplet("3", 2, 1, 6),
    Multiplet("3bar", 1, 2, 3),
    Multiplet("3bar", 1, -4, 3),
    Multiplet("1", 2, -3, 2),
    Multiplet("1", 1, 6, 1),
    Multiplet("1", 1, 0, 1),
)

FULL_PATI_SALAM_STRUCTURE = frozenset(
    {
        "SU4_color_b_minus_l",
        "SU2L_cartan_T3L",
        "SU2R_cartan_T3R",
        "spin10_chiral_16",
    }
)


def spinor16_weights() -> tuple[tuple[Fraction, Fraction, Fraction, Fraction, Fraction], ...]:
    """Return the Spin(10) chiral spinor weights with even minus parity."""
    weights = tuple(product((HALF, -HALF), repeat=5))
    return tuple(
        weight
        for weight in weights
        if sum(1 for component in weight if component < 0) % 2 == 0
    )


def standard_pati_salam_audit() -> TransportAudit:
    return audit_transport(
        name="standard_pati_salam_to_sm",
        include_t3r=True,
        hypercharge_rule="Y = T3R + (B-L)/2",
        losskernel=frozenset(),
    )


def bl_only_projection_audit() -> TransportAudit:
    return audit_transport(
        name="b_minus_l_only_projection",
        include_t3r=False,
        hypercharge_rule="Y' = (B-L)/2",
        losskernel=frozenset({"SU2R_cartan_T3R", "right_isospin_splitting"}),
    )


def audit_transport(
    name: str,
    include_t3r: bool,
    hypercharge_rule: str,
    losskernel: frozenset[str],
) -> TransportAudit:
    states = compute_states(include_t3r=include_t3r)
    multiplets = collapse_to_multiplets(states)
    table_match = _counter(multiplets) == _counter(PAPER_TABLE)
    total_dimension = sum(multiplet.dim for multiplet in multiplets)
    missing, extra = _table_delta(multiplets)
    n_values = tuple(sorted({multiplet.n for multiplet in multiplets}))
    charge_values = tuple(sorted({_format_fraction(state.q) for state in states}, key=_charge_sort_key))
    used_structure = FULL_PATI_SALAM_STRUCTURE - losskernel

    if table_match:
        verdict = "exact_table_reconstruction"
        interpretation = (
            "The full Pati-Salam map preserves the right-isospin Cartan data "
            "needed to reconstruct the one-generation hypercharge table."
        )
    else:
        verdict = "typed_forgetting_failure"
        interpretation = (
            "The projection preserves the 16-state carrier but forgets the "
            "SU(2)_R Cartan split that separates right-handed singlets into "
            "the correct hypercharge rows."
        )

    return TransportAudit(
        name=name,
        hypercharge_rule=hypercharge_rule,
        used_structure=used_structure,
        losskernel=losskernel,
        multiplets=multiplets,
        n_values=n_values,
        charge_values=charge_values,
        total_dimension=total_dimension,
        exact_table_match=table_match,
        dimension_preserved=(total_dimension == 16),
        missing_paper_multiplets=missing,
        extra_multiplets=extra,
        verdict=verdict,
        interpretation=interpretation,
    )


def compute_states(include_t3r: bool) -> tuple[SpinorState, ...]:
    states: list[SpinorState] = []
    for weight in spinor16_weights():
        s1, s2, s3, s4, s5 = weight
        bml = -Fraction(2, 3) * (s1 + s2 + s3)
        t3l = (s4 + s5) / 2
        t3r = (s4 - s5) / 2
        y = (t3r if include_t3r else Fraction(0)) + bml / 2
        q = t3l + y
        n_fraction = 6 * y
        if n_fraction.denominator != 1:
            raise ValueError(f"non-integral n=6Y for weight {weight}: {n_fraction}")
        states.append(
            SpinorState(
                weight=weight,
                su3=_su3_label((s1, s2, s3), bml),
                b_minus_l=bml,
                t3l=t3l,
                t3r=t3r,
                y=y,
                q=q,
                n=int(n_fraction),
            )
        )
    return tuple(states)


def collapse_to_multiplets(states: Iterable[SpinorState]) -> tuple[Multiplet, ...]:
    grouped: dict[tuple[str, int], list[SpinorState]] = defaultdict(list)
    for state in states:
        grouped[(state.su3, state.n)].append(state)

    multiplets: list[Multiplet] = []
    for (su3, n), members in grouped.items():
        su2_l_dim = len({member.t3l for member in members})
        multiplets.append(
            Multiplet(
                su3=su3,
                su2_l_dim=su2_l_dim,
                n=n,
                dim=len(members),
            )
        )
    return tuple(sorted(multiplets, key=lambda item: (-item.dim, item.su3, item.n)))


def run_t88_analysis() -> T88Result:
    standard = standard_pati_salam_audit()
    bl_only = bl_only_projection_audit()

    if standard.exact_table_match and not bl_only.exact_table_match:
        loss_attribution = (
            "Within the tested map family, the failure is attributable to a "
            "non-empty LossKernel naming SU2R_cartan_T3R. Restoring T3R in "
            "Y = T3R + (B-L)/2 restores the exact table."
        )
        strongest = (
            "The GU Pati-Salam verification supplies a clean external "
            "typed-forgetting witness for TaF: the 16-state carrier and B-L "
            "data survive the naive projection, but the forgotten T3R term is "
            "load-bearing for the Standard-Model hypercharge invariant."
        )
    else:
        loss_attribution = (
            "The tested maps did not isolate T3R as the table-reconstruction "
            "difference; the crosswalk should not be used."
        )
        strongest = (
            "The Pati-Salam crosswalk failed to isolate a typed-forgetting "
            "witness."
        )

    return T88Result(
        standard_audit=standard,
        bl_only_audit=bl_only,
        loss_attribution=loss_attribution,
        po1_status=(
            "not_a_po1_instance_without_gluing_object: this is an invariant "
            "reconstruction failure under typed forgetting, not yet a "
            "D1RestrictionSystem local-to-global obstruction."
        ),
        strongest_claim=strongest,
        weakened_claim=(
            "T88 does not validate GU physics, TaF physics, Q1, H1, H7, or "
            "spacetime reconstruction. It imports only a finite representation "
            "arithmetic witness for typed structure preservation."
        ),
        falsification_condition=(
            "Reject this crosswalk if B-L alone reproduces the paper n=1 "
            "multiplet table, if the full Pati-Salam map fails to reproduce "
            "the table, or if the failure can be repaired without restoring a "
            "right-isospin-equivalent term."
        ),
        taf_update=(
            "TF1 gains a narrow external mathematics witness: named forgotten "
            "structure can be necessary for preserving a downstream invariant. "
            "No current TaF physics claim is upgraded."
        ),
        recommended_next=(
            "If this route is continued, reformulate the Pati-Salam table as a "
            "typed transport object with source, target, preserved invariants, "
            "and LossKernel fields; only then ask whether it can be embedded in "
            "PO1-style gluing machinery."
        ),
    )


def t88_result_to_dict(result: T88Result) -> dict[str, object]:
    return {
        "standard_audit": _audit_to_dict(result.standard_audit),
        "bl_only_audit": _audit_to_dict(result.bl_only_audit),
        "loss_attribution": result.loss_attribution,
        "po1_status": result.po1_status,
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "taf_update": result.taf_update,
        "recommended_next": result.recommended_next,
    }


def _su3_label(w123: tuple[Fraction, Fraction, Fraction], bml: Fraction) -> str:
    n_minus = sum(1 for component in w123 if component < 0)
    if n_minus in (0, 3):
        return "1"
    return "3" if bml > 0 else "3bar"


def _counter(multiplets: Iterable[Multiplet]) -> Counter[tuple[str, int, int, int]]:
    return Counter(multiplet.as_tuple() for multiplet in multiplets)


def _table_delta(
    multiplets: tuple[Multiplet, ...],
) -> tuple[tuple[Multiplet, ...], tuple[Multiplet, ...]]:
    computed = _counter(multiplets)
    expected = _counter(PAPER_TABLE)
    missing_counter = expected - computed
    extra_counter = computed - expected
    missing = tuple(
        Multiplet(*key)
        for key, count in missing_counter.items()
        for _ in range(count)
    )
    extra = tuple(
        Multiplet(*key)
        for key, count in extra_counter.items()
        for _ in range(count)
    )
    return missing, extra


def _audit_to_dict(audit: TransportAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "hypercharge_rule": audit.hypercharge_rule,
        "used_structure": sorted(audit.used_structure),
        "losskernel": sorted(audit.losskernel),
        "multiplets": [_multiplet_to_dict(multiplet) for multiplet in audit.multiplets],
        "n_values": list(audit.n_values),
        "charge_values": list(audit.charge_values),
        "total_dimension": audit.total_dimension,
        "exact_table_match": audit.exact_table_match,
        "dimension_preserved": audit.dimension_preserved,
        "missing_paper_multiplets": [
            _multiplet_to_dict(multiplet) for multiplet in audit.missing_paper_multiplets
        ],
        "extra_multiplets": [
            _multiplet_to_dict(multiplet) for multiplet in audit.extra_multiplets
        ],
        "verdict": audit.verdict,
        "interpretation": audit.interpretation,
    }


def _multiplet_to_dict(multiplet: Multiplet) -> dict[str, object]:
    return {
        "su3": multiplet.su3,
        "su2_l_dim": multiplet.su2_l_dim,
        "n": multiplet.n,
        "dim": multiplet.dim,
    }


def _format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _charge_sort_key(value: str) -> Fraction:
    if "/" in value:
        numerator, denominator = value.split("/", 1)
        return Fraction(int(numerator), int(denominator))
    return Fraction(int(value), 1)
