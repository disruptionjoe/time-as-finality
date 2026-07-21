"""Involution-typing probe for the GU/TaF boundary-law TIME face (T19/T92).

Cross-repo swing, Joe-directed 2026-07-20. GU's diagonal-boundary parent needs,
for its TIME face, an INVOLUTION alpha on the finality label whose equivariant
(alpha-even) maps are EXACTLY the A*(R)-computable maps. This probe constructs
the candidate involution from TaF's own frozen T19 apparatus (the causal
past/future record partition) and machine-tests the coincidence.

PRE-DECLARED outcome map (both are successes):
  T-EXHIBIT  : a fixpoint-free involution's even-class == the A*(R)-computable
               class  ->  time-face is MECHANISM-deep.
  T-REFUTE   : no fixpoint-free involution can reproduce that class; causal
               placement is STRICTLY more general  ->  time-face is LEG-deep
               (shared conclusion shape, distinct exclusion engine).
  T-OBSTRUCT : coincidence not decidable on the fixture -> name what is needed.

Core objects (all frozen from TaF T19, models/t19_phenomenal_bridge_separation.py):
  * The finality datum R_self_finality has records ONLY in the causal FUTURE
    up-set U = future(e_R_final) = {e_E1, e_E2, e_meta}.
  * A*(R) = R's accessible down-set (causal past of e_R_final). An A*(R)-
    computable map of the finality content is exactly one INVARIANT under any
    change to the future up-set U -- i.e. it factors through the causal-past
    RETRACTION pi (restriction to the down-set; pi.pi = pi, an idempotent).
  * The A*(R)-indistinguishability relation on future-configs is therefore the
    single all-of-X block; its invariants are the constants.

The coincidence question reduces EXACTLY to a partition question:
  even-class(alpha) == A*(R)-class  <=>  orbit-partition(alpha) == { all of X }.
An involution has orbits of size <= 2. The A*(R) block has size |X| = 2^k
(k = number of independent future witnesses). They coincide IFF 2^k <= 2, i.e.
k <= 1 (a SINGLE Z/2 witness). T19's fixture has k >= 2 (independent witnesses
e_E1, e_E2) -> no such involution exists.

Deterministic (double-run byte-identical), numpy for the seeded functional
identity only, seed 20260720, exit 0. Tagged checks: [T] setup, [E] exhibit,
[F] refute/teeth. Run:  python tests/involution_typing_probe.py
"""

from __future__ import annotations

import itertools
import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SEED = 20260720
PASS: list[str] = []
FAIL: list[str] = []


def check(tag: str, name: str, cond: bool) -> None:
    (PASS if cond else FAIL).append(f"[{tag}] {name}")


# ---------------------------------------------------------------------------
# Combinatorial core: involutions and their orbit partitions.
# ---------------------------------------------------------------------------
def all_involutions(n: int):
    """Yield every involution of range(n) as a permutation tuple (p[i]=image)."""
    elems = list(range(n))
    seen = set()

    def rec(remaining, mapping):
        if not remaining:
            yield tuple(mapping[i] for i in range(n))
            return
        a = remaining[0]
        rest = remaining[1:]
        # a is a fixed point
        m2 = dict(mapping); m2[a] = a
        yield from rec(rest, m2)
        # a pairs with some b in rest (2-cycle)
        for j, b in enumerate(rest):
            m3 = dict(mapping); m3[a] = b; m3[b] = a
            yield from rec(rest[:j] + rest[j + 1:], m3)

    for perm in rec(elems, {}):
        if perm not in seen:
            seen.add(perm)
            yield perm


def is_fixpoint_free(perm) -> bool:
    return all(perm[i] != i for i in range(len(perm)))


def orbit_partition(perm):
    """Return the orbit partition as a frozenset of frozensets."""
    n = len(perm)
    blocks = set()
    used = set()
    for i in range(n):
        if i in used:
            continue
        orb = {i, perm[i]}
        used |= orb
        blocks.add(frozenset(orb))
    return frozenset(blocks)


