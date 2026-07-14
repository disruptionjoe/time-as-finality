"""Time-as-Finality attention priority.

This is the ranking engine for the Time-as-Finality research-steering card.
Joe does not read the card. When he says he has attention for this repo, hand
him the top few ranked items with one-line reasons.

Condorcet is the primary rule: item X outranks item Y if a majority of council
personas prefer X to Y. If a cycle prevents a strict Condorcet order, rank by
Copeland score, meaning pairwise wins minus pairwise losses. Ties are broken by
average ballot position. Re-ranking means editing ITEMS and BALLOTS, then
running this script again.

Run:
    python attention/taf_priority_condorcet.py
"""
from __future__ import annotations

from itertools import combinations
from statistics import mean


ITEMS = {
    "TAF11": {
        "title": "TAF11 review-package closeout router",
        "why": (
            "T580 closed the current external panel for limited review; the "
            "next burden preserves the package, names reopen conditions, and "
            "blocks promotion by momentum."
        ),
    },
    "TAF12": {
        "title": "Data-bearing C(R) packet acquisition for TAF10",
        "why": (
            "T535 found no real packet in hand; the branch waits for exact full-stack "
            "profiles plus an independent noncompletion witness."
        ),
    },
    "TAF3": {
        "title": "Law-derived C(R) menus and physical noncompletion witness",
        "why": (
            "The current C(R) line keeps losing to declared-boundary and "
            "completion absorbers; derive the operation menu from dynamics."
        ),
    },
    "TAF4": {
        "title": "Finite-to-continuum finality colimit bridge",
        "why": (
            "Still blocked after T579: the causal-set measure-law probe "
            "supplied no finality-native continuum bridge."
        ),
    },
    "TAF5": {
        "title": "Adapter de-correlation for GU/TI/TAF boundary functors",
        "why": (
            "The current two-adapter signal remains review-only until source "
            "categories and encodings are de-correlated."
        ),
    },
    "TAF6": {
        "title": "Quantum access-structure and monogamy finality theorem",
        "why": (
            "T514-T520 leave a cleaner secret-sharing/access-structure strut than "
            "the falsified BFT threshold analogy."
        ),
    },
    "TAF7": {
        "title": "Detector provenance raw-log independent-axis packet",
        "why": (
            "The manifest is ready, but the lane needs a predeclared independent "
            "axis and data-bearing packet before it can move Q1."
        ),
    },
    "TAF8": {
        "title": "Cross-domain shadow-protection theorem target",
        "why": (
            "T579 preserved the T541 wait state: absorber pressure is not a "
            "domain-native cross-domain packet."
        ),
    },
}


BALLOTS = {
    "orthodox_professor": [
        "TAF11",
        "TAF8",
        "TAF4",
        "TAF3",
        "TAF12",
        "TAF6",
        "TAF5",
        "TAF7",
    ],
    "heterodox_rigorous_professor": [
        "TAF11",
        "TAF8",
        "TAF3",
        "TAF4",
        "TAF5",
        "TAF12",
        "TAF6",
        "TAF7",
    ],
    "commercial_scientist": [
        "TAF11",
        "TAF8",
        "TAF12",
        "TAF3",
        "TAF7",
        "TAF6",
        "TAF4",
        "TAF5",
    ],
    "philosopher_of_science": [
        "TAF11",
        "TAF8",
        "TAF3",
        "TAF12",
        "TAF4",
        "TAF6",
        "TAF5",
        "TAF7",
    ],
    "wild_frontier_scientist": [
        "TAF11",
        "TAF8",
        "TAF4",
        "TAF3",
        "TAF5",
        "TAF12",
        "TAF6",
        "TAF7",
    ],
    "causal_set_lorentzian": [
        "TAF11",
        "TAF8",
        "TAF4",
        "TAF3",
        "TAF12",
        "TAF5",
        "TAF6",
        "TAF7",
    ],
    "quantum_information_decoherence": [
        "TAF6",
        "TAF11",
        "TAF8",
        "TAF12",
        "TAF3",
        "TAF7",
        "TAF4",
        "TAF5",
    ],
    "distributed_systems_consensus": [
        "TAF12",
        "TAF3",
        "TAF11",
        "TAF8",
        "TAF7",
        "TAF6",
        "TAF5",
        "TAF4",
    ],
    "resource_theory_thermodynamics": [
        "TAF12",
        "TAF3",
        "TAF6",
        "TAF11",
        "TAF8",
        "TAF4",
        "TAF5",
        "TAF7",
    ],
    "category_sheaf_obstruction": [
        "TAF11",
        "TAF8",
        "TAF4",
        "TAF5",
        "TAF3",
        "TAF12",
        "TAF6",
        "TAF7",
    ],
    "complexity_cryptography": [
        "TAF11",
        "TAF8",
        "TAF12",
        "TAF3",
        "TAF6",
        "TAF4",
        "TAF5",
        "TAF7",
    ],
    "detector_metrology_provenance": [
        "TAF7",
        "TAF12",
        "TAF11",
        "TAF3",
        "TAF6",
        "TAF8",
        "TAF4",
        "TAF5",
    ],
}


