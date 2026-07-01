# T21 — What Really Sets $M_\text{Ch}(c)$? The Strong/Weak Sector Coupling Problem

*Status: speculative, structural map plus two closed sub-derivations. Cross-references T4
(Chandrasekhar-mass candle systematic), T7 (fine-structure constant), T8 (invariant $G$),
T13 (BBN), T18 ($k_BT$ convention), T20 (white dwarf age ceiling). Session: 2026-07-01.*

---

## Why This Document Exists

T4 already flagged the problem this document tackles, in its own words: *"A second
unspecified input: the $^{56}$Ni weak-decay rate scaling. The model has fixed the EM
sector ($\epsilon_0\propto c^{-1}$) but not the weak sector."* T13 flagged the same gap
from the BBN side: *"nuclear reaction rates also depend on $c$ (via the nuclear Gamow
energy, thermal velocities, and electromagnetic coupling)... A full BBN calculation
within the model's framework has not been done."*

This document is the requested dive into that gap, specifically as it bears on
$M_\text{Ch}$. The concern raised: naively applying $M_\text{Ch}\propto c^{3/2}$
(pure $\hbar,c,G,m_p$ physics) to the SN Ia candle overcorrects the $q_0$ signal (T4).
The suspicion is that $M_\text{Ch}$ is not, in real astrophysics, purely a gravity/electron-
degeneracy quantity — nuclear and weak physics enter, and we do not know how those
sectors couple to $c$. This document maps out exactly where that happens, does the pieces
of the calculation that close cleanly, and identifies where the genuinely open piece is.

**Bottom line in advance.** One candidate channel (electron-capture instability) is
closed — it is a small, bounded correction *no matter what* is assumed about
nuclear-sector $c$-scaling, so it cannot be where the SN overcorrection gets resolved. A
second, composition-independent channel — **plasmon decay**, the dominant neutrino
cooling process in degenerate cores — is a second *closed* sub-calculation: its rate
scales as $c^{-1}$ at fixed density, using only two couplings already fixed elsewhere in
this document ($\alpha$, $G_F$). Turning that rate result into an observable consequence
(Part 5) gives the genuinely load-bearing finding of this document: **standard
white-dwarf cooling ages systematically overstate the true age**, by an amount that
plausibly explains T20's marginal ceiling violations outright and meaningfully reduces
its larger ones. A narrower, composition-specific channel (carbon ignition vs. Urca
cooling) is identified but not closed, and is demoted to a secondary note. A concrete,
derived replacement for T4's ad hoc weak-decay-rate placeholder is also proposed as a
byproduct.

---

## Part 0 — What the Model Has Actually Fixed So Far

| Quantity | Model prescription | Established in |
|---|---|---|
| $G$ | invariant | T8 |
| $\hbar$ | invariant | Core Principles |
| $e$ (electric charge) | invariant | Core Principles |
| $\epsilon_0,\mu_0$ | $\propto c^{-1}$ (forced by $c=1/\sqrt{\epsilon_0\mu_0}$ + symmetric split) | Core §2 |
| $\alpha = e^2/4\pi\epsilon_0\hbar c$ | invariant (forced, exact cancellation) | T7 |
| Fundamental rest masses ($m_e,m_p,m_n$) | invariant | Core Principles, T8 |
| **Weak sector** ($G_F$, decay rates) | **unfixed before this document** | T4 (flagged open) |
| **Strong sector** (nuclear binding, hadron radii) | **unfixed before this document** | T13 (flagged open) |

The Chandrasekhar-mass problem sits exactly on top of the two previously-unfixed rows.
This document makes progress on both, specifically as they bear on $M_\text{Ch}$.

---

## Part 1 — The Idealized $M_\text{Ch}\propto c^{3/2}$ Is Not Wrong — It's Answering a Slightly Different Question

The textbook Chandrasekhar mass,
$$M_\text{Ch} = \frac{\omega_3^0\sqrt{3\pi}}{2}\left(\frac{\hbar c}{G}\right)^{3/2}\frac{1}{(\mu_e m_H)^2},$$
is the mass of the $n=3$ polytrope: the exact, ultra-relativistic-electron-gas
asymptote reached only as central density $\rho_c\to\infty$. Under the model's already-
fixed premises ($G,\hbar,m_p$ invariant), this quantity scales exactly as $c^{3/2}$ — T4's
derivation of this piece is correct and is not being revised here.

**But no real white dwarf ever reaches $\rho_c=\infty$.** Real stars are intercepted at a
finite critical density by one of two processes, both of which involve physics beyond
$\hbar,c,G,m_p$:

- **O/Ne/Mg-core white dwarfs** (the progenitors of most observed *ultra-massive* WDs,
  and of accretion-induced collapse, AIC): intercepted by **electron capture** on
  $^{24}$Mg (onset $\rho_c\approx3$–$4\times10^9\ \text{g/cm}^3$) and then $^{20}$Ne
  ($\rho_c\approx1\times10^{10}\ \text{g/cm}^3$), triggering collapse to a neutron star
  before the idealized $M_\text{Ch}$ is reached (Nomoto & Kondo 1991; Schwab et al. 2015,
  2017; the "AIC mass" is usually quoted around $1.37$–$1.39\,M_\odot$, a few percent
  below the idealized $1.4\,M_\odot$, though one recent EOS-dependent study quotes
  $1.48\,M_\odot$).
