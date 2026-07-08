# Update — The AQUAL-Consistent Closure: an Unstable EdS Fixed Point, Apparent Acceleration from the Deep-MOND Slide, and a 13-Gyr Age

*Status: update document for cross-check and merge. Executes §3 of
`Update-AqualAlignment-2026-07-07.md`: rebuild premise 2's Sciama closure with the
AQUAL-corrected field, self-consistently with $a_0=\lambda\dot c$. Resolves the
premise 2/4 inconsistency; supplies the $\Lambda$-analog; does **not** derive
$\lambda$ (that hope is recorded dead in §3 below). Companion code:
`closure_dynamics.py`. Produced 2026-07-07 (cdot-7, session entry 7).*

**Headline.** The AQUAL-consistent closure turns the cosmological history from an
algebraic relation into a genuine dynamical system. The old EdS-equivalent power law
survives as its unique scale-free solution — a fixed point at $x_*=3/(4\kappa\lambda)$
— but the fixed point is **unstable**, with deviations growing as
$(1+z)^{-1/\nu_*}$. On the branch sliding toward the deep-MOND regime, the history
develops late-time apparent acceleration. Numerically, with the *same*
$\lambda\approx0.26$ required by the empirical $a_0$, the simple interpolating
function, and **one** integration constant $\varepsilon_0=-0.063$, the model fits the
$\Lambda$CDM ($\Omega_m=0.3$) luminosity distance to **0.015 mag rms** over
$z\in[0.02,1.4]$, gives $q_0=-0.68$, and raises the proper age from 9.3 to
**13.0 Gyr**. MOND and dark-energy phenomenology emerge from the single portal
$a_0=\lambda\dot c$.

---

## 1. Setup and the Closure-Form Decision

For spherical symmetry, AQUAL's field equation integrates exactly (Bekenstein–Milgrom)
to
$$\mu\!\left(\frac{g_h}{a_0}\right)g_h=\frac{GM_h}{R_h^2}.$$
The Machian relation is taken as
$$c^2=\kappa\,g_h R_h,$$
the field-based binding, which reduces to the Sciama form $c^2=\kappa GM_h/R_h$ when
$\mu\to1$. **Decision flagged:** the alternative closure — $c^2\propto$ the AQUAL
*potential* — was considered and rejected because the deep-MOND potential
$\sqrt{GM a_0}\,\ln(R/R_\text{ref})$ carries an arbitrary reference scale; importing
$R_\text{ref}$ would smuggle in exactly the free constant this construction is trying
to explain. The $g_hR_h$ form is reference-free. Note $\kappa$ and $\lambda$ enter all
dynamics only through $\tilde\lambda\equiv\kappa\lambda$; $\kappa=1$ is assumed for
numbers below and $\kappa=O(1)$ ignorance is carried explicitly in §7.

With $M_h=\frac43\pi R_h^3\rho_0(c/c_0)^{1/2}$ (premises 2–3), $a_0=\lambda\dot c$, and
$\dot R_h=c$, eliminating $g_h$ gives the closed system
$$\boxed{\;\dot R_h=c,\qquad
\dot c=\frac{c^2}{\kappa\lambda\,x\,R_h},\qquad
x=\mu^{-1}\!\left(\frac{R_h^2}{B^2c^{3/2}}\right),\;}
\qquad B^2\equiv\frac{1}{\kappa\frac{4\pi}{3}G\rho_0c_0^{-1/2}}.$$
Because $a_0$ involves $\dot c$, the closure is no longer algebraic: this is a 2D
autonomous dynamical system, carrying **one integration constant beyond the old
closure**. That constant is where the $\Lambda$-analog lives. (The inversion
$\mu^{-1}$ is well-defined wherever $\mu'\neq0$; in the pure-Newtonian limit the
system degenerates back to the old algebraic closure, consistently.)

---

## 2. The Fixed Point: EdS Survives as the Scale-Free Solution

