# T4 — Supernovae and Cosmic Acceleration

## Observational Background

Type Ia supernovae (SNe Ia) are used as cosmological "standard candles": their peak
luminosities are approximately uniform (with empirical corrections via the
Phillips relation between peak brightness and decline rate, and colour), allowing
distances to be inferred from observed fluxes. The luminosity distance $D_L$ is:
$$\mu = 5\log_{10}\!\left(\frac{D_L}{10\ \text{pc}}\right), \qquad D_L = (1+z)D_\text{p}.$$

The 1998 discovery (Riess et al., Perlmutter et al.) that distant SNe Ia
($z\sim0.3$–$1$) appear $\sim0.2$–$0.3$ magnitudes **dimmer** than expected in a
matter-only decelerating universe was the primary evidence for cosmic acceleration and
the dark energy ($\Lambda$). The result has been confirmed and extended by the Pantheon
and Pantheon+ datasets (Scolnic et al. 2018, Brout et al. 2022), which together cover
$0<z<2.3$.

The inferred cosmological deceleration parameter for $\Lambda\text{CDM}$ is
$q_0\approx-0.55$ (with $\Omega_m\approx0.3$, $\Omega_\Lambda\approx0.7$), indicating
that the expansion of the universe is currently accelerating.

---

## The Model's Prediction: Marginal (Coasting) Deceleration

### The deceleration parameter

For the connectivity-counting law, $D_p(z)=(L/P)\ln(1+z)$ (Core Principles §4, general
mass-scaling exponent $P=s+2$), combined with the standard-candle luminosity distance
$D_L=(1+z)D_p$: expanding to second order in $z$,
$$D_L(z)=(1+z)\frac{L}{P}\ln(1+z)=\frac{L}{P}\left[z+\frac{z^2}{2}+O(z^3)\right].$$
Using $L/P=c_0/H_0^\text{obs}$ (Core Principles §4a — this ratio is independent of $P$,
since $P$ only rescales $L$ itself), this is
$$D_L(z)=\frac{c_0}{H_0^\text{obs}}\left[z+\frac{z^2}{2}+O(z^3)\right].$$
Comparing to the standard expansion $D_L=(c/H_0)[z+\tfrac{1-q_0}{2}z^2+\ldots]$:
$$\boxed{\,q_0=0\,}$$
**exactly, at leading order, for any mass-scaling exponent $P$.** This is a genuinely
different structural result from cdot-4's $q_0=1/(nP)>0$: the coefficient is fixed by
the exponential/logarithmic *functional form* of $D_p(z)$ alone, not by any exponent in
the counting law (there is no exponent left to tune — the connectivity law has only the
one scale $L$, which is degenerate with $H_0$ and drops out of $q_0$ entirely). The
model now sits exactly on the deceleration/acceleration boundary at leading order — a
marginal, "coasting" prediction, structurally analogous to the classic
$\Omega_m=2/3,\Omega_\Lambda=1/3$ reference cosmology, though arrived at through
completely different physics.

### Why cdot-4's "structurally impossible" argument no longer applies

cdot-4 could state, as a rigid structural fact independent of any fit, that $q_0<0$ was
impossible for any $n,P>0$ under the power-law counting family. **That argument does
not carry over.** With $q_0=0$ exactly at second order, whether the *full* $D_L(z)$
curve looks more like acceleration or deceleration over the range SN data actually probe
is no longer decided by a single sign at leading order — it depends on the higher-order
shape, which can only be assessed by fitting the full function against data (below), not
by inspecting one coefficient. This is a real loss of a previously clean argument, not a
detail to gloss over: **the model can no longer claim by construction that it is
distinguishable from acceleration in the way cdot-4 asserted.** What replaces it is an
actual, quantitative fit (below), which is the more honest test in any case.

---

## What This Means for the Model

The SN tension remains a serious single empirical constraint for the model, but its
severity has changed substantially with the new counting law (see the fit below):
cdot-4's $\Delta\chi^2=+195$ (Pantheon+, diagonal errors) falls to $\Delta\chi^2=+79$
under the connectivity law — a large, direct improvement, though still a formal
exclusion at face value.

