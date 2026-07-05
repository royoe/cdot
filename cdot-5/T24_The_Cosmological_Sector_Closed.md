# T24 — The Cosmological Sector, Closed: Four Counting Laws, One Recurring Failure

*Status: closing ledger, in the same role cdot-4's `T23_The_Failed_Tests.md` played —
consolidating a line of work that is being set aside, honestly and in detail, rather
than continuing to patch it. Written 2026-07-05. Supersedes, for the purpose of
deciding where to spend effort next, T23 (Autocatalytic Counting) and the entire
cosmological thread of T16 (CMB Power Spectrum). Neither of those documents is deleted
or edited into silence — they remain the detailed record of what was tried — but both
are now closed chapters, not active open items. cdot-4 and cdot-5's T1–T22 stand as
written; this document only concerns premise 2 (the counting law) and its downstream
consequence, the redshift–distance–CMB sector.*

---

## 0. What This Document Decides

Four successive constructions for premise 2 — the rule that sets how the local speed
of light $c$ depends on cosmic history — have now been tried, fit against data, and
failed, each in a way that took real, non-trivial work to expose (this is not a story
of laziness or sloppiness; every failure below was caught by deliberately checking a
consequence nobody had checked yet). After the fourth failure, a structural pattern is
visible across all four, and a **premise-3-and-4-level diagnosis** (§2) shows that the
sector's hardest failure — the CMB — was never actually a premise-2 problem in the
first place. Continuing to invent replacement counting laws is very unlikely to
succeed where four attempts already haven't, for reasons that have nothing to do with
which specific counting law is tried next. This document records that decision and its
reasoning, so it does not need to be re-derived the next time someone is tempted to try
a fifth.

**What is and is not affected.** This closes the cosmological (premise-2,
redshift–distance–CMB) sector only. The connecton local-gravity program — T14, T15,
T17, T19, T22 — is explicitly unaffected (§3) and remains the live, working part of
this project.

---

## Part I — The Four-Iteration Arc

### I.1 — Occupancy counting (cdot-4's premise 2): excluded

$c\propto N\propto R^n$, $N$ = particles occupying a horizon of radius $R$. Excluded by
the DESI DR2 BAO Alcock–Paczyński test for **every** exponent $n$: $\chi^2\approx94$/6
at the model's own preferred $n=3$ (volume), and a full family-level scan over $n$ never
does better than $\chi^2\approx35$, requiring an effective $nP\approx10.5$ against the
model's own $n=3,P=2$. Full account: cdot-4 `T23_The_Failed_Tests.md` §1.1–§1.3. This
is the exclusion cdot-5 was created to fix.

### I.2 — Autocatalytic counting: fit, then failed at high $z$

Premise 2 replaced with connectivity rather than occupancy: $dN/dR=N/L$ for a fixed
length $L$, giving $c\propto e^{R/L}$ (T23 §3). Fit to the four clean DESI galaxy bins
alone: $\chi^2=13.2/7$, competitive with $\Lambda$CDM's $10.5/6$ (T23 §4) — a genuine,
non-trivial success on the data it was fit to. Extended to the two excluded tracers
(QSO, Ly$\alpha$, $z>1.3$): overshoots badly, $\chi^2\approx139/10$ on all six bins
(T23 §5) — a clean, decisive high-$z$ failure.

### I.3 — Percolation-broken two-phase law: fixed DESI, then failed at the CMB

Patched with a percolation transition — subcritical/occupancy counting above a break
$z_*$, supercritical/connectivity counting below — introducing three more parameters
($z_*=1.201$, $q=1.37$, plus the offset $D_0$) on top of $L$. Fit to all six DESI bins:
$\chi^2=6.8/8=0.85$ (T23 §6) — an excellent fit, and this became the working cdot-5 law,
threaded through Core Principles and every T1–T22 rewrite.

Extended to recombination ($z\approx1090$) for the CMB first-peak test: $\ell_1\approx
1674$, a $7.6\times$ miss (T16). A follow-up decomposition (independently reviewed and
verified, `REVIEW_NOTE_T16_First_Peak.md`) reattributed most of this miss to the
baryon-loading value $R\approx680$, not the counting law's extrapolation — $R$ alone
would need to shrink $\sim63\times$ to fix the position, and independently fails an
extrapolation-free peak-*height* test by $\sim400\times$. This looked, briefly, like
good news for the counting law specifically ("substantially exonerated" on this number)
— but see I.4: the $R\approx680$ problem itself turned out to be a premise-1/3/4
problem, not a premise-2 one, so this "exoneration" didn't actually rescue anything.

