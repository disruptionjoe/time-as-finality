# T38: Minimal Multiscale Transport Formalization

## Setup

This test evaluates five competing hypotheses (H0-H4) against ten core
transport questions, using five executable scenarios. The central question
is what the smallest mathematical object capable of expressing all ten
questions is.

The test does not assume layers, hierarchies, bundles, sheaves, or
categories are correct abstractions. It asks which abstraction is
minimally justified by the evidence.

## Competing Hypotheses

| ID | Claim |
|----|-------|
| H0 | D1RestrictionSystem is sufficient. |
| H1 | TypedTransportNetwork is sufficient. |
| H2 | Graph-of-graphs or recursive transport is required. |
| H3 | Bundle, presheaf, or category is already required. |
| H4 | No canonical transport formalism is currently justified. |

## Core Transport Questions

| Q  | Question |
|----|----------|
| Q1 | What information is transported? |
| Q2 | What information is preserved? |
| Q3 | What information is forgotten? |
| Q4 | What information is compressed? |
| Q5 | What information only exists after transport? |
| Q6 | Can transport skip intermediate organizational levels? |
| Q7 | Can multiple transport channels coexist? |
| Q8 | Are different transport channels composable? |
| Q9 | When do paths produce equivalent observable outcomes? |
| Q10 | When do paths produce fundamentally different structures? |

## Executable Scenarios

### Compression Scenario (Q4)
- Source: 4-site D1RestrictionSystem, D1Profile(2,2,2,2) per site, no patches.
- Target: 2-site D1RestrictionSystem, D1Profile(4,2,2,2) per site, obstructed (contradictory patches).
- Morphism: many-to-one — sites {0,1} → tgt_A; sites {2,3} → tgt_B.
- forgotten_structure: ("individual_site_profiles",)
- Expected: PO1 admissible (AC5 fires: accessible_support 2≠4, forgotten non-empty).
- CompressionRecord tracks: ratio=0.5, retained aggregate=total_accessible_support, lost=individual profiles.

### Emergence Scenario (Q5)
- Source: 3-site system, no patches (no global constraints).
- Target: 3-site system, with patches (A=B, B=C) — globally satisfiable.
- Morphism: identity site map, all dims declared.
- Expected: NOT a PO1 instance (AC6 fails: target is unobstructed, patches are satisfiable).
- EmergenceRecord tracks: source_patches=0, target_patches=2, genuine_emergence=True.
- Key: emergence and obstruction are orthogonal phenomena.

### Level-Skip Test (Q6)
- Stepwise: SRC→MID→TGT via spectre_network (T37).
- Direct: SRC→TGT with composed morphism.
- Expected: verdict-equivalent (both PO1), information-equivalent in the spectre case
  (MID→TGT forgets nothing, so accumulated forgotten_structure matches).
- General principle: when intermediate step forgets additional structure,
  stepwise and direct are verdict-equivalent but information-inequivalent.
  TypedTransportNetwork detects this; D1RestrictionSystem alone cannot.

### Simultaneous Channels (Q7)
- Reuses diamond_network from T37: SRC→L_A→TGT and SRC→L_B→TGT.
- Expected: path_dependent=True, different PO1 verdicts per path.
- Already established in T37; reconfirmed here.

## Success Criteria

- [ ] Compression scenario: PO1 admissible, ratio=0.5, CompressionRecord populated.
- [ ] Emergence scenario: NOT PO1, genuine_emergence=True, EmergenceRecord populated.
- [ ] Level-skip test: verdict_equivalent=True; finding includes information-inequivalence principle.
- [ ] Simultaneous channels: path_dependent=True (diamond network).
- [ ] H0 coverage: 3/10 questions (Q1-Q3 only), verdict=rejected.
- [ ] H1 coverage: 8/10 questions (Q1-Q3, Q6-Q10), verdict=best_supported_with_extension.
- [ ] H2 verdict: not_required.
- [ ] H3 verdict: premature.
- [ ] H4 verdict: rejected.
- [ ] best_supported_hypothesis = "H1_extended".
- [ ] new_objects_required = (CompressionRecord, EmergenceRecord).
- [ ] h2_required = False, h3_required = False.
- [ ] 60 unit tests pass.

## Failure Conditions

- H0 should not be returned as sufficient — it cannot express compression ratio
  or emergence without explicit record objects.
- H2 should not be required — no scenario shows transport needing to be transported.
- H3 should not be required — no scenario demands identity morphisms or natural
  transformations; the open composition law is an H1 gap, not H3 evidence.
- The compression scenario must be PO1-admissible (if it is not, AC5 wiring is wrong).
- The emergence scenario must NOT be PO1-admissible (if it is, AC6 has been violated).

## Known Constraints

- many-to-one morphisms require preserved_dimensions=D1_DIMENSIONS so that
  accessible_support (2 vs 4) is compared, forcing local_profiles_preserved=False,
  which makes AC5 fire.
- EmergenceRecord is an annotation object; it does not add new axioms or change
  morphism semantics.
- CompressionRecord is an annotation object; compression_ratio is computed from
  site counts, not derived from morphism mathematics.
- The composition law (associativity) remains open; this is a gap in H1, not
  evidence for H3.
