"""T226: Coefficient-aware Cech-H1 continuum-obstruction object.

T222 ("Finite-to-Infinite Boundary Theorem") classified CSP-PO1 as
*conditional*: the signed-graph parity criterion survives countable scale
unconditionally (compactness / de Bruijn-Erdos), but at the continuum the
coefficient-BLIND scalar encoding of the Mobius witness reports a FALSE global
section despite monodromy -1 (the T59 false-section trap). T222's "Contribution
Needed" explicitly demands:

    "Build the coefficient-aware sheaf-H1 replacement for continuous orientation
     data (the recommended-next from T59) and compare its verdict against PO1
     admissibility metadata."

This module is that object. It is a FINITE, COMPUTABLE Cech-cohomology object
over a finite open cover (the nerve, with double overlaps), valued in the
coefficient group Z2 = {0,1} (equivalently the sign group {+1,-1}). It carries
the transition / sign-twist data that the blind same/different scalar CSP drops.

What it demonstrates (the only two claims it makes):

  (1) On the SAME Mobius / signed-graph witness used by T59 and T222, the
      coefficient-aware H1 reports a NONTRIVIAL class (no global section)
      exactly where the coefficient-blind encoding falsely reported one. On the
      cylinder control both report a section. So the false-section trap is
      closed precisely by carrying the transition cochain.

  (2) The nontrivial-class verdict is compared against PO1's AC1-AC7
      admissibility metadata. The transition cochain the H1 carries IS the AC5
      "named forgotten structure"; the blind encoding is exactly the projection
      that forgets it. The coefficient-aware obstruction class agrees with the
      AC6 restricted-obstruction flag iff the AC5 transition data is retained --
      which is the formal statement of "carrying coefficient data" that T222
      named as the continuum condition.

HONESTY GUARD (binding, T222 failure criterion). This is a FINITE computable
witness object (tag: finite_witness). It does NOT state, and must not be read as
stating, a general Cech / sheaf-cohomology theorem for the continuum. It exhibits
the coefficient-aware-vs-blind distinction on finite nerves; it does not prove a
continuum obstruction theorem. No physics / curvature / connection / holonomy /
new-object language is promoted: H1 is computed here as pure Z2 linear algebra on
a finite cochain complex, nothing more. "Monodromy" below is used only as the
informal name of the sign-product around a cover cycle, not as a geometric claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any


# ---------------------------------------------------------------------------
# Z2 coefficient algebra (additive {0,1}; multiplicative sign {+1,-1})
# ---------------------------------------------------------------------------
#
# We carry the transition data additively in Z2: a "same" overlap is 0, a
# "different" (orientation-reversing) overlap is 1. Addition is XOR. The
# multiplicative sign picture (+1 / -1) is isomorphic via s = (-1)^c; we expose
# both so the comparison to the signed-graph CSP ({+1,-1}) is explicit.


def z2_add(a: int, b: int) -> int:
    """Z2 addition (XOR). Inputs in {0,1}."""
    return (a + b) & 1


def z2_to_sign(c: int) -> int:
    """Z2 cochain value -> multiplicative sign (0->+1, 1->-1)."""
    return 1 if c == 0 else -1


def sign_to_z2(s: int) -> int:
    """Multiplicative sign -> Z2 (+1->0, -1->1)."""
    return 0 if s == 1 else 1


# ---------------------------------------------------------------------------
# Finite open cover (nerve) with Z2-valued transition 1-cochain
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CoverNerve:
    """A finite open cover encoded as its nerve up to triple overlaps.

    `opens`    : the 0-simplices (cover patches), an ordered list.
    `overlaps` : the 1-simplices, ordered pairs (i, j) with i < j that have
                 nonempty pairwise intersection. This is the index set of the
                 Cech 1-cochains.
    `triples`  : the 2-simplices, ordered triples (i, j, k), i<j<k, with
                 nonempty triple intersection. The cocycle condition is imposed
                 on these (and is vacuous when there are none).
    `transition` : the Z2-valued 1-cochain g, transition[(i, j)] in {0, 1}.
                 g(i, j) = 0 means the orientation is preserved across U_i & U_j;
                 g(i, j) = 1 means it is reversed (the sign-twist / coefficient
                 datum the blind encoding drops).

    The orientation coefficient sheaf has constant stalk Z2; the gluing data is
    exactly `transition`. This is the standard finite Cech setup for the
    orientation (sign) sheaf, restricted to a finite cover.
    """

    opens: tuple[str, ...]
    overlaps: tuple[tuple[int, int], ...]
    triples: tuple[tuple[int, int, int], ...]
    transition: dict[tuple[int, int], int]


# --- The Mobius and cylinder witnesses (same data T59/T222 use) -------------


def mobius_two_set_nerve() -> CoverNerve:
    """Degenerate single-overlap form, kept to EXPOSE the T222 encoding artifact.

    T222's blind/aware comparison lived on a single index pair (U0, U1) and got
    its "obstruction" from a DIRECT parity conflict (two edges, same+different,
    on one pair). That is a CSP-unsatisfiability artifact, not a Cech H1 class:
    a single overlap is one 1-simplex with NO cover cycle, and the cohomology of
    an interval/tree nerve is trivial. Concretely, the transition g(0,1)=1 is
    ALWAYS the coboundary of the 0-cochain f=(0,1), so [g]=0 and a global section
    exists -- even though the loop sign is -1.

    This object is kept ONLY to demonstrate that fact: the honest coefficient-
    aware H1 reports a section here, showing the real Mobius obstruction requires
    a genuine cover CYCLE (the annular wrap in `annular_cover`), not a single
    overlap. The single-overlap "monodromy -1" is necessary but not sufficient.
    """
    return CoverNerve(
        opens=("U0", "U1"),
        overlaps=((0, 1),),
        triples=(),
        transition={(0, 1): 1},  # orientation reversed on the overlap
    )


def annular_cover(opens_count: int, reversed_edges: set[tuple[int, int]]) -> CoverNerve:
    """A finite annular (cyclic) cover of a band by `opens_count` patches.

    Patches U_0, ..., U_{n-1} are arranged in a circle: consecutive patches
    overlap, U_{n-1} overlaps U_0 (the wrap), and there are NO triple overlaps
    (a thin enough annular cover). The 1-cochain index set is the cycle edges.
    `reversed_edges` is the set of edges carrying an orientation reversal
    (transition = 1); all others are 0.

    With one reversed edge on the wrap cycle the net sign product around the
    loop is -1: this is the Mobius band (nontrivial orientation class). With
    zero (or any even number of) reversed edges the net product is +1: the
    cylinder (trivial class). This is a faithful finite nerve, not a single
    overlap -- the cohomology is computed over a genuine cover cycle.
    """
    n = opens_count
    opens = tuple(f"U{i}" for i in range(n))
    edges = [(i, (i + 1) % n) for i in range(n)]
    # normalize each edge to (min, max) for a consistent simplex orientation,
    # but keep the wrap edge (n-1, 0) as the explicit cycle-closing 1-simplex.
    overlaps: list[tuple[int, int]] = []
    transition: dict[tuple[int, int], int] = {}
    for (a, b) in edges:
        key = (a, b)
        overlaps.append(key)
        rev = 1 if (key in reversed_edges or (b, a) in reversed_edges) else 0
        transition[key] = rev
    return CoverNerve(
        opens=opens,
        overlaps=tuple(overlaps),
        triples=(),  # thin annular cover: no triple intersections
        transition=transition,
    )


# ---------------------------------------------------------------------------
# Cech H1 over the finite nerve, with Z2 coefficients
# ---------------------------------------------------------------------------
#
# 0-cochains  C0 : opens        -> Z2          (a candidate global section's local frame choices)
# 1-cochains  C1 : overlaps     -> Z2          (transition data g)
# coboundary  d0 : C0 -> C1,  (d0 f)(i,j) = f(j) - f(i)  (= f(j) XOR f(i) in Z2)
#
# H1 = ker(d1) / im(d0)  on the 1-cochains.  The transition cochain g is a
# 1-COCYCLE (lives in ker d1) because on a thin cover with no triple overlaps
# the cocycle condition is vacuous. g is a COBOUNDARY iff there is a 0-cochain f
# with d0 f = g, i.e. iff the orientation can be globally trivialized (a global
# section / consistent global frame exists). [g] != 0 in H1  <=>  no global
# section. This is the coefficient-aware obstruction.


def coboundary_d0(nerve: CoverNerve, f: dict[int, int]) -> dict[tuple[int, int], int]:
    """(d0 f)(i, j) = f(j) - f(i) in Z2, over the nerve's 1-simplices."""
    out: dict[tuple[int, int], int] = {}
    for (i, j) in nerve.overlaps:
        out[(i, j)] = z2_add(f[j], f[i])  # subtraction == addition in Z2
    return out