def validate() -> None:
    item_ids = set(ITEMS)
    for name, ballot in BALLOTS.items():
        if len(ballot) != len(item_ids):
            raise ValueError(f"{name} ballot has {len(ballot)} entries, expected {len(item_ids)}")
        if len(set(ballot)) != len(ballot):
            raise ValueError(f"{name} ballot contains duplicate item ids")
        missing = item_ids - set(ballot)
        extra = set(ballot) - item_ids
        if missing or extra:
            raise ValueError(f"{name} ballot mismatch, missing={sorted(missing)}, extra={sorted(extra)}")


def prefers(ballot: list[str], left: str, right: str) -> bool:
    return ballot.index(left) < ballot.index(right)


def pairwise_margin(items: list[str]) -> dict[tuple[str, str], int]:
    margins: dict[tuple[str, str], int] = {}
    voter_count = len(BALLOTS)
    for left, right in combinations(items, 2):
        left_count = sum(1 for ballot in BALLOTS.values() if prefers(ballot, left, right))
        right_count = voter_count - left_count
        margins[(left, right)] = left_count - right_count
        margins[(right, left)] = right_count - left_count
    return margins


def copeland_scores(items: list[str], margins: dict[tuple[str, str], int]) -> dict[str, int]:
    scores = {item: 0 for item in items}
    for left, right in combinations(items, 2):
        margin = margins[(left, right)]
        if margin > 0:
            scores[left] += 1
            scores[right] -= 1
        elif margin < 0:
            scores[right] += 1
            scores[left] -= 1
    return scores


def condorcet_winner(items: list[str], margins: dict[tuple[str, str], int]) -> str | None:
    for item in items:
        if all(margins[(item, other)] > 0 for other in items if other != item):
            return item
    return None


def average_position(item: str) -> float:
    return mean(ballot.index(item) for ballot in BALLOTS.values())


def rank_items() -> list[str]:
    validate()
    items = list(ITEMS)
    margins = pairwise_margin(items)
    scores = copeland_scores(items, margins)
    return sorted(items, key=lambda item: (-scores[item], average_position(item), item))


def main() -> int:
    validate()
    items = list(ITEMS)
    margins = pairwise_margin(items)
    scores = copeland_scores(items, margins)
    winner = condorcet_winner(items, margins)
    ranked = rank_items()

    print("=" * 78)
    print("TAF ATTENTION PRIORITY")
    print("=" * 78)
    if winner:
        print(f"Condorcet winner: {winner} - {ITEMS[winner]['title']}")
    else:
        print("Condorcet winner: NONE, cycle resolved by Copeland order")
    print()
    print("Ranked list:")
    for index, item in enumerate(ranked, start=1):
        print(f"{index}. {item} | Copeland {scores[item]:+d} | avg position {average_position(item):.2f}")
        print(f"   {ITEMS[item]['title']}")
        print(f"   Why: {ITEMS[item]['why']}")
    print()
    print("Persona first choices:")
    for persona, ballot in BALLOTS.items():
        first = ballot[0]
        print(f"{persona}: {first} - {ITEMS[first]['title']}")
    print()
    print("Pairwise margins among top four, positive means row beats column:")
    top = ranked[:4]
    print("      " + " ".join(f"{item:>5}" for item in top))
    for left in top:
        row = []
        for right in top:
            row.append("    ." if left == right else f"{margins[(left, right)]:+5d}")
        print(f"{left:>5} " + " ".join(row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
