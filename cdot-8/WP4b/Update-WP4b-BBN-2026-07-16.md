# Update — WP4b: The e+e- Census Kink, Derived Properly, and a Leading-Order BBN Estimate

*Companion: `SessionLog-2026-07-16.md` (this directory, new). Executes WP4b,
gated per Foundation §6 item 5(a) on "actually computing the $e^+e^-$/QCD
kinks in census form (order-of-magnitude only so far)." Attempts that
derivation directly rather than continuing to patch in the standard result,
and catches two genuine errors of its own along the way before trusting any
number built on top of them.*

---

## 1. QCD transition: confirmed irrelevant to BBN, not attempted further

The QCD (quark-hadron) transition occurs at $T\sim150$–$200$ MeV; BBN's
weak-freeze-out and light-element formation happen at $T\sim0.05$–$1$ MeV —
more than two orders of magnitude in temperature, hence many more in redshift,
earlier. By the time BBN's physics runs, the QCD transition's only possible
residual effect is already frozen into the standard $g_*$/$N_\text{eff}$
bookkeeping this program already uses. **No separate census-form treatment of
the QCD transition is needed for WP4b**; it would only matter for physics at
temperatures BBN never probes.

## 2. The e+e- kink — two attempts, one wrong, caught before use

**First attempt, wrong**: treat $e^+e^-$ the same way as the neutrino mass
term (§2.4's massive-FD dispersion, $m_e(t)\propto c^{1/2}$, conserved
coordinate wavenumber). Numerically, this gives $u_{e^\pm}/u_\gamma$ *growing*
with $A=m_e/T$ instead of Boltzmann-suppressing toward zero — because that
formula assumes a **frozen, decoupled comoving distribution** (correct for
neutrinos, which decouple while relativistic and free-stream forever after)
— not correct for $e^\pm$, which stay in full thermal *and chemical*
equilibrium with photons via $e^+e^-\leftrightarrow\gamma\gamma$ and
genuinely annihilate away (comoving number density is not conserved).
Caught by the sign of the numerical trend before building anything on it.

**Second attempt, correct**: the true equilibrium Fermi-Dirac energy density,
with the *energy* (not momentum) in the exponent,
$$F_\text{eq}(A)=\int_0^\infty\frac{x^2\sqrt{x^2+A^2}}{e^{\sqrt{x^2+A^2}}+1}\,dx,$$
evaluated at the actual, shared photon temperature $T_\gamma(z)=T_{\gamma,0}
(1+z)$. Verified this reduces to the relativistic limit ($u_{e^\pm}/u_\gamma
\to\tfrac78\cdot4=3.5$ for $A\to0$) and Boltzmann-suppresses correctly
($F_\text{eq}(50)/F_\text{eq}(0)\sim10^{-19}$) — the right qualitative shape
for a species that disappears via annihilation, unlike the first attempt.

**A stated limitation, not resolved here**: using $T_\gamma(z)=T_{\gamma,0}
(1+z)$ throughout (including *during* the annihilation transition itself)
assumes the temperature-redshift relation holds exactly at all epochs, when
in fact the entropy dump from annihilating pairs causes small departures from
pure $\propto1/a$ scaling *during* the transition specifically (the same
physics standard BBN codes track via a properly time-resolved $g_{*S}(T)$,
and the reason $N_\text{eff}=3.044$ rather than the naive instantaneous-
decoupling value of $3$ is a small correction of this same character). Not
re-derived here — this is exactly the standard, invariant, already-known local
physics Foundation's own principle says should be imported rather than
rebuilt, and re-deriving it in full would mean reimplementing a precision
thermal-history code. Flagged as a leading-order, not final-precision,
treatment.

## 3. The photon-temperature boost itself: entropy conservation, not energy conservation

