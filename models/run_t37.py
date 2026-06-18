"""Runner for T37: typed transport network analysis."""

import json
import sys
from pathlib import Path

from models.transport_network import run_t37_analysis, t37_result_to_dict


def main() -> None:
    result = run_t37_analysis()
    data = t37_result_to_dict(result)

    out_path = Path("results") / "transport-network-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2))

    spec = result.spectre_network_analysis
    diag = result.diamond_network_analysis

    print("T37: Typed Transport Network")
    print(f"  Spectre network: {spec.layer_count} layers, {spec.transport_count} transports")
    print(f"  Spectre verdict:  {spec.verdict}")
    print(f"  T34 consistency:  {result.t34_consistency}")
    print()
    print(f"  Diamond network: {diag.layer_count} layers, {diag.transport_count} transports")
    print(f"  Diamond verdict:  {diag.verdict}")
    print(f"  Path dependence:  {result.path_dependence_witnessed}")
    if diag.path_dependence_witness:
        w = diag.path_dependence_witness
        print(f"  PO1 path:         {' -> '.join(w.po1_path.layer_names)}")
        print(f"    forgotten: {w.po1_forgotten}")
        print(f"  Non-PO1 path:     {' -> '.join(w.non_po1_path.layer_names)}")
        print(f"    forgotten: {w.non_po1_forgotten}")
        print(f"    failing:   {w.failing_conditions}")
    print()
    print(f"  Results written to {out_path}")


if __name__ == "__main__":
    main()
    sys.exit(0)
