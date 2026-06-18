# Technical Report: Projection-Obstruction Discovery Engine v0.1

## Purpose

T35 asks whether the finite PO1 framework can become generative rather than
only explanatory. Instead of starting from a known theorem or domain example,
the engine starts from bounded finite `D1RestrictionSystem` families and asks:

```text
Which projection structures naturally emerge?
```

This is not automated theorem discovery. It is a deterministic finite
exploration tool for generating candidate Projection-Obstruction structures
for human review.

## Method

The engine has five pieces:

| Component | Role |
| --- | --- |
| `RestrictionSystemGenerator` | generates bounded 3-site and 4-site finite systems |
| `ProjectionGenerator` | enumerates total and partial projection maps |
| `AdmissibilityEvaluator` | classifies each projection with the T31 checker |
| `CounterexampleReducer` | extracts minimal finite witnesses |
| `ObstructionExplorer` | runs the experiment and compares against T27-T34 signatures |

The generator uses only generic finite shapes:

```text
empty
consistent_chain
triangle_obstruction
square_obstruction
local_failure
```

No domain heuristics are used. Labels such as `generic_profile_detail` and
`generic_resolution_data` are structural placeholders only.

## Results

T35 generated:

| Quantity | Count |
| --- | --- |
| Generated finite systems | 18 |
| Projection candidates | 172 |
| Positive PO1 candidates | 9 |
| Boundary non-definable candidates | 90 |
| Lossy non-obstructing candidates | 12 |
| Obstruction-removed candidates | 12 |
| Shared-obstruction candidates | 10 |
| Trivial local-failure candidates | 18 |
| Outside-PO1 candidates | 21 |

Best supported hypothesis:

```text
H2 with H3 caution
```

The engine rediscovers at least one known PO1 signature and also generates
structurally novel positive candidates. The strongest new finite witness is a
four-patch obstruction:

```text
a = b
b = c
c = d
a != d
```

Each local patch is satisfiable, but the four patches do not admit a global
assignment. This is a generated positive PO1 candidate requiring four
restricted patches, unlike the familiar three-patch pattern used in several
prior examples.

## Classification

T35 keeps the T31 admissibility checker as the source of truth. It then adds
discovery labels:

| Discovery label | Meaning |
| --- | --- |
| `admissible_po1` | all AC1-AC7 conditions hold |
| `boundary_non_definable` | site map is not total |
| `shared_obstruction` | source and target are both obstructed |
| `lossy_non_obstructing` | projection is lossy but target remains globally satisfiable |
| `obstruction_removed` | source is obstructed but endpoint is not |
| `trivial_local_failure` | target fails locally rather than by gluing |
| `outside_po1` | no interesting PO1 class under current rules |

This makes T35 an explorer over finite restriction systems, not a replacement
for the PO1 theorem statement.

## Minimal Witnesses

The reducer found:

| Witness class | Example |
| --- | --- |
| minimal gluing obstruction | four-patch square obstruction |
| missing site map | partial projection with unmapped source sites |
| minimal loss without obstruction | lossy projection into an empty or consistent target |
| obstruction removed | obstructed source projected to globally satisfiable target |

For the four-patch positive witness, no smaller patch subset preserves the
restricted gluing obstruction. All four patches are needed.

## Hypothesis Evaluation

| Hypothesis | Verdict |
| --- | --- |
| H0: little generative value beyond known examples | rejected |
| H1: can rediscover known PO1 patterns | supported |
| H2: generates structurally novel finite candidates | best supported with caution |
| H3: generates mostly trivial or redundant structures | partially supported |
| H4: meaningful discovery requires richer machinery | not required by this bounded result |

The caution is important: many generated candidates are redundant. The engine
is useful as a triage surface, not as a discovery oracle.

## Recommendation

Keep PO1 at `partially_supported`, but record that the framework now has
generative value inside bounded finite systems.

The next worthwhile step is a blinded hostile test such as Arrow, but only if
the T35 classifier is used before domain interpretation. The right protocol is:

```text
1. encode the finite restriction systems;
2. run the T35 classifier;
3. record the structural prediction;
4. only then interpret the domain meaning.
```

This prevents domain stories from rescuing failed predictions after the fact.

## Guardrails

- T35 does not claim automated theorem discovery.
- T35 does not use machine learning or statistical pattern recognition.
- T35 does not use physics, software, voting, or logic domain heuristics.
- T35 generated structures are mathematical candidates only.
- Independent mathematical analysis is required before treating any generated
  structure as a theorem or scientific result.

## Artifacts

- `models/projection_obstruction_discovery.py`
- `models/run_t35.py`
- `tests/test_projection_obstruction_discovery.py`
- `tests/T35-projection-obstruction-discovery-engine.md`
- `results/projection-obstruction-discovery-engine-v0.1.json`
- `results/projection-obstruction-discovery-engine-v0.1-results.md`
