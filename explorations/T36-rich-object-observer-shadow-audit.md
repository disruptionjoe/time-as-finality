# T36 Rich Object -> Observer Shadow Architecture Audit

## Verdict

There is a real structure here, but only in the finite, typed,
local-to-global sense already earned by T24-T35. The defensible architecture
is:

```text
rich structured object
  -> typed access / restriction / projection / forgetting map
  -> observer-accessible shadow
  -> invariant ledger + lost-structure ledger + obstruction check
```

The strongest current form is `D1RestrictionSystem -> scalar/vector/local
observer shadow`, plus PO1 for cases where forgetting creates a finite gluing
obstruction. This is more than analogy inside TaF/T26/PO1. It is not yet a
general theorem about observation, spacetime, GU, physics, or category theory.

No literal `Observerse` term was found in the repo evidence inspected for this
audit. Treating "GU Observerse -> spacetime" as "richer GU/source layer ->
spacetime/interface shadow," the repo does not yet establish that architecture.
T27 establishes a narrower GU bridge for Witten and Nielsen-Ninomiya, and
explicitly fails for Distler-Garibaldi as a site-map boundary case.

## Closest Existing Mathematics

1. Finite CSP / constraint satisfaction: finite variables, local constraints,
   local satisfiability, and global assignment failure.
2. Sheaf and Cech obstruction theory: T13/T21 are the cleanest analogy, though
   T26/PO1 has not yet earned full sheaf language.
3. Category theory / forgetful functors: useful language, but not yet earned
   as a full category.
4. Resource theories: T33's `R = global_assignment_exists` is a Boolean
   resource; PO1 is strict resource decrease plus named forgetting.
5. Fiber bundles / gauge theory: promising but open. The repo has only an open
   problem for D1 as connection/curvature, not a built bundle.
6. Quantum Darwinism: strong neighbor for environmental record redundancy, but
   only D1 holder redundancy has executable physical traction.
7. RQM and causal sets: good conceptual neighbors for observer-relative facts
   and causal partial orders, but neither supplies TaF's D1 profile or gluing
   obstruction by itself.

## Clean Mappings

- `D1RestrictionSystem -> scalar D1`: projection collapses local profiles,
  graph, and patches under an explicit rule.
- `D1RestrictionSystem -> vector D1`: preserves site-indexed profiles but
  forgets graph and patch constraints.
- T24/T26: same vector can have different transport, so observer shadow without
  graph data is non-faithful.
- T13/T21: valid local finality sections can fail to assemble into one global
  assignment.
- T27/T29: Witten and Nielsen-Ninomiya fit the finite
  rich-to-restricted projection-obstruction pattern.
- T28/T30: CAP and Git semantic merge show the pattern is not only GU-specific.
- T2/T22/T23: global measurement state restricts to observer-access D1 view;
  decoherence/redundancy do not imply finality for every observer.

## Failed or Weak Mappings

- Distler-Garibaldi is the crucial failure: the site map is incomplete, so the
  projection is not definable inside T26.
- "Observation is a functor" is not yet valid. The repo has maps and morphism
  checks, not a proved category.
- "Observation is a pullback" is plausible for observer windows over a base
  domain, but not implemented.
- "Observation is projection" is too broad. In T1/T2 it is access-filtering
  plus profile computation; in T26 it can be scalar/vector projection; in T13
  it is restriction.
- Fiber-bundle and gauge language is underdeveloped. No connection, curvature,
  covariance, or physical gauge invariant has been defined.
- Quantum Darwinism maps only redundancy well; branch support and reversal cost
  remain physically weak or formal.

## Overclaims

- Do not say TaF has derived spacetime.
- Do not say GU and TaF instantiate the same architecture globally.
- Do not say every observation is projection-created obstruction.
- Do not say PO1 proves the original physical no-go theorems.
- Do not say D1 is a completed physical observable theory.
- Do not say full sheaf, bundle, or category theory has been earned.

## Underdeveloped Mathematics

- A category of `D1RestrictionSystem` objects with identities, composition, and
  obstruction-preservation laws.
- A first-class `ObserverShadow` object: what fields it contains, what it
  omits, and how shadows compare.
- Formal P5, informative forgetting, as data rather than metadata.
- A sheaf/presheaf upgrade with explicit restriction maps over observer
  domains.
- A resource theory with allowed operations, monotones beyond Boolean
  satisfiability, and non-monotone optimizer morphisms.
- A physical observer-access model with covariance, Lorentz sanity checks, and
  noisy quantum dynamics.

## Required Mathematics Before Serious Uptake

1. Define `Shadow(S, O)` for a rich system `S` and observer/access protocol
   `O`.
2. Prove what is invariant under all admissible shadow maps, if anything
   beyond typing and declared preserved invariants.
3. Characterize the kernel of each projection: graph data, patch data,
   transport data, inaccessible records, phase/amplitude data, or semantic
   structure.
4. Prove a PO1 representation theorem: typed projection + strict resource
   decrease + P5 iff projection-created obstruction.
5. Prove or refute a category of D1 restriction systems with composable
   observation/projection arrows.
6. Give at least one external-domain theorem not inherited from
   TaF/GU/CAP/Git examples.

## Recommended Next Theorem or Counterexample

Best next target:

**Observer Shadow Non-Faithfulness Theorem**

Statement sketch:

```text
There exist two valid rich D1RestrictionSystems S and S'
such that every one-site observer shadow, scalar projection, and vector
projection agrees, but global_assignment(S) != global_assignment(S').
```

If proved, this precisely shows what observer shadows cannot recover: gluing,
transport, and obstruction status. If false under a strengthened shadow
definition, the theorem forces the repo to define the minimum shadow data
needed for faithful global reconstruction.

A second target is the composition theorem suggested by T34: composed
projection is PO1 iff the endpoint pair satisfies AC1-AC7 and cumulative P5
names all forgotten structure.

## Anti-Hypothesis: Why This Could Be Wrong

The architecture may be attractive notation for ordinary finite CSP
projection. "Rich object -> shadow" is so general that it can fit nearly
anything unless allowed maps and invariants are tightly typed.

The obstruction may be manufactured by choosing patches after the story is
known. T35 reduces this risk but does not remove it.

The physical bridge may collapse: accessible support and holder redundancy may
reduce to standard causal access and quantum Darwinism, while branch support
and reversal cost may never become observables.

The GU comparison may be mathematically noisy. T27's positive cases are finite
abstractions; Distler-Garibaldi shows that richer category changes break the
current machinery.

The observer-shadow language may slide into interface metaphysics unless
grounded in record access, causal domains, and explicit failure conditions.

## Notes for Synthesis

Use the lens, but phrase it narrowly:

```text
TaF currently supports a finite observer-shadow architecture:
local D1 values live in richer restriction systems;
observer-accessible summaries are projections or restrictions;
obstruction arises when forgotten structure was exactly what allowed global
gluing.
```

Do not synthesize this as a universal theory of observation. The synthesis
should say: genuine finite structure inside TaF/PO1, strong overlap with
sheaf/CSP/resource mathematics, partial GU bridge, and open category/bundle/
physics upgrades.
