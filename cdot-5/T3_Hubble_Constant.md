# T3 — The Hubble Constant

## Observational Background

The Hubble constant $H_0$ quantifies the present-day rate of apparent recession of
distant galaxies: $v=H_0D$ at low redshift, where $v=cz$ is the apparent recession
velocity and $D$ is the proper distance. It is among the most precisely measured and
most contested quantities in cosmology.

Current measurements fall into two groups with a $\sim5\sigma$ tension:

- **Early-universe (CMB-based) methods:** Planck 2018 gives $H_0=67.4\pm0.5$ km/s/Mpc.
  This is derived by fitting the acoustic structure of the CMB power spectrum within
  the $\Lambda\text{CDM}$ framework; it is a model-dependent inference, not a direct
  measurement.
- **Late-universe (distance ladder) methods:** The SH0ES collaboration gives
  $H_0=73.04\pm1.04$ km/s/Mpc, anchored to Cepheid-calibrated Type Ia supernovae. This
  is a more direct geometric measurement but depends on calibration steps.

The discrepancy between these two values — the "Hubble tension" — is one of the most
discussed open problems in modern cosmology. It may indicate new physics, unresolved
systematic errors in one or both methods, or both.

---

## Two Hubble Constants in the Model

The model has **two distinct quantities** that both carry the label $H_0$, and
conflating them is a serious source of error — this structural point is unchanged from
every earlier iteration, only the formulas connecting them to the underlying counting
law have changed.

### Horizon rate $H_0^\text{hor}$

This is the fractional growth rate of $c$: $H_0^\text{hor}\equiv(\dot c/c)_0$. Under
connectivity counting (Core Principles §3), $c(R)=c_0e^{(R-R_\text{now})/L}$, so
$$H_0^\text{hor}=\frac{c_0}{L}.$$
This is a different relation from the old occupancy-counting law's $H_0^\text{hor}=3kR_0^2$ —
there, $H_0^\text{hor}$ depended on a horizon *radius* $R_0$ and a counting exponent;
here it depends only on the single recruitment length $L$. There is no longer a
meaningful "present horizon radius $R_0$" in the sense the old law had — $R$ is now
only a bookkeeping coordinate (only differences $R-R_\text{now}$ enter anything
physical), not a physical horizon size (Core Principles §3).

### Observable Hubble constant $H_0^\text{obs}$

This is what an astronomer measures from the low-$z$ redshift–distance slope. The
relation between the two Hubble constants, derived from the redshift law (T2) and the
low-$z$ expansion of $D_p(z)$, is
$$H_0^\text{obs}=P\,H_0^\text{hor},\qquad P=s+2,$$
**exactly the same relation as in every earlier iteration of the model** — this comes
from the mass-scaling exponent $P$, via the redshift law, and does not reference the
counting law at all (T2; verified directly for the new law in Core Principles §4a).
For invariant mass ($s=0$, $P=2$): $H_0^\text{obs}=2H_0^\text{hor}$, hence
$$L=\frac{2c_0}{H_0^\text{obs}}=\frac{c_0}{H_0^\text{hor}}.$$
Using $H_0^\text{obs}=70$ km/s/Mpc: $L\approx8.57$ Gpc. (Compare the old occupancy law's
$R_0=6c_0/H_0^\text{obs}\approx25.7$ Gpc — a different quantity playing a related
structural role, not a rescaled version of the same number; there is no "$\times3$" or
similar simple conversion between them.) When "$H_0=70$" is quoted, it is
$H_0^\text{obs}$, exactly as before.

### Physical meaning of $H$ in this model

Unchanged from every earlier iteration: in standard cosmology, $H$ is the rate of
expansion of space, $H=\dot a/a$. In this model, space is static; there is no $\dot a$.
Instead,
$$H\equiv\frac{\dot c}{c}.$$
The Hubble "constant" is the fractional rate of increase of the speed of light, not a
constant in time. Under connectivity counting, $H^\text{hor}(t)=c(t)/L$, and using
$c(z)=c_0(1+z)^{-1/2}$ (T2):
$$H^\text{hor}(z)=H_0^\text{hor}(1+z)^{-1/2}.$$
This falls with $z$ (the horizon rate was smaller in the past) — **a different power
from the old law's $(1+z)^{-1/3}$**, but the same qualitative statement: $H^\text{hor}$
is a present-day maximum in coordinate-rate terms, unrelated to the deceleration
question (T4), which concerns the *observable* distance–redshift relation, not this
coordinate-time rate.

---

## The Hubble Tension and This Model

The Hubble tension is a discrepancy within the $\Lambda\text{CDM}$ framework — between the
value of $H_0$ inferred from early-universe physics (CMB) and late-universe distance
measurements (distance ladder). This model offers a different conceptual framing, but
it does not automatically resolve the tension — this remains true under the new
counting law exactly as it was under the old one.