**Framing 1 (pessimistic).** The Pantheon+ data robustly establish $q_0<0$ at
$>5\sigma$ within $\Lambda\text{CDM}$. This model no longer has a rigid structural argument
against mimicking that (previous section); the model-native fit below still disfavours
it, just less severely than before.

**Framing 2 (honest and open).** The $q_0<0$ conclusion still rests on SNe Ia being
standard candles to better than $\sim0.1$–$0.2$ mag precision over the full $z$ range,
and on Phillips/colour corrections and host-galaxy systematics that remain debated in
the wider community — none of this cdot-4 caveat has changed. The relevant statement is
now: **the model's SN tension shrank by more than half under the new counting law, on
identical data and identical fit methodology.** Whether that improvement is enough to
call the model viable depends on redoing the fit with the full covariance and folding
in the (unchanged, still-unresolved) Chandrasekhar-mass candle systematic below.

---

## Pantheon+ Fit Results (2026-07-04, cdot-5)

Script: `cdot-5/fit_pantheon.py`. Data: Brout et al. 2022 (`data/Pantheon+SH0ES.dat`). Sample: 1371
Hubble-flow SNe ($z>0.023$, Cepheid calibrators excluded). Fit strategy: for each model
a single nuisance parameter (absorbing $M_B+5\log_{10}H_0$) is fitted analytically as
the inverse-variance-weighted mean offset; the shape of $D_L(z)$ is the sole
discriminant. Errors are diagonal only (`MU_SH0ES_ERR_DIAG`); the full $1701\times1701$
stat+sys covariance matrix is on disk for future use, pending a reassessment of the
standard-candle physics with respect to the Chandrasekhar mass (below).

Model formula: $D_p(z)=(c_0/H_0)\ln(1+z)$, $D_L=(1+z)D_p$ — note this is *independent
of $P$* (Core Principles §4a), so there is no separate "$n$, $P$" choice to make the way
cdot-4's `dl_vsl(z, H0, P, n)` needed.

### $\chi^2$ summary (diagonal errors, dof$=1370$)

| Model | $q_0$ | $\chi^2/\text{dof}$ | $\chi^2$ | $H_0^\text{eff}$ [km/s/Mpc] |
|:---|---:|---:|---:|---:|
| $\Lambda\text{CDM}$ ($\Omega_m=0.30,\Omega_\Lambda=0.70$) | $-0.55$ | **0.4345** | 595.2 | 73.65 |
| **cdot-5 connectivity law** | $0$ | **0.4920** | **674.0** | **70.39** |
| $q_0=0$ coasting reference ($\Omega_m=2/3,\Omega_\Lambda=1/3$) | $0$ | 0.5659 | 775.3 | 69.74 |
| cdot-4 volume law | $+1/6$ | 0.5771 | 790.6 | 69.22 |