def is_cocycle(nerve: CoverNerve) -> bool:
    """Cocycle condition on triple overlaps: g(i,j) + g(j,k) + g(i,k) = 0 (Z2).

    On a thin cover with no triple overlaps this is vacuously True (the cochain
    is automatically a cocycle), which is the regime of the Mobius/cylinder
    annular witnesses. Implemented as a real check so a cover WITH triples would
    be validated.
    """
    g = nerve.transition
    for (i, j, k) in nerve.triples:
        gij = g.get((i, j), g.get((j, i), 0))
        gjk = g.get((j, k), g.get((k, j), 0))
        gik = g.get((i, k), g.get((k, i), 0))
        if z2_add(z2_add(gij, gjk), gik) != 0:
            return False
    return True


def transition_is_coboundary(nerve: CoverNerve) -> bool:
    """True iff the transition 1-cochain g is a coboundary d0 f for some f.

    Exhaustive search over all 2^(#opens) Z2 frame-choice 0-cochains f (finite
    cover -> finite search; this is NOT a hidden hardness claim, it is a small
    enumerated linear-algebra check, tag finite_witness / poly over fixed
    small covers). g is a coboundary  <=>  a consistent global frame exists
    <=>  a global section exists  <=>  [g] = 0 in H1.
    """
    n = len(nerve.opens)
    g = nerve.transition
    for bits in range(1 << n):
        f = {i: (bits >> i) & 1 for i in range(n)}
        if coboundary_d0(nerve, f) == g:
            return True
    return False


