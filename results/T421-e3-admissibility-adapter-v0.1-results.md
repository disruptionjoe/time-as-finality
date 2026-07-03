# T421 — E3 Admissibility Adapter (GU-adjacent physics ↔ TaF) — Results v0.1

- **Artifact:** `T421-e3-admissibility-adapter-v0.1`
- **Spec:** [tests/T421-e3-admissibility-adapter.md](../tests/T421-e3-admissibility-adapter.md)
- **Model:** [models/e3_admissibility_adapter.py](../models/e3_admissibility_adapter.py)
- **Test:** [tests/test_e3_admissibility_adapter.py](../tests/test_e3_admissibility_adapter.py)
- **Adversarial probes:** [_local/no-functor-probe.py](../_local/no-functor-probe.py),
  [_local/no-functor-probe2.py](../_local/no-functor-probe2.py),
  [_local/no-functor-probe3.py](../_local/no-functor-probe3.py),
  [_local/pure_reduction_probe2.py](../_local/pure_reduction_probe2.py),
  [_local/oneway_violation_probe.py](../_local/oneway_violation_probe.py)
- **Tags:** exploratory_cross_repo_adapter, D3, E3_admissibility, natural_transformation,
  krein_pseudo_hermitian_adjacency, one_way_rule, import_free, kinematic_only,
  no_claim_promotion, provisional_T_number, logged_disanalogy

> Provisional next-free T-number (repo highest was T420). TESTS.md and
> CLAIM-LEDGER.md UNTOUCHED. Recorded-tier exploratory swing. GU / pseudo-Hermitian
> QM is a two-sided structural check and adjacency ONLY — never cited as support
> for a TaF claim. No CLAIM-LEDGER entry. Ledger actions pause for Joe.

## Verdict (house vocabulary): the adapter does NOT type-check as a functor

**Recommendation: ABANDON the typed-adapter / natural-iso claim; record as a
LOGGED DISANALOGY.** The `no-functor` kill leg — the frozen spec's primary
ABANDON criterion — **FIRED**, corroborated by four independently reproduced
probes. The claimed natural transformation `η : F_TaF ⇒ F_phys` is NOT a
correspondence between the two functors; it is an equality that holds only at
2–3 hand-picked toy points and fails everywhere on the legitimate observable
class. What survives is genuinely informative but is a *disanalogy*, not an
adapter: it localizes precisely why TaF-admissibility and physics
metric-selection are different objects.

This is the honest, predeclared outcome. The frozen spec says: *"No functor: the
correspondence stays analogy (different types). → ABANDON to a logged
disanalogy (still informative: it localizes why the two E3s differ)."* That is
exactly what happened. A clean disanalogy is a real result; it is not a GO.

## What actually broke (four reproduced cracks)

The initial build reported the toy agreement as a genuine two-functor + natural
transformation. Adversarial probing shows the categorical costume does not
survive contact with the category it claims to live in. Each crack is
independently sufficient and was re-run at finalization:

1. **The "shared signature type-check" is vacuous.** `VerdictFunctor` is a
   `runtime_checkable` Protocol, so `isinstance` checks only that method *names*
   exist, not return types. A `Bogus` class whose `on_object` returns a string
   and `on_morphism` returns an integer passes:
   `isinstance(Bogus(), VerdictFunctor) == True`. So "both functors instantiate
   the ONE signature `Obs → Adm`" carries **zero** type content — it is a
   name-check any two callables pass. The build's headline "genuine type-check"
   checks nothing load-bearing.

2. **The two functors are not the same map — they agree only at cherry-picked
   points.** Scanning **500 random menus from the *legitimate* observable class**
   (K-pseudo-Hermitian operators, `A† = KAK` — the actual Krein observables),
   `F_TaF` and `F_phys` **DISAGREE 500/500** (`_local/no-functor-probe2.py`).
   `F_phys` reports `(graded, FORCED)` for essentially every irreducible
   K-observable menu (the unique Mostafazadeh metric is `K` itself, which is
   indefinite); `F_TaF` reports `DECLARED` whenever irreducible. `is_iso` holds
   nowhere in a neighborhood of the toy. The "natural transformation with iso
   components" and the "single shared knob decides both" are properties of two
   engineered points, not of the functors. This is the textbook signature of a
   loose analogy dressed as a natural transformation — and it is the K1
   falsifier the build predeclared OPEN, now fired on legitimate objects.