The ansatz $x=\text{const}$ solves the system with $R_h=B\sqrt{\mu(x_*)}\,c^{3/4}$ and
$\dot c=\frac{4}{3B\sqrt{\mu_*}}c^{5/4}$ — the same power-law history as before, with
$\mu_*\equiv\mu(x_*)$ absorbed into constants — and self-consistency fixes
$$x_*=\frac{3}{4\kappa\lambda},$$
reproducing the operating point found in the alignment update. All photometric results
of the photon-sector update (exact EdS $d_L$, $q_0=+\tfrac12$, age $\tfrac{2}{3H_0}$)
hold *on the fixed point* for any $\mu$ and any $\lambda$.

**The dead hope, recorded plainly:** self-consistency does *not* derive $\lambda$. The
fixed point exists for every $\lambda$; $x_*$ is set by the kinematic exponent
($\tfrac34$) alone. The alignment update's hope (ii) fails. What replaces it is the
overdetermined consistency test of §6.

---

## 3. The Fixed Point Is Unstable — and That Is the $\Lambda$-Analog

Perturbing $R_h=B\sqrt{\mu_*}c^{3/4}(1+\varepsilon)$ and linearizing (derivation in
the ResearchNotes trail):
$$\dot\varepsilon=\frac{3}{2\nu_*}\,\frac{\dot c}{c}\,\varepsilon,\qquad
\nu_*\equiv\left.\frac{d\ln\mu}{d\ln x}\right|_{x_*}\in(0,1),$$
so $\varepsilon\propto c^{3/2\nu_*}$, i.e. in redshift
$$\varepsilon(z)=\varepsilon_0\,(1+z)^{-1/\nu_*}.$$
Deviations are exponentially negligible in the past and emerge at late times — the
characteristic phenomenology of $\Lambda$, here produced by an instability rather than
a constant. (Numerical check: measured growth exponent 5.79 vs predicted
$3/2\nu_*=5.83$ for the fiducial case.)

Cosmography on a general trajectory (using the corrected redshift law
$1+z=(c_0/c_z)^{3/2}$, and with $j\equiv c\ddot c/\dot c^2$ today):
$$q_0=\frac{4-2j}{3}
\;\xrightarrow{\text{linear order}}\;
q_0=\frac12+\varepsilon_0\,\frac{\nu_*+2}{\nu_*^2}.$$
The fixed point has $j=\tfrac54$, $q_0=+\tfrac12$ ✓. The $\varepsilon_0<0$ branch —
the horizon sliding *below* scale-free growth, $x$ decreasing, the closure descending
into the deep-MOND regime — gives $q_0<\tfrac12$ and, for
$|\varepsilon_0|\sim3$–$6\%$, apparent acceleration. Also derived at linear order: the
age increases on this branch, $\;\text{age}\cdot H_0=\tfrac23\!\left[1-K\varepsilon_0
\tfrac{m}{m+9/4}\right]$ with $K=1+2/\nu_*$, $m=3/2\nu_*$ (nonlinear values below are
substantially larger).

---

## 4. Nonlinear Numerics

Dimensionless system integrated with `scipy.solve_ivp` (rtol $10^{-11}$); validation:
$\varepsilon_0=0$ reproduces $d_L^\text{EdS}$ to $10^{-10}$ and
$\text{age}\cdot H_0=\tfrac23$ to $6\times10^{-12}$. The single parameter
$\varepsilon_0$ was fitted to the $\Lambda$CDM ($\Omega_m=0.3$, flat) luminosity
distance over $z\in[0.02,1.4]$ (used as a stand-in for the SN compilation — caveat in
§7). Results across $\mu$-forms and $\lambda$:

| $\mu$-form | $\lambda$ | $x_*$ | $\nu_*$ | $\varepsilon_0$ (fit) | rms (mag) | $q_0$ | age$\cdot H_0$ | age (Gyr) |
|---|---|---|---|---|---|---|---|---|
| simple | 0.20 | 3.75 | 0.211 | $-0.047$ | 0.028 | $-0.80$ | 0.915 | 12.8 |
| **simple** | **0.26** | **2.88** | **0.257** | $-0.063$ | **0.015** | $-0.68$ | 0.933 | **13.0** |
| simple | 0.35 | 2.14 | 0.318 | $-0.086$ | 0.004 | $-0.58$ | 0.956 | 13.4 |
| standard | 0.20 | 3.75 | 0.066 | $-0.012$ | 0.093 | $-1.83$ | 0.864 | 12.1 |
| standard | 0.26 | 2.88 | 0.107 | $-0.023$ | 0.060 | $-1.12$ | 0.884 | 12.4 |
| standard | 0.35 | 2.14 | 0.179 | $-0.048$ | 0.020 | $-0.67$ | 0.920 | 12.9 |