$$\boxed{\,\Delta\chi^2\ (\text{cdot-5}-\Lambda\text{CDM})=+78.8\,}
\qquad\text{vs. cdot-4's}\ \Delta\chi^2=+195.4\ \ (\Delta[\Delta\chi^2]=-116.6).$$

**The improvement is large and not a rounding effect.** Both fits use identical data,
identical methodology, and the identical one-nuisance-parameter treatment; only the
model's $D_L(z)$ shape changed. Two things stand out: (i) the connectivity law's
best-fit effective $H_0=70.4$ km/s/Mpc lands almost exactly on the reference value used
throughout this document, essentially by coincidence of the SN data's own preferred
normalization, whereas cdot-4's model wanted $H_0=69.2$; (ii) the connectivity law
**beats even the $q_0=0$ coasting reference** ($\chi^2=674.0$ vs. $775.3$) despite both
having $q_0=0$ at leading order — the full-shape difference beyond leading order (the
$\ln(1+z)$ curve vs. the coasting model's own $\Omega_m=2/3$ Friedmann shape) matters,
confirming the previous section's point that leading-order $q_0$ alone does not
determine fit quality.

### $\Delta\mu$ between the connectivity law and $\Lambda\text{CDM}$ (after best-fit offsets)

| $z$ | $\Delta\mu$ [mag] |
|----:|------------------:|
| 0.10 | $+0.044$ |
| 0.20 | $+0.001$ |
| 0.50 | $-0.084$ |
| 1.00 | $-0.134$ |
| 1.50 | $-0.132$ |
| 2.00 | $-0.111$ |
| 2.30 | $-0.094$ |

Compare cdot-4's own $\Delta\mu$ table at the same redshifts (which ranged from $+0.064$
at $z=0.1$ to $-0.270$ at $z=2.0$): the residual shape is qualitatively the same (small
near $z\approx0.2$, negative and largest in magnitude near $z\sim1$–$1.5$, easing at
high $z$) but roughly **half the amplitude** throughout. The model still predicts SNe
slightly brighter than $\Lambda\text{CDM}$ in the data-rich intermediate-$z$ range, which is
still the wrong direction relative to what the original 1998 discovery needed — but by
a substantially smaller margin than before.

### Interpretation

The connectivity-counting model is disfavoured relative to $\Lambda\text{CDM}$ at
$\Delta\chi^2\approx+79$ on the diagonal-error metric — still nominally excluded at
face value, but a categorically different situation from cdot-4's $+195$. As in cdot-4,
two steps remain before treating either number as definitive: repeating the fit with
the full stat+sys covariance matrix (not yet done, for either counting law), and
folding in the Chandrasekhar-mass candle systematic below, whose net sign is still
undetermined and could move this result in either direction.

---

## The Standard-Candle Assumption in the Model

This entire derivation is independent of the counting law — it depends only on
premises 3 (invariant mass) and 4 (photon frequency conserved in flight) and T18's
stellar-structure result, none of which reference how $c$'s cosmological history is
generated. Restated in full because it is the foundation the fit above rests on.

**Proper-time stretch.** Atomic clocks scale as $\nu\propto c^2$ (Core Principles §5a),
so the ratio of observation-epoch to emission-epoch proper duration per photon is
$d\tau_\text{obs}/d\tau_\text{emit}=(c_0/c_e)^2=(1+z)$. Time dilation here is derived
from clock-rate scaling and photon-number conservation, not metric expansion.

**Per-photon energy (the non-obvious step).** Premise 4 states the photon's absolute
frequency is conserved in flight. The emission-epoch clock ran slow by $(c_e/c_0)^2$
relative to today, so the proper emission frequency $\nu_e$ corresponds to absolute
frequency $\nu_o=\nu_e/(1+z)$ — and it is $h\nu_o$ that a detector deposits, not
$h\nu_e$. The apparent "redshift energy factor" is a proper-vs-absolute frequency
difference at the source, not an in-flight energy loss (premise 4 forbids the latter).
Misreading this step as $h\nu_e$ would give $D_L=(1+z)^{1/2}D_p$; the correct reading
restores $D_L=(1+z)D_p$.

**The observable.** Assembling bolometric flux ($h\nu_o$ per photon, arrival duration
stretched by $(1+z)$, spread over $4\pi D_p^2$) confirms $D_L=(1+z)D_p$. The actual
survey observable — peak specific flux $F_\nu$ plus K-correction — gives the same
result: at the instant of peak the rate-dilation $1/(1+z)$ and bandwidth $(1+z)$
cancel, leaving one power of $(1+z)$ from the per-photon energy alone. The K-correction
depends only on the frequency mapping $\nu_e=(1+z)\nu_o$ and the intrinsic SED shape,
both identical to FRW; SALT2/Pantheon+ pipelines apply unchanged.

**Why stellar luminosity drift does not affect the SN distance ladder in the general
case.** The SN flux chain runs entirely within the photon/atomic sector: emission
energy, photon frequency, and clock rate share the *same* power structure, so all
$c$-factors reassemble into the clean $(1+z)$ powers above. Gravity never enters the
photon's journey. With $L\propto c^0$ (T18: corrected Eddington/electron-scattering
mass–luminosity relation), ordinary stellar luminosity has no net $c$-drift at fixed
composition; any constant rescaling is absorbed into $M_B$ and introduces no
$z$-dependent terms.

