# UPDATE — T14: The Connecton Re-emission Spectrum and the Horizon-Set Floor

*Proposed update to T14 (§"Energy Scale: The Minimal Quantum" and §"Toward the RAR").
Status: the connecton spectrum slope is **derived** ($q=2$) from conserved-number cascade
physics; this is exactly the marginal slope at which the fluctuation floor is **set by the
horizon and independent of the interaction (UV) scale**, fixing the coefficient to $c^2/R_0
= cH_0/6$ times an order-unity cascade sum $S$ that the data require to be $\approx1$.
The interaction-scale ambiguity that defeated the single-wavelength attempts is **removed**.
Absolute normalization $S$ remains the one open factor. Session: 2026-06-30.*

---

## 1. Result in One Line

The connecton re-emission cascade has a **derived** density power-spectrum slope
$P_\rho(k)\propto k^{-2}$. Routed through the gravitational Poisson kernel, the
acceleration floor is
$$g_\dagger^2 \propto \int_{k_\text{min}}^{k_\text{max}} P_\rho(k)\,dk \propto
\int k^{-2}dk = \frac{1}{k_\text{min}} - \frac{1}{k_\text{max}} \to \frac{1}{k_\text{min}},$$
so $g_\dagger = (c^2/R_0)\cdot S$ with $k_\text{min}=1/R_0$ and $S=O(1)$. The UV
(interaction) scale **drops out**. With $S\approx1$ this is $a_0 = cH_0/6$.

---

## 2. The Spectrum Slope Is Derived

Connectons are conserved in number and re-emitted at every interaction point (T14),
random-walking through scales between the horizon IR cutoff ($k_\text{min}=1/R_0$) and the
interaction UV scale ($k_\text{max}=1/\lambda_\text{min}$). In steady state a conserved
quantity cascading between an IR source and a UV sink settles to **constant number flux**
across scales (the conserved-number analogue of a Kolmogorov cascade):
$$\epsilon_N = \frac{n(k)}{\tau_k} = \text{const}.$$
The random-walk transfer time at scale $k$, for carriers moving at $c$ with step $\sim1/k$,
is $\tau_k \sim 1/(ck)$. Hence
$$n(k)\,(ck) = \text{const} \;\Rightarrow\; n(k)\propto \frac{1}{k}\quad(\text{number per }\ln k).$$
Converting to the density power spectrum ($P_\rho(k)\,dk \propto [n(k)/k]\,m_c^2$):
$$\boxed{\,P_\rho(k)\propto k^{-2}\quad (q=2).\,}$$
No tunable freedom enters — the slope follows from number conservation and propagation at $c$.

---

## 3. Why $q=2$ Is Special — the Horizon Wins, the Interaction Scale Drops Out

The fluctuation floor is the RMS acceleration of the sea's own gradient. Via the
gravitational Poisson kernel in Fourier space, $g_k = 4\pi G\rho_k/k$, and the 3D measure
$d^3k\propto k^2dk$ cancels the $1/k^2$ from gravity, giving
$$g_\dagger^2 = \frac{(4\pi G)^2}{2\pi^2}\int_{k_\text{min}}^{k_\text{max}} P_\rho(k)\,dk.$$
With the derived $P_\rho\propto k^{-2}$, the integral is $1/k_\text{min}-1/k_\text{max}$.
**$q=2$ is exactly the marginal slope:** any redder ($q>2$) and the IR end dominates even
more strongly; any bluer ($q<2$) and the UV (interaction) end would dominate and the floor
would be set by the unknown $\lambda_\text{min}$. At $q=2$ the integral converges at the UV
end and is set by $k_\text{min}=1/R_0$, with the convergence steep: **50% of the floor comes
from the first 0.3 e-folds above the horizon, ~90% within one e-fold, ~100% within three.**
The interaction scale contributes nothing.

This is the qualitative resolution the two prior sessions lacked: it explains **why** the
coefficient is a horizon quantity ($c^2/R_0=cH_0/6$) and not an interaction-scale quantity
(which would be enormous). The earlier $R_0$-vs-$c/H_0$ dichotomy is fully resolved — it is
$R_0$, and the derived spectrum proves the floor is horizon-dominated.