- **C/O-core white dwarfs** (classical single-degenerate SN Ia progenitors):
  intercepted by **carbon ignition**, at $\rho_c\approx1.5$–$5\times10^9\ \text{g/cm}^3$
  — a density range that sits right on top of two convective-Urca-pair thresholds
  ($^{23}$Na–$^{23}$Ne at $\log\rho\approx9.2$; $^{25}$Mg–$^{25}$Na at
  $\log\rho\approx9.1$; Iben 1978, Piro & Bildsten 2008, Schwab et al. 2016).

Both processes bring in the two unfixed sectors from Part 0: **nuclear binding-energy
differences (Q-values)** — strong + electromagnetic physics — and **weak-interaction
rates** — the Fermi constant $G_F$.

---

## Part 2 — Channel A: The Electron-Capture/AIC Threshold (a closed calculation)

### Setup

Electron capture, $(Z,A)+e^-\to(Z-1,A)+\nu$, turns on once the electron Fermi energy
reaches the nuclear threshold $Q_{EC}$ (ignoring the small nuclear recoil correction):
$$\sqrt{p_{F,\text{crit}}^2c^2+m_e^2c^4}-m_ec^2 = Q_{EC}.$$

### General scaling result

Suppose $Q_{EC}$ (an energy) scales as $Q_{EC}\propto c^n$ for some exponent $n$ to be
determined by the (currently unfixed) nuclear sector. In the relevant regime
($p_{F,\text{crit}}c\gg m_ec^2$, checked below), this gives
$$p_{F,\text{crit}} \propto c^{n-1} \quad\Rightarrow\quad
n_{e,\text{crit}} \propto p_{F,\text{crit}}^3/\hbar^3 \propto c^{3(n-1)}
\quad\Rightarrow\quad \rho_\text{crit}\propto c^{3(n-1)}$$
(using $\hbar, m_e, m_p$ invariant). The dimensionless relativity parameter at the
threshold, $x_c \equiv p_{F,\text{crit}}/(m_ec)$, is the quantity that actually controls
how close the star sits to the idealized $M_\text{Ch}$ asymptote:
$$x_c \propto c^{n-2}.$$

### The key bound: this channel cannot produce a large correction, for **any** $n$

The realized mass at threshold is $M_\text{crit} = g(x_c)\cdot M_\text{Ch}(c)$, where
$g(x)\in(0,1)$ is Chandrasekhar's exact mass-vs-central-density function, which
approaches $1$ monotonically as $x\to\infty$. Using the real threshold densities above
($\rho_c\sim3\times10^9$–$10^{10}\ \text{g/cm}^3$) and the standard relativity-parameter
normalization ($\rho_0\equiv$ density at $x=1$ is $\approx2\times10^6\,\mu_e\ \text{g/cm}^3$,
so $\mu_e=2$ gives $\rho_0\approx2\times10^6\ \text{g/cm}^3$): these densities correspond
to $x_c\approx13$–$17$ **today**, i.e. already deep in the asymptotic regime, where
$g(x_c)$ is empirically within a few percent of 1 (consistent with the real AIC mass,
$1.37$–$1.39\,M_\odot$, sitting only $\sim1$–$3\%$ below the idealized $1.40\,M_\odot$).
Since $g$ is bounded in $[0,1]$ and its approach to 1 is slow (power-law in $1/x_c^2$),
**no choice of $n$ can turn this into an order-unity correction** — at worst, pushing
$x_c$ down by a factor of a few (extreme choices of $n$ over cosmological $\Delta c$)
moves $g$ from $\sim0.98$ down toward, say, $\sim0.9$–$0.95$ at very early times — a
percent-level shift in the *coefficient*, not in the *exponent* of $M_\text{crit}(c)$.

**Robust conclusion:** the electron-capture/AIC channel gives
$$M_\text{crit}(c) = g\big(x_c(c)\big)\cdot M_{\text{Ch},0}\left(\frac{c}{c_0}\right)^{3/2},
\qquad g(x_c)\approx 0.97\text{–}0.99\ \text{(today), varying slowly},$$
i.e. **still $\propto c^{3/2}$ to good approximation, regardless of the nuclear
sector's unknown $c$-scaling.** This channel is not where the SN overcorrection problem
gets resolved. (It is, however, good news for T20: the age-ceiling formula there,
built on the same idealized $c^{3/2}$ scaling, is safe to a few percent from this
particular systematic.)

### An elegant special case ($n=2$)

