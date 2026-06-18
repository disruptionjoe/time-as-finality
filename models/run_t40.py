"""Runner for T40: Holarchy Lab — Emergent Holonic Finality."""

import json
import sys
from pathlib import Path

from models.holarchy_lab import run_t40_analysis, t40_result_to_dict


def main() -> None:
    result = run_t40_analysis()
    data = t40_result_to_dict(result)

    out_path = Path("results") / "holarchy-lab-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2))

    print("T40: Holarchy Lab — Emergent Holonic Finality")
    print()
    print("  Scenario results:")
    for s in result.scenarios:
        micro_tag = "all-micro-sat" if s.all_micro_satisfiable else "MICRO-OBSTRUCTED"
        holonic_tag = "holonic-sat" if s.holonic_globally_satisfiable else "HOLONIC-OBSTRUCTED"
        emerg_tag = "  [EMERGENCE]" if s.emergence_detected else ""
        print(f"    {s.network_name:40s}  {micro_tag:17s}  {holonic_tag:20s}{emerg_tag}")
    print()
    print(f"  Emergence count:      {result.emergence_count}")
    print(f"  PO1 admissible count: {result.po1_admissible_count}")
    print()
    print("  Holonic PO1 bridges:")
    for b in result.holonic_po1_bridges:
        adm = "ADMISSIBLE" if b.holonic_po1_admissible else "not admissible"
        ac5 = "AC5" if b.ac5_fires else "no-AC5"
        print(f"    {b.case_name:45s}  {adm:12s}  {ac5}")
    print()
    print("  Hypothesis verdicts:")
    for h in result.hypothesis_evaluations:
        print(f"    {h.hypothesis_id}: {h.verdict}")
    print()
    print(f"  Best supported: {result.best_supported_hypothesis}")
    print()
    print(f"  Results written to {out_path}")


if __name__ == "__main__":
    main()
    sys.exit(0)
