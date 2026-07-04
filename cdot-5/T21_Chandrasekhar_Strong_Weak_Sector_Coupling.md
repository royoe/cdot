# T21 — What Really Sets $M_\text{Ch}(c)$? The Strong/Weak Sector Coupling Problem

*Checked against the counting-law change. Parts 0–4 (the electron-capture/AIC bound,
the invariant-coupling-plus-Compton-wavelength principle, the weak-decay-rate
correction, and the plasmon-decay cooling rate) are all **present-value scalings** — how
a quantity depends on the instantaneous value of $c$, at fixed physical state, via
couplings ($\alpha$, $G_F$) and invariant masses fixed elsewhere in the model. None of
them reference $N$, $R$, or the horizon law, so **all four are confirmed unaffected**,
the same pattern established for T7/T8/T18. Part 5, which converts the plasmon-decay
rate into a white-dwarf cooling-age correction, **does** depend on cosmic history (via
T20's $c(\tau)$ relation) and is **redone** below with cdot-5's exact linear relation in
place of cdot-4's power law — the numbers turn out to be close to cdot-4's, for the same
reason T20 found its own tables close to cdot-4's. Cross-references T4 (Chandrasekhar-mass
candle systematic), T7 (fine-structure constant), T8 (invariant $G$), T13 (BBN), T18
($k_BT$ convention), T20 (white dwarf age ceiling, including its new percolation-break
validity boundary).*

---

## Why This Document Exists

T4 already flagged the problem this document tackles, in its own words: *"A second
unspecified input: the $^{56}$Ni weak-decay rate scaling. The model has fixed the EM
sector ($\epsilon_0\propto c^{-1}$) but not the weak sector."* T13 flagged the same gap
from the BBN side. This document is the dive into that gap, specifically as it bears on
$M_\text{Ch}$. The concern: naively applying $M_\text{Ch}\propto c^{3/2}$ (pure
$\hbar,c,G,m_p$ physics) to the SN Ia candle overcorrects the $q_0$ signal (T4).

**Bottom line, unchanged from cdot-4.** The electron-capture instability channel is
closed — a small, bounded correction *no matter what* is assumed about nuclear-sector
$c$-scaling. Plasmon decay, the dominant neutrino cooling process in degenerate cores,
is a second closed sub-calculation: its rate scales as $c^{-1}$ at fixed density, using
only two couplings already fixed elsewhere ($\alpha$, $G_F$). Turning that rate result
into an observable consequence (Part 5) gives the load-bearing finding: **standard
white-dwarf cooling ages systematically overstate the true age**. A narrower,
composition-specific channel (carbon ignition vs. Urca cooling) remains open and
secondary. A concrete, derived replacement for T4's ad hoc weak-decay-rate placeholder
is also proposed as a byproduct.

---

## Part 0 — What the Model Has Actually Fixed So Far

Unchanged from cdot-4 — every row is a statement about instantaneous physics, none about
the counting law:

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

---

## Part 1 — The Idealized $M_\text{Ch}\propto c^{3/2}$ Is Not Wrong — It's Answering a Slightly Different Question

Unchanged from cdot-4. The textbook Chandrasekhar mass,
$$M_\text{Ch} = \frac{\omega_3^0\sqrt{3\pi}}{2}\left(\frac{\hbar c}{G}\right)^{3/2}\frac{1}{(\mu_e m_H)^2},$$
scales exactly as $c^{3/2}$ under the model's already-fixed premises ($G,\hbar,m_p$
invariant) — T4's derivation of this piece is correct and is not revised here.

**But no real white dwarf ever reaches $\rho_c=\infty$.** Real stars are intercepted at a
finite critical density by one of two processes, both involving physics beyond
$\hbar,c,G,m_p$:

- **O/Ne/Mg-core white dwarfs**: intercepted by **electron capture** on $^{24}$Mg
  (onset $\rho_c\approx3$–$4\times10^9\ \text{g/cm}^3$) and then $^{20}$Ne
  ($\rho_c\approx1\times10^{10}\ \text{g/cm}^3$), triggering collapse before the
  idealized $M_\text{Ch}$ is reached ("AIC mass" $\approx1.37$–$1.39\,M_\odot$, one
  study quoting $1.48\,M_\odot$).
