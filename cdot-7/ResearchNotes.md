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

## 6. First Attempt at Deriving $s=+\frac12$ (2026-07-07) — Full Working

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

### 6.1 The fork resolved: number-conservation adopted, closure rebuilt (2026-07-07)

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
  the proper-time-diverges resolution (§6 above) was verified explicitly here, not just
  asserted by analogy to cdot-5: $\Delta\tau_\text{proper}(U)=\frac\tau9[(1-U/\tau)^{-9}-1]
  \to\infty$ as $U\to\tau^-$. Confirmed, not just plausible.

All of this is now in `Foundation.md` §2.1, §2.2, §3.4, §5.2, §5.3 directly — this
section retains the derivation trail (including the caught error) for anyone who needs
to redo or check it, per this project's standing practice of keeping working shown, not
just conclusions.

---

## 7. Open Threads Not Yet Reflected in the Foundation

- Whether the connecton ontology (cdot-4's T12, T14) or the earlier iterations'
  occupancy-counting mechanisms have anything to contribute to *deriving* premise 3's
  mass law or premise 4's $\lambda$ — not yet examined; cdot-7's own open item 1
  (`Foundation.md` §6) is currently unconstrained by any specific mechanism.
- Whether the auxiliary electromagnetic-sector assumption ($\epsilon_0\propto c^{-1}$)
  should itself be revisited under "all local physics scales the same way," rather than
  flagged as an unresolved tension (`Foundation.md` §6 item 7) — this may require
  either changing the EM-sector assumption or narrowing what "universal scaling" is
  claimed to mean.
- Whether cdot-4/5's flux/luminosity machinery (T4, T18) can be adapted directly for
  cdot-7's own §6 item 2, given the different redshift exponent, or needs rebuilding
  from scratch under premise 3's universal scaling.
- Whether §6's finite-future singularity (if the particle-number-conserved reading is
  adopted) resolves the same way cdot-5's did (proper time to reach it diverges) — not
  yet checked here; would need §2.2 rebuilt under that reading first.