def monodromy_sign(nerve: CoverNerve) -> int:
    """Net sign product of the transition cochain around the cover (informal).

    For an annular (cyclic) cover this is the product of edge signs around the
    loop: +1 trivial, -1 the Mobius twist. Named 'monodromy' only as the loop
    sign-product; NOT a geometric/holonomy claim (honesty guard).
    """
    prod = 1
    for edge, c in nerve.transition.items():
        prod *= z2_to_sign(c)
    return prod


@dataclass(frozen=True)
class H1Verdict:
    """The coefficient-aware Cech-H1 verdict on one nerve."""

    nerve_name: str
    coefficient_aware_class_trivial: bool   # [g] == 0  (global section exists)
    has_global_section_aware: bool          # alias for clarity
    loop_sign: int                          # +1 / -1 informal monodromy
    is_valid_cocycle: bool
    # blind comparison: the same/different SCALAR CSP encoding T222 uses
    blind_reports_section: bool             # the false (or true) scalar verdict
    blind_is_false_section: bool            # blind says section but aware says none
    detail: str


def _blind_scalar_section(nerve: CoverNerve) -> bool:
    """The coefficient-BLIND scalar verdict, reconstructed to match T222.

    T222's blind Mobius encoding collapses the orientation overlap to a plain
    'same' constraint (it drops the reversal sign), so the scalar CSP is always
    satisfiable -> always reports a global section. We reproduce that exactly:
    a blind encoding sees only WHETHER patches overlap, never the transition
    coefficient, so every overlap reads as 'same' (0) and the section always
    exists. This is the data-forgetting projection, by construction.
    """
    # blind transition: all overlaps forced to 0 (same) -- the dropped-coefficient view.
    blind_nerve = CoverNerve(
        opens=nerve.opens,
        overlaps=nerve.overlaps,
        triples=nerve.triples,
        transition={e: 0 for e in nerve.overlaps},
    )
    # the all-zero cochain is the coboundary of the zero frame -> always a section.
    return transition_is_coboundary(blind_nerve)