- **C/O-core white dwarfs**: intercepted by **carbon ignition**, at
  $\rho_c\approx1.5$–$5\times10^9\ \text{g/cm}^3$, on top of two convective-Urca-pair
  thresholds.

---

## Part 2 — Channel A: The Electron-Capture/AIC Threshold (a closed calculation)

Unchanged from cdot-4 — every step is instantaneous physics.

Electron capture, $(Z,A)+e^-\to(Z-1,A)+\nu$, turns on once the electron Fermi energy
reaches the nuclear threshold $Q_{EC}$:
$$\sqrt{p_{F,\text{crit}}^2c^2+m_e^2c^4}-m_ec^2 = Q_{EC}.$$
Writing $Q_{EC}\propto c^n$ for unknown $n$, in the relevant regime
($p_{F,\text{crit}}c\gg m_ec^2$):
$$p_{F,\text{crit}} \propto c^{n-1},\qquad \rho_\text{crit}\propto c^{3(n-1)},\qquad
x_c \equiv p_{F,\text{crit}}/(m_ec) \propto c^{n-2}.$$

**The key bound: this channel cannot produce a large correction, for any $n$.** Using
real threshold densities ($\rho_c\sim3\times10^9$–$10^{10}\ \text{g/cm}^3$), today's
$x_c\approx13$–$17$ is already deep in the asymptotic regime where $g(x_c)$ (the exact
Chandrasekhar mass-vs-density function) is within a few percent of $1$. Since $g$ is
bounded in $[0,1]$ and its approach is slow (power-law in $1/x_c^2$), no choice of $n$
turns this into an order-unity correction:
$$M_\text{crit}(c) = g\big(x_c(c)\big)\cdot M_{\text{Ch},0}\left(\frac{c}{c_0}\right)^{3/2},
\qquad g(x_c)\approx 0.97\text{–}0.99\ \text{(today)}.$$
This is still $\propto c^{3/2}$ to good approximation, regardless of the nuclear
sector's unknown $c$-scaling — safe to a few percent for T20's own age-ceiling formula.

**An elegant special case ($n=2$).** If nuclear mass-energy differences are invariant
*in mass (kg) units*, $Q_{EC}\propto c^2$, giving $x_c\propto c^0$: the dimensionless
relativity parameter at threshold is exactly invariant.

---

## Part 3 — A Candidate Unifying Principle: Invariant Couplings, Compton-Wavelength Scales

Unchanged from cdot-4 — a structural extension of T7's already-adopted EM-sector
pattern, entirely a statement about instantaneous physics:

> **Every fundamental interaction has an invariant dimensionless coupling, and every
> length scale it generates is a Compton wavelength $\hbar/(mc)$ of an invariant-mass
> particle.**

**Check: reproduces the EM sector (T7).** $\alpha$ invariant, Bohr radius
$a_B\propto\epsilon_0\propto c^{-1}$, Rydberg energy $E_\text{Ryd}\propto c^2$ — exactly
T7's result.

**Strong sector.** Nuclear radius $r_0\sim\hbar/(m_\pi c)\propto c^{-1}$ (pion Compton
wavelength, invariant $m_\pi$); the Coulomb term of the semi-empirical mass formula,
$E_C\propto c/r_0\propto c^2$; if the "strong fine-structure constant" is likewise
invariant, every nuclear binding-energy term (and every $Q$-value) scales as $c^2$
together — deriving, rather than merely asserting, T4's placeholder and validating the
$n=2$ case of Part 2.

**Weak sector.** $G_F/\sqrt2=g_w^2/(8M_W^2)$; if $g_w$ and $M_W$ are both invariant,
$G_F$ itself is invariant, full stop. Restoring $\hbar,c$ in the standard weak
decay-rate formula:
$$\Gamma \propto \frac{G_F^2\,(Qc^2)^5}{\hbar^7c^6}.$$
With $G_F$ invariant, $Q$ (mass units) invariant so $Qc^2\propto c^2$, and $\hbar$
invariant:
$$\Gamma \propto \frac{(c^2)^5}{c^6} = c^{4}.$$
**Correction to T4: weak decay rate $\propto c^4$, not $c^2$.** T4's rate-independent
total radiated energy bound, $E_\text{total}\propto c^{3/2}\cdot c^2=c^{7/2}$, is
unaffected (explicitly rate-independent). What is affected is the still-open
$q$-gated peak-luminosity route and the BBN weak-rate input in T13.

