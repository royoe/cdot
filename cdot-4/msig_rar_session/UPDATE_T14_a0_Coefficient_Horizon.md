# UPDATE — T14/T6: The $a_0$ Coefficient is $cH_0/6$ from Horizon Geometry

*Proposed update to T14 (§"Toward the RAR: The Natural Acceleration Scale") and T6, with a
correction flag for Core §7. Status: the order-one coefficient is derived from horizon
geometry as **exactly 6** (not $2\pi$), giving $a_0 = cH_0^{\text{obs}}/6$, consistent with
the measured value across the Hubble-tension range. Corrects two errors in the current T14
text. Session: 2026-06-30.*

---

## 1. Result in One Line

$$\boxed{\,a_0 = g_\dagger = \frac{c^2}{R_0} = \frac{cH_0^{\text{obs}}}{6}\,}$$
from the background-gradient picture (force = spatial gradient of the connecton sea over
one horizon radius) plus the model's own horizon radius $R_0 = 3P\,c/H_0^{\text{obs}} =
6c/H_0^{\text{obs}}$ ($P=2$). At $H_0=70$ this is $1.13\times10^{-10}$ m/s², within
$-0.3\sigma_\text{sys}$ of the measured $a_0 = 1.20\times10^{-10}$ m/s²; it stays inside the
McGaugh systematic band across the entire Planck–SH0ES range.

---

## 2. The Derivation

**Step 1 — the force is a spatial gradient, not a temporal rate.** Orbits feel the gradient
of the background connecton field. T14's own form:
$$g_\dagger = c^2\,\frac{|\nabla\rho_\text{bg}|}{\rho_\text{bg}}.$$
The natural gradient scale is the horizon: $|\nabla\rho_\text{bg}|/\rho_\text{bg} = 1/R_0$.
Hence $g_\dagger = c^2/R_0$.

**Step 2 — insert the model's horizon radius.** Core §4a/§5 and T3 fix
$$R_0 = \frac{3P\,c_0}{H_0^{\text{obs}}} = \frac{6c_0}{H_0^{\text{obs}}}\quad(P=2),$$
where the **3** is the horizon ODE ($H^{\text{hor}}=3c/R$) and $P=2$ is the
horizon-to-observable Hubble conversion ($H_0^{\text{obs}}=P\,H_0^{\text{hor}}$). Therefore
$$g_\dagger = \frac{c^2}{R_0} = \frac{cH_0^{\text{obs}}}{6}.$$

**Step 3 — the closure passes it through unchanged.** The RAR closure's deep limit is
$g_\text{obs}=\sqrt{g_\text{bar}\,g_\dagger}$, and MOND's $a_0$ is *defined* by
$g_\text{obs}=\sqrt{g_\text{bar}\,a_0}$. The deep coefficient was verified = 1 (prior
session), so $a_0 = g_\dagger$ with no extra factor. The prediction is therefore
$a_0 = cH_0^{\text{obs}}/6$ directly.

**Numerical check** ($a_0^\text{obs} = (1.20\pm0.02_\text{stat}\pm0.24_\text{sys})\times
10^{-10}$, McGaugh et al. 2016):

| $H_0^{\text{obs}}$ | $cH_0/6$ (m/s²) | offset |
|---:|---:|---:|
| 67.4 (Planck) | $1.09\times10^{-10}$ | $-0.46\sigma_\text{sys}$ |
| 70.0 | $1.13\times10^{-10}$ | $-0.28\sigma_\text{sys}$ |
| 73.0 (SH0ES) | $1.18\times10^{-10}$ | $-0.08\sigma_\text{sys}$ |

Exact match at $H_0 = 74.1$ km/s/Mpc — just above SH0ES, well within reach given the
combined $a_0$ and $H_0$ uncertainties.

---

## 3. Two Corrections to the Current T14 Text

The present T14 (lines 137–139, 153) states $g_\dagger = \dot c = cH_0$ and
$a_0 \approx cH_0/2\pi$. Both are slightly off; the corrected derivation fixes both **in the
direction of better agreement**.

**Correction A — the coefficient is 6, not $2\pi$.** Horizon geometry gives exactly 6.
$2\pi\approx6.28$ is a numerical near-miss for the horizon's 6. Factor 6 needs $H_0=74.1$
for an exact $a_0$; $2\pi$ needs $H_0=77.6$ — so 6 is both the *derived* value and the
*better-fitting* one.