**However, the SN Ia candle is not an ordinary star.** It detonates near the
Chandrasekhar mass, which carries its own $c$-dependence under invariant $G$ that is
*not* a constant offset and does *not* drop out of the Hubble-diagram fit — this is the
systematic below, and it too is independent of the counting law.

---

## The Chandrasekhar-Mass Candle Systematic

*Unaffected by the counting-law change — this entire section depends only on invariant
$G$, invariant $\hbar,m_p$, and the redshift law's $P=2$, none of which reference how
$c$'s cosmological history is generated. Restated in full; the physics and its open
question (the sign of $q$) are identical to cdot-4.*

### $M_\text{Ch}\propto c^{3/2}$

Type Ia SNe are standardisable because they detonate near the Chandrasekhar mass:
$$M_\text{Ch}\propto\left(\frac{\hbar c}{G}\right)^{3/2}\frac{1}{m_p^2}.$$
Under invariant $G$ (and invariant $\hbar,m_p$) with $c$ varying:
$$M_\text{Ch}\propto c^{3/2}.$$
In the past ($c$ smaller) the detonating mass — and hence the $^{56}\text{Ni}$ yield powering
the light curve — was smaller. With the redshift law $c_\text{emit}/c_\text{now}=(1+z)^{-1/2}$,
any candle quantity scaling as $c^k$ acquires a factor $(1+z)^{-k/2}$. Unlike a constant
offset, this is **$z$-dependent** and does not drop out of the fit. High-$z$ SNe Ia are
**intrinsically fainter** in the model than at low $z$.

### The robust bound: total radiated energy

The time-integrated bolometric output equals the nuclear energy released by the
$^{56}\text{Ni}\to^{56}\text{Co}\to^{56}\text{Fe}$ chain:
$$E_\text{total}=M_\text{Ni}\times(\text{energy per unit mass})\propto c^{3/2}\cdot c^2=c^{7/2}.$$
This is rate-independent and width-independent — the most trustworthy statement. As a
magnitude shift (positive = fainter at high $z$):
$$\Delta m=+\tfrac{5}{2}\cdot\tfrac{7}{4}\log_{10}(1+z)=+4.375\log_{10}(1+z).$$
Representative values: $+0.18$ mag at $z=0.1$; $+0.77$ mag at $z=0.5$; $+1.3$ mag at
$z=1$. There is no double-counting with the flux-chain factors above: those are
propagation/clock effects on the *same* photons; this is the *source* being
intrinsically weaker, so they multiply independently.

**Direction is favourable relative to the fit above** (the connectivity law's residual
still has SNe too *bright* at high $z$ relative to $\Lambda\text{CDM}$; this systematic dims
them, pushing the right way). **Magnitude taken raw overshoots massively** — far larger
than the residual actually available in the data ($\lesssim0.13$ mag in the connectivity
fit's own residual table above, smaller even than cdot-4's $\lesssim0.27$ mag window) —
and would, unmoderated, make the model predict SNe much too *faint*, worsening the fit
in the other direction.

### Whether Phillips standardisation absorbs the systematic

The raw dimming can only be reconciled with data if the Phillips width–luminosity
calibration absorbs most of it — i.e. the $M_\text{Ch}$ shift moves SNe *along* the
observed brighter–broader locus, so the pipeline calibrates it away. This hinges on the
**ejecta expansion velocity scaling** $v_\text{exp}\propto c^{-q}$. The light-curve
diffusion time scales as $\tau_\text{LC}\propto c^{(q/2-3/4)}$ (Arnett); the model's
track slope is:
$$\frac{d\log L_\text{peak}}{d\log\tau_\text{LC}}=\frac{17-2q}{2q-3}.$$
This matches the observed Phillips slope ($\sim+2$ to $+3$) only for $q\approx3.3$–$3.8$
(absorption works); for small or negative $q$ the slope is large-negative
(brighter–narrower, opposite to Phillips → no absorption → fit worsens).