### I.4 — The recombination-physics investigation: a genuine improvement, then a genuine, unresolved split

**$R\approx680$ retracted.** Its derivation ("$\rho_b,\rho_\gamma\propto c^2$
identically, so $R$ is epoch-invariant") is void — a trivial unit-conversion tautology,
not a real statement about how a real plasma's densities evolve with cosmic time. An
imported $\Lambda$CDM "hot bath cooling" alternative ($T_\text{rec}=T_0(1+z)$) was
tried and rejected — it imports an adiabatic-expansion mechanism this static ($a=1$)
model doesn't have.

**A corrected, better-grounded value: $R_\text{rec}\approx20.6$.** Derived from
baryon-number conservation ($n_b=$const, forced by $a=1$) and, symmetrically,
photon-number conservation ($n_\gamma=$const), combined with this model's own
already-established Stefan-Boltzmann $c$-dependence ($a_\text{rad}\propto c^{-3}$,
T18). This forces $T_\text{eff}(t)\propto c(t)$ and $R(t)\propto c(t)$, cross-checked
against T18's *independently*-derived stellar $T_\text{eff}\propto c^{+1}$ result (same
exponent, unrelated physics — a real consistency signal) and independently re-audited
via an explicit constant-by-constant $c$-dependence check
(`UPDATE_NOTE_Constants_c_Dependence_Audit.md`), which confirmed it on firmer footing.
This closed most of both CMB gaps: position $7.6\times\to1.35\times$; height
$\sim400\times\to\sim13.5\times$. **This was real, verified progress, achieved by
following the model's own premises rather than importing an outside mechanism.**

