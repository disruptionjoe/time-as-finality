"""Record-layer reconciliation naturality probe (exploration-attached; no T-number).

Spec and pre-registered predictions:
    explorations/record-layer-naturality-spec-2026-07-28.md

Fixture: the T588 twin fixture at ratio 2, read as a T585/T586-style record
store pair -- context 1 (stay_at_home, proper time 2.0, shared rate 1.0) holds
two records, context 2 (traveller, proper time 1.0) holds one. Records are
(record_id, clock_label); clock labels are order-inert per T586 and treated as
gauge per the spec's declared instantiation of T584's admissible classes.

Naturality square tested for componentwise admissible morphisms f, g
(record-ID transpositions = representation relabels; clock-label permutations
= gauge):

    Rec(f v g) . r  =?=  r . (Rec f x Rec g)

for four reconciliation forms: A_union_provenance (contract-A origin-tagged
union), C_canonical_pairing (contract-C, canonical full-product metadata),
C_lex_rank_pairing (contract-C, enumeration-order metadata),
C_clock_match_pairing (contract-C, gauge-reading metadata).

Outcome content is data, not an assertion: exit 0 iff internal sanity checks
pass. Stdlib only.
"""
from __future__ import annotations

import itertools
import json

RID_UNIVERSE = ("r1a", "r1b", "r2a", "z9", "w0")
CLOCK_ALPHABET = (0, 1)


def fixture():
    ctx1 = frozenset({("r1a", 0), ("r1b", 1)})  # stay_at_home, 2 records
    ctx2 = frozenset({("r2a", 0)})              # traveller, 1 record
    return ctx1, ctx2


def apply_m(m, store):
    rid_map, clock_map = m
    return frozenset((rid_map.get(r, r), clock_map.get(c, c)) for r, c in store)


def apply_joint(f, g, joint):
    """f v g: componentwise on origin-tagged records; on pair metadata by
    reference consistency (renames follow the record IDs they cite)."""
    out = set()
    for el in joint:
        if el[0] == "pair":
            out.add(("pair", f[0].get(el[1], el[1]), g[0].get(el[2], el[2])))
        else:
            m = f if el[0] == "ctx1" else g
            ((r, c),) = apply_m(m, frozenset({el[1:]}))
            out.add((el[0], r, c))
    return frozenset(out)


def base_union(r1, r2):
    return frozenset({("ctx1", r, c) for r, c in r1}
                     | {("ctx2", r, c) for r, c in r2})


def rec_a(r1, r2):
    return base_union(r1, r2)


def rec_c_canonical(r1, r2):
    return base_union(r1, r2) | {("pair", a, b) for a, _ in r1 for b, _ in r2}


def rec_c_lex(r1, r2):
    ranked = zip(sorted(r for r, _ in r1), sorted(r for r, _ in r2))
    return base_union(r1, r2) | {("pair", a, b) for a, b in ranked}


def rec_c_clock(r1, r2):
    return base_union(r1, r2) | {
        ("pair", a, b) for a, ca in r1 for b, cb in r2 if ca == cb}


FORMS = {
    "A_union_provenance": rec_a,
    "C_canonical_pairing": rec_c_canonical,
    "C_lex_rank_pairing": rec_c_lex,
    "C_clock_match_pairing": rec_c_clock,
}
IDENT = ({}, {})
RENAME_1 = {"r1a": "z9", "z9": "r1a"}  # transposition, flips ctx1 lex order
MORPHISMS_1 = {
    "id": IDENT,
    "rid_rename_lex_flip": (RENAME_1, {}),   # representation relabel
    "clock_swap": ({}, {0: 1, 1: 0}),        # gauge
    "rename_and_clock_swap": (RENAME_1, {0: 1, 1: 0}),
}
MORPHISMS_2 = {
    "id": IDENT,
    "rid_rename": ({"r2a": "w0", "w0": "r2a"}, {}),
    "clock_swap": ({}, {0: 1, 1: 0}),
}


def total_map_bijective(partial, universe):
    image = [partial.get(x, x) for x in universe]
    return len(set(image)) == len(image)


def run():
    r1, r2 = fixture()
    all_morphisms = list(MORPHISMS_1.values()) + list(MORPHISMS_2.values())
    sanity = {
        "morphisms_bijective": all(
            total_map_bijective(m[0], RID_UNIVERSE)
            and total_map_bijective(m[1], CLOCK_ALPHABET)
            for m in all_morphisms),
        "identity_square_commutes_all_forms": all(
            apply_joint(IDENT, IDENT, form(r1, r2)) == form(r1, r2)
            for form in FORMS.values()),
        "morphisms_preserve_cardinality": all(
            len(apply_m(m, s)) == len(s)
            for m in all_morphisms for s in (r1, r2)),
    }
    report = {}
    for name, form in FORMS.items():
        failures = []
        for (fn, f), (gn, g) in itertools.product(
                MORPHISMS_1.items(), MORPHISMS_2.items()):
            lhs = apply_joint(f, g, form(r1, r2))
            rhs = form(apply_m(f, r1), apply_m(g, r2))
            if lhs != rhs:
                failures.append({
                    "f": fn, "g": gn,
                    "lhs_only": sorted(map(list, lhs - rhs)),
                    "rhs_only": sorted(map(list, rhs - lhs)),
                })
        report[name] = {
            "status": "NATURAL_over_probe" if not failures else "NON_NATURAL",
            "squares_checked": len(MORPHISMS_1) * len(MORPHISMS_2),
            "failing_squares": len(failures),
            "witness": failures[0] if failures else None,
            "failing_pairs": [(w["f"], w["g"]) for w in failures],
        }
    payload = {
        "artifact": "record-reconciliation-naturality-probe-v0.1",
        "spec": "explorations/record-layer-naturality-spec-2026-07-28.md",
        "sanity": sanity,
        "forms": report,
    }
    print(json.dumps(payload, indent=2))
    return 0 if all(sanity.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
