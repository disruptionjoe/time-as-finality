"""Runner for T44: local mechanism identifiability audit."""

from __future__ import annotations

import json
from pathlib import Path

from models.local_mechanism_identifiability import run_t44_analysis, t44_result_to_dict


def main() -> None:
    result = run_t44_analysis()
    data = t44_result_to_dict(result)

    out_path = Path("results") / "local-mechanism-identifiability-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("T44: Local Mechanism Identifiability Audit")
    print()
    print("  Probe protocols:")
    for probe in result.probe_results:
        print(f"    {probe.probe_name}")
        print(f"      separates all:    {probe.separates_all}")
        print(f"      separated pairs:  {probe.separated_pairs}")
        print(f"      unresolved pairs: {probe.unresolved_pairs}")
    print()
    print("  Minimal basis:")
    print(f"    probes:        {result.minimal_basis.probe_names}")
    print(f"    separates all: {result.minimal_basis.separates_all}")
    print()
    print("  Unresolved weaker equivalences:")
    for item in result.unresolved_equivalences:
        print(f"    {item.name}: {item.unresolved_pairs}")
    print()
    print("  Hypothesis verdicts:")
    for h in result.hypothesis_evaluations:
        print(f"    {h.hypothesis_id}: {h.status}")
    print()
    print(f"  Best supported: {result.best_supported_hypothesis}")
    print()
    print(f"  Results written to {out_path}")


if __name__ == "__main__":
    main()