**The sign of $q$ is currently not settled**, exactly as in cdot-4 — this question is
about stellar/nuclear physics at a given epoch, not about the cosmological counting
law, so nothing about the cdot-5 transition moves it either way:

- *Opacity argument (favourable, $q>0$):* lengths are larger in the past ($\propto c^{-1}$),
  so opacity is higher ($\kappa\propto c^{-2}$), coupling radiation more strongly and
  driving higher past expansion velocities — the direction that can yield
  Phillips-parallel behaviour.
- *Self-consistent radiation-hydro (unfavourable, $q=-1$):* closing the coupled system
  (impulse $a=\kappa F/c$, diffusion time, expanding radius, $E_\text{rad}\sim E_\text{nuclear}$,
  fixed kinetic fraction) gives $v_\text{exp}\propto c^{+1}$ ($q=-1$). Higher opacity
  increases trapping but also reduces flux; the net dynamics place the candle
  **off** the Phillips locus (fit worsens).

The two arguments address slightly different questions: the self-consistent solve held
the kinetic-energy fraction $f_\text{KE}$ fixed; the opacity argument implicitly lets
$f_\text{KE}$ rise with $\kappa$ (more trapping → more work on ejecta). The crux — the
opacity-dependence of the kinetic/radiated energy partition — is not settleable by
dimensional scaling alone and requires a radiation-hydrodynamics treatment.

A second input: the $^{56}\text{Ni}$ weak-decay rate scaling (T21): invariant $G_F$ (from
invariant $g_w,M_W$) plus invariant nuclear $Q$-values give energy per decay
$\propto c^2$ and decay rate $\propto c^4$. Even under this scaling the peak-luminosity
route is gated by $q$; the $E_\text{total}\propto c^{7/2}$ bound is independent of the
rate and unaffected.

### Effect on the fit (honest summary)

The Chandrasekhar-mass systematic adds a real, robust, $z$-dependent intrinsic dimming
on top of the kinematic curve — now the connectivity law's $q_0=0$ curve rather than
cdot-4's $q_0=+1/6$ curve, but the systematic itself is identical either way. Sign is
favourable; raw magnitude massively overshoots the *smaller* residual now available
(the connectivity fit leaves even less room to absorb it than cdot-4's fit did, since
the baseline tension is smaller to begin with). Net outcome is **still undetermined**:
resolving the sign of $q$ matters at least as much as it did in cdot-4, and arguably
more, since the connectivity law's improved baseline fit means this systematic is now
the dominant remaining lever on whether the model's SN tension closes further or
reopens.

---

## Tolman Surface-Brightness Test — Reclassified from "Non-Discriminating" to Real

*From cdot-4's deferred test battery (T23 Part III), which filed this under "explicitly
non-discriminating" on the assumption that Etherington reciprocity holds here and the
result therefore automatically matches $\Lambda$CDM. **That assumption is wrong** —
Etherington does not apply to this model's non-geodesic redshift (T16/Core Principles
§4, already adopted), and using the model's own actual $D_A\equiv D_p$, $D_L=(1+z)D_p$
relations instead of the borrowed $\Lambda$CDM ones gives a different, genuinely
discriminating prediction.*

Surface brightness of a standard-sized object scales as $\text{SB}\propto
L/(D_L^2\,\Omega)$ where the subtended solid angle $\Omega\propto(\text{size}/D_A)^2$,
so $\text{SB}\propto(D_A/D_L)^2$ (size and $L$ cancel for a population of standard
rulers/candles). In $\Lambda$CDM, Etherington reciprocity ($D_L=(1+z)^2D_A$) gives the
classic Tolman result $\text{SB}\propto(1+z)^{-4}$.

