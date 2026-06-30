# Change Document — T4 Supernovae: the $M_\text{Ch}\propto c^{3/2}$ Standard-Candle Systematic under Invariant $G$

**Date:** 2026-06-29
**Status:** New material / open tension. A downstream consequence of the invariant-$G$
adoption (companion *Change Document — Adoption of Invariant $G$*). Records a real,
robust $z$-dependent systematic in the Type Ia standard candle that invariant $G$
introduces, whose net effect on the SN fit is **currently undetermined** — gated by
physics the model has not yet specified. Also corrects one benign legacy statement in T4.
Suggested home: a new subsection in **T4** ("The Chandrasekhar-Mass Candle Systematic")
plus an Open-Questions entry; no change to the $q_0$ kinematic result.

---

## 1. Two separate edits to T4

**(a) Benign correction — the $L\propto c^4$ reference.** T4 §"The Standard-Candle
Assumption", final paragraph (the "Why T9's non-cancellation principle does not transfer"
note), states the stellar brightening is $L\propto c^4$. The luminosity audit (companion
*Paleo-Insolation* change doc) corrected this: bolometric luminosity is radius-independent
and scales as $L\propto c^0$ (Eddington/electron-scattering). For **ordinary stars** this
does not affect T4's argument (a constant luminosity rescaling is absorbed into the
absolute-magnitude calibration $M_B$, which the Pantheon+ fit marginalises). Replace
"$L\propto c^4$" with "$L\propto c^0$" and note the conclusion is unchanged.

**(b) Substantive — the SN Ia candle itself is not a fixed candle under invariant $G$.**
This is the real content, below.

## 2. The systematic: $M_\text{Ch}\propto c^{3/2}$

Type Ia SNe are standardisable because they detonate near the Chandrasekhar mass
$$M_\text{Ch}\propto \left(\frac{\hbar c}{G}\right)^{3/2}\frac{1}{m_p^2}.$$
Under **invariant $G$** (and invariant $\hbar, m_p$) with varying $c$:
$$M_\text{Ch}\propto c^{3/2}.$$
So in the past ($c$ smaller) the detonating mass — and the $^{56}$Ni yield that powers
the light curve — was **smaller**, making high-$z$ SNe Ia **intrinsically fainter**. With
the redshift law $c_\text{emit}/c_\text{now}=(1+z)^{-1/2}$, any candle quantity scaling
as $c^k$ acquires a factor $(1+z)^{-k/2}$. Unlike a constant luminosity rescaling, this is
**$z$-dependent** and therefore does **not** drop out of the Hubble-diagram fit — it is a
genuine standard-candle systematic that T4 did not previously account for.

## 3. The robust part: total radiated energy

Independent of decay rates and light-curve shape, the time-integrated bolometric output
equals the nuclear energy released by the $^{56}$Ni→$^{56}$Co→$^{56}$Fe chain:
$$E_\text{total}=M_\text{Ni}\times(\text{energy per unit mass})\propto c^{3/2}\cdot c^{2}
= c^{7/2}\propto (1+z)^{-7/4}.$$
This is **rate-independent and width-independent** — the most trustworthy statement.
As a magnitude shift, $\Delta m = +\tfrac{5}{2}\cdot\tfrac{7}{4}\log_{10}(1+z) = +4.375\log_{10}(1+z)$ (positive = fainter): about $+0.18$ at $z=0.1$, $+0.77$ at
$z=0.5$, $+1.3$ at $z=1$. Verified there is **no double-counting** with T4's flux chain:
T4's $(1+z)$ factors are propagation/clock effects; this is the *source* being
intrinsically weaker, so the factors multiply.

**Direction:** favourable in sign (T4's problem was the model predicting SNe slightly
*too bright* at high $z$; this dims them). **Magnitude:** taken raw, it **overshoots
massively** — far larger than the $\lesssim0.12$ mag residual it would need to close in
the data-rich $0.1<z<0.5$ window — and would make the model predict SNe much *too faint*,
**worsening** the fit. So the raw systematic is not a gentle correction; it is large.

## 4. What decides the net effect (and why it is currently undetermined)

The raw $E_\text{total}$ dimming can only be reconciled with the data if the **Phillips
standardisation** absorbs most of it — i.e. if the $M_\text{Ch}$ shift moves SNe *along*
the observed width–luminosity (brighter–broader) locus, so the pipeline calibrates it
away. Whether it does hinges on the **light-curve width scaling**, which depends on the
**ejecta expansion velocity** $v_\text{exp}\propto c^{-q}$:
- $\tau_\text{LC}\propto c^{(q/2-3/4)}$ (Arnett diffusion time);
- the model's track slope $d\log L_\text{peak}/d\log\tau_\text{LC}=(17-2q)/(2q-3)$;
- this matches the observed Phillips slope ($\sim+2$ to $+3$) only for $q\approx 3.3$–$3.8$
  (absorption works); for small or negative $q$ the slope is large-negative
  (brighter–narrower, opposite to Phillips → **no** absorption → fit worsens).

