"""Runner for T45: Measurement PO1 asymmetry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.measurement_po1_asymmetry import run_t45_analysis, t45_result_to_dict


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t45_analysis()
    data = t45_result_to_dict(result)

    out_path = Path("results") / "measurement-po1-asymmetry-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T45: Measurement PO1 Asymmetry ===")
    print()
    print(f"Quantum system:  {result.quantum_system.name}")
    print(f"  obstruction: {result.quantum_section.obstruction_detected}")
    print(f"  global witnesses: {result.quantum_section.global_witness_count}")
    print()
    print(f"Classical system: {result.classical_system.name}")
    print(f"  obstruction: {result.classical_section.obstruction_detected}")
    print(f"  global witnesses: {result.classical_section.global_witness_count}")
    print()

    fwd = result.forward_admissibility
    print(f"Forward morphism f: Y -> X")
    print(f"  verdict: {fwd.verdict}")
    print(f"  PO1 evidence: {fwd.po1_evidence}")
    if fwd.failed_conditions:
        print(f"  failed: {fwd.failed_conditions}")
    else:
        ac = fwd
        print(f"  AC1={ac.ac1_richer_valid} AC2={ac.ac2_restricted_valid} "
              f"AC3={ac.ac3_projection_definable} AC4={ac.ac4_local_compat} "
              f"AC5={ac.ac5_structure_forgotten} AC6={ac.ac6_restricted_obstructed} "
              f"AC7={ac.ac7_richer_unobstructed}")
    print()

    inv = result.inverse_admissibility
    print(f"Inverse morphism g: X -> Y")
    print(f"  verdict: {inv.verdict}")
    print(f"  PO1 evidence: {inv.po1_evidence}")
    print(f"  failed conditions: {inv.failed_conditions}")
    print()

    print("Asymmetry tests (g: X -> Z for various Z):")
    for t in result.asymmetry_tests:
        status = "CONFIRMED" if t.asymmetry_confirmed else "FAILED"
        print(f"  [{status}] X -> {t.target_name}")
        print(f"    verdict: {t.admissibility.verdict}  AC7: {t.ac7_held}")
    print()

    print(f"Forward is PO1:         {result.forward_is_po1}")
    print(f"Inverse fails PO1:      {result.inverse_fails_po1}")
    print(f"Asymmetry theorem holds: {result.asymmetry_theorem_holds}")
    print()
    print("Theorem:")
    print(f"  {result.theorem_statement}")
    print()
    print("Proof sketch:")
    print(f"  {result.proof_sketch}")
    print()
    print("Hypotheses:")
    for h in result.hypothesis_evaluations:
        print(f"  {h.hypothesis_id} [{h.status}]: {h.claim}")
        print(f"    {h.evidence}")
    print()
    print(f"Best supported: {result.best_supported}")
    print()
    print(f"Results written to {out_path}")


if __name__ == "__main__":
    main()
