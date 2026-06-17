# Cognitive And Social Renderer Layer Split

## Status

Exploration. This note preserves a heterodox idea by splitting it into claim layers. Only the lower layers are currently repo-ready as formalization targets.

## Seed Idea

Human consciousness can be modeled as a local renderer over memory records, learned scripts, sensory inputs, attention, and shared social records. The body is not treated as the deepest observer in this exploration. It is treated as a high-finality participation interface: the rendered sensor/action boundary through which the observer becomes causally addressable inside the local world.

Human societies then become multi-agent record graphs where laws, identities, money, calendars, reputations, and scientific facts become hard to undo through durable shared traces.

The speculative extension is that spacetime itself may be an observer-facing compatibility interface, and black-hole horizons may expose boundaries between rendered causal domains.

## Layer 1: Cognitive Renderer

### Working Claim

A conscious human can be modeled as a record-bearing agent that renders a usable world from:

```text
memory records
  + procedural scripts
  + sensory inputs
  + attention / working context
  + inherited high-finality context
  + shared social records
  -> rendered world model
  -> rendered body-interface
```

### Why It Is Repo-Worthy

This fits the core project because Time as Finality is already about experienced temporal order and record-stabilization. The cognitive layer asks how an embedded observer integrates records into a lived sequence.

### Guardrail

This does not imply that consciousness creates physical spacetime or collapses the wavefunction.

### Candidate Formal Object

```text
Agent A = (M, P, I, H, S, C) -> (W_A, B_A)

M = memory records
P = procedures / scripts / habits
I = sensory inputs
H = inherited high-finality context
S = shared social records
C = causal-access constraints
W_A = rendered world
B_A = rendered body-interface

Rendered world and body-interface:

(W_A, B_A) = f(M, P, I, H, S, C)
```

## Layer 2: Social Finality

### Working Claim

Shared human reality can be modeled as overlapping rendered worlds stabilized by durable records and mutual constraints.

Examples:

- contracts;
- laws;
- money;
- calendars;
- reputations;
- scientific instruments and datasets;
- family stories;
- institutional archives.

### Why It Is Repo-Worthy

This layer gives the project a bridge between physical record-finality and human-scale reality. It also makes "hard to undo" vivid without claiming human belief creates matter.

### Guardrail

Social finality is real but domain-relative. A legal fact, memory, or institutional record can become very hard to undo socially while remaining different from a physical invariant.

### Candidate Formal Object

```text
Shared world W_AB =
  stable overlap between W_A and W_B
  constrained by record exchange,
  institutions,
  physical traces,
  and causal accessibility.
```

## Layer 3: Physics-Facing Causal Domains

### Working Claim

Observer-facing reality is constrained by causal access. Records can become shared only where causal domains overlap or where signals enter a common causal future.

This layer connects directly to [T7: Overlapping Causal Domains](../tests/T7-overlapping-causal-domains.md).

### Why It Is Repo-Worthy

It preserves the strongest part of the heterodox intuition: there may be no observer-available global consensus state, only locally consistent record histories that reconcile where causal access permits.

### Guardrail

Remote observation is still causal access. Photons from a distant galaxy are records in the observer's graph. Direct local participation is different, but it is not required for a remote source to become part of the observer's record-accessible world.

## Layer 4: Speculative Interface Domains

### Working Claim

Spacetime may be an observer-facing compatibility interface among causally bounded record systems.

### Why It Is Interesting

This keeps the wild idea alive without promoting it: perhaps horizons, inaccessible regions, or deeper source-to-interface maps expose limits of the observer-facing domain.

### Guardrail

This layer is not currently a physics claim. It does not imply:

- humans create spacetime;
- we do not exist in spacetime;
- black holes are traversable transportation hubs;
- remote galaxies are unrendered until visited;
- no-go theorems can be bypassed by saying "deeper layer."

Any version of this layer must pass [Rendered Interface Assumptions](../open-problems/rendered-interface-assumptions.md).

## What Remains Repo-Worthy

Promote:

- the cognitive renderer model as an open problem;
- social finality as a human-scale application of record-finality;
- overlapping causal domains as the physics-facing constraint;
- rendered-interface questions only with explicit mechanism and failure criteria.

Do not promote:

- black-hole travel;
- human creation of physical spacetime;
- mind-created matter;
- claims that ordinary astronomy is not already record access;
- "outside spacetime" language without a source-to-interface map.

## Next Useful Test

Build a small agent model:

```text
Agent A memory + scripts + inputs -> W_A
Agent B memory + scripts + inputs -> W_B
record exchange -> W_AB overlap
record correction -> revised W_A / W_B
durable artifact -> increased social finality
```

The point is not to prove metaphysics. The point is to see whether record-finality can model how lived time, identity, and shared human reality become hard to undo.
