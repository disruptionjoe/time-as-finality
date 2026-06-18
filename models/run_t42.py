"""Runner for T42: local persistence and reconciliation split audit."""

from __future__ import annotations

import json
from pathlib import Path

from models.local_persistence_reconciliation import run_t42_analysis, t42_result_to_dict


def main() -> None:
    result = run_t42_analysis()
    data = t42_result_to_dict(result)

    out_path = Path("results") / "local-persistence-reconciliation-split-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("T42: Local Persistence and Reconciliation Split Audit")
    print()
    print("  Witness cases:")
    for scenario in result.scenarios:
        status = "PASS" if scenario.passed else "FAIL"
        obs = scenario.observation
        print(f"    [{status}] {scenario.name}")
        print(f"      classification:       {obs.classification}")
        print(f"      accumulation diff:    {obs.local_accumulation_difference}")
        print(f"      reconciliation lag:   {obs.reconciliation_lag_events}")
        print(f"      source accumulation:  {obs.source_total_accumulation}")
        print(f"      target accumulation:  {obs.target_total_accumulation}")
        print(f"      visible source index: {obs.source_visible_index}")
    print()
    print(f"  All witnesses pass:      {result.all_witnesses_pass}")
    print(f"  Independence witnessed:  {result.independence_witnessed}")
    print()
    print("  Hypothesis verdicts:")
    for h in result.hypothesis_evaluations:
        print(f"    {h.hypothesis_id}: {h.status}")
    print()
    print(f"  Best supported: {result.best_supported_hypothesis}")
    print()
    print("  Theorem:")
    print(f"    {result.theorem}")
    print()
    print("  Boundary:")
    print(f"    {result.boundary}")
    print()
    print(f"  Results written to {out_path}")


if __name__ == "__main__":
    main()