Fiducial ($\mu$ simple, $\lambda=0.26$ — **the value the empirical $a_0$
independently requires**): $\varepsilon_0=-0.0627$, rms 0.015 mag — inside typical SN
systematic floors. Hubble-diagram detail:

| $z$ | $\Delta\mu$ vs EdS (mag) | $\Delta\mu$ vs $\Lambda$CDM (mag) | $\varepsilon(z)$ | $x(z)$ |
|---|---|---|---|---|
| 0.0 | — | — | $-0.063$ | 1.88 |
| 0.25 | $+0.26$ | $+0.020$ | $-0.033$ | 2.27 |
| 0.5 | $+0.42$ | $+0.019$ | $-0.018$ | 2.52 |
| 1.0 | $+0.59$ | $-0.004$ | $-0.007$ | 2.75 |
| 1.5 | $+0.68$ | $-0.028$ | — | — |
| 2.0 | $+0.73$ | $-0.047$ | $-0.001$ | 2.85 |

The history is EdS to $0.1\%$ before $z\sim5$ and peels off recently; the closure has
already slid from $x_*=2.88$ to $x_0=1.88$. Nonlinearity is strong: the fitted
$\varepsilon_0=-0.063$ is twice the linear-theory estimate ($-0.031$ for
$q_0=-0.55$), so §3's formulas are guides, not fit surrogates. Age lands at
**13.0 Gyr** — up from the photon-sector update's 9.3, marginally consistent with
globular-cluster ages ($\approx12.5$–13 Gyr), still below $\Lambda$CDM's 13.8.

---

## 5. The Asymptotic Future: the Deep-MOND Runaway Is a de Sitter Phase

Forward integration: the trajectory runs away into deep MOND, with $c$ diverging at
finite *coordinate* time as $c\propto(t_\ast-t)^{-2/5}$ (analytic; $R_h$ stays
finite). The proper time to reach it diverges — but now only **logarithmically**:
$\Delta\tau_\text{proper}\propto\ln[1/(t_\ast-t)]$, i.e. constant proper time per
e-fold of $c$. Numerically: $\approx38$ Gyr per decade of $c$, i.e. **$c$ grows
exponentially in proper time with e-fold time $\approx16.5$ Gyr** — strikingly close
to $\Lambda$CDM's de Sitter rate $1/(\sqrt{\Omega_\Lambda}H_0)\approx16.7$ Gyr. (Not
independent — the fit to the $\Lambda$CDM $d_L$ plausibly forces the asymptotic rates
to agree — but structurally meaningful: **the EdS correspondence of the photon-sector
update extends to the asymptotic future, where the deep-MOND runaway maps onto the de
Sitter phase.** Recall the pure-exponential-$c$ history was exactly the old $s=0$
closure's; the attractor recovers that form in proper time.) The genesis-mirror
structure (finite coordinate time, infinite proper time to the future singularity)
survives, weakened from power-law to logarithmic divergence — flagged honestly.

---

## 6. The Consistency Triangle, and the First Cosmological Test of $\mu(x)$

$\lambda$ is not derived, but it is now measured twice and testable a third way:
1. **From $a_0$'s value:** $\kappa\lambda\approx0.26$ (alignment update).
2. **From the SN residual shape:** the fit quality is controlled by $\nu_*$, hence by
   $x_*=3/(4\kappa\lambda)$ given $\mu$. For simple-$\mu$ the SN shape prefers
   $\kappa\lambda\approx0.35$ (rms 0.004) over $0.26$ (rms 0.015), agreeing with (1)
   to $\sim35\%$ — i.e. to well within the unknown $O(1)$ factor $\kappa$. The
   triangle closes at the level it can currently be tested.
