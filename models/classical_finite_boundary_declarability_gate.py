"""T432 - Classical finite-boundary declarability gate.

This artifact makes the classical fragment of the capability-boundary taxonomy
executable. In a finite classical product model, A0 is the declared region
observable algebra and A1 is the full co-present classical code. Any separator
that is outside A0 but defined on the finite closed code is recoverable by A1,
so it is declared relative to A1 rather than single-instance physical.

Recorded-tier only. No claim promotion. This does not touch the quantum E3
route, WAY-style symmetry barriers, or any cross-repo truth.

Run:

    python -m models.classical_finite_boundary_declarability_gate --write-results
    python -m pytest tests/test_classical_finite_boundary_declarability_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
from typing import Callable, Iterable


Config = tuple[int, ...]
Coords = tuple[int, ...]
TruthTable = tuple[int, ...]


def configurations(n_bits: int) -> tuple[Config, ...]:
    if n_bits < 1:
        raise ValueError("n_bits must be positive")
    return tuple(product((0, 1), repeat=n_bits))


def coordinate_subsets(n_bits: int, include_full: bool = True) -> Iterable[Coords]:
    stop = n_bits + 1 if include_full else n_bits
    for size in range(stop):
        for subset in combinations(range(n_bits), size):
            yield subset


def config_index(config: Config) -> int:
    index = 0
    for bit in config:
        index = (index << 1) | bit
    return index


def table_value(table: TruthTable, config: Config) -> int:
    return table[config_index(config)]


def table_from_callable(n_bits: int, fn: Callable[[Config], int]) -> TruthTable:
    values = []
    for config in configurations(n_bits):
        value = fn(config)
        if value not in (0, 1):
            raise ValueError("truth table values must be binary")
        values.append(value)
    return tuple(values)


def all_binary_tables(n_bits: int) -> Iterable[TruthTable]:
    return product((0, 1), repeat=2 ** n_bits)


def projection(config: Config, coords: Coords) -> tuple[int, ...]:
    return tuple(config[index] for index in coords)


def is_constant_on_projection(table: TruthTable, n_bits: int, coords: Coords) -> bool:
    seen: dict[tuple[int, ...], int] = {}
    for config in configurations(n_bits):
        key = projection(config, coords)
        value = table_value(table, config)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def minimal_coordinate_supports(table: TruthTable, n_bits: int) -> tuple[Coords, ...]:
    supports: list[Coords] = []
    for coords in coordinate_subsets(n_bits):
        coord_set = set(coords)
        if any(set(existing).issubset(coord_set) for existing in supports):
            continue
        if is_constant_on_projection(table, n_bits, coords):
            supports.append(coords)
    return tuple(supports)


def boundary_pairs(table: TruthTable, n_bits: int, region: Coords) -> tuple[tuple[Config, Config], ...]:
    pairs: list[tuple[Config, Config]] = []
    configs = configurations(n_bits)
    for left, right in combinations(configs, 2):
        if projection(left, region) != projection(right, region):
            continue
        if table_value(table, left) != table_value(table, right):
            pairs.append((left, right))
    return tuple(pairs)


def coords_label(coords: Coords) -> str:
    if not coords:
        return "{}"
    return "{" + ",".join(f"x{coord}" for coord in coords) + "}"


@dataclass(frozen=True)
class ClassicalBoundaryCertificate:
    name: str
    n_bits: int
    region: Coords
    truth_table: TruthTable

    @property
    def full_coords(self) -> Coords:
        return tuple(range(self.n_bits))

    @property
    def a0_measurable(self) -> bool:
        return is_constant_on_projection(self.truth_table, self.n_bits, self.region)

    @property
    def a1_measurable(self) -> bool:
        return is_constant_on_projection(self.truth_table, self.n_bits, self.full_coords)

    @property
    def minimal_supports(self) -> tuple[Coords, ...]:
        return minimal_coordinate_supports(self.truth_table, self.n_bits)

    @property
    def boundary_pairs(self) -> tuple[tuple[Config, Config], ...]:
        return boundary_pairs(self.truth_table, self.n_bits, self.region)

    @property
    def has_boundary(self) -> bool:
        return bool(self.boundary_pairs)

    @property
    def has_no_proper_coordinate_support(self) -> bool:
        return self.minimal_supports == (self.full_coords,)

    @property
    def lookup_upper_bound(self) -> int:
        return 2 ** self.n_bits

    @property
    def verdict(self) -> str:
        if self.a0_measurable:
            return "NO_BOUNDARY_A0_REGION_DETERMINES_DATUM"
        if self.a1_measurable:
            return "E0_DECLARED_RELATIVE_TO_A1_FULL_CODE"
        return "INVALID_CLASSICAL_CLOSED_CODE"

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "n_bits": self.n_bits,
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
            "minimal_coordinate_supports": [
                list(support) for support in self.minimal_supports
            ],
            "minimal_coordinate_support_labels": [
                coords_label(support) for support in self.minimal_supports
            ],
            "has_no_proper_coordinate_support": self.has_no_proper_coordinate_support,
            "single_instance_lookup_upper_bound": self.lookup_upper_bound,
            "single_instance_physical_boundary_relative_to_A1": False,
            "verdict": self.verdict,
        }


def named_certificates() -> tuple[ClassicalBoundaryCertificate, ...]:
    return (
        ClassicalBoundaryCertificate(
            name="hidden_complement_bit",
            n_bits=2,
            region=(0,),
            truth_table=table_from_callable(2, lambda config: config[1]),
        ),
        ClassicalBoundaryCertificate(
            name="region_visible_control",
            n_bits=3,
            region=(0, 1),
            truth_table=table_from_callable(3, lambda config: config[0]),
        ),
        ClassicalBoundaryCertificate(
            name="full_support_parity_separator",
            n_bits=3,
            region=(0, 1),
            truth_table=table_from_callable(3, lambda config: config[0] ^ config[1] ^ config[2]),
        ),
        ClassicalBoundaryCertificate(
            name="region_plus_complement_relation",
            n_bits=3,
            region=(0,),
            truth_table=table_from_callable(3, lambda config: config[0] ^ config[1]),
        ),
    )


def exhaustive_boolean_summary(max_n_bits: int = 3) -> list[dict[str, object]]:
    summaries: list[dict[str, object]] = []
    for n_bits in range(1, max_n_bits + 1):
        total_region_function_checks = 0
        boundary_functions = 0
        a1_declared_boundaries = 0
        invalid_or_physical_candidates = 0
        no_proper_support_boundaries = 0

        for region in coordinate_subsets(n_bits, include_full=False):
            for table in all_binary_tables(n_bits):
                total_region_function_checks += 1
                cert = ClassicalBoundaryCertificate(
                    name="exhaustive",
                    n_bits=n_bits,
                    region=region,
                    truth_table=tuple(table),
                )
                if not cert.has_boundary:
                    continue
                boundary_functions += 1
                if cert.verdict == "E0_DECLARED_RELATIVE_TO_A1_FULL_CODE":
                    a1_declared_boundaries += 1
                else:
                    invalid_or_physical_candidates += 1
                if cert.has_no_proper_coordinate_support:
                    no_proper_support_boundaries += 1

        summaries.append(
            {
                "n_bits": n_bits,
                "proper_region_count": 2 ** n_bits - 1,
                "total_region_function_checks": total_region_function_checks,
                "boundary_functions": boundary_functions,
                "a1_declared_boundaries": a1_declared_boundaries,
                "invalid_or_physical_candidates": invalid_or_physical_candidates,
                "no_proper_support_boundaries": no_proper_support_boundaries,
            }
        )
    return summaries


def run() -> dict[str, object]:
    certificates = named_certificates()
    exhaustive = exhaustive_boolean_summary(max_n_bits=3)
    boundary_certificates = [cert for cert in certificates if cert.has_boundary]
    return {
        "artifact": "T432-classical-finite-boundary-declarability-gate-v0.1",
        "scope": (
            "Recorded-tier executable gate for the classical finite-state fragment "
            "of the capability-boundary mode taxonomy."
        ),
        "admissible_classes": {
            "A0": "own-region observables generated by the declared region coordinates",
            "A1": "full co-present finite classical code for the closed instance",
        },
        "overall_verdict": {
            "verdict": "C_FRAGMENT_EXECUTABLE_E0_FOR_SINGLE_INSTANCE",
            "reading": (
                "In the tested classical finite product regime, every separator "
                "outside the A0 region algebra is recovered by A1 full-code lookup. "
                "Even a full-support parity separator with no proper coordinate "
                "support is declared relative to A1, not single-instance physical."
            ),
            "no_physical_candidates_in_exhaustive_sweep": all(
                row["invalid_or_physical_candidates"] == 0 for row in exhaustive
            ),
        },
        "named_certificates": [cert.to_dict() for cert in certificates],
        "exhaustive_boolean_sweep": exhaustive,
        "all_named_boundaries_declared_relative_to_A1": all(
            cert.verdict == "E0_DECLARED_RELATIVE_TO_A1_FULL_CODE"
            for cert in boundary_certificates
        ),
        "honest_ceiling": (
            "This supports only the classical finite-state C fragment as an "
            "executable certificate. It is not a universal no-go theorem, not a "
            "quantum statement, not an E3 result, not claim-ledger movement, and "
            "not cross-repo evidence."
        ),
    }


def render_markdown(result: dict[str, object]) -> str:
    named_rows = []
    for cert in result["named_certificates"]:
        named_rows.append(
            "| {name} | {region} | {supports} | {boundary} | {verdict} |".format(
                name=cert["name"],
                region=cert["region_label"],
                supports=", ".join(cert["minimal_coordinate_support_labels"]),
                boundary="yes" if cert["has_boundary_pair"] else "no",
                verdict=cert["verdict"],
            )
        )

    sweep_rows = []
    for row in result["exhaustive_boolean_sweep"]:
        sweep_rows.append(
            "| {n_bits} | {checks} | {boundaries} | {declared} | {physical} | {full} |".format(
                n_bits=row["n_bits"],
                checks=row["total_region_function_checks"],
                boundaries=row["boundary_functions"],
                declared=row["a1_declared_boundaries"],
                physical=row["invalid_or_physical_candidates"],
                full=row["no_proper_support_boundaries"],
            )
        )

    verdict = result["overall_verdict"]
    return "\n".join(
        [
            "# T432 - Classical Finite-Boundary Declarability Gate - v0.1 results",
            "",
            "> Recorded-tier exploratory artifact. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are UNTOUCHED. No claim promotion. This is a "
            "classical finite-state C-fragment certificate only; it does not touch "
            "the quantum E3 route.",
            "",
            "- Spec (frozen first): `tests/T432-classical-finite-boundary-declarability-gate.md`",
            "- Model: `models/classical_finite_boundary_declarability_gate.py`",
            "- Tests: `tests/test_classical_finite_boundary_declarability_gate.py`",
            "- Artifact JSON: `results/T432-classical-finite-boundary-declarability-gate-v0.1.json`",
            "- Run: `python -m pytest tests/test_classical_finite_boundary_declarability_gate.py -q`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Named Certificates",
            "",
            "| certificate | region A0 | minimal coordinate supports | boundary pair? | verdict |",
            "| --- | --- | --- | --- | --- |",
            *named_rows,
            "",
            "## Exhaustive Small Boolean Sweep",
            "",
            "| n bits | checks | boundary functions | A1-declared boundaries | physical candidates | no-proper-support boundaries |",
            "| --- | --- | --- | --- | --- | --- |",
            *sweep_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: an executable finite-classical check for the taxonomy's C-fragment: "
            "single-instance separators outside A0 are still recovered by A1 full-code "
            "lookup. The `full_support_parity_separator` is the guard case: no proper "
            "coordinate subset determines it, but the finite closed full code still does.",
            "",
            "Does not earn: a universal no-go theorem, a quantum theorem, a WAY/E3 "
            "result, a claim-ledger update, a public-posture update, or cross-repo "
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
        json_path = results_dir / "T432-classical-finite-boundary-declarability-gate-v0.1.json"
        md_path = results_dir / "T432-classical-finite-boundary-declarability-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
