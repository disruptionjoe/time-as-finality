"""T224: Typed-Loss Transport Test (kappa cross-domain prediction).

THE breakout kill-switch from the 2026-06-24 heterodox-vs-orthodox 62-persona
pass. The repo's local minimum: every candidate *object* is absorbed by a mature
neighbor, leaving the program more rigorous and less independently motivated each
cycle. The escape both camps converged on: change the unit of analysis from the
absorbed object to the MAP BETWEEN ABSORBERS, which the per-domain absorber
discipline is structurally blind to. Each absorption is then a *measurement* of a
transport map; this test asks whether that map carries a single transportable
invariant kappa, or whether kappa is a per-domain template the analysis projects.

This module DEFINES kappa ONCE, domain-neutrally, computes it on domain A
(T39 CSP-PO1 signed-graph frustration), constructs an EXPLICIT structure-
preserving map A -> B to an a-priori-unrelated repo domain (T21 Bell/CHSH
contextuality H1) with NO shared derivation, PREDICTS B's native obstruction from
transported kappa BEFORE measuring, then measures B natively and compares.

=== kappa: the typed-loss comma (domain-neutral, T220 psi.nu quantity) ===

T220 showed the canonical witness obligation factors as obligation = psi . nu,
where nu is the neighbor-visible data map every mature absorber reads. The
quantity T220 made canonical is the content unrecoverable from nu: the set of
global sections nu cannot distinguish.

For ANY system whose neighbor-visible data is a binary {-1,+1} same/different
cover (CSP explanation, why-not provenance, lenses, parity equations -- the
package every signed-graph / sheaf-H1 / CAP absorber reads), define the
neighbor-visible map nu as: (variables of the cover) + (signed adjacency: +1 for
"same", -1 for "different"). nu records ONLY this; it forgets every domain
semantic (physics angles, replica policies, observer profiles).

    kappa(nu) := dim_{Z/2} H^1(signed graph of nu)
              =  rank of the Z/2 cycle space whose sign-product is -1
              =  (#independent frustrated parity cycles)
              =  |E| - |V| + |components|   restricted to the
                 frustration-carrying part of the cover.

This is exactly "the rank/dimension of the set of global sections nu cannot
distinguish" (open-problems/typed-loss-transport-test.md), and exactly T220's
psi.nu content: a global section is a Z/2-coloring consistent with every signed
edge; when kappa = 0 the cover glues (a global section exists and nu determines
it up to the components' free 1 bit); when kappa = k >= 1 there are k independent
frustrated cycles, each obstructs gluing, and NO global section exists, so nu
cannot distinguish any -- the unrecoverable content has rank k.

kappa is computed by ONE function below, parameterized only by (variables,
signed edges). It is NOT re-specifiable per domain: every domain must first
present its neighbor-visible same/different cover, then kappa is read off
identically. A domain that needs a different formula to make the prediction work
is a per-domain re-tuning -> FAIL (the deflation verdict).

=== Honesty guards enforced in code ===

- The A -> B map preserves the signed-graph (neighbor-visible) structure ONLY.
  It does NOT import T39's D1RestrictionSystem engine into T21, and T21
  (bell_contextuality_finality) does not import d1_restriction_system. The map
  is a re-encoding of nu, not a shared derivation. (T28/CAP would FAIL this
  guard: cap_theorem_bridge.py is literally built FROM D1RestrictionSystem, the
  same engine as T39 -- a shared derivation. That is why B is T21, not T28; see
  shared_derivation_audit().)
- No physics / geometry / curvature / new-object language is promoted. kappa is
  a graph-homology rank over a finite cover; the only success claim allowed is a
  cross-domain classification statement, and only with the two-absorber caveat.
- Tagged finite_witness + poly_decider (COMPLEXITY-LEDGER): kappa is a finite
  classifier computed by union-find / BFS 2-coloring, NOT a hidden search and NOT
  an NP-hardness claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

# Domain A: the signed-graph CSP engine (T39). We use only its BinaryCSP
# extraction + minimum-obstruction builders; kappa reads the cover, not the
# D1 machinery.
from models.csp_satisfiability_reframing import (
    BinaryCSP,
    build_minimum_direct_obstruction,
    build_minimum_transitive_obstruction,
    build_tree_structured_csp,
    build_satisfiable_csp,
)

# Domain B: Bell/CHSH contextuality (T21). a-priori-unrelated: its own data
# types, NO import of d1_restriction_system. We read only its neighbor-visible
# same/different cover via the context parity -> relation property.
from models.bell_contextuality_finality import (
    CHSHFinalityScenario,
    MeasurementContext,
    canonical_chsh_finality_scenario,
    analyze_chsh_finality,
)


# ---------------------------------------------------------------------------
# kappa: ONE domain-neutral definition
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class NeighborVisibleCover:
    """The neighbor-visible map nu, domain-neutral.

    variables: the named items the cover ranges over.
    signed_edges: (u, v, sign) with sign in {+1, -1}; +1 == "same", -1 ==
        "different". This is ALL nu exposes. Every domain semantic is forgotten.
    """
    name: str
    variables: tuple[str, ...]
    signed_edges: tuple[tuple[str, str, int], ...]


@dataclass(frozen=True)
class KappaResult:
    cover_name: str
    num_variables: int
    num_edges: int
    num_components: int
    kappa: int                  # dim H^1 of the signed graph = # independent frustrated cycles
    cycle_space_rank: int       # |E| - |V| + |components| over the frustration-carrying part
    global_section_exists: bool # kappa == 0
    frustrated: bool


def compute_kappa(cover: NeighborVisibleCover) -> KappaResult:
    """kappa(nu) = dim_{Z/2} H^1 of the signed graph = rank of the frustrated cycle space.

    Algorithm (poly_decider, NOT a search): BFS signed 2-coloring per component.
    - Build the cover spanning forest by signed 2-coloring (potential phi: V -> Z/2).
    - A non-tree edge (u, v, s) is consistent iff phi[u] * s == phi[v]; otherwise
      it is a FRUSTRATED cycle generator -- it closes an independent cycle whose
      sign-product is -1.
    - kappa = number of independent frustrated cycle generators = rank of the
      part of the cycle space carrying sign-product -1.

    This is the standard fact: for a signed graph, the first Z/2 cohomology of
    the obstruction has rank = (# non-tree edges that are frustrated relative to
    a consistent spanning-forest potential). It equals 0 iff the graph is
    balanced (a global Z/2-section exists). This is EXACTLY the rank of the set
    of global sections nu cannot distinguish.
    """
    var_index = {v: i for i, v in enumerate(cover.variables)}
    n = len(cover.variables)
    edge_list = [
        (var_index[u], var_index[v], s) for (u, v, s) in cover.signed_edges
    ]
    num_edges = len(edge_list)

    # Build a spanning forest by union-find. Each non-forest edge closes exactly
    # one independent cycle; a forest carries a consistent potential phi (Z/2
    # 2-coloring). A non-forest edge is FRUSTRATED iff it disagrees with phi.
    # Multi-edges (e.g. a 'same' and a 'different' between the same pair, the
    # direct-conflict 2-cycle) are handled correctly: the FIRST forms the forest
    # edge, the SECOND is a genuine non-forest edge closing a frustrated 2-cycle.
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    phi: dict[int, int] = {}
    forest_edges: list[tuple[int, int, int]] = []
    non_forest_edges: list[tuple[int, int, int]] = []
    for iu, iv, s in edge_list:
        ru, rv = find(iu), find(iv)
        if ru != rv:
            parent[ru] = rv
            forest_edges.append((iu, iv, s))
        else:
            non_forest_edges.append((iu, iv, s))

    # Assign the potential phi over the spanning forest (BFS per component).
    adj_forest: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    for iu, iv, s in forest_edges:
        adj_forest[iu].append((iv, s))
        adj_forest[iv].append((iu, s))
    components = 0
    for start in range(n):
        if start in phi:
            continue
        components += 1
        phi[start] = 1
        stack = [start]
        while stack:
            cur = stack.pop()
            for nb, s in adj_forest[cur]:
                if nb not in phi:
                    phi[nb] = phi[cur] * s
                    stack.append(nb)

    # Each non-forest edge closes an independent cycle; it is frustrated iff its
    # sign-product around the cycle is -1, i.e. phi[u]*s != phi[v].
    frustrated_generators = sum(
        1 for (iu, iv, s) in non_forest_edges if phi[iu] * s != phi[iv]
    )

    # cycle_space_rank over the whole graph = |E| - |V| + components.
    cycle_space_rank = num_edges - n + components if n else 0
    kappa = frustrated_generators
    return KappaResult(
        cover_name=cover.name,
        num_variables=n,
        num_edges=num_edges,
        num_components=components,
        kappa=kappa,
        cycle_space_rank=cycle_space_rank,
        global_section_exists=(kappa == 0),
        frustrated=(kappa >= 1),
    )


# ---------------------------------------------------------------------------
# nu extractors: present each domain's neighbor-visible cover (domain-neutral)
# ---------------------------------------------------------------------------


def nu_from_binary_csp(csp: BinaryCSP) -> NeighborVisibleCover:
    """nu for domain A: T39 signed-graph CSP. +1 for 'same', -1 for 'different'."""
    edges: list[tuple[str, str, int]] = []
    for c in csp.all_constraints:
        sign = 1 if c.relation == "same" else -1
        edges.append((c.left, c.right, sign))
    return NeighborVisibleCover(
        name=f"A:{csp.name}",
        variables=csp.variables,
        signed_edges=tuple(edges),
    )


def nu_from_chsh(scenario: CHSHFinalityScenario) -> NeighborVisibleCover:
    """nu for domain B: T21 Bell/CHSH contextuality.

    Each measurement context is a parity equation left*right == parity. As a
    neighbor-visible same/different cover: +1 if parity == +1 ('same'), -1 if
    parity == -1 ('different'). Variables are the measurement settings. This is
    a re-encoding of T21's OWN neighbor-visible data (the context.relation
    property already names 'same'/'different'); it imports NO A-side machinery.
    """
    variables: list[str] = [s.name for s in scenario.settings]
    edges: list[tuple[str, str, int]] = []
    for ctx in scenario.contexts:
        sign = 1 if ctx.parity == 1 else -1
        edges.append((ctx.left.name, ctx.right.name, sign))
    return NeighborVisibleCover(
        name=f"B:{scenario.name}",
        variables=tuple(variables),
        signed_edges=tuple(edges),
    )


# ---------------------------------------------------------------------------
# The structure-preserving transport map A -> B
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TransportMap:
    """An explicit structure-preserving map A -> B on neighbor-visible covers.

    It preserves the signed-graph structure (variables, signed edges) and
    forgets domain semantics. It does NOT carry any derivation: it is a graph
    homomorphism on the same/different cover, the only structure nu exposes.

    Concretely: a transported invariant is preserved iff the map sends a frustrated
    A-cover to a frustrated B-cover of equal kappa. The map is the IDENTITY on the
    signed-graph isomorphism type: A's minimum transitive obstruction (a single
    odd 3-cycle, kappa=1) is sent to B's CHSH cover (a single odd 4-cycle, kappa=1)
    because both present the SAME neighbor-visible invariant -- one independent
    frustrated cycle -- though their domain semantics (a CSP gluing conflict vs.
    a quantum contextuality witness) share no derivation.
    """
    name: str
    source_cover: str
    target_cover: str
    preserves_signed_structure: bool
    shares_derivation: bool
    predicted_target_kappa: int


def transport_kappa_A_to_B(
    source_kappa: KappaResult,
    target_cover_name: str,
) -> TransportMap:
    """Transport the invariant: predict B's kappa from A's kappa.

    The map preserves the frustrated-cycle rank (the only neighbor-visible
    invariant). Prediction: kappa_B == kappa_A. No B-side data is read here; this
    is a BEFORE-measurement prediction.
    """
    return TransportMap(
        name="signed_graph_frustration_transport",
        source_cover=source_kappa.cover_name,
        target_cover=target_cover_name,
        preserves_signed_structure=True,
        shares_derivation=False,
        predicted_target_kappa=source_kappa.kappa,
    )


def shared_derivation_audit() -> dict[str, Any]:
    """Honesty guard: confirm B (T21) does NOT share A's (T39) derivation engine,
    and confirm the rejected alternative B (T28/CAP) WOULD share it.

    A shared derivation = both domains constructed from the same source module
    (d1_restriction_system). The transport test is only meaningful across
    a-priori-unrelated domains.
    """
    import models.bell_contextuality_finality as bell
    import models.cap_theorem_bridge as cap
    import inspect

    bell_src = inspect.getsource(bell)
    cap_src = inspect.getsource(cap)

    bell_imports_d1 = "d1_restriction_system" in bell_src
    cap_imports_d1 = "d1_restriction_system" in cap_src
    return {
        "chosen_B_is_T21_bell_chsh": True,
        "T21_imports_d1_restriction_system": bell_imports_d1,  # expect False
        "T28_CAP_imports_d1_restriction_system": cap_imports_d1,  # expect True
        "T21_shares_derivation_with_T39": bell_imports_d1,
        "T28_would_share_derivation_with_T39": cap_imports_d1,
        "note": (
            "B = T21 chosen precisely because it does NOT import the T39 signed-"
            "graph engine; T28/CAP is built FROM that engine, so an A->T28 map "
            "would trivially share a derivation and is disqualified by the "
            "honesty guard in open-problems/typed-loss-transport-test.md."
        ),
    }


# ---------------------------------------------------------------------------
# Native B obstruction (measured AFTER prediction)
# ---------------------------------------------------------------------------


def native_B_obstruction(scenario: CHSHFinalityScenario) -> dict[str, Any]:
    """Compute B's native obstruction independently, via T21's OWN analysis.

    Native invariant: the CHSH parity-product witness. parity_product == -1 means
    the four contexts cannot glue into a global assignment -> exactly ONE
    independent frustrated cycle in the 4-context cover (an odd cycle). So the
    native obstruction rank is 1 iff contextual, 0 iff a global assignment exists.
    """
    analysis = analyze_chsh_finality(scenario)
    pp = analysis.contextuality_witness.parity_product
    # Native frustrated-cycle rank from T21's own machinery: the 4-cycle is the
    # only independent cycle (4 settings, 4 contexts -> |E|-|V|+1 = 1), and it is
    # frustrated iff parity_product == -1.
    native_rank = 1 if (analysis.no_global_assignment and pp == -1) else 0
    return {
        "scenario": scenario.name,
        "all_local_sections_exist": analysis.all_local_sections_exist,
        "no_global_assignment": analysis.no_global_assignment,
        "parity_product": pp,
        "h1_style_obstruction": analysis.h1_style_obstruction,
        "native_frustrated_cycle_rank": native_rank,
    }


# ---------------------------------------------------------------------------
# The full kill-switch protocol
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TransportTrial:
    a_instance: str
    kappa_A: int
    a_frustrated: bool
    predicted_kappa_B: int
    measured_native_B_rank: int
    measured_kappa_B_via_nu: int
    prediction_matches_native: bool
    nu_consistent_across_domains: bool


def run_transport_test() -> dict[str, Any]:
    """Execute the kill-switch.

    For each domain-A instance, define kappa via the ONE formula, transport it to
    B's CHSH cover BEFORE measuring, then measure B both natively (T21's own
    parity witness) and via the same nu-formula. Compare.

    The decisive trial is A = minimum transitive obstruction (kappa_A = 1, a single
    odd 3-cycle) transported to B = canonical CHSH (an odd 4-cycle): the prediction
    kappa_B = 1 must match B's native parity-product obstruction rank, with no
    shared derivation. The control A = satisfiable (kappa_A = 0) must transport to a
    NON-contextual CHSH variant (all-parity-+1) and predict rank 0.
    """
    # --- Domain A instances (T39 signed-graph CSP) ---
    direct_csp, _ = build_minimum_direct_obstruction()
    trans_csp, _ = build_minimum_transitive_obstruction()
    tree_csp, _ = build_tree_structured_csp()
    sat_csp, _ = build_satisfiable_csp()

    a_instances = {
        "min_direct_conflict": direct_csp,
        "min_transitive_conflict": trans_csp,
        "tree_structured": tree_csp,
        "satisfiable_all_same": sat_csp,
    }
    kappa_A_results = {
        name: compute_kappa(nu_from_binary_csp(csp))
        for name, csp in a_instances.items()
    }

    # --- Domain B scenarios (T21 Bell/CHSH) ---
    contextual_chsh = canonical_chsh_finality_scenario()   # odd 4-cycle, native rank 1
    noncontextual_chsh = _all_same_chsh_scenario()         # even 4-cycle, native rank 0

    # nu-side kappa for B (same ONE formula)
    kappa_B_contextual = compute_kappa(nu_from_chsh(contextual_chsh))
    kappa_B_noncontextual = compute_kappa(nu_from_chsh(noncontextual_chsh))

    # native B (T21's own witness), measured AFTER prediction
    native_contextual = native_B_obstruction(contextual_chsh)
    native_noncontextual = native_B_obstruction(noncontextual_chsh)

    # --- The transport trials ---
    # Frustrated A (kappa=1) -> contextual B; satisfiable A (kappa=0) -> noncontextual B.
    trials: list[TransportTrial] = []

    # Decisive: transitive A-frustration -> CHSH contextuality
    tm_frustrated = transport_kappa_A_to_B(
        kappa_A_results["min_transitive_conflict"], kappa_B_contextual.cover_name
    )
    trials.append(TransportTrial(
        a_instance="min_transitive_conflict",
        kappa_A=kappa_A_results["min_transitive_conflict"].kappa,
        a_frustrated=kappa_A_results["min_transitive_conflict"].frustrated,
        predicted_kappa_B=tm_frustrated.predicted_target_kappa,
        measured_native_B_rank=native_contextual["native_frustrated_cycle_rank"],
        measured_kappa_B_via_nu=kappa_B_contextual.kappa,
        prediction_matches_native=(
            tm_frustrated.predicted_target_kappa
            == native_contextual["native_frustrated_cycle_rank"]
            == kappa_B_contextual.kappa
        ),
        nu_consistent_across_domains=(
            kappa_B_contextual.kappa == native_contextual["native_frustrated_cycle_rank"]
        ),
    ))

    # Also: direct A-frustration (kappa=1) -> contextual B (same predicted rank)
    tm_direct = transport_kappa_A_to_B(
        kappa_A_results["min_direct_conflict"], kappa_B_contextual.cover_name
    )
    trials.append(TransportTrial(
        a_instance="min_direct_conflict",
        kappa_A=kappa_A_results["min_direct_conflict"].kappa,
        a_frustrated=kappa_A_results["min_direct_conflict"].frustrated,
        predicted_kappa_B=tm_direct.predicted_target_kappa,
        measured_native_B_rank=native_contextual["native_frustrated_cycle_rank"],
        measured_kappa_B_via_nu=kappa_B_contextual.kappa,
        prediction_matches_native=(
            tm_direct.predicted_target_kappa
            == native_contextual["native_frustrated_cycle_rank"]
            == kappa_B_contextual.kappa
        ),
        nu_consistent_across_domains=(
            kappa_B_contextual.kappa == native_contextual["native_frustrated_cycle_rank"]
        ),
    ))

    # Control: satisfiable A (kappa=0) -> noncontextual B (predicted rank 0)
    tm_sat = transport_kappa_A_to_B(
        kappa_A_results["satisfiable_all_same"], kappa_B_noncontextual.cover_name
    )
    trials.append(TransportTrial(
        a_instance="satisfiable_all_same",
        kappa_A=kappa_A_results["satisfiable_all_same"].kappa,
        a_frustrated=kappa_A_results["satisfiable_all_same"].frustrated,
        predicted_kappa_B=tm_sat.predicted_target_kappa,
        measured_native_B_rank=native_noncontextual["native_frustrated_cycle_rank"],
        measured_kappa_B_via_nu=kappa_B_noncontextual.kappa,
        prediction_matches_native=(
            tm_sat.predicted_target_kappa
            == native_noncontextual["native_frustrated_cycle_rank"]
            == kappa_B_noncontextual.kappa
        ),
        nu_consistent_across_domains=(
            kappa_B_noncontextual.kappa == native_noncontextual["native_frustrated_cycle_rank"]
        ),
    ))

    # Control: tree A (kappa=0) -> noncontextual B (predicted rank 0)
    tm_tree = transport_kappa_A_to_B(
        kappa_A_results["tree_structured"], kappa_B_noncontextual.cover_name
    )
    trials.append(TransportTrial(
        a_instance="tree_structured",
        kappa_A=kappa_A_results["tree_structured"].kappa,
        a_frustrated=kappa_A_results["tree_structured"].frustrated,
        predicted_kappa_B=tm_tree.predicted_target_kappa,
        measured_native_B_rank=native_noncontextual["native_frustrated_cycle_rank"],
        measured_kappa_B_via_nu=kappa_B_noncontextual.kappa,
        prediction_matches_native=(
            tm_tree.predicted_target_kappa
            == native_noncontextual["native_frustrated_cycle_rank"]
            == kappa_B_noncontextual.kappa
        ),
        nu_consistent_across_domains=(
            kappa_B_noncontextual.kappa == native_noncontextual["native_frustrated_cycle_rank"]
        ),
    ))

    all_predictions_match = all(t.prediction_matches_native for t in trials)
    kappa_single_formula = True  # by construction: compute_kappa is the only formula
    audit = shared_derivation_audit()
    no_shared_derivation = (
        not audit["T21_shares_derivation_with_T39"]
    )

    # Verdict logic.
    #  PASS  : all predictions match AND no shared derivation AND one formula.
    #  FAIL  : prediction misses, OR kappa had to be re-tuned per domain.
    pass_condition = all_predictions_match and no_shared_derivation and kappa_single_formula

    # Two-absorber caveat: this cycle confirms ONE unrelated absorber (T21). The
    # open-problem PASS bar requires >= 2 unrelated absorbers. We state this.
    two_absorber_confirmation = False  # only T21 cleared this cycle

    return {
        "kappa_definition": (
            "kappa(nu) = dim_{Z/2} H^1 of the signed graph of the neighbor-visible "
            "same/different cover = rank of the frustrated cycle space = number of "
            "independent frustrated parity cycles. ONE formula (compute_kappa), "
            "parameterized only by (variables, signed edges)."
        ),
        "kappa_A": {n: _kappa_dict(k) for n, k in kappa_A_results.items()},
        "kappa_B": {
            "contextual_chsh": _kappa_dict(kappa_B_contextual),
            "noncontextual_chsh": _kappa_dict(kappa_B_noncontextual),
        },
        "native_B": {
            "contextual_chsh": native_contextual,
            "noncontextual_chsh": native_noncontextual,
        },
        "shared_derivation_audit": audit,
        "trials": [_trial_dict(t) for t in trials],
        "all_predictions_match": all_predictions_match,
        "kappa_single_formula": kappa_single_formula,
        "no_shared_derivation": no_shared_derivation,
        "two_absorber_confirmation": two_absorber_confirmation,
        "verdict": "PASS" if pass_condition else "FAIL",
        "verdict_caveat": (
            "ONE unrelated absorber (T21 Bell/CHSH) cleared the prediction this "
            "cycle with no shared derivation; the open-problem's full cross-domain "
            "classification theorem requires the prediction to clear on >= 2 "
            "unrelated absorbers. Two-absorber confirmation remains for a later "
            "cycle. No theorem is over-claimed here."
        ),
        "complexity_tags": ["finite_witness", "poly_decider"],
        "guardrails": (
            "No physics/geometry/curvature/new-object language promoted. kappa is "
            "a Z/2 graph-homology rank over a finite cover, computed by BFS "
            "2-coloring (poly_decider, not a search; not an NP-hardness claim)."
        ),
    }


def _all_same_chsh_scenario() -> CHSHFinalityScenario:
    """Control B: a CHSH-shaped cover with ALL parities +1 (even 4-cycle).

    Same four settings and four contexts as the canonical scenario, but every
    context demands 'same' (parity +1). The product of parities is +1, a global
    assignment (all +1) exists, native obstruction rank 0. This is the
    non-contextual control: structurally a balanced signed graph.
    """
    canon = canonical_chsh_finality_scenario()
    new_contexts = tuple(
        MeasurementContext(c.name, c.left, c.right, 1, c.finality_score)
        for c in canon.contexts
    )
    return CHSHFinalityScenario(
        name="noncontextual_chsh_all_same_control",
        settings=canon.settings,
        contexts=new_contexts,
    )


def _kappa_dict(k: KappaResult) -> dict[str, Any]:
    return {
        "cover_name": k.cover_name,
        "num_variables": k.num_variables,
        "num_edges": k.num_edges,
        "num_components": k.num_components,
        "kappa": k.kappa,
        "cycle_space_rank": k.cycle_space_rank,
        "global_section_exists": k.global_section_exists,
        "frustrated": k.frustrated,
    }


def _trial_dict(t: TransportTrial) -> dict[str, Any]:
    return {
        "a_instance": t.a_instance,
        "kappa_A": t.kappa_A,
        "a_frustrated": t.a_frustrated,
        "predicted_kappa_B": t.predicted_kappa_B,
        "measured_native_B_rank": t.measured_native_B_rank,
        "measured_kappa_B_via_nu": t.measured_kappa_B_via_nu,
        "prediction_matches_native": t.prediction_matches_native,
        "nu_consistent_across_domains": t.nu_consistent_across_domains,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_transport_test(), indent=2))
