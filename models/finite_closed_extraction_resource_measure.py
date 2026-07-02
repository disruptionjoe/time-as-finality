"""Finite-closed extraction-resource measure support model.

This is a support artifact for
open-problems/finite-closed-capability-boundary-scope-theorem.md.

It formalizes the single-instance "brute-force is finite" step without
promoting the scope theorem. The model is deliberately abstract: a finite closed
boundary instance has a visible signature for the declared region/menu, a
co-present closed code, and a separating datum. If the datum is not determined
by the visible signature but is determined by the closed code, then a finite
lookup extractor exists for the single instance.

The extractor is not efficient and does not prove a physical boundary. It is
the opposite: it makes the single-instance declared/crackable ceiling explicit.
Physical force has to come from a family-level resource growth theorem or a
hardness assumption.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import json
from typing import Hashable


@dataclass(frozen=True)
class FiniteClosedBoundary:
    """A finite closed capability-boundary instance.

    configurations are finite labels.
    visible_signature is what the declared region/menu can decide.
    closed_code is the co-present retained code in the closed model.
    datum is the boundary-crossing capability/readout.
    """

    name: str
    configurations: tuple[Hashable, ...]
    visible_signature: dict[Hashable, Hashable]
    closed_code: dict[Hashable, Hashable]
    datum: dict[Hashable, Hashable]
    gap_mode: str
    assumption: str | None = None
    family_costs: tuple[int, ...] = ()

    def __post_init__(self) -> None:
        if not self.configurations:
            raise ValueError("finite boundary must have at least one configuration")
        config_set = set(self.configurations)
        for name, mapping in (
            ("visible_signature", self.visible_signature),
            ("closed_code", self.closed_code),
            ("datum", self.datum),
        ):
            if set(mapping) != config_set:
                raise ValueError(f"{name} must be defined exactly on configurations")

    def visible_fibers(self) -> dict[Hashable, tuple[Hashable, ...]]:
        fibers: dict[Hashable, list[Hashable]] = {}
        for config in self.configurations:
            fibers.setdefault(self.visible_signature[config], []).append(config)
        return {key: tuple(value) for key, value in fibers.items()}

    def closed_code_determines_datum(self) -> bool:
        table: dict[Hashable, Hashable] = {}
        for config in self.configurations:
            code = self.closed_code[config]
            value = self.datum[config]
            if code in table and table[code] != value:
                return False
            table[code] = value
        return True

    def datum_factors_through_visible_signature(self) -> bool:
        for fiber in self.visible_fibers().values():
            values = {self.datum[config] for config in fiber}
            if len(values) > 1:
                return False
        return True

    def boundary_pairs(self) -> tuple[tuple[Hashable, Hashable], ...]:
        pairs: list[tuple[Hashable, Hashable]] = []
        for left, right in combinations(self.configurations, 2):
            same_visible = self.visible_signature[left] == self.visible_signature[right]
            different_datum = self.datum[left] != self.datum[right]
            if same_visible and different_datum:
                pairs.append((left, right))
        return tuple(pairs)

    def finite_lookup_upper_bound(self) -> int:
        """Lookup-table upper bound for a single finite instance.

        This is a model-size / enumeration bound, not an efficiency claim.
        """

        return len({self.closed_code[config] for config in self.configurations})

    def family_costs_strictly_increase(self) -> bool | None:
        if not self.family_costs:
            return None
        return all(
            self.family_costs[index] < self.family_costs[index + 1]
            for index in range(len(self.family_costs) - 1)
        )

    def summary(self) -> dict[str, object]:
        return {
            "name": self.name,
            "finite_configurations": len(self.configurations),
            "visible_classes": len(self.visible_fibers()),
            "closed_code_values": self.finite_lookup_upper_bound(),
            "datum_determined_by_closed_code": self.closed_code_determines_datum(),
            "datum_factors_through_visible_signature": (
                self.datum_factors_through_visible_signature()
            ),
            "boundary_pairs": [list(pair) for pair in self.boundary_pairs()],
            "single_instance_lookup_cost_is_finite": True,
            "single_instance_lookup_upper_bound": self.finite_lookup_upper_bound(),
            "gap_mode": self.gap_mode,
            "assumption": self.assumption,
            "family_costs": list(self.family_costs),
            "family_costs_strictly_increase": self.family_costs_strictly_increase(),
        }


def t411_departed_record_shadow() -> FiniteClosedBoundary:
    return FiniteClosedBoundary(
        name="T411 departed-record shadow",
        configurations=("even_global_correlation", "odd_global_correlation"),
        visible_signature={
            "even_global_correlation": "all_R_supported_statistics_equal",
            "odd_global_correlation": "all_R_supported_statistics_equal",
        },
        closed_code={
            "even_global_correlation": "retained_tier1_even_witness",
            "odd_global_correlation": "retained_tier1_odd_witness",
        },
        datum={
            "even_global_correlation": "boundary_readout_even",
            "odd_global_correlation": "boundary_readout_odd",
        },
        gap_mode="E0_declared_or_crackable",
    )


def t413_grand_coalition_shadow() -> FiniteClosedBoundary:
    return FiniteClosedBoundary(
        name="T413 grand-coalition shadow",
        configurations=("same_proper_values_vN_0", "same_proper_values_vN_1"),
        visible_signature={
            "same_proper_values_vN_0": "all_proper_coalitions_equal",
            "same_proper_values_vN_1": "all_proper_coalitions_equal",
        },
        closed_code={
            "same_proper_values_vN_0": "grand_coalition_value_0",
            "same_proper_values_vN_1": "grand_coalition_value_1",
        },
        datum={
            "same_proper_values_vN_0": "certificate_absent",
            "same_proper_values_vN_1": "certificate_present",
        },
        gap_mode="E0_single_instance_or_E1_nonatomic_limit",
        family_costs=(1, 2, 4, 8),
    )


def t417_quadratic_residuosity_shadow() -> FiniteClosedBoundary:
    return FiniteClosedBoundary(
        name="T417 quadratic-residuosity shadow",
        configurations=("x_58_mod_77", "x_24_mod_77"),
        visible_signature={
            "x_58_mod_77": "N_77_jacobi_plus_one",
            "x_24_mod_77": "N_77_jacobi_plus_one",
        },
        closed_code={
            "x_58_mod_77": ("x", 58, "N", 77),
            "x_24_mod_77": ("x", 24, "N", 77),
        },
        datum={
            "x_58_mod_77": "quadratic_residue",
            "x_24_mod_77": "quadratic_nonresidue_jacobi_plus_one",
        },
        gap_mode="E2_hardness_assumption_plus_E1_family_growth",
        assumption="Quadratic Residuosity Assumption / factoring hardness",
        family_costs=(2, 6, 10, 28, 58),
    )


def run() -> dict[str, object]:
    witnesses = (
        t411_departed_record_shadow(),
        t413_grand_coalition_shadow(),
        t417_quadratic_residuosity_shadow(),
    )
    summaries = [witness.summary() for witness in witnesses]
    return {
        "artifact": "finite-closed-extraction-resource-measure-v0.1",
        "claim_ledger_update": "none; support artifact only",
        "scope_theorem_status": "candidate; no promotion",
        "generic_result": {
            "single_instance_boundary": (
                "if the datum is determined by a finite closed code, a finite "
                "lookup extractor exists for that instance"
            ),
            "physical_force_requires": (
                "an asymptotic lower-bound theorem (E1) or a forcing assumption "
                "(E2); stipulated finite budgets remain E0"
            ),
        },
        "witnesses": summaries,
        "all_closed_codes_determine_datum": all(
            witness.closed_code_determines_datum() for witness in witnesses
        ),
        "all_have_visible_boundary_pair": all(
            bool(witness.boundary_pairs()) for witness in witnesses
        ),
        "all_single_instance_bounds_finite": all(
            witness.finite_lookup_upper_bound() < float("inf")
            for witness in witnesses
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