**Caveat, unchanged from cdot-4:** "invariant $g_w,M_W$" is *a* natural choice, not the
only one — flagged as an open flexibility, parallel to T8's standing debt for invariant
$G$/mass.

---

## Part 4 — Channel B: Neutrino Cooling Sets the Ignition Competition

### Part 4a — Plasmon Decay: the clean, composition-independent result

Unchanged from cdot-4 — the dominant neutrino-cooling process, $\gamma^*\to\nu\bar\nu$
(plasmon decay), depends only on $G_F^2$ and $1/\alpha$ — both fixed above, no separate
nuclear input:
$$\Gamma_{\gamma^*\to\nu\bar\nu} \propto \frac{G_F^2\,E_p^5}{\alpha\,\hbar^7c^6},
\qquad E_p=\hbar\omega_p,\qquad
\omega_p = \sqrt{\frac{4\alpha}{3\pi}}\,\frac{p_Fc}{\hbar}.$$
Holding the star's physical state fixed (fixed $p_F$, i.e. fixed density) and using
$\alpha$ invariant (T7), $G_F,\hbar$ invariant (Part 3): $E_p\propto c$, so:
$$\boxed{\Gamma_{\gamma^*\to\nu\bar\nu} \propto \frac{c^5}{c^6} = c^{-1}}$$
**Plasmon-decay neutrino cooling was more efficient by a factor $c_0/c(t)$ in the past.**
This is a present-value statement (a rate as a function of the instantaneous $c$ at
fixed density) and does not itself reference the counting law — what changes below
(Part 5) is only the conversion of "the past" into a specific $\tau$-dependent number,
which does depend on which counting law sets $c(\tau)$.

**Qualitative implication for the ignition competition — unchanged, still a direction
not a verdict.** Enhanced past cooling suggests either (i) single-degenerate SN Ia
progressively suppressed relative to AIC at earlier times, or (ii) SNe Ia that do occur
early ignite closer to the idealized $M_\text{Ch}(c)$ — reinforcing rather than relieving
T4's overcorrection concern. Requires the (undone) compressional-heating side of the
competition.

### Part 4b — Carbon Ignition vs. Urca Pairs (secondary note)

Unchanged from cdot-4 — not closed, not the recommended primary path, retained for
completeness only. See cdot-4 T21 Part 4b for the full statement of what remains to be
done (unaffected in scope by the counting-law change, since none of the required inputs
reference it either).

---

## Part 5 — From Plasmon Decay to a WD Cooling-Age Correction — Redone

*This is the one part of the document that converts a present-value rate scaling into a
statement about a specific white dwarf's age, and therefore the one part that needs the
counting law's $c(\tau)$ relation as an input. Redone here with T20's cdot-5 relation.*

### Getting the direction right — unchanged

A white dwarf's cooling age is inferred by comparing its observed luminosity to a
**standard cooling model** computed with no time variation. If early neutrino cooling
was enhanced, the real star is fainter at any given true age than the standard model
predicts, so inverting the observed (dimmer) luminosity through the standard curve gives
an inferred age **larger** than the true age. **Standard cooling ages overstate the true
age** — exactly the direction needed to ease T20's flagged ceiling violations.

### Converting a rate enhancement into an age correction — unchanged formula

Using the classical Mestel cooling law $L\propto t^{-7/5}$, $E\propto t^{-2/5}$: if a
fraction $\delta$ of the thermal reservoir is additionally removed by enhanced neutrino
losses,
$$\boxed{\frac{\Delta A}{A} \approx \frac{5}{2}\delta, \qquad \delta \equiv f_\nu(M)\times\left[\frac{c_0}{c(A)}-1\right]}$$
— the formula itself is unchanged; only the numeric input $c_0/c(A)-1$ changes, since it
now uses T20's cdot-5 relation, $c(\tau)/c_0=1-\tau/\tau_\infty$ ($\tau_\infty\approx27.9$
Gyr), in place of cdot-4's $3/4$-power law:

