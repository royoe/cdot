# T7 — The Fine-Structure Constant

*Checked carefully against the counting-law change (Core Principles §1), as with T5/T6.
Result here is the opposite of T6's: **every claim in this document is confirmed
unaffected.** The reason is structural, not incidental — everything below depends only
on the ratio $c_\text{now}/c_\text{emit}$ *at a given redshift* $z$, which is fixed by
the squared redshift law ($P=2$, T2) alone. The redshift law does not reference the
counting law at all; the counting law only determines *how much cosmic time* elapsed to
reach a given $z$ (T1), which never enters any formula in this document. This is the
same separability T2 already established, now confirmed by direct inspection rather
than by analogy.*

## Observational Background

The fine-structure constant $\alpha$ characterizes the strength of the electromagnetic
interaction:
$$\alpha=\frac{e^2}{4\pi\epsilon_0\hbar c}\approx\frac{1}{137.036}.$$
It is dimensionless and appears in the splittings of atomic spectral lines, the Lamb
shift, the electron's anomalous magnetic moment, and the opacity of atoms to
electromagnetic radiation.

Because $\alpha$ is dimensionless, its value is independent of unit conventions. Any
change in $\alpha$ over cosmic time would alter the pattern of atomic spectra in a way
distinguishable from a simple Doppler or cosmological redshift — it would change *line
ratios*, not just line positions. This makes $\alpha$ variation a unique probe: it can
be measured from absorption-line spectra of quasars at high redshift without needing an
independent distance calibration.

### Current observational bounds

The most precise measurements use the Many Multiplet (MM) method applied to
high-resolution quasar absorption spectra. Key results:

- **ESPRESSO (VLT):** $\Delta\alpha/\alpha=1.3\pm1.3$ ppm at $z\sim1.15$
  (Martins et al. 2022). Consistent with zero variation.
- **Earlier Webb et al. (2011) claims** of a spatial dipole variation (at
  $\sim5\sigma$, with $|\Delta\alpha/\alpha|\lesssim10$ ppm) remain controversial and
  have not been confirmed by independent groups.
- **Overall constraint:** $|\Delta\alpha/\alpha|\lesssim$ a few ppm over $0<z<2$, and
  $\lesssim10^{-5}$ on laboratory timescales (optical clock comparisons).

Any model predicting $|\Delta\alpha/\alpha|>1$–$2$ ppm at $z\sim1$ is in tension with
ESPRESSO.

---

## The Model's Prediction: Classical $\alpha$ Invariance

### Why $\alpha$ is invariant at tree level

The fine-structure constant is:
$$\alpha=\frac{e^2}{4\pi\epsilon_0\hbar c}.$$
In this model:
- $e$ is invariant (premise 4).
- $\hbar=h/(2\pi)$ is invariant (premise 4).
- $\epsilon_0\propto c^{-1}$ (forced by electromagnetism — Core Principles §2).
- $c$ varies as $c(t)$.

Substituting $\epsilon_0\propto c^{-1}$:
$$\alpha\propto\frac{e^2}{\epsilon_0\hbar c}\propto\frac{e^2}{c^{-1}\cdot\hbar\cdot c}=\frac{e^2}{\hbar}=\text{const}.$$
The factors of $c$ and $c^{-1}$ cancel identically. **Classical $\alpha$ is exactly
invariant in this model.** This is not fine-tuned — it is forced by the same argument
that makes $\epsilon_0\propto c^{-1}$: the electromagnetic relation
$c=1/\sqrt{\epsilon_0\mu_0}$ fixes the product $\epsilon_0c$ once $c$ is chosen and
$\mu_0\propto c^{-1}$ (which follows from the symmetric split preserving
$Z_0=\sqrt{\mu_0/\epsilon_0}$).