If nuclear mass-energy differences are invariant *in mass (kg) units* — the natural
generalization of the model's existing "invariant rest mass" premise to composite nuclear
systems — then $Q_{EC}$ (an energy, $=\Delta m\cdot c^2$ with $\Delta m$ fixed) scales as
$Q_{EC}\propto c^2$, i.e. $n=2$. This gives $x_c\propto c^{2-2}=c^0$: **the dimensionless
relativity parameter at threshold is then exactly invariant** — the star always hits
electron capture at precisely the same fractional point on the mass-radius curve, at
every epoch. This is the cleanest possible version of the "robust, bounded" conclusion
above, and it emerges from the most natural extension of a premise the model has already
adopted.

---

## Part 3 — A Candidate Unifying Principle: Invariant Couplings, Compton-Wavelength Scales

Part 2's elegant $n=2$ case did not come from nowhere — it follows from extending a
pattern the model has *already used* for the electromagnetic sector (T7) to the strong
and weak sectors. Stating it explicitly, as a candidate new premise (not yet adopted):

> **Every fundamental interaction has an invariant dimensionless coupling, and every
> length scale it generates is a Compton wavelength $\hbar/(mc)$ of an invariant-mass
> particle.**

### Check: this exactly reproduces the EM sector (T7)

$\alpha=e^2/4\pi\epsilon_0\hbar c$ invariant (given), Bohr radius
$a_B=4\pi\epsilon_0\hbar^2/(m_ee^2)\propto\epsilon_0\propto c^{-1}$ (a Compton-like
length built from invariant $\hbar,e,m_e$ and the EM coupling), and Rydberg energy
$E_\text{Ryd}=m_ee^4/(2(4\pi\epsilon_0)^2\hbar^2)\propto\epsilon_0^{-2}\propto c^2$. This
is exactly the existing T7 result — the candidate principle is not new physics for the
EM sector, just a re-statement of what's already there.

### Extending to the strong sector: nuclear radii and binding energy

Take the nuclear radius scale to be a pion Compton wavelength,
$r_0\sim\hbar/(m_\pi c)$, with $m_\pi$ an invariant rest mass — exactly parallel to the
Bohr radius. Then $r_0\propto c^{-1}$. The Coulomb term of the semi-empirical mass
formula,
$$E_C = \frac{3}{5}\frac{1}{4\pi\epsilon_0}\frac{Z(Z-1)e^2}{r_0A^{1/3}} \propto
\frac{c}{r_0}\propto \frac{c}{c^{-1}} = c^2,$$
scales as $c^2$ — using only pieces the model has *already fixed* ($\epsilon_0\propto
c^{-1}$, $e$ invariant) plus the new length-scale assumption. If the analogous
"strong fine-structure constant" (whatever plays $\alpha$'s role in the volume, surface,
asymmetry, and pairing terms) is likewise invariant, **every term in the nuclear binding
energy scales as $c^2$ together**, and so does every $Q$-value built from differences of
them — confirming, and now *deriving* rather than merely asserting, T4's "energy per
decay $\propto c^2$" placeholder, and validating the $n=2$ case of Part 2.

### Extending to the weak sector: $G_F$ and the decay-rate correction to T4

Write $G_F/\sqrt2 = g_w^2/(8M_W^2)$ (Standard Model relation). If the weak coupling
$g_w$ (parallel to invariant $e$) and the $W$-boson mass $M_W$ (parallel to invariant
$m_e,m_p$ — extending "invariant rest mass" to fundamental bosons) are both invariant,
then **$G_F$ itself is an invariant number** — not "intrinsically $c$-invariant except
through time/energy scales" as T4 guessed, but literally constant, full stop.

This changes the derived decay-rate scaling. Restoring $\hbar,c$ in the standard (muon,
or any comparable 5th-power) weak decay-rate formula by dimensional analysis:
$$\Gamma \;\propto\; \frac{G_F^2\,(Qc^2)^5}{\hbar^7c^6}$$
(the unique combination of $G_F$, the released energy $Q c^2$, $\hbar$, and $c$ with
units of a rate — this is the standard restored form of the muon-decay formula,
$\Gamma_\mu=G_F^2m_\mu^5c^4/192\pi^3\hbar^7$, generalized to any weak decay with energy
release $Qc^2$). With $G_F$ invariant and $Q$ (in mass units) invariant — so $Qc^2\propto
c^2$, Part 3's own result — and $\hbar$ invariant:
$$\Gamma \propto \frac{(c^2)^5}{c^6} = c^{4}.$$

**Correction to T4: weak decay rate $\propto c^4$, not $c^2$.** The "energy per decay
$\propto c^2$" half of T4's placeholder is confirmed (and now derived); the "decay rate
$\propto c^2$" half is revised to $c^4$.

**What this does and does not change in T4.** T4's most trustworthy result — the
rate-independent total radiated energy bound, $E_\text{total}\propto M_\text{Ni}c^2_{\text{per
decay}}\propto c^{3/2}\cdot c^2=c^{7/2}$ — is unaffected, because it is explicitly
rate-independent. What *is* affected is the still-open, $q$-gated peak-luminosity/
light-curve-timescale route, and the BBN weak-rate input in T13.

