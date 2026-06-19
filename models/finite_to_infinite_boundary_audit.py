"""T59: Finite-to-Infinite Boundary Audit.

This model tests one boundary raised by T59:

    Does the T39 signed-graph parity criterion survive the move from finite
    binary same/different CSPs to continuous orientation data?

The audit uses a minimal Mobius-style orientation witness. A two-patch cover of
the base circle has two disconnected overlap components. For the trivial
cylinder both transition signs are +1. For the Mobius case one overlap has
transition +1 and the other has transition -1, giving nontrivial monodromy.

The result is intentionally not a universal theorem. It separates two
encodings:

* transition-aware Z2 encoding: preserves the two overlap components and their
  signs, so T39 parity detects the Mobius obstruction.
* coefficient-blind scalar encoding: forgets the transition signs and treats all
  overlaps as ordinary agreement, so T39 parity reports a false global section.

The boundary is therefore: parity survives only after the correct coefficient
and transition data have been reduced to a signed finite problem. It is not a
generic detector for continuous-domain obstruction.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Any


Relation = str


@dataclass(frozen=True)
class OverlapComponent:
    """One connected component of an overlap between two chart patches."""

    name: str
    transition_sign: int  # +1 keeps orientation; -1 reverses orientation.


@dataclass(frozen=True)
class OrientationCover:
    """A two-patch orientation cover with signed transition data."""

    name: str
    patches: tuple[str, str]
    overlap_components: tuple[OverlapComponent, ...]

    @property
    def monodromy_sign(self) -> int:
        sign = 1
        for component in self.overlap_components:
            sign *= component.transition_sign
        return sign

    @property
    def orientation_global_section_exists(self) -> bool:
        return self.monodromy_sign == 1

    @property
    def orientation_obstructed(self) -> bool:
        return not self.orientation_global_section_exists


@dataclass(frozen=True)
class SignedConstraint:
    """Finite same/different constraint used by the T39 parity criterion."""

    left: str
    right: str
    relation: Relation  # "same" or "different"
    source_component: str


@dataclass(frozen=True)
class SignedParityVerdict:
    """Result of signed-graph parity analysis."""

    variables: tuple[str, ...]
    constraints: tuple[SignedConstraint, ...]
    globally_satisfiable: bool
    obstruction_detected: bool
    global_witness_count: int
    obstruction_type: str
    witness_assignment: dict[str, int] | None


@dataclass(frozen=True)
class BoundaryEncodingAudit:
    """Comparison between topological orientation obstruction and parity."""

    cover_name: str
    encoding: str
    topological_monodromy_sign: int
    orientation_global_section_exists: bool
    parity_global_section_exists: bool
    parity_obstruction_detected: bool
    parity_matches_orientation: bool
    false_global_section: bool
    constraints: tuple[SignedConstraint, ...]
    conclusion: str


@dataclass(frozen=True)
class HypothesisResult:
    """Evaluation of one T59 finite-to-continuous boundary hypothesis."""

    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T59Result:
    """Complete T59 Mobius-boundary audit result."""

    audits: tuple[BoundaryEncodingAudit, ...]
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    transition_aware_detects_mobius: bool
    coefficient_blind_misses_mobius: bool
    cylinder_controls_pass: bool
    best_supported: str
    boundary: str
    recommended_next: str


def build_mobius_orientation_cover() -> OrientationCover:
    """Return a two-patch Mobius-style orientation witness."""

    return OrientationCover(
        name="mobius_two_patch_orientation_cover",
        patches=("U0", "U1"),
        overlap_components=(
            OverlapComponent("I_plus", 1),
            OverlapComponent("I_minus", -1),
        ),
    )


def build_cylinder_orientation_cover() -> OrientationCover:
    """Return the trivial control cover."""

    return OrientationCover(
        name="cylinder_two_patch_orientation_cover",
        patches=("U0", "U1"),
        overlap_components=(
            OverlapComponent("I_plus", 1),
            OverlapComponent("I_minus", 1),
        ),
    )


def _relation_from_sign(sign: int) -> Relation:
    if sign == 1:
        return "same"
    if sign == -1:
        return "different"
    raise ValueError(f"transition_sign must be +1 or -1, got {sign!r}")


def transition_aware_z2_constraints(cover: OrientationCover) -> tuple[SignedConstraint, ...]:
    """Encode every overlap component and transition sign as a finite constraint."""

    left, right = cover.patches
    return tuple(
        SignedConstraint(
            left=left,
            right=right,
            relation=_relation_from_sign(component.transition_sign),
            source_component=component.name,
        )
        for component in cover.overlap_components
    )


def coefficient_blind_scalar_constraints(cover: OrientationCover) -> tuple[SignedConstraint, ...]:
    """Forget transition signs and encode every overlap as ordinary agreement."""

    left, right = cover.patches
    return tuple(
        SignedConstraint(
            left=left,
            right=right,
            relation="same",
            source_component=component.name,
        )
        for component in cover.overlap_components
    )


def signed_parity_verdict(constraints: tuple[SignedConstraint, ...]) -> SignedParityVerdict:
    """Apply the T39 signed-graph parity criterion to finite constraints."""

    variables = tuple(sorted({c.left for c in constraints} | {c.right for c in constraints}))
    witness: dict[str, int] | None = None
    witness_count = 0

    for values in product((-1, 1), repeat=len(variables)):
        assignment = dict(zip(variables, values))
        if all(_satisfies(assignment, constraint) for constraint in constraints):
            witness_count += 1
            if witness is None:
                witness = assignment

    obstruction_detected = witness_count == 0
    if not obstruction_detected:
        obstruction_type = "none"
    elif _has_direct_conflict(constraints):
        obstruction_type = "direct_parity_conflict"
    else:
        obstruction_type = "negative_cycle"

    return SignedParityVerdict(
        variables=variables,
        constraints=constraints,
        globally_satisfiable=not obstruction_detected,
        obstruction_detected=obstruction_detected,
        global_witness_count=witness_count,
        obstruction_type=obstruction_type,
        witness_assignment=witness,
    )


def _satisfies(assignment: dict[str, int], constraint: SignedConstraint) -> bool:
    left = assignment[constraint.left]
    right = assignment[constraint.right]
    if constraint.relation == "same":
        return left == right
    if constraint.relation == "different":
        return left != right
    raise ValueError(f"unknown relation: {constraint.relation!r}")


def _has_direct_conflict(constraints: tuple[SignedConstraint, ...]) -> bool:
    seen: dict[frozenset[str], set[str]] = {}
    for constraint in constraints:
        pair = frozenset((constraint.left, constraint.right))
        seen.setdefault(pair, set()).add(constraint.relation)
    return any({"same", "different"}.issubset(relations) for relations in seen.values())


def audit_cover_encoding(cover: OrientationCover, encoding: str) -> BoundaryEncodingAudit:
    """Compare one finite parity encoding against the orientation-cover truth."""

    if encoding == "transition_aware_z2":
        constraints = transition_aware_z2_constraints(cover)
    elif encoding == "coefficient_blind_scalar":
        constraints = coefficient_blind_scalar_constraints(cover)
    else:
        raise ValueError(f"unknown encoding: {encoding!r}")

    parity = signed_parity_verdict(constraints)
    parity_matches = parity.globally_satisfiable == cover.orientation_global_section_exists
    false_global_section = parity.globally_satisfiable and cover.orientation_obstructed

    if parity_matches and parity.obstruction_detected:
        conclusion = (
            "parity detects the orientation obstruction because the encoding "
            "preserves transition signs"
        )
    elif parity_matches:
        conclusion = "parity agrees with the unobstructed control"
    elif false_global_section:
        conclusion = (
            "false global section: coefficient-blind parity forgets the Mobius "
            "transition sign and misses the continuous orientation obstruction"
        )
    else:
        conclusion = "mismatch: parity and orientation truth diverge"

    return BoundaryEncodingAudit(
        cover_name=cover.name,
        encoding=encoding,
        topological_monodromy_sign=cover.monodromy_sign,
        orientation_global_section_exists=cover.orientation_global_section_exists,
        parity_global_section_exists=parity.globally_satisfiable,
        parity_obstruction_detected=parity.obstruction_detected,
        parity_matches_orientation=parity_matches,
        false_global_section=false_global_section,
        constraints=constraints,
        conclusion=conclusion,
    )


def run_t59_analysis() -> T59Result:
    """Run the bounded Mobius finite-to-continuous boundary audit."""

    mobius = build_mobius_orientation_cover()
    cylinder = build_cylinder_orientation_cover()

    audits = (
        audit_cover_encoding(mobius, "transition_aware_z2"),
        audit_cover_encoding(mobius, "coefficient_blind_scalar"),
        audit_cover_encoding(cylinder, "transition_aware_z2"),
        audit_cover_encoding(cylinder, "coefficient_blind_scalar"),
    )

    by_key = {(audit.cover_name, audit.encoding): audit for audit in audits}
    mobius_aware = by_key[(mobius.name, "transition_aware_z2")]
    mobius_blind = by_key[(mobius.name, "coefficient_blind_scalar")]
    cylinder_audits = tuple(a for a in audits if a.cover_name == cylinder.name)

    transition_aware_detects = (
        mobius.orientation_obstructed
        and mobius_aware.parity_obstruction_detected
        and mobius_aware.parity_matches_orientation
    )
    coefficient_blind_misses = mobius_blind.false_global_section
    cylinder_controls_pass = all(
        audit.parity_matches_orientation
        and audit.orientation_global_section_exists
        and audit.parity_global_section_exists
        for audit in cylinder_audits
    )

    hypotheses = (
        HypothesisResult(
            "H0",
            "The T39 signed-graph parity criterion is a universal continuous-domain obstruction detector.",
            "refuted" if coefficient_blind_misses else "not_refuted",
            (
                "The coefficient-blind scalar encoding of the Mobius cover has "
                "monodromy -1 but parity reports a satisfiable same/same finite "
                "constraint system."
            ),
        ),
        HypothesisResult(
            "H1",
            "The Mobius orientation obstruction is detected after a transition-aware Z2 reduction.",
            "supported" if transition_aware_detects else "refuted",
            (
                "Preserving both overlap components and their signs gives same "
                "plus different constraints on U0/U1, which parity classifies "
                "as a direct parity conflict."
            ),
        ),
        HypothesisResult(
            "H2",
            "Coefficient and transition data are load-bearing at the finite-to-continuous boundary.",
            "best_supported" if (
                transition_aware_detects and coefficient_blind_misses and cylinder_controls_pass
            ) else "partially_supported",
            (
                "The same Mobius topological case is correctly obstructed by the "
                "transition-aware encoding and incorrectly accepted by the "
                "coefficient-blind encoding; the cylinder controls remain "
                "accepted in both encodings."
            ),
        ),
    )

    best_supported = (
        "T39 parity survives the Mobius boundary only as a transition-aware Z2 "
        "special case. It is not licensed as a generic continuous-domain "
        "obstruction detector."
    )
    boundary = (
        "Continuous-domain claims must state the coefficient object and transition "
        "maps before applying finite parity language. Forgetting that data can "
        "produce a false global section even when the orientation monodromy is "
        "nontrivial."
    )
    recommended_next = (
        "Build the sheaf-H1 replacement for continuous orientation data and then "
        "compare its obstruction verdict against PO1 admissibility metadata."
    )

    return T59Result(
        audits=audits,
        hypothesis_evaluations=hypotheses,
        transition_aware_detects_mobius=transition_aware_detects,
        coefficient_blind_misses_mobius=coefficient_blind_misses,
        cylinder_controls_pass=cylinder_controls_pass,
        best_supported=best_supported,
        boundary=boundary,
        recommended_next=recommended_next,
    )


def t59_result_to_dict(result: T59Result) -> dict[str, Any]:
    """Serialize T59 results for reproducible evidence artifacts."""

    def _constraint_dict(constraint: SignedConstraint) -> dict[str, str]:
        return {
            "left": constraint.left,
            "right": constraint.right,
            "relation": constraint.relation,
            "source_component": constraint.source_component,
        }

    def _audit_dict(audit: BoundaryEncodingAudit) -> dict[str, Any]:
        return {
            "cover_name": audit.cover_name,
            "encoding": audit.encoding,
            "topological_monodromy_sign": audit.topological_monodromy_sign,
            "orientation_global_section_exists": audit.orientation_global_section_exists,
            "parity_global_section_exists": audit.parity_global_section_exists,
            "parity_obstruction_detected": audit.parity_obstruction_detected,
            "parity_matches_orientation": audit.parity_matches_orientation,
            "false_global_section": audit.false_global_section,
            "constraints": [_constraint_dict(c) for c in audit.constraints],
            "conclusion": audit.conclusion,
        }

    return {
        "audits": [_audit_dict(audit) for audit in result.audits],
        "hypothesis_evaluations": [
            {
                "id": h.hypothesis_id,
                "claim": h.claim,
                "status": h.status,
                "evidence": h.evidence,
            }
            for h in result.hypothesis_evaluations
        ],
        "transition_aware_detects_mobius": result.transition_aware_detects_mobius,
        "coefficient_blind_misses_mobius": result.coefficient_blind_misses_mobius,
        "cylinder_controls_pass": result.cylinder_controls_pass,
        "best_supported": result.best_supported,
        "boundary": result.boundary,
        "recommended_next": result.recommended_next,
    }