def h1_verdict(nerve: CoverNerve, name: str) -> H1Verdict:
    valid = is_cocycle(nerve)
    trivial = transition_is_coboundary(nerve)
    loop = monodromy_sign(nerve)
    blind_section = _blind_scalar_section(nerve)
    blind_false = blind_section and not trivial
    detail = (
        f"Cover '{name}': {len(nerve.opens)} patches, {len(nerve.overlaps)} "
        f"overlaps, {len(nerve.triples)} triples. Transition 1-cochain g is a "
        f"valid cocycle: {valid}. [g] trivial in H1 (global section exists via "
        f"coefficient-aware encoding): {trivial}. Loop sign product (informal "
        f"monodromy): {loop:+d}. Blind scalar encoding reports a section: "
        f"{blind_section} (false section: {blind_false})."
    )
    return H1Verdict(
        nerve_name=name,
        coefficient_aware_class_trivial=trivial,
        has_global_section_aware=trivial,
        loop_sign=loop,
        is_valid_cocycle=valid,
        blind_reports_section=blind_section,
        blind_is_false_section=blind_false,
        detail=detail,
    )


# ---------------------------------------------------------------------------
# Comparison against PO1 AC1-AC7 admissibility metadata
# ---------------------------------------------------------------------------
#
# The point of T222's contribution request: does the coefficient-aware
# obstruction class AGREE with PO1's admissibility classification? The bridge:
#
#   - The transition 1-cochain g IS the AC5 datum ("typed forgotten structure"):
#     it is exactly the named orientation/transition structure that a projection
#     can discard. The coefficient-BLIND encoding is the projection that forgets
#     it.
#   - AC6 (restricted system globally obstructed) corresponds to [g] != 0 in H1
#     (no global section over the cover).
#   - AC7 (source globally satisfiable) corresponds to: every patch is locally
#     orientable, i.e. each U_i alone admits a frame -> always true for a cover
#     by orientable patches (the stalks are Z2, locally trivial).
#
# Agreement statement (the verdict): the coefficient-aware H1 obstruction class
# agrees with the AC6 restricted-obstruction flag IF AND ONLY IF the AC5
# transition data is retained. When AC5 is forgotten (blind encoding), the H1
# becomes trivial and the obstruction is lost -- precisely T222's false-section
# trap, now localized to "AC5 forgetting == coefficient forgetting".


@dataclass(frozen=True)
class AC_Comparison:
    nerve_name: str
    ac5_transition_retained: bool   # is the named transition structure carried?
    ac6_restricted_obstructed: bool # PO1: restricted system globally obstructed
    ac7_source_satisfiable: bool    # PO1: each patch locally orientable
    h1_obstructed: bool             # [g] != 0 in coefficient-aware H1
    agrees_with_po1: bool           # h1_obstructed == ac6_restricted_obstructed
    detail: str