**In this model**, using $D_A\equiv D_p$ and $D_L=(1+z)D_p$ (both already established,
Core Principles §4, unaffected by the counting-law change):
$$\left(\frac{D_A}{D_L}\right)^2=\left(\frac{D_p}{(1+z)D_p}\right)^2=(1+z)^{-2}
\quad\Longrightarrow\quad\boxed{\,\text{SB}\propto(1+z)^{-2}\,}$$
— **half the exponent of $\Lambda$CDM's $(1+z)^{-4}$, not the same law "by
construction."** This is a clean, falsifiable, model-native prediction: standard
rulers (well-resolved cluster galaxies, e.g. Lubin & Sandage 2001-style programs) should
show markedly *less* surface-brightness dimming with redshift than $\Lambda$CDM
predicts, growing to a factor of $(1+z)^2$ difference by $z\sim1$–$2$. Not yet compared
against any actual measured Tolman-test dataset.

**What remains genuinely non-discriminating** (unaffected by this correction): SN
light-curve time dilation (any standard redshift mechanism predicts observed-duration
$\propto(1+z)$, matching data, and does not discriminate this model from $\Lambda$CDM)
and laboratory $\dot c$-drift searches (the real drift rate is far below any
achievable lab sensitivity). See `To_Do.md` for the short list of tests not worth
re-deriving.

---

## Open Questions

- **New, actionable:** compare the corrected Tolman prediction ($\text{SB}\propto
  (1+z)^{-2}$, above) against an actual surface-brightness-vs-redshift dataset — not
  yet done. This is now a real, standalone discriminating test, not a "passes by
  construction" bookkeeping item.
- ~~A direct Pantheon+ fit under the connectivity-counting law~~ **Done (2026-07-04):**
  $\Delta\chi^2=+78.8$ on diagonal errors, down from cdot-4's $+195.4$. Next: repeat with
  the full stat+sys covariance matrix (`data/Pantheon+SH0ES_STAT+SYS.cov`) to obtain a
  correctly normalised $\chi^2/\text{dof}$ and formal significance — not yet done for
  either counting law.
- **Resolve the sign of $q$** ($v_\text{exp}\propto c^{-q}$) — unchanged from cdot-4,
  now higher-priority given the smaller baseline residual leaves less room for error:
  does the opacity-dependence of the kinetic/radiated energy partition $f_\text{KE}(\kappa)$
  push $q$ into the Phillips-absorption window ($q\approx3.3$–$3.8$), or does the
  self-consistent radiation-hydrodynamics result ($q=-1$) win? Requires a radiation-hydro
  treatment that floats both dynamics and the energy partition simultaneously.
- **Redo the Pantheon+ fit with $M_\text{Ch}$ candle evolution included**, as a function
  of the net Phillips-absorbed fraction, restricted to the well-constrained
  $0.1<z<0.5$ window where data dominate; quantify whether any plausible $q$ yields a
  fit competitive with the connectivity law's own $\Delta\chi^2=+78.8$ baseline.
- **Standardisation observable:** does the Pantheon+ pipeline effectively standardise
  on peak luminosity or on fluence? The two carry different $c$-scalings
  ($L_\text{peak}$ vs. $E_\text{total}\propto c^{7/2}$) and the answer changes the net —
  unchanged question from cdot-4.
- What is the constraint on the mass-scaling exponent $s$ from SN data under the
  connectivity law? Since $D_L(z)$'s normalization is $P$-independent (this document,
  §"The Model's Prediction"), $P$ no longer shifts the *shape* the way it did in
  cdot-4's power-law family — a fit for $s$ would need to enter through the redshift
  law itself (T2) rather than through the counting law. Not yet examined.
- If the SN data firmly require a fit substantially worse than $\Lambda\text{CDM}$ even after
  model-native analysis and the full covariance, the model is excluded on this ground —
  this outcome should be pursued, not avoided, exactly as cdot-4 held.
- The Etherington-reciprocity finding (T16, carried into Core Principles §4: $D_A\equiv
  D_p$, no $(1+z)^2$ suppression) is unaffected by the counting-law change and does not
  need re-examination here — it was about the redshift mechanism, not the counting law.