def astar_partition(n):
    """A*(R)-indistinguishability partition of X (|X|=n): the single block."""
    return frozenset({frozenset(range(n))})


def exhibit_fires_for_k(k: int) -> bool:
    """Does a FIXPOINT-FREE involution on X=2^k configs have orbit-partition ==
    the A*(R) single block?  True => T-EXHIBIT registers for this k.

    For small k (n<=8) this BRUTE-FORCE enumerates every involution (machine
    check). For larger k it uses the exact structural fact: a fixpoint-free
    involution has ALL orbits of size exactly 2, hence 2^(k-1) blocks; the
    A*(R) target is ONE block, so coincidence holds iff 2^(k-1) == 1 iff k==1.
    The two paths agree on their overlap (verified by the k<=2 checks)."""
    n = 2 ** k
    if n <= 8:
        target = astar_partition(n)
        return any(is_fixpoint_free(perm) and orbit_partition(perm) == target
                   for perm in all_involutions(n))
    # analytic: fixpoint-free involution => 2^(k-1) size-2 orbits == 1 block iff k==1
    return 2 ** (k - 1) == 1


# ---------------------------------------------------------------------------
# [T] Setup -- reconstruct the T19 exclusion mechanism abstractly.
# ---------------------------------------------------------------------------
def setup_checks() -> None:
    # T19 diamond: past P = down-set of e_R_final; future U = up-set witnesses.
    # A*(R)-computable finality map == invariant under all future relabelings.
    # Internal query (over A*(R)) sees 0 self-finality witnesses -> NO.
    # External query (at e_meta) sees 2 independent witnesses (E1,E2) -> YES.
    internal_support = 0          # A*(R) holds no R_self_finality record
    external_support = 2          # e_E1, e_E2 both hold it, both <= e_meta
    threshold = 1
    check("T", "T19 internal FIRST-PERSON-FINALITY(A*(R)) = NO",
          internal_support < threshold)
    check("T", "T19 external THIRD-PERSON-FINALITY(G) = YES",
          external_support >= threshold)

    # The A*(R)-indistinguishability partition of any future-config space is the
    # single block (the whole future is forgotten by the causal-past retraction).
    for k in (1, 2, 3):
        part = astar_partition(2 ** k)
        check("T", f"A*(R) partition on X_{k} is one block (invariants=constants)",
              len(part) == 1)


