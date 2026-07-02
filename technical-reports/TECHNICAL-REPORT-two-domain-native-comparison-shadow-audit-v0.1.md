# Technical Report: Two-Domain Native-Comparison Shadow Audit v0.1

## Status

Internal method-hardening and witness-calibration artifact.

This report does not promote a claim, change the North Star, alter public
posture, update the claim ledger, update the roadmap, register a numbered
test, or assert new physics. It executes the next bounded artifact recommended
by `TECHNICAL-REPORT-native-comparison-regime-appendix-v0.1.md`: fill the
North Star shadow-audit spine in two mature domains and compare only the
audit structure.

The report also advances the next research action in
`Method - Research Program Guidelines.md`: run QRT Witness 2 with explicit
access profiles.

## Objective

Test whether the shared audit spine:

```text
visible fiber -> capability spread -> native absorber -> minimal enrichment
```

works across two mature domains without forcing the same surface vocabulary
or the same capability codomain.

The two domains are:

1. vector/ANN retrieval, using the prior `Witness-Run-VectorANN-v0.1.md`;
2. quantum resource theory access profiles, using the prior
   `Physics-Witness-QRT-v0.1.md` and tightening the access-profile discipline.

Expected posture:

```text
translation residue unless a domain-native comparison survives native
state completion and native theorem absorption
```

## Shared Rule Before Both Fills

Every row below must declare:

```text
Y       source structure
X       visible interface
O       observer or access profile
pi_O    observer-shadow projection
~=_X    visible equivalence
Cap     capability object
K       native capability codomain
R_K     native capability comparison
```

No witness pair may choose `R_K` after the pair is known. The absorber domain
gets its normal state variables, operation classes, equivalences, thresholds,
and theorems before any residue label is assigned.

## Domain 1: Vector/ANN Retrieval

### Claim Under Test

Vision sentence:

```text
An observer-visible stored corpus may fail to determine future retrieval
capability when the hidden system state includes index and execution data.
```

Research route:

```text
approximate retrieval envelope under fixed workload, recall, and latency
```

Expected artifact type:

```text
method calibration, not a new ANN theorem
```

Not claimed:

- no novelty in ANN retrieval;
- no claim that index-dependent recall/latency is surprising;
- no claim that corpus-only projection is the domain's canonical state.

### Known Source Domain

Known theory or mature field:

```text
approximate nearest-neighbor retrieval and vector search systems
```

Legitimate absorber state:

```text
corpus, metric, index family, index construction parameters, query-time
parameters, workload, filter policy, hardware/resource budget, and
recall/latency target
```

Native operations:

```text
index construction, search-time traversal/probing, exact scan, approximate
query execution, filtering, and benchmark evaluation
```

Native equivalences:

```text
same retrieval envelope under the declared workload and resource budget
```

Native comparison:

```text
equivalence or bounded gap of achievable recall/latency/top-k envelopes
```

Primary native-comparison regime:

```text
metric/tolerance-valued plus decision/workload-valued K
```

### Source And Shadow

Source structure `Y`:

```text
full deployed vector retrieval system state
```

Observed base or interface `X`:

```text
readable vector corpus and metadata table
```

Observer/access profile `O`:

```text
user or auditor who can inspect stored vectors and issue queries, but cannot
inspect index internals, graph layers, inverted-file assignments, construction
parameters, or hardware profile
```

Projection `pi_O : Y -> X`:

```text
forget index family, index structure, build parameters, search parameters,
workload envelope, and hardware budget; retain corpus and metadata
```

Visible equivalence `~=_X`:

```text
byte-identical corpus, vector values, identifiers, and visible metadata
```

Admissible source states:

```text
systems over the same corpus and metric with standard ANN index families and
fixed workload declarations
```

Access boundary, horizon, budget, or resource condition:

```text
single-query horizon, fixed recall target, fixed latency ceiling, fixed
hardware budget, and fixed filter/workload declaration
```

### Capability Object

Task family `T`:

```text
approximate top-k retrieval for a declared workload
```

Horizon `h`:

```text
one query execution or a declared benchmark workload
```

Capability object:

```text
Cap(y) = achievable recall/latency/top-k result envelope under the declared
query workload and budget
```

Capability codomain `K`:

```text
retrieval envelopes ordered or compared by recall, latency, and admissible
top-k result sets
```

Native capability comparison `R_K`:

```text
same envelope, or bounded envelope gap under the predeclared recall/latency
threshold
```

Why `Cap` is domain-native:

```text
ANN systems are evaluated by recall/latency behavior under index family,
parameter, workload, and resource choices.
```

Positive preservation control:

```text
exact search over the same corpus and metric collapses the index distinction;
the same corpus determines the exact top-k answer.
```

Negative non-factorization fixture:

```text
same corpus with HNSW-like and IVFFlat-like approximate indexes can expose
the same visible corpus while producing different recall/latency envelopes.
```

Capability spread over visible fibers:

```text
Spread_Cap([corpus]) =
  { exact-search envelope,
    HNSW-parameterized envelopes,
    IVFFlat-parameterized envelopes,
    other ANN-family envelopes }
```

The spread is non-singleton under corpus-only projection.

### Absorber Passes

Native state completion tested:

```text
Add index family, construction parameters, search-time parameters, workload,
filter policy, metric, and hardware budget. The capability envelope is then
domain-standard state, not residue.
```

Native theorem absorption tested:

```text
The ANN field treats the recall/latency/index-family tradeoff as its ordinary
object of study. The non-factorization through corpus-only projection is the
reason the field exists, not a new result.
```

Repair, tolerance, or threshold absorption tested:

```text
If the envelope gap is inside the declared recall/latency tolerance, the
witness demotes to no operational split. If outside tolerance, the split is
still absorbed by index/parameter completion.
```

Gauge, coordinate, basis, phase, relabeling, and representation absorption:

```text
Identifier relabeling and equivalent vector encodings must be quotiented
before comparing capability. No physics gauge issue is involved.
```

Trivial enrichment tested:

```text
pi'(y) = (pi_O(y), Cap(y))
```

This restores sufficiency but is vacuous. The domain-natural enrichment is
smaller and stronger: corpus plus metric, index, parameters, workload, and
resource budget.

### Verdict

Projection-sufficient?

```text
No, not for corpus-only X under approximate retrieval.
```

Projection-insufficient?

```text
Yes, before native state completion.
```

Minimal enrichment or repair:

```text
add the ANN system state that the native field already treats as operational:
index family, construction parameters, search parameters, workload, metric,
and resource budget
```

Residue label:

```text
translation residue, with heuristic value for detecting underdescribed
projection
```

Kill condition:

```text
If a future report claims ANN residue while omitting index and workload state,
this audit kills the claim as projection-underdescribed.
```

## Domain 2: Quantum Resource Theory Access Profiles

### Claim Under Test

Vision sentence:

```text
The same local reduced state may fail to determine a global resource
capability, but the failure is meaningful only after the observer/access
profile and free-operation class are aligned.
```

Research route:

```text
QRT Witness 2: local reduced state versus global resource preorder under
explicit access profiles O_A, O_AB, and O_ABE/reference
```

Expected artifact type:

```text
physics/resource-facing template calibration, not a new quantum theorem
```

Not claimed:

- no new quantum resource theory;
- no claim that local marginals determine global resource properties;
- no claim that QRT supports the North Star beyond translation/audit value;
- no claim that a local observer has access to global entanglement capability.

### Known Source Domain

Known theory or mature field:

```text
quantum resource theory, especially entanglement resource theory under a
declared free-operation class
```

Legitimate absorber state:

```text
quantum state on the relevant system, access profile, free-operation class,
communication rights, catalysts if admitted, asymptotic/exact regime, and
purifier or environment access if physically granted
```

Native operations:

```text
local operations, LOCC, free operations for the declared resource theory,
global operations for reference ceilings, and purifier/environment operations
only when the access profile grants them
```

Native equivalences:

```text
mutual convertibility under the declared free-operation class; local-unitary
equivalence where appropriate; equality of complete monotone data only when
that monotone family is complete for the declared fixture
```

Native comparison:

```text
resource preorder, mutual convertibility, or declared monotone-vector
comparison under fixed free operations
```

