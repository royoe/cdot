# Research Notes — The Path to cdot-7's Foundation

*This document exists so `Foundation.md` can stay clean of history. Everything here is
context, motivation, and a record of dead ends. Cross-references to `cdot-1` through
`cdot-6` live here, not there.*

---

## 1. Why cdot-7 Starts Over, Rather Than Patching cdot-6

cdot-6 (`cdot-6/Foundation.md`, `cdot-6/ResearchNotes.md`) built a framework on
Atkinson's (1963) local closure — position-dependent postulates for $c_r(\psi)$ and
$\mu_r(\psi)$ that exactly reproduce single-mass GR predictions — extended by a Machian
cosmological closure for $c(t)$, sourced by the horizon's own enclosed mass. Two
decisive results closed it out in the same session it was built:

1. **The LLR check.** Redoing cdot-4's T8-style self-consistent Lunar Laser Ranging
   calculation for cdot-6's own relations found that even with $G$ and the reference
   mass invariant (removing orbital expansion), *any* genuinely evolving $c(t)$ produces
   an irreducible light-travel-time bookkeeping signal at the same order as the bound
   excludes — not fixable by any local mass or clock law, since the exposure is
   structural (`cdot-6/Foundation.md` §3.6, `cdot-6/ResearchNotes.md` §7). A specific
   mass-scaling exponent, $s=+1/2$ (with $G$ exactly invariant), was found to cancel
   this exactly — but at that point in cdot-6, it was a *fitted* number with no
   independent motivation, exactly the "selected because it works, not derived" move
   this whole project line has tried to avoid (T8's own standing self-criticism,
   `cdot-4/T8_Gravitational_Constant.md`).
2. **The MOND-mechanism check.** Foundation §4's conjecture — that a test particle
   simultaneously feels a local $\psi_\text{loc}$ and a cosmological background
   $\psi_h$, with MOND emerging where they become comparable — was checked *exactly*
   using Atkinson's own postulates and found to fail categorically, not just for the
   specific additive combination tried: for *any* smooth function combining
   $\psi_\text{loc}(r)$ and $\psi_h$, the force at large $r$ is $\propto1/r^2$,
   because the local mass's contribution always vanishes linearly in $1/r$ and any
   smooth function of a linearly-vanishing perturbation gives a quadratically-vanishing
   force. Three specific combination attempts (additive, nested/ambient-$c$,
   self-referential) all failed for this identical structural reason
   (`cdot-6/Foundation.md` §4).

The second result is the more important one: it shows Atkinson's entire strategy — local
dynamics as a function of a potential-like scalar $\psi$ — cannot produce MOND by
construction, regardless of cleverness in combining local and cosmological
contributions. The right fix, identified but not built out in cdot-6, is that MOND is
structurally a statement about the *field* ($|\nabla\Phi|$ vs. a reference acceleration),
not the *potential*'s value — matching how real MOND/AQUAL theories are actually built.
**cdot-7 acts on that finding directly: it drops Atkinson's local closure entirely and
adopts an AQUAL-spirit modified-gravity postulate instead**, and separately settles the
LLR question by *adopting* $s=+1/2$ (with $G$ invariant) as an exact premise rather than
treating it as a number to be justified after the fact.

---

## 2. What Atkinson Contributed, and What's Actually Kept

Atkinson's (1963) local closure itself — `references/Atkinson63.md` still holds the
citation notes — is not carried into cdot-7 at all; §1 above is why. What *is* kept from
cdot-6, because it never depended on Atkinson in the first place:

- **The horizon/mass-radius machinery** (`cdot-6/Foundation.md` §3.2): $\dot R_h=c(t)$,
  $M_h=\frac43\pi R_h^3\rho$, and the Sciama-type $c\propto R_h$ closure. This was always
  a separate track from Atkinson's rational-function attempt (`cdot-6/Foundation.md`
  §3.3, the rejected direct substitution) — it survives cdot-6's closure unscathed and
  is cdot-7's §2 verbatim in substance, restated fresh.
- **The relational, not-measured status of $c_0,c_z$** (`cdot-6/Foundation.md` §3.1).
  Also independent of Atkinson; carried into cdot-7 §2.3.
- **The general LLR-exponent formula**, $E=-2s-g+1$, derived in `cdot-6/ResearchNotes.md`
  §3.2 while checking whether PV's own combined package (not just cdot-4's tested
  hybrid) survives LLR — this is pure classical mechanics (angular momentum
  conservation) plus the Rydberg formula, uses Atkinson nowhere, and is exactly what
  justifies cdot-7 §5.1's exact cancellation at $(g,s)=(0,\tfrac12)$.

---

## 3. The $s=+1/2$ Decision: From Fitted Number to Adopted Premise

`cdot-6/ResearchNotes.md` §7.2 and the exchange that followed it worked out, in order:

1. $g=1-2s$ is a full one-parameter family that cancels the LLR range-rate signal, not
   a single point — but the independent, much tighter *direct* $\dot G/G$ bound pins $g$
   to within $\sim0.4\%$ of zero, collapsing the family to a thin sliver around
   $s\approx0.5$.
2. Choosing $s\ne0$ is not a free, local choice: cdot-6's imported redshift relation,
   $1+z=(c_0/c_z)^2$, implicitly assumed $s=0$; any other $s$ changes the redshift
   exponent to $s+2$ and propagates into the whole cosmological sector (age, distance,
   deceleration). cdot-7 §3.3, §5.2 carry this through explicitly for $s=\tfrac12$
   (exponent $\tfrac52$) rather than leaving it implicit.
3. A principled (not fitted) derivation of the mass-transformation law, attempted via a
   guessed conformal factor $\Omega=c_0/c_z$ and the standard scalar-tensor "$m\to
   m/\Omega$" rule, gave $s=+1$ — which does *not* cancel the LLR signal (`cdot-6`
   session log, entry 16) — so no independently-motivated derivation was in hand by the
   time this was revisited.

Given that, the author's decision (2026-07-07) was to stop treating $s$ as a number to
be justified and adopt $s=+\tfrac12$, $g=0$ as an exact premise — explicitly flagged in
`Foundation.md` §3 and §6 item 1 as a standing theoretical debt, in the same spirit as
cdot-4's own honest flagging of invariant $G$ as adopted-not-derived
(`cdot-4/T8_Gravitational_Constant.md`).

---

## 4. Why AQUAL, Specifically