Separately from the energy-density term above: checked whether the
already-used $T_{\nu,0}=(4/11)^{1/3}T_{\gamma,0}$ (used throughout this
session's machinery) is actually justified by this framework's own stated
principle ("census continuity through energy-conserving conversions",
Foundation/ResearchNotes §20 item iv), or needs a sharper statement. **Naive
coordinate-energy conservation at the conversion gives the wrong exponent**:
$g_\text{before}T_\text{before}^4=g_\text{after}T_\text{after}^4$ gives
$T_\text{after}/T_\text{before}=(11/4)^{1/4}\approx1.288$, not the correct
$(11/4)^{1/3}\approx1.401$. The correct principle is **entropy conservation**
($g_\text{before}T_\text{before}^3=g_\text{after}T_\text{after}^3$) — valid
because the process is a bulk, many-body, adiabatic conversion, not the smooth
single-particle energy-conservation used for the neutrino mass threshold.
Entropy conservation is itself standard, invariant local thermodynamics
(per K1), so this is import-not-rebuild, same as $z_*$ in WP4a — but the
distinction from the framework's generic "energy-conserving conversions"
language is real and worth recording precisely rather than leaving the two
principles conflated.

## 4. Resulting $H(z)$ deficit at BBN, and a leading-order abundance estimate

With the corrected $e^\pm$ term included, cdot-8's own $E(z)$ (same
established closure trajectory, same census machinery as WP4a) gives, at
BBN-relevant temperatures:

| $T$ (MeV) | $H_{\hat\tau}/H_\text{SBBN}$ |
|---:|---:|
| $2.0$ | $0.96$ |
| $1.0$ | $0.95$ |
| $0.7$ | $0.93$ |
| $0.05$ | $0.94$ |

— consistent with, and now derived rather than order-of-magnitude estimated,
the previously-flagged $H/H_\text{std}\approx0.93$–$0.96$. Converting to an
effective $\Delta N_\text{eff}\approx-0.7$ at the representative ratio
$0.94$, and applying **standard, literature sensitivity coefficients** (not a
full reaction-network code — explicitly leading-order):
$$Y_p\approx0.238\ \text{(SBBN }0.247\text{, observed }0.245\text{)},\qquad
\text{D/H}\approx2.47\times10^{-5}\ \text{(SBBN }2.53\times10^{-5}\text{,
observed }2.55\times10^{-5}\text{)}.$$

**Reading**: $Y_p$ moves in the direction the observation favors (SBBN
overshoots slightly; cdot-8 undershoots) but by more than needed at this
leading-order estimate — a mild, not dramatic, tension, in the opposite
direction from SBBN's own small tension. D/H shifts slightly *away* from the
observed value, but by an amount ($\sim2\%$) well inside current observational
precision — not a meaningful discriminator either way. This updates the
qualitative picture from the WP4a discrepancy hunt (which used the
order-of-magnitude $\Delta N_\text{eff}\approx-0.5$): the more carefully
derived $-0.7$ shifts $Y_p$ somewhat further than "mildly favorable," into a
genuine but modest tension of its own — not resolving anything, not
worsening the overall picture dramatically either.

## 5. Status

**Not a full BBN confrontation** — this is leading-order, using standard
sensitivity coefficients rather than a reaction-network calculation
(PRIMAT/PArthENoPE-class code), which would be needed for a precision
verdict. What it does establish: the e+e- census kink is now derived, not
merely patched in, closing Foundation §6 item 5(a) for the piece that
actually matters at BBN energies; the QCD transition is confirmed irrelevant
to this epoch; the previously-estimated $H/H_\text{std}\approx0.93$–$0.96$
is confirmed by first-principles derivation, with a specific number
($-0.7$ effective $\Delta N_\text{eff}$) rather than a range. Two genuine
errors caught and fixed in the process (frozen vs. equilibrium distribution
for $e^\pm$; energy vs. entropy conservation for the temperature boost) —
consistent with this program's now well-established pattern of catching such
things before they propagate. Recommend: if BBN is to be pursued further,
a real reaction-network calculation is the next concrete step; otherwise this
stands as WP4b's leading-order result alongside WP4a's, both routed to the
same author-level assessment Foundation §6 item 6 already established for
this territory. The KATRIN clock remains the program's most time-critical
item; nothing in `cdot-7/` was touched.
