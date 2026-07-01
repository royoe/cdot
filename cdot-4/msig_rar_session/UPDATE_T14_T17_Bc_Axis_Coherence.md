# UPDATE — T14/T17: $B_c$ Gets Its Axis from Bulk Motion; Two Geometric Factors Identified

*Proposed update to T14 (§"Energy Scale" and §"Toward the RAR") and T17 (§"What Sources
$B_c$" and M-σ normalization). Status: reframes the failed coefficient derivation. $B_c$ is
a vector whose amplitude comes from the connecton sea and whose axis comes from the galaxy's
bulk circulation. This identifies two distinct geometric contributions to the $a_0$
normalization — a spectral integral (undetermined) and an orbital-coherence factor
(computed). Resolves the under-justified $v_f\approx\sigma$ bridge. Session: 2026-06-30.*

---

## 1. Two Reframings (read first)

**(A) The connecton spectrum, not a single wavelength.** Connectons are re-emitted at every
interaction point (T14), so the horizon is only the **IR cutoff** — the longest wavelength —
of a broad spectrum, not a monochromatic line. The previous session's $R_0$-vs-$c/H_0$
dichotomy for $\lambda_\text{floor}$ was therefore a **false choice**: neither is "the"
wavelength. The fluctuation floor a mass-induced perturbation competes against is a
**spectral integral** over the connecton spectrum, weighted by its shape. The factor-6
clash between the two earlier candidates was an artifact of each picking one end of a
distribution. The spectrum is currently undetermined, so this contributes an
**undetermined O(1) factor** — but it is now correctly located (spectral shape), not a
contradiction.

**(B) $B_c$ is a vector; its axis comes from bulk motion.** An isotropic horizon-sourced sea
has amplitude but **no direction**. The previous sessions tacitly assumed $B_c$ points
tangentially (so $v\times B_c$ acts along the orbit) without saying where the axis came
from. It comes from the galaxy's own bulk circulation: the sea supplies the amplitude, the
coherent mass current supplies the axis. This makes the **disk and bulge physically
different**, and supplies a *computed* geometric factor.

---

## 2. The Orbital-Coherence Factor (computed)

Model the connecton gravitomagnetic sourcing like a mass current: the coherent $B_c$ is set
by the **vector-averaged** current $\langle\mathbf v\rangle$, while the orbits carry total
speed $\langle|\mathbf v|\rangle$. Define the coherent fraction $f = J_\text{coh}/J_\text{tot}$.

For a drifting isotropic (Maxwellian) velocity distribution with bulk drift $v_\text{rot}$
and dispersion $\sigma$ (per axis):
- $J_\text{coh} = v_\text{rot}$,
- $J_\text{tot} = \langle|\mathbf v|\rangle \to \sqrt{8/\pi}\,\sigma$ as $v_\text{rot}\to0$,

so in the **bulge** (dispersion-dominated) limit
$$f \approx \sqrt{\tfrac{\pi}{8}}\,\frac{v_\text{rot}}{\sigma} \approx 0.627\,\frac{v_\text{rot}}{\sigma},$$
and in the **disk** (fully ordered) limit $f\to1$. Monte-Carlo confirms the smooth crossover
($f = 0.063, 0.30, 0.54, 0.80, 0.96$ at $v_\text{rot}/\sigma = 0.1, 0.5, 1, 2, 5$).

**Consequence for M-σ.** A suppressed coherent $B_c\to f B_c$ gives the bulge an effective
$a_0^\text{eff} = f^2 a_0$ (since $B_c\propto\sqrt{a_0}$). The deep-MOND balance in the bulge
then reads $\sigma^4 \sim GM\,a_0^\text{eff} = GM f^2 a_0$. With a virial closure
$v_\text{rot} = \beta\sigma$ (constant rotational support):
$$\boxed{\,M_\text{bulge} \sim \frac{8}{\pi\beta^2}\,\frac{\sigma^4}{G\,a_0}.\,}$$

**The exponent 4 is preserved** — this does not break M-σ. The geometry contributes a
**prefactor $8/(\pi\beta^2)$ to the M-σ normalization that the disk BTFR does not carry.**
This is exactly the missing content behind the previously under-justified $v_f\approx\sigma$
bridge (flagged two sessions ago): disk and bulge normalizations differ by a *computed*
geometric factor $\sqrt{8/(\pi\beta^2)}$, not an unexplained order-unity fudge.

---

## 3. A Falsifiable Prediction (bonus)

$\beta = v_\text{rot}/\sigma$ varies across bulges (~0.3–1.0), so the prefactor swings from
~28 to ~2.5. The model therefore predicts **M-σ scatter tied to rotational support**:
slow-rotating (dispersion-dominated, low $\beta$) bulges sit higher in $M/\sigma^4$ than
fast-rotating ones. This naturally explains why **M-σ has larger intrinsic scatter (~0.3
dex) than BTFR (~0.1 dex)** — the disk has no $\beta$ freedom ($f=1$ always), the bulge
does. Testable against resolved-kinematics samples (e.g. ATLAS3D-type $v/\sigma$ vs M-σ
residuals). *Not yet checked against data in this session.*

---

## 4. Honest Status of the $a_0$ Coefficient

The coefficient now has **two identified geometric contributions**, replacing the single
mystery $1/6$:
1. **Spectral integral** over the connecton spectrum (sets the amplitude floor) — *O(1),
   undetermined* pending the spectrum.
2. **Orbital-coherence factor** $f$ (sets the per-system projection) — *computed*: 1 for
   disks, $\sqrt{\pi/8}\,v_\text{rot}/\sigma$ for bulges.

This is genuine progress over the prior negative result: the disk/bulge offset is now
derived, and the floor ambiguity is correctly relocated from "contradiction in T14" to
"undetermined spectral shape." It does **not** yet deliver the absolute disk $a_0$
coefficient — that still awaits the spectral integral. So: **the disk-vs-bulge relative
normalization is derived; the absolute disk normalization remains open**, now as a
spectral-integral problem rather than a single-wavelength choice.

---

## 5. Honest Limitations

1. **Virial closure $v_\text{rot}=\beta\sigma$ assumed, not derived.** The clean $\sigma^4$
   requires $\beta$ roughly constant across bulges. Real $\beta$ has a spread (which is the
   source of the predicted scatter, §3) — so "constant $\beta$" is an idealization, and the
   M-σ exponent is only as clean as that idealization.
2. **Gravitomagnetic-analogy sourcing assumed.** "$B_c$ sourced by the coherent mass
   current $\langle\rho\mathbf v\rangle$" is the natural gravitomagnetic form but is taken
   by analogy, not derived from the connecton transport equation.
3. **Spectral integral not done.** §1(A) correctly reframes the floor but does not compute
   it; the absolute $a_0$ coefficient is still open.
4. **$\sqrt{8/\pi}$ assumes a Maxwellian ellipsoid.** Real bulge distribution functions are
   anisotropic; the 0.627 coefficient will shift with anisotropy.

---

## 6. Suggested Document Edits (on merge)

- **T14 §"Energy Scale: The Minimal Quantum"** — replace "wavelength = horizon" / "$\nu=H_0$"
  (the inconsistent pair flagged last session) with: the horizon is the **IR cutoff** of a
  broad re-emission spectrum; the fluctuation floor is a spectral integral; the single-
  wavelength values were endpoints, not the answer. Mark the spectrum as an open object.
- **T14 §"Toward the RAR"** — add that $B_c$'s **axis** comes from bulk circulation (the sea
  sets amplitude only); the absolute $a_0$ awaits the spectral integral; keep "coefficient
  open" but reframed (spectral, not single-wavelength).
