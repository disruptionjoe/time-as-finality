# T38 Results: Minimal Multiscale Transport Formalization

## Run

```
python -m models.run_t38
```

Output artifact: `results/minimal-multiscale-transport-v0.1.json`

## Evidence Table

| Scenario | Phenomenon | PO1 | Key finding |
|----------|-----------|-----|-------------|
| Compression (4→2 sites) | Q4 compression | Yes | ratio=0.5; accessible_support aggregated; CompressionRecord needed to express ratio and retained invariant |
| Emergence (no patches → satisfiable patches) | Q5 emergence | No | target gains global section; source lacks it; orthogonal to PO1; EmergenceRecord needed |
| Level-skip (stepwise vs. direct, spectre) | Q6 level-skip | Yes (both) | verdict-equivalent; information-equivalent when intermediate forgets nothing; TypedTransportNetwork detects inequivalence when intermediate forgets additional structure |
| Simultaneous channels (diamond network, T37) | Q7 channels | Path-dependent | path_dependent=True; different PO1 verdicts per channel |

## Hypothesis Coverage

| Hypothesis | Questions handled | Not handled | Verdict |
|------------|-------------------|-------------|---------|
| H0 (D1RestrictionSystem) | Q1, Q2, Q3 | Q4–Q10 | rejected |
| H1 (TypedTransportNetwork) | Q1–Q3, Q6–Q10 | Q4, Q5 | best_supported_with_extension |
| H2 (graph-of-graphs) | all (richer) | none | not_required |
| H3 (bundle/presheaf/category) | all (richer) | none | premature |
| H4 (no formalism justified) | none | all | rejected |

**Best supported:** H1_extended (TypedTransportNetwork + CompressionRecord + EmergenceRecord)

## Two Minimal New Objects

### CompressionRecord

Tracks:
- `source_site_count`, `target_site_count`, `compression_ratio`
- `retained_invariants`: aggregate properties that survived the collapse
- `lost_detail`: individual site properties lost
- `aggregate_rule`: how multiple source sites merged into one target site
- `po1_admissible`: whether the compression morphism is a PO1 instance

Why needed: `forgotten_structure` in a TypedTransportNetwork declares what was lost. A CompressionRecord additionally declares what aggregate was retained and at what ratio. These are distinct claims. Without CompressionRecord, two different transport events — one that forgets a specific structure and one that compresses 4 sites to 2 while summing accessible_support — look the same.

### EmergenceRecord

Tracks:
- `source_patch_count`, `target_patch_count`
- `source_has_global_section`, `target_has_global_section`
- `emergence_kind`, `is_genuine_emergence`
- `description`

Why needed: PO1 is about obstruction-creation (the restricted system loses a global section the richer system had). Emergence is about structure-creation (the target gains a global section the source lacked). Neither H0 nor H1 has a primitive for structure-creation. EmergenceRecord is the minimal object to name this orthogonal phenomenon.

## Level-Skip Finding

Stepwise (SRC→MID→TGT) and direct (SRC→TGT) transport are **verdict-equivalent** in the spectre network: both are PO1 instances. They are **information-equivalent** in this case because the intermediate MID→TGT transport declares empty `forgotten_structure`.

In general: when an intermediate transport forgets structure that the direct transport does not declare, stepwise and direct paths accumulate different `forgotten_structure` even when their PO1 verdicts agree. TypedTransportNetwork (H1) can detect this information inequivalence. D1RestrictionSystem (H0) cannot.

This means: level-skip is safe when the skipped level forgets nothing. It is information-obscuring (though not verdict-changing) when the skipped level forgets additional structure.

## Why H2 and H3 Are Not Required

**H2 (graph-of-graphs):** Would be needed if transport itself needed to be transported. No current scenario demonstrates this. Morphism composition already telescopes multi-level transport without requiring recursive nesting.

**H3 (bundle/presheaf/category):** Would be needed if identity morphisms, natural transformations, or fiber structures were required. No current scenario demands them. The composition law (associativity) is open, but that is a gap in H1, not evidence for H3. If associativity fails, that would be the first positive evidence for H3.

## Verdict

H1+ is the minimal justified transport formalism. The two annotation objects introduce no new axioms. The next formal obligation is proving (or falsifying) the composition law.