Within this model, the observable $H_0^\text{obs}$ is what the distance-ladder methods
measure directly from the redshift–distance slope. The CMB would need to be
reinterpreted within the model's framework (the CMB acoustic scale maps differently to
$H_0$ because the model's $H(z)$ history differs from $\Lambda\text{CDM}$'s) — this requires a
full CMB power-spectrum treatment, which remains a separate, only partially worked
program (see the CMB first-peak calculation carried over from cdot-4, flagged for
re-examination once T16 is rewritten for cdot-5 — not done here).

What is clear: the model's leading-order deceleration signature changed from cdot-4's
firm structural $q_0=+1/6>0$ to a marginal $q_0=0$ (T4) — a qualitatively different
starting point for asking whether the model's own late-time/early-time structure could
speak to the Hubble tension. No quantitative answer is available yet; this question is
at least as open as it was in cdot-4, and arguably reopened by the change in $q_0$.

---

## $H_0$ and the Proper Age

The proper age of the universe in the model is (T1)
$$\tau_\infty=\frac{2}{H_0^\text{obs}}.$$
The age–$H_0$ relation is therefore:
$$\boxed{\,\tau_\infty H_0^\text{obs}=2\,.}$$
Compare cdot-4's occupancy-counting value, $\tau_\infty H_0^\text{obs}=3/2=1.5$, and
$\Lambda\text{CDM}$'s concordance value, $\approx0.96$. The new law's product is **larger
still than cdot-4's**, meaning for the same $H_0$ the connectivity-counting model
predicts an even older universe than the occupancy-counting model did ($\approx27.9$ Gyr
vs. $\approx21$ Gyr for $H_0=70$; see T1 for the full discussion and the open question
of whether this larger age remains consistent with every other observational
constraint).

---

## $H(z)$: Comparison with $\Lambda\text{CDM}$, and Which $H(z)$ Actually Matters

This section carries forward cdot-4's own flagged ambiguity — **which $H(z)$
definition is the physically relevant one for comparing to BAO data** — and reports
how the ambiguity was, in practice, sidestepped rather than resolved when the actual
DESI comparison was carried out (T23; the counting-law replacement itself was selected
by fitting DESI's $D_M(z)$ and $D_H(z)$ observables directly, not by constructing a
"model $H(z)$" and comparing it to a literature value).

**Three distinct rate-like quantities exist in this model, and they are not the same
function of $z$:**

1. **Horizon rate** $H^\text{hor}(z)=H_0^\text{hor}(1+z)^{-1/2}$ — a coordinate-time
   rate, falls with $z$; not itself an observable.
2. **Proper-time-converted horizon rate**
   $H_\tau(z)\equiv H^\text{hor}(z)\,dt/d\tau=H_0^\text{hor}(1+z)^{-1/2}\cdot(1+z)
   =H_0^\text{hor}(1+z)^{1/2}$, i.e. $H_\tau(z)/H_\tau(0)=(1+z)^{1/2}$ — the
   direct analogue of cdot-4's own candidate BAO-comparison quantity (there,
   $(1+z)^{2/3}$), carried over here with the exponent that the new counting law
   actually gives, but **still not independently justified as the right clock for BAO
   purposes** — exactly the gap cdot-4 flagged and never closed.
3. **The AP-relevant observable** $H_\text{obs}(z)\equiv c_0/D_H(z)$, where
   $D_H(z)=dD_p/dz$ is literally the radial BAO distance (Core Principles §4a):
   $$H_\text{obs}(z)=H_0^\text{obs}(1+z).$$
   This is the quantity that is actually fit against DESI data (via $D_M,D_H$
   directly — T23, `autocatalytic_counting/`), and it is **linear in $(1+z)$, not
   $(1+z)^{1/2}$** — a genuinely different function from $H_\tau(z)$ above, by
   construction (they answer different questions: $H_\tau$ asks how fast the horizon
   grows per unit of a clock's own proper time; $H_\text{obs}$ asks what an observer
   infers from the ratio of two actual geometric distances).

| $z$ | $H_\tau(z)/H_\tau(0)$ | $H_\text{obs}(z)/H_\text{obs}(0)$ | $H(z)/H_0$ ($\Lambda\text{CDM}$) |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 0.5 | $1.5^{1/2}\approx1.22$ | $1.5$ | $\approx1.32$ |
| 1 | $2^{1/2}\approx1.41$ | $2.0$ | $\approx1.72$ |
| 2 | $3^{1/2}\approx1.73$ | $3.0$ | $\approx2.60$ |

**The practical resolution, in this document's honest reading:** the actual BAO
confrontation that selected the connectivity law (T23) never needed to pick between
$H_\tau$ and $H_\text{obs}$ — it fit the geometric observables $D_M(z)=D_p(z)$ and
$D_H(z)=dD_p/dz$ directly against DESI's own tabulated $D_M/r_d$, $D_H/r_d$ values,
which is unambiguous. The "which $H(z)$" question above is a real, still-open
*conceptual* question (what does a clock-based cosmic-chronometer measurement, as
opposed to a BAO geometric measurement, actually probe in this model?) but it is not a
gating one for the fits already performed, since those used the geometric distances,
not a constructed $H(z)$.