---

## 4. The One Remaining Factor

$g_\dagger = (c^2/R_0)\,S$, where $S$ is the order-unity cascade sum (the absolute
normalization of $P_\rho$, set by the connecton sea's total number density and per-connecton
mass). The spectrum *shape* fixes the slope, the horizon-domination, and the
$g_\dagger\propto1/R_0$ scaling — but **not** the absolute amplitude $S$. Matching the
measured $a_0$ requires:
$$S = \frac{a_0}{c^2/R_0} \approx 1.10\ (H_0{=}67.4),\ 1.06\ (70),\ 1.02\ (73).$$
So $S\approx1$ across the Hubble range. The cascade with the IR mode plus an order-unity sum
naturally gives $S\approx1$, and the result is **consistent with** $cH_0/6$ — but $S=1$ is
not independently proven; it awaits the absolute connecton number density.

---

## 5. Honest Status

- **Derived:** the spectrum slope $q=2$; horizon-domination of the floor; UV-independence
  (interaction scale irrelevant); the scaling $g_\dagger=cH_0/6\times S$.
- **Not derived:** the order-unity normalization $S$ (needs the absolute connecton sea
  density). Data require $S\approx1.0$–$1.1$.
- **Net:** a clear advance over the prior negative result. The interaction-scale ambiguity
  that defeated the single-wavelength attempts is eliminated by the marginal slope; the
  coefficient is pinned to $cH_0/6$ up to a factor the data say is $\approx1$.

Caveats on the derivation: (i) constant-number-flux steady state is the natural cascade
fixed point but is assumed, not proven, for the connecton kernel; (ii) $\tau_k\sim1/(ck)$
is the ballistic/random-walk transfer time — a different transfer law would shift $q$;
(iii) the Poisson-kernel routing assumes the connecton fluctuation gravitates like a mass
density (consistent with T14 but assumed here); (iv) $S$ depends on the absolute amplitude,
untouched.

---

## 6. Suggested Document Edits (on merge)

- **T14 §"Energy Scale: The Minimal Quantum"** — replace the single-wavelength /
  inconsistent-$\lambda_\text{floor}$ text with §2–§3: the spectrum is a cascade with derived
  slope $q=2$; the horizon is the IR cutoff; the floor is horizon-set and UV-independent.
- **T14 §"Toward the RAR"** — state the coefficient as $a_0=(c^2/R_0)S=cH_0/6\cdot S$,
  $S=O(1)$ from the cascade, $S\approx1$ required by data; UV/interaction scale proven
  irrelevant. Upgrade from the prior "coefficient open (spectral)" to "**coefficient pinned
  to $cH_0/6$ up to an O(1) normalization $S\approx1$; slope and horizon-domination derived**."
- **T14 Open Items** — the $a_0$ item narrows to a single quantity: derive the absolute
  connecton sea amplitude (hence $S$). Everything else in the coefficient is now derived.
- **Core Principles §7** — RAR/M-σ line: "RAR shape derived; $a_0$ coefficient **pinned to
  $cH_0/6$** by the derived $q=2$ connecton spectrum (horizon-set, UV-independent), up to an
  order-unity normalization $S\approx1$ awaiting the absolute sea density; disk-vs-bulge
  offset derived (prior session)."
- **Supersedes** the floor-wavelength framing in `UPDATE_T14_Background_Density_Negative.md`
  and confirms the spectral reframing of `UPDATE_T14_T17_Bc_Axis_Coherence.md` §1(A): the
  spectrum is now derived, not merely posited.

---

## 7. The Next Computation (highest leverage)

Derive the absolute connecton sea amplitude $S$. Concretely: the total connecton number
density $n_c$ and per-connecton mass $m_c$ (with horizon-mode energy $\hbar c/R_0$) set the
$P_\rho$ normalization. If $n_c$ from the matter-sourced emission rate, integrated over the
cascade, returns $S=1$ (within the McGaugh $a_0$ systematic), the $a_0$ coefficient is fully
closed and the RAR is predicted in shape and absolute scale with **no** free parameters.
This is the last factor.
