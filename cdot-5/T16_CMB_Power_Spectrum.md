# T16 — The CMB Power Spectrum

*This is the model's hardest observational constraint. **Session 2026-07-04 update:**
the "$R\approx680$, self-similar at all epochs" claim below is **retracted** — its
derivation ("$\rho_b,\rho_\gamma\propto c^2$ identically, so $R$ is epoch-invariant") is
void: the $c^2$ factors are a trivial mass-to-energy unit conversion at *fixed* number
densities, and say nothing about whether the number densities and temperature actually
track cosmic history that way. A corrected derivation (below, §C) — baryon number
conserved (forced by $a=1$) and, symmetrically, **photon number conserved** (nothing
dilutes, nothing is created or destroyed, matching the model's own static-map ethos),
combined with this model's *already-established* Stefan-Boltzmann $c$-dependence
($a_\text{rad}\propto c^{-3}$, T18) — forces $T_\text{eff}(t)\propto c(t)$ and
$R(t)\propto c(t)$, cross-checked against T18's independently-derived stellar
$T_\text{eff}\propto c^{+1}$ result (same exponent, unrelated physics). This gives
$R_\text{rec}\approx20.6$ at $z_\text{rec}=1090$ — neither $680$ nor the
relic-cooling alternative considered and rejected below ($R_\text{rec}\sim5\times10^{-10}$,
which imports a "hot bath cooling" picture this static model doesn't actually need or
support) — and **substantially closes both gaps**: the first-peak position miss drops
from $7.6\times$ to $\approx1.35\times$, and the peak-height miss drops from
$\sim400\times$ to $\approx13.5\times$. Still a failure, but a far smaller one, and one
now built on the model's own established physics rather than an ad hoc analogy or an
imported $\Lambda$CDM kinematic relation. Full details in §C.*

---

## Observational Background

The Cosmic Microwave Background (CMB) angular power spectrum is the tightest
quantitative success of $\Lambda$CDM. A six-parameter fit accounts for thousands of
multipoles at sub-percent residuals. For a static $c(t)$ model with $a=1$, the CMB is
the hardest test on the table — harder than rotation curves, because the
baryon-photon acoustic physics is tightly quantitative and cannot be fudged.

The key features to explain:
1. **The near-perfect blackbody spectrum** ($T\approx2.725$ K, deviations $<10^{-5}$),
   implying genuine thermalization in an optically thick early phase.
2. **The acoustic peak structure.** The angular positions of the peaks encode the
   sound horizon at recombination (hence the angular-diameter distance to the
   last-scattering surface). The *relative heights* of the peaks encode the
   baryon-to-photon ratio and, crucially, whether pressureless dark matter is present
   before recombination.
3. **The third-to-first peak height ratio** is $\Lambda$CDM's cleanest argument for
   cold dark matter: photons oscillate; DM does not. The third peak being of
   comparable height to the first requires $\Omega_\text{DM}\approx5\Omega_b$.
4. **The primordial power spectrum** ($n_s\approx0.96$, nearly scale-invariant),
   attributed to inflation in $\Lambda$CDM.

---

## Translating the CMB: Four Ingredients

### (A) Thermal Origin

**Unaffected by the counting-law change; sharpened by §C's corrected derivation.** In
$\Lambda$CDM the CMB is hot because $a$ (the scale factor) was small; in this model
$a=1$ always, so there is no "the universe was smaller and hotter" story available, and
none is needed. **Recombination is a $c$-threshold-crossing event, not a
temperature-drop event** — this was cdot-4's original candidate translation, and it
survives, now on firmer footing: §C derives $T_\text{eff}(t)\propto c(t)$ (linear, from
photon-number conservation plus this model's own Stefan-Boltzmann $c$-dependence) while
atomic ionization energy scales as $E_\text{ion}(t)\propto c(t)^2$ (T7's Rydberg-like
scaling). The ratio $E_\text{ion}/k_BT_\text{eff}\propto c(t)$ **increases monotonically
with cosmic time** (since $c(t)$ increases): in the deep past ($c\to0$) thermal photon
energy exceeds the ionization threshold — fully ionized — and the ratio crosses $1$ at
some epoch, after which ionization energy dominates and the gas recombines and stays
neutral. This is a genuine, one-way, non-reversible threshold, exactly the kind of event
needed — not an artifact of holding something fixed by fiat. The mechanism by which the
resulting radiation actually *thermalizes* into a clean blackbody remains unworked (§B).

### (B) Blackbody Thermalization

**Unaffected in status.** A near-perfect Planck spectrum requires genuine
thermalization in an optically thick early phase. The static model needs the genesis
density itself to provide the required optical depth. Whether it suffices is unworked
and remains a genuine difficulty — unchanged from cdot-4.

### (C) Acoustic Peaks — The Crux

**The baryon-photon plasma physics — functional form unaffected; the value of $R$ is
corrected below.** The sound speed is
$$c_s=\frac{c}{\sqrt{3(1+R)}},\qquad R\equiv\frac{3\rho_b}{4\rho_\gamma}.$$
This functional form is untouched by anything in this section — only the *value* of
$R$ at recombination is at stake.

**The "$R\approx680$, self-similar at every epoch" claim is retracted — its argument
was void.** The claim (cdot-4, carried into early cdot-5) was: "$\rho_b\propto
mc^2\propto c^2$ and $\rho_\gamma\propto h\nu\propto c^2$ scale identically, so $R$ is
epoch-invariant." This is not a derivation about how a real photon-baryon plasma's
densities evolve with cosmic time — it is a trivial statement that *if* baryon number
$n_b$ and photon number $n_\gamma$ are each independently held fixed, *then* converting
their rest/characteristic energies to Joules using whatever $c(t)$ happens to be "at
that epoch" trivially gives $c^2$ in both numerator and denominator, which cancels
identically **regardless of the true history of $n_b,n_\gamma,T$** — a tautology that
looks like a result. It says nothing about the actual value, which is fixed by the real
number densities and the temperature: $R\propto n_b/T^4$. Using today's measured
$\Omega_bh^2=0.0224$, $T_0=2.725$ K to get $R_0=679.8$ (equivalently
$\eta\approx6.1\times10^{-10}$, the standard baryon-to-photon ratio) is correct **as a
statement about today** — it is the error to then assume this same number applies,
unchanged, at recombination.

**Two forced inputs, derived rather than assumed.**

*Baryon number density $n_b\approx$ const* — forced by $a=1$. Baryon number is
conserved, and on a static map the proper volume of a comoving region never changes, by
definition of premise 1. There is no mechanism in this model for $n_b$ to dilute the way
$n_b\propto(1+z)^3$ does in $\Lambda$CDM (that dilution *is* the definition of volume
expansion). So $\rho_b(t)=n_bm_pc(t)^2$ with $n_b,m_p$ genuinely constant — this part of
the old argument survives, on solid ground.

*Photon temperature $T_\text{eff}(t)\propto c(t)$ — derived, not $T\propto c^2$ and not
the imported $\Lambda$CDM kinematic relation $T\propto(1+z)^1$.* Two candidates were
considered and rejected before reaching this one:

- **$T\propto c^2$ (the old, retracted convention)** treats a photon's characteristic
  energy like a single atomic transition, at *fixed photon number* $n_\gamma$. This is
  internally inconsistent for an actual thermal (Bose-Einstein) photon gas: the standard
  relation $n_\gamma\propto(k_BT/\hbar c)^3$ (from the same mode-density integral that
  gives the radiation constant $a$) means $n_\gamma$ and $T$ are not independent — you
  cannot hold $n_\gamma$ fixed while also imposing $T\propto c^2$ without contradiction.
- **$T\propto(1+z)^1$ (the standard $\Lambda$CDM "hot bath cooling" relation)** was
  tried and rejected in an earlier pass at this problem (session
  `recombination_radius/`): it correctly diagnoses that the old $T\propto c^2$
  convention gives a *colder* past (backwards — no threshold-crossing possible), but its
  own fix imports $\Lambda$CDM's adiabatic-expansion argument (phase-space dilution
  $\propto a^{-3}$ combined with wavelength stretch $\propto a$), a mechanism this
  static ($a=1$) model does not have and does not need. There is no "cooling from a hot
  early bath" here — there is no expansion to cool into.
- **The corrected relation** comes from the same symmetry already used for baryons:
  **photon number is also conserved** ($n_\gamma\approx$ const — nothing dilutes,
  nothing is created or destroyed, exactly parallel to $n_b$). Using
  $n_\gamma\propto(k_BT/\hbar c)^3$ (invariant $\hbar,k_B$) with $n_\gamma$ fixed forces
  $$\boxed{\,T_\text{eff}(t)\propto c(t)\,}.$$
  **Independent cross-check**: T18 derives $T_\text{eff}\propto c^{+1}$ for *stellar*
  photospheres, via completely unrelated physics ($L\propto c^0$, $R_\star\propto
  c^{-1}$, and this same model's Stefan-Boltzmann $c$-dependence, $\sigma_\text{SB}
  \propto c^{-2}$). Getting the identical exponent from two independent routes — one a
  static cosmic photon gas, one a stellar structure calculation — is a genuine
  consistency signal that $T\propto c$, not $c^2$ and not $(1+z)^1$, is this model's own
  answer, not an artifact of which route is taken.

**The corrected $R(t)$.** Using the model's own already-established radiation-constant
scaling ($a_\text{rad}=\pi^2k_B^4/(15\hbar^3c^3)\propto c^{-3}$, T18) with
$T_\text{eff}\propto c$:
$$\rho_\gamma=a_\text{rad}T_\text{eff}^4\propto c^{-3}\cdot c^4=c^{+1},\qquad
\rho_b=n_bm_pc^2\propto c^{+2}\quad\Longrightarrow\quad
\boxed{\,R(t)\propto c(t)\,}.$$
Using $c(t_\text{rec})/c_0=(1+z_\text{rec})^{-1/2}$ (T2, the redshift law, unaffected by
either the counting law or anything in this section):
$$\boxed{\,R_\text{rec}=R_0\,(1+z_\text{rec})^{-1/2}\,}\qquad\Longrightarrow\qquad
R_\text{rec}=679.8\times(1091)^{-1/2}\approx20.6\quad(z_\text{rec}=1090).$$
**Neither $680$ nor $\sim5\times10^{-10}$** — a third, distinct, better-grounded value,
roughly $34\times$ the $\Lambda$CDM-like value real recombination needs ($R\sim0.6$),
compared to the old claim's $\sim1130\times$ miss or the rejected relic-cooling
alternative's $\sim10^9\times$ miss in the other direction.

**Caveat, not yet closed.** This still assumes the photon population is well-described
by an equilibrium Bose-Einstein/Planck distribution at each epoch, re-evaluated using
that epoch's own mode-density normalization ($8\pi\nu^2/c^3$) — reconciling this with
premise 4's literal claim that an individual photon's energy is exactly conserved once
it stops interacting is subtle and not fully worked out (it requires distinguishing the
*actual, frozen* energy content of a decoupled population, which genuinely never
changes, from the *locally relevant effective temperature* used to evaluate ionization
physics at any given epoch, which does change with $c(t)$). This is flagged as an open
item, not resolved here — but it does not change the fact that $n_b,n_\gamma=$const is
the only assumption this model's own premises actually license, and the resulting
$R_\text{rec}\approx20.6$ rests on strictly less imported machinery than either
alternative considered above.

**The angular position — recomputed with $R_\text{rec}\approx20.6$ in place of both
$680$ and the single-phase-law's earlier $1.4\times$-near-miss number (neither of which
carries over: the counting law changed since cdot-4, and $R$'s value is corrected
above).** Using $D_A\equiv D_p$ (proper transverse size over subtended angle, the
model's own static geometry, unaffected by anything in this section) and
$\theta_s=r_s/D_A(z_\text{rec})$.

**Method.** The sound horizon is the sound-speed fraction of the proper distance sound
could traverse between genesis (the total, now-finite particle horizon $D_p(\infty)$)
and recombination: $r_s=(c_s/c)\times[D_p(z\to\infty)-D_p(z_\text{rec})]$.
$D_p(z\to\infty)\approx116.7\,r_d$ is **finite** (T23 §6, because the subcritical index
$q\approx1.37>1$ makes the tail integrable) — a precondition for this calculation to
even be attempted.

**Numbers** (fitted broken law: $B=33.55\,r_d$, $z_*=1.201$, $q=1.37$,
$D_0=-0.46\,r_d$; $R_\text{rec}\approx20.6$ as derived above):
$$D_p(z_\text{rec}{=}1090)\approx107.56\,r_d,\qquad D_p(\infty)-D_p(z_\text{rec})\approx9.13\,r_d,$$
$$c_s/c=\frac{1}{\sqrt{3(1+R_\text{rec})}}\approx0.1243,\qquad
r_s=(c_s/c)\times9.13\approx1.135\,r_d,\qquad
\theta_s=\frac{r_s}{D_p(z_\text{rec})}\approx0.01055\ \text{rad},$$
$$\boxed{\,\ell_1\approx\frac{\pi}{\theta_s}\approx298\,}\qquad\text{vs. observed }\ell_1\approx220\ (1.35\times\text{ too high}).$$
Down from $7.6\times$ (the earlier miss, computed with the retracted $R\approx680$) —
correcting $R$ alone, with the distance law untouched, closes most of the position gap.

**Decomposition, updated.** Writing $\ell_1=\pi\,[D_p^\text{rec}/(D_p^\infty-D_p^\text{rec})]/(c_s/c)$
separates the **distance factor** ($\approx11.79$, from the fitted counting law,
unchanged by this section) from the **sound speed** ($c_s/c$, set by $R$):

| $R$ | $c_s/c$ | $\ell_1$ |
|---:|---:|---:|
| $0.6$ ($\Lambda$CDM-like) | $0.456$ | $81$ |
| $6$ | $0.218$ | $170$ |
| $20.6$ (this document, corrected) | $0.1243$ | $\mathbf{298}$ |
| $68$ | $0.070$ | $533$ |
| $680$ (retracted) | $0.0221$ | $1674$ |

Matching $\ell_1=220$ exactly at the fitted distance factor needs $R\approx10.8$ (an
already-established number, unaffected by this section) — the corrected
$R_\text{rec}\approx20.6$ is within a factor of $\sim1.9$ of this, compared to the old
claim's $\sim63\times$ miss. **The remaining gap is a real, order-of-magnitude-smaller
tension, not a qualitative failure.**

**The independent check: does $R_\text{rec}\approx20.6$ survive contact with peak
*heights*?** The odd/even (compression/rarefaction) peak-height asymmetry scales
approximately as $(1+R)$; the observed asymmetry corresponds to
$(1+R)_\text{obs}\approx1.6$ ($R_\text{obs}\approx0.6$). At $R_\text{rec}\approx20.6$:
$(1+R)\approx21.6$, an asymmetry $\approx21.6/1.6\approx13.5\times$ **stronger** than
observed. This is still a real failure — the standard $(1+R)$ heuristic, not a
Boltzmann-code calculation — but it is a $\sim13.5\times$ miss, not the retracted
claim's $\sim426\times$ miss: a $\sim30\times$ improvement, tracking the position
result's own improvement closely (both come from the same corrected $R$).

**Reframing the verdict.** The corrected $R_\text{rec}\approx20.6$ is derived from this
model's own established Stefan-Boltzmann $c$-dependence (T18) plus baryon- and
photon-number conservation (both forced by $a=1$) — not from an ad hoc atomic-transition
analogy (the retracted $c^2$ convention) and not from an imported $\Lambda$CDM
adiabatic-cooling relation (the rejected $(1+z)^1$ alternative, `recombination_radius/`
session). It closes most, though not all, of both the position gap ($7.6\times\to
1.35\times$) and the height gap ($\sim400\times\to\sim13.5\times$). **The CMB no longer
looks like a clean, order-of-magnitude falsification on either front — it looks like a
real but much smaller residual tension**, on the same footing as the model's other
open, unresolved-but-not-fatal problems (T6/T14's $g_\dagger$ coefficient, T13's PBH
genesis question) rather than a standout catastrophic failure.

**The counting-law caveat, still real, still separately scoped.** The subcritical
branch's index $q\approx1.37$ is a fit to six DESI points at $z\le2.33$ (T23 §6); using
it at $z=1090$ is a $\sim3$-order-of-magnitude extrapolation that T23 §7 already
flagged as untrustworthy — this caveat is unchanged by anything in this section, since
it concerns the *distance factor*, not $R$. With the position miss now only
$1.35\times$, the $z_\text{rec}$ shift needed to close the remaining gap (holding $R$
fixed) is presumably far more modest than the old $z_\text{rec}\approx13$ figure — not
recomputed here, flagged as the natural next calculation (Open Questions).

**The higher-peak requirement, unaffected in statement.** The third-to-first peak
height ratio still needs a clustered, pressureless component present before
recombination — gravitating, pressureless, present before recombination, and
clustered. In $\Lambda$CDM this is cold dark matter. What does this model offer? (See
below — unaffected by this section's finding, since it concerns peak heights, not
position.)

### (D) Primordial Spectral Index

**Unaffected**, unworked in cdot-4 and still unworked: $n_s\approx0.96$ would need to
emerge from genesis (T13); no prediction currently exists under either counting law.

---

## The PBH Candidate: Dark Matter = Primordial Black Holes

**Unaffected in structure.** The clustered, pressureless wells needed for the higher
peaks are a natural output of PBH formation at genesis (T13). PBH properties vs. CMB
requirements (gravitating, pressureless, present before recombination, clustered) are
satisfied by construction, exactly as in cdot-4. The connecton field (T14) is
gravitating and pressureless but horizon-smooth, not clustered — PBHs remain needed for
the reason cdot-4 gave.

**PBH triple duty** — CMB higher-peak wells, galactic dark matter (T5, T15), SMBH seeds
via mergers — carries forward unchanged; none of these roles depends on the
cosmological counting law directly, only on T13's genesis mechanism, which is
separately flagged (below and in T13's cdot-5 rewrite) as needing re-examination for
different reasons.

---

## PBH Mergers and Supermassive Black Holes

**Unaffected**, unchanged from cdot-4: the merger-rate/mass-budget discussion (going
from asteroid-mass PBHs to SMBHs needs $10^{22}$–$10^{25}$ mergers) does not reference
the cosmological counting law. Still speculative, still a direction, not a result.

---

## The Load-Bearing Gate: PBH Formation at Genesis

**Updated using T13's cdot-5 finding, carried over rather than re-derived here.** The
constraint comes from $r_s/R\propto R^{2-2n}$ ($r_s=2GM_\text{horizon}/c^2$, invariant
$G$, $M_\text{horizon}\propto R^3$), where $n$ is the local counting-law exponent —
this derivation uses only ordinary uniform-density matter and *whatever* power law
locally describes $c(R)$, so it is well-posed for genesis (deep in the pre-percolation,
occupancy-type regime, T23) even though the *global* premise-2 fork it was originally
part of is retired (T12).

cdot-4's three named exponents (volume $n=3$: PBH genesis survives; surface $n=2$:
survives; S$'$ $n=2/3$: fails) were candidates for describing *all* of history and are
now understood as, at most, candidates for the pre-percolation regime specifically.
T13's cdot-5 rewrite computed a fourth data point: extrapolating T23's fitted
subcritical index ($q\approx1.37$) gives an implied $n_\text{eff}\approx1.35$, for
which the $r_s/R$ exponent is $2-2n_\text{eff}\approx-0.70<0$ — **Reading 2 would
tentatively survive** under this number, but it rests on the same untrustworthy
extrapolation flagged above and in T13, and should be weighted accordingly (i.e., not
much, independently of this section's own finding above).

**Two readings, unchanged from cdot-4:** Reading 1 (super-Schwarzschild forbids PBH
formation) vs. Reading 2 (preferred: the crossover at $r_s/R\sim1$ leaves overdense
relics as PBHs). The unproven step (whether an overdense lump cleanly collapses rather
than remaining a denser patch) remains the single highest-leverage open question,
gating CMB, galactic DM, and SMBH threads simultaneously — unaffected by anything in
this document.

---

## Current Status and Fit Assessment

| Ingredient | Status |
|---|---|
| (A) Thermal origin | Unaffected — $c$-threshold recombination, now with a derived (not asserted) rising $E_\text{ion}/k_BT_\text{eff}\propto c(t)$ crossing; thermalization mechanism (B) still unworked |
| (B) Blackbody thermalization | Unaffected — genuine difficulty, unworked |
| (C) First acoustic peak, plasma shape | Functional form unaffected; the epoch-invariant-$R$ claim (self-similarity) is **retracted** — its argument was void |
| (C) $R$ at recombination | **Corrected: $R_\text{rec}\approx20.6$** (was $680$; a rejected alternative gave $\sim5\times10^{-10}$), from $n_b,n_\gamma=$const $+$ this model's own Stefan-Boltzmann $c$-dependence, cross-checked against T18's independent stellar $T_\text{eff}\propto c$ result |
| (C) First acoustic peak, angular position | $\ell_1\approx298$, $1.35\times$ too high (was $7.6\times$ under the retracted $R\approx680$) |
| (C) Higher peak heights | $\approx13.5\times$ too strong odd/even asymmetry (was $\sim400\times$) |
| (D) Primordial $n_s$ | Unaffected — unworked |

**Both headline CMB failures shrank by roughly an order of magnitude** once $R$ was
rederived from the model's own established physics (T18's Stefan-Boltzmann scaling,
baryon/photon number conservation) instead of the void "$\rho_b,\rho_\gamma\propto c^2$"
self-similarity argument or an imported $\Lambda$CDM relic-cooling relation. The
remaining $1.35\times$ (position) and $13.5\times$ (height) misses are real, unresolved
tensions — the CMB is still the hardest test on the table — but they are no longer the
$\sim7.6\times$/$\sim400\times$ order-of-magnitude failures that made this look like a
clean falsification. The sharpest open question is no longer "is $R\approx680$
correct" (it clearly wasn't, and isn't) but "does the $n_b,n_\gamma=$const $+$
Stefan-Boltzmann derivation itself hold up," since $R_\text{rec}\approx20.6$ rests on
one still-unclosed subtlety (the mode-density/thermalization reconciliation flagged in
§C above).

---

## Open Questions

- **Resolved, and now resolved differently.** ~~Is $R\approx680$ correct at
  recombination?~~ No — retracted; its derivation was void. ~~Does the
  percolation-broken counting law, fit only to DESI, give a sensible CMB first-peak
  position when extended to recombination?~~ Once $R$ is corrected to
  $\approx20.6$, the distance law (unchanged, still the same extrapolation-flagged fit)
  gives a $1.35\times$ miss, not $7.6\times$ — substantially, though not completely,
  exonerated.
- **New top-priority question: does the $n_b,n_\gamma=$const $+$ Stefan-Boltzmann
  derivation of $R_\text{rec}\approx20.6$ actually hold up?** The baryon-number-conserved
  half is solid (forced by $a=1$, no live alternative). The photon-number-conserved
  half, and the resulting $T_\text{eff}\propto c$, is cross-checked against T18's
  independent stellar result but still rests on treating the photon population as
  re-evaluated by an equilibrium Planck formula at each epoch's own mode-density — not
  yet reconciled with premise 4's literal per-photon energy conservation (§C's
  caveat). Closing this would either confirm $R_\text{rec}\approx20.6$ on firmer
  footing or reveal a different value; either way it is now the load-bearing open
  question for this document, superseding "is $R\approx680$ correct."
- **New, actionable:** redo the $z_\text{rec}$ scan (previously: matching $\ell_1=220$
  at fixed $R\approx680$ needed an absurd $z_\text{rec}\approx13$) using the corrected
  $R_\text{rec}\approx20.6$ instead. Since the position miss is now only $1.35\times$,
  the required $z_\text{rec}$ shift is presumably far more modest and plausibly within
  reach of a real physical value — not computed here, since $R(z_\text{rec})$ and the
  distance factor both depend on $z_\text{rec}$ and need to be solved jointly, not
  independently as in the old scan.
- **Demoted, not dropped:** is there a third regime between DESI's redshift range and
  recombination that changes the subcritical branch's index before reaching the CMB?
  Still open, still worth deriving $q$ from first principles (T23), but secondary to
  the $R_\text{rec}$ derivation above — even a perfectly-derived distance law leaves
  most of the height failure untouched, since that depends on $R$, not the distance
  factor.
- Derive $z_\text{rec}$ within the model (item A) — still open, still circular (T16-A's
  $T_0(1+z_\text{rec})\approx3000$K check no longer applies as stated, since $T_\text{eff}
  \propto c$ replaces the kinematic $T\propto(1+z)$ relation; the $c$-threshold
  crossing condition of §A needs its own, not-yet-worked-out numerical check against
  $z_\text{rec}=1090$).
- Does genesis produce PBHs? (T13's own top open question, unaffected in status,
  compounded by the same extrapolation uncertainty noted there.)
- What is the PBH mass function from genesis? Unaffected, unchanged from cdot-4.
- What sets $n_s$? Unaffected, unworked.
- Can the blackbody thermalization requirement be met without compression heating?
  Unaffected, unworked.
- The PBH merger channel to SMBHs — unaffected, unchanged from cdot-4.
- **Double-counting with the baryon-only RAR (T15)** — unaffected by this document's
  findings; still open (T5, T6, T15).