Primary native-comparison regime:

```text
resource-theoretic K, with preorder-valued comparison
```

### Source And Shadow

Source structure `Y`:

```text
rho_AB plus the declared resource-theory frame:
  access profile O,
  free-operation class F,
  exact/approximate/asymptotic regime,
  catalysts and side channels if admitted
```

Observed base or interface `X`:

```text
profile-dependent:
  X_A    = rho_A for strict local-A access;
  X_AB   = rho_AB or a tomographically complete operational description for
           cooperative A+B access;
  X_ABE  = rho_ABE when purifier/environment access is explicitly granted.
```

Observer/access profile `O`:

```text
O_A    strict local holder of A only;
O_AB   cooperative holders of A and B with the declared LOCC rights;
O_ABE  reference profile with purifier/environment access, if granted.
```

Projection or shadow map `pi_O : Y -> X`:

```text
pi_A(rho_AB) = Tr_B(rho_AB)
pi_AB(rho_AB) = rho_AB, or the declared tomographically complete operational
                state available to O_AB
pi_ABE(rho_ABE) = rho_ABE
```

Visible equivalence `~=_X`:

```text
equality of the profile-visible quantum state up to the native equivalences
declared for that access profile
```

Admissible source states:

```text
finite-dimensional bipartite states sufficient for the access-profile audit;
pure-state controls and mixed/product-vs-entangled fixtures are allowed
```

Access boundary, horizon, budget, or resource condition:

```text
fixed ownership of subsystems, fixed communication rights, fixed free
operation class, and fixed exact/asymptotic/catalytic assumptions
```

### Capability Object

Task family `T`:

```text
resource conversion, certification, or operation availability under the
declared free-operation class
```

Horizon `h`:

```text
single-shot exact conversion unless an asymptotic or approximate regime is
explicitly declared
```

Capability object:

```text
Cap_O,F(rho) = reachable resource downset or conversion envelope under the
operations available to access profile O and free class F
```

Capability codomain `K`:

```text
resource preorder or conversion-envelope object
```

Native capability comparison `R_K`:

```text
mutual convertibility under F, or equality of a declared complete monotone
certificate for the finite fixture
```

Why `Cap` is domain-native:

```text
QRT is organized around states, free operations, resources, convertibility,
and monotones; conversion envelopes are native objects, not audit inventions.
```

Positive preservation controls:

```text
1. Access-aligned local case: for O_A with only local measurements and local
   operations on A, rho_A determines the local operational statistics and
   local operation envelope.
2. Pure bipartite LOCC control: for pure states under O_AB/LOCC, the reduced
   state spectrum determines the Schmidt coefficients, which determine the
   pure-state LOCC convertibility preorder.
3. Full-state control: if X_AB includes rho_AB and F is fixed, Cap_O,F is a
   function of the full declared state and frame.
```

Negative non-factorization fixture:

```text
If one deliberately projects O_AB/LOCC capability down to the O_A-visible
rho_A, product and entangled states can share the same rho_A while having
different global resource conversion envelopes.
```

Canonical warning:

```text
That fixture is useful only as an access-mismatch diagnostic. It must not be
reported as a capability of O_A unless O_A receives B access, communication,
or a side channel.
```

Capability spread over visible fibers:

```text
Spread_Cap([rho_A]) =
  { local-A operation envelopes }                 under aligned O_A/Cap_A

Spread_Cap([rho_A]) =
  { product, entangled, catalyst-sensitive, and other global resource
    conversion envelopes consistent with rho_A }  if Cap_AB is compared
                                                   against pi_A
```

The first spread is collapsed by aligned access. The second spread is
non-singleton but reveals a profile mismatch or an intentionally local-shadow
question.

### Absorber Passes

Native state completion tested:

```text
For O_AB/LOCC capability, enrich X from rho_A to rho_AB and declare the free
operation class, communication rights, catalyst policy, and exact/asymptotic
regime. For purifier-sensitive questions, enrich only if O_ABE access is
physically granted.
```

Native theorem absorption tested:

```text
QRT already owns convertibility preorders, monotones, free-operation classes,
and pure-state/mixed-state distinctions. A local marginal not determining
global resource capability is ordinary QRT state-completion behavior.
```

