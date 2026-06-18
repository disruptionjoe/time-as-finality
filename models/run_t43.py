"""Runner for T43: local persistence accumulation mechanism audit."""

from __future__ import annotations

import json
from pathlib import Path

from models.local_persistence_mechanisms import run_t43_analysis, t43_result_to_dict


def main() -> None:
    result = run_t43_analysis()
    data = t43_result_to_dict(result)

    out_path = Path("results") / "local-persistence-mechanisms-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("T43: Local Persistence Accumulation Mechanism Audit")
    print()
    print("  Mechanism cases:")
    for case in result.mechanism_cases:
        obs = case.observation
        print(f"    {case.name}: {case.verdict}")
        print(f"      hypothesis:          {case.hypothesis_id}")
        print(f"      source total:        {obs.source_total_accumulation}")
        print(f"      target total:        {obs.target_total_accumulation}")
        print(f"      accumulation diff:   {obs.local_accumulation_difference}")
        print(f"      reconciliation lag:  {obs.reconciliation_lag_events}")
    print()
    print("  Propagation control:")
    print(f"    {result.propagation_control.verdict}")
    print()
    print("  Rejected candidate:")
    shadow = result.propagation_shadow_counterexample
    print(f"    {shadow.name}: eliminated={shadow.eliminated}")
    print(f"    reason: {shadow.reason}")
    print()
    print("  Equivalence classes:")
    for eq in result.equivalence_classes:
        print(f"    signature={eq.signature}: {eq.members}")
    print()
    print("  Hypothesis verdicts:")
    for h in result.hypothesis_evaluations:
        print(f"    {h.hypothesis_id}: {h.status}")
    print()
    print(f"  Best supported: {result.best_supported_hypothesis}")
    print(f"  Minimal extension: {result.minimal_extension}")
    print()
    print(f"  Results written to {out_path}")


if __name__ == "__main__":
    main()