3. **`reads_physics = False` is behaviorally false.** `F_TaF`'s verdict is set by
   `recovery_exists(line_from → line_to)`, and those lines are `LINE_GHOST` /
   `LINE_PHYS` — the ghost-parity `P`-eigenlines. Changing the datum to generic
   `e1 → e2` flips M0 from FORCED to DECLARED (`_local/no-functor-probe.py`). So
   `F_TaF` is fed the ghost-parity eigenstructure as input; the disjoint-
   provenance flag is a decorative attribute contradicted by the code's
   behavior. The "two independent readings that agree" are one physics-loaded
   datum evaluated two ways and tuned to coincide at the P-eigenline locus.

4. **The grading-breaker `Z` is not a legitimate observable — the ambient is not
   fixed across the arrow.** `Z = diag(1,−1)` gives `KZK = −Z ≠ Z† = Z`
   (reproduced), so `Z` is NOT K-pseudo-Hermitian and `M_all = ⟨P,Z⟩` is not a
   legitimate observable menu on the fixed Krein ambient `(V, K)`. `F_phys`'s
   "unique definite metric" at M_all is the **identity**, not `K`
   (`_local/no-functor-probe3.py`). The "single observable-algebra move" silently
   swapped the ambient indefinite metric `K` for the definite metric `I`. The
   fixed Krein ambient is not fixed.

Net: there is a real pair of Python maps `ObsObject → AdmObject`, but the
substantive claim — a natural iso making TaF-admissibility and physics
metric-selection "the same object" via one shared map — holds only at engineered
points, rests on a trivial Protocol, and on a physics-loaded input mislabeled as
disjoint. That is the kill condition in the frozen spec.

## The shared signature (as designed — recorded for the disanalogy)

**Source category `Obs`.** Objects = fixed finite Krein ambient `(V, K)` plus a
chosen observable menu `M` (a unital *-algebra `= ⟨M_R⟩`). Morphisms = menu-
enlargement inclusions `M ⊂ M'`.

**Target category `Adm`.** Objects = admissibility structure
`(grading, verdict, witness)`, `verdict ∈ {DECLARED = E0, FORCED = E3}`. Morphisms
= verdict-monotone refinements (`FORCED → DECLARED` only).

**`F_TaF` (operational recoverability).** `M ↦` invariant decomposition of `V`;
`DECLARED` iff some operation in the algebra generated by `M` recovers the
separating datum (ghost line → physical line), else `FORCED`.

**`F_phys` (Mostafazadeh metric selection).** `M ↦` Hermitian pseudo-Hermiticity
intertwiners `η g = g† η` and their positive sector; `DECLARED` iff the family
pins a UNIQUE definite metric, else `FORCED`.

**The intended adapter `η : F_TaF ⇒ F_phys`.** *This is the object that failed:*
its components are isos and its naturality square commutes only on the toy
sub-poset; on the legitimate observable class it is not a natural transformation
at all.

## The worked toy — numbers (accurate, but the agreement is engineered)

`V = ℂ²`, `K = [[0,1],[1,0]]`, `P = swap = K`. Eigenlines: `(1,1)` K-norm **+2**
(physical), `(1,−1)` K-norm **−2** (ghost). `Z = diag(1,−1)` (grading-breaking,
**not** K-pseudo-Hermitian).

