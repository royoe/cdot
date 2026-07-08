# Update — Attacking the $\varepsilon_0$ Seed: a Scaling-Symmetry Theorem, the Radiation Floor, the Two-Component Closure, and the Invariant Statement of the Problem

*Status: update document for cross-check and merge. Attacks `Foundation.md` §6 item 2
(origin and amplitude of the seed $\varepsilon_0$); in doing so, builds the
background-level radiation-era closure (a substantial piece of item 4), derives a
hard consistency requirement on the future perturbation sector (item 5), and
uncovers one new internal tension (the closure density problem). Companion code:
`seed_analysis.py`. Produced 2026-07-07 (Fable-2 session, entry 2).*

**Summary.** The seed problem is reorganized by a theorem: the matter-era closure has
an exact scaling symmetry under which all same-sign trajectories are a single group
orbit, so $\varepsilon_0$ *by itself has no invariant meaning* — any explanation must
invoke a symmetry breaker, and the framework contains exactly three: radiation,
inhomogeneities, and the particle content. Working the radiation channel to
completion (analytically and numerically) yields: a calculable **deviation floor**
$\varepsilon_\text{floor}(z)=-2.4\times10^{-4}(1+z)$ that makes exact-EdS impossible;
a proof that the observed (negative, accelerating) homogeneous mode **cannot have
been generated after matter–radiation equality**; the framework's radiation-era
background solution ($x_\text{rad}=2x_*$, $R_h\propto c^{3/2}$), numerically
confirmed as the past attractor; and the **invariant statement of the problem**: one
dimensionless initial datum, $|\varepsilon_\text{hom}(z_\text{eq})|\approx
6.5\times10^{-13}$ — the framework's analog of $\Lambda$'s value, 110 orders of
magnitude milder, now sharply localized. The inhomogeneity channel yields a
double-edged result: a severe over-excitation *constraint* on the closure's coupling
to horizon-scale fluctuations, and, if that coupling has the right history, the most
promising *physical* seed candidate. A byproduct check exposes a new tension: the
closure predicts $\Omega_\text{closure}=0.134$, a factor 2.7 above the baryon census.

---

## 1. The Scaling-Symmetry Theorem

**Theorem.** The matter-era closure ($\dot R_h=c$; $\dot c=c^2/(\kappa\lambda xR_h)$;
$\mu(x)=R_h^2/(B^2c^{3/2})$, $B$ fixed) is exactly invariant under the one-parameter
group
$$(R_h,\,c,\,t)\;\longrightarrow\;(\sigma^{3/4}R_h,\;\sigma c,\;\sigma^{-1/4}t).$$
*Proof:* the argument of $\mu$ carries weight $2\cdot\tfrac34-\tfrac32\cdot1=0$; the
kinematic equation carries $\tfrac34-(-\tfrac14)=1$ on both sides; the dynamical
equation carries $1-(-\tfrac14)=2-\tfrac34$ on both sides. $\square$

The fixed point is group-invariant, and a perturbed trajectory maps to another with
$\varepsilon_0\to\sigma^{-m}\varepsilon_0$ ($m=3/2\nu_*$). **Corollary: all
trajectories of a given sign form a single orbit** — verified numerically to
$10^{-6}$ through the nonlinear regime ($\varepsilon_B(a)=\varepsilon_A(a/\sigma)$
exactly, `seed_analysis.py`). Consequences:

1. $\varepsilon_0$ alone is *not* a physical number — it is a coordinate on a
   symmetry orbit. The invariant content is $\varepsilon$ measured against a
   symmetry-**breaking** clock. The available breakers: radiation ($\eta\equiv
   \rho_\gamma/\rho_m\propto c^{-3/2}$, weight $-\tfrac32\neq0$), inhomogeneities,
   and the particle-content scales ($n$, masses) hidden in $B$.
2. Equivalent invariant formulations of "the seed": the value of the enclosed
   particle number when the instability reaches $O(1)$ — observed
   $N_h\sim2\times10^{80}$ — a Dirac-large-number statement; or the e-fold gap
   between the framework's equality and the deviation epoch; or the number in §4.

## 2. The Radiation Channel, Worked to Completion

Radiation enters the Machian source as $M_\gamma=\tfrac43\pi R_h^3u_\gamma/c^2$ with
$u_\gamma\propto c$ (thermal sector) — a premise-level choice, flagged: counting only
rest mass would instead leave radiation invisible to the closure. Linearizing about
the matter fixed point with $\eta(z)=\eta_0(1+z)$:
$$\frac{d\varepsilon}{d\ln c}=m\,\varepsilon+\frac{m}{2}\,\eta,\qquad m=\frac{3}{2\nu_*},$$
(derivation in the ResearchNotes trail; verified numerically to $10^{-4}$). Three
consequences:

**2.1 The deviation floor.** The co-decaying (adiabatic) particular solution is
$$\varepsilon_\text{floor}(z)=-\frac{m}{2m+3}\,\eta_0\,(1+z)
=-2.4\times10^{-4}\,(1+z)$$
(at the joint-fit $\nu_*=0.290$ and the framework's self-consistent
$\eta_0=6.3\times10^{-4}$, using $\Omega_\text{closure}=0.134$ and
photon+neutrino radiation). **The framework cannot sit exactly on the EdS fixed
point** — a qualitatively new, falsifiable statement: percent-level EdS deviations in
the dark ages ($\varepsilon\approx-2.5\%$ at $z=100$), and a $\sim$19% correction to
the total $\varepsilon$ at the top of the MUSE range ($z=1.44$: floor
$-6.0\times10^{-4}$ vs homogeneous $-3.1\times10^{-3}$) — a refinement the definitive
joint fit should include. The floor/homogeneous crossover is at $z=2.55$: above it,
the deviation from EdS is *calculable*, not fitted.

**2.2 The sign structure — the seed is not post-equality.** Although the adiabatic
track is negative (accelerating side), the growing mode excited by switching the
forcing on from rest is **positive** ($\varepsilon\to+\tfrac{m}{2m+3}\eta_ie^{m\Delta
u}$, verified numerically): post-equality radiation forcing alone drives the
*decelerating* branch. The observed negative homogeneous mode therefore **must be
inherited through the radiation era or earlier** — the seed problem and the
radiation-era closure (item 4) are rigorously linked.

**2.3 The two-component background closure** (item 4, background level, now built).
With the radiation source included, the pure-radiation era has its own scale-free
solution:
$$R_h\propto\sqrt{\mu}\,c^{3/2},\qquad x_\text{rad}=\frac{3}{2\kappa\lambda}=2x_*
\;(\approx4.89),\qquad
\left.\frac{d\varepsilon}{d\ln c}\right|_\text{rad}=\frac{3}{\nu_\text{rad}}\approx17.7,$$
and its own scaling symmetry ($R\to\sigma^{3/2}R$, $c\to\sigma c$,
$t\to\sigma^{1/2}t$), broken only by the matter component. Numerical integration of
the full two-component system backward from the joint-fit state confirms all of
this: $x\to4.87$, $R_h/c^{3/2}\to$ const by $z\sim3\times10^5$, and at
$10\lesssim z\lesssim200$ the trajectory sits *on* the analytic floor to $\sim$7%.
The framework's own equality is at $z_\text{eq}\approx1600$ (baryonic-scale matter
density; contrast standard 3400), and in the deep radiation era the trajectory lies
*below* the matter fixed point ($\varepsilon\to-1$), rising through the transition.
Caveats: background level only; simple $\mu$; neutrinos treated as massless
radiation; no recombination-era source physics.

## 3. The Invariant Statement of the Problem

Because both eras are unstable (growth 5.2 and 17.7 per e-fold of $c$ respectively),
the homogeneous amplitude is genuine cosmic initial data — the two-component
dynamics does *not* self-select it; the freedom regresses to genesis. What this
session fixes is its invariant magnitude: propagating the fitted
$\varepsilon_0=-0.0678$ back to the framework's equality,
$$\boxed{\;\big|\varepsilon_\text{hom}(z_\text{eq})\big|
=|\varepsilon_0|\,(1+z_\text{eq})^{-1/\nu_*}\approx6.5\times10^{-13}.\;}$$
This single dimensionless number *is* the framework's $\Lambda$-value problem —
structurally the same kind of question (the amplitude of a growing mode at a natural
matching epoch), but $\sim$110 orders of magnitude milder than
$\rho_\Lambda/\rho_\text{Pl}\sim10^{-123}$, and now localized to a specific epoch and
mode. Unless genesis-era physics (the $c\to0$ limit; possibly the connecton-ontology
thread, ResearchNotes §11) supplies it, it has the same epistemic status as
$\Lambda$'s value — stated plainly.

## 4. The Inhomogeneity Channel: Constraint and Opportunity