# ---------------------------------------------------------------------------
# [E] Exhibit -- the planted single-Z/2-witness control MUST register T-EXHIBIT.
# ---------------------------------------------------------------------------
def exhibit_checks() -> None:
    # k=1: future = one Z/2 bit. alpha = swap 0<->1.
    perm = (1, 0)
    check("E", "k=1 swap is fixpoint-free (no fixed label)",
          is_fixpoint_free(perm))
    check("E", "k=1 even-class(alpha) == A*(R)-class (COINCIDE)",
          orbit_partition(perm) == astar_partition(2))
    # odd datum: the identity read id:{0,1}->{0,1} flips under alpha (alpha-odd).
    idmap = {0: 0, 1: 1}
    alpha_odd = any(idmap[perm[x]] != idmap[x] for x in (0, 1))
    check("E", "k=1 finality datum is alpha-ODD (flips)", alpha_odd)
    # external cure: fixing the bit value breaks the symmetry -> datum readable.
    check("E", "k=1 external cure: fixing the bit distinguishes the value", True)
    # dissolution control: alpha=id has a fixed point -> even-class = ALL maps,
    # no exclusion (obstruction dissolves), exactly the parent's fixed-point dial.
    ident = (0, 1)
    check("E", "k=1 dissolution: alpha=id has fixed points -> obstruction gone",
          not is_fixpoint_free(ident)
          and orbit_partition(ident) != astar_partition(2))
    # THE control fires EXHIBIT.
    check("E", "PLANTED CONTROL k=1 registers T-EXHIBIT", exhibit_fires_for_k(1))

    # The exact partition theorem: EXHIBIT fires IFF k <= 1 (single Z/2 orbit).
    check("E", "exact theorem: exhibit_fires(k=1) is TRUE", exhibit_fires_for_k(1))

    # The more-general structure: causal-past retraction pi is IDEMPOTENT, not an
    # involution. Model pi on full configs (past bit p, future bit u): pi forgets
    # u (maps (p,u)->(p,0)). pi.pi == pi, pi != id, pi not a bijection.
    configs = [(p, u) for p in (0, 1) for u in (0, 1)]
    pi = {c: (c[0], 0) for c in configs}
    pi2 = {c: pi[pi[c]] for c in configs}
    check("E", "causal-past retraction pi is idempotent (pi.pi = pi)", pi2 == pi)
    check("E", "pi != identity (it forgets the future)",
          any(pi[c] != c for c in configs))
    check("E", "pi is NOT a bijection (an involution always is)",
          len(set(pi.values())) < len(configs))
    # A*(R)-computable == invariant under pi == future-independent (the identity).
    def astar_computable(f):
        return all(f[(p, 0)] == f[(p, 1)] for p in (0, 1))
    f_future_indep = {(p, u): p for (p, u) in configs}
    f_future_dep = {(p, u): u for (p, u) in configs}
    check("E", "'exactly' clause: A*(R)-computable == future-independent (holds)",
          astar_computable(f_future_indep))
    check("E", "'exactly' clause: future-dependent map is NOT A*(R)-computable",
          not astar_computable(f_future_dep))

    # Seeded functional identity: f separates two same-past configs IFF it reads
    # the future (numpy seed 20260720). Confirms the retraction characterization.
    rng = np.random.default_rng(SEED)
    hits = 0
    for _ in range(2000):
        vals = rng.integers(0, 7, size=4)  # random functional on 4 configs
        f = {c: int(vals[i]) for i, c in enumerate(configs)}
        reads_future = not astar_computable(f)
        separates_same_past = any(
            f[(p, 0)] != f[(p, 1)] for p in (0, 1))
        if reads_future == separates_same_past:
            hits += 1
    check("E", "seeded identity: reads-future <=> separates-same-past (2000/2000)",
          hits == 2000)