**Caveat — this is a new premise, not a derivation from anything already in the model.**
Just as T8 flags "invariant $G$" and "invariant mass" as empirically-required but
theoretically underived choices, "invariant $g_w,M_W$" (equivalently, invariant $G_F$)
is *a* natural choice, not *the only* choice — one could instead hold the Higgs vacuum
expectation value invariant and let $M_W=g_wv/2$ float, or make other combinations
invariant, each giving a different $\Gamma(c)$. This is flagged as an open flexibility,
exactly parallel to the standing debts already recorded in T8.

---

## Part 4 — Channel B: Neutrino Cooling Sets the Ignition Competition

Whether a compressing degenerate core ignites (SN Ia) or collapses (AIC) before
reaching the idealized $M_\text{Ch}$ is set by a competition between compressional
heating and neutrino cooling. Two cooling processes were considered; they turn out to be
very different in tractability.

### Part 4a — Plasmon Decay: the clean, composition-independent result

The dominant neutrino-cooling process in a degenerate stellar core across a wide
swath of the relevant density–temperature plane is not the Urca process but **plasmon
decay**, $\gamma^*\to\nu\bar\nu$ (Adams, Ruderman & Woo 1963; Braaten & Segel 1993;
Itoh et al. 1989–1996). In a plasma, the photon acquires an effective mass from the
medium (the plasma frequency $\omega_p$), which makes the otherwise kinematically
forbidden decay to a neutrino pair possible. Two features make this a much better
candidate for a clean calculation than the Urca pairs of Part 4b:

- **It requires no composition-specific nuclear data.** Unlike Urca pairs (which need
  the trace abundance and exact threshold density of specific isotopes like
  $^{23}$Na/$^{23}$Ne), plasmon decay is a universal property of any degenerate electron
  plasma — it depends only on the electron density and two fundamental couplings.
- **Those two couplings are exactly the ones already fixed in this document.** The
  standard result (e.g. Braaten & Segel 1993; the compiled formula in Kachelriess et al.
  for the vector-current contribution) is
  $$\Gamma_{\gamma^*\to\nu\bar\nu} \;\propto\; \frac{G_F^2}{\alpha}\,\frac{Z\,\Pi^3}{\omega_p},$$
  where $Z$ is a dimensionless residue factor and $\Pi\sim\omega_p^2$ is the transverse
  plasmon self-energy at the pole — i.e. the rate depends on the weak sector only through
  $G_F^2$ and on the electromagnetic sector only through $1/\alpha$, with no separate
  nuclear input at all.

**The calculation.** Restoring $\hbar,c$ by the same dimensional-analysis method as
Part 3's muon-decay formula (matching powers so that $[G_F^2E_p^5/(\hbar^ac^b)]=1/\text{time}$
gives the identical exponents $a=7,\,b=6$):
$$\Gamma_{\gamma^*\to\nu\bar\nu} \;\propto\; \frac{G_F^2\,E_p^5}{\alpha\,\hbar^7c^6},
\qquad E_p\equiv\hbar\omega_p.$$
The plasmon energy itself, in the relativistic-degenerate limit relevant to a
near-$M_\text{Ch}$ core, is
$$\omega_p = \sqrt{\frac{4\alpha}{3\pi}}\,\frac{E_F}{\hbar} = \sqrt{\frac{4\alpha}{3\pi}}\,\frac{p_Fc}{\hbar}
\quad\Rightarrow\quad E_p=\hbar\omega_p \propto \sqrt{\alpha}\,p_Fc.$$
Holding the star's physical state fixed (fixed electron Fermi momentum $p_F$, i.e.
fixed density) and applying the model's scalings — $\alpha$ invariant (T7) and
$G_F,\hbar$ invariant (Part 3) — gives $E_p\propto c$, and therefore:
$$\boxed{\Gamma_{\gamma^*\to\nu\bar\nu} \;\propto\; \frac{c^5}{c^6} = c^{-1}}$$

**The plasmon decay rate is affected by a varying $c$, and the answer is clean and
unambiguous given the couplings already fixed elsewhere in the model.** At fixed
physical density, plasmon-decay neutrino cooling was *more* efficient by a factor
$c_0/c(t)$ in the past (small $c$), not less. This follows directly from $E_p\propto c$
(a fixed-momentum, relativistic energy grows with $c$, exactly as $E=pc$ demands)
combined with the steep 5th-power energy dependence of the weak-decay phase space, only
partially offset by the $c^6$ in the denominator from the dimensional restoration.

**Qualitative implication for the ignition competition (not a full answer).** Because
cooling was relatively *more* effective at fixed density in the past, a compressing core
in the deep past would need to be pushed to a *higher* density before compressional
heating could win against plasmon cooling. This suggests two possible consequences,
either a genuine, checkable prediction of the model: (i) the single-degenerate SN Ia
channel becomes progressively suppressed relative to AIC at earlier times/higher
redshift, testable via the SN Ia delay-time distribution and progenitor mix with
redshift; or (ii) SNe Ia that do occur at early times ignite closer to the idealized
$M_\text{Ch}(c)$ at their epoch, which would make the *realized* explosion mass track the
idealized $c^{3/2}$ curve **more** tightly in the past — reinforcing rather than relieving
T4's overcorrection concern. **This is a direction, not a verdict** — it requires the
compressional-heating side of the competition (not derived here) before either
consequence can be stated quantitatively.

