"""Runner for T41: Typed transport category prototype."""

from __future__ import annotations

import json
import os

from models.typed_transport_category import run_t41_analysis, t41_result_to_dict

RESULTS_PATH = os.path.join(
    os.path.dirname(__file__), "..", "results", "typed-transport-category-v0.1.json"
)


def main() -> None:
    result = run_t41_analysis()
    data = t41_result_to_dict(result)

    print("=== T41: Typed Transport Category Prototype ===\n")
    print(f"Category objects: {result.category_objects}")
    print(f"Identity morphisms: {result.identity_morphisms}")

    print("\n--- Associativity tests ---")
    for t in result.associativity_tests:
        status = "PASS" if t.associativity_holds else "FAIL"
        print(f"  [{status}] {t.label}")
        if not t.associativity_holds:
            print(f"         site_map_associative={t.site_map_associative}")
            print(f"         preserved_dims_associative={t.preserved_dims_associative}")

    print("\n--- Left unit law tests ---")
    for t in result.left_unit_tests:
        status = "PASS" if t.law_holds else "FAIL"
        print(f"  [{status}] id_{t.identity_name.replace('id_', '')};{t.morphism_name} == {t.morphism_name}")

    print("\n--- Right unit law tests ---")
    for t in result.right_unit_tests:
        status = "PASS" if t.law_holds else "FAIL"
        print(f"  [{status}] {t.morphism_name};id_{t.identity_name.replace('id_', '')} == {t.morphism_name}")

    print("\n--- Category laws summary ---")
    for law in result.category_laws:
        status = "HOLDS" if law.holds else "FAILS"
        print(f"  [{status}] {law.law_name}: {law.tests_passed}/{law.tests_run} tests passed")

    print(f"\nForms proper category: {result.forms_proper_category}")

    print("\n--- PO1 functor tests ---")
    for t in result.po1_functor_tests:
        print(f"  {t.name}")
        print(f"    f ({t.f_name}) PO1: {t.f_po1} (failed: {t.f_failed_conditions})")
        print(f"    g ({t.g_name}) PO1: {t.g_po1} (failed: {t.g_failed_conditions})")
        print(f"    f;g ({t.fg_name}) PO1: {t.fg_po1} (failed: {t.fg_failed_conditions})")
        print(f"    Boolean-AND predicts PO1: {t.boolean_and_predicts_po1}")
        print(f"    Functor law violated: {t.functor_law_violated}")

    print("\n--- Hypotheses ---")
    for h in result.hypothesis_evaluations:
        print(f"  {h.hypothesis_id} [{h.status}]: {h.verdict[:80]}...")

    print(f"\nBest supported hypothesis: {result.best_supported_hypothesis}")

    print("\n--- Theorem ---")
    print(result.theorem_category)
    print()
    print(result.theorem_po1_nonfunctor)

    print("\n--- Boundary ---")
    print(result.boundary)

    print("\n--- Recommendation ---")
    print(result.recommendation)

    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)
    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\nResults written to {RESULTS_PATH}")


if __name__ == "__main__":
    main()