| Object | P central? | commutant dim | metric-space dim | F_TaF | F_phys | η "iso" | legitimate menu? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **M0 = ⟨I,P⟩** (reducible) | yes | 2 | 2 (K indefinite survives) | (graded, FORCED) | (graded, FORCED) | ✓ (engineered) | yes |
| **M_all = ⟨P,Z⟩ = M₂(ℂ)** (irreducible) | no | 1 | 1 (**metric = I, not K**) | (ungraded, DECLARED) | (ungraded, DECLARED) | ✓ (engineered) | **NO — Z not K-pseudo-Hermitian; ambient swapped** |
| **M1 = ⟨I,P,U⟩** (grading-preserving control) | yes | 2 | 2 | (graded, FORCED) | (graded, FORCED) | ✓ | yes |

- The M0 agreement (both FORCED) is **measure-zero**: the datum lines `(1,±1)`
  are exactly the P-eigenlines, the special alignment that makes a reducible
  algebra fail to recover. Generic reducible menus *recover* (DECLARED on the TaF
  side) while `F_phys` still says FORCED — 400/400 disagreement on random
  single-Hermitian-generator menus (`_local/pure_reduction_probe2.py`).
- The M_all agreement is spurious: `Z` takes the state off the fixed Krein
  ambient, so this is not a move within `(V, K)`.

### Test suite status

`python -m pytest tests/test_e3_admissibility_adapter.py -q` → **27 passed**.
The tests are all TRUE — but they only assert properties *at the toy objects and
over the single toy arrow*. They do not (and given the design cannot) assert the
functor property on the legitimate observable class, which is where it fails. The
green suite is consistent with the disanalogy: it certifies the toy arithmetic,
not the adapter.

## Six kill legs — status at finalization

Five adversarial passes were run (the frozen spec's four kill criteria + a
dynamical-overreach pass); the `no-functor` pass subsumes both the K1
naturality falsifier and the K5 thin-functor vacuity leg, and K3 sign-inversion
was checked build-internally. Mapping to the predeclared six legs:

- **K1 / no-functor — FIRED (breaks, conf ≈ 0.82).** Reproduced: vacuous
  Protocol, 500/500 disagreement on legitimate menus, physics-loaded datum,
  ambient swap. This is the ABANDON trigger. → **logged disanalogy.**
- **K5 / thin-functor vacuity — FIRED (subsumed by K1).** The `Bogus` probe
  shows the type-check is a bare name-check; the "categorical content above the
  monotone-verdict bar" is not established off the two toy points.
- **K2 / pure reduction — PARTIAL (conf ≈ 0.62).** Does NOT fully fire:
  recoverability is a *demonstrably distinct* predicate (400/400 disagreement),
  so "TaF adds nothing" is false — it is not a clean reduction. BUT the grading
  axis collapses to a single Schur/commutant invariant read twice
  (`metric_space_dim == commutant_dim` on every self-adjoint toy menu), so the
  "same knob" framing is one representation-theory invariant, not cross-repo
  content. The non-redundant half (recoverability) secures agreement only on the
  engineered measure-zero locus. Cross-repo content is thinner than claimed.
- **K3 / sign inversion — did not fire.** Direction reducible→FORCED,
  irreducible→DECLARED is consistent with standard superselection theory; the
  toy does not invert it. (This was never the weak point.)
- **K4 / one-way violation — did NOT fire (survives, conf ≈ 0.90).** GU/pseudo-
  Hermitian physics is adjacency and object-of-study only. Poisoning probes
  confirm: patching the metric machinery to raise leaves all `F_TaF` verdicts
  unchanged; mutating `K_FORM` from the Krein form to identity leaves every
  `F_TaF` verdict identical. No GU claim is load-bearing for any TaF conclusion.
  The one-way rule held cleanly. (Notably, this is *because* the two sides are
  independent — the same independence that makes them disagree.)
- **K6 / prior art — PARTIAL (conf ≈ 0.62).** No prior statement of the *exact*
  Krein-specialized verdict-functor adapter, so the strict kill does not fire.
  BUT the general connection it trades on — operational restriction ↔ accessible
  observable algebra ↔ superselection-sector structure ↔ resource theory — is
  solidly prior art (Bartlett–Rudolph–Spekkens, RMP 79, 555 / quant-ph/0610030;
  the taxonomy reference itself files E3's home as superselection + WAY +
  resource theory of asymmetry). The genuinely-new margin is confined to the
  indefinite-metric/Krein specialization + the cross-repo packaging — a thin,
  decoration-level margin, and it is exactly the packaging that broke. (Confirmed
  the strongest near-miss, arXiv:2606.19678, was a confabulated summary; a
  neutral re-fetch shows it contains no declared/forced, metric-operator,
  pseudo-Hermitian, Krein, or ghost-parity content — it is a fusion-category
  distinguishability result, an operational endpoint, not the connection.)
