"""Runner for T39: CSP / satisfiability reframing."""

import json
import sys
from pathlib import Path

from models.csp_satisfiability_reframing import run_t39_analysis, t39_result_to_dict


def main() -> None:
    result = run_t39_analysis()
    data = t39_result_to_dict(result)

    out_path = Path("results") / "csp-satisfiability-reframing-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2))

    print("T39: CSP / Satisfiability Reframing")
    print()
    print("  D1-to-CSP analyses:")
    for a in result.d1_to_csp_analyses:
        gs = "satisfiable" if a.parity.globally_satisfiable else f"OBSTRUCTED ({a.parity.obstruction_type})"
        print(f"    {a.csp.name:30s}  vars={len(a.csp.variables)}  {gs}")
        print(f"      arc-consistent={a.arc_consistency.all_arc_consistent}  "
              f"locally={a.parity.locally_satisfiable}  D1-equiv={a.d1_equivalence_verified}")
    print()
    print("  Minimum obstructions:")
    d = result.minimum_direct_obstruction
    t = result.minimum_transitive_obstruction
    print(f"    direct:     {d.csp.name}  "
          f"{len(d.csp.variables)} vars, {len(d.csp.all_constraints)} constraints — "
          f"{d.parity.obstruction_type}")
    print(f"    transitive: {t.csp.name}  "
          f"{len(t.csp.variables)} vars, {len(t.csp.all_constraints)} constraints — "
          f"{t.parity.obstruction_type}")
    print()
    print("  PO1-as-CSP bridges:")
    for b in result.po1_as_csp_bridges:
        print(f"    {b.case_name:40s}  PO1={b.po1_verdict}  "
              f"csp_detects={b.csp_detects_obstruction}  "
              f"target={b.target_obstruction_type}")
    print()
    print("  Hypothesis verdicts:")
    for h in result.hypothesis_evaluations:
        print(f"    {h.hypothesis_id}: {h.verdict}")
    print()
    print(f"  Best supported:   {result.best_supported_hypothesis}")
    print()
    print(f"  Results written to {out_path}")


if __name__ == "__main__":
    main()
    sys.exit(0)