| Age $A$ (Gyr) | $c(A)/c_0$ | Plasmon enhancement, $c_0/c(A)-1$ |
|---:|---:|---:|
| 0.5 | 0.982 | 1.8% |
| 1 | 0.964 | 3.7% |
| 2 | 0.928 | 7.7% |
| 3 | 0.893 | 12.0% |
| 4 | 0.857 | 16.7% |
| 5 | 0.821 | 21.8% |
| 6 | 0.785 | 27.4% |
| 8 | 0.714 | 40.1% |

(Identical to T20's own table — both are the same calculation.) **These enhancement
percentages are, to within a percentage point, the same as cdot-4's** (1.8%, 3.7%, 7.8%,
12.3%, 17.2%, 22.7%, 28.8%, 43.5%) — the different exponent and different $\tau_\infty$
largely cancel, as they did for T20's $M_\text{Ch}(\tau)$ tables.

### The uncertain piece: $f_\nu(M)$ — unchanged

Genuine, mass-dependent, not derivable here without a real numerical cooling
calculation. Real literature bounds: $f_\nu\lesssim$ a few percent for ordinary-mass WDs
($M\sim0.6$–$1.0\,M_\odot$); climbing to perhaps $10$–$40\%$ for the highest-mass tail
($M\gtrsim1.1$–$1.3\,M_\odot$), based on Camisassa et al. (2019) and Fuentes et al.
(2021). **Illustrative (not derived) mass-dependent ansatz, unchanged:**
$f_\nu\approx0.02$–$0.05$ for $M\sim0.6$–$1.0\,M_\odot$; $f_\nu\approx0.1$–$0.2$ for
$M\sim1.0$–$1.2\,M_\odot$; $f_\nu\approx0.2$–$0.4$ for $M\sim1.2$–$1.35\,M_\odot$.

### Resulting age-correction estimates — recomputed

| Age $A$ (Gyr) | $f_\nu=0.05$ | $f_\nu=0.1$ | $f_\nu=0.2$ | $f_\nu=0.3$ | $f_\nu=0.5$ |
|---:|---:|---:|---:|---:|---:|
| 1 | 4.6 Myr (0.5%) | 9.3 Myr (0.9%) | 18.5 Myr (1.9%) | 27.8 Myr (2.8%) | 46.3 Myr (4.6%) |
| 2 | 19.3 Myr (1.0%) | 38.5 Myr (1.9%) | 77.0 Myr (3.9%) | 115.5 Myr (5.8%) | 192.5 Myr (9.6%) |
| 3 | 45 Myr (1.5%) | 90 Myr (3.0%) | 180 Myr (6.0%) | 270 Myr (9.0%) | 450 Myr (15.0%) |
| 4 | 83.5 Myr (2.1%) | 167 Myr (4.2%) | 334 Myr (8.4%) | 501 Myr (12.5%) | 835 Myr (20.9%) |
| 5 | 136 Myr (2.7%) | 273 Myr (5.5%) | 545 Myr (10.9%) | 818 Myr (16.4%) | 1363 Myr (27.3%) |

Within rounding of cdot-4's table (whose corresponding entries ran 5/9/19/28/47 Myr,
20/39/78/117/195 Myr, 46/92/184/277/461 Myr, 86/172/344/517/861 Myr, and
142/284/567/851/1418 Myr respectively) — **the recomputation changes essentially
nothing about T21's conclusions**, for the same near-cancellation reason found
throughout this pair of documents.

### Cross-check against T20's flagged violations — unchanged conclusion

Applying the ansatz to T20's specific ceiling-violating objects (using
$M_{\text{Ch},0}=1.44$):

- **Marginal violations** ($5$–$15\%$ excess, ages $\sim1.8$–$4.6$ Gyr, masses
  $1.11$–$1.31\,M_\odot$, $f_\nu\sim0.1$–$0.3$ plausible): $\Delta A/A\sim3$–$13\%$ —
  **plausibly enough to fully explain these on its own**.
- **Larger violations** ($1.37$–$1.53\times$ over, ages $\sim4$ Gyr): need
  $\Delta A/A\sim27$–$34\%$; even $f_\nu=0.5$ reaches only $\sim13$–$21\%$ — this
  mechanism alone is insufficient but removes roughly half the required gap.