---

## Redshift Drift (Sandage–Loeb) — Recomputed, an Exact Null Result

*From cdot-4's deferred test battery (T23 Part III), which quoted an old-law formula
that does not carry over. Redone here from scratch for the connectivity law.*

For a source at fixed proper distance $D_p$ (static map — the source does not move),
light continuously emitted arrives at the observer at coordinate time $t_o$; the
emission time $t_e(t_o)$ is fixed by $D_p=\int_{t_e}^{t_o}c(t')\,dt'=$const. Using the
closed form $c(t)=L/(t_*-t)$ (Core Principles §3):
$$D_p=L\ln\!\left(\frac{t_*-t_e}{t_*-t_o}\right)\quad\Longrightarrow\quad
\frac{t_*-t_e}{t_*-t_o}=e^{D_p/L}\equiv K\ \ (\text{a constant, independent of }t_o).$$
The redshift is $1+z(t_o)=(c(t_o)/c(t_e))^2=\left(\frac{t_*-t_e}{t_*-t_o}\right)^2=K^2$
— **exactly constant in $t_o$**, for any fixed source. Hence
$$\boxed{\,\dot z\equiv\frac{dz}{dt_o}=0\ \text{identically, at every redshift}\,}$$
not an approximation and not restricted to low $z$ — a direct, exact consequence of the
hyperbolic form $c(t)=L/(t_*-t)$ (verified independently via the general Sandage-Loeb
identity $\dot z=(1+z)H_0^\text{obs}-H_\text{obs}(z)$, which vanishes identically given
this document's own $H_\text{obs}(z)=H_0^\text{obs}(1+z)$ above — both routes agree).

**A much sharper, cleaner prediction than cdot-4's version.** cdot-4's occupancy law
gave $\dot z=H_0^\text{obs}(1+z)[1-(1+z)^{1/6}]$ — always negative, no zero crossing,
but a nonzero magnitude requiring a sensitivity comparison against instrument noise.
cdot-5's prediction is not "small" or "a different sign" — it is **exactly zero, at
every redshift, to all orders**. Any confirmed nonzero redshift drift, of either sign,
at any $z$, directly falsifies this branch of the model; conversely, a null result
(indistinguishable from zero within instrument error) is a clean pass, distinguishable
in principle from $\Lambda$CDM's own predicted sign-changing drift (zero crossing near
$z\approx2.5$) at any redshift where the two differ by more than instrument noise.
Instruments: ELT-ANDES (2030s–2040s, optical), CHIME/HIRAX 21cm ($z\lesssim2$).

**Caveat.** This result is specific to the post-percolation branch's exact functional
form; it says nothing about drift measurements reaching past $z_*\approx1.2$ into the
undetermined pre-percolation regime (T23) — not addressed here.

---

## Open Questions

- **The cosmic-chronometer clock-choice question — partially resolved.** Using the
  already-derived $H_\tau(z)/H_\tau(0)=(1+z)^{1/2}$ and $H_\text{obs}(z)/H_\text{obs}(0)
  =(1+z)$ above: **if** a direct cosmic-chronometer measurement (differential stellar
  ages) actually recovers $H_\tau(z)$ rather than $H_\text{obs}(z)$ — itself still the
  open, unresolved half of this question — then chronometer-$H$ and BAO-$H$ must
  disagree by exactly
  $$\frac{H_\text{obs}(z)}{H_\tau(z)}=(1+z)^{1/2},$$
  a distinctive, falsifiable split with no $\Lambda$CDM analogue (there the two agree
  by construction). This closes the "what's the predicted split" half of the deferred
  test-battery item (T23 Part III) but not the "which clock does a chronometer actually
  measure" half, which remains exactly as open as stated above.
- **A full BAO-data comparison at the level of individual $H(z)$ points** (as opposed
  to the $D_M,D_H$-level fit already done, T23) has not been attempted; whether it
  would sharpen or complicate the clock-choice question above is unknown.
- **The Hubble tension:** could the model's reinterpretation of the CMB acoustic scale,
  once T16 is rewritten for the connectivity law, reduce or eliminate the tension? Still
  entirely open; no quantitative treatment exists for either counting law.
- The two-$H_0$ distinction, and now the three-rate distinction ($H^\text{hor}$,
  $H_\tau$, $H_\text{obs}$), remain essential bookkeeping — flag explicitly in every
  numerical comparison with observational data, exactly as cdot-4 insisted.
- **New for cdot-5:** does the connectivity law's $\tau_\infty H_0^\text{obs}=2$ relation
  (vs. cdot-4's $1.5$ and $\Lambda\text{CDM}$'s $\approx0.96$) have any independent
  observational handle — e.g. does a joint age/$H_0$ constraint (T1) favour one
  counting law over the other once real age data (globular clusters, T20's white
  dwarfs) are brought in quantitatively rather than as a lower-bound check? Not yet
  examined.