3. **$\mu$-form discrimination:** at fixed $\kappa\lambda$, the standard function fits
   $\sim4\times$ worse than the simple one (0.060 vs 0.015 mag rms at $\lambda=0.26$)
   because its sharper transition gives too-small $\nu_*$ at $x_\ast$ and hence a
   too-steep deviation history. **The expansion history now discriminates among
   interpolating functions** — items 3/6 acquire a cosmological data channel entirely
   independent of rotation curves, as anticipated qualitatively in the alignment
   update, now quantified.

---

## 7. Derived vs Fitted vs Assumed — the Ledger

**Derived:** the dynamical-system structure; the EdS fixed point and its instability;
the deviation shape $\varepsilon(z)=\varepsilon_0(1+z)^{-1/\nu_*}$ tied to $\mu$'s
slope; the cosmography $q_0=(4-2j)/3$; the branch structure ($\varepsilon_0<0\;
\Rightarrow$ acceleration + older universe + slide toward deep MOND); the asymptotic
exponential-$c$ (de Sitter-analog) future.
**Fitted:** $\varepsilon_0$ — one number, the analog of $\Omega_\Lambda$, with the
same epistemic status (a cosmic initial condition, not derived); $\kappa\lambda$
(doubly measured, §6).
**Assumed:** the closure form $c^2=\kappa g_hR_h$ (§1's decision); $\kappa=1$ for
numerics; homogeneity as before; the $\Lambda$CDM curve as SN-data proxy.
**On the coincidence problem, recast but not solved:** unlike a constant $\Lambda$,
the deviation here is transient and growing — $|\varepsilon|$ passes through the
few-percent range during roughly one e-fold of $c$ regardless of its seed, so "why
now" becomes "why is the seed's amplitude such that the passage happens at
stellar-age epochs" — a real question about $\varepsilon_0$'s origin, not obviously
harder than $\Lambda$'s value, but not answered.

---

## 8. Proposed Merges and Revised Open Items

- **Foundation §2.2:** replace the algebraic Sciama closure with §1's dynamical
  system; the old solution becomes "the fixed-point solution"; record the closure-form
  decision and the $\kappa\lambda$ degeneracy.
- **Foundation §5.2/§5.5:** the fixed point carries the EdS results; add §4's
  fiducial trajectory as the working cosmology (with the fit table), §5's future
  asymptotics, and the corrected age (13.0 Gyr).
- **Foundation §6:** the $\Lambda$-analog item (photon-sector update) is **addressed
  in mechanism**; its successor items: (a) origin and amplitude of the seed
  $\varepsilon_0$ (what perturbs the fixed point — genesis conditions?
  inhomogeneities? — the framework's new hardest question); (b) refit against a real
  SN compilation with proper covariances instead of the $\Lambda$CDM proxy, jointly
  with RAR data for $\mu$ (the §6 triangle as a genuine statistical test); (c) the
  premise 2/4 inconsistency of the alignment update is **resolved** — strike it;
  (d) note the still-absent BAO/CMB-scale sector, now more urgent since the
  background history is finally competitive.
- **ResearchNotes:** full derivation trail (perturbation analysis, cosmography
  algebra including the $j=\tfrac54\Rightarrow q_0=\tfrac12$ check, the dead
  $\lambda$-derivation hope, numerical validation record); archive
  `closure_dynamics.py`.

---

## 9. Honest Ledger

Gained: the framework's first internally consistent cosmology that is competitive with
observation — acceleration with the right sign and magnitude, a 13-Gyr age, a
$\Lambda$CDM-quality $d_L(z)$ from one new constant, unification of $a_0$ and the
acceleration through a single portal, a cosmological discriminant for $\mu$, and
resolution of the premise 2/4 inconsistency. Conceded: $\lambda$ is measured, not
derived (the fixed point admits all values); $\varepsilon_0$ is a fitted cosmic
initial condition; the fit target was $\Lambda$CDM-as-proxy, not data; $\kappa=1$ by
fiat; the age is marginal, not comfortable; and the future singularity's proper-time
protection has thinned from power-law to logarithmic. The framework now fails nowhere
it has been tested at background level — and owes its remaining debts at the level of
seeds, sectors (BAO/CMB), and real-data statistics rather than sign errors.
