# Foundation — Universal Scaling and AQUAL-Spirit Local Dynamics

*Status: foundational, actively under construction. This is the third premise-set
attempted for this variable-$c$ program (see `ResearchNotes.md` for why the first two
were superseded). This document is self-contained — no cross-references to earlier
iterations. History and cross-references live in `ResearchNotes.md`.*

---

## 0. Purpose and Scope

This is a minimal foundation for a physical theory in which the speed of light $c$ is
not a universal constant but a cosmologically-determined quantity, sourced by the mass
enclosed within an observer's horizon, and in which *all* local physics is invariant in
Planck units — only $c(t)$ itself carries cosmological time-dependence. Local
gravitational dynamics is modified at low acceleration in the spirit of Bekenstein &
Milgrom's AQUAL, with the modification's characteristic acceleration scale tied to the
same cosmological quantity. The goal remains a framework capable of producing MOND-like
dynamics (flat rotation curves, the radial acceleration relation, the M-σ relation) and
late-time cosmic acceleration without separate dark-matter or dark-energy sectors.
**This "no dark matter" claim is currently conditional, not settled**: §5.6 finds the
cosmological closure itself demands a mass density $2$–$3\times$ the directly measured
baryon content, with only a narrow, externally time-limited escape (laboratory-bound
relic neutrino mass) currently available. This is stated here, in the opening scope
statement, rather than left for §5.6 alone to carry, because it bears directly on the
document's central claim.

**Scope reduction from earlier attempts, stated plainly.** This document does not
attempt to reproduce General Relativity's relativistic predictions (light deflection,
perihelion advance) exactly. That was a feature of an earlier, now-superseded local
closure; the mechanism adopted here is explicitly Newtonian-level, matching the AQUAL
program it draws from. A relativistic completion, if one is needed, is future work
(§6 item 7).

**Scope limit, newly identified and stated plainly.** The Machian closure (§2) sources
$c(t)$ from rest mass only. Radiation energy density, relative to rest-mass energy
density, grows into the past ($\hat u_\gamma/\hat\rho_mc^2\propto(1+z)$, exactly as in
standard cosmology) and must eventually dominate, at the analog of $z_\text{eq}$. Until
the closure is extended to include radiation energy, every result in this document is a
**late-universe result** ($z\ll z_\text{eq}$); BBN- and CMB-era physics cannot yet be
posed (§6 item 5).

**A deliberate scope boundary, stated as a standing test for what belongs in this
document.** Premise 2's homogeneity assumption and premise 4's local application of
$a_0$ to arbitrarily clumped, structured systems are not in tension — they do different
jobs. Homogeneity is used *only* to compute the single background number $a_0(t)$ from
the horizon-scale closure; premise 4 then imports that number as an external constant
into ordinary, local equilibrium dynamics, exactly as standard MOND uses $a_0$,
regardless of how anisotropic the local mass distribution is. RAR, BTFR, and M-σ (§5.5)
are consequently all **equilibrium-dynamics tests of already-formed, virialized
systems**: each takes $a_0(z)$ as given and asks how one system's internal dynamics
respond to it. This is categorically different from asking how density perturbations
*grow* into structure in the first place, which requires cosmological perturbation
theory built on the homogeneous background — exactly the territory (BAO, CMB
anisotropies) that has broken every prior iteration of this project and is deliberately
deferred (§6 items 5–6). The standing test for any future addition to this section:
*does the calculation take $a_0$ as an already-existing external input, or does it need
to explain how structure grew?* Only the former belongs here until the radiation-era
and perturbation sectors are built.

**The framework's falsifiable content is now localized.** A running theme of this
document's own consistency checks (§3, §5.5) is that essentially every locally
calibrated quantity — atomic clocks, standard candles, rulers — turns out to be exactly
invariant across cosmic epochs once measured in its own local units. The precise
statement:

> **Local physics is Planck-unit invariant, except through a single portal: the
> acceleration scale $a_0(t)=\lambda\dot c(t)$ entering AQUAL's interpolating
> function (§4).**

Everything else — the photon sector, the flux/luminosity sector, standard candles — has
been shown (not assumed) to be a change of description relative to an ordinary
expanding, constant-$c$ picture. This sharpens the methodological note below: the
correspondence is not merely assumed to exist in the abstract; it has been **partially
constructed**.

**A methodological note on scope — partially constructed, not merely assumed.** Earlier
versions of this document treated the canonical correspondence between this description
and an ordinary expanding, constant-$c$ one as a pure working assumption. It no longer
is, in two places: (i) the *photon sector* (§3.3, §5.5) maps exactly onto the
Einstein–de Sitter ($\Omega_m=1$) comoving-frame description — every purely photometric
or geometric observable computed so far (redshift, time dilation, luminosity distance,
angular-diameter distance, Tolman dimming, distance duality, blackbody thermodynamics)
coincides exactly with EdS; (ii) the *asymptotic future* (§2.2) maps onto a de Sitter
phase. The remaining, genuinely open question this correspondence answers in standard
terms is: **what is this framework's analog of $\Lambda$?** §2.2 answers it — an
instability of the naive (EdS-equivalent) history, not a constant — but the mechanism
behind its one free parameter is not yet known (§6 item 3). The point of building this
framework's own internal consistency requirements has been vindicated in one respect:
the search for "what standard cosmology is missing" led directly to a concrete,
checkable candidate mechanism, not merely a restatement of the problem.

This document commits to three premises (§1–§3) and one adopted (not derived) dynamical
postulate (§4), and derives their consequences. Every quantity that is *adopted* rather
than *derived* is flagged as such at the point it is introduced.

---

## 1. Premise 1 — The Geometric Arena: Static Euclidean Space, Independent Time

Space is ordinary, static, flat Euclidean 3-space. Time is an independent, Newtonian-style
parameter, not a fourth coordinate mixed with space by a metric. Nothing expands; nothing
curves. Every dynamical effect that might otherwise be attributed to spatial expansion or
spacetime curvature must instead be attributed to position- or time-dependence of
physical quantities — the speed of light foremost among them, per premise 2. This is a
convenient, physically legitimate choice of description, not an assertion that
expanding-spacetime descriptions are wrong: it is one self-consistent way to organize the
same physics, and (unlike an earlier attempt built on reproducing General Relativity's
curved-spacetime predictions exactly) this framework's own dynamical postulate is native
to flat space — Bekenstein & Milgrom's AQUAL, which this framework draws its local
dynamics from, is itself a modification of ordinary Newtonian gravity in Euclidean space.

A direct kinematic consequence, used throughout §3: in this static, spatially homogeneous
space, a light signal's wave crests all move at the *same* instantaneous $c(t)$ — there is
no position-dependence for them to move differently across. Crest spacing (wavelength)
therefore cannot change during flight; only $c(t)$'s own time-dependence, which is common
to every crest, can. This single fact is what forces §3.3's redshift law and rules out
the alternative once tried and abandoned (`ResearchNotes.md` §6).

---

## 2. Premise 2 — The Cosmological Machian Closure

The speed of light's cosmological value is set by the mass enclosed within the observer's
own horizon, in the Machian sense: $c$ is not fixed externally but is mutually consistent
with the horizon mass and radius that themselves depend on $c$'s history — and, as this
section now shows, with premise 4's modification of gravity, since the horizon's own
binding acceleration turns out not to be safely in the Newtonian regime.

### 2.1 Horizon and enclosed mass — Machian by number

