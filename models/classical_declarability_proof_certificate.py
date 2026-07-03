"""T433 - Classical declarability proof certificate.

This artifact turns T432's finite classical sweep into a constructive proof
certificate for the classical C-fragment of the capability-boundary taxonomy.

For a finite classical product code Omega and a total datum d: Omega -> V,
A1 contains the full co-present code / identity readout. Therefore d factors
through A1 by lookup. If d fails to factor through the A0 region projection,
that creates an A0 boundary, but the boundary is E0-declared relative to A1.

Recorded-tier only. No claim promotion. This does not touch the quantum E3
route, WAY-style symmetry barriers, GU/TI truth, or public posture.

Run:

    python -m models.classical_declarability_proof_certificate --write-results
    python -m pytest tests/test_classical_declarability_proof_certificate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
from typing import Iterable


Config = tuple[str, ...]
Coords = tuple[int, ...]
TruthTable = tuple[str, ...]


def coordinate_subsets(n_coords: int, include_full: bool = True) -> Iterable[Coords]:
    stop = n_coords + 1 if include_full else n_coords
    for size in range(stop):
        for subset in combinations(range(n_coords), size):
            yield subset


def coords_label(coords: Coords) -> str:
    if not coords:
        return "{}"
    return "{" + ",".join(f"x{coord}" for coord in coords) + "}"


@dataclass(frozen=True)
class FiniteProductCode:
    """A finite classical product configuration space."""

    domains: tuple[tuple[str, ...], ...]

    def __post_init__(self) -> None:
        if not self.domains:
            raise ValueError("finite product code needs at least one coordinate")
        for domain in self.domains:
            if not domain:
                raise ValueError("coordinate domains must be nonempty")
            if len(set(domain)) != len(domain):
                raise ValueError("coordinate domain values must be unique")

    @property
    def n_coords(self) -> int:
        return len(self.domains)

    @property
    def full_coords(self) -> Coords:
        return tuple(range(self.n_coords))

    @property
    def size(self) -> int:
        total = 1
        for domain in self.domains:
            total *= len(domain)
        return total

    def configurations(self) -> tuple[Config, ...]:
        return tuple(product(*self.domains))

    def config_index(self, config: Config) -> int:
        if len(config) != self.n_coords:
            raise ValueError("configuration has wrong arity")
        index = 0
        for value, domain in zip(config, self.domains):
            index = index * len(domain) + domain.index(value)
        return index


def projection(config: Config, coords: Coords) -> Config:
    return tuple(config[index] for index in coords)


def table_value(code: FiniteProductCode, table: TruthTable, config: Config) -> str:
    if len(table) != code.size:
        raise ValueError("truth table length must match product-code size")
    return table[code.config_index(config)]


def is_constant_on_projection(
    code: FiniteProductCode, table: TruthTable, coords: Coords
) -> bool:
    seen: dict[Config, str] = {}
    for config in code.configurations():
        key = projection(config, coords)
        value = table_value(code, table, config)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def boundary_pairs(
    code: FiniteProductCode, table: TruthTable, region: Coords
) -> tuple[tuple[Config, Config], ...]:
    pairs: list[tuple[Config, Config]] = []
    configs = code.configurations()
    for left, right in combinations(configs, 2):
        if projection(left, region) != projection(right, region):
            continue
        if table_value(code, table, left) != table_value(code, table, right):
            pairs.append((left, right))
    return tuple(pairs)


def minimal_coordinate_supports(
    code: FiniteProductCode, table: TruthTable
) -> tuple[Coords, ...]:
    supports: list[Coords] = []
    for coords in coordinate_subsets(code.n_coords):
        coord_set = set(coords)
        if any(set(existing).issubset(coord_set) for existing in supports):
            continue
        if is_constant_on_projection(code, table, coords):
            supports.append(coords)
    return tuple(supports)


@dataclass(frozen=True)
class ClassicalDeclarabilityCase:
    name: str
    code: FiniteProductCode
    region: Coords
    truth_table: TruthTable

    def __post_init__(self) -> None:
        if len(self.truth_table) != self.code.size:
            raise ValueError("truth table length must match product-code size")
        if any(coord < 0 or coord >= self.code.n_coords for coord in self.region):
            raise ValueError("region coordinates must exist in the product code")

    @property
    def a0_measurable(self) -> bool:
        return is_constant_on_projection(self.code, self.truth_table, self.region)

    @property
    def a1_measurable(self) -> bool:
        return is_constant_on_projection(
            self.code, self.truth_table, self.code.full_coords
        )

    @property
    def boundary_pairs(self) -> tuple[tuple[Config, Config], ...]:
        return boundary_pairs(self.code, self.truth_table, self.region)

    @property
    def has_boundary(self) -> bool:
        return bool(self.boundary_pairs)

    @property
    def minimal_supports(self) -> tuple[Coords, ...]:
        return minimal_coordinate_supports(self.code, self.truth_table)

    @property
    def has_no_proper_coordinate_support(self) -> bool:
        return self.minimal_supports == (self.code.full_coords,)

    @property
    def single_instance_physical_candidate_relative_to_a1(self) -> bool:
        return self.has_boundary and not self.a1_measurable

    @property
    def verdict(self) -> str:
        if self.a0_measurable:
            return "NO_BOUNDARY_A0_REGION_DETERMINES_DATUM"
        if self.a1_measurable:
            return "E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP"
        return "INVALID_A1_FOR_CLASSICAL_CLOSED_CODE"

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "domain_sizes": [len(domain) for domain in self.code.domains],
            "region": list(self.region),
            "region_label": coords_label(self.region),
            "truth_table": list(self.truth_table),
            "a0_region_measurable": self.a0_measurable,
            "a1_full_code_measurable": self.a1_measurable,
            "has_boundary_pair": self.has_boundary,
            "boundary_pair_count": len(self.boundary_pairs),
            "boundary_pair_examples": [
                [list(left), list(right)] for left, right in self.boundary_pairs[:4]
            ],
            "minimal_coordinate_support_labels": [
                coords_label(support) for support in self.minimal_supports
            ],
            "has_no_proper_coordinate_support": self.has_no_proper_coordinate_support,
            "a1_lookup_upper_bound": self.code.size,
            "single_instance_physical_candidate_relative_to_A1": (
                self.single_instance_physical_candidate_relative_to_a1
            ),
            "verdict": self.verdict,
        }


def table_from_values(values: Iterable[object]) -> TruthTable:
    return tuple(str(value) for value in values)


def named_cases() -> tuple[ClassicalDeclarabilityCase, ...]:
    binary2 = FiniteProductCode((("0", "1"), ("0", "1")))
    binary3 = FiniteProductCode((("0", "1"), ("0", "1"), ("0", "1")))
    ternary_binary = FiniteProductCode((("0", "1", "2"), ("a", "b")))

    return (
        ClassicalDeclarabilityCase(
            name="region_visible_control",
            code=binary3,
            region=(0, 1),
            truth_table=table_from_values(config[0] for config in binary3.configurations()),
        ),
        ClassicalDeclarabilityCase(
            name="hidden_complement_bit",
            code=binary2,
            region=(0,),
            truth_table=table_from_values(config[1] for config in binary2.configurations()),
        ),
        ClassicalDeclarabilityCase(
            name="full_support_parity_guard",
            code=binary3,
            region=(0, 1),
            truth_table=table_from_values(
                str(
                    int(config[0])
                    ^ int(config[1])
                    ^ int(config[2])
                )
                for config in binary3.configurations()
            ),
        ),
        ClassicalDeclarabilityCase(
            name="nonbinary_region_complement_relation",
            code=ternary_binary,
            region=(0,),
            truth_table=table_from_values(
                f"{config[0]}-{config[1]}" for config in ternary_binary.configurations()
            ),
        ),
    )


def proof_certificate() -> dict[str, object]:
    return {
        "theorem_name": "Classical finite A1 declarability lemma",
        "statement": (
            "For any finite classical product code Omega and any total datum "
            "d: Omega -> V, d is A1-measurable when A1 contains the full "
            "co-present code / identity readout. Therefore an A0 boundary "
            "created by d not factoring through the region projection is "
            "E0-declared relative to A1, not a single-instance physical boundary."
        ),
        "proof_steps": [
            {
                "id": "P1",
                "step": "Classical instance is a finite product code Omega.",
                "discharged_by": "FiniteProductCode(domains)",
            },
            {
                "id": "P2",
                "step": "A0 observables factor through the declared region projection pi_R.",
                "discharged_by": "is_constant_on_projection(code, table, region)",
            },
            {
                "id": "P3",
                "step": "A1 includes the identity/full-code readout on Omega.",
                "discharged_by": "code.full_coords",
            },
            {
                "id": "P4",
                "step": "Every total datum factors through identity by finite lookup.",
                "discharged_by": "is_constant_on_projection(code, table, code.full_coords)",
            },
            {
                "id": "P5",
                "step": "A boundary is physical relative to A1 only if it has an A0 same-fiber split and fails A1 measurability.",
                "discharged_by": "has_boundary and not a1_measurable is always false for valid cases",
            },
        ],
        "verdict": "CLASSICAL_DECLARABILITY_PROOF_CERTIFIED",
        "honest_scope": (
            "Classical finite product codes only. This is not a quantum theorem, "
            "not an E3/WAY statement, not a universal no-go, not claim-ledger "
            "movement, and not cross-repo evidence."
        ),
        "failure_conditions": [
            "A1 does not contain the full co-present code / identity readout.",
            "The datum is not a total function on the finite classical instance.",
            "The model is quantum/operational rather than a classical product code.",
            "The question is family-level cost or hardness rather than single-instance declarability.",
        ],
    }


def exhaustive_mixed_sweep() -> list[dict[str, object]]:
    shapes = (
        (2,),
        (2, 2),
        (2, 3),
        (3, 2),
        (2, 2, 2),
    )
    summaries: list[dict[str, object]] = []
    for shape in shapes:
        code = FiniteProductCode(
            tuple(tuple(str(index) for index in range(size)) for size in shape)
        )
        total_region_function_checks = 0
        boundary_functions = 0
        a1_declared_boundaries = 0
        physical_candidates = 0

        for region in coordinate_subsets(code.n_coords, include_full=False):
            for table in product(("0", "1"), repeat=code.size):
                total_region_function_checks += 1
                case = ClassicalDeclarabilityCase(
                    name="sweep",
                    code=code,
                    region=region,
                    truth_table=tuple(table),
                )
                if not case.has_boundary:
                    continue
                boundary_functions += 1
                if case.verdict == "E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP":
                    a1_declared_boundaries += 1
                if case.single_instance_physical_candidate_relative_to_a1:
                    physical_candidates += 1

        summaries.append(
            {
                "domain_shape": list(shape),
                "proper_region_count": 2 ** code.n_coords - 1,
                "total_region_function_checks": total_region_function_checks,
                "boundary_functions": boundary_functions,
                "a1_declared_boundaries": a1_declared_boundaries,
                "single_instance_physical_candidates_relative_to_A1": physical_candidates,
            }
        )
    return summaries


def run() -> dict[str, object]:
    cases = named_cases()
    sweep = exhaustive_mixed_sweep()
    proof = proof_certificate()
    boundary_cases = [case for case in cases if case.has_boundary]
    return {
        "artifact": "T433-classical-declarability-proof-certificate-v0.1",
        "scope": "Recorded-tier constructive proof certificate for the classical C-fragment.",
        "proof_certificate": proof,
        "overall_verdict": {
            "verdict": proof["verdict"],
            "all_named_boundary_cases_declared_relative_to_A1": all(
                case.verdict == "E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP"
                for case in boundary_cases
            ),
            "no_physical_candidates_in_mixed_sweep": all(
                row["single_instance_physical_candidates_relative_to_A1"] == 0
                for row in sweep
            ),
            "reading": (
                "T433 discharges the classical single-instance proof obligation: "
                "once A1 contains the full co-present finite classical code, every "
                "total separator is recoverable by lookup. A0 insufficiency is a "
                "declared boundary relative to A1, not a physical one."
            ),
        },
        "named_cases": [case.to_dict() for case in cases],
        "exhaustive_mixed_sweep": sweep,
        "honest_ceiling": proof["honest_scope"],
    }


def render_markdown(result: dict[str, object]) -> str:
    proof = result["proof_certificate"]
    verdict = result["overall_verdict"]

    step_rows = [
        "| {id} | {step} | {discharged_by} |".format(**step)
        for step in proof["proof_steps"]
    ]
    case_rows = [
        "| {name} | {shape} | {region} | {supports} | {boundary} | {verdict} |".format(
            name=case["name"],
            shape=" x ".join(str(size) for size in case["domain_sizes"]),
            region=case["region_label"],
            supports=", ".join(case["minimal_coordinate_support_labels"]),
            boundary="yes" if case["has_boundary_pair"] else "no",
            verdict=case["verdict"],
        )
        for case in result["named_cases"]
    ]
    sweep_rows = [
        "| {shape} | {checks} | {boundaries} | {declared} | {physical} |".format(
            shape=" x ".join(str(size) for size in row["domain_shape"]),
            checks=row["total_region_function_checks"],
            boundaries=row["boundary_functions"],
            declared=row["a1_declared_boundaries"],
            physical=row["single_instance_physical_candidates_relative_to_A1"],
        )
        for row in result["exhaustive_mixed_sweep"]
    ]

    return "\n".join(
        [
            "# T433 - Classical Declarability Proof Certificate - v0.1 results",
            "",
            "> Recorded-tier exploratory artifact. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are UNTOUCHED. No claim promotion. This is a "
            "classical finite-product proof certificate only; it does not touch "
            "the quantum E3 route.",
            "",
            "- Spec (frozen first): `tests/T433-classical-declarability-proof-certificate.md`",
            "- Model: `models/classical_declarability_proof_certificate.py`",
            "- Tests: `tests/test_classical_declarability_proof_certificate.py`",
            "- Artifact JSON: `results/T433-classical-declarability-proof-certificate-v0.1.json`",
            "- Run: `python -m pytest tests/test_classical_declarability_proof_certificate.py -q`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Theorem Statement",
            "",
            proof["statement"],
            "",
            "## Proof Certificate",
            "",
            "| step | content | discharged by |",
            "| --- | --- | --- |",
            *step_rows,
            "",
            "## Named Cases",
            "",
            "| case | domain shape | region A0 | minimal supports | boundary pair? | verdict |",
            "| --- | --- | --- | --- | --- | --- |",
            *case_rows,
            "",
            "## Mixed Finite Sweep",
            "",
            "| domain shape | checks | boundary functions | A1-declared boundaries | physical candidates |",
            "| --- | --- | --- | --- | --- |",
            *sweep_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a constructive classical proof certificate replacing the small-sweep "
            "reading with the general finite-product argument: every total datum "
            "factors through the A1 identity/full-code readout by lookup.",
            "",
            "Does not earn: a universal no-go theorem, a quantum theorem, an E3/WAY "
            "statement, a claim-ledger update, a public-posture update, or cross-repo "
            "support.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
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
        json_path = results_dir / "T433-classical-declarability-proof-certificate-v0.1.json"
        md_path = results_dir / "T433-classical-declarability-proof-certificate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