### Part 4b — Carbon Ignition vs. Urca Pairs (secondary note)

Retained for completeness, but not expected to be the channel that resolves the
$M_\text{Ch}$ question — it is composition- and threshold-specific (only matters in the
narrow density window around particular isotope pairs), is already regarded as unsettled
even in mainstream, fixed-$c$ astrophysics, and does not offer the same clean, two-coupling
closure that plasmon decay does.

Unlike Channel A, this is **not** a "how close to a bounded asymptote" question. Carbon
ignition in a slowly-accreting C/O white dwarf occurs when the local heating rate from
gravitational compression first exceeds the local cooling rate from convective-Urca-pair
neutrino losses — a genuine **crossing point** between two physically distinct processes
with different scaling behavior:

- **Compressional heating rate**: gravitational in origin, set by the model's
  already-fixed $G$ and mass-accretion physics.
- **Urca cooling rate**: a weak-interaction process. The standard result (Tsuruta &
  Cameron 1970) is that the Urca neutrino energy-loss rate scales steeply with local
  temperature ($\propto T^4$ near threshold), with an overall normalization set by
  $G_F^2$ and the specific pair's nuclear matrix elements and threshold density
  ($^{23}$Na–$^{23}$Ne, $^{25}$Mg–$^{25}$Na).

Because this is a crossing point between two *differently-scaling* functions rather than
an approach to a fixed asymptote, a shift in the weak-rate normalization can shift *where
the two curves cross* by an amount not bounded the way Channel A's correction is. It is
also precisely the process real astrophysics still finds difficult even at fixed,
present-day $c$: convective Urca physics is described as "not well understood," requiring
dedicated 3D hydrodynamic simulation (Denissenkov et al. 2024, MAESTROeX-based work), and
SN Ia nucleosynthetic yields are demonstrably sensitive to hand-modifications of the weak
rates (Bravo 2019).

**This document does not close this calculation.** What can be stated is the concrete
shape of what's needed:
1. The strong-sector $Q$-value scaling for the specific Urca pairs, from Part 3's
   principle — expected $\propto c^2$, giving a shifted threshold density
   $\rho_\text{th}(c)$ via $\rho_\text{th}\propto c^{3(n-1)}$, $n=2\Rightarrow
   \rho_\text{th}\propto c^3$.
2. The weak-rate normalization, $G_F(c)$ — Part 3 proposes invariant; an alternative
   choice would give a different power.
3. **A temperature-scaling convention.** The Urca cooling rate's $T^4$ dependence
   requires knowing how the model's temperature scale ($k_BT$, an energy) scales with
   $c$ — the "$k_B$ convention" caveat already flagged in T18 ($T_\text{mol}\propto c^2$
   at fixed entropy/particle content), consistent with the "energy $\propto c^2$" pattern
   used throughout this document.
4. With (1)–(3) fixed, solve for the shifted crossing density $\rho_c^*(c)$, hence the
   shifted ignition mass $M_\text{ign}(c)$, and compare its $c$-scaling exponent against
   the idealized $M_\text{Ch}(c)\propto c^{3/2}$ used in T4's SN calculation.

This calculation is no longer the recommended primary path (Part 4a is), but remains a
well-enough-specified secondary correction for anyone extending this work.

---

## Part 5 — From Plasmon Decay to a WD Cooling-Age Correction

The point of Part 4a is not (only) that plasmon decay was faster in the past — it's what
that implies for how we *read* a white dwarf's age off its current luminosity. This part
works that out, and it is favorable for both T4 and T20, not neutral.

### Getting the direction right

A white dwarf's cooling age is inferred by comparing its observed luminosity/temperature
to a **standard cooling model** $L_\text{std}(t)$ — computed once, using today's physics
throughout, with no time variation. If a real star's early neutrino cooling was enhanced
relative to that standard assumption, the real star is **fainter at any given true age**
than the standard model predicts for that age ($L_\text{real}(A) < L_\text{std}(A)$,
since it shed extra heat early on). Because $L_\text{std}$ is a decreasing function of
age, inverting the *observed* (dimmer) luminosity through the *standard* curve necessarily
gives an inferred age **larger** than the true age:
$$A_\text{std} = L_\text{std}^{-1}\!\big(L_\text{real}(A_\text{true})\big) > A_\text{true}.$$
**Standard cooling ages overstate the true age.** This is exactly the direction needed:
every "ceiling violation" flagged in T20 used exactly these standard, no-time-variation
cooling ages, so if this effect is large enough, some or all of those violations could be
artifacts of over-aging, not real tension.

### Converting a rate enhancement into an age correction