- **T17 §"What Sources $B_c$"** — extend: $B_c$ amplitude from the sea, **axis from the
  galaxy's coherent mass current**. Add the coherence factor $f$ and the disk ($f=1$) vs
  bulge ($f\approx\sqrt{\pi/8}\,v_\text{rot}/\sigma$) distinction.
- **T17 M-σ section** — replace the $v_f\approx\sigma$ bridge with the derived relation
  $M_\text{bulge}\sim(8/\pi\beta^2)\sigma^4/(Ga_0)$; note exponent 4 preserved, geometric
  prefactor on the normalization, and the predicted scatter-vs-rotational-support (§3) as a
  new falsifiable handle. This supersedes the Issue-4 / $v_f\approx\sigma$ note from the
  earlier consistency check.
- **Core Principles §7** — RAR/M-σ line: "RAR shape derived; absolute $a_0$ coefficient open
  (now a connecton-spectral-integral problem); **disk-vs-bulge normalization offset derived**
  from orbital coherence; M-σ scatter predicted to track rotational support."
- **Cross-ref the prior negative update** (`UPDATE_T14_Background_Density_Negative.md`): this
  update *builds on* it — same conclusion (single-wavelength coefficient not derivable),
  now with the constructive reframing (spectrum + coherence) the user supplied.

---

## 7. The Next Computations (two, independent)

1. **Spectral integral.** Posit a connecton re-emission spectrum (e.g. set by the
   interaction-point density and the horizon IR cutoff) and compute the fluctuation-floor
   integral that fixes the absolute disk $a_0$. This is the remaining piece of the
   normalization.
2. **Test the scatter prediction.** Compare M-σ residuals against $v/\sigma$ (rotational
   support) in a resolved-kinematics sample. The model predicts a definite sign: lower
   $\beta$ → higher $M/\sigma^4$. A clean way to falsify (or support) the coherence picture
   independent of the absolute coefficient.
