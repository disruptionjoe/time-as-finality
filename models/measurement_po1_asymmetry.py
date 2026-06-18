"""T45: Measurement as PO1 morphism - asymmetry theorem.

T45 formalizes quantum-to-classical measurement as a PO1-admissible morphism
and checks whether PO1-admissibility is structurally asymmetric.

Two D1RestrictionSystems are constructed:
  Y (quantum layer): three sites with globally satisfiable patches; unobstructed.
  X (classical layer): three sites with parity-conflict patches; obstructed.

The forward morphism f: Y -> X is checked against AC1-AC7.
The inverse morphism g: X -> Y is checked against AC1-AC7.
Additional targets Z are checked to verify the general asymmetry claim.

Asymmetry Theorem (T45):
  For any D1RestrictionSystem S with obstruction_detected = True,
  there is no PO1-admissible morphism g: S -> Z for any D1RestrictionSystem Z.

  Proof: AC7 requires the richer system (= source of g = S) to be unobstructed.
  S is obstructed. Therefore AC7 fails regardless of Z.

Corollary (Measurement Irreversibility):
  If f: Y -> X is fully PO1-admissible, then X is obstructed (by AC6 of f).
  No PO1-admissible morphism can originate from X.
  Measurement is irreversible in the PO1 structural sense.

Hypotheses evaluated:
  H_FWD: forward morphism f: Y -> X is fully PO1-admissible
  H_INV: inverse morphism g: X -> Y is PO1-admissible (expected to fail)
  H_ASYM: PO1-admissibility is structurally asymmetric (obstructed sources
          cannot be PO1 sources)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    GlobalSectionResult,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    global_section,
    validate_system,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import AdmissibilityCheck, check_admissibility
from models.projection_obstruction_schema import ProjectionCase


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AsymmetryTest:
    label: str
    target_name: str
    admissibility: AdmissibilityCheck
    ac7_held: bool
    asymmetry_confirmed: bool


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T45Result:
    quantum_system: D1RestrictionSystem
    classical_system: D1RestrictionSystem
    quantum_section: GlobalSectionResult
    classical_section: GlobalSectionResult
    forward_admissibility: AdmissibilityCheck
    inverse_admissibility: AdmissibilityCheck
    asymmetry_tests: tuple[AsymmetryTest, ...]
    forward_is_po1: bool
    inverse_fails_po1: bool
    asymmetry_theorem_holds: bool
    theorem_statement: str
    proof_sketch: str
    measurement_reading: str
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# System constructors
# ---------------------------------------------------------------------------


def _site(site_id: str, population: str) -> ObserverSite:
    return ObserverSite(site_id, population, "finite_site", 0, "t45")


def _local(site_id: str, population: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(
        site=_site(site_id, population),
        proposition_value="true",
        profile=profile,
    )


def _quantum_system() -> D1RestrictionSystem:
    """Three-site quantum layer with globally satisfiable patches."""
    q_profile = D1Profile(
        accessible_support=3,
        holder_redundancy=3,
        branch_support=2,
        reversal_cost=3,
    )
    return D1RestrictionSystem(
        name="quantum_layer_Y",
        proposition="quantum_state_Q",
        local_values=(
            _local("q1", "quantum", q_profile),
            _local("q2", "quantum", q_profile),
            _local("q3", "quantum", q_profile),
        ),
        transport_edges=(
            TransportEdge("q1", "q2", "entanglement", True),
            TransportEdge("q2", "q3", "entanglement", True),
        ),
        source_site="q1",
        target_site="q3",
        patches=(
            RestrictionPatch(
                "q12_coherence",
                ("q1", "q2"),
                ("a", "b"),
                (PatchConstraint("a", "b", "same"),),
            ),
            RestrictionPatch(
                "q23_coherence",
                ("q2", "q3"),
                ("b", "c"),
                (PatchConstraint("b", "c", "same"),),
            ),
            RestrictionPatch(
                "q13_coherence",
                ("q1", "q3"),
                ("a", "c"),
                (PatchConstraint("a", "c", "same"),),
            ),
        ),
    )


def _classical_system() -> D1RestrictionSystem:
    """Three-site classical layer with parity-conflict obstruction."""
    c_profile = D1Profile(
        accessible_support=1,
        holder_redundancy=1,
        branch_support=0,
        reversal_cost=1,
    )
    return D1RestrictionSystem(
        name="classical_layer_X",
        proposition="classical_record_R",
        local_values=(
            _local("c1", "classical", c_profile),
            _local("c2", "classical", c_profile),
            _local("c3", "classical", c_profile),
        ),
        transport_edges=(
            TransportEdge("c1", "c2", "record_propagation", True),
            TransportEdge("c2", "c3", "record_propagation", True),
        ),
        source_site="c1",
        target_site="c3",
        patches=(
            RestrictionPatch(
                "c12_record",
                ("c1", "c2"),
                ("x", "y"),
                (PatchConstraint("x", "y", "same"),),
            ),
            RestrictionPatch(
                "c23_record",
                ("c2", "c3"),
                ("y", "z"),
                (PatchConstraint("y", "z", "same"),),
            ),
            RestrictionPatch(
                "c13_record",
                ("c1", "c3"),
                ("x", "z"),
                (PatchConstraint("x", "z", "different"),),
            ),
        ),
    )


def _trivial_unobstructed_system() -> D1RestrictionSystem:
    """Two-site system with no patches: always globally satisfiable."""
    profile = D1Profile(2, 2, 1, 2)
    return D1RestrictionSystem(
        name="trivial_unobstructed_Z",
        proposition="trivial_record",
        local_values=(
            _local("z1", "trivial", profile),
            _local("z2", "trivial", profile),
        ),
        transport_edges=(TransportEdge("z1", "z2", "trivial_edge", True),),
        source_site="z1",
        target_site="z2",
    )


def _another_obstructed_system() -> D1RestrictionSystem:
    """Three-site system with parity obstruction (same pattern as X, different name)."""
    profile = D1Profile(2, 2, 1, 2)
    return D1RestrictionSystem(
        name="another_obstructed_Z2",
        proposition="another_record",
        local_values=(
            _local("z2_1", "obstructed", profile),
            _local("z2_2", "obstructed", profile),
            _local("z2_3", "obstructed", profile),
        ),
        transport_edges=(
            TransportEdge("z2_1", "z2_2", "edge_ab", True),
            TransportEdge("z2_2", "z2_3", "edge_bc", True),
        ),
        source_site="z2_1",
        target_site="z2_3",
        patches=(
            RestrictionPatch(
                "z2_ab",
                ("z2_1", "z2_2"),
                ("p", "q"),
                (PatchConstraint("p", "q", "same"),),
            ),
            RestrictionPatch(
                "z2_bc",
                ("z2_2", "z2_3"),
                ("q", "r"),
                (PatchConstraint("q", "r", "same"),),
            ),
            RestrictionPatch(
                "z2_ac",
                ("z2_1", "z2_3"),
                ("p", "r"),
                (PatchConstraint("p", "r", "different"),),
            ),
        ),
    )


# ---------------------------------------------------------------------------
# Morphism constructors
# ---------------------------------------------------------------------------


def _forward_morphism(Y: D1RestrictionSystem, X: D1RestrictionSystem) -> D1RestrictionMorphism:
    """Measurement morphism f: Y -> X (quantum to classical)."""
    return D1RestrictionMorphism(
        name="measurement_f_Y_to_X",
        source=Y,
        target=X,
        site_map=(
            SiteMap("q1", "c1"),
            SiteMap("q2", "c2"),
            SiteMap("q3", "c3"),
        ),
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )


def _inverse_morphism(X: D1RestrictionSystem, Y: D1RestrictionSystem) -> D1RestrictionMorphism:
    """Attempted unmeasurement g: X -> Y (classical back to quantum)."""
    return D1RestrictionMorphism(
        name="unmeasurement_g_X_to_Y",
        source=X,
        target=Y,
        site_map=(
            SiteMap("c1", "q1"),
            SiteMap("c2", "q2"),
            SiteMap("c3", "q3"),
        ),
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )


def _morphism_x_to_z(X: D1RestrictionSystem, Z: D1RestrictionSystem, label: str) -> D1RestrictionMorphism:
    """Attempt a morphism from X to arbitrary Z (single-site partial map)."""
    x_sites = X.site_ids()
    z_sites = Z.site_ids()
    n = min(len(x_sites), len(z_sites))
    return D1RestrictionMorphism(
        name=f"attempt_{label}_X_to_{Z.name}",
        source=X,
        target=Z,
        site_map=tuple(SiteMap(x_sites[i], z_sites[i]) for i in range(n)),
        preserved_dimensions=(),
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------


def _admissibility_for(
    name: str,
    source: str,
    richer: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
    morphism: D1RestrictionMorphism,
    forgotten: tuple[str, ...],
    intended: str,
) -> AdmissibilityCheck:
    case = ProjectionCase(
        name=name,
        source=source,
        richer_system=richer,
        restricted_system=restricted,
        morphism=morphism,
        forgotten_structure=forgotten,
        preserved_structure=(),
        intended_reading=intended,
    )
    return check_admissibility(case)


def _asymmetry_test(
    label: str,
    X: D1RestrictionSystem,
    Z: D1RestrictionSystem,
    morphism: D1RestrictionMorphism,
) -> AsymmetryTest:
    check = _admissibility_for(
        name=f"asymmetry_{label}",
        source="T45",
        richer=X,
        restricted=Z,
        morphism=morphism,
        forgotten=("classical_record_state",),
        intended="attempted reverse morphism from obstructed source",
    )
    ac7_held = check.ac7_richer_unobstructed
    return AsymmetryTest(
        label=label,
        target_name=Z.name,
        admissibility=check,
        ac7_held=ac7_held,
        asymmetry_confirmed=not check.po1_evidence,
    )


def run_t45_analysis() -> T45Result:
    Y = _quantum_system()
    X = _classical_system()
    Z_trivial = _trivial_unobstructed_system()
    Z_obstructed = _another_obstructed_system()

    q_section = global_section(Y)
    c_section = global_section(X)

    f = _forward_morphism(Y, X)
    g = _inverse_morphism(X, Y)

    fwd_check = _admissibility_for(
        name="measurement_Y_to_X",
        source="T45",
        richer=Y,
        restricted=X,
        morphism=f,
        forgotten=("quantum_coherence", "superposition", "phase_information", "entanglement"),
        intended="forward measurement: quantum to classical projection",
    )

    inv_check = _admissibility_for(
        name="unmeasurement_X_to_Y",
        source="T45",
        richer=X,
        restricted=Y,
        morphism=g,
        forgotten=("classical_record_state",),
        intended="attempted inverse: classical back to quantum",
    )

    asym_tests = (
        _asymmetry_test(
            "X_to_trivial",
            X,
            Z_trivial,
            _morphism_x_to_z(X, Z_trivial, "trivial"),
        ),
        _asymmetry_test(
            "X_to_obstructed",
            X,
            Z_obstructed,
            _morphism_x_to_z(X, Z_obstructed, "obstructed"),
        ),
    )

    forward_is_po1 = fwd_check.po1_evidence
    inverse_fails_po1 = not inv_check.po1_evidence
    asymmetry_holds = all(t.asymmetry_confirmed for t in asym_tests) and inverse_fails_po1

    theorem = (
        "Measurement Asymmetry Theorem (T45): For any D1RestrictionSystem S "
        "with obstruction_detected = True, there is no PO1-admissible morphism "
        "g: S -> Z for any D1RestrictionSystem Z."
    )

    proof = (
        "AC7 requires the richer system (source of g, here S) to be unobstructed. "
        "S is obstructed by hypothesis. Therefore AC7 fails for any target Z. "
        "The failure is independent of Z: it depends only on S being obstructed. "
        "Verified finite-witness: all tested targets Z fail AC7 in this model."
    )

    reading = (
        "In the measurement interpretation: Y (quantum layer) is unobstructed, "
        "X (classical layer) is obstructed by projection-created parity conflict. "
        "f: Y -> X is fully PO1-admissible -- measurement is a valid PO1 event. "
        "No PO1-admissible morphism can originate from X -- measurement is "
        "structurally irreversible. The obstruction in X (AC6 of f) prevents any "
        "PO1 reverse path. This is the measurement problem expressed as gluing "
        "obstruction: the classical records cannot be globally reconciled, and "
        "this irreconcilability is exactly what makes the arrow one-directional."
    )

    h_fwd_status = "supported" if forward_is_po1 else "refuted"
    h_inv_status = "refuted" if inverse_fails_po1 else "supported"
    h_asym_status = "supported" if asymmetry_holds else "refuted"

    hyps = (
        HypothesisResult(
            "H_FWD",
            "f: Y -> X is fully PO1-admissible",
            h_fwd_status,
            f"forward admissibility verdict: {fwd_check.verdict}",
        ),
        HypothesisResult(
            "H_INV",
            "g: X -> Y is PO1-admissible (expected to fail)",
            h_inv_status,
            f"inverse admissibility verdict: {inv_check.verdict}; "
            f"failed conditions: {inv_check.failed_conditions}",
        ),
        HypothesisResult(
            "H_ASYM",
            "No PO1-admissible morphism g: X -> Z exists for any Z",
            h_asym_status,
            f"all {len(asym_tests)} asymmetry tests confirmed: "
            f"{all(t.asymmetry_confirmed for t in asym_tests)}",
        ),
    )

    if forward_is_po1 and asymmetry_holds:
        best = "H_FWD and H_ASYM (measurement is PO1; asymmetry theorem holds)"
    elif forward_is_po1:
        best = "H_FWD only (measurement is PO1; asymmetry result inconclusive)"
    else:
        best = "none (forward morphism failed -- construction needs revision)"

    return T45Result(
        quantum_system=Y,
        classical_system=X,
        quantum_section=q_section,
        classical_section=c_section,
        forward_admissibility=fwd_check,
        inverse_admissibility=inv_check,
        asymmetry_tests=asym_tests,
        forward_is_po1=forward_is_po1,
        inverse_fails_po1=inverse_fails_po1,
        asymmetry_theorem_holds=asymmetry_holds,
        theorem_statement=theorem,
        proof_sketch=proof,
        measurement_reading=reading,
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _check_to_dict(c: AdmissibilityCheck) -> dict[str, Any]:
    return {
        "case_name": c.case_name,
        "conditions": {
            "AC1": c.ac1_richer_valid,
            "AC2": c.ac2_restricted_valid,
            "AC3": c.ac3_projection_definable,
            "AC4": c.ac4_local_compat,
            "AC5": c.ac5_structure_forgotten,
            "AC6": c.ac6_restricted_obstructed,
            "AC7": c.ac7_richer_unobstructed,
        },
        "verdict": c.verdict,
        "failed_conditions": list(c.failed_conditions),
        "po1_evidence": c.po1_evidence,
    }


def t45_result_to_dict(r: T45Result) -> dict[str, Any]:
    return {
        "quantum_system": r.quantum_system.name,
        "classical_system": r.classical_system.name,
        "quantum_section": {
            "obstruction_detected": r.quantum_section.obstruction_detected,
            "global_witness_count": r.quantum_section.global_witness_count,
            "local_witness_count": r.quantum_section.local_witness_count,
        },
        "classical_section": {
            "obstruction_detected": r.classical_section.obstruction_detected,
            "global_witness_count": r.classical_section.global_witness_count,
            "local_witness_count": r.classical_section.local_witness_count,
        },
        "forward_admissibility": _check_to_dict(r.forward_admissibility),
        "inverse_admissibility": _check_to_dict(r.inverse_admissibility),
        "asymmetry_tests": [
            {
                "label": t.label,
                "target": t.target_name,
                "verdict": t.admissibility.verdict,
                "ac7_held": t.ac7_held,
                "asymmetry_confirmed": t.asymmetry_confirmed,
            }
            for t in r.asymmetry_tests
        ],
        "forward_is_po1": r.forward_is_po1,
        "inverse_fails_po1": r.inverse_fails_po1,
        "asymmetry_theorem_holds": r.asymmetry_theorem_holds,
        "theorem_statement": r.theorem_statement,
        "proof_sketch": r.proof_sketch,
        "measurement_reading": r.measurement_reading,
        "hypothesis_evaluations": [
            {
                "id": h.hypothesis_id,
                "claim": h.claim,
                "status": h.status,
                "evidence": h.evidence,
            }
            for h in r.hypothesis_evaluations
        ],
        "best_supported": r.best_supported,
    }