The early neutrino phase is brief (Myr-scale) compared to total cooling ages (Gyr-scale)
— on its own, shortening *that phase's duration* is observationally irrelevant (the WD
cooling literature states explicitly that for ordinary-mass WDs, "the time necessary to
reach [the end of the neutrino-dominated phase] is $\le8\times10^7$ years for any model,
[so] its influence on the total cooling time is negligible"). **The effect that matters
is not the duration of the phase, but the *extra energy* it removes** — the star
subsequently cools along the same (slow, photon-dominated, Mestel-type) track, just
starting from a lower thermal reservoir, and that deficit persists and compounds for the
rest of the star's life.

Using the classical Mestel cooling law $L\propto t^{-7/5}$, so $E\propto t^{-2/5}$
(since $L=-dE/dt$): if a fraction $\delta$ of the thermal reservoir $E_0$ (relevant at
the start of the photon-dominated phase) is *additionally* removed by enhanced neutrino
losses, the star's state matches what a standard star reaches only after extra time
$\Delta A$ where $(1+\Delta A/A)^{-2/5}=(1-\delta)$, giving for small $\delta$:
$$\boxed{\frac{\Delta A}{A} \approx \frac{5}{2}\delta, \qquad \delta \equiv f_\nu(M)\times\left[\frac{c_0}{c(A)}-1\right]}$$
where $f_\nu(M)$ is the fraction of $E_0$ attributable to the *enhanced portion* of
neutrino cooling (mass-dependent — see below), and $[c_0/c(A)-1]$ is the plasmon-decay
rate enhancement at the star's own formation epoch (Part 4a), evaluated using T20's
established $c(\tau)$ relation:

| Age $A$ (Gyr) | $c(A)/c_0$ | Plasmon enhancement, $c_0/c(A)-1$ |
|---:|---:|---:|
| 0.5 | 0.982 | 1.8% |
| 1 | 0.964 | 3.7% |
| 2 | 0.928 | 7.8% |
| 3 | 0.891 | 12.3% |
| 4 | 0.853 | 17.2% |
| 5 | 0.815 | 22.7% |
| 6 | 0.776 | 28.8% |
| 8 | 0.697 | 43.5% |

### The uncertain piece: $f_\nu(M)$

This is a genuine, mass-dependent input this document cannot pin down precisely without
a real numerical cooling calculation, but real literature bounds its plausible range:

- For **ordinary-mass WDs** ($M\sim0.6$–$1.0\,M_\odot$), the neutrino phase is a small
  perturbation on the total energy budget — the literature's explicit statement that its
  influence on total cooling time is "negligible" suggests $f_\nu\lesssim$ a few percent.
- For **ultra-massive WDs** ($M\gtrsim1.1$–$1.3\,M_\odot$), neutrino cooling (plasmon
  decay, then increasingly Urca and bremsstrahlung) remains the dominant energy sink for
  much longer (Camisassa et al. 2019's own $1.16\,M_\odot$ model: neutrino losses "of
  about the same order of magnitude as the gravothermal energy release" persisting to
  $\log t\sim7$), and for $M\gtrsim1.33\,M_\odot$ the effect is dramatic enough that a
  $1.33\,M_\odot$ O/Ne model reaches $T_\text{eff}=46$ kK at a cooling age of only $70$
  Myr (Fuentes et al. 2021) — an acceleration that would be difficult to reconcile with
  $f_\nu\lesssim$ a few percent. This suggests $f_\nu$ climbing to perhaps
  $10$–$40\%$ for the highest-mass tail.

**Illustrative (not derived) mass-dependent ansatz**, consistent with the above
signposts: $f_\nu\approx0.02$–$0.05$ for $M\sim0.6$–$1.0\,M_\odot$; $f_\nu\approx0.1$–$0.2$
for $M\sim1.0$–$1.2\,M_\odot$; $f_\nu\approx0.2$–$0.4$ for $M\sim1.2$–$1.35\,M_\odot$.

### Resulting age-correction estimates

| Age $A$ (Gyr) | $f_\nu=0.05$ | $f_\nu=0.1$ | $f_\nu=0.2$ | $f_\nu=0.3$ | $f_\nu=0.5$ |
|---:|---:|---:|---:|---:|---:|
| 1 | 5 Myr (0.5%) | 9 Myr (0.9%) | 19 Myr (1.9%) | 28 Myr (2.8%) | 47 Myr (4.7%) |
| 2 | 20 Myr (1.0%) | 39 Myr (2.0%) | 78 Myr (3.9%) | 117 Myr (5.9%) | 195 Myr (9.8%) |
| 3 | 46 Myr (1.5%) | 92 Myr (3.1%) | 184 Myr (6.1%) | 277 Myr (9.2%) | 461 Myr (15.4%) |
| 4 | 86 Myr (2.2%) | 172 Myr (4.3%) | 344 Myr (8.6%) | 517 Myr (12.9%) | 861 Myr (21.5%) |
| 5 | 142 Myr (2.8%) | 284 Myr (5.7%) | 567 Myr (11.4%) | 851 Myr (17.0%) | 1418 Myr (28.4%) |