**Correction B — $\dot c$ uses the horizon rate, and is the wrong object anyway.** T14
wrote $g_\dagger=\dot c=cH_0$, but $\dot c/c = H^{\text{hor}}$ (the horizon rate), so the
bare $\dot c = cH_0^{\text{obs}}/P = cH_0^{\text{obs}}/2$ — already a factor $P$ below the
naive $cH_0^{\text{obs}}$. More fundamentally, the force is the **spatial gradient**
$c^2/R_0$, not the **temporal rate** $\dot c$. They share dimensions but differ by the
horizon ODE factor 3: $\dot c = cH^{\text{hor}} = 3c^2/R_0 = 3g_\dagger$. The clean identity
is $g_\dagger = \dot c/3 = c^2/R_0$, not $g_\dagger=\dot c$.

---

## 4. Honest Limitations

1. **One O(1) input is assumed, not derived: the gradient coefficient.** The step
   $|\nabla\rho_\text{bg}|/\rho_\text{bg} = 1/R_0$ assumes the background density varies on
   exactly one horizon radius with coefficient exactly 1 (not $1/2R_0$ or $2/R_0$). This is
   the natural choice, and the agreement with $a_0$ *favors* unity — but that is a mild use
   of the data, so the result is "coefficient $= cH_0/6$ with the **6 fully derived** from
   horizon geometry, contingent on an O(1) gradient coefficient the data favor being 1,"
   not a closed proof. To remove the contingency: derive the background density profile
   $\rho_\text{bg}(r)$ from horizon growth and compute its logarithmic gradient directly.
2. **This is the connecton (gradient) route, not the kinetic-closure route.** It does **not**
   derive the coefficient from $4\pi GL\rho_\text{bg}/(3\sigma)=c$ (T14's flagged target).
   Instead it supersedes that target with a cleaner geometric one. The two should be checked
   for mutual consistency.
3. **Depends on $P=2$.** The volume law $P=s+2=2$ is used throughout Core (it sets
   $q_0=+1/6$, $\tau_\infty=21$ Gyr, the distance ladder). The coefficient 6 = 3P inherits
   this. If $P$ were revised, the coefficient would track as $3P$.

---

## 5. Suggested Document Edits (on merge)

- **T14 §"Toward the RAR: The Natural Acceleration Scale"** — replace the
  "$a_0\approx cH_0/2\pi$" identity (lines 137–139) and the "$g_\dagger=\dot c=cH_0$"
  framing (line 136, 153) with §2 above: $g_\dagger = c^2/R_0 = cH_0^{\text{obs}}/6$,
  derived; note $g_\dagger=\dot c/3$ (gradient vs rate). Mark Corrections A and B explicitly
  so the cross-check catches the prior $2\pi$ wording.
- **T14 Open Items** — the coefficient item is now **substantially discharged** (down to one
  O(1) gradient assumption). Rewrite as: "derive $\rho_\text{bg}(r)$ from horizon growth and
  confirm $|\nabla\ln\rho_\text{bg}| = 1/R_0$ exactly; reconcile the gradient route with the
  kinetic closure condition $4\pi GL\rho_\text{bg}/(3\sigma)=c$."
- **T6** — update the $a_0$-coefficient discussion: coefficient derived as $cH_0/6$ from
  horizon geometry, consistent with measurement across the Hubble-tension range; replace any
  $2\pi$ statement.
- **Core Principles §7** — RAR line: from "scale coefficient $a_0\approx cH_0/2\pi$ remains
  the open item" to "**scale coefficient derived: $a_0=cH_0^{\text{obs}}/6=c^2/R_0$ from
  horizon geometry**, consistent with measurement; remaining open item is the O(1) gradient
  coefficient (one density-profile calculation)." No core premise changes — the result uses
  the existing horizon radius $R_0=6c/H_0$ (T3/Core).
- **Cross-check flag:** the same $2\pi$ may appear in T6 or T15; search and correct to 6.

---

## 6. The Next Computation (highest leverage)

Derive the background connecton density profile $\rho_\text{bg}(r)$ from horizon growth and
compute $|\nabla\ln\rho_\text{bg}|$ directly. If it returns $1/R_0$ with coefficient 1, the
$a_0$ coefficient is fully closed (no remaining O(1) freedom) and the RAR is predicted in
both shape (prior session) and absolute scale — moving the RAR from "predicts the shape" to
"predicts the complete relation, normalization included."