Repair, tolerance, or threshold absorption tested:

```text
Approximate or asymptotic resource comparison must declare its error,
rate, smoothing, or catalytic regime before fixture selection.
```

Gauge, coordinate, basis, phase, relabeling, and representation absorption:

```text
Local unitaries and presentation choices are free/equivalent where the
declared resource theory makes them so. Basis-dependent resource theories,
such as coherence, require a separate basis declaration and are not settled
by this entanglement-oriented fill.
```

Trivial enrichment tested:

```text
pi'(y) = (pi_O(y), Cap(y))
```

This restores sufficiency vacuously. The native enrichment is the state and
resource-theory frame the field already uses.

### Verdict

Projection-sufficient?

```text
Yes for access-aligned O_A local operational capability.
Yes for O_AB when X includes rho_AB and the free-operation frame is fixed.
No for O_AB/LOCC capability if X is only rho_A.
```

Projection-insufficient?

```text
Only when the projection deliberately forgets joint state/correlation data
needed by the global or cooperative resource capability.
```

Minimal enrichment or repair:

```text
align the observer/access profile with the capability object; for LOCC
capability, include rho_AB plus the declared free-operation frame
```

Residue label:

```text
translation residue
```

Kill condition:

```text
Any future QRT witness that pairs pi_A with Cap_AB without declaring the
cross-profile question is killed as an access-profile mismatch.
```

## Cross-Domain Comparison

### Same Spine

Both domains instantiate:

```text
visible fiber -> capability spread -> native absorber -> minimal enrichment
```

Vector/ANN:

```text
corpus-visible fiber
-> recall/latency envelope spread
-> ANN index/workload absorber
-> corpus + metric + index + parameters + workload + budget
```

QRT:

```text
local-state-visible fiber
-> resource-conversion envelope spread
-> QRT state/access/free-operation absorber
-> aligned access profile + rho_AB + free-operation frame
```

### Different Native Regimes

The domains do not share the same `K`.

Vector/ANN uses a metric, tolerance, and workload envelope.

QRT uses a resource preorder and mutual convertibility under fixed free
operations.

The shared result is therefore not a theorem about one universal capability
object. It is a reusable audit procedure for checking whether the declared
visible projection is sufficient for the declared native capability object.

### What Survives Absorption

Survives:

```text
The audit spine is reusable and catches underdescribed projections before
they inflate into false residue.
```

Does not survive:

```text
No new ANN theorem.
No new QRT theorem.
No physics claim.
No cross-domain shadow-protection theorem beyond the trivial spread criterion.
```

Practical result:

```text
The strongest immediate value is an access/profile alignment rule:
Cap must be indexed to the same observer/access boundary as pi unless the
run explicitly declares a cross-profile insufficiency question.
```

## Relationship To The Dormant Cross-Domain Theorem Target

`open-problems/cross-domain-shadow-protection-theorem.md` asks whether the
same proof spine can be filled in a formal/computational domain and a
physics-facing domain.

This report gives a bounded answer:

```text
Yes as an audit spine.
No as a nontrivial theorem yet.
```

The only domain-independent mathematical statement earned here is still:

```text
Projection sufficiency means the native capability spread over visible
fibers collapses under the declared R_K.
```

That is useful as a review gate, but it is not enough to revive the dormant
theorem as an active claim.

## Next Bounded Artifact

The next safe artifact is not another broad synthesis. It should be one of:

1. an access-profile alignment lemma as a short technical note;
2. a GR causal-accessibility witness using the same template; or
3. a small executable fixture that demonstrates the access-mismatch diagnostic
   in a finite toy resource preorder without invoking new physics.

Do not update claims from this report alone.

## Governance Impact

No North Star change.

No claim-status change.

No claim-ledger update.

No roadmap edit.

No test-registry edit.

No executable model or result file.

No external-facing posture change.

## Short Verdict

The two-domain audit works as method hardening. It turns the native-comparison
appendix into a usable gate and runs QRT Witness 2 with explicit access
profiles. Both example domains honestly demote to translation residue after
native state completion and native theorem absorption.