(Columns are $\Delta A$ in Myr, with $\Delta A/A_\text{true}$ in parentheses; read
$A_\text{std}\approx A_\text{true}+\Delta A$.)

### Cross-check against T20's flagged violations

Applying the illustrative ansatz to T20's specific ceiling-violating objects (using
$M_{\text{Ch},0}=1.44$, the generous bracket):

- **Marginal violations** (ratio $1.03$–$1.15$: SDSS J110054.91, J232257.27, J093710.25,
  J102553.68) sit at $5$–$15\%$ excess. At their ages ($\sim1.8$–$4.6$ Gyr) and masses
  ($1.11$–$1.31\,M_\odot$, so $f_\nu\sim0.1$–$0.3$ plausible), the table above gives
  $\Delta A/A$ of order $3$–$13\%$ — **plausibly enough to fully explain these on its
  own**, with no need to invoke the Gaia mass-revision systematic (T20 §A) at all.
- **Larger violations** (ratio $1.37$–$1.53$: SDSS J234044.83 at $53\%$ over,
  SDSS J100944.29 at $37\%$ over) need $\Delta A/A\sim27$–$34\%$. Even the generous
  $f_\nu=0.5$ column only reaches $\sim13$–$21\%$ at their ages ($\sim4$ Gyr) — **this
  mechanism alone is not sufficient**, but it removes roughly half of the required gap,
  meaning it would only need to *combine* with a modest (not extreme) mass-revision
  correction from the Gaia-recalibration issue in T20 §A to close the rest.

**Net effect on T20:** this mechanism, even taken as a rough order-of-magnitude
estimate, substantially changes T20's picture — it plausibly resolves the marginal
violations outright and meaningfully reduces (without fully closing) the larger ones,
*on top of* the already-identified Gaia spectroscopic-mass-bias issue. Combined, the two
effects make it considerably more plausible that few or none of T20's originally flagged
violations reflect genuine tension with the model.

### What would turn this into a real number