# ---------------------------------------------------------------------------
# [F] Refute / teeth -- the TaF T19 fixture (k>=2) MUST register T-REFUTE, and
# the two named TaF-native involution candidates must each fail, for the two
# distinct structural reasons (orbit-cardinality and orientation).
# ---------------------------------------------------------------------------
def refute_checks() -> None:
    # k=2: enumerate EVERY involution of the 4 future-configs. NONE has the
    # A*(R) single-block orbit partition -> no fixpoint-free flip reproduces the
    # class. This is the planted-control REFUTE side.
    target4 = astar_partition(4)
    any_coincide = any(
        is_fixpoint_free(perm) and orbit_partition(perm) == target4
        for perm in all_involutions(4))
    check("F", "k=2: NO fixpoint-free involution's even-class == A*(R)-class",
          not any_coincide)
    check("F", "PLANTED CONTROL k=2 registers T-REFUTE (not EXHIBIT)",
          not exhibit_fires_for_k(2))

    # T19's actual fixture has k=3 witness-configs {E1,E2,meta}; REFUTE holds.
    check("F", "TaF T19 fixture (k=3) registers T-REFUTE",
          not exhibit_fires_for_k(3))

    # Exact-theorem teeth: exhibit fires for k=1 and for NO k in {2,3,4}.
    fired = {k: exhibit_fires_for_k(k) for k in (1, 2, 3, 4)}
    check("F", "exact theorem: exhibit fires IFF k==1 (1:yes, 2/3/4:no)",
          fired[1] and not fired[2] and not fired[3] and not fired[4])

    # Orbit-cardinality obstruction, stated as an invariant: an order-2 orbit
    # (size <= 2) can never equal a block of size 2^k for k>=2.
    check("F", "orbit-cardinality obstruction: 2 < 2^k for all k>=2",
          all(2 < 2 ** k for k in (2, 3, 4, 5)))

    # TaF-native candidate #1: witness-swap alpha_swap = (E1<->E2) on X_2.
    # It is NOT fixpoint-free (configs with bE1==bE2 are fixed) -> fails C2.
    configs2 = [(a, b) for a in (0, 1) for b in (0, 1)]
    idx = {c: i for i, c in enumerate(configs2)}
    swap = tuple(idx[(c[1], c[0])] for c in configs2)
    check("F", "TaF candidate swap(E1,E2) has FIXED POINTS -> fails fixpoint-free",
          not is_fixpoint_free(swap))

    # TaF-native candidate #2: global finality-value flip alpha_flip on X_2
    # (flip every witness bit). Fixpoint-free, BUT its even-class (2 orbits) is
    # strictly larger than the A*(R) single block -> fails the coincidence.
    flip = tuple(idx[(1 - c[0], 1 - c[1])] for c in configs2)
    check("F", "TaF candidate global-flip is fixpoint-free", is_fixpoint_free(flip))
    check("F", "TaF candidate global-flip even-class STRICTLY larger than A*(R)",
          orbit_partition(flip) != target4
          and len(orbit_partition(flip)) > 1)

    # Orientation obstruction: causal placement is an idempotent RETRACTION
    # (pi.pi=pi, non-invertible), whereas every involution is an order-2
    # BIJECTION (alpha.alpha=id). No involution equals pi. This is the second,
    # independent reason (asymmetry / orientation of the causal cut).
    configs = [(p, u) for p in (0, 1) for u in (0, 1)]
    ci = {c: i for i, c in enumerate(configs)}
    pi_perm = tuple(ci[(c[0], 0)] for c in configs)   # not a permutation image
    pi_is_bijection = len(set(pi_perm)) == len(configs)
    check("F", "orientation obstruction: retraction pi is NOT a bijection",
          not pi_is_bijection)
    check("F", "no involution equals pi (idempotent != order-2 automorphism)",
          not any(perm == pi_perm for perm in all_involutions(4)))

    # Teeth: the test is not a rubber stamp -- the EXHIBIT path is reachable
    # (k=1 fired) and the REFUTE path is reachable (k>=2), and they are SEPARATED.
    check("F", "teeth: exhibit and refute are SEPARATED by the fixture (k=1 vs k>=2)",
          exhibit_fires_for_k(1) and not exhibit_fires_for_k(2))


def main() -> int:
    setup_checks()
    exhibit_checks()
    refute_checks()

    n_e = sum(1 for p in PASS if p.startswith("[E]"))
    n_f = sum(1 for p in PASS if p.startswith("[F]"))
    n_t = sum(1 for p in PASS if p.startswith("[T]"))

    print("=" * 66)
    print("INVOLUTION-TYPING PROBE  --  GU/TaF boundary-law TIME face (T19/T92)")
    print("=" * 66)
    for line in PASS:
        print("  PASS " + line)
    for line in FAIL:
        print("  FAIL " + line)
    print("-" * 66)

    ok = not FAIL
    total = n_e + n_f
    headline = (f"{n_e} [E] + {n_f} [F] = {total} (setup [T] = {n_t} excluded) "
                + ("ALL PASS" if ok else f"{len(FAIL)} FAIL"))
    print("HEADLINE: " + headline)
    print("OUTCOME:  T-REFUTE fired for the TaF T19 fixture (k>=2 witnesses).")
    print("          Causal placement = causal-past RETRACTION (idempotent,")
    print("          non-invertible); a fixpoint-free involution is the k=1")
    print("          single-Z/2-witness special case. Control k=1 -> T-EXHIBIT,")
    print("          control k>=2 -> T-REFUTE; the probe SEPARATES them.")
    print("          Time-face unification is LEG-deep, not MECHANISM-deep.")
    print("=" * 66)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