Bekenstein & Milgrom's AQUAL (1984) was chosen over other MOND-family relativistic or
field-theoretic completions (TeVeS, MOG, superfluid dark matter, etc.) for a narrow
reason: it is the simplest, most direct statement of "modify the field, not the
potential" — a single modified Poisson equation, no additional fields or metric
structure — which is exactly the minimal fix identified by cdot-6's own negative result
(§1 above). It is explicitly *not* chosen for any relativistic-completeness property;
cdot-7 §4 states plainly that this framework currently makes no relativistic-level
predictions at all, a real scope reduction from cdot-6 (which, via Atkinson, reproduced
GR's predictions for light bending and perihelion advance exactly). Whether a relativistic
completion is later needed, and whether AQUAL specifically (versus some other
field-based modification) is the right long-term choice, is open (`Foundation.md` §6
item 4).

The connection between $a_0$ and this framework's own $H_0^\text{hor}$
(`Foundation.md` §4) continues a candidate relation ($a_0\sim cH_0$) that has recurred
throughout this entire project's history — cdot-4/5's "three-candidate-length problem
for $g_\dagger$" (`cdot-5/T6_MOND_Acceleration_Scale.md`, `cdot-4/T14_Connecton_
Gravity.md`) found the same order-of-magnitude relation without a derived prefactor.
cdot-7 inherits that same unresolved $\sim2$–$3\times$ tension (`Foundation.md` §5.3),
not a new problem.

---

## 5. First Attempt at Deriving $s=+\frac12$ (2026-07-07) — Full Working

Per the author's request to give Foundation §6 item 1 a first attempt, three candidate
Machian mechanisms were tried, all treating the particle's rest energy as sourced by
Sciama-type gravitational self-binding to the horizon mass $M_h$, differing only in what
length scale the binding is evaluated at.

**Attempt A — binding at the particle's own Compton wavelength.**
$mc^2\sim GmM_h/\lambda_C$ with $\lambda_C=\hbar/(mc)$ gives, after substituting and
simplifying, $m=\hbar c/(GM_h)$. Using premise 2's $M_h\propto R_h^3$ (with $\rho$ flat)
and $R_h\propto c$ (§2.2, unaffected by this attempt since it uses bulk density, not
per-particle mass): $m\propto c/R_h^3\propto c^{-2}$. Wrong sign and wrong magnitude.

**Attempt B — binding at the particle's own gravitational radius.**
$mc^2\sim GmM_h/r_s$ with $r_s=2Gm/c^2$ collapses immediately to $m=M_h/2$ — the
particle's own mass would have to equal half the total horizon mass, which is
dimensionally consistent but physically degenerate (true for no particle). Not a real
candidate; recorded so the dead end isn't retried.

**Attempt C — the mass-conservation reading matters, and changes premise 2 itself.**
Foundation §2.1 states $\rho$ (mass density) flat, without distinguishing whether that
or particle *number* density is the actually-conserved quantity — a distinction that
only matters once premise 3 allows individual particle mass to vary, so it was never a
live ambiguity before this iteration. Taking particle number as conserved instead
(density $\rho\propto m(t)\propto c^s$) and rebuilding §2.2's Sciama closure with this
density law: $c^2\propto GM_h/R_h\propto GR_h^2c^s\Rightarrow R_h\propto c^{(2-s)/2}$.
Combined with the kinematic $\dot R_h=c$:
$$\dot R_h = A\cdot\frac{2-s}{2}c^{-s/2}\dot c \overset{!}{=} c \quad\Rightarrow\quad \dot c = \frac{2}{A(2-s)}c^{1+s/2}.$$
At $s=0$: $\dot c\propto c$, reproducing §2.2's exponential exactly — confirms the setup
is a genuine generalization, not a different calculation. At $s=+\frac12$: separating
and integrating, $c^{-1/4}\propto(t_*-t)$ for some constant $t_*$ — genesis ($c\to0$ as
$t\to-\infty$) still holds, but $c$ now diverges at a *finite future* cosmic time $t_*$,
not only in the $t\to+\infty$ limit as under the current exponential law.

**Not treated as fatal — this exact phenomenon has precedent.** cdot-5's own
connectivity-counting cosmology independently produced a finite-future coordinate-time
singularity, and it was resolved (not dismissed) by noting the *proper time* (clock time)
needed to reach it diverges — a clock never actually gets there, exact mirror of how the
past genesis is at coordinate $t\to-\infty$ but finite proper time away. The same check
would need to be redone here before treating this consequence as either a problem or a
feature.

**What this attempt actually accomplished.** No mechanism reproduced $s=+\frac12$ as a
clean output — this remains adopted, not derived, exactly as `Foundation.md` §6 item 1
says. But Attempt C found that the *adopted* value is not independent of an ambiguity in
premise 2 that was invisible before premise 3 existed (whether particle number or mass
density is the conserved quantity), and that resolving it in favor of the more literal
reading of "mass neither created nor destroyed" would require rebuilding §2.2's
cosmology, not just re-justifying §3's exponent in isolation. This is now recorded in
`Foundation.md` §2.1 and §3.4 as a load-bearing open dependency, not left as an
in-conversation dead end.

### 5.1 The fork resolved: number-conservation adopted, closure rebuilt (2026-07-07)

The author's decision, on seeing the fork: adopt the particle-number-conserved reading
outright ("back to Machian by number"). `Foundation.md` §2.1–2.2 were rewritten
accordingly, replacing the flat-$\rho$ Sciama closure with one built from constant
particle number density $n$ and premise 3's own $m(t)\propto c^{1/2}$, giving
$M_h(t)\propto R_h(t)^3(c/c_0)^{1/2}$ instead of $M_h\propto R_h^3$.

**Full derivation, checked twice (an intermediate dimensional slip in fixing the
constant $A$ was caught and corrected before trusting the final relations — recorded so
the same slip isn't repeated: $R_h=Ac^{3/4}$ requires $A=\kappa^{-1/2}c_0^{1/4}$, not
$c_0^{-1/4}$, for the dimensions to balance; the final $t$-vs-$R_{h,0}$ relations used
below turned out to be unaffected by this specific slip, but that was confirmed, not
assumed).**

Solving $\dot c=\frac{4}{3A}c^{5/4}$ gives $c(t)=c_0(1-(t-t_0)/\tau)^{-4}$ with
$\tau=3R_{h,0}/c_0$. Key results, cross-checked by two independent routes each
(direct integration and substitution):
- $H_0^\text{hor}\equiv(\dot c/c)|_{t_0}=4/\tau$ — and combined with the low-$z$
  expansion of the new $D_p(z)=R_{h,0}[1-(1+z)^{-3/10}]$, $H_0^\text{obs}=10/\tau=
  \frac52H_0^\text{hor}$ — the *same ratio* as the simpler closure, since it depends
  only on the redshift exponent (a local, today's-epoch fact), not on the global
  history of $c(t)$. Numerically unchanged: $H_0^\text{hor}\approx2.86\times
  10^{-11}\,\text{yr}^{-1}$, and consequently $a_0=c_0H_0^\text{hor}$ is unchanged too
  — a clean robustness result, not assumed in advance.
- Proper age $\tau_\infty=\tau/9\approx15.5$ Gyr (was $\approx13.97$ Gyr) — the
  $\tau_\infty=1/H_0^\text{obs}$ identity used before was a special feature of the pure
  exponential specifically, and does not generalize; this is a genuine, not merely
  cosmetic, change.
- Particle horizon $D_p(\infty)=R_{h,0}=\tau c_0/3\approx14.3$ Gpc (was $\approx10.7$
  Gpc).
- The finite-future coordinate singularity survives into this fully-worked version, and
  the proper-time-diverges resolution (§5 above) was verified explicitly here, not just
  asserted by analogy to cdot-5: $\Delta\tau_\text{proper}(U)=\frac\tau9[(1-U/\tau)^{-9}-1]
  \to\infty$ as $U\to\tau^-$. Confirmed, not just plausible.

All of this is now in `Foundation.md` §2.1, §2.2, §3.4, §5.2, §5.3 directly — this
section retains the derivation trail (including the caught error) for anyone who needs
to redo or check it, per this project's standing practice of keeping working shown, not
just conclusions.

---

## 6. The Photon-Sector Correction: a Real Bug in §3.3, Found and Fixed (2026-07-07)

A collaborative session with another Claude instance ("Fable"; full transcript and
working documents archived in `Fable-1/`) began by stress-testing the premises against
each other, before working any specific open item, and found that Foundation §3.3's
redshift law — "a photon's conserved frequency" — directly contradicts premise 1 +
premise 2's own propagation kinematics.

**Two independent arguments, cross-checked and verified by the main session before
merging (not accepted on the sub-session's authority alone):**

1. **Crest-transit kinematics.** In static space (premise 1), a source at fixed distance
   $D$ emits two crests separated by coordinate interval $\Delta t_e$; both travel the
   same $D=\int c\,dt$, giving $c(t_e)\Delta t_e=c(t_0)\Delta t_0$ to first order — the
   arrival rate exceeds the emission rate by $c_0/c_z$. The arrival rate of crests *is*
   the received frequency, so coordinate frequency is not conserved in flight; it grows
   with $c(t)$.
2. **Wave mechanics.** Premise 1's exact spatial translation invariance conserves the
   spatial wavenumber $k$ (Noether), not the frequency; a mode $\varphi=a(t)e^{ikx}$ of
   $\ddot\varphi=c(t)^2\nabla^2\varphi$ is an oscillator with adiabatically varying
   $\omega(t)=c(t)k$ ($\dot c/c\sim10^{-18}\,\text{s}^{-1}$ against optical frequencies
   $\sim10^{15}\,\text{s}^{-1}$), so the WKB adiabatic invariant conserves photon
   number, not photon energy: $E_\gamma(t)=\hbar c(t)k\propto c(t)$.

Both use nothing but premises 1–2's own kinematics — this is an internal-consistency
correction, not a new assumption, and it was independently re-derived (both routes) by
the main session before being accepted, not merely taken on the sub-session's say.

**The superseded law, for the record.** The old law, $1+z=(c_0/c_z)^{5/2}$
(equivalently: photon frequency literally conserved from emission to reception), is
**retired, not merely deprecated** — it fails a direct, now-available observational
test. Light-curve time dilation and redshift are the same measurement under conserved
$k$ (frequency is an inverse period), giving dilation exponent $b=1$ exactly, generic
in the mass-scaling exponent $s$. The old law instead predicts $b=(s+2-1)/(s+1)\times
\ldots$ — worked out to $b=3/5$ at $s=\tfrac12$ specifically — which the Dark Energy
Survey's direct measurement of SN Ia light-curve widths (White et al. 2024, *MNRAS*
533, 3365; $b=1.003\pm0.005\pm0.010$) excludes at $\sim36\sigma$. **The correction was
not a matter of taste between two internally-consistent options — the old law was
simply wrong**, and demonstrably so once the right observational test is applied. Do
not revive the conserved-frequency reading; if a future session is tempted to import a
redshift law from an earlier cdot iteration by analogy again, check it against premise
1's own crest kinematics first, the way this session eventually did.

**Corrected law and its consequences** are now `Foundation.md` §3.3 directly (redshift
exponent $s+1=\tfrac32$; the Bohr-radius-exponent coincidence; time dilation $=1+z$
exactly). The flux/luminosity sector built on it ($d_L=(1+z)D_p$, $d_A=D_p/(1+z)$,
Etherington duality, Tolman dimming, the exact Einstein–de Sitter degeneracy on the
fixed point, $q_0=+\tfrac12$) is `Foundation.md` §5.5. **The EdS degeneracy is a genuine
finding, not a defect of the correction**: every purely photometric observable computed
matches $\Omega_m=1$ exactly, which is simultaneously why the framework passes every
test that kills tired-light models (dilation, duality, Tolman) and why it inherited
EdS's own two decisive failures (the SN Ia Hubble diagram; the age problem) until §8
below repaired the closure.

**A general result worth remembering for any future closure attempt**: for *general*
mass exponent $s$ (holding $g=0$), the fixed-point deceleration parameter is
$q_0=\beta\equiv(2-s)/(2(s+1))$, and acceleration ($q_0<0$) requires $s>2$ — which
contradicts the kinematic $\dot R_h=c>0$ (the horizon would have to shrink as $c$
grows). **No rescaling of $s$ within this closure family can ever produce acceleration**;
this is structural, not a fine-tuning failure of $s=\tfrac12$ specifically, and rules out
an entire class of "just pick a different exponent" fixes before they're tried.

---

## 7. The Planck-Unit Invariance Principle, and the LLR $\Leftrightarrow\alpha_G$ Identity

Prompted by the author's suggestion to check whether the Chandrasekhar mass's
$c$-dependence could mitigate the new EdS/SN conflict (§6): checked, and found
unavailable. $M_\text{Ch}\propto(\hbar c/G)^{3/2}/m_H^2\propto c^{1/2}$ exactly
(using $\hbar,G$ invariant, $m_H\propto c^{1/2}$) — the Chandrasekhar mass scales
*exactly* as every rest mass does under premise 3, so it is epoch-invariant in local
units and the candle is exactly standard. Checked further (Ni-56 energetics, ejecta
velocities, Thomson opacity per unit mass, diffusion times): every dimensionless ratio
entering standard SN Ia physics is epoch-invariant, under the further, explicitly
flagged extension that strong- and weak-sector dimensionless couplings are also
Planck-unit invariant (new, load-bearing assumption, not previously stated).

**Why no $(g,s)$ choice can ever rescue the candle, proven, not just checked at
$s=\tfrac12$.** Define $E'\equiv g+2s-1$, the drift exponent of $\alpha_G=Gm^2/\hbar c$.
This is the *same quantity, up to sign*, as `Foundation.md` §5.1's LLR-cancellation
exponent: $E'=-E_\text{LLR}$, since $E_\text{LLR}=1-2s-g$ (this document's own earlier
general formula, §3 above). Reproducing the standard $\Lambda$CDM-vs-EdS SN residual
via candle evolution requires $E'\approx-0.6$ to $-0.7$; LLR safety requires
$E_\text{LLR}\approx0$, i.e. $E'\approx0$ — the *same* dimensionless comparison
(gravitational binding against the atomic sector), measured at $z=0$ (LLR) and
$z\sim1$ (the candle). A framework cannot drift one without drifting the other, for
*any* $(g,s)$, not just the adopted values. This closes the Chandrasekhar-mitigation
route decisively — record it so it is not attempted again.

**The larger find, reading the identity in the other direction.** Given $G,\hbar$
invariant (a units choice, not physics), $s=+\tfrac12$ is the *unique* value making
$\alpha_G$ epoch-invariant — i.e. $m_\text{Pl}=\sqrt{\hbar c/G}\propto c^{1/2}$
automatically obeys premise 3's own law, so premise 3 *is* the statement "all mass is
constant in Planck units." The identical move on the electromagnetic sector
($q_\text{Pl}=\sqrt{4\pi\epsilon_0\hbar c}$; $e/q_\text{Pl}=\sqrt\alpha$ invariant iff
$\epsilon_0\propto c^{-1}$ given $e,\hbar$ fixed) derives the auxiliary EM assumption
from the *same* principle. **This dissolves the tension recorded as open item 7 in an
earlier pass through the Foundation**: "all local physics scales the same way with
$c$" was never quite the right slogan (different-dimension quantities necessarily carry
different powers); "all *dimensionless* physics is invariant" is the correct
statement, and it implies both exponents at once. Recorded here as a genuine
unification (two previously-independent postulates reduce to one), with an important
caveat the merge into `Foundation.md` §3 preserves: **this upgrades the status of
$s=+\tfrac12$ from "fitted number" to "the unique value under a stated symmetry
principle" — it does not yet explain *why* that symmetry should hold.** The mechanism
for Planck-unit invariance itself remains a genuine, unresolved debt (`Foundation.md`
§6 item 3), not something this identity should be read as having closed.

---

## 8. The AQUAL-Consistent Closure: Perturbation Analysis, Cosmography, and the Dead $\lambda$-Derivation Hope

Prompted by the author's request to align premise 4 with the invariance principle (§7):
found, first, an identity hiding in `Foundation.md` §4's own definitions —
$a_0\equiv\lambda c_0H_0^\text{hor}$ composed with $H_0^\text{hor}\equiv(\dot c/c)|_{t_0}$
gives $a_0=\lambda\dot c(t_0)$ exactly. Sharpened to an epoch-dependent
$a_0(t)=\lambda\dot c(t)\propto c^{5/4}$ (frozen-$a_0$ considered and rejected: it makes
today's epoch special for no Machian reason, and breaks the exact EdS correspondence of
§6, which requires $\hat a_0(z)\propto(1+z)^{3/2}=c\,H_\text{EdS}(z)$ in local units — a
result cross-checked independently by the main session via direct computation of the
local acceleration-unit exponent, $c^{7/2}$, obtained two different ways).

**The inconsistency that motivated the rebuild.** The Sciama closure's own horizon
binding acceleration is $g_h=c^2/R_h=\tfrac34\dot c$ (exact algebra, verified: with
$R_h=Ac^{3/4}$ and $\dot c=\frac{4}{3A}c^{5/4}$, $c^2/R_h=c^{5/4}/A=\tfrac34\dot c$
identically), giving $x_h\equiv g_h/a_0=3/(4\lambda)\approx2.9$ at $\lambda\approx0.26$
— squarely in AQUAL's transition regime. Premise 2, as written before this session,
computed this binding with pure Newtonian gravity, which premise 4 declares invalid
exactly there. This is a genuine internal contradiction, present all along and
previously unnoticed, not a hypothetical.

**The closure-form decision.** $c^2\propto GM_h/R_h$ (potential-based) was rejected in
favor of $c^2=\kappa g_hR_h$ (field-based, using AQUAL's exact spherical relation
$\mu(g_h/a_0)g_h=GM_h/R_h^2$) because the deep-MOND potential
$\sqrt{GMa_0}\ln(R/R_\text{ref})$ carries an arbitrary reference scale $R_\text{ref}$ —
importing it would smuggle in exactly the free constant this construction is trying to
explain. $\kappa,\lambda$ enter every downstream result only through
$\tilde\lambda\equiv\kappa\lambda$; $\kappa=1$ is assumed for all numerics, with the
resulting $O(1)$ ignorance carried explicitly rather than absorbed silently into
$\lambda$.

**Perturbation analysis (full derivation).** Writing $R_h=B\sqrt{\mu_*}c^{3/4}(1+\varepsilon)$
and linearizing the dynamical system of `Foundation.md` §2.2 about the fixed point
$x_*=3/(4\kappa\lambda)$ gives $\dot\varepsilon=\frac{3}{2\nu_*}\frac{\dot c}{c}\varepsilon$
with $\nu_*\equiv d\ln\mu/d\ln x|_{x_*}$, hence $\varepsilon(z)=\varepsilon_0(1+z)^{-1/\nu_*}$
— verified numerically in `closure_dynamics.py` (measured growth exponent $5.795$ vs.
predicted $3/(2\nu_*)=5.827$ for the fiducial case; run directly by the main session,
not merely trusted). Cosmography: $q_0=(4-2j)/3$ with $j\equiv c\ddot c/\dot c^2$;
checked $j=\tfrac54$ on the fixed point gives $q_0=+\tfrac12$ exactly, matching §6's
independent photon-sector derivation — an important cross-check, since the two were
derived by different routes (redshift-law algebra vs. dynamical-systems cosmography)
and agree.

**The dead hope, recorded so it is not retried.** The original motivation for rebuilding
the closure included the hope that self-consistency between the closure and $a_0=\lambda
\dot c$ would *derive* $\lambda$. It does not: the fixed point $x_*=3/(4\kappa\lambda)$
exists for *every* value of $\lambda$ — the kinematic exponent $\tfrac34$ alone fixes
$x_*$'s functional form, not its numerical value. $\lambda$ remains measured (twice,
independently — from $a_0$'s empirical value, and from the SN residual shape,
agreeing to $\sim35\%$, `Foundation.md` §6 item 3), never derived.

**Numerical validation record.** `closure_dynamics.py` (archived in `Fable-1/`, also
directly re-run by the main session with identical results — every number in
`Foundation.md` §2.2 and §5.5 was independently reproduced, not merely copied from the
sub-session's report): $\varepsilon_0=0$ reproduces exact EdS $d_L(z)$ (to $10^{-10}$
relative) and $\text{age}\times H_0=2/3$ (to $6\times10^{-12}$); the fiducial fit
($\mu$ simple, $\lambda=0.26$) gives $\varepsilon_0=-0.0627$, rms $0.015$ mag against the
$\Lambda$CDM ($\Omega_m=0.3$) proxy curve over $z\in[0.02,1.4]$, $q_0=-0.68$, age
$13.0$ Gyr; the standard interpolating function fits the same proxy $\sim4\times$ worse
(rms $0.060$) at the same $\lambda$. Forward integration: $c\to\infty$ at finite
coordinate time $t_*$ as $c\propto(t_*-t)^{-2/5}$, but proper time diverges
logarithmically ($\approx16.4$ Gyr of proper time per e-fold of $c$ in the deep regime,
directly reproduced) — the genesis-mirror structure survives, weakened from power-law
to logarithmic.

**Ledger for this closure, precisely.** Derived: the dynamical-system structure, the
fixed point and its instability, the deviation shape tied to $\mu$'s slope, the
cosmography, the branch structure, the asymptotic exponential-$c$ future. Fitted:
$\varepsilon_0$ (one number, the framework's analog of $\Omega_\Lambda$, with the same
epistemic status — a cosmic initial condition, not derived) and $\kappa\lambda$ (doubly
measured). Assumed: the closure-form decision above; $\kappa=1$; the $\Lambda$CDM curve
as an SN-data proxy (a real compilation fit is still open work, `Foundation.md` §6
item 1). **On the coincidence problem, recast but not solved**: unlike a constant
$\Lambda$, the deviation is transient and growing — $|\varepsilon|$ passes through the
few-percent range during roughly one e-fold of $c$ regardless of the seed's exact value,
so "why now" becomes "why is the seed's amplitude such that this passage coincides with
stellar-age epochs" (`Foundation.md` §6 item 2) — a real question about $\varepsilon_0$'s
origin, not obviously harder than $\Lambda$'s own value problem, but not answered.

---

## 9. Confronting the Evolving $a_0$ with Observation

Prompted by the author's request to confront the evolving $a_0(t)=\lambda\dot c(t)$ (§8)
with data. Two steps, done in this order and kept in this order deliberately (see the
chronology note below):

**Step 1 — correct the prediction to the fitted trajectory, before consulting any
data.** The naive fixed-point law $\hat a_0(z)\propto(1+z)^{3/2}$ (§8, before the
closure rebuild's own instability was accounted for) is superseded: the *same* slide
($\varepsilon_0=-0.0627$) that produces late-time acceleration also boosts today's
$\dot c$, suppressing the predicted past evolution to $\hat a_0(z)/\hat a_0(0)=
[x_0r_0/(x(z)r(z))](1+z)^{3/2}\to0.61(1+z)^{3/2}$ asymptotically — computed directly
from the integrated trajectory (`a0_confrontation.py`, re-run directly by the main
session, reproducing the reported table exactly), not a separate fit. The suppression
factor is fixed by the *same* $\varepsilon_0$ already fitted to the SN Hubble diagram —
a rigid, zero-new-parameters consistency relation between the expansion history and the
RAR's redshift evolution — and is nearly parameter-free across the $(\mu,\lambda)$
family (amplitude varies $\pm3\%$, slope $\pm10\%$ once $\varepsilon_0$ is re-fit per
case).

**Step 2 — the measurement.** MUSE-DARK III (Ciocan et al. 2026, *A&A* 709, L16) and
Vărăşteanu et al. (2025, MIGHTEE-HI) were located via literature search and their
citations, DOIs, and quoted numbers **independently verified by the main session**
(both papers, and the specific quoted values — $a_0(z\sim1)=2.38^{+0.12}_{-0.10}$,
$a_1=1.59^{+0.11}_{-0.10}$, and the MIGHTEE $1.69\pm0.13$ at $z<0.08$ — confirmed to
match exactly via independent web search before being trusted; this is exactly the
kind of load-bearing external citation that should always be checked rather than
taken on a sub-session's authority, and in this case it checked out precisely).
**Chronology, recorded because it matters for how much weight the agreement deserves**:
Step 1's trajectory numbers were computed before Step 2's literature search, within the
same session — genuinely blind, not reverse-engineered to fit, though same-day.

**The confrontation.** Three-way discrimination: constant $a_0$ (standard MOND) is
excluded outright by the detected evolution; the naive, unsuppressed $(1+z)^{3/2}$ law
overshoots badly ($a_1^\text{eff}=2.46$ vs. measured $1.59$); the fitted trajectory
predicts $a_1^\text{eff}\approx1.2$–$1.4$ and $a_0(z{=}1)\approx2.2$ — roughly 85% of the
measured amplitude, landing between the two excluded alternatives, with no parameter
tuned for this specific observable. Face-value residual: $\sim15$–$20\%$ low,
formally $3$–$5\sigma$. **Not treated as decisive against the framework**, for a
reason visible inside the data themselves: the MIGHTEE-HI point at $z<0.08$ is
inconsistent with *any* smooth evolution anchored to the local (SPARC) value — including
MUSE-DARK's own linear fit extrapolated backward — demonstrating cross-survey/
methodology zero-point offsets of order $0.3$–$0.5\times10^{-10}$ m/s², comparable to
the framework's own shortfall. This is an external puzzle the framework inherits, not
one it created, and it is not this framework's job to resolve MIGHTEE-vs-MUSE-DARK
systematics — but it does mean the face-value $\sigma$ overstates how decisively the
current data constrain the model.

**The decisive test is not yet run.** A joint statistical fit — the SN compilation,
binned $a_0(z)$ across surveys with per-survey zero-point nuisance parameters, and the
local RAR shape, fit jointly over $(\varepsilon_0,\kappa\lambda,\mu)$ — is the right
analysis and has not been performed (`Foundation.md` §6 item 1). After the SN fit the
framework retains essentially one shape degree of freedom, so this test can genuinely
kill it. Ranked future channels: low-acceleration lensing RAR by lens redshift
(systematics-clean, small effect); SKA-era BTFR zero-point evolution (larger effect,
diluted by current quasi-Newtonian-radius TFR samples); early structure formation
(qualitative only, awaits the radiation-era/perturbation sector, §10 below).

---

## 10. The Thermal Sector, and the Missing Radiation Era

The photon-sector machinery (§6: conserved $k$, conserved mode occupation, adiabatic
evolution) determines blackbody radiation's behavior with no new assumptions. A Planck
spectrum at emission keeps its occupation number per mode; since every mode's frequency
scales identically ($\omega=c(t)k$), the spectrum stays exactly Planckian at every later
epoch with coordinate temperature $T(t)=T_ec(t)/c_e$ — no spectral distortion is
generated by propagation, consistent with the FIRAS blackbody at the $10^{-5}$ level (a
test that kills most non-expanding photon sectors). In local units,
$\hat T(z)=\hat T_0(1+z)$ (matching SZ-cluster and molecular-absorber measurements),
$\hat n_\gamma\propto(1+z)^3$, $\hat u_\gamma\propto(1+z)^4$ — the complete background
thermal phenomenology of an expanding universe, reproduced with zero new assumptions.

**This derivation is also what exposed a real gap, now on the books as a first-class
open item.** Premise 2's Machian source counts rest mass only
($M_h=\frac43\pi R_h^3nm(t)$), but $\hat u_\gamma/\hat\rho_mc^2\propto(1+z)$ grows into
the past exactly as in standard cosmology — at the analog of $z_\text{eq}\sim3400$,
radiation energy must dominate the horizon's actual content, while the closure as
written sources $c(t)$ from the subdominant component. Every result derived this
session (and in this document) is therefore a **late-universe result**
($z\ll z_\text{eq}$) — unaffected by this gap, but BBN- and CMB-era physics cannot even
be *posed* until the closure is extended to include radiation energy (presumably as
$u_\gamma/c^2$, itself raising new questions since photon energy is epoch-dependent in
coordinate units — not a small extension). Recorded as `Foundation.md` §6 item 4,
logically prior to the already-flagged perturbation/BAO/CMB sector (item 5).

**Two small consistency lemmas, folded directly into the Foundation rather than kept
here:** (i) $a_0=\tfrac23\lambda c_0H_0^\text{obs}$ is trajectory-invariant, since
$H_0^\text{obs}=\tfrac32\dot c_0/c_0$ holds exactly on *any* solution of §8's dynamical
system — the $\lambda\approx0.26$ calibration made before the closure rebuild survives
it untouched (verified numerically: $a_0=1.18\times10^{-10}$ m/s² on the fitted
trajectory at $\lambda=0.26$); (ii) AQUAL's deep-MOND limit gives the Faber–Jackson-type
relation $\sigma^4\sim GMa_0$ for pressure-supported systems, so `Foundation.md` §0's
M-σ goal follows for free from the machinery already in place, with the same
$\hat a_0(z)$ evolution as the BTFR ($\Delta\log\sigma=\tfrac14\Delta\log\hat a_0(z)$) —
a secondary confrontation channel, not yet run.

**On citations: the SN time-dilation constraint was upgraded, not merely footnoted.**
An earlier pass through this session's photon-sector correction (§6) quoted the SN
Ia spectral-aging dilation bound from memory (Blondin et al. 2008,
$b\approx0.97\pm0.10$) and flagged it for verification. Verified, and superseded: the
Dark Energy Survey measurement (White et al. 2024, *MNRAS* 533, 3365) is both stronger
and directly checked against the correct observable (light-curve width, not spectral
aging specifically), giving the $b=1.003\pm0.005\pm0.010$ figure used throughout §6 and
now in `Foundation.md` §3.3. Blondin et al. (2008) remains a valid earlier measurement
in the same literature; DES is the citation of record going forward.

**Code archive.** `closure_dynamics.py` and `a0_confrontation.py` (originally produced
in the `Fable-1/` sub-session, both independently re-run end-to-end by the main session
with identical results before any number from them was trusted or merged) are the
computational record for §8–§9 above. Keep them alongside this document; they reproduce
every quoted number in `Foundation.md` §2.2 and §5.5 directly from source, and should be
the first thing re-run if any of those numbers are ever in doubt.

---

## 11. M-σ: What Carries Over from cdot-4, What's Generic AQUAL, and Why the Confrontation Is Weaker Than RAR's

Before deriving anything for cdot-7, checked cdot-4's own M-σ mechanism
(`cdot-4/T17_Galaxy_Morphology_and_MSigma.md`) to see what was mechanism-specific versus
generic. cdot-4's core algebraic move — $M_\text{bulge}\sim\sigma^4/(Ga_0)$ from
deep-MOND virial balance, with $M_\text{BH}$ treated as an external correlate of
$M_\text{bulge}$ rather than something MOND itself fixes ("would break the universality
of $a_0$ and the RAR's tightness" if it were the source) — is generic AQUAL physics,
needing nothing beyond the deep-MOND limit already in `Foundation.md` §4. Everything
else in T17 (the $\mathbf v\times\mathbf B_c$ Lorentz-filter/dynamical-selection
stripping picture that explains *why* ellipticals versus disks, the connecton-sourced
coherence factor $f\approx0.627\,v_\text{rot}/\sigma$, the evaporation-ceiling account
of overmassive BCG black holes) is specific to cdot-4/5's connecton-gravity mechanism
and does not carry over — cdot-7 has no analogous local-gravity ontology to hang it on,
and does not need one for the core relation. cdot-4's own T17 never performed a
quantitative fit against real M-σ catalogs either (Ferrarese & Merritt 2000, Gebhardt et
al. 2000 cited for the exponent only) — this was already an honest gap, not something
cdot-7 is regressing from.

**The derivation, generic-AQUAL version.** Virial balance for a dispersion-supported
system in deep-MOND, $M\sigma^2\sim M\times g\times r$ with $g=\sqrt{GMa_0}/r$, gives
$\sigma^4\sim\Gamma GMa_0$. Unlike the rotation-curve BTFR (an exact deep-MOND result,
$\Gamma\equiv1$ identically, since a flat rotation curve has a clean asymptotic limit),
$\Gamma$ here depends on the system's actual density/velocity-anisotropy profile and is
only $O(1)$ — this is the same honest limitation cdot-4's own derivation had (there,
$\Gamma=8/(\pi\beta^2)$, $\beta\equiv v_\text{rot}/\sigma$, ranging $\approx2.5$–$28$
over plausible $\beta$; cdot-7 has no $\beta$-analog to compute a value with, so simply
states $\Gamma=O(1)$, undetermined, rather than importing a number from a mechanism
that no longer applies).

**Checking the evolution channel against the literature — the honest result: real, but
not yet testable.** The $\Gamma$-independent prediction, $\Delta\log\hat\sigma=\tfrac14
\Delta\log\hat a_0(z)$ at fixed bulge mass, is in principle as clean as the RAR's
$\hat a_0(z)$ test. Checked two literature channels (both verified via search, not
assumed):
- **The black-hole $M_\text{BH}$-$\sigma$ relation** shows a large, real, well-measured
  redshift evolution: JWST/ALMA observations of quasar hosts at $z\sim1$–2 find black
  holes offset *above* the local relation, up to $10\times$ overmassive at fixed
  $\sigma$, with the relation's slope flattening and normalization rising with $z$. This
  is dramatic, but it is squarely the channel just excluded above as outside this
  framework's scope — the standard interpretation is black-hole assembly history (heavy
  seeds, super-Eddington accretion phases, and plausibly sample selection in
  flux-limited quasar surveys), not bulge dynamics. It would be a mistake to either
  claim this as support or treat it as an exclusion; it simply isn't a test of the
  relation this framework actually derives.
- **The correct channel — stellar-mass-vs-$\sigma$ for quiescent galaxies, no black
  hole involved** — shows no significant evolution at $z<0.7$ and only mild evolution
  at $0.9<z<1.7$ (Zahid et al. 2016, *ApJ* 832, 203, and related work), and the existing
  literature already attributes that mild evolution to ordinary galaxy size evolution
  (more compact "red nugget" progenitors at higher $z$, well established independently
  via direct imaging) — a completely conventional explanation, degenerate in *sign*
  with this framework's own prediction (both predict $\sigma$ higher at fixed mass
  toward higher $z$). Distinguishing them requires checking whether the *observed*
  amount of evolution exceeds what size evolution alone predicts, using each study's own
  size-evolution model as the null. Not done here — a well-posed, tractable task
  (`Foundation.md` §6 item 1), but a genuinely different and harder one than "check
  against an existing measurement of exactly this quantity," which is what made the
  RAR confrontation (§9) decisive.

**Verdict, stated plainly for the ledger:** M-σ is safely and correctly brought into
scope now — it is an equilibrium-dynamics test, not a structure-formation one, so it
does not require touching the deliberately-deferred radiation/perturbation sector. But
its current evidentiary status is genuinely weaker than RAR's: qualitatively right
shape, an honestly undetermined normalization, and an evolution channel that is real in
principle but not yet separable from a conventional competing explanation with existing
data. This should not be presented with RAR's confidence in any write-up.

---

## 13. The Real Pantheon+ Joint Fit (Fable-2 Session, 2026-07-07)

A second sub-session ("Fable-2") executed `Foundation.md` §6 item 1 at first-pass level
against **real data**, replacing the $\Lambda$CDM-proxy fit of §8. Verified directly by
the main session, not taken on trust: symlinked the project's own Pantheon+ release
(`data/Pantheon+SH0ES.dat`, `.cov` — the same 1701-SN, full-STAT+SYS-covariance data
cdot-5's own T4 used) into `Fable-1/data/` and ran `joint_fit.py` end to end.

**Method.** SN sector: $z_\text{HD}>0.01$ (1590 SNe), $m_b^\text{corr}$ with the full
published covariance, absolute-magnitude/$H_0$ offset marginalized analytically (so
only the $d_L(z)$ shape is tested). $a_0$ sector: SPARC $1.20\pm0.26$ ($z=0$),
MIGHTEE-HI $1.69\pm0.13$ ($z\approx0.05$), MUSE-DARK III $2.38\pm0.055$
($z_\text{eff}\approx0.9$) and slope $1.59\pm0.054$ ($0.33<z<1.44$), all fit through the
*same* $(\varepsilon_0,\kappa\lambda)$ as the SN sector via the integrated trajectory
ratio. Known caveat, carried forward: the MUSE point and slope share the same 79
galaxies and are correlated — first-pass indicative, not definitive, pending per-bin
data and covariance.

**Verification record (every number reproduced by the main session, independently):**
pipeline validation, $\Omega_m=0.331\pm0.018$, $\chi^2=1403.7$ (matches published
Pantheon+ SN-only, $0.334\pm0.018$, to a third of a sigma); joint rigid fit
$\varepsilon_0=-0.0678$, $\kappa\lambda=0.307$, $\chi^2_\text{SN}=1405.3$
($\Delta\chi^2=+1.6$), $\chi^2_{a_0}=6.5$; standard-$\mu$ comparison
$\chi^2=1453.7$ ($\Delta\chi^2=42$ vs. simple, confirmed: $1453.7-1411.8=41.9$);
free-$A$ variant $\kappa\lambda=0.312$, $A=1.39$, $\kappa=1.01$. The one number not
printed by the script — the best free *linear* $a_0(z)$ reference, $\chi^2=20.0$ — was
independently re-fit by hand (`scipy.optimize.minimize`, same four data points) and
returned $19.98$, confirming it rather than assuming it.

**What this changes, and what it doesn't.** $\kappa\approx1$ coming out of a genuine fit
(not assumed by fiat) is a real, unforced success. But the local-$a_0$ value that
achieves it ($1.39$) is *not* the same number used elsewhere in the document as the
"empirical" SPARC anchor ($1.20$) — checked directly: using $1.39$ instead of $1.20$ in
the §14 mass-census calculation shifts $F$ from $2.52$ to $2.92$, a real, not
cosmetic, difference. This is exactly the kind of thing a properly marginalized $a_0$
prior in the eventual four-term fit needs to settle, not something to paper over by
picking whichever number reads better.

**Figures regenerated against real data.** `cdot-7/make_figures.py` was rewritten to
build directly on `joint_fit.py`'s trajectory and the real, binned Pantheon+ residuals
(not the smooth $\Lambda$CDM proxy curve used previously) — both SVGs in `Foundation.md`
§2.2 and §5.5 now show the actual data, not a curve-vs-curve comparison.

---

## 14. The Closure Density Problem: Elevated, Quantified, and Reconciled

Prompted directly by the main session's pushback on an earlier seed-analysis update,
which had filed $\Omega_\text{closure}=0.134$ (vs. baryon census $\Omega_b=0.049$) as a
"byproduct" rather than a first-class finding. Two follow-up rounds resulted.

### 14.1 First response: quantifying the over-constraint

Verified the closure's own demand for a density is exact, not approximate: from the
AQUAL horizon condition $\mu(x_0)g_h=GM_h/R_{h,0}^2$ with $g_h=c_0^2/(\kappa R_{h,0})$,
$$\rho_0=\frac{3\mu(x_0)c_0^2}{4\pi G\kappa R_{h,0}^2}\quad\Longrightarrow\quad
\Omega_\text{closure}=\frac89(\kappa\lambda)\lambda x_0^2\mu(x_0)$$
(main session's independent re-derivation, exact, using the trajectory identity
$H_0^\text{obs}=\tfrac32\dot c_0/c_0$ — matches the fixed-point specialization
$\Omega_*=\mu(x_*)/(2\kappa)$ too, checked separately). Scanning the $(\mu,\kappa\lambda)$
family gave $\Omega_\text{closure}\in[0.08,0.22]$ — robustly *below* $\Lambda$CDM's
$\Omega_m\approx0.315$ (not a back-door reproduction of the standard matter budget) but
robustly *above* baryons alone (forcing equality with $\Omega_b$ requires
$\kappa\approx2.5$, driving $a_0$ off its empirical value by $\times2$). The one
known-physics escape — relic neutrino mass, $\Omega_\nu\lesssim0.030$ at the KATRIN
bound ($m_\beta<0.45$ eV, $\Sigma m_\nu\lesssim1.35$ eV) — closes the budget only at the
SN-shape-preferred edge ($\kappa\lambda=0.35$) and only marginally.

### 14.2 Second response: exact reconciliation, no refit needed

The main session's own independent recomputation gave $\Omega_\text{closure}=0.115$ at
the joint-fit central values — a three-way spread (0.134 / 0.115 / 0.104) that needed
explaining before any of it could be merged. Resolved analytically, not by refitting:
all three numbers are the *same formula* under three different, previously-implicit
conventions for $\lambda$ and $\varepsilon_0$ (verified by direct substitution,
`omega_reconciliation.py`, independently re-run):

| Value | Convention |
|---|---|
| 0.134 | $\kappa=1$ (i.e. $\lambda=\kappa\lambda=0.307$), $\varepsilon_0=-0.0678$ |
| 0.115 | $a_0$-anchored $\lambda=0.2647$ ($\kappa=1.16$), $\varepsilon_0=-0.0678$ |
| 0.104 | $a_0$-anchored $\lambda$, proxy-fit $\varepsilon_0=-0.0752$ |

The dominant split is the $\lambda$-convention (which value of $a_0$ anchors $\lambda$),
not which $\varepsilon_0$ fit variant is used — the $\varepsilon_0$-variant spread alone
is only $\pm5\%$. **A cleaner, $H_0$-free form was derived and independently verified**
by substituting the $a_0=\lambda\dot c_0$ identity directly into the density relation:
$$\rho_0=\frac{3}{4\pi}\,\kappa\,\mu(x_0)\,x_0^2\,\frac{a_0^2}{Gc_0^2}$$
— $H_0$ cancels entirely, tying the required density to the measured MOND scale alone
(main session re-derived this by direct substitution and confirmed it algebraically,
independent of the code). In this form, $F\equiv\rho_0/\rho_b\approx2.3$–$2.5$
(SPARC-anchored) or $\approx2.9$ (fit's-own-value-anchored, §13) — the dominant
sensitivity is $a_0$'s own $\pm20\%$ empirical uncertainty ($F\propto a_0$ linearly,
since $\kappa\propto1/a_0$ at fixed $\kappa\lambda$), not which $\varepsilon_0$ or
$\Omega_b$ convention is used (each $\lesssim5\%$). $\Omega_bh^2=0.0224$ was used
throughout — the BBN/primordial-deuterium value (Cooke, Pettini & Steidel 2018,
confirmed via search: $100\,\Omega_bh^2=2.166\pm0.015\pm0.011$), chosen specifically
because it does not depend on CMB/$\Lambda$CDM fitting, which would undermine the
point of an independent mass-budget check.

**What this round could not do, stated honestly rather than glossed over**: the actual
four-term fit (adding the local RAR shape and the mass census as likelihood terms,
jointly with the SN and $a_0(z)$ sectors already built) was not run — it requires real
SPARC RAR data (not yet in the repository) and a properly marginalized $a_0$ prior, both
flagged as the necessary next steps rather than skipped silently. The reconciliation
closes the *merge blocker*; the tension itself ($F\approx2.4$–$2.9$) stands, unresolved,
exactly where §14.1 left it.

### 14.3 Precise specification handed to the next attempt

Given the reconciliation, the main session wrote a complete implementation spec for the
decisive four-term fit before the author's next round with Fable-1, covering: the
parameterization ($\varepsilon_0,\kappa\lambda,\lambda$ jointly, not $\lambda$ fixed a
priori); the SPARC RAR shape likelihood (source: Lelli, McGaugh & Schombert 2016, *AJ*
152, 157; McGaugh, Lelli & Schombert 2016, *PRL* 117, 201101 — location to be confirmed
live before hardcoding, since hosted URLs move); the mass-census term using the BBN
$\Omega_b$ value above and a bounded $\Sigma m_\nu$ nuisance with the current, verified
KATRIN bound; and two decisions to state explicitly rather than leave implicit — $H_0$
held fixed at 70 km/s/Mpc for this pass (not fit, since Pantheon+ alone is
$H_0$-degenerate once the offset is marginalized), and a validation requirement that
switching the two new likelihood terms off must exactly reproduce the existing
three-term result before anything new is trusted. This spec is what the next round
executed against (§14.2) — the four-term fit itself remains open.

---

## 15. Open Threads Not Yet Reflected in the Foundation

**Resolved by the Fable-1 session (§6–§10 above), retained here only as a record of
what happened to them, not restated as open:** the flux/luminosity sector (was open
item 2 — built, `Foundation.md` §5.5); the EM-sector tension (was open item 7 —
dissolved by the Planck-unit invariance principle, §7); the directional-prediction
dataset hunt (was open item 8 — reframed into $d_A(z)$ and the now data-confronted
$\hat a_0(z)$); whether the finite-future singularity resolves the way cdot-5's did
(confirmed directly, §8 — proper time diverges logarithmically); whether the
connecton ontology contributes to deriving $s$ or $\lambda$ (superseded — the Planck-
unit invariance principle derives $s$'s uniqueness given the symmetry, without needing
connecton microphysics; whether connecton mechanisms could explain the symmetry
*itself* is folded into the still-open item below, not a separate thread).

**Still genuinely open:**
- Whether the connecton ontology (cdot-4's T12, T14) or the earlier iterations'
  occupancy-counting mechanisms have anything to contribute to a *mechanism* for
  Planck-unit invariance itself (`Foundation.md` §6 item 4) — not yet examined.
- Whether cdot-4/5's flux/luminosity machinery (T4, T18) has anything further to
  contribute now that §6's corrected redshift law and §8's closure rebuild have
  produced a working, EdS-then-$\Lambda$CDM-like cosmology of this framework's own —
  possibly relevant to the still-missing radiation-era extension (§10;
  `Foundation.md` §6 item 5).
- Whether the AQUAL closure-form decision (§8: $c^2=\kappa g_hR_h$, rejecting the
  potential-based alternative) is really the *only* reference-free option, or whether
  a different field-based construction would change the instability's shape
  ($\nu_*$-dependence) enough to matter for the $\mu(x)$-discrimination result
  (`Foundation.md` §6 item 8) — not explored; only one construction was tried.
- Whether the MIGHTEE-HI/MUSE-DARK III zero-point discrepancy (§9) has a known
  resolution in the observational literature (a genuine systematics question this
  framework inherits but did not create, and cannot resolve on its own) — worth a
  literature check before the joint statistical fit (`Foundation.md` §6 item 1) is
  run, since it directly affects how the zero-point nuisance parameters should be
  set up.
