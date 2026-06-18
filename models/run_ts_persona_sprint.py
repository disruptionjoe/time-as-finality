"""Runner for TS-PERSONA-SPRINT-001: Time-series persona sprint on holonic records.

Writes machine-readable results to results/ts-persona-sprint-001-v0.1.json.
"""

import json
import pathlib
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from models.ts_persona_sprint import run_sprint, sprint_to_dict


def main() -> None:
    summary = run_sprint()
    data = sprint_to_dict(summary)

    out_path = pathlib.Path("results/ts-persona-sprint-001-v0.1.json")
    out_path.parent.mkdir(exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    c = summary.canonical_result
    n = len(summary.trajectories)

    print("=" * 68)
    print("TS-PERSONA-SPRINT-001 Results")
    print("=" * 68)
    print()
    print("CENTRAL QUESTION:")
    print("  Do TS dynamics provide new math structure or derived observables?")
    print()
    print(f"Trajectories tested: {n}")
    print(f"Persistence gap range: {summary.persistence_gap_range[0]}–{summary.persistence_gap_range[1]} steps")
    print(f"Canonical PG: {c.persistence_gap} | LOD: {c.lag_onset_distance}")
    print()
    print("Canonical trajectory coordinates:")
    for coord in c.coordinates:
        print(f"  {coord.level:12s}  DT_mean={coord.dwell_time_mean:5.1f}  "
              f"DT_max={coord.dwell_time_max:2d}  obstr={coord.obstruction_fraction:.2f}")
    print()
    print("Cross-trajectory agreement:")
    print(f"  Holonic dwell dominates (all variants):  {summary.holonic_dwell_dominates}")
    print(f"  Micro leads onset (all variants):        {summary.micro_leads_onset_all}")
    print(f"  Holonic leads offset (all variants):     {summary.holonic_leads_offset_all}")
    print(f"  Holonic more predictable: {summary.holonic_more_predictable_count}/{n}")
    print(f"  Holonic more irreversible: {summary.holonic_more_irreversible_count}/{n}")
    print(f"  Cointegration detected: {summary.cointegration_count}/{n}")
    print()
    print("COORDINATE CLASSIFICATIONS:")
    for cc in summary.coordinate_classifications:
        print(f"  {cc.symbol} ({cc.name}): {cc.classification}")
    print()
    print("INVESTIGATION VERDICT:")
    print(f"  {summary.investigation_verdict}")
    print()
    print("Elena Voss (canonical):")
    print(f"  {c.elena_voss.finding}")
    print()
    print("Marcus Hale (canonical):")
    print(f"  {c.marcus_hale.finding}")
    print()
    print("Aisha Rahman (canonical):")
    print(f"  {c.aisha_rahman.finding}")
    print()
    print("Rafael Cortez (canonical):")
    print(f"  {c.rafael_cortez.finding}")
    print()
    print("Lena Kowalski (canonical):")
    print(f"  {c.lena_kowalski.finding}")
    print()
    print("Follow-on goals:")
    for g in summary.follow_on_goals:
        print(f"  • {g}")
    print()
    print(f"Output written to {out_path}")


if __name__ == "__main__":
    main()