All of these ages sit within T20's newly-identified valid regime ($\tau<9.1$ Gyr), so
none of Part 5's cross-checks are affected by the percolation-break caveat that now
retires T20 §D.

### What would turn this into a real number — unchanged

A trustworthy number needs a real WD cooling code with the plasmon-decay rate enhanced
by $[c_0/c(\tau)-1]$ at each epoch during the run (now using cdot-5's exact linear
relation rather than cdot-4's power law), accounting for crystallization, and checking
other neutrino-cooling channels' own $c$-scaling.

---

## Cross-Edits Needed Elsewhere

- **T4**: replace "decay rate $\propto c^2$" with the derived "decay rate $\propto c^4$"
  (Part 3); the robust $E_\text{total}\propto c^{7/2}$ bound is unaffected.
- **T13**: use $\Gamma_\text{weak}\propto c^4$ (Part 3) as the candidate input for the
  BBN $n\leftrightarrow p$ freeze-out weak rate; the deuteron-binding-energy input can
  use the same Part 3 principle ($\propto c^2$).
- **T20**: Part 2 shows the idealized $M_\text{Ch}(c)\propto c^{3/2}$ scaling used in
  T20's ceiling formula is safe to a few percent against the electron-capture/AIC
  correction, regardless of the counting law. Part 5's cooling-age correction table
  above **is** T20 §E's table — identical numbers, both derived from the same cdot-5
  $c(\tau)$ relation.

---

## Verdict

Unchanged from cdot-4 in substance. **Framing 1 (real, favorable progress).** Two of
three candidate corrections are closed calculations (Parts 2, 4a), both present-value
and both unaffected by the counting-law change. Turned into its cooling-age consequence
(Part 5), standard cooling ages plausibly overstate true ages by a few percent up to
$\sim10$–$20\%$ — recomputed here with cdot-5's exact $c(\tau)$ relation, and found to
change T21's numbers by less than a percentage point almost everywhere. **Framing 2
(honest and open).** Every quantitative result still rests on the Part 3 premise
(invariant couplings + Compton-wavelength length scales), a standing debt parallel to
T8's; $f_\nu(M)$ remains an illustrative ansatz, not a calculated quantity; Part 4b
remains unsolved. This document is a structural map, two closed sub-results, and one
genuinely promising but not yet numerically verified consequence — not a completed
resolution of either the SN Ia tension or T20's age-ceiling tension.

---

## Open Questions

1. **[Highest priority]** Replace Part 5's illustrative $f_\nu(M)$ ansatz with a real
   number: re-run a standard WD cooling code with the plasmon-decay rate enhanced by
   $[c_0/c(\tau)-1]$ (cdot-5's exact relation) at each epoch, for a grid of masses.
2. **[High priority]** Propagate Part 5's result into T20 — already done in this
   rewrite's cross-reference; a future numerical (non-illustrative) $f_\nu(M)$ would
   still need re-propagating.
3. Derive the compressional/gravitational heating-rate scaling with $c$ to complete
   Part 4a's ignition/collapse-competition question — unchanged from cdot-4.
4. Account for crystallization-phase complications in Part 5's estimate — unchanged.
5. Complete the Channel B (carbon-ignition-vs-Urca) calculation — unchanged.
6. Pin down the model's temperature-scaling convention ($k_BT\propto c^2$, T18) —
   unchanged, needed for Part 4a's full closure and Part 4b.
7. Test whether "invariant $g_w,M_W$" is consistent with T13's BBN calculation —
   unchanged.
8. Consider the alternative weak-sector choice (invariant Higgs vev, floating $M_W$) —
   unchanged.
9. Extend Part 3's strong-sector treatment beyond the Coulomb term (QCD running
   coupling) — unchanged.
10. Revisit the AIC real-mass numbers to pin down $g(x_c)$'s present-day coefficient —
    unchanged.
11. Once item 3 is derived, redo T4's Pantheon+ fit with the corrected $M_\text{crit}(c)$
    scaling — unchanged in scope, now feeding into cdot-5's own $q_0=0$ result (Core
    Principles §4a) rather than cdot-4's $q_0=1/(nP)>0$.