**Why this is untouched by the counting-law change:** every ingredient above (premise
4's invariance of $e,\hbar$; the EM-forced $\epsilon_0\propto c^{-1}$) is a statement
about physics *at a given value of $c$*, with no reference to how $c$ got there or how
long it took. The counting law (Core Principles §1) governs the latter question
exclusively. There is nothing here for it to touch.

### The Bohr radius and atomic sizes

As a consequence, the Bohr radius
$$a_B=\frac{4\pi\epsilon_0\hbar^2}{m_ee^2}\propto\epsilon_0\propto c^{-1}$$
scales inversely with $c$. Atoms were physically **larger** when $c$ was smaller. At
$z=1$ (where $c_\text{emit}=c_\text{now}/\sqrt2$, from the squared redshift law, T2,
unaffected by the counting law), atoms were $\sqrt2\approx1.41$ times larger than
today — **exactly the same number as in every earlier iteration of the model**, because
it depends only on the redshift-to-$c$-ratio mapping (T2), not on the cosmic-time
history behind it.

This does not affect the fine-structure constant (it cancels in $\alpha$), but it does
affect lengths and cross-sections. It is consistent with the general scaling of all
length scales with $c^{-1}$ in the model.

---

## The Open Question: QED Corrections

The classical ($\alpha$-invariant) result is robust. However, the actual value of
$\alpha$ at any epoch includes radiative corrections from quantum electrodynamics
(QED) — the Uehling potential, vacuum polarization, and higher-order loops.

The leading vacuum-polarization correction to the effective coupling at a momentum
scale $q$ is of order $\alpha/(3\pi)\ln(q^2/m_e^2c^4/\hbar^2)$. If the electron's
Compton wavelength $\lambda_C=h/(m_ec)$ changes with $c$ (it does: $\lambda_C\propto
c^{-1}$), then the renormalization group running of $\alpha$ between two epochs could
introduce a small drift.

The relevant question: **does the QED effective coupling $\alpha(q^2)$, evaluated at the
atomic momentum scale $q\sim m_ec$, drift with cosmic time due to the changing Compton
wavelength?**

Multiple derivation attempts in earlier sessions produced inconsistent magnitudes, due
to errors in distinguishing additive from multiplicative perturbations. A clean
first-order calculation has not been completed — this remains true; the counting-law
change gives no new leverage on it either way, since (as below) the estimate depends
only on the $c$-ratio between two redshifts, not on the time elapsed between them.

**What is needed:** a systematic QED treatment in the background of varying $c$, keeping
track of which quantities are physical observables (transition energies,
cross-sections) and which are artifacts of the renormalization scheme. The drift, if
any, must be compared to the ESPRESSO bound of $|\Delta\alpha/\alpha|\lesssim1$–$2$ ppm
at $z\sim1$.

With $c$ changing by a factor of $\sqrt2$ from $z=1$ to today
($(1+z)^{-1/2}=1/\sqrt2$, so $c_\text{now}/c_\text{emit}=\sqrt2\approx1.41$, a
$\sim41\%$ increase — **unchanged from every earlier iteration, since it comes directly
from the squared redshift law alone**), the relevant log-change at the atomic scale
$q\sim m_ec$ is:
$$\Delta\ln\!\left(\frac{m_e^2c^4}{q^2}\right)=\Delta\ln(c^2)=\ln2\approx0.69.$$
A naive QED correction of order $\alpha/(3\pi)\sim7.7\times10^{-4}$ then gives:
$$\frac{\Delta\alpha}{\alpha}\sim\frac{\alpha}{3\pi}\ln2\approx5\times10^{-4},
\quad\text{or}\ \sim500\ \text{ppm}$$
— far above the ESPRESSO bound if correct. However, this estimate is speculative; the
actual QED correction in this framework needs careful treatment. **This entire estimate
carries over numerically unchanged**, because $\Delta\ln(c^2)$ is evaluated between two
*redshifts* (via the fixed $c_\text{now}/c_\text{emit}$ ratio), not between two *times* —
exactly the distinction that makes this document counting-law-independent.

---

## Observational Implications

Unchanged from cdot-4. If the model's QED correction is large ($\gg1$ ppm), it would be
**excluded by ESPRESSO**. This would be a clean, model-independent falsification. If the
QED correction is small ($\ll1$ ppm), the model is safe and in fact makes a clean
prediction: $\alpha$ is exactly invariant at the classical level, and any future
detection of $\alpha$ variation would challenge the model's premises.

The ESPRESSO constraint applies at $z\sim1.15$. More distant measurements (e.g., from
ALMA spectra at $z>3$) would probe larger changes in $c$ and therefore larger potential
QED corrections — this logic is entirely redshift-indexed and unaffected by the
counting-law change.

---

## The Proton-to-Electron Mass Ratio $\mu$ — A Free, Already-Passed Test

*From cdot-4's deferred test battery (T23 Part III), never previously recorded as a
passed test anywhere in the repository.*

$\mu\equiv m_p/m_e$ is independently constrained by molecular (ammonia, methanol)
absorption-line spectroscopy and by laboratory optical-clock comparisons, at the
$|\Delta\mu/\mu|\lesssim10^{-6}$–$10^{-7}$ level over cosmological baselines and
$\lesssim10^{-16}$/yr in the lab. In this model, $m_p$ and $m_e$ are **both invariant**
(premise 3, unchanged since cdot-3), so $\mu=m_p/m_e$ is invariant identically —
$\Delta\mu/\mu=0$, exactly, at every epoch, trivially inside every existing bound. This
costs nothing beyond premise 3 (already adopted for other reasons, T4/T8) and is
unaffected by the counting-law change, the same present-value-physics pattern as every
other result in this document. Not a derivation exercise — recorded here simply because
it was never written down anywhere before.

---

## Open Questions

Unchanged from cdot-4 — none of these are counting-law-sensitive:

- A clean first-order QED calculation of the running of $\alpha$ in a variable-$c$
  background. Specifically: does the Compton wavelength's change with $c$ feed into the
  renormalization group running in a way observable in atomic spectra?
- The ESPRESSO bound is the most stringent test currently available. A predicted
  $\Delta\alpha/\alpha$ as a function of $z$ would allow direct comparison.
- The Bohr radius $\propto c^{-1}$: are there observational consequences for atomic
  cross-sections or opacities at high redshift that could test this scaling?
- The symmetric split ($\epsilon_0=\mu_0=K\epsilon_0^{(0)}$) is the assumption that
  enforces $Z_0=$ const and hence $\alpha=$ const classically. An asymmetric split
  (e.g., only $\epsilon_0$ varying) would break $\alpha$-invariance at tree level. The
  polarization-alignment observational argument for the symmetric split should be
  examined more carefully.
