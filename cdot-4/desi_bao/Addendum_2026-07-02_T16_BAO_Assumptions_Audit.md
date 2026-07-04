# Addendum to the T16 BAO Update — Assumptions Audit: Where the Early Universe Does and Does Not Enter (2026-07-02)

*Session type: constructive (audit + one new constraint). Prompted by the author's
challenge: BAOs are frozen since recombination, the model's hot-plasma era is unworked,
and the assumption had been that energy scaling makes the initial conditions identical
to the standard model's — did the DESI test use different conditions, and is there a
misunderstanding? **Answer: the test's construction is confirmed correct, and it was
maximally charitable on precisely the physics the author is worried about.** The early
universe entered through exactly three assumptions, two of which are forced by
symmetry and staticity, and the third (the ruler's value) was marginalized. The
"identical initial conditions" intuition, taken literally, would make the result
catastrophically worse, not better. As a by-product, the audit yields the model's
first quantitative constraint on its own genesis epoch: to produce the required
~122 Mpc ruler, the acoustic/perturbation era must span only z ≈ 1290 → 1100.*

---

## 1. Re-Derivation of the Failing Quantity (no early physics anywhere in it)

The radial mapping was re-derived from scratch by chain rule:
$1+z = (c_0/c_e)^2$, $D = \int c\,dt \Rightarrow dD/dt_e = -c_e$, and
$\dot c_e/c_e = H_0^\text{hor}(1+z)^{-1/3}$ give
$$\frac{dz}{dD} = \frac{2(1+z)\,\dot c_e/c_e}{c_e}
= \frac{H_0^\text{obs}}{c_0}(1+z)^{7/6}\quad\text{(confirmed, third independent derivation).}$$
Every symbol in this expression is late-time: the counting law's horizon rate and the
propagation of light through the static map. **No plasma-era quantity can appear in
$dz/dD$ or in $D_p(z)$** — they are properties of the observation epoch's kinematics.
The discrepancy the data register is a discrepancy in these two functions.

## 2. Exactly Three Early-Universe Assumptions — Audited

The test assumed about the pre-recombination era only:

**(i) One intrinsic scale.** Standard for any acoustic feature; shared with ΛCDM
analyses; if the model produced multiple scales the fit could only get *worse*.

**(ii) Statistical isotropy of the imprint.** This is *not* an assumption about plasma
details — it is a symmetry theorem. At the imprint epoch, the plasma cannot know any
future observer's line of sight; homogeneity and isotropy of the static map force the
imprinted two-point function to depend on proper separation $|\Delta x|$ only.
Consequently, **any imprint physics whatsoever — identical to ΛCDM's, or arbitrarily
different — changes only the isotropic scale $L$, never the observed anisotropy.**
The AP channel compares the same frozen object along and across the line of sight at
the same redshift; $L$ cancels exactly. The early universe is common-mode in
$F_\text{AP}$ *by construction*. This is why the AP failure (χ² = 67.8/6, zero
parameters) is insulated from the author's concern.

**(iii) Frozen proper length after recombination.** Forced by the model's own premise:
static space, no expansion, linear-regime positions fixed. (The percent-level
nonlinear peak shift is common to both analyses.)

Everything else — the plasma equation of state, the energy scalings, the recombination
mechanism, the thermalization history, and above all **the value of $r_d$** — was
deliberately left free (the single nuisance $A$). Sanity check: the fitted 122 Mpc
frozen ruler reproduces the raw observed BAO angles (4.2° at $z=0.5$, matching ΛCDM's
4.3°); the failure is exclusively that the radial and transverse channels *demand
different rulers at the same redshift*, which no imprint can supply.

## 3. The "Identical Initial Conditions" Intuition, Taken Literally

The intuition was that energy scaling makes the model's initial conditions identical
to the standard model's, so the BAO should come out the same. Audited quantitatively,
this assumption *cannot* hold in the helpful sense, and in the literal sense it is
catastrophic:

- ΛCDM's $r_d = 147.1$ Mpc is a **comoving** length; at recombination it is a
  **proper** length of $147.1/1101 = 0.134$ Mpc.
- "Identical local physics at recombination" would imprint the *same proper scale*:
  0.134 Mpc. ΛCDM then stretches it ×1101 by today; the static model **freezes** it.
- A frozen 0.134 Mpc ruler is ~900× smaller than the ~122 Mpc the data require: the
  literal identical-ICs assumption fails the *normalization* by three orders of
  magnitude before the shape is even examined.

The marginalization of $r_d$ in the test was therefore maximal charity: it silently
excused the model from this normalization problem and judged it on shape alone — and
the shape is where it failed. There was no misunderstanding; the test gave the
early universe every benefit of the doubt it is possible to give.

## 4. By-Product: the Model's First Genesis-Epoch Constraint (new)

What *would* the model's own plasma era produce? In static space, the sound horizon is
$$L_s = \frac{1}{\sqrt3}\int_{t_\text{gen}}^{t_\text{rec}} c\,dt
= \frac{R(t_\text{rec}) - R(t_\text{gen})}{\sqrt3},$$
using $\int c\,dt = \Delta R$ (the horizon grows at $c$) and $c_s = c/\sqrt3$. With
$R(z) = R_0(1+z)^{-1/6}$ and the model's recombination at $z_\text{rec} \approx 1100$
(same local atomic threshold; $T(z) = T_0(1+z)$ holds exactly per the earlier
derivation): $R_\text{rec} = 8.0$ Gpc. Then:

- **Perturbations from the BBN epoch ($z \sim 10^{10}$):** $L_s = 4.3$ Gpc — ~35×
  *too large*.
- **To obtain the required $L_s = 122$ Mpc:** the acoustic/perturbation era must begin
  at $z_\text{gen} \approx 1290$ — i.e. span only $z \approx 1290 \to 1100$,
  $(1+z_\text{gen})/(1+z_\text{rec}) = 1.17$.

This is a sharp, previously-unavailable constraint on T16's genesis gate: **either the
model's perturbation genesis (the PBH-formation/structure-seeding epoch) sits at
$z \approx 1300$ — remarkably late, just before recombination — or the model's own
predicted ruler is Gpc-scale and the BAO normalization fails independently of the
shape.** Note the corollary either way: the "identical initial conditions" picture is
excluded within the model's own kinematics; its plasma era, whatever it is, is *not*
a relabeled ΛCDM plasma era.

## 5. The One Residual Channel, Restated Precisely

The single place where unworked model physics could still touch the measurement is
redshift-space distortions: the observed $\Delta z$ includes peculiar-velocity Doppler,
and the model has no computed velocity-field theory. Two points narrow this residual:
(a) DESI's pipeline *fits* the RSD amplitude rather than assuming ΛCDM's, and
reconstruction hardens the peak position, leaving template-shape systematics
controlled at 0.1–0.5%; (b) the rescue requires a coherent ~10% bias in the *peak
position* anisotropy at $z \approx 0.9$ — 20–100× the systematic budget — from a
velocity field the model has not yet proposed, in a framework (momentum-conserving
$u \approx$ const, no Hubble drag, no derived growing mode) with no evident source of
such coherence. Formally open; to close it either way the model must produce its own
$\xi(s,\mu)$. This remains escape route 1 of the main update, unchanged.

## 6. Consolidated Edits

| # | File | Edit | Type |
|---|------|------|------|
| 1 | T16 BAO section | Append this audit as an "Assumptions" subsection (§2's symmetry theorem; §3's normalization reductio) | Hardening |
| 2 | T16 §Genesis gate | Add the §4 constraint: $z_\text{gen} \approx 1300$ required for a 122 Mpc ruler; $L_s = (R_\text{rec}-R_\text{gen})/\sqrt3$ as the model's sound-horizon formula | **New result** |
| 3 | T16 | Note the corollary: the model's plasma era cannot be "identical initial conditions" — its ruler is either Gpc-scale or requires late genesis | Clarification |

**Bottom line.** The re-check confirms the test's construction: the early universe
entered only through a symmetry-forced isotropy, a staticity-forced frozenness, and a
fully marginalized ruler value — the plasma era, worked or unworked, cannot reach the
quantity that failed, which is the late-time mapping $dz/dD$ against $D_p(z)$. The
identical-initial-conditions assumption, examined quantitatively, would have added a
~900× normalization failure on top of the shape failure; marginalizing it away was
the charitable choice. The audit's silver lining is real, though: the model now has
its first quantitative statement about its own genesis epoch — $z_\text{gen} \approx
1300$ if a viable ruler is ever to come out — which is a concrete, falsifiable target
for T16's PBH-genesis gate, and an independent indication of how different from the
standard picture the model's early universe would have to be.