This is a scaling/energetics estimate, not a stellar-structure calculation. A trustworthy
number needs: (i) a real WD cooling code (e.g. re-running Bédard et al. 2020 or
Camisassa et al. 2019-style models) with the plasmon-decay rate enhanced by
$[c_0/c(\tau)-1]$ at each epoch $\tau$ during the run (not just at formation — the
enhancement factor itself evolves as the star ages toward the present), replacing the
hand-wavy constant-$f_\nu$ approximation; (ii) accounting for the fact that some old,
massive WDs are already in or near the crystallization phase (T20's discussion), which
changes the effective power-law this document assumed (pure Mestel) partway through the
star's life; (iii) checking whether other neutrino-cooling channels active at these
densities (bremsstrahlung, sub-dominant Urca) carry their own, possibly different,
$c$-scaling that should be added to the budget.

---

## Cross-Edits Needed Elsewhere

- **T4**: replace "decay rate $\propto c^2$" with the derived "decay rate $\propto c^4$"
  (Part 3); note the "energy per decay $\propto c^2$" half is now derived, not assumed
  (Part 3); note the robust $E_\text{total}\propto c^{7/2}$ bound is unaffected (rate-
  independent); flag that the still-open $q$-gated peak-luminosity route and the
  ignition-mass question (Part 4 here) are the paths forward, not the total-energy bound.
- **T13**: use $\Gamma_\text{weak}\propto c^4$ (Part 3) as the candidate input for the
  BBN $n\leftrightarrow p$ freeze-out weak rate, replacing the absence of any stated
  scaling; note the deuteron-binding-energy input to the BBN reaction network can use the
  same Part 3 principle ($\propto c^2$) as a first pass. Plasmon decay (Part 4a) is also a
  relevant neutrino-cooling process in the early universe and could be cross-checked
  against the same $\Gamma\propto c^{-1}$ (fixed-density) result derived here.
- **T20**: Part 2 shows the idealized $M_\text{Ch}(c)\propto c^{3/2}$ scaling used in
  T20's ceiling formula is safe to a few percent against the electron-capture/AIC
  correction. Part 5's cooling-age correction is a substantive, favorable revision:
  standard cooling ages (used throughout T20 §A/§C) overstate true ages, plausibly
  enough to fully explain T20's marginal ceiling violations and significantly reduce the
  larger ones. (Applied in T20 §E and its Verdict.)

---

## Verdict

**Framing 1 (real, favorable progress).** Two of the three candidate nuclear/weak-
physics corrections examined are now closed calculations. The electron-capture/AIC
threshold (Part 2) is bounded to a few percent regardless of nuclear-sector assumptions.
Plasmon decay (Part 4a) has a definite scaling, $\Gamma\propto c^{-1}$ at fixed density,
derived from the two couplings already fixed in this document. Turned into its
observable consequence (Part 5), this gives a genuinely useful result: because enhanced
past neutrino cooling makes real white dwarfs fainter, at any true age, than standard
(no-time-variation) cooling models predict, **standard cooling ages systematically
overstate true ages** — plausibly by a few percent up to $\sim10$–$20\%$ depending on
mass and age, using only an order-of-magnitude estimate of the one uncertain input,
$f_\nu(M)$. Checked directly against T20's flagged ceiling violations, this plausibly
resolves the marginal cases outright and cuts the larger ones roughly in half, working
*in addition to*, not instead of, the Gaia spectroscopic-mass-bias issue already
identified in T20 §A. A byproduct of this investigation — the "invariant coupling +
Compton wavelength" extension of the model to the strong and weak sectors — also
derives (rather than assumes) T4's "energy per decay $\propto c^2$," and corrects its
"decay rate $\propto c^2$" to $c^4$.

**Framing 2 (honest and open).** Every quantitative result in Parts 2, 4a, and 5 rests
on the Part 3 premise (invariant couplings + Compton-wavelength length scales) that is
natural but not the only possible choice — the same standing debt already carried by
invariant $G$/mass (T8). Part 5's headline numbers additionally depend on $f_\nu(M)$, a
mass-dependent fraction that this document bounds only qualitatively from real cooling
literature, not derives — it is an illustrative ansatz, not a calculated quantity. The
carbon-ignition/Urca-pair channel (Part 4b) remains unsolved and is no longer the
recommended focus. This document should be read as a structural map, two closed
sub-results (Parts 2 and 4a), and one genuinely promising but not yet numerically
verified consequence (Part 5) — not a completed resolution of either the SN Ia tension
or T20's age-ceiling tension, though it meaningfully improves the outlook on the latter.

---

## Open Questions

1. **[Highest priority, newly identified]** Replace Part 5's illustrative $f_\nu(M)$
   ansatz with a real number: re-run a standard WD cooling code (Bédard et al. 2020 or
   Camisassa et al. 2019-style) with the plasmon-decay rate enhanced by
   $[c_0/c(\tau)-1]$ at each epoch $\tau$ along the track, for a grid of masses, and
   read off the actual shift in inferred cooling age directly, replacing the
   energy-budget scaling estimate used here.
2. **[High priority]** Propagate Part 5's result into T20: revise T20's treatment of the
   flagged ceiling violations (§A, §C) to account for the plausible over-aging
   correction, and reassess how many of the original violations survive both this
   correction and the Gaia mass-revision issue combined.
3. Derive the compressional/gravitational heating-rate scaling with $c$ (from the
   model's already-fixed $G$ and the WD mass-radius relation) to complete Part 4a's
   original ignition/collapse-competition question, now secondary to Part 5's more
   directly useful cooling-age application.
4. Account for crystallization-phase complications (T20) in Part 5's estimate — many of
   the relevant old, massive WDs are at or past the onset of crystallization, which
   changes the effective cooling power-law partway through the star's life and was not
   modeled here (pure Mestel law assumed throughout).
5. Complete the Channel B (carbon-ignition-vs-Urca) calculation as a secondary check
   (Part 4b): obtain the explicit density/temperature-dependent forms of the Urca
   cooling rate from the specialist literature (Piro & Bildsten 2008; Lesaffre et al.
   2005/2006; Schwab et al. 2015/2017; Denissenkov et al. 2024), combine with the
   $c$-scalings proposed in Part 3, and solve for the shifted crossing density.
6. Pin down the model's temperature-scaling convention ($k_BT\propto c^?$) — needed for
   both Part 4a's full closure and Part 4b; T18 already adopts $T_\text{mol}\propto c^2$
   for the same reason, so this is a consistency check rather than an open choice.
7. Test whether "invariant $g_w, M_W$" (this document's weak-sector choice) is consistent
   with, or in tension with, any other part of the model — e.g. does it affect neutrino
   free-streaming or decoupling physics relevant to T13's BBN calculation in a way that
   creates new tensions?
8. Consider the alternative weak-sector choice (invariant Higgs vev, floating $M_W$) and
   whether it gives a distinguishable prediction anywhere before committing to the
   $G_F$-invariant choice made here.
9. Extend Part 3's strong-sector treatment beyond the Coulomb term: work out whether a
   genuine "invariant $\alpha_s$" analogue is well-defined given QCD's running coupling
   (unlike QED's $\alpha$, $\alpha_s$ runs significantly with energy scale even in
   standard physics — this may complicate the clean invariance argument used here for the
   volume/surface/asymmetry SEMF terms, which was asserted by analogy rather than shown).
10. Revisit the AIC real-mass numbers ($1.37$–$1.48\,M_\odot$ across different studies) to
    pin down a more precise present-day $g(x_c)$ coefficient for Part 2's bound.
11. Once the heating-rate side (item 3) is derived, redo T4's Pantheon+ fit with the
    corrected (not purely idealized) $M_\text{crit}(c)$ scaling in place of the naive
    $M_\text{Ch}\propto c^{3/2}$, to see whether the $q_0$ overcorrection is actually
    relieved.