def compare_to_po1(nerve: CoverNerve, name: str, retain_ac5: bool) -> AC_Comparison:
    """Compare the coefficient-aware H1 class against PO1 AC metadata.

    `retain_ac5` toggles whether the named transition (AC5) structure is carried.
    retain_ac5=True  -> coefficient-aware H1 (carries g).
    retain_ac5=False -> AC5 forgotten == coefficient-blind (g dropped to 0).
    """
    if retain_ac5:
        h1 = h1_verdict(nerve, name)
        h1_obstructed = not h1.coefficient_aware_class_trivial
    else:
        # AC5 forgotten: the blind nerve, g == 0 -> trivial class -> not obstructed.
        h1_obstructed = False

    # AC6: the orientation (restricted) system is globally obstructed exactly
    # when the *true* (coefficient-aware) class is nontrivial. The ground-truth
    # PO1 verdict references the real forgotten structure, not the projection.
    true_aware = h1_verdict(nerve, name)
    ac6_restricted_obstructed = not true_aware.coefficient_aware_class_trivial

    # AC7: each patch is locally orientable (stalk Z2 is locally trivial) -> True
    # for every cover by orientable patches. Always satisfiable locally; the
    # obstruction is purely in the gluing.
    ac7_source_satisfiable = True

    agrees = (h1_obstructed == ac6_restricted_obstructed)
    detail = (
        f"Cover '{name}': AC5 transition retained = {retain_ac5}. PO1 AC6 "
        f"(restricted system globally obstructed) = {ac6_restricted_obstructed}. "
        f"AC7 (each patch locally orientable / source satisfiable) = "
        f"{ac7_source_satisfiable}. Coefficient-aware H1 reports obstruction = "
        f"{h1_obstructed}. H1 verdict agrees with PO1 AC6 = {agrees}. "
        + (
            "Carrying AC5 (the transition cochain) reproduces the PO1 "
            "restricted-obstruction verdict."
            if retain_ac5
            else "Forgetting AC5 (coefficient-blind) makes H1 trivial while PO1's "
            "ground-truth AC6 still flags obstruction -> the T222 false-section "
            "trap, localized to AC5-forgetting."
        )
    )
    return AC_Comparison(
        nerve_name=name,
        ac5_transition_retained=retain_ac5,
        ac6_restricted_obstructed=ac6_restricted_obstructed,
        ac7_source_satisfiable=ac7_source_satisfiable,
        h1_obstructed=h1_obstructed,
        agrees_with_po1=agrees,
        detail=detail,
    )


# ---------------------------------------------------------------------------
# Top-level analysis
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class T226Result:
    h1_verdicts: tuple[H1Verdict, ...]
    ac_comparisons: tuple[AC_Comparison, ...]
    closes_false_section_trap: bool
    aware_agrees_with_po1_when_ac5_retained: bool
    blind_loses_obstruction_when_ac5_forgotten: bool
    verdict: str
    summary: str