**But checking $z_\text{rec}$ against the model's own Saha equation broke it again.**
$z_\text{rec}=1090$ had been a *borrowed* number throughout — never actually derived
from this model's own recombination physics. Deriving it self-consistently, using the
*same* $T_\text{eff}\propto c(t)$ relation that gave the good $R_\text{rec}$, in the
ionization-threshold (Saha) equation: $z_\text{rec}\approx2\times10^6$ — not 1090, off
by roughly $1700\times$. Independently re-derived by two separate lines of work (this
document's author and a parallel session) with closely matching numbers, and stress-
tested: $n_b$/$\eta$ is a weak, purely *logarithmic* lever ($10^{12}$ in $\eta$ moves
$z_\text{rec}$ by less than one order of magnitude) — it cannot be the fix. The actual
driver is the large, fixed ratio $X_0\equiv E_\text{ion}^{(0)}/k_BT_0\approx5.8\times
10^4$ combined with the *exponent* relating the ionization threshold to $c(t)$.

**An alternative convention (treating the ionizing photons as already frozen/decoupled,
using fixed $T_0$ rather than the evolving $T_\text{eff}(t)$) gives $z_\text{rec}
\approx1095$** — remarkably close to the observed $1090$, and a mathematically clean
result (this model's $E_\text{ion}\propto c^2=E_\text{ion}^{(0)}/(1+z)$ exactly
reproduces $\Lambda$CDM's own "$T$ rises as $(1+z)$" leading term when compared against
a fixed reference). **But this same "frozen" convention, applied consistently to the
bulk photon energy density needed for $R_\text{rec}$, gives $R_\text{rec}\sim2\times
10^{-5}$** — catastrophically wrong in the opposite direction from the good result
above. **No single, consistent convention for the photon sector gives both a sensible
$R_\text{rec}$ and a sensible $z_\text{rec}$ at the same time.** A physically plausible
resolution (bulk plasma stays thermally coupled; the specific ionization-balance
photons decouple suddenly, before full photon decoupling — real recombination has
exactly this kind of near-decoupling behavior via Ly-$\alpha$ escape) was identified but
never completed: it requires comparing the recombination/photoionization rate to the
horizon growth rate $H^\text{hor}(t)$ at the candidate epoch, and that calculation was
never finished.

**This is the load-bearing finding of the whole arc, and it is addressed in full in
§2 below: none of the ingredients in this split (§I.4) reference the counting law at
all.**

### I.5 — Hyperbolic-holographic geometry: the mechanism itself failed, the replacement failed differently

A direct check of the percolation-broken law's own microscopic mechanism
($dN/dR=N/L$ via "transitive reachability") found it **geometrically impossible**: a
short-range, dense connecton network is space-filling (giving the volume law, not the
exponential); a sparse multiplicative tree cannot embed in fixed-density flat 3-space
(exponential node-count outruns cubic volume within a few hops). This is a real,
structural no-go, not a data-fit problem — the mechanism cdot-5's entire premise-2
replacement rested on does not actually work as stated.

**Proposed replacement**: posit that the connecton relation-space has intrinsic
*hyperbolic* geometry $H^d$, where boundary area $A(R)\propto\sinh^{d-1}(R/r_c)$
naturally interpolates between a flat power law (small $R$) and the exponential law
(large $R$), with the "percolation transition" reinterpreted as a smooth curvature
crossover. This derives the counting law's *functional form* from geometry rather than
positing kinetics — a genuine improvement in *principle* over the refuted autocatalytic
mechanism.

**In practice, it does not work either.** A direct fit to all six DESI bins under this
picture gives $\chi^2/\text{dof}\approx30$ — a large regression from the
percolation-broken law's $0.85$. The only way to recover a good fit is to fit galaxies
alone and treat the QSO/Ly$\alpha$ bins as likely data artifacts — discarding the two
data points that disagree, on a construction whose only prior selling point was fitting
DESI. The one new free parameter (the geometry's dimension $d$) is **over-determined**:
the crossover location implies $d\approx2$; the DESI subcritical index $n\approx1.35$
implies $d\approx2.35$ if $c$ tracks boundary area, or $d\approx1.35$ if it tracks bulk
volume — three incompatible readings from the same construction, with no way to
reconcile them. And critically, **it still does not fix the CMB**: the sharp-break
reading overshoots ($\ell_1\approx298$, using the corrected $R_\text{rec}$); the
smooth, extreme-$z$-crossover reading *undershoots* ($\ell_1\approx90$–$100$) — the
observed $220$ sits between two versions of the same mechanism, tunable to either side,
which is a sign of a free parameter with no independent constraint, not evidence for
the mechanism.

---

## Part II — The Diagnosis: This Was Never a Premise-2 Problem

The single most important finding of the entire arc is in §I.4, and it is worth stating
starkly. The $R_\text{rec}$/$z_\text{rec}$ split uses exactly these ingredients:

- $E_\text{ion}(t)\propto c(t)^2$ — T7's Rydberg-like scaling (premises 3, 4; EM-forced
  $\epsilon_0\propto c^{-1}$).
- $n_b(t)=$const, $n_\gamma(t)=$const — both forced by premise 1 (static $a$) plus
  ordinary conservation, with no counting-law input.
- $a_\text{rad}\propto c^{-3}$ — T18, from invariant $\hbar,k_B$ plus explicit $c$ in
  the mode-density integral (premises 3, 4 again).
- $1+z=(c_0/c_e)^2$ — T2, the redshift law, explicitly and repeatedly confirmed
  independent of the counting law throughout every T-document in this project.

**None of these reference premise 2.** The calculation never needs to know whether
$c(t)$ follows occupancy counting, autocatalytic counting, the percolation-broken law,
or hyperbolic-holographic counting — it only uses the *ratio* $c_0/c_e$ through $z$,
which is fixed by the redshift law alone. This means **the $R_\text{rec}$/$z_\text{rec}$
inconsistency would appear identically under cdot-4's original occupancy law**, or under
any future replacement for premise 2. It is rooted in premises 1 (static geometry), 3
(invariant mass), and 4 (photon frequency conserved in flight) — the three premises
common to every version of this model tried so far, cdot-3 through cdot-5.

**Consequence for "revert to cdot-4 and solve the CMB independently of DESI":** this
does not escape the problem. It removes DESI's already-failed constraint from
simultaneous consideration, which may be worth doing for other reasons, but it leaves
the actual CMB obstruction completely untouched, because premises 1, 3, and 4 are
identical between cdot-4 and cdot-5. cdot-4 never derived $z_\text{rec}$ from its own
Saha equation either — it also just borrowed $1090$. Had anyone checked it there, the
same split would have appeared.

**The pattern across all four iterations, named plainly.** Each successive
construction fixed the immediately preceding objection and introduced a new,
structurally similar failure: a free parameter that turned out to be over- or
under-determined by the very data meant to constrain it (I.3's four-parameter
percolation law "worked" until the CMB; I.5's dimension $d$ is pulled three
incompatible ways at once), or a downstream inconsistency in a calculation nobody had
run yet (I.4's split). Four iterations without convergence toward a single, stable,
internally consistent picture is a signal about the underlying structure, not a run of
bad luck. Continuing to iterate on premise 2 specifically has been tried four times and
has not once produced a version of the model that survives contact with a calculation
nobody had checked yet.

---

## Part III — What Survives, Untouched by Any of This

The connecton local-gravity program has been checked against every one of the four
iterations above and has not needed rescuing once, because it is genuinely separable —
it needs a connecton sea and a local horizon/acceleration scale $g_\dagger$, not the
specific cosmological $c(t)$ history:

- **T14** — diffusion-sourced Newtonian gravity from foam scattering; the RAR closure
  derived from connecton indistinguishability.
- **T15** — the RAR closure's 0.020 dex fit to McGaugh-Lelli-Schombert data, unaffected
  across every counting-law change tried.
- **T17** — the M-$\sigma$ relation and the dynamical-selection/Lorentz-filter
  morphology chain.
- **T19** — disk vertical flattening from the coherent $B_c$ field, tied to the same
  rotation-curve physics with no new parameter.
- **T22** — the river/flow derivation of Newtonian gravity and PPN phenomenology
  ($w=\sqrt{2GM/r}$), the RAR-vs-planetary-ephemeris confrontation.

This is where the project's genuinely interesting, still-open, and *tractable* problems
live: the un-derived entrainment/depletion law (T22 item 1, merging what were three
separate open items across T14/T15/T22); pinning which length sets $g_\dagger$ (T6/T14);
the attractor-convergence proof (T14/T17). None of these have failed a check the way
premise 2 has, four times running.

---

## Part IV — Conclusion and Recommendation

**What cannot stand.** Every version of premise 2 tried in this project — occupancy
(cdot-4), autocatalytic connectivity, the percolation-broken two-phase law, and
hyperbolic-holographic geometry — has failed a decisive, non-trivial check. The CMB
failure specifically is not a premise-2 problem and will not be fixed by inventing a
fifth counting law; it traces to premises 1, 3, and 4, which are common to every
iteration of this model, including cdot-4.

**What survives.** The connecton local-gravity program (T14, T15, T17, T19, T22),
confirmed separable and unaffected across all four iterations above.

**Recommendation.** Redirect effort to the local-gravity program's own open items
(the entrainment law is the single most consequential one, per T22's own accounting).
The cosmological/redshift-distance/CMB sector is closed for now. If it is ever
revisited, the productive move is not another counting law — that has been tried four
times — but a direct, principled examination of premise 1 (is static geometry really
required?) or premise 4 (is photon frequency really exactly conserved in flight, or
could a controlled, motivated relaxation supply the dilution mechanism that both
$n_b$ and $n_\gamma$ currently lack under $a=1$?). Either of those would be a
foundational move addressing the actual mechanism behind the recurring failure, not a
fifth patch to its symptom.

---

## Cross-References

- **cdot-4 `T23_The_Failed_Tests.md`** — the closing ledger this document's arc
  continues from; not edited, referenced throughout Part I.
- **T23 (Autocatalytic Counting)** — the detailed record of I.2–I.3 and the open items
  that were live before this closure; superseded for prioritization purposes, not
  deleted.
- **T16 (CMB Power Spectrum)** — the detailed record of I.3's CMB test and I.4's
  recombination-physics investigation; superseded for prioritization purposes, not
  deleted. Its own Open Questions section should be read as closed pending the
  foundational move described in Part IV, not as a live to-do list.
- **T14, T15, T17, T19, T22** — the surviving program (Part III); unaffected, active.
- **Core Principles** — premise 2's status should point here for the overall verdict;
  premises 1, 3, 4 are unaffected in their stated form but are now flagged as the
  actual locus of the CMB obstruction, per Part II.