The closure responds to the *actual* enclosed mass; horizon-scale fluctuations
$\delta M/M$ kick the mode, and kicks at redshift $z$ are amplified by
$(1+z)^{1/\nu_*}$. Requiring today's $|\varepsilon|$ not be exceeded bounds the
effective coupling $g$:
$$|g\,\delta M/M|(z)\;\lesssim\;0.068\,(1+z)^{-3.44}:
\quad1.5\times10^{-3}\ (z{=}2),\quad1.8\times10^{-5}\ (z{=}10),
\quad8.5\times10^{-9}\ (z{=}100),\quad6.5\times10^{-13}\ (z_\text{eq}).$$
Since horizon-scale adiabatic fluctuations are generically
$\delta_H\sim10^{-5}$ at every epoch, an $O(1)$ coupling is **excluded by many
orders of magnitude at high $z$** — a hard, derived requirement on the future
perturbation sector (item 5): the Machian average must strongly suppress the
closure's response to inhomogeneities at early times, or the framework dies.
**The opportunity:** if the effective $g\,\delta$ history instead *peaks* at
$z\sim5$–15 at the $10^{-5}$ level (e.g. suppressed earlier, growing later — the
epoch ordering a baryon-only, MOND-boosted growth history might naturally provide),
the amplified kicks give $\varepsilon_0\sim10^{-5}\times(1+z)^{3.44}\sim
\text{few}\times10^{-2}$ — **the right order, from measured primordial amplitudes,
with no new scales.** This is the most promising physical seed candidate identified.
Distinguishing signature: stochastic seeding makes $\text{sign}(\varepsilon_0)$ a
coin flip across realizations, whereas an inherited/deterministic seed is
sign-definite — a genuine anthropic-vs-dynamical fork to resolve within item 5.

## 5. Byproduct — the Closure Density Problem (new)

The absolute normalization of the closure, never used by the joint fit (it cancels
from all shape observables), independently predicts today's mean matter density:
$\rho_0=3\mu_0c_0^2/(4\pi\kappa GR_{h,0}^2)$, giving
$$\Omega_\text{closure}=0.134/\kappa.$$
With $\kappa\approx1$ (measured from the $a_0$ amplitude), this is **2.7× the baryon
census** ($\Omega_b\approx0.049$); conversely the census demands $\kappa\approx2.7$,
conflicting with the $a_0$ measurement. A genuine three-way over-constraint
($a_0$-amplitude, SN shape, density budget) now binds $(\kappa,\lambda)$ — and
currently fails at factor $\sim$2.7. Noted without leaning on it: the factor is
eerily close to MOND's own residual cluster missing-mass factor ($\sim$2), hinting
the two may share a resolution. Recorded as a new open sub-item; it also feeds §1's
invariant ($N_h\sim2\times10^{80}$ uses the closure density).

## 6. The Attack Program, Ranked

1. **Minimal perturbation sector for the closure's inhomogeneity response** (decides
   §4's constraint-vs-opportunity; the only route to a *dynamical* origin of
   $\varepsilon_0$; prerequisite: none — can be built as a toy model on the existing
   background).
2. **Definitive-fit refinement:** include the radiation floor in the trajectory used
   for the SN and $\hat a_0(z)$ likelihoods (19% effect at $z=1.44$; also makes the
   $z\gtrsim2.5$ deviation from EdS parameter-free).
3. **Radiation-era completion** (item 4's remainder): recombination-era source
   physics, massive neutrinos, and the premise decision on what energizes the
   Machian source — the background skeleton now exists.
4. **Genesis-era speculation** (connecton thread): what, if anything, sets the
   $6.5\times10^{-13}$ datum — lowest priority until 1–3 exist.
5. **The closure density problem** (§5): re-examine the baryon census interplay and
   whether the radiation-era rebuild shifts the normalization.

## 7. Proposed Merges

- **Foundation §2.2:** add the scaling-symmetry theorem and its corollary (trajectory
  family = one orbit); add the two-component system with the radiation-era fixed
  point and the framework's own $z_\text{eq}\approx1600$; state the floor.
- **Foundation §5.5:** the floor as a falsifiable sub-prediction (dark-ages
  deviation; $z>2.5$ parameter-free regime); flag the $\hat a_0(z{=}1.44)$
  refinement.
- **Foundation §6:** item 2 rewritten around §3's invariant statement (the
  $6.5\times10^{-13}$ datum) with §4 and §6.1's program; item 4 marked "background
  level built, source-physics remainder open"; item 5 acquires the over-excitation
  requirement as a design constraint; new sub-item: the closure density problem.
- **ResearchNotes:** full derivation trail (symmetry proof, forced-response algebra
  including the sign analysis, radiation-era exponents, numerical validation
  record), and the §5 computation.

## 8. Honest Ledger

Gained: the seed problem is no longer amorphous — it is one invariant dimensionless
number at a specific epoch, with its sign provably not post-equality, a calculable
radiation floor beneath it, a candidate physical mechanism (amplified horizon-scale
inhomogeneities) that lands on the right order of magnitude from measured inputs,
and the radiation-era background built en route. Conceded: the amplitude itself
remains initial data pending the perturbation sector or genesis physics — the
framework has not explained $\varepsilon_0$, it has cornered it; the over-excitation
analysis shows the framework *survives only if* the closure's coupling to
inhomogeneities is strongly epoch-suppressed, which is a liability until item 5
demonstrates it; and the session's byproduct density check *adds* a new factor-2.7
tension rather than removing one. The framework's hardest problems are now three
sharp numbers — $6.5\times10^{-13}$, the coupling-suppression profile, and $2.7$ —
instead of three vague questions.