- **Dynamical-overreach — did NOT fire (survives, conf ≈ 0.95).** The build
  never asserted the dynamical identity: no `Adm_dyn`, no source action `S`, no
  `[P_ghost, S] = 0`, no Hamiltonian. The honest kinematic ceiling was respected
  throughout; the dynamical lift is correctly left gated on GU's unbuilt source
  action and a TaF dynamics, which neither repo owns.

## HOLD / BREAK map

**BREAKS:**
- **The typed adapter / natural iso (headline claim).** Not a functor
  correspondence — agreement is confined to engineered measure-zero points; the
  Protocol type-check is vacuous; `M_all` leaves the fixed ambient.
- **"Single shared knob decides both readings."** Off the toy, centrality of `P`
  does not co-decide the two verdicts; on legitimate menus they diverge.
- **Provenance-disjoint agreement.** The agreement is manufactured by feeding
  `F_TaF` the ghost-parity eigenlines, not two independent readings converging.

**HOLDS (the salvage — a real, informative disanalogy):**
- **The one-way rule (K4).** Clean and independently verified — no GU claim is
  load-bearing. Import-free in the strong sense.
- **Recoverability is a genuinely distinct predicate** from Mostafazadeh
  metric-selection (K2 does not fully fire). So this is *not* a pure reduction of
  TaF to physics either — the two E3s are different objects, and we can now say
  exactly how: they coincide only on the ghost-parity-eigenline / all-irreducible
  locus and diverge generically.
- **The kinematic ceiling was honored.** No dynamical overreach; the build's
  self-imposed bound was accurate.
- **The localization is the deliverable.** "Why the two E3s differ": physics
  metric-selection tracks whether the observable family pins a definite metric
  (a Schur/commutant fact about the *algebra*); TaF admissibility tracks whether
  an operational datum is *reachable* (a fact about the algebra's *action on a
  specific line*). These agree only when the datum is aligned to the grading and
  the ambient metric is the one the family pins — a coincidence, not a functor.

## Honest bottom line

The swing set out to test whether TaF operational-admissibility and physics
metric/grading selection *type-check as one object*. Honestly tested, they do
**not**. The apparent adapter was a pair of independently-correct maps tuned to
coincide at two engineered points; on the legitimate observable class they
disagree 500/500, the type-check is vacuous, and the toy's decisive move leaves
the fixed Krein ambient. The `no-functor` kill — the frozen spec's primary
ABANDON criterion — fired.

**Recommendation: ABANDON as a typed adapter; keep as a LOGGED DISANALOGY.**
This is a legitimate result, not a null one: the tri-repo interface-signature
contract now has one honestly-refuted candidate, with a precise account of the
obstruction (operational-reachability ≠ metric-selection off the eigenline
locus; the Krein observable class breaks the naturality). The one-way rule held,
no claim moves, and the dynamical identity remains correctly gated. Do not
promote; ledger pauses for Joe.

## Reproduction

```bash
python -m pytest tests/test_e3_admissibility_adapter.py -q          # 27 passed (toy-only)
python -m models.e3_admissibility_adapter                            # prints the toy numbers
PYTHONPATH=. python _local/no-functor-probe2.py                      # 500/500 disagree (legit menus)
PYTHONPATH=. python _local/no-functor-probe3.py                      # Z not K-pseudo-Hermitian; M_all metric = I
PYTHONPATH=. python _local/pure_reduction_probe2.py                  # recoverability distinct (400/400) but grading axis = commutant invariant
PYTHONPATH=. python _local/oneway_violation_probe.py                 # one-way rule holds under poisoning
```