The horizon grows at the local light speed: $\dot R_h=c(t)$, equivalently, in integral
form, $R_h(t)=\int_{-\infty}^t c(t')\,dt'$ — the accumulated light-travel distance since
genesis. The two forms are the same statement (fundamental theorem of calculus), not
separate claims.

**Mass conservation is stated at the level of particle number, not mass density —
this is a decision, not the only reading available (§6 item 4 records why).** Particle
number density $n$ is homogeneous and constant (assumed, not derived — §6 item 9): the
enclosed particle count is $N_h(t)=\frac43\pi R_h(t)^3 n$. Combined with premise 3's
universal mass law, the enclosed *rest mass* is
$$M_h(t) = N_h(t)\,m(t) = \frac43\pi R_h(t)^3\, n\, m_0\!\left(\frac{c(t)}{c_0}\right)^{1/2} = \frac43\pi R_h(t)^3\,\rho_0\!\left(\frac{c(t)}{c_0}\right)^{1/2},$$
where $\rho_0\equiv nm_0$ is today's rest-mass density. This counts rest mass only —
radiation energy is not yet included (§0's scope limit; §6 item 5).

### 2.2 The working closure: an AQUAL-consistent dynamical system

**The naive Newtonian closure is inconsistent with premise 4, at its own operating
point.** The Sciama-type relation $c^2\propto GM_h/R_h$ (used in an earlier pass through
this derivation) implicitly assumes Newtonian gravity — but the horizon's own binding
acceleration, $g_h\equiv c^2/R_h$, turns out (self-consistently, below) to sit only a
factor of a few above $a_0$: squarely in AQUAL's transition regime, where premise 4
says Newtonian gravity does *not* apply. Premises 2 and 4, taken together with the
Newtonian closure, contradict each other at the closure's own operating point. The
repair is mandatory, not optional, and — as it turns out — supplies the mechanism this
framework was missing for late-time cosmic acceleration.

**The corrected closure.** For spherical symmetry, AQUAL's field equation integrates
exactly (Bekenstein–Milgrom) to $\mu(g_h/a_0)\,g_h=GM_h/R_h^2$. The Machian relation is
taken as
$$c^2=\kappa\,g_h R_h,$$
the field-based binding, reducing to the old Sciama form when $\mu\to1$. (An alternative
— $c^2\propto$ the AQUAL *potential* directly — was considered and rejected: the
deep-MOND potential $\sqrt{GMa_0}\ln(R/R_\text{ref})$ carries an arbitrary reference
scale, and importing $R_\text{ref}$ would smuggle in exactly the free constant this
construction is trying to explain. The field-based form is reference-free.) Using
$a_0=\lambda\dot c$ (§4) and §2.1's $M_h(t)$, eliminating $g_h$ gives the closed,
autonomous system
$$\dot R_h=c,\qquad \dot c=\frac{c^2}{\kappa\lambda\,x\,R_h},\qquad x=\mu^{-1}\!\left(\frac{R_h^2}{B^2c^{3/2}}\right),$$
for a constant $B$ fixed by $G,\rho_0,c_0,\kappa$. Because $a_0$ involves $\dot c$, this
is a genuine two-dimensional dynamical system — one integration constant beyond the old
algebraic closure. $\kappa$ and $\lambda$ enter every result only through the combination
$\tilde\lambda\equiv\kappa\lambda$; $\kappa=1$ is assumed for the numerics below, with the
resulting $O(1)$ ignorance carried explicitly (§5.5).

**The fixed point: the earlier, simpler closure survives as a special solution.** The
scale-free ansatz $x=\text{const}$ solves the system with $R_h\propto c^{3/4}$ — the
same power-law history derived in an earlier pass — with the operating point fixed at
$$x_*=\frac{3}{4\kappa\lambda}.$$
Every result derived from the pure power-law closure (§3.3's redshift law, §5.5's exact
Einstein–de Sitter photometry) holds *on this fixed point*, for any $\mu$ and any
$\lambda$. **This closure choice does not derive $\lambda$**: the fixed point exists for
every value of $\lambda$, so the earlier hope that self-consistency would pin it down is
recorded here as dead (`ResearchNotes.md` §8).

**The fixed point is unstable — and that instability is this framework's analog of
$\Lambda$.** Linearizing $R_h=B\sqrt{\mu_*}\,c^{3/4}(1+\varepsilon)$:
$$\dot\varepsilon=\frac{3}{2\nu_*}\frac{\dot c}{c}\,\varepsilon,\qquad
\nu_*\equiv\left.\frac{d\ln\mu}{d\ln x}\right|_{x_*}\in(0,1)
\quad\Longrightarrow\quad
\varepsilon(z)=\varepsilon_0\,(1+z)^{-1/\nu_*}.$$
Deviations from the scale-free history are negligible in the past and grow at late
times — exactly $\Lambda$'s characteristic phenomenology, produced here by an
instability rather than a constant. The sign of the one new integration constant
$\varepsilon_0$ sets the branch: $\varepsilon_0<0$ (the horizon sliding *below*
scale-free growth, into the deep-MOND regime) gives late-time acceleration and an older
universe. Cosmography, using the redshift law of §3.3: $q_0=(4-2j)/3$ with
$j\equiv c\ddot c/\dot c^2$; the fixed point gives $j=\tfrac54,\ q_0=+\tfrac12$
(consistent with the EdS correspondence, §5.5), and at linear order
$q_0=\tfrac12+\varepsilon_0(\nu_*+2)/\nu_*^2$.

**Result against real data (the working cosmology of this document).** Fit jointly
against the actual Pantheon+ compilation (1701 SNe, full published STAT+SYS covariance,
$z_\text{HD}>0.01$ cut leaving 1590 SNe, absolute-magnitude/$H_0$ offset analytically
marginalized so only the shape is tested) and the published $a_0(z)$ constraints (§5.5)
jointly, with $\kappa=1$ (simple interpolating function):
$$\varepsilon_0=-0.0678,\qquad \kappa\lambda=0.307,\qquad q_0=-0.56,\qquad
\text{age}=12.8\ \text{Gyr (up from 9.3 on the fixed point)}.$$
The pipeline was validated first: run on flat $\Lambda$CDM alone, it returns
$\Omega_m=0.331\pm0.018$, $\chi^2=1403.7$ — reproducing the published Pantheon+ SN-only
result ($0.334\pm0.018$) to a third of a sigma. At the joint best fit, the framework's
own SN shape costs only $\Delta\chi^2_\text{SN}=+1.6$ relative to that $\Lambda$CDM
fit (equal parameter count on the SN side), while the $a_0(z)$ sector — rigid, sharing
the same $\varepsilon_0,\kappa\lambda$ with no per-survey freedom — is described at
$\chi^2=6.5$ for four constraints, against $\chi^2=20.0$ for the best *free linear*
$a_0(z)$ law fit to the same points. The history is EdS to $0.1\%$ before $z\sim5$ and
departs recently; today's operating point has slid from $x_*=2.44$ to $x_0\approx1.5$–
$1.6$. (Reproduced end-to-end by `joint_fit.py`, archived with `ResearchNotes.md`;
pipeline validation and every fit number independently re-run before merging.) The
standard interpolating function fits distinctly worse once the $a_0$ sector is included
($\Delta\chi^2=42$ jointly) — on the SN data alone the two $\mu$-forms are nearly
degenerate, so it is the $a_0$ data, not the SN shape by itself, that discriminates
$\mu$ (§6 item 8).

**Freeing the local amplitude measures $\kappa$ directly.** Letting the $a_0$
normalization float rather than fixing $\kappa=1$, the joint data prefer a local
$a_0=1.39\times10^{-10}$ m/s² — between SPARC's canonical $1.20\pm0.26$ and MIGHTEE-HI's
$1.69\pm0.13$, i.e. arbitrating that zero-point dispute rather than being tuned to
either — giving $\kappa\approx1.01$: the coefficient assumed unity by fiat above comes
out empirically unity. This is not fully self-consistent yet with §5.5's mass-census
check below, which anchors $a_0$ to SPARC's value specifically for that comparison;
reconciling which $a_0$ anchor is correct is part of the still-open decisive fit
(§6 item 1).

![](../figures/cdot7_hubble_diagram_data.svg)
*Figure: the raw Hubble diagram — real Pantheon+ magnitudes (binned) and both model
curves together, before looking at residuals. The joint-fit trajectory and the exact-EdS
fixed point are visually close over most of the range; the next figure shows where and
by how much they actually differ. Generated by `cdot-7/make_figures.py`, built on
`joint_fit.py`.*

![](../figures/cdot7_hubble_diagram.svg)
*Figure: the same comparison in residual form — binned differences against the real
Pantheon+ compilation (1701 SNe, full covariance), not a smooth proxy curve. The
framework's joint fit (zero line, by construction of the fit) tracks the data at
$\Delta\chi^2=+1.6$ relative to $\Lambda$CDM; the exact-EdS fixed point (dashed)
diverges at high $z$, reproducing EdS's own well-known SN Ia failure — the divergence
visible here is easy to miss in the raw magnitudes above. Generated by
`cdot-7/make_figures.py`, built on `joint_fit.py`.*

**Genesis is unaffected; the asymptotic future is a de Sitter phase.** With lookback
time $w\equiv t_0-t>0$, the backward attractor to $c\to0$ as $w\to\infty$ survives from
the earlier, simpler closure — genesis is not sensitive to this repair. Forward in time,
the trajectory runs away into deep MOND, with $c$ diverging at a *finite coordinate
time* $t_*$ as $c\propto(t_*-t)^{-2/5}$, but the *proper* time needed to reach it
diverges — now only logarithmically ($\Delta\tau_\text{proper}\propto\ln[1/(t_*-t)]$,
numerically $\approx16$ Gyr of proper time per decade of $c$, i.e. $c$ grows
exponentially in proper time with an e-fold time close to $\Lambda$CDM's own de Sitter
rate, $1/(\sqrt{\Omega_\Lambda}H_0)$). A clock never reaches the coordinate singularity —
the genesis-mirror structure (finite coordinate time, infinite proper time) survives,
weakened from power-law to logarithmic. The correspondence of this document's
methodological note therefore extends to the future as well as the past: the deep-MOND
runaway maps onto a de Sitter phase.

**$H_0^\text{hor}$ is an instantaneous rate, and today's $a_0$ is trajectory-invariant.**
$H_0^\text{hor}\equiv(\dot c/c)|_{t_0}$ (not a global ratio $c_0/R_{h,0}$, which held only
under the earlier, simpler closure). Exactly on *any* trajectory of this dynamical
system, $H_0^\text{obs}=\tfrac32\dot c_0/c_0$ (§5.5), so today's $a_0=\lambda\dot
c_0=\tfrac23\lambda c_0H_0^\text{obs}$ regardless of $\varepsilon_0$ — the calibration of
§4 survives this section's closure rebuild untouched.

### 2.3 $c_0$ and $c_z$ are relational, not measured

Under the SI convention (the second fixed by an atomic-transition cycle count, the metre
fixed as a fraction of a light-second), $c$'s numerical value is a tautology: any
observer, at any epoch, calibrating units the same way gets the identical number, always.
**$c_0$ and $c_z$ denote a cross-epoch relational quantity, not an instrument reading** —
the same role redshift $z$ itself plays: $z$ compares a received photon's fixed frequency
against the *receiving* observer's own local reference, not a universal standard, so two
observers at different epochs intercepting the same photons infer different $z$, not
because the photons changed or either observer's own $c$ reads differently on their own
instruments, but because the local reference each compares against differs.

---

## 3. Premise 3 — Planck-Unit Invariance

**Adopted, not derived, but now stated as a single principle rather than two
independent scaling laws.**

> **Planck-unit invariance.** All local physics — every dimensionless coupling
> ($\alpha$, the gravitational fine-structure constant $\alpha_G=Gm^2/\hbar c$, mass
> ratios, and by extension the strong and weak sectors) — is epoch-invariant. Only
> $c(t)$ carries cosmological time-dependence. The conventional choice of which
> dimensionful constants to hold fixed ($G,\hbar,e$) is a units convention, not physics.

Given $G,\hbar$ fixed by this convention, $\alpha_G$-invariance forces a *unique* mass
exponent:
$$m(t) = m_0\left(\frac{c(t)}{c_0}\right)^{1/2}\qquad(\text{equivalently: }m_\text{Pl}\propto c^{1/2}\text{, so "all mass is constant in Planck units"}),$$
exactly, with no exceptions and no position-dependence (unlike an earlier, now-abandoned
attempt at a *local*, position-dependent mass law — `ResearchNotes.md` §2). Newton's
constant $G$ is exactly invariant: $G(t)=G_0$. Given $e,\hbar$ fixed, $\alpha$-invariance
forces the vacuum permittivity $\epsilon_0\propto c^{-1}$ by the identical move (the
Planck charge $q_\text{Pl}=\sqrt{4\pi\epsilon_0\hbar c}$; $e/q_\text{Pl}=\sqrt\alpha$
invariant iff $\epsilon_0\propto c^{-1}$). **What was an unresolved tension in an
earlier pass through this document ("all local physics scales the same way" is false as
dimensionful powers, since $m\propto c^{1/2}$ but $\epsilon_0\propto c^{-1}$) dissolves
here**: the correct statement was never about a shared dimensionful power — it is that
all *dimensionless* physics is invariant, and different dimensionful quantities
necessarily carry different powers of $c$ as a result.

This principle is a postulate, checked below against high-precision data (§5) and
retro-explains several results derived independently before it was identified (the
exact LLR cancellation, §5.1; the exact-standard SN candle, §5.5) — providing them a
common cause rather than merely surviving them. What remains owed is a *mechanism* for
the invariance itself (§6 item 4) — the normal epistemic status of a symmetry
principle, and a better standing debt than an unexplained numerical coincidence, but a
debt nonetheless. **A predictive consequence at zero further cost**: zero drift in
$\alpha$, in $\mu=m_p/m_e$, or in any laboratory dimensionless constant, at every epoch
— trivially satisfied where a generic varying-$c$ proposal would need to tune.

### 3.1 Immediate consequence: atomic scales

The Bohr radius $a_\text{Bohr}\propto\epsilon_0/m_e\propto c^{-1}\cdot c^{-1/2}=c^{-3/2}$.
The Rydberg-type atomic transition frequency $\nu\propto m_e\epsilon_0^{-2}\propto
c^{1/2}\cdot c^2=c^{5/2}$.

### 3.2 Immediate consequence: orbital dynamics

For a two-body system (masses $M,m$, separation $r$) with $G$ invariant and both masses
scaling as $c^{1/2}$, angular momentum conservation for a circular orbit,
$L=m\sqrt{GMr}=\text{const}$, with $GM\propto c^{1/2}$:
$$L\propto c^{1/2}\sqrt{c^{1/2}r}=c^{3/4}r^{1/2}=\text{const}\ \Rightarrow\ r\propto c^{-3/2}.$$

**This exactly matches the atomic-radius exponent found in §3.1.** Orbital radius and
atomic radius scale identically with $c(t)$ — the orbit shrinks in lockstep with the
ruler used to measure it, at every epoch, not only today. This was the design target
(`ResearchNotes.md` §3 records how it was found), not a coincidence discovered after the
fact. §3.4 below shows this lockstep is itself forced by the same invariance principle,
not an independent coincidence.

### 3.3 Immediate consequence: the redshift law — corrected

**An internal inconsistency, found and fixed.** An earlier pass through this document
derived the redshift law from "a photon's conserved frequency" — but that premise is
not available here. Premise 1's static, spatially homogeneous space conserves the
spatial wavenumber $k$ of a propagating wave, not its frequency: a mode
$\varphi=a(t)e^{ikx}$ of the wave equation $\ddot\varphi=c(t)^2\nabla^2\varphi$ obeys an
oscillator equation with slowly varying frequency $\omega(t)=c(t)k$, and the deeply
adiabatic evolution ($\dot c/c\sim10^{-18}\,\text{s}^{-1}$ against optical frequencies)
conserves the photon number (WKB adiabatic invariant), not the photon energy — each
photon's energy *grows* in flight, $E_\gamma(t)\propto c(t)$. Equivalently and more
directly: every wave crest moves at the same instantaneous $c(t)$ (premise 1), so crest
spacing (wavelength) cannot change mid-flight; only a position-dependent $c$ could
stretch it, which is exactly the structure this framework dropped. The old
conserved-frequency law is recorded, and the reasons it fails, in `ResearchNotes.md` §6.

**The corrected law.** A photon emitted at $t_e$ (epoch $c_z$) matches the emitter's
local atomic standard, $\nu_e\propto c_z^{5/2}$ (§3.1); its wavelength,
$\lambda=c(t_e)/\nu_e\propto c_z^{-3/2}$, is conserved in flight. At reception it
oscillates at $\omega_\text{rec}=c_0k\propto c_0c_z^{3/2}$, compared against the
receiver's own standard $\nu_\text{atom}(t_0)\propto c_0^{5/2}$:
$$\boxed{\;1+z=\frac{\nu_\text{atom}(t_0)}{\omega_\text{rec}}=\left(\frac{c_0}{c_z}\right)^{3/2}\quad\Longleftrightarrow\quad c_z=c_0(1+z)^{-2/3}.\;}$$
**The exponent is exactly the Bohr-radius exponent (§3.1), and that is not a
coincidence** — the identical result follows from comparing the conserved wavelength
against the local ruler directly. The physical picture is now sharp: light does not
stretch in flight; the ruler used to measure it has shrunk since emission. For general
mass exponent $s$, $1+z=(c_0/c_z)^{s+1}$; $\tfrac32$ is $s=\tfrac12$'s value.

**Light-curve time dilation is exactly $(1+z)$, and generic in $s$** — redshift and time
dilation are the same physical measurement here (frequency is an inverse period):
$\Delta\tau_0/\Delta\tau_e=(c_0/c_z)^{(s+2)-1}=(c_0/c_z)^{s+1}=1+z$. This distinguishes
the corrected law empirically from the old one (which predicted dilation
$(1+z)^{3/5}\ne1+z$): SN Ia light-curve widths measure the dilation exponent $b$ in
$\Delta t_\text{obs}=\Delta t_\text{em}(1+z)^b$ directly, and the Dark Energy Survey
(White et al. 2024, *MNRAS* 533, 3365; 1504 SNe Ia, $0.1\lesssim z\lesssim1.2$) finds
$b=1.003\pm0.005\,(\text{stat})\pm0.010\,(\text{sys})$ — consistent with this
framework's $b=1$ at $0.3\sigma$, and excluding the old law's $b=3/5$ at $\sim36\sigma$.
**This correction was empirically mandatory, not merely a matter of internal
consistency.**

### 3.4 Why $s=+\frac12$ specifically — from a fitted number to a symmetry statement

Two direct attempts to derive $s=+\tfrac12$ from a Sciama-type self-binding mechanism
failed (full working in `ResearchNotes.md` §5): evaluated at a particle's own Compton
wavelength, $m\propto c^{-2}$; evaluated at its own gravitational radius, dimensionally
degenerate. A third attempt did not derive $s$ either, but forced a decision, now
recorded in §2.1: whether "mass neither created nor destroyed" means particle-number or
mass-density conservation. The number-conserved reading was adopted, with §2.2's
cosmological closure rebuilt to match.

**What derives $s=+\frac12$ now is §3's own invariance principle, not a Machian
self-binding argument.** Given $G,\hbar$ invariant, $s=+\tfrac12$ is the *unique*
exponent making $\alpha_G=Gm^2/\hbar c$ epoch-invariant — and this is exactly the LLR
safety condition of §5.1, restated: LLR safety and $\alpha_G$-invariance are the same
dimensionless statement. This retro-explains why no other value of $s$ was ever going
to survive contact with laser ranging (`ResearchNotes.md` §7 works this identity
through in full), and upgrades the standing debt from "why this fitted exponent" to
"why is local physics Planck-unit invariant" (§6 item 4) — a mechanism owed for a
symmetry, not a numerical coincidence to explain away.

---

## 4. Premise 4 — AQUAL-Spirit Modified Local Dynamics

**Adopted, not derived.** Local gravitational dynamics follows a modified Poisson
equation, in the spirit of Bekenstein & Milgrom's AQUAL[^1]:
$$\nabla\cdot\left[\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right] = 4\pi G\rho,$$
with the interpolating function $\mu(x)\to1$ for $x\gg1$ (recovering ordinary Newtonian
gravity, hence §3.2's orbital-dynamics result in the strong-field regime) and $\mu(x)\to
x$ for $x\ll1$ (the deep-MOND regime, giving flat rotation curves, $v^4=GMa_0$). No
specific form of $\mu$ is fixed by this document yet (§6 item 8); §5.5 shows the
expansion history (§2.2) now constrains it alongside galaxy rotation curves.

**$a_0$ is epoch-dependent, not frozen — and its identity with $\dot c$ is what makes
premise 4 Machian.** Composing $a_0\equiv\lambda c_0H_0^\text{hor}$ with §2.2's
$H_0^\text{hor}\equiv(\dot c/c)|_{t_0}$ gives, at any single epoch,
$$a_0(t)=\lambda\,\dot c(t).$$
**The MOND acceleration scale is, up to $\lambda$, the acceleration of the speed of
light itself** — Newtonian gravity fails precisely where gravitational accelerations
fall below the rate at which $c$ is cosmologically changing. Freezing $a_0$ at today's
value (an earlier, simpler reading) makes the present epoch special for no Machian
reason, and breaks the exact Einstein–de Sitter correspondence of §5.5 (which requires
$\hat a_0(z)\propto(1+z)^{3/2}=c\,H_\text{EdS}(z)$ in local units, the epoch-dependent
reading transported to the standard picture). The epoch-dependent reading is adopted;
the frozen one is recorded as considered and rejected.

**Local physics is Planck-unit invariant except through this one portal.** $a_0$ is not
a local coupling in premise 3's sense — it is cosmological data ($\dot c$) imported into
local dynamics. Every genuinely distinguishable prediction this framework makes flows
through $a_0(t)$: the evolving radial-acceleration-relation scale
$\hat a_0(z)$ (§5.5, now confronted with data), the resulting evolution of the BTFR and
M-σ zero points (§5.5), and (§2.2) the late-time cosmic acceleration itself, once the
closure is built self-consistently with this same $a_0$.

**Numerically**, $\kappa$ and $\lambda$ are no longer independently free: the joint
Pantheon+/$a_0(z)$ fit (§2.2) pins $\kappa\lambda=0.307$, and $a_0$'s empirical value
then fixes the split. Two conventions have both been used and need to be told apart
(§5.3 states the rule): letting $a_0$ float in the fit gives $a_0=1.39\times10^{-10}$
m/s², $\kappa\approx1.01$ — the coefficient assumed unity by fiat comes out essentially
unity, unforced; anchoring $a_0$ instead to SPARC's own local value ($1.20\pm0.26$,
used specifically for the mass-census check in §5.5) gives $\lambda\approx0.265$,
$\kappa\approx1.16$. The two differ because SPARC alone is not the fit's own preferred
global value — reconciling which anchor is correct is explicitly part of the still-open
decisive fit (§6 item 1), not yet settled.

**What this does not yet do.** AQUAL is a non-relativistic theory. It does not, by
itself, guarantee correct relativistic-level predictions (light bending, PPN
parameters) — a limitation shared with the original AQUAL/MOND program, addressed there
only by relativistic completions (e.g. TeVeS) not attempted here (§6 item 7, now more
urgent — see §5.5's lensing-RAR discussion).

---

## 5. Consequences and Checks

### 5.1 LLR safety — checked exactly, by construction, in the Newtonian sector

Round-trip ranging time in coordinate time is $\Delta t_\text{coord}=2r/c(t)$. With
$r\propto c^{-3/2}$ (§3.2) and the atomic clock ticking at $\nu\propto c^{5/2}$ (§3.1):
$$\Delta t_\text{coord}\propto c^{-3/2-1}=c^{-5/2},\qquad \Delta\tau=\nu\,\Delta t_\text{coord}\propto c^{5/2}\cdot c^{-5/2}=c^0=\text{const}.$$
The number of clock ticks recorded for a round trip does not depend on $c(t)$ at all,
hence a data-reduction pipeline assuming constant $c,\nu$ infers a constant range:
$$\frac{\dot r_\text{LLR}}{r_\text{LLR}} = 0,\qquad\text{exactly, at every epoch.}$$
This is not a fitted cancellation checked once at today's epoch — the exponents cancel
identically, for the same reason at any $t$, and (§3.4) it is the same statement as
$\alpha_G$-invariance under premise 3.

**Caveat: exactness here is a theorem of the Newtonian ($\mu=1$) sector.** At lunar
accelerations ($x\sim10^7$), a simple interpolating function ($\mu=x/(1+x)$) leaves
relative residuals $\sim1/x\sim10^{-7}$ — within reach of LLR-class precision;
exponentially saturating forms do not. High-$x$ behavior of $\mu$ is therefore
constrained by solar-system data, not just galaxy rotation curves and the expansion
history (§5.5, §6 item 8).

### 5.2 The fixed-point (EdS-equivalent) cosmology

On §2.2's fixed point, with redshift exponent $n\equiv\tfrac32$ (§3.3): lookback time
and redshift are related by $w(z)=\tau[(1+z)^{1/6}-1]$, and the particle distance is
$$D_p(z)=R_{h,0}\left[1-(1+z)^{-1/2}\right],\qquad D_p(\infty)=R_{h,0}=\frac{2c_0}{H_0^\text{obs}}\approx8.6\ \text{Gpc}.$$
Today's rate: $H_0^\text{hor}=\tfrac23H_0^\text{obs}\approx4.77\times10^{-11}\,
\text{yr}^{-1}$ ($H_0^\text{obs}=70$ km/s/Mpc) — **this ratio ($n=3/2$) is not the value
an earlier pass through this document used ($5/2$); §3.3's redshift correction changes
it, even though the closure-rebuild of §2.2 by itself did not** (a claimed
"$H_0^\text{hor}$ robustness" survived one change but not the other — recorded, not
hidden, in `ResearchNotes.md` §8). Proper age on the fixed point, $\tau_\infty=\tfrac23
H_0^{-1}\approx9.3$ Gyr — the fixed point's own EdS age problem, resolved on the actual
(unstable) trajectory below.

### 5.3 The acceleration scale, numerically

$a_0=\lambda c_0H_0^\text{hor}\approx4.5\times10^{-10}\,\text{m/s}^2$ for $\lambda=1$
(using §5.2's corrected $H_0^\text{hor}$), versus the empirical MOND value
$a_0\approx1.2\times10^{-10}\,\text{m/s}^2$ — $\lambda\approx0.26$ to match. The
order-of-magnitude relation $a_0\sim cH_0$ survives (a long-standing feature of this
research line, not new here), though the tension factor without a derived prefactor is
now $\approx3.8$, not the $\approx2.3$ an earlier pass through this document quoted
before the redshift-law correction. **This value is trajectory-invariant** (§2.2): since
$H_0^\text{obs}=\tfrac32\dot c_0/c_0$ holds exactly on any solution of the dynamical
system, $a_0=\tfrac23\lambda c_0H_0^\text{obs}$ regardless of $\varepsilon_0$ — a
calibration made anywhere on the trajectory survives the closure rebuild untouched.

**Two conventions for $\lambda$ are in use and must be kept straight (§4).** Fit
directly (letting the joint fit's own local-$a_0$ normalization float): $a_0=1.39\times
10^{-10}$ m/s², $\kappa\approx1.01$ — arbitrating between SPARC and MIGHTEE-HI rather
than being anchored to either. Anchored instead to SPARC's own value specifically (used
for the mass-census check below, §5.5, where comparing against an independent baryon
census makes it important not to use a number this same fit re-derives): $\lambda
\approx0.265$, $\kappa\approx1.16$. **Both are legitimate readings of the same fit; they
are not yet reconciled**, and the gap between them (a factor of $\sim1.15$ in $a_0$) is
exactly the kind of thing the decisive four-term fit (§6 item 1) needs to settle,
by carrying $a_0$ as a properly marginalized parameter with its own empirical prior
rather than fixed to either single number.

Numerically, without leaning on it: $\lambda\approx\tfrac32\cdot\tfrac1{2\pi}\approx0.24$
— i.e. $a_0\approx c_0H_0^\text{obs}/2\pi$, the long-standing MOND numerology — sits
within the spread above. Recorded as numerology, not a result; §2.2's closure gives
$\lambda$ a genuine mechanism to attach to, but does not itself derive its value
(§6 item 4).

### 5.4 The lockstep shrinkage is unobservable locally — but only in the Newtonian sector

The lockstep of §3.2 (orbits and atomic rulers shrinking identically) is unobservable
*in principle* by any local Newtonian-regime measurement — §5.1's exact LLR cancellation
is the proof, not a special case: every local length standard shrinks identically, so
there is no local residual to detect, at any epoch. **This is a theorem of the
Newtonian ($\mu=1$) sector specifically, not of the framework generally.** In the
deep-MOND regime, adiabatic evolution of a circular orbit ($v=(GMa_0)^{1/4}$, $L=mvr$
conserved, with $m,GM\propto c^{1/2}$, $a_0\propto c^{5/4}$) gives $v\propto c^{7/16}$,
$r\propto c^{-15/16}$ — *not* the Newtonian $r\propto c^{-3/2}$ — so in local units,
deep-MOND orbits slowly expand and slow down: $\hat r\propto c^{9/16}$, $\hat
v\propto c^{-9/16}$ (equivalently $\hat v\propto(1+z)^{3/8}$ into the past on the fixed
point, consistent with §5.5's $\hat a_0(z)$ evolution, as it must be). Drift rates are
$O(H)$ — a $10^4$ AU binary drifts by tens of metres per year, unobservable directly —
but the lockstep's one genuine escape hatch is deep-MOND systems, and its practical
observable consequence is exactly §5.5's $\hat a_0(z)$ evolution, not a separate dataset
to hunt for.

### 5.5 The flux/luminosity sector, the working cosmology, and confrontation with data

**Luminosity and angular-diameter distance.** Converting local to coordinate units and
propagating to a receiver at fixed proper distance $D_p$, the received flux picks up
exactly two factors of $(1+z)^{-1}$ (per-photon energy growth against a faster-growing
local energy unit; arrival-rate compression against a faster-ticking local clock — both
generic in $s$), giving $d_L(z)=(1+z)D_p(z)$. A bound object of fixed size in local units
was physically larger in the past ($\ell_\text{phys}(t_e)=\ell_0(1+z)$, §3.2's lockstep),
and light travels in straight lines in static Euclidean space, giving
$\theta=\ell_0(1+z)/D_p$, hence $d_A=D_p/(1+z)$. Both results are generic in $s$ — they
are structural consequences of "everything local scales together," not of the specific
exponent $\tfrac12$. Consequently, **Etherington distance duality holds exactly**,
$d_L/d_A=(1+z)^2$ — the standard executioner of tired-light models, passed here — and
**Tolman surface-brightness dimming holds exactly**, $F/\theta^2\propto(1+z)^{-4}$.

**On the fixed point, these assemble into $d_L(z)=\frac{2c_0}{H_0}\left[(1+z)-\sqrt{1+z}\right]$
— term for term the Einstein–de Sitter relation.** This is why §0 can now state the
correspondence as partially *constructed* rather than merely assumed. It is also why an
earlier pass through this framework needed §2.2's closure repair: EdS alone is
observationally excluded by the SN Ia Hubble diagram and its own age problem — and,
independently of any specific value of $s$, **no rescaling of the mass exponent can fix
this**: for general $s$ the fixed-point deceleration is $q_0=\beta\equiv(2-s)/(2(s+1))$,
negative only for $s>2$, which contradicts the kinematic $\dot R_h=c>0$. The failure is
structural to a pure power-law closure, not a tunable artifact — which is exactly what
motivated §2.2's AQUAL-consistent repair.

**The working cosmology (§2.2's fitted trajectory) is fit against real data.** With
$\varepsilon_0=-0.0678,\ \kappa\lambda=0.307$ (simple $\mu$, real Pantheon+ joint fit):
$q_0=-0.56$, age $=12.8$ Gyr (marginally consistent with globular-cluster ages,
$\approx12.5$–13 Gyr, still below $\Lambda$CDM's 13.8), costing only
$\Delta\chi^2_\text{SN}=+1.6$ relative to $\Lambda$CDM at equal parameter count on the
SN side. **This supersedes an earlier pass's fit to a theoretical $\Lambda$CDM proxy
curve** — the pipeline was validated first by reproducing the published Pantheon+
SN-only result exactly (§2.2). The remaining empirical work is the four-term extension
(local RAR shape plus the mass census, §5.6) — the framework's top open item (§6 item 1).

**Standard candles are exactly standard — no astrophysical escape from the EdS
degeneracy.** The Chandrasekhar mass, $M_\text{Ch}\propto(\hbar c/G)^{3/2}/m_H^2\propto
c^{1/2}$ (using $\hbar,G$ invariant, $m_H\propto c^{1/2}$), scales *exactly* as premise 3
requires every mass to — the baryon count $N_\text{Ch}\propto\alpha_G^{-3/2}$ is exactly
constant, and (checked explicitly: Ni-56 energetics, ejecta velocities, Thomson opacity
per unit mass, diffusion times, all invariant in local units under the further, flagged
assumption that strong/weak dimensionless couplings are also Planck-unit invariant) the
peak luminosity in local units is epoch-invariant. This is not an accident of
$s=\tfrac12$ specifically: the candle's drift exponent is *identical* (up to sign) to
the LLR cancellation exponent (§3.4), so any candle evolution large enough to mimic
$\Lambda$CDM's residual against EdS would violate LLR by roughly two orders of
magnitude, for every $(g,s)$ in the family. Every locally-calibrated standard candle or
ruler is therefore exactly standard across epochs, as a matter of principle — the
$\Lambda$-analog could only ever come from the cosmological closure itself (§2.2), never
from astrophysics.

**The thermal sector is reproduced exactly, with no new assumptions.** Conserved mode
occupation plus conserved wavenumber (§3.3) preserve a Planck spectrum exactly in
flight — no spectral distortion is generated by propagation, consistent with the FIRAS
blackbody at the $10^{-5}$ level. In local units, $\hat T(z)=\hat T_0(1+z)$ (matching SZ
and molecular-absorber measurements), $\hat n_\gamma\propto(1+z)^3$,
$\hat u_\gamma\propto(1+z)^4$ — the complete background thermal phenomenology of an
expanding universe, reproduced by a static, shrinking-ruler description.

**A falsifiable, near-parameter-free prediction: the RAR scale evolves.** In local
units, $\hat a_0(z)$ is computed directly from §2.2's real-data joint-fit trajectory
(not the naive fixed-point $(1+z)^{3/2}$, which the trajectory's own slide toward
deep-MOND suppresses):
$$\hat a_0(z)/\hat a_0(0) = 1.44,\ 2.03,\ 2.24,\ 2.91\quad\text{at } z=0.33,\ 0.85,\ 1.00,\ 1.44,$$
fixed by the *same* $\varepsilon_0,\kappa\lambda$ already fitted jointly to the SN
Hubble diagram and this same $a_0(z)$ data (this is now a fit result, not an
independent prediction checked afterward — see the caveat below). **The measurement
this curve is fit against**: MUSE-DARK III (Ciocan et al. 2026, *A&A* 709, L16; 79
star-forming galaxies, $0.33<z<1.44$) finds $a_0(z\sim1)=2.38^{+0.12}_{-0.10}\times
10^{-10}$ m/s² and a global slope $a_1=1.59^{+0.11}_{-0.10}\times10^{-10}$ m/s² (95%
CI) — a detected evolution that by itself excludes standard (constant-$a_0$) MOND, and
which the joint fit above describes at $\chi^2=6.5$ for four constraints against
$\chi^2=20.0$ for the best free linear law. An independent measurement at $z<0.08$
(Vărăşteanu et al. 2025, MIGHTEE-HI, $a_0=1.69\pm0.13\times10^{-10}$) is itself
inconsistent with *any* smooth evolution anchored to the local (SPARC) value, including
MUSE-DARK's own fit extrapolated backward — indicating $\gtrsim0.3$–$0.5\times10^{-10}$
zero-point offsets between surveys and methodologies, which the joint fit's own
residuals (SPARC $0.7\sigma$, MIGHTEE $2.1\sigma$, MUSE amplitude/slope
$\approx1\sigma$) sit inside.

**Caveat, stated plainly.** Because $\varepsilon_0,\kappa\lambda$ are now fit to the
$a_0(z)$ data directly rather than fixed by the SN diagram alone, this is a
*joint description*, not the independent, blind confirmation an earlier pass through
this document reported (where the SN-only $\varepsilon_0$ was checked against $a_0(z)$
data not used to fit it, and landed at $\approx85\%$ of the measured amplitude with the
naive law overshooting to $a_1^\text{eff}=2.46$ — the same qualitative story, less
tightly coupled). Both are legitimate; the earlier, blind version is the more
conservative claim, and the current joint fit is the more decisive one, since it is the
version the four-term extension below builds on directly.

The decisive test — a joint fit of the SN compilation, binned $a_0(z)$ across surveys
with zero-point nuisances, the local RAR shape (not just its amplitude), and the mass
census (§5.6), over $(\varepsilon_0,\kappa\lambda,\lambda)$ jointly with $\Sigma m_\nu$
as a bounded nuisance — has not yet been run (§6 item 1); after the SN+$a_0$ fit this
framework retains essentially one shape degree of freedom, so that test can genuinely
fail it.

![](../figures/cdot7_a0_evolution.svg)
*Figure: the evolving MOND scale, three hypotheses vs. data. Constant $a_0$ (dotted)
is excluded outright by the detected evolution; the naive, unsuppressed fixed-point law
(dashed) overshoots badly; the joint-fit trajectory (solid) describes the data at
$\chi^2=6.5$ for four constraints. Data: MUSE-DARK III (Ciocan et al. 2026, circle and
global-fit crosses) and MIGHTEE-HI (Vărăşteanu et al. 2025, square), whose mutual
inconsistency at low $z$ indicates the cross-survey systematic floor discussed in the
text. Generated by `cdot-7/make_figures.py`, built on `joint_fit.py`.*

### 5.6 The closure density problem — the framework's sharpest current internal tension

The closure of §2.2 does not merely permit a mass density — it demands a specific one,
and that demand is now known to be in tension with the directly measured baryon
content. From the AQUAL horizon condition and the exact trajectory identities:
$$\Omega_\text{closure}\equiv\frac{\rho_0}{\rho_\text{crit}}=\frac89(\kappa\lambda)\lambda x_0^2\mu(x_0)
\qquad\Longleftrightarrow\qquad
\rho_0=\frac{3}{4\pi}\,\kappa\,\mu(x_0)\,x_0^2\,\frac{a_0^2}{Gc_0^2}$$
— the second, $H_0$-independent form (verified algebraically and numerically) is the
right one to use for a mass-budget statement, since it ties the required density
directly to the measured MOND scale rather than to $H_0$ and $\lambda$ separately.
Every factor on the right is already fixed by the fits above: $a_0$ by its empirical
value, $(x_0,\mu_0)$ by the SN+$a_0$ joint fit. **$\Omega_\text{closure}$ is therefore
an output with zero remaining freedom, not a quantity that can be tuned to match the
baryon census after the fact.**

Stated as $F\equiv\rho_0/\rho_b$ (using the primordial-deuterium/BBN value
$\Omega_bh^2=0.0224$, chosen specifically because it does not depend on CMB/$\Lambda$CDM
fitting — the point of this check is precisely to avoid smuggling in an
already-model-dependent number): at the joint-fit $\kappa\lambda=0.307$,
$$F \approx 2.5\text{–}2.9,$$
depending on which of §4's two $a_0$ conventions is used (SPARC-anchored vs. the fit's
own preferred local value — not yet reconciled, see above). **This is not the same
problem as needing dark matter**: $F$ sits robustly *below* $\Lambda$CDM's own
$\Omega_m/\Omega_b\approx6.4$ — the closure is not quietly reproducing the standard
matter budget through a back door. But it is robustly *above* baryons alone: forcing
$\Omega_\text{closure}=\Omega_b$ at fixed SN-fit shape requires $\kappa\approx2.5$,
which drives $a_0$ off its empirical value by a factor of $\sim2$. **The correct
statement of the problem: three independent measurements ($a_0$'s value, the SN shape,
the baryon census) over-determine two parameters $(\lambda,\kappa)$, and at central
values they fail to close by a factor of $1.6$–$2.9$.**

**The one escape within known physics, and why it is only marginal.** Relic neutrino
rest mass is Standard-Model mass not counted in $\Omega_b$ — the one form of additional
mass that does not concede the "no dark matter" claim. With the current direct
laboratory bound (KATRIN, $m_\beta<0.45$ eV at 90% CL, 2025) and the standard
(degenerate-hierarchy) conversion $\Sigma m_\nu\approx3m_\beta\lesssim1.35$ eV:
$\Omega_\nu\lesssim0.030$. This closes the budget only at the most favorable corner of
the fit (low-end $a_0$, high-end $\kappa\lambda$, $F\approx1.4$–$1.6$) and requires
$\Sigma m_\nu\approx1.3$–$1.5$ eV — at or just beyond the current laboratory edge.
**This escape has an external expiry date**: KATRIN's bound is expected to tighten
toward $\sim0.3$ eV; any meaningful improvement closes this option regardless of
anything internal to this framework. (Standard cosmological neutrino-mass bounds,
$\Sigma m_\nu<0.12$ eV, are $\Lambda$CDM/CMB results this framework has no perturbation
sector to inherit — they do not automatically apply here, but by the same token this
framework cannot yet claim the perturbation-level consistency those bounds encode
either.)

**Resolution space, ranked, none of it free:** (i) a Machian-source amendment — should
the horizon's own field/binding energy also source the closure? Order-of-magnitude
plausible, but the coefficient of gravitational field energy is notoriously
convention-dependent and must come from a principled accounting, not be tuned to close
the gap; (ii) a closure-form revision — the one place a factor of $2$–$3$ could
legitimately live, but any change must preserve the fixed-point-plus-instability
structure that already fits the SN diagram and $\hat a_0(z)$; (iii) new non-baryonic
rest mass beyond neutrinos — this is precisely MOND's own historical retreat at cluster
scales, and if ever adopted, §0's "no dark matter" claim must be rewritten to "no dark
matter in galactic dynamics," stated plainly, not left implicit; (iv) acceptance as this
framework's own version of the real, unresolved MOND cluster-mass residual
($\sim2$–$3\times$, suggestively close to the $F$ found here) — legitimate only as a
labeled, standing failure, never treated as background noise.

**Standing falsification condition.** If the decisive four-term fit (SN + $\hat
a_0(z)$ + local RAR + mass census, with $\Sigma m_\nu$ a bounded nuisance) cannot close
the mass budget within $a_0$'s own $\pm20\%$ uncertainty and the laboratory neutrino
bound, the "no unaccounted mass" claim fails at cosmological scales, and this framework
survives only in the weakened form real MOND itself already occupies. Seed-origin work
on $\varepsilon_0$ (§6 item 3) is frozen until this triage completes — the seed's
amplitude is not a meaningful target while the closure's own normalization is in
question.

### 5.7 The M-σ goal of §0: derived qualitatively, honestly short of RAR's decisiveness

For a pressure-supported (dispersion-, not rotation-supported) system in deep-MOND,
virial balance ($M\sigma^2\sim M\times g\times r$ with $g=\sqrt{GMa_0}/r$) gives
$$\sigma^4 \sim \Gamma\,GMa_0,$$
where $M$ is the system's *bulge/stellar* mass. **Unlike the rotation-curve BTFR
relation, $\Gamma$ is not fixed at exactly 1 by this argument** — a flat rotation curve
has an exact asymptotic deep-MOND value, but a dispersion-supported system's virial
balance depends on its density/velocity-anisotropy profile, so $\Gamma=O(1)$ but
structure-dependent, not universal. This mirrors exactly why the observed Faber-Jackson
relation has more scatter than the BTFR. **This relation is about stellar/bulge mass,
not black hole mass** — this framework, like the AQUAL/MOND program generally, treats
$M_\text{BH}$ as an external correlate of $M_\text{bulge}$ (via the empirical, non-MOND
$M_\text{BH}/M_\text{bulge}$ ratio), not something the modified force law itself
determines; the well-known "$M$-$\sigma$ relation" in the black-hole literature is
therefore not a direct test of this section.

The zero-point-evolution prediction, $\Delta\log\hat\sigma=\tfrac14\Delta\log\hat
a_0(z)$ at fixed bulge mass, is $\Gamma$-independent and in principle as clean a test as
the RAR's — but **no clean confrontation is currently available, for a specific,
checked reason, not merely because it hasn't been run.** Two literature findings: (i)
the dramatic $M_\text{BH}$-$\sigma$ evolution reported at $z\sim1$–2 (JWST/ALMA
quasar-host observations, black holes up to $10\times$ overmassive at fixed $\sigma$
relative to the local relation) is on the black-hole channel just excluded above — the
standard interpretation attributes it to black-hole assembly history (heavy seeds,
super-Eddington growth), not bulge dynamics, so it neither supports nor excludes this
section; (ii) the correct channel — stellar-mass-vs-$\sigma$ for quiescent galaxies,
no black hole involved — shows no significant evolution at $z<0.7$ and only mild
evolution at $0.9<z<1.7$, and the existing literature already attributes that mild
evolution to ordinary galaxy size evolution (more compact progenitors at higher $z$), a
completely conventional explanation degenerate in sign with this section's own
prediction. Distinguishing the two requires checking whether the *observed* amount of
evolution exceeds what size evolution alone predicts — a real, well-posed analysis, but
one this document has not performed. Recorded as a genuinely open, tractable item
(§6), distinct in kind from the BTFR/RAR confrontation, which had a ready-made,
already-decisive dataset.

---

## 6. Status and Open Items, In Priority

1. **Extend the real-data joint fit to four terms, and reconcile the two $a_0$
   conventions.** The SN+$a_0(z)$ joint fit (§2.2) is done against real Pantheon+ data
   and real published $a_0(z)$ constraints — no longer a proxy. What remains: add the
   local RAR *shape* (SPARC point-by-point, Lelli/McGaugh/Schombert 2016, not just its
   single $a_0$ value) and the mass census (§5.6) as two more likelihood terms, fit
   jointly over $(\varepsilon_0,\kappa\lambda,\lambda)$ with $\Sigma m_\nu$ a bounded
   nuisance parameter and $a_0$ carried as a properly marginalized parameter with its
   own empirical prior rather than fixed to either the SPARC value or the fit's own
   emergent one — the split between those two conventions ($a_0=1.20$ vs. $1.39\times
   10^{-10}$ m/s², §4/§5.3) is exactly what this resolves. This is now the framework's
   single highest-priority open item, ahead of the seed question, since §5.6 shows the
   mass-budget tension depends on it directly. Secondary channels once it exists:
   low-acceleration lensing RAR by lens redshift; SKA-era BTFR zero-point evolution.
   **M-σ specifically needs a different kind of work first, not just more data**
   (§5.7): its evolution channel is degenerate with ordinary galaxy size evolution in
   the existing literature — the open task is a joint analysis that separates the two.
2. **The closure density problem (§5.6).** A live, quantified, three-way
   over-constraint ($a_0$, SN shape, baryon census) failing by $\times1.6$–$2.9$ at
   central values, with one narrow, externally time-limited escape (laboratory-bound
   relic neutrino mass). Not a byproduct — this bears directly on the "no dark matter"
   claim in §0. Resolution ranked in §5.6; adjudicated by item 1's four-term fit.
3. **Origin and amplitude of the seed $\varepsilon_0$ — frozen pending item 2.** Not a
   constant like $\Lambda$ — a transient, growing instability, so "why now" becomes "why
   does the seed's amplitude put the few-percent-deviation epoch at stellar-age epochs
   regardless of when it started." The amplitude is not a meaningful target while the
   closure's own mass normalization is in question (§5.6); do not resume this until
   item 2 triages.
4. **A mechanism for Planck-unit invariance** (successor to "derive $s$"), which would
   also fix $\lambda$ and $\kappa$ independently of any fit.
5. **Radiation-era closure.** Extend §2.1's Machian source to include radiation energy
   (presumably $u_\gamma/c^2$, itself epoch-dependent in coordinate units, raising its
   own questions) — prerequisite to posing BBN, $z_\text{eq}$, or any CMB-era physics.
   Every result in this document is currently scope-limited to $z\ll z_\text{eq}$.
6. **The perturbation/structure sector** — BAO, CMB anisotropies, growth of structure.
   Depends on item 5. The larger early $\hat a_0$ (§5.5) is a helpful direction for
   early massive-galaxy formation, motivation only, not a result.
7. **Relativistic completion.** This framework currently makes no relativistic-level
   predictions (light bending, PPN parameters, perihelion advance) at all — a real
   scope reduction from an earlier iteration, and now more urgent: the lensing-RAR
   channel proposed under item 1 requires a light-bending prediction this framework does
   not yet have.
8. **Finalize $\mu(x)$'s specific form.** Now triply constrained: high-$x$ by LLR/
   solar-system precision (§5.1); mid-$x$ by the local RAR; and now also by the
   expansion history itself (§2.2/§5.5) — the simple interpolating function currently
   fits the real Pantheon+ SN data alone comparably to the standard one, but the joint
   $a_0(z)$ sector prefers it by $\Delta\chi^2=42$ — an independent, cosmological data
   channel for a choice previously fixed only by galaxy dynamics.
9. **Justify or replace the homogeneity assumption** (§2.1: particle number density $n$
   constant).

**Resolved, recorded for the ledger, not restated as open:** the flux/luminosity sector
(built, §5.5); the tension between premise 3's mass law and the auxiliary EM assumption
(dissolved by the Planck-unit invariance principle, §3); the directional-prediction
dataset hunt (reframed into $d_A(z)$ and $\hat a_0(z)$, both now data-confronted,
§5.4–5.5); the premise 2/4 inconsistency (found and resolved by §2.2's closure
rebuild); the SN time-dilation literature caveat (superseded by DES, §3.3, with
$36\sigma$ margin in this framework's favor over the corrected law's predecessor); the
$\Lambda$CDM-proxy SN fit (superseded by the real Pantheon+ joint fit, §2.2); the
three-way numerical discrepancy in $\Omega_\text{closure}$ (0.134 vs. 0.115 vs. 0.104 —
reconciled exactly as three stated conventions applied to the same formula, §5.6;
`ResearchNotes.md` §14).

[^1]: J. D. Bekenstein and M. Milgrom, "Does the missing mass problem signal the breakdown
of Newtonian gravity?" *Astrophysical Journal* 286, 7–14 (1984). AQUAL's modified Poisson
equation is public, well-established physics; no reproduction concern applies here the
way it did for the scanned Atkinson (1963) source used in an earlier iteration.
