---
artifact_type: exploration
status: active
governance_role: cross_repo_salvage_and_restart_packet
claim_refs:
  - D1
  - PO1
  - MTI
  - S1
depends_on:
  - ../gu-source-action/ADAPTER-DISCRIMINATOR-GOAL-2026-06-30.md
  - ../gu-source-action/COMPENSATOR-ADAPTER-GOAL-2026-06-30.md
  - ../gu-source-action/SPECTRAL-SECTION-CARRIER-GOAL-2026-06-30.md
  - ../gu-formalization/docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
  - ../gu-formalization/canon/source-action-seiberg-witten-RESULTS.md
created: 2026-06-30
---

# GU Source-Action Salvage And TaF Restart

## Purpose

This packet records the handoff decision after the short `gu-source-action`
run and starts the next `time-as-finality` lane without promoting any claim.

The user-level correction was:

```text
We were supposed to be in the finality repo. The source-action sandbox may no
longer be needed. Check whether anything should fold back into GU formalization,
then restart in Time as Finality.
```

## Quick Assessment Of `gu-source-action`

The sandbox is not currently needed as an active construction repo.

The recent results are useful as a closure pattern, not as standalone machinery:

| result | plain-English lesson | fold into `gu-formalization`? |
|---|---|---|
| adapter discriminator | simple structured non-metric probes stay zero; arbitrary dense H-linear noise can move the index but has no source carrier | yes, as a short static-adapter closure note |
| compensator adapter | shapes built only from `E = Q M_D Pi_RS` cancel, damp, or twist the escape channel without producing an index/source signal | yes, as evidence for the "obvious compensator shapes fail" bucket |
| spectral-section carrier | static sections of `D_Sigma` are either symmetric or fixed zero-mode projector choices | yes, as a static spectral-section absorber warning |

Do not fold the sandbox modules themselves unless `gu-formalization` wants a
regression suite for this exact closure class. The parent repo already has
stronger source-action tests, including Seiberg-Witten/BV material. The useful
import is the synthesis:

```text
Static adapters generated from the current GU bridge data are exhausted into
four failure classes: zero signal, arbitrary perturbation, fixed-projector
absorber, or RS escape decoupling.
```

Recommended parent-repo artifact:

```text
gu-formalization/explorations/firewall-and-two-geometries/static-adapter-closure-note-2026-06-30.md
```

Recommended parent-repo claim posture:

```text
This is not a new no-go theorem. It is a bounded closure note for the static
adapter class tested in the sandbox.
```

## TaF-Relevant Lesson

The most portable lesson is not GU-specific.

Both the temporal-issuance `E097` result and the GU spectral-section pass hit
the same absorber pattern:

```text
An apparent source-side or finality-side distinction can be fully absorbed by a
fixed compatibility predicate, fixed projector, fixed-H state space, or fixed
latent source plus changing access.
```

In Time as Finality language, this is a fixed-admissibility absorber.

It matters because many attractive TaF claims have this shape:

```text
local observers see coherent records;
some records are rejected or stabilized;
therefore there may be a source-side finality mechanism.
```

The absorber says:

```text
Maybe not. A fixed admissibility structure plus changing access may reproduce
the behavior without any new source-side dynamics.
```

## Restart Target

The next meaningful TaF goal should make this absorber reusable.

Proposed goal:

```text
Build a fixed-admissibility absorber template for Time as Finality.

Given a candidate finality or issuance witness, ask whether the observed record
admission/rejection/stabilization behavior is already reproduced by:

1. a fixed compatibility predicate;
2. a fixed projector or fixed-H state space;
3. a fixed latent source with changing observer access;
4. ordinary schema/constraint checking;
5. ordinary causal order plus a declared value predicate.

If yes, demote the witness to reconstruction-layer discipline unless it supplies
a nonfixed admissibility datum.
```

## First Executable Shape

Create a small model, probably under `models/`, that accepts a finite trace:

```text
records
observer projections
candidate accept/reject decisions
compatibility predicate family
access schedule
```

and emits:

```text
fixed_predicate_absorbs: true/false
fixed_projector_absorbs: true/false
fixed_latent_access_absorbs: true/false
nonfixed_admissibility_needed: true/false
residue_label
```

The model should not assert new physics. Its job is to prevent false positives.

## Why This Is The Right Start

This repo already knows how to run absorber passes. The gap is that the
fixed-admissibility pattern is recurring across repositories:

- temporal-issuance clock-free cadence;
- GU static spectral sections;
- TaF observer-shadow / capability-projection witnesses;
- any future record-admission story that risks mistaking fixed constraints for
  source-side finality.

Turning that pattern into a reusable TaF test would advance the repo more than
another broad essay.

## Not Claimed

This packet does not claim:

- `gu-source-action` is worthless;
- GU has a final no-go theorem against all adapters;
- Time as Finality is strengthened;
- fixed admissibility explains all record-finality behavior;
- source-side finality is impossible.

It only records that the next TaF step should explicitly defeat fixed
admissibility before treating any coherence, section, or record-filtering result
as source-side residue.