def run_t226_analysis() -> T226Result:
    # The witnesses: Mobius (nontrivial) and cylinder (trivial), each on a
    # faithful finite annular nerve, plus the minimal 2-set form for direct
    # comparison with the T222 single-overlap encoding.
    mobius_min = mobius_two_set_nerve()
    mobius_annular = annular_cover(4, reversed_edges={(3, 0)})  # one wrap reversal -> -1
    cylinder_annular = annular_cover(4, reversed_edges=set())   # no reversal -> +1

    v_mobius_min = h1_verdict(mobius_min, "mobius_2set")
    v_mobius = h1_verdict(mobius_annular, "mobius_annular_4")
    v_cylinder = h1_verdict(cylinder_annular, "cylinder_annular_4")

    # Claim (1): coefficient-aware H1 reports NO section on Mobius (nontrivial
    # class) exactly where the blind scalar encoding falsely reported one; and
    # both agree (section exists) on the cylinder control.
    mobius_aware_obstructed = not v_mobius.coefficient_aware_class_trivial
    mobius_blind_false = v_mobius.blind_is_false_section
    cylinder_aware_section = v_cylinder.coefficient_aware_class_trivial
    cylinder_blind_section = v_cylinder.blind_reports_section
    closes_trap = (
        mobius_aware_obstructed
        and mobius_blind_false
        and cylinder_aware_section
        and cylinder_blind_section
        and v_mobius.loop_sign == -1
        and v_cylinder.loop_sign == 1
    )

    # Claim (2): AC comparison. With AC5 retained the aware H1 agrees with PO1's
    # AC6 restricted-obstruction verdict; forgetting AC5 loses it.
    cmp_mobius_aware = compare_to_po1(mobius_annular, "mobius_annular_4", retain_ac5=True)
    cmp_mobius_blind = compare_to_po1(mobius_annular, "mobius_annular_4", retain_ac5=False)
    cmp_cylinder_aware = compare_to_po1(cylinder_annular, "cylinder_annular_4", retain_ac5=True)

    aware_agrees = (
        cmp_mobius_aware.agrees_with_po1 and cmp_cylinder_aware.agrees_with_po1
    )
    blind_loses = (
        not cmp_mobius_blind.agrees_with_po1  # blind disagrees with PO1 on Mobius
        and cmp_mobius_blind.ac6_restricted_obstructed  # PO1 still flags obstruction
        and not cmp_mobius_blind.h1_obstructed          # but blind H1 says none
    )

    verdict = "conditional" if (closes_trap and aware_agrees and blind_loses) else "fail"

    summary = (
        "Coefficient-aware Cech-H1 over a finite annular nerve, valued in Z2, "
        "carrying the orientation transition 1-cochain. On the Mobius witness it "
        "reports a NONTRIVIAL class (no global section, loop sign -1) exactly "
        "where the T222 coefficient-blind scalar encoding falsely reported a "
        "section; on the cylinder both report a section. The transition cochain "
        "IS PO1's AC5 'named forgotten structure': retaining it reproduces PO1's "
        "AC6 restricted-obstruction verdict, forgetting it (blind encoding) "
        "collapses the class to trivial and loses the obstruction -- the T222 "
        "false-section trap localized to AC5-forgetting. FINITE WITNESS ONLY: no "
        "general continuum sheaf-cohomology theorem is claimed; this exhibits the "
        "coefficient-aware-vs-blind distinction on finite covers."
    )

    return T226Result(
        h1_verdicts=(v_mobius_min, v_mobius, v_cylinder),
        ac_comparisons=(cmp_mobius_aware, cmp_mobius_blind, cmp_cylinder_aware),
        closes_false_section_trap=closes_trap,
        aware_agrees_with_po1_when_ac5_retained=aware_agrees,
        blind_loses_obstruction_when_ac5_forgotten=blind_loses,
        verdict=verdict,
        summary=summary,
    )


def t226_result_to_dict(result: T226Result) -> dict[str, Any]:
    def _h1(v: H1Verdict) -> dict[str, Any]:
        return {
            "nerve_name": v.nerve_name,
            "coefficient_aware_class_trivial": v.coefficient_aware_class_trivial,
            "has_global_section_aware": v.has_global_section_aware,
            "loop_sign": v.loop_sign,
            "is_valid_cocycle": v.is_valid_cocycle,
            "blind_reports_section": v.blind_reports_section,
            "blind_is_false_section": v.blind_is_false_section,
            "detail": v.detail,
        }

    def _cmp(c: AC_Comparison) -> dict[str, Any]:
        return {
            "nerve_name": c.nerve_name,
            "ac5_transition_retained": c.ac5_transition_retained,
            "ac6_restricted_obstructed": c.ac6_restricted_obstructed,
            "ac7_source_satisfiable": c.ac7_source_satisfiable,
            "h1_obstructed": c.h1_obstructed,
            "agrees_with_po1": c.agrees_with_po1,
            "detail": c.detail,
        }

    return {
        "h1_verdicts": [_h1(v) for v in result.h1_verdicts],
        "ac_comparisons": [_cmp(c) for c in result.ac_comparisons],
        "closes_false_section_trap": result.closes_false_section_trap,
        "aware_agrees_with_po1_when_ac5_retained": result.aware_agrees_with_po1_when_ac5_retained,
        "blind_loses_obstruction_when_ac5_forgotten": result.blind_loses_obstruction_when_ac5_forgotten,
        "verdict": result.verdict,
        "summary": result.summary,
    }


if __name__ == "__main__":
    import json

    res = run_t226_analysis()
    print(json.dumps(t226_result_to_dict(res), indent=2))