**The sign of $q$ is not settled.** Two physical arguments disagree:
- *Opacity/cross-section (favourable, $q>0$):* lengths are larger in the past
  ($\propto c^{-1}$), so opacity is higher ($\kappa\propto c^{-2}$), coupling radiation
  more strongly and driving **higher** past expansion velocities ($v_\text{exp}\propto c^{-q}$, $q>0$) — the direction that can yield Phillips-parallel behaviour.
- *Self-consistent radiation-hydro (unfavourable, $q=-1$):* closing the coupled system
  (impulse $a=\kappa F/c$, diffusion time, expanding radius, $E_\text{rad}\sim E_\text{nuclear}$, fixed kinetic fraction) gives $v_\text{exp}\propto c^{+1}$
  ($q=-1$) — the higher-opacity coupling is outweighed by longer trapping / lower flux,
  and the candle dimming is **not** absorbed (fit worsens).

These answer slightly different questions: the self-consistent solve held the
kinetic-energy *fraction* $f_\text{KE}$ fixed and floated the dynamics; the opacity
argument is really that $f_\text{KE}=f_\text{KE}(\kappa)$ rises with opacity (more
trapping → more work on the ejecta). The crux that divides them — the opacity-dependence
of the kinetic/radiated energy partition — is **not resolved**, and is not settleable by
dimensional scaling alone. Confidence: low-to-moderate on the specific $q=-1$; higher on
the meta-conclusion that the answer depends on unclosed radiation-hydrodynamics.

A second unspecified input compounds this: the $^{56}$Ni weak-decay rate scaling (the
model has fixed the EM sector via $\epsilon_0\propto c^{-1}$ but **not** the weak sector).
*Provisional working assumption (this session): the weak interaction is intrinsically
$c$-invariant except through the model's time and energy scales (decay rate $\propto c^2$,
energy per decay $\propto c^2$).* Even under this assumption the peak-luminosity route
remains gated by $q$; the **$E_\text{total}\propto c^{7/2}$ result is independent of it**.

## 5. Effect on $q_0$ (precise statement)

- The kinematic deceleration parameter $q_0=1/(nP)=+1/6$ (volume law) is **unchanged** —
  it is pure geometry, independent of $G$ and of the candle physics.
- What changes is the **predicted apparent magnitude of the candle** at each $z$: an
  intrinsic dimming term is added on top of the $q_0=+1/6$ curve. Including it does not
  alter $q_0$; it alters the Hubble diagram the model predicts.
- **Net outcome: undetermined.** Raw, the dimming overshoots and worsens the existing
  $\Delta\chi^2=+195$ (diagonal) tension. Whether Phillips standardisation rescues it
  depends on $q$ (sign unresolved) and on whether standardisation keys on peak luminosity
  or on fluence. The robust $E_\text{total}\propto c^{7/2}$ dimming persists regardless.

## 6. Honest summary

Invariant $G$ buys the LLR fix (companion doc) but, through $M_\text{Ch}\propto c^{3/2}$,
hands the SN sector a **real, robust, $z$-dependent intrinsic dimming** of high-$z$ SNe Ia
($E_\text{total}\propto(1+z)^{-7/4}$). The sign is favourable for the model's prior
too-bright tendency, but the magnitude is large and, taken raw, over-corrects and worsens
the fit. Reconciliation requires the Phillips standardisation to absorb most of the shift,
which depends on (i) the ejecta-velocity scaling $q$ (sign currently undetermined — a
self-consistent radiation-hydro solve gives the *unfavourable* sign, an opacity-partition
argument the *favourable* one) and (ii) the weak-sector $c$-scaling (provisionally assumed
benign). **Net effect on the SN fit: open.** This is logged as a genuine new tension
introduced by invariant $G$, not resolved.

## 7. Open questions (for the T4 Open-Questions list)

1. **Resolve the sign of $q$** ($v_\text{exp}\propto c^{-q}$): does the opacity-dependence
   of the kinetic/radiated energy partition $f_\text{KE}(\kappa)$ push $q$ into the
   Phillips-absorption window ($q\approx3.3$–$3.8$), or does the self-consistent dynamics
   ($q=-1$) win? Requires a radiation-hydrodynamics treatment that floats both the
   dynamics and the energy partition. **This single exponent gates SN viability.**
2. **Specify the weak sector's $c$-scaling** (currently assumed $c$-invariant except via
   time/energy). Needed for the peak-luminosity route and for BBN (next on the agenda).
3. **Redo the Pantheon+ fit with the $M_\text{Ch}$ candle evolution included**, as a
   function of the net absorbed fraction, restricted to the well-constrained $0.1<z<0.5$
   window where the data dominate; quantify whether any plausible $q$ yields a fit
   competitive with the current $\Delta\chi^2=+195$.
4. **Standardisation observable:** does the Pantheon+ pipeline effectively standardise on
   peak luminosity or on fluence? The two have different $c$-scalings
   ($L_\text{peak}$ vs $E_\text{total}\propto c^{7/2}$) and the answer changes the net.
