"""T389: persona narrative, scientific story, Hegelian analysis, metasynthesis.

This is a synthesis artifact over the T376-T388 relativity-substrate ladder.
It uses the ten T387 personas to steelman the plain-English narrative, reverse
that narrative into a cautious scientific story, analyze the dialectic, and
produce a metasynthesis for the next research move.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.ten_persona_gap_audit import persona_lenses


@dataclass(frozen=True)
class PersonaNarrativePass:
    persona_id: str
    narrative_steelman: str
    scientific_reverse: str
    key_warning: str


@dataclass(frozen=True)
class ScientificStory:
    story_id: str
    status: str
    statement: str
    depends_on: tuple[str, ...]
    open_risk: str


@dataclass(frozen=True)
class HegelianMoment:
    moment_id: str
    name: str
    statement: str
    pressure: str


@dataclass(frozen=True)
class T389Result:
    persona_count: int
    persona_ids: tuple[str, ...]
    persona_passes: tuple[PersonaNarrativePass, ...]
    plain_english_narrative: str
    scientific_story: tuple[ScientificStory, ...]
    hegelian_analysis: tuple[HegelianMoment, ...]
    metasynthesis: str
    conditional_chain: tuple[str, ...]
    claim_upgrade_allowed: bool
    next_open_object: str
    recommended_next_goal: str
    overall_verdict: str
    claim_ledger_update: str


def persona_narrative_passes() -> tuple[PersonaNarrativePass, ...]:
    return (
        PersonaNarrativePass(
            "mathematical_formalist",
            (
                "The story is becoming a chain of definitions: final records, local "
                "compatibility, mutual attestability, handshake, and observer rendering."
            ),
            (
                "A theorem-ready version should state exactly which predicates are primitive, "
                "which are derived, and which remain open."
            ),
            "Do not let evocative words like compatibility or signal stand in for definitions.",
        ),
        PersonaNarrativePass(
            "relativity_physicist",
            (
                "The narrative is that spacetime-looking behavior may be a rendering of "
                "invariant record compatibility rather than a preloaded background grid."
            ),
            (
                "The scientific core is conditional Lorentz-pattern recovery from a shared "
                "record substrate plus a two-null-channel signal interface."
            ),
            "Two protocol legs are not yet lightlike legs with a bilinear interval.",
        ),
        PersonaNarrativePass(
            "distributed_systems_engineer",
            (
                "The picture resembles a distributed system where finality is not a single "
                "clock, but a durable relationship both endpoints can attest."
            ),
            (
                "Record-finalizable shared state can force mutual receipts without a global "
                "coordinator, which then motivates a bidirectional handshake."
            ),
            "Message acknowledgment must not be confused with physical compatibility.",
        ),
        PersonaNarrativePass(
            "category_sheaf_theorist",
            (
                "The local story is strong: compatible records witness each other. The global "
                "story asks whether those witnesses glue into coherent observer views."
            ),
            (
                "The next mathematical burden is descent: pairwise finalizable attestations "
                "must remain consistent on overlaps."
            ),
            "Local mutuality can fail globally unless overlap conditions are tested.",
        ),
        PersonaNarrativePass(
            "information_theorist",
            (
                "The system reads like information cannot appear everywhere at once; records "
                "become compatible only through a finite shared signal unit."
            ),
            (
                "A stronger scientific story would derive the invariant signal unit and "
                "speed-limit behavior from finite information transfer constraints."
            ),
            "The invariant unit is still granted after the two-leg story begins.",
        ),
        PersonaNarrativePass(
            "gauge_invariance_auditor",
            (
                "The narrative is trying to separate what is real in the substrate from how "
                "an observer labels or renders it."
            ),
            (
                "Scientific progress requires quotienting away relabels while preserving "
                "interval-bearing signal structure."
            ),
            "A hidden counter, queue, or foliation can smuggle background time back in.",
        ),
        PersonaNarrativePass(
            "adversarial_security_reviewer",
            (
                "The story depends on receipts being real records, not fake claims of mutuality."
            ),
            (
                "The scientific semantics must include provenance and authenticity so spoofed "
                "or replayed receipts cannot simulate compatibility."
            ),
            "Forged mutuality can make the whole bridge look stronger than it is.",
        ),
        PersonaNarrativePass(
            "minimality_auditor",
            (
                "The elegant version keeps stripping away what is not needed until the two-leg "
                "adapter is left."
            ),
            (
                "Minimality currently acts as a selection principle: no global clock, no scalar "
                "shortcut, no overcomplete protocol, no redundant primitive phase."
            ),
            "Minimality itself needs an origin, or it remains a modeling preference.",
        ),
        PersonaNarrativePass(
            "experimental_falsification_designer",
            (
                "The narrative is now testable as a sequence of alternatives that should fail "
                "for explicit reasons."
            ),
            (
                "The next scientific screen should compare null, timelike, delayed, noisy, "
                "and purely causal two-leg protocols."
            ),
            "The strongest positive control must show why null geometry wins, not just why alternatives fail.",
        ),
        PersonaNarrativePass(
            "paper_reviewer",
            (
                "The strongest paper narrative is not 'we derived relativity,' but 'we found a "
                "conditional path from final records to relativity-like rendering.'"
            ),
            (
                "The publishable story should separate derived, motivated, imported, and open "
                "objects before claiming physical significance."
            ),
            "Overstating the conditional result would make the work easier to dismiss.",
        ),
    )


def scientific_story() -> tuple[ScientificStory, ...]:
    return (
        ScientificStory(
            "substrate",
            "derived_in_ladder",
            (
                "A shared compatibility substrate can generate observer renderings without "
                "source rows storing primitive time or space."
            ),
            ("T377", "T378"),
            "Finite fixture scope and generated-closure assumptions remain.",
        ),
        ScientificStory(
            "relativity_pattern",
            "conditional_pattern_theorem",
            (
                "Given two primitive null signal directions, a bilinear interval, and "
                "round-trip calibration, observers recover Lorentz-pattern invariants."
            ),
            ("T379", "T380", "T384"),
            "The nullness and bilinear interval premises are not fully derived.",
        ),
        ScientificStory(
            "adapter_origin",
            "motivated_conditionally",
            (
                "A minimal local round-trip handshake motivates exactly two primitive signal "
                "directions better than scalar, one-way, global-clock, or overcomplete controls."
            ),
            ("T385", "T386"),
            "Minimality still does real selection work.",
        ),
        ScientificStory(
            "mutuality_origin",
            "derived_under_record_finality_semantics",
            (
                "If compatibility means record-finalizable shared state, durable authentic "
                "receipts at both endpoints force mutual local attestability."
            ),
            ("T388",),
            "Raw compatibility alone remains underdetermined.",
        ),
        ScientificStory(
            "live_frontier",
            "open",
            (
                "The next scientific question is whether the two protocol legs must be null "
                "signal directions with bilinear interval structure, rather than merely a "
                "communication analogy."
            ),
            ("T387", "T388"),
            "This is the two_leg_to_null_signal_bridge.",
        ),
    )


def hegelian_analysis() -> tuple[HegelianMoment, ...]:
    return (
        HegelianMoment(
            "thesis",
            "background spacetime",
            (
                "The ordinary thesis is that observers live inside spacetime and measure "
                "events against an already-given time/space structure."
            ),
            "This makes relativity natural, but imports the arena the repo wants to reconstruct.",
        ),
        HegelianMoment(
            "antithesis",
            "record finality without background time",
            (
                "The antithesis is that only final records and compatibility relations are "
                "primitive; observer time and space are renderings."
            ),
            "This avoids imported spacetime, but risks becoming only a protocol metaphor.",
        ),
        HegelianMoment(
            "synthesis",
            "relativity as invariant rendering of finalizable compatibility",
            (
                "The synthesis is that relativistic structure can arise as the invariant way "
                "observers render a shared finalizable compatibility substrate."
            ),
            "The synthesis is conditional on the bridge from finalizable two-leg protocols to null geometry.",
        ),
        HegelianMoment(
            "new_contradiction",
            "protocol legs versus physical null signals",
            (
                "The new contradiction is that the ladder now grounds mutual two-leg exchange, "
                "but has not shown why those legs are physically null and interval-bearing."
            ),
            "This contradiction selects the next research target.",
        ),
        HegelianMoment(
            "next_movement",
            "derive or falsify the two-leg-to-null bridge",
            (
                "The next movement should test whether finalizable compatibility forces null "
                "propagation, or whether nullness remains an external adapter assumption."
            ),
            "A failed bridge would demote the result to a strong protocol analogy.",
        ),
    )


def run_t389_analysis() -> T389Result:
    lenses = persona_lenses()
    passes = persona_narrative_passes()
    persona_ids = tuple(lens.persona_id for lens in lenses)
    return T389Result(
        persona_count=len(passes),
        persona_ids=persona_ids,
        persona_passes=passes,
        plain_english_narrative=(
            "The steelman story is that spacetime is not being assumed first. Instead, "
            "there is a substrate of final records. Records become compatible only when "
            "their relation can be finalized as shared state: both sides have durable, "
            "authentic local receipts, without a global clock or reconciler. That mutual "
            "finality minimally looks like a bidirectional handshake. If those two legs "
            "are the primitive null signal directions, then different observers can render "
            "the same substrate with relativity-like disagreement about time while preserving "
            "the same interval structure."
        ),
        scientific_story=scientific_story(),
        hegelian_analysis=hegelian_analysis(),
        metasynthesis=(
            "The best current interpretation is a conditional scientific program, not a "
            "finished derivation. TaF has built a plausible path from record-finalizable "
            "compatibility to mutuality, from mutuality to a bidirectional handshake, and "
            "from a granted two-null signal basis to Lorentz-pattern rendering. The decisive "
            "next step is to test the bridge between the handshake and null geometry. If that "
            "bridge holds, the narrative becomes much more than a distributed-systems analogy. "
            "If it fails, the repo still gains a precise boundary: finality explains mutual "
            "record compatibility, while null spacetime geometry remains an imported adapter."
        ),
        conditional_chain=(
            "record-finalizable shared-state compatibility",
            "mutual local attestability",
            "minimal bidirectional handshake",
            "two primitive signal directions",
            "two-null basis only if nullness/bilinearity bridge holds",
            "Lorentz-pattern observer rendering",
        ),
        claim_upgrade_allowed=False,
        next_open_object="two_leg_to_null_signal_bridge",
        recommended_next_goal=(
            "T390 two-leg-to-null signal bridge screen: compare finalizable two-leg protocols "
            "that are null, timelike, delayed, noisy, causal-only, and gauge-relabel-only; "
            "determine whether record-finality plus invariant propagation forces null "
            "bilinear signal geometry or merely assumes it."
        ),
        overall_verdict=(
            "persona_metasynthesis_supports_conditional_record_finality_narrative_and_prioritizes_two_leg_to_null_bridge"
        ),
        claim_ledger_update=(
            "Register T389 as narrative/scientific/Hegelian/metasynthesis: no claim upgrade; "
            "the live frontier is two_leg_to_null_signal_bridge."
        ),
    )


def t389_result_to_dict(result: T389Result) -> dict[str, object]:
    return {
        "persona_count": result.persona_count,
        "persona_ids": list(result.persona_ids),
        "persona_passes": [
            {
                "persona_id": item.persona_id,
                "narrative_steelman": item.narrative_steelman,
                "scientific_reverse": item.scientific_reverse,
                "key_warning": item.key_warning,
            }
            for item in result.persona_passes
        ],
        "plain_english_narrative": result.plain_english_narrative,
        "scientific_story": [
            {
                "story_id": item.story_id,
                "status": item.status,
                "statement": item.statement,
                "depends_on": list(item.depends_on),
                "open_risk": item.open_risk,
            }
            for item in result.scientific_story
        ],
        "hegelian_analysis": [
            {
                "moment_id": item.moment_id,
                "name": item.name,
                "statement": item.statement,
                "pressure": item.pressure,
            }
            for item in result.hegelian_analysis
        ],
        "metasynthesis": result.metasynthesis,
        "conditional_chain": list(result.conditional_chain),
        "claim_upgrade_allowed": result.claim_upgrade_allowed,
        "next_open_object": result.next_open_object,
        "recommended_next_goal": result.recommended_next_goal,
        "overall_verdict": result.overall_verdict,
        "claim_ledger_update": result.claim_ledger_update,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t389_result_to_dict(run_t389_analysis()), indent=2))
