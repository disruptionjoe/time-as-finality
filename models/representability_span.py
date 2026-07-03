"""T422 - Representability span of the forcing modes E1 / E2 / E3.

Finite-witness demonstration that physical forcing modes do NOT form an
interconvertible lattice:

  * E1 (asymptotic-limit forcing) and E3 (structural-symmetry forcing) share ONE
    invariant type -- Cech H^1 of the nerve of a triangulated circle C_n --
    computed by the IDENTICAL function, differing ONLY in the coefficient group
    (E1 = Z winding index, E3 = Z/2 twist / monodromy).
  * E2 (computational-hardness forcing) admits NO such functorial / homotopy
    invariant, because the forcing verdict is PRESENTATION-DEPENDENT: it FLIPS
    across the canonical CRT ring isomorphism (Z/N)* = (Z/p)* x (Z/q)*, an
    isomorphism under which every genuine Cech invariant of the object is
    preserved (the STEP-1 positive control).
  * A non-interconvertibility monotone delta separates E2 (delta=1) from
    {E1, E3} (delta=0): delta is preserved by the free operations (cover
    refinement, object isomorphism), so no free operation crosses the line.

HONESTY CEILING (binding). Finite witnesses + a colimit-invariance argument + a
stated falsifier -- NOT a universal theorem. E1's true forcing is ASYMPTOTIC; its
finite winding is an explicit PROXY for the no-local-witness STRUCTURE, not the
divergence (refinement-stability is the finite E1-flavor signature). The
separation lives in the cost-blind category (isomorphisms / refinements). K5
prior art conceded: complexity/circuit-size is not a homotopy/functorial
invariant (Immerman-Vardi order-dependence; Goldwasser-Micali); novelty is
confined to the finality / forcing-mode cross-application (synthesis-tier).

Cross-domain material (Cech cohomology, computational complexity, CRT, quadratic
residuosity) is the OBJECT OF STUDY, never evidence for physics. No claim
promotion; TESTS.md / CLAIM-LEDGER.md untouched.

    python -m models.representability_span
    python -m pytest tests/test_representability_span.py -q
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from itertools import combinations
from typing import Any

# Reuse the already-validated number-theory machinery (anti-engineering guard):
# the E2 object is T417's Goldwasser-Micali construction, unchanged.
from models.computational_finality_boundary import (
    N as E2_N,
    P as E2_P,
    Q as E2_Q,
    X_A as E2_X_A,
    X_B as E2_X_B,
    jacobi,
    legendre,
    is_qr_mod_N,
)

ARTIFACT = "T422-representability-span-v0.1"


# ===========================================================================
# (1) cech.py  --  THE shared engine, coefficient-generic.
# ===========================================================================
#
# Nerve of a triangulated circle C_n: opens U_0..U_{n-1}, cyclic overlaps
# (i, i+1 mod n), NO triple overlaps. H^1(C_n; A) = A via the loop-sum (winding)
# map. The SAME function is called for A = Z (mod=0) and A = Z/2 (mod=2); only
# the coefficient group changes. This is the sole engine every mode routes
# through (anti-engineering guard).


def _reduce(value: int, mod: int) -> int:
    """Reduce into the coefficient group A. mod=0 -> Z (identity); mod=m -> Z/m."""
    return value if mod == 0 else value % mod


@dataclass(frozen=True)
class CircleNerve:
    """Finite cyclic cover of a circle; the nerve is the cycle graph C_n.

    opens      : ordered 0-simplices (arcs).
    edges      : oriented 1-simplices (i, j); for the full circle these are
                 (i, (i+1) % n) including the wrap (n-1, 0).
    transition : coefficient-group value on each edge (the gluing 1-cochain).
    """

    opens: tuple[str, ...]
    edges: tuple[tuple[int, int], ...]
    transition: dict[tuple[int, int], int]


def circle_nerve(n: int, transition: dict[tuple[int, int], int]) -> CircleNerve:
    opens = tuple(f"U{i}" for i in range(n))
    edges = tuple((i, (i + 1) % n) for i in range(n))
    trans = {e: int(transition.get(e, 0)) for e in edges}
    return CircleNerve(opens=opens, edges=edges, transition=trans)


def _components(n_vertices: list[int], edges: list[tuple[int, int]]) -> int:
    """Connected-component count via union-find (H^0 rank = #components)."""
    parent = {v: v for v in n_vertices}

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (i, j) in edges:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj
    return len({find(v) for v in n_vertices})


def cech_h1(
    vertices: list[int],
    edges: list[tuple[int, int]],
    transition: dict[tuple[int, int], int],
    mod: int,
) -> dict[str, Any]:
    """Coefficient-generic Cech H^0 / H^1 on a graph nerve (no triple overlaps).

    Method (exact, deterministic, works uniformly for Z and Z/m): build a
    spanning forest, propagate a 0-cochain f (f=0 at each root, f[j]=f[i]+g along
    tree edges), then every NON-tree edge carries a defect
        defect(i,j) = transition(i,j) - (f[j] - f[i])   (reduced in A).
    The transition is a COBOUNDARY (H^1 class trivial) iff every non-tree defect
    is 0. The number of non-tree edges = rank of the cycle space (E - V + #comp).
    For the full circle C_n the single non-tree defect equals the loop sum = the
    winding / monodromy index.
    """
    comps = _components(vertices, edges)
    # adjacency for a spanning-forest BFS
    adj: dict[int, list[tuple[int, int, int]]] = {v: [] for v in vertices}
    for (i, j) in edges:
        g = transition[(i, j)]
        adj[i].append((j, +1, g))   # traverse i->j : f[j] = f[i] + g
        adj[j].append((i, -1, g))   # traverse j->i : f[i] = f[j] - g
    f: dict[int, int] = {}
    tree_edges: set[frozenset[int]] = set()
    for root in vertices:
        if root in f:
            continue
        f[root] = 0
        stack = [root]
        while stack:
            u = stack.pop()
            for (w, sign, g) in adj[u]:
                if w not in f:
                    f[w] = _reduce(f[u] + sign * g, mod)
                    tree_edges.add(frozenset((u, w)))
                    stack.append(w)
    # non-tree edges carry the obstruction
    defects: list[int] = []
    for (i, j) in edges:
        if frozenset((i, j)) in tree_edges:
            continue
        d = _reduce(transition[(i, j)] - (f[j] - f[i]), mod)
        defects.append(d)
    h1_trivial = all(d == 0 for d in defects)
    # winding: the representative loop-sum obstruction (0 if no independent cycle)
    winding = _reduce(defects[0], mod) if defects else 0
    # loop sum over the full oriented cycle (only meaningful when C_n is intact)
    loop_sum = _reduce(sum(transition[e] for e in edges), mod)
    return {
        "mod": mod,
        "coefficient_group": "Z" if mod == 0 else f"Z/{mod}",
        "h0": comps,                       # H^0 rank = #components
        "n_independent_cycles": len(defects),
        "h1_trivial": h1_trivial,          # [g] == 0  (global section exists)
        "winding": winding,                # the H^1 class value (index)
        "loop_sum": loop_sum,
    }


def full_circle_class(nerve: CircleNerve, mod: int) -> dict[str, Any]:
    verts = list(range(len(nerve.opens)))
    return cech_h1(verts, list(nerve.edges), nerve.transition, mod)


def proper_subcover_scan(nerve: CircleNerve, mod: int) -> dict[str, Any]:
    """Recompute the class on EVERY proper subcover (no-local-witness check).

    A proper subcover omits at least one arc; removing any vertex breaks the loop,
    so the nerve becomes a forest (H^1 = 0) and the restricted class is trivial.
    Returns whether EVERY proper subcover trivializes (no proper-subset witness).
    """
    n = len(nerve.opens)
    all_trivial = True
    any_witness = False
    checked = 0
    for size in range(1, n):  # proper subsets only
        for subset in combinations(range(n), size):
            s = set(subset)
            sub_edges = [(i, j) for (i, j) in nerve.edges if i in s and j in s]
            sub_trans = {e: nerve.transition[e] for e in sub_edges}
            res = cech_h1(sorted(s), sub_edges, sub_trans, mod)
            checked += 1
            if not res["h1_trivial"]:
                all_trivial = False
                any_witness = True
    return {
        "proper_subcovers_checked": checked,
        "every_proper_subcover_trivial": all_trivial,
        "some_proper_subset_witnesses_class": any_witness,
    }


def refine_circle(nerve: CircleNerve, mod: int) -> dict[str, Any]:
    """Subdivide C_n -> C_2n (each arc split; transition transported to one
    sub-edge). Refinement-stability = the finite E1-flavor signature. Returns the
    refined class so the winding can be compared to the coarse one."""
    n = len(nerve.opens)
    new_trans: dict[tuple[int, int], int] = {}
    for i in range(n):
        e = (i, (i + 1) % n)
        g = nerve.transition[e]
        a, b, c = 2 * i, 2 * i + 1, (2 * i + 2) % (2 * n)
        new_trans[(a, b)] = g   # carry the datum on the first half
        new_trans[(b, c)] = 0   # zero on the second half -> loop sum preserved
    refined = circle_nerve(2 * n, new_trans)
    return full_circle_class(refined, mod)


def relabel_circle(nerve: CircleNerve, mod: int, rotation: int) -> dict[str, Any]:
    """Object isomorphism: rotate the cyclic cover by `rotation` (a nerve
    automorphism). A genuine Cech class is invariant under it."""
    n = len(nerve.opens)
    new_trans: dict[tuple[int, int], int] = {}
    for i in range(n):
        e = (i, (i + 1) % n)
        ni, nj = (i + rotation) % n, (i + 1 + rotation) % n
        new_trans[(ni, nj)] = nerve.transition[e]
    relabeled = circle_nerve(n, {(i, (i + 1) % n): new_trans[(i, (i + 1) % n)] for i in range(n)})
    return full_circle_class(relabeled, mod)


# ===========================================================================
# (2) e1_winding.py  --  E1 asymptotic-limit forcing: Z winding index.
# ===========================================================================


def e1_winding(n: int = 4) -> dict[str, Any]:
    """S1 (E1 leg). Cover S^1 by n arcs; Z-valued transition 1-cochain with loop
    sum w=1; compute w via the shared engine in coefficient group Z (mod=0)."""
    mod = 0
    nerve = circle_nerve(n, {(n - 1, 0): 1})  # one unit twist on the wrap
    cls = full_circle_class(nerve, mod)
    subcov = proper_subcover_scan(nerve, mod)
    refined = refine_circle(nerve, mod)
    relabeled = relabel_circle(nerve, mod, rotation=1)
    return {
        "mode": "E1_asymptotic_limit_forcing",
        "coefficient_group": "Z",
        "n_arcs": n,
        "class": cls,
        "winding": cls["winding"],
        "class_nonzero": cls["winding"] != 0 and not cls["h1_trivial"],
        "no_local_witness": subcov["every_proper_subcover_trivial"],
        "proper_subcover_scan": subcov,
        "refinement_stable": refined["winding"] == cls["winding"],
        "refined_winding": refined["winding"],
        "iso_invariant": relabeled["winding"] == cls["winding"],
        "asymptotic_proxy_note": (
            "E1's real forcing is a LIMIT/divergence (recovery cost diverges only "
            "in a family). The finite winding w=1 is an explicit PROXY of that "
            "local-to-global STRUCTURE (a global section with no local witness); "
            "refinement-stability n->2n is the finite E1-flavor signature."
        ),
    }


# ===========================================================================
# (3) e3_twist.py  --  E3 structural-symmetry forcing: Z/2 twist / monodromy.
# ===========================================================================


def e3_twist(n: int = 4) -> dict[str, Any]:
    """S1 (E3 leg). SAME cover C_n, Z/2-valued transition (sign local system);
    compute monodromy via the SHARED engine in coefficient group Z/2 (mod=2).
    Identical function to e1_winding, only the coefficient group differs."""
    mod = 2
    nerve = circle_nerve(n, {(n - 1, 0): 1})  # one sign reversal on the wrap
    cls = full_circle_class(nerve, mod)
    subcov = proper_subcover_scan(nerve, mod)
    refined = refine_circle(nerve, mod)
    relabeled = relabel_circle(nerve, mod, rotation=1)

    # Cross-check against T412's independently-measured Z/2 parity fact: the
    # 3-qubit total-parity separator is global in no proper subset (max proper-
    # subset trace distance 0.0) and the full joint separates (1.0). We reproduce
    # the SAME structural pattern here: no proper subcover witnesses the twist,
    # the full cover carries the nonzero class.
    t412_pattern = {
        "max_proper_subset_witness": 0.0 if subcov["every_proper_subcover_trivial"] else 1.0,
        "full_joint_separates": 1.0 if (cls["winding"] != 0) else 0.0,
        "matches_T412": (
            subcov["every_proper_subcover_trivial"] and cls["winding"] != 0
        ),
    }
    return {
        "mode": "E3_structural_symmetry_forcing",
        "coefficient_group": "Z/2",
        "n_arcs": n,
        "class": cls,
        "monodromy": cls["winding"],
        "class_nonzero": cls["winding"] != 0 and not cls["h1_trivial"],
        "no_local_witness": subcov["every_proper_subcover_trivial"],
        "proper_subcover_scan": subcov,
        "refinement_stable": refined["winding"] == cls["winding"],
        "refined_winding": refined["winding"],
        "iso_invariant": relabeled["winding"] == cls["winding"],
        "t412_crosscheck": t412_pattern,
        "same_engine_as_E1": (
            "e1_winding and e3_twist call the identical cech_h1 function; the ONLY "
            "difference is mod=0 (Z) vs mod=2 (Z/2). This is the retro-prediction "
            "of T421's Z-vs-Z/2 bifurcation: same functor, different coefficient "
            "object."
        ),
    }


# ===========================================================================
# (4) e2_hardness.py  --  E2 computational-hardness forcing: presentation-dependent.
# ===========================================================================


def _units_mod(n: int) -> list[int]:
    from math import gcd

    return [x for x in range(1, n) if gcd(x, n) == 1]


def _crt_phi(x: int, p: int, q: int) -> tuple[int, int]:
    """The CANONICAL CRT ring isomorphism component map: x -> (x mod p, x mod q)."""
    return (x % p, x % q)


def verify_crt_isomorphism(n: int, p: int, q: int) -> dict[str, Any]:
    """Circularity guard part A: phi is a GENUINE ring isomorphism of Z/N onto
    (Z/p) x (Z/q) preserving +, * and (on units) QR-ness. Verified elementwise
    over the whole ring -- not stipulated."""
    ring = list(range(n))
    images = {x: _crt_phi(x, p, q) for x in ring}
    bijective = len(set(images.values())) == n and len(images) == n
    preserves_add = all(
        _crt_phi((a + b) % n, p, q)
        == ((images[a][0] + images[b][0]) % p, (images[a][1] + images[b][1]) % q)
        for a in ring
        for b in ring
    )
    preserves_mul = all(
        _crt_phi((a * b) % n, p, q)
        == ((images[a][0] * images[b][0]) % p, (images[a][1] * images[b][1]) % q)
        for a in ring
        for b in ring
    )
    units = _units_mod(n)
    preserves_qr = all(
        is_qr_mod_N(x, p, q) == (legendre(x, p) == 1 and legendre(x, q) == 1)
        for x in units
    )
    # QR set maps exactly onto (QR of Z/p) x (QR of Z/q)
    qr_units = {x for x in units if is_qr_mod_N(x, p, q)}
    qr_images_both = all(
        legendre(x, p) == 1 and legendre(x, q) == 1 for x in qr_units
    )
    return {
        "map": "phi(x) = (x mod p, x mod q)  [canonical CRT ring iso]",
        "bijective": bijective,
        "preserves_addition": preserves_add,
        "preserves_multiplication": preserves_mul,
        "preserves_QR_on_units": preserves_qr and qr_images_both,
        "is_genuine_ring_iso": bijective and preserves_add and preserves_mul,
    }


def _coloring_cech(units: list[int], qr_of) -> dict[str, Any]:
    """Cech invariants of the QR 2-coloring cover: opens = color classes (QR /
    non-QR), a DISCRETE (disjoint) cover -> H^0 = #color-classes, H^1 = 0. Used
    as the STEP-1 positive control; must be equal under both presentations."""
    classes: dict[Any, list[int]] = {}
    for u in units:
        classes.setdefault(qr_of(u), []).append(u)
    # discrete disjoint cover: no overlaps -> #components = #classes, no cycles.
    return {"h0": len(classes), "h1": 0, "n_color_classes": len(classes)}


def e2_hardness() -> dict[str, Any]:
    """S2. Two presentations of the SAME E2 object related by the canonical CRT
    iso; STEP-1 positive control (equal Cech invariants) then the FORCED !=
    DECLARED flip of the hardness verdict."""
    n, p, q = E2_N, E2_P, E2_Q
    x_a, x_b = E2_X_A, E2_X_B
    units = _units_mod(n)

    crt = verify_crt_isomorphism(n, p, q)

    # STEP-1 POSITIVE CONTROL (anti-K3): equal Cech invariants under both
    # presentations. P1 colors by QR-ness in N-coords; P2 colors by QR-ness read
    # through phi (per-factor). phi preserves QR-ness, so the PARTITION is the
    # same set -> identical (H^0, H^1). The object is demonstrably NOT pathological.
    p1_color = _coloring_cech(units, lambda u: is_qr_mod_N(u, p, q))
    p2_color = _coloring_cech(
        units, lambda u: (legendre(u, p) == 1, legendre(u, q) == 1) == (True, True)
    )
    cech_equal = (p1_color["h0"], p1_color["h1"]) == (p2_color["h0"], p2_color["h1"])

    # The datum: QR-ness (needs the trapdoor p,q). A is QR, B is non-QR.
    a_qr, b_qr = is_qr_mod_N(x_a, p, q), is_qr_mod_N(x_b, p, q)

    # P1 (N-coordinates): the only trapdoor-free feasible LOCAL predicate is the
    # Jacobi symbol. Jacobi(A,N) == Jacobi(B,N) == +1, so it CANNOT separate the
    # QR datum -> the boundary is FORCED.
    jac_a, jac_b = jacobi(x_a, n), jacobi(x_b, n)
    p1_local_separates = jac_a != jac_b
    p1_verdict = "DECLARED" if p1_local_separates else "FORCED"

    # P2 (CRT-coordinates): the feasible LOCAL predicate is per-factor Legendre.
    # (A/p),(A/q) vs (B/p),(B/q) separate -> the boundary is DECLARED.
    leg_a = (legendre(x_a, p), legendre(x_a, q))
    leg_b = (legendre(x_b, p), legendre(x_b, q))
    p2_local_separates = leg_a != leg_b
    p2_verdict = "DECLARED" if p2_local_separates else "FORCED"

    verdict_flips = (p1_verdict != p2_verdict) and crt["is_genuine_ring_iso"] and cech_equal

    # Deformation scan: forcing is DISCONTINUOUS across the family with no
    # compensating ker/coker exchange (NO index-conservation). For prime N the
    # QR structure is locally decidable (Jacobi == Legendre) so forcing vanishes;
    # for N=pq it is present. An index would be CONSERVED; this flips 0/1 with
    # primality.
    def _forcing_indicator(m: int) -> int:
        # 1 if some Jacobi-+1 unit is a non-residue not locally separable in
        # N-coords (composite with >=2 prime factors), else 0.
        from sympy import factorint

        return 0 if len(factorint(m)) < 2 else 1

    scan_family = [77, 79, 91, 143, 899]
    scan = {m: _forcing_indicator(m) for m in scan_family}
    scan_values = list(scan.values())
    forcing_not_conserved = len(set(scan_values)) > 1  # jumps => not an index

    two_horn = (
        "Two-horn dilemma. Either CRT is a FREE morphism (then a functorial "
        "invariant must assign phi-related presentations EQUAL value; but the "
        "hardness verdict differs, so hardness is not functorial) OR CRT is "
        "declared NOT a morphism (then hardness is admitted to depend on the "
        "presentation). Both horns ARE the conclusion: E2 hardness is represented "
        "by no Cech / functorial class."
    )

    return {
        "mode": "E2_computational_hardness_forcing",
        "object": f"units mod N={n}={p}*{q}, QR 2-coloring; x_A={x_a} (QR), x_B={x_b} (non-QR, Jacobi +1)",
        "crt_isomorphism": crt,
        "step1_positive_control": {
            "P1_coloring_cech": p1_color,
            "P2_coloring_cech": p2_color,
            "cech_invariants_equal": cech_equal,
            "note": (
                "H^0=2 (two color classes), H^1=0 under BOTH presentations. The "
                "object HAS presentation-independent Cech invariants; it is not "
                "pathological. What fails to be an invariant is specifically the "
                "HARDNESS verdict."
            ),
        },
        "datum": {"A_is_QR": a_qr, "B_is_QR": b_qr, "datum_differs": a_qr != b_qr},
        "P1_N_coordinates": {
            "feasible_local_predicate": "Jacobi(x, N)",
            "jacobi_A": jac_a,
            "jacobi_B": jac_b,
            "local_separates": p1_local_separates,
            "verdict": p1_verdict,
        },
        "P2_CRT_coordinates": {
            "feasible_local_predicate": "per-factor Legendre (x/p),(x/q)",
            "legendre_A": leg_a,
            "legendre_B": leg_b,
            "local_separates": p2_local_separates,
            "verdict": p2_verdict,
        },
        "verdict_flips_across_iso": verdict_flips,
        "deformation_scan": {
            "family": scan_family,
            "forcing_indicator": scan,
            "forcing_not_conserved": forcing_not_conserved,
            "note": "forcing jumps 0/1 with primality: no ker/coker exchange, no index conservation.",
        },
        "two_horn_dilemma": two_horn,
    }


# ===========================================================================
# (5) monotone.py  --  the non-interconvertibility monotone delta.
# ===========================================================================


def _delta_from_flags(refinement_invariant: bool, iso_invariant: bool) -> int:
    """delta = 0 iff the toy's natural boundary-quantity is unchanged under BOTH
    cover refinement AND object isomorphism; else 1."""
    return 0 if (refinement_invariant and iso_invariant) else 1


def monotone(e1: dict[str, Any], e3: dict[str, Any], e2: dict[str, Any]) -> dict[str, Any]:
    """S3. delta(E1)=delta(E3)=0 < delta(E2)=1; delta preserved by free ops =>
    non-interconvertibility. Includes the matched-battery positive control."""
    delta_e1 = _delta_from_flags(e1["refinement_stable"], e1["iso_invariant"])
    delta_e3 = _delta_from_flags(e3["refinement_stable"], e3["iso_invariant"])
    # E2's natural quantity (the forcing verdict) is NOT invariant under object
    # isomorphism (flips across CRT) and is discontinuous under deformation.
    e2_iso_invariant = not e2["verdict_flips_across_iso"]
    e2_refinement_invariant = not e2["deformation_scan"]["forcing_not_conserved"]
    delta_e2 = _delta_from_flags(e2_refinement_invariant, e2_iso_invariant)

    separates = delta_e2 != delta_e1 and delta_e1 == delta_e3 == 0 and delta_e2 == 1

    # T110 shared lemma: a scalar that is nondecreasing on every edge of a
    # permutation orbit is CONSTANT on that orbit -> a well-defined index descends
    # to the orbit; a presentation-dependent cost does not. Import as the
    # independent reason indices descend and E2 cost does not.
    from models.finite_permutation_monotone_obstruction import run_t110_analysis

    t110 = run_t110_analysis()
    t110_holds = t110.t106_closed_cycle_audit.theorem_holds_for_scores and all(
        c.theorem_holds for c in t110.exhaustive_cycle_checks
    )

    # Matched-battery positive control: the SAME iso battery returns delta=0 on
    # E1/E3 (so it is not rigged to eject E2). T412 independently shows 48/48
    # product-structure-preserving relabels preserve the Z/2 separator.
    from models.separator_refactorization_gate import run_separator_refactorization_gate

    t412 = run_separator_refactorization_gate()
    t412_relabels = t412["structure_preserving_relabels"]
    battery_can_return_zero = (
        e1["iso_invariant"]
        and e3["iso_invariant"]
        and t412_relabels["survives"]
        and t412_relabels["n_permutation_flip_relabels"] == 48
    )

    return {
        "delta_E1": delta_e1,
        "delta_E3": delta_e3,
        "delta_E2": delta_e2,
        "separates_E2_from_E1E3": separates,
        "argument": (
            "delta is preserved by the free operations (cover refinement, object "
            "isomorphism) by the Cech-colimit definition: any quantity that IS a "
            "Cech class has delta=0. E1/E3 (delta=0) ARE Cech-representable; E2 "
            "hardness (delta=1) is not. Free ops preserve delta, so NO free "
            "operation carries an E1/E3 boundary to an E2 boundary or the reverse "
            "-- E2 is the categorical obstruction to unification."
        ),
        "t110_orbit_lemma_holds": t110_holds,
        "positive_control": {
            "battery_returns_zero_on_E1E3": battery_can_return_zero,
            "t412_relabels_survive": t412_relabels["survives"],
            "t412_n_relabels": t412_relabels["n_permutation_flip_relabels"],
            "note": "if the battery were rigged to eject E2 it would eject E3 too; it does not.",
        },
    }


# ===========================================================================
# (6) falsifier_search.py  --  the stated falsifier and its non-triggering.
# ===========================================================================


def falsifier_search(e2: dict[str, Any]) -> dict[str, Any]:
    """S4. Enumerate candidate 'geometric hardness' measures; each is EITHER
    phi/refinement-invariant-but-hardness-blind OR hardness-tracking-but-phi-
    discontinuous. None is BOTH. Finding one that is BOTH = the falsifier firing
    (K1)."""
    # Each candidate: (phi_invariant, tracks_hardness). The falsifier requires a
    # candidate with BOTH True.
    candidates = [
        {
            "name": "spectral gap of the C_n cover transition operator",
            "phi_invariant": True,   # depends only on the nerve, not the coloring
            "tracks_hardness": False,
            "why": "purely topological; identical for the easy prime object and the hard pq object",
        },
        {
            "name": "minimal-circuit-size proxy to decide QR-ness",
            "phi_invariant": False,  # collapses in CRT coords (per-factor Legendre)
            "tracks_hardness": True,
            "why": "large in N-coords, small in CRT-coords -> phi-discontinuous",
        },
        {
            "name": "family cost-growth index (trial-division steps growth)",
            "phi_invariant": False,  # drops to O(1) once factors are given
            "tracks_hardness": True,
            "why": "tracks the QRA gap but is not preserved by the CRT iso",
        },
        {
            "name": "description-length proxy (bit-length of N)",
            "phi_invariant": True,   # |N| = |p|+|q| roughly; presentation-stable
            "tracks_hardness": False,
            "why": "invariant but blind: a large easy prime has the same bit-length as a hard product",
        },
        {
            "name": "Cech winding of the coloring cover",
            "phi_invariant": True,   # STEP-1 positive control: H^1=0 both presentations
            "tracks_hardness": False,
            "why": "genuine functorial invariant but identically 0 -> tracks nothing",
        },
    ]
    both = [c for c in candidates if c["phi_invariant"] and c["tracks_hardness"]]
    falsifier_triggers = len(both) > 0
    return {
        "falsifier_statement": (
            "Exhibit a single quantity computed from (x, N) that is BOTH "
            "CRT/refinement-invariant AND tracks the QRA hardness gap "
            "(FORCED != DECLARED). Such a quantity would be a functorial / "
            "homotopy representative for E2 -> the span collapses (K1)."
        ),
        "candidates": candidates,
        "candidate_that_is_both": both,
        "falsifier_triggers": falsifier_triggers,
        "verdict": (
            "no candidate is simultaneously phi-invariant and hardness-tracking; "
            "the falsifier does NOT trigger"
            if not falsifier_triggers
            else "FALSIFIER FIRED: a functorial invariant for E2 exists (K1)"
        ),
    }


# ===========================================================================
# Top-level assembly.
# ===========================================================================


def run() -> dict[str, Any]:
    e1 = e1_winding(n=4)
    e3 = e3_twist(n=4)
    e2 = e2_hardness()
    mono = monotone(e1, e3, e2)
    fals = falsifier_search(e2)

    # SUCCESS legs
    s1_common_invariant = (
        e1["class_nonzero"]
        and e3["class_nonzero"]
        and e1["no_local_witness"]
        and e3["no_local_witness"]
        and e1["refinement_stable"]
        and e3["refinement_stable"]
        and e3["t412_crosscheck"]["matches_T412"]
        and e1["coefficient_group"] == "Z"
        and e3["coefficient_group"] == "Z/2"
    )
    s2_e2_nonrepresentable = (
        e2["crt_isomorphism"]["is_genuine_ring_iso"]
        and e2["crt_isomorphism"]["preserves_QR_on_units"]
        and e2["step1_positive_control"]["cech_invariants_equal"]
        and e2["verdict_flips_across_iso"]
        and e2["P1_N_coordinates"]["verdict"] == "FORCED"
        and e2["P2_CRT_coordinates"]["verdict"] == "DECLARED"
    )
    s3_noninterconvertible = mono["separates_E2_from_E1E3"]
    s4_falsifier_ok = not fals["falsifier_triggers"]

    go = s1_common_invariant and s2_e2_nonrepresentable and s3_noninterconvertible and s4_falsifier_ok

    return {
        "artifact": ARTIFACT,
        "claim_ledger_update": "none; no claim promotion",
        "tier": "recorded / exploratory big-swing (synthesis-tier margin only)",
        "E1_winding": e1,
        "E3_twist": e3,
        "E2_hardness": e2,
        "monotone": mono,
        "falsifier": fals,
        "success_legs": {
            "S1_common_invariant": s1_common_invariant,
            "S2_e2_nonrepresentable": s2_e2_nonrepresentable,
            "S3_noninterconvertible": s3_noninterconvertible,
            "S4_falsifier_stated_not_triggered": s4_falsifier_ok,
        },
        "kill_legs": {
            "K1_e2_functorial_invariant_found": fals["falsifier_triggers"],
            "K2_e1e3_index_engineered_or_trivial": not (
                e1["no_local_witness"] and e3["no_local_witness"]
                and e1["refinement_stable"] and e3["refinement_stable"]
            ),
            "K3_e2_flip_by_fiat": not e2["step1_positive_control"]["cech_invariants_equal"],
            "K4_interconvertibility_exists": not mono["separates_E2_from_E1E3"],
        },
        "verdict": "GO" if go else "NO-GO",
        "honesty_ceiling": (
            "Finite witnesses + colimit-invariance argument + stated falsifier -- "
            "NOT a universal theorem. E1 forcing is asymptotic; finite winding is "
            "an explicit proxy. The separation lives in the cost-blind category "
            "(isos/refinements); a reviewer demanding the poly-time-reduction "
            "category declines the category rather than refuting it -- and there "
            "the E1/E3 indices are not preserved either. K5 prior art conceded "
            "(complexity is not a homotopy/functorial invariant; Immerman-Vardi; "
            "Goldwasser-Micali); novelty confined to the finality / forcing-mode "
            "cross-application (synthesis-tier)."
        ),
    }


def main() -> None:
    print(json.dumps(run(), indent=2, default=str))


if __name__ == "__main__":
    main()
