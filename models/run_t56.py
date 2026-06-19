"""Runner for T56: Sheaf Cohomology of Apparent Finality — Research Audit."""

from __future__ import annotations

import json

from models.sheaf_cohomology_apparent_finality import (
    AuditOutcome,
    CircularRisk,
    _build_hidden_intermediary_cover,
    _build_dense_cover,
    compute_apparent_order,
    compute_cech_complex,
    compute_global_order,
    run_t56_audit,
    t56_result_to_dict,
)


def _hr(char: str = "-", width: int = 72) -> str:
    return char * width


def main() -> None:
    print(_hr("="))
    print("T56: Sheaf Cohomology of Apparent Finality -- Research Audit")
    print(_hr("="))

    result = run_t56_audit()

    # -----------------------------------------------------------------------
    # Cover summary
    # -----------------------------------------------------------------------
    print(f"\nCover: {result.cover.name}")
    print(f"Events: {[e.name for e in result.cover.events]}")
    for patch in result.cover.patches:
        acc = result.cover.accessible_event_names(patch)
        print(f"  {patch.name}: records={sorted(patch.accessible_records)}, "
              f"events={sorted(acc)}")

    # -----------------------------------------------------------------------
    # Global order
    # -----------------------------------------------------------------------
    non_refl = sorted(
        (a, b) for (a, b) in result.global_order if a != b
    )
    print(f"\nGlobal order (non-reflexive): {non_refl}")

    # -----------------------------------------------------------------------
    # Local apparent orders
    # -----------------------------------------------------------------------
    print("\nLocal apparent orders:")
    for patch in result.cover.patches:
        lo = compute_apparent_order(result.cover, patch)
        nr = sorted((a, b) for (a, b) in lo if a != b)
        print(f"  F({patch.name}) = {nr}")

    # -----------------------------------------------------------------------
    # Presheaf checks
    # -----------------------------------------------------------------------
    print(_hr())
    print("PRESHEAF ANALYSIS")
    print(_hr())
    print(f"\nAmbient presheaf A(U) = ρ_U(S_global):")
    print(f"  Functorial: {result.ambient_presheaf_check.is_functorial}")
    print(f"  {result.ambient_presheaf_check.explanation}")

    print(f"\nApparent-finality assignment F(U) = S_local(U):")
    print(f"  Is presheaf: {result.apparent_presheaf_check.is_functorial}")
    if not result.apparent_presheaf_check.is_functorial:
        print(f"  Violation: {result.apparent_presheaf_check.violation_example}")
    print(f"  {result.apparent_presheaf_check.explanation}")

    # -----------------------------------------------------------------------
    # Phantom pairs
    # -----------------------------------------------------------------------
    print(_hr())
    print("PHANTOM INCOMPARABILITY DETECTION")
    print(_hr())
    if result.phantom_pairs:
        for p in result.phantom_pairs:
            print(f"\n  Phantom at {p.observer}:")
            print(f"    Local:  {p.local_order_at_observer}")
            print(f"    Global: {p.global_order}")
            print(f"    Hidden intermediaries: {list(p.hidden_intermediaries)}")
    else:
        print("  No phantom pairs detected.")

    # -----------------------------------------------------------------------
    # Section compatibility
    # -----------------------------------------------------------------------
    print(_hr())
    print("SECTION COMPATIBILITY (H⁰ ANALYSIS)")
    print(_hr())
    sc = result.section_compatibility
    print(f"\n  Local sections compatible: {sc.local_sections_compatible}")
    print(f"  Colimit is global section: {sc.colimit_section_compatible}")
    if sc.incompatibility_witnesses:
        print(f"  Incompatibilities ({len(sc.incompatibility_witnesses)}):")
        for (v_name, u_name, gap) in sc.incompatibility_witnesses:
            print(f"    ρ(F({v_name}))|_{{U={u_name}}} vs F({u_name}): gap = {sorted(gap)}")
    print(f"\n  Finding: {sc.finding}")

    # -----------------------------------------------------------------------
    # Čech H¹ analysis
    # -----------------------------------------------------------------------
    print(_hr())
    print("ČECH H¹ ANALYSIS")
    print(_hr())
    print("\nApparent presheaf F:")
    ha = result.cech_h1_apparent
    print(f"  dim(C¹) = {ha.c1_dimension}")
    print(f"  dim(im δ⁰) = {ha.im_d0_dimension}")
    print(f"  dim(H¹) = {ha.h1_dimension}")
    print(f"  Phantom in H¹: {ha.phantom_generates_h1}")
    print(f"  Finding: {ha.finding}")

    print("\nAmbient presheaf A:")
    hb = result.cech_h1_ambient
    print(f"  dim(C¹) = {hb.c1_dimension}")
    print(f"  dim(im δ⁰) = {hb.im_d0_dimension}")
    print(f"  dim(H¹) = {hb.h1_dimension}")
    print(f"  Phantom in H¹: {hb.phantom_generates_h1}")
    print(f"  Finding: {hb.finding}")

    # -----------------------------------------------------------------------
    # Dense cover supplemental check
    # -----------------------------------------------------------------------
    print(_hr())
    print("SUPPLEMENTAL: DENSE COVER (U_P + U_full)")
    print(_hr())
    dense = _build_dense_cover()
    dense_global = compute_global_order(dense)
    dense_h1 = compute_cech_complex(dense, dense_global, use_apparent_for_local=True)
    print(f"\n  dim(C¹) = {dense_h1.c1_dimension}")
    print(f"  dim(im δ⁰) = {dense_h1.im_d0_dimension}")
    print(f"  dim(H¹) = {dense_h1.h1_dimension}")
    print(f"  Finding: {dense_h1.finding}")
    print(
        "\n  Note: in the dense cover {U_P, U_full}, the overlap U_P ∩ U_full = U_P "
        "has two accessible events (e_j, e_i). The C¹ slot for (U_P, U_full) is "
        "non-trivial. H¹ is computed above — if nonzero, it indicates the phantom "
        "pair (e_j, e_i) CAN appear in H¹ with a richer cover."
    )

    # -----------------------------------------------------------------------
    # Assumption ledger
    # -----------------------------------------------------------------------
    print(_hr())
    print("ASSUMPTION LEDGER")
    print(_hr())
    for entry in result.assumption_ledger:
        risk_str = entry.circular_risk.value.upper()
        print(f"\n  [{entry.name}]")
        print(f"    Inherited: {entry.inherited_from}")
        print(f"    Status:    {entry.status.value}")
        print(f"    Circ risk: {risk_str}")
        if entry.circular_risk in (CircularRisk.MEDIUM, CircularRisk.HIGH):
            print(f"    Risk note: {entry.risk_note[:120]}...")

    # -----------------------------------------------------------------------
    # Outcome
    # -----------------------------------------------------------------------
    print(_hr("═"))
    print(f"OUTCOME: {result.outcome.value.upper()}")
    print(_hr("═"))
    print(f"\n{result.finding}\n")

    print("REFINED HYPOTHESIS:")
    print(result.refined_hypothesis)

    print("\nOPEN QUESTIONS:")
    for q in result.open_questions:
        print(f"  {q}")

    # -----------------------------------------------------------------------
    # Export JSON
    # -----------------------------------------------------------------------
    out_path = "results/sheaf-cohomology-apparent-finality-v0.1-results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(t56_result_to_dict(result), f, indent=2)
    print(f"\nResults written to {out_path}")


if __name__ == "__main__":
    main()
