# T6 — The MOND Acceleration Scale

## Observational Background

Modified Newtonian Dynamics (MOND), proposed by Milgrom (1983), is an empirical
modification of Newtonian gravity that reproduces flat rotation curves without dark
matter. In its simplest form, the effective gravitational acceleration $g$ felt by a
test particle transitions between Newtonian behaviour ($g = g_N$ when $g_N \gg a_0$)
and modified behaviour ($g = \sqrt{g_N a_0}$ when $g_N \ll a_0$), where $g_N = GM/r^2$
is the standard Newtonian acceleration.

The critical acceleration is:
$$a_0 \approx 1.2 \times 10^{-10}\ \text{m/s}^2.$$

This value is empirically determined from galaxy rotation curves and is remarkably
universal — it is the same constant across galaxies spanning orders of magnitude in
mass, surface brightness, and morphology.

### The Baryonic Tully-Fisher Relation

The most precise statement of MOND's success is the **Baryonic Tully-Fisher Relation**
(BTFR), the empirical correlation
$$v_\text{flat}^4 = G M_\text{bar} a_0.$$
This arises naturally in MOND: in the low-acceleration regime ($g \ll a_0$), circular
orbit equilibrium gives $v^2/r = \sqrt{GM a_0}/r \Rightarrow v^4 = GMa_0$. The
relation holds over five decades in baryonic mass with remarkably small scatter
($\lesssim 0.1$ dex), far tighter than predicted by dark-matter models without fine-tuning.

### The numerical coincidence

The MOND acceleration is numerically very close to several combinations of fundamental
constants:
$$a_0 \approx \frac{cH_0}{6} \approx 1.2 \times 10^{-10}\ \text{m/s}^2.$$
Using $H_0 = 70$ km/s/Mpc $= 2.27 \times 10^{-18}$ s$^{-1}$:
$$\frac{cH_0}{6} = \frac{3 \times 10^8 \times 2.27 \times 10^{-18}}{6} \approx 1.14 \times 10^{-10}\ \text{m/s}^2,$$
which is within $\sim5\%$ of the observed $a_0$. The coefficient $6=3P$ is not a
numerical near-miss: it is derived from the horizon radius $R_0=6c/H_0$ (Core §4a).
The $cH_0/(2\pi)$ expression from the literature ($2\pi\approx6.28$) is a cruder
approximation (10% low, and requires $H_0\approx78$ km/s/Mpc for an exact match).
In the connecton picture (T14), $g_\dagger=c^2/R_0$ is identified as the sea's kinematic acceleration — the coefficient is fixed by horizon geometry alone. This cosmological–galactic connection has been noted since Milgrom (1983) and is now structural in the connecton picture (T14).

---

## The Model's Relationship to MOND

### What the model has

This model naturally contains the scale $cH_0^{\text{obs}}$. The two Hubble constants
(Core Principles §4a) are:
- $H_0^{\text{hor}} = \dot{c}/c = 35$ km/s/Mpc (the horizon rate, internal parameter);
- $H_0^{\text{obs}} = P\,H_0^{\text{hor}} = 70$ km/s/Mpc (the observable low-$z$ slope).

They give two natural accelerations:
$$\dot{c}_0 = c_0\,H_0^{\text{hor}} \approx 3.4\times10^{-10}\ \text{m/s}^2,
\qquad
c_0\,H_0^{\text{obs}} \approx 6.8\times10^{-10}\ \text{m/s}^2.$$
The observed MOND scale $a_0 \approx 1.2\times10^{-10}$ m/s$^2$ sits within this
range; the coefficient $cH_0^{\text{obs}}/6$ is derived from $R_0=6c/H_0$ (§"The numerical coincidence"). The model "knows" the MOND scale dimensionally — most theories do not naturally generate an acceleration of this magnitude.

### What the model does not have

The model does not currently have a **working force law** that produces MOND-like
behaviour at galactic scales. The retardation mechanism (T5) was the attempted bridge,
but it fails by $\sim 10^3$–$10^6$ at galactic radii — and not merely quantitatively:
it is structurally the wrong type of mechanism (distance-keyed, not acceleration-keyed,
T5). The coefficient $cH_0/6$ is derived from the horizon geometry $R_0=6c/H_0$ (Core §4a); the RAR closure is derived from connecton indistinguishability (T14) — the $a_0\sim cH_0$ relation is structural in the connecton picture, not a bare coincidence. See T14 for the full derivation and its honest caveats (open: force-law derivation of kinematic identification, transport kernel, attractor convergence).

---

## The Sharpest Statement: The Radial Acceleration Relation (T15)

The RAR (McGaugh, Lelli, Schombert 2016) is the sharpest, most theory-neutral form
of the rotation-curve challenge. Across $\sim150$ galaxies, the observed gravitational
acceleration $g_\text{obs}$ is a **tight one-parameter function** of the Newtonian
baryonic acceleration $g_\text{bar}$:
$$g_\text{obs} = \frac{g_\text{bar}}{1 - e^{-\sqrt{g_\text{bar}/g_\dagger}}},
\qquad g_\dagger \approx 1.2\times10^{-10}\ \text{m/s}^2.$$
Scatter is $\sim0.13$ dex; there is **no residual dependence** on galaxy size,
environment, or morphology. The BTFR is the deep-MOND limit of this relation.

For this model, $g_\dagger \sim cH_0$ is the natural scale. The dimensional match is
structurally inevitable (it is the only acceleration formable from $c$ and $H_0$),
shared by MOND and all cosmologically motivated proposals. The RAR closure is now substantially derived from connecton indistinguishability (T14), matching McGaugh to 0.020 dex; $g_\dagger=c^2/R_0=cH_0/6$ from horizon kinematics. See T14 for status and open items (transport kernel, attractor convergence, force-law derivation of kinematic identification).

See T15 for the full RAR discussion. The MOND acceleration scale (T6), rotation
curves (T5), and RAR (T15) **stand or fall together**: solving any one solves
all three, and the $\sim10^{-6}$ order problem of T5 must be resolved first.

---

## The $\sqrt{M}$ Signature: Why Linear Mechanisms Fail

The key structural feature of MOND is the Baryonic Tully-Fisher Relation $v^4 = GM a_0$.
In the deep-MOND regime this requires the force at radius $r$ to go as
$g_\text{MOND} \propto \sqrt{M}/r$ — note the $\sqrt{M}$, not the $M/r^2$ of Newton.
This is MOND's **irreducible nonlinear signature**.

Every natural mechanism the model produces is **linear in the source mass** $M$
(retardation terms, linear diffusion, additive GEM-like fields). A linear additive
term gives $M/r$, hence $v^4 \propto M^2$ — the wrong Tully-Fisher slope.

**Resolution (T14):** The non-analytic wall holds for *direct-source* couplings, but the transition-radius geometric mean shows that the quarter power emerges from *where the surviving population sits* ($r_t\propto\sqrt{M}$), not from the source coupling — the field equations remain linear. The RAR closure then follows from connecton indistinguishability (0.020 dex vs McGaugh). See T14 for the derivation; criticality-as-license is superseded.

---

## Physical Interpretation of the Coincidence

Several interpretations have been proposed in the literature (not specific to this model):

1. **Cosmological boundary condition.** The MOND scale arises because gravity becomes
   modified when the centripetal acceleration of a circular orbit equals the "cosmic
   acceleration" set by $H_0$. This is phenomenological and lacks a microphysical
   mechanism.

2. **Vacuum energy / dark energy.** $a_0 \sim (c^4\Lambda/3)^{1/2}$ where $\Lambda$
   is the cosmological constant. Since $\Lambda \sim H_0^2$ in ΛCDM, this is the same
   coincidence. The model has no $\Lambda$, so this route is not available here.

3. **Gravitational polarization of the vacuum.** In theories like MOND's relativistic
   extensions (TEVES, AeST), the vacuum polarizability sets the transition scale. The
   connecton foam-sea (T14) is the best candidate from this model: it gives Newtonian
   $1/r$ through diffusion; the transition scale $g_\dagger=c^2/R_0$ comes from the
   horizon radius (not a background gradient — the homogeneous sea has no net directional
   force); the RAR closure is derived from connecton indistinguishability (T14).

4. **Inertia modification.** Some MOND formulations (MILU, QI) modify inertia rather
   than gravity. This is not the framing of the present model, but the possibility is
   not excluded.

---

## The Connecton Sea: The Derived Mechanism

The connecton sea = quantum foam (T14) is the leading mechanism from this model for
addressing rotation curves. It:
- Resolves the ballistic/diffusive dilemma that previously blocked $1/r$ gravity.
- Gives diffusion everywhere (through the dense virtual $e^+e^-$ foam), restoring Newtonian $1/r$.
- Is not distance-keyed — a steady-state diffusion effect, free of the geometric $10^6$ (T5).
- Sets the acceleration floor $g_\dagger=c^2/R_0=cH_0/6$ as the sea's kinematic acceleration (crossing rate $c/R_0$ times $c$; the 6 from $R_0=6c/H_0$, Core §4a). The background connecton sea is a **holographic standing population** with density $\rho_\text{bg}=(\pi/6)\rho_\text{crit}$ ($\hbar$-free, T14) — a standalone result linking the sea to dark energy, not the source of $g_\dagger$.

**The RAR closure is derived (not just motivated).** The Lorentz-form force law
$$\mathbf{g} = \mathbf{g}_\text{Newton} + \mathbf{v}_\text{star} \times \mathbf{B}_c,$$
with $B_c=(GM_\text{bary}\,g_\dagger)^{1/4}/r$ (T14, T17), carries the correct $\sqrt{M}$ in the deep-MOND limit. The $M^{1/4}$ amplitude is the geometric mean of two linear quantities at the transition radius — the field equations are linear; the nonlinearity is in the attractor geometry. The constitutive law $D(g)=g/(g+g_\dagger)$ (MOND's "simple" interpolation) is derived from connecton indistinguishability (T14), matching McGaugh to 0.020 dex; the three alternatives are data-excluded.

**BH role clarified.** The BH is a co-tracer of the baryonic normalization $GM_\text{bary}\,a_0$, not a source of $B_c$. Criticality-as-license is superseded — the closure is derived without it.

---

## Relation to the BTFR

If the model eventually produces a force law with a MOND-like regime, the BTFR
emerges automatically (it is a consequence of the MOND interpolation formula in the
deep-MOND limit). The tight observed scatter in the BTFR ($\lesssim 0.1$ dex, with no
residual dependence on galaxy size or surface brightness) strongly constrains the
mechanism: it must be baryonic mass alone that enters, with no other galaxy property.
Any mechanism that introduces a dependence on halo size, velocity dispersion, or
environment is disfavoured.

With PBH dark matter now the leading candidate (T5, T13, T16), the BTFR becomes a
constraint on that dark component being gravitationally inert with respect to the
MOND interpolation: PBHs provide mass silently, while baryons source the modified
coupling. The tight scatter ($\lesssim 0.1$ dex, no residual on halo size or
environment) then constrains any PBH model — the dark matter must not contribute
independently to the rotation curve beyond its gravitational pull, or the baryonic
tightness breaks. The challenge shifts from "no dark matter needed" to "baryons alone
drive the MOND-like term, PBHs sit inertly below it."

---

## Open Questions

- **Force-law derivation of $g_\dagger$:** The coefficient $g_\dagger=c^2/R_0=cH_0/6$ is identified kinematically (sea's crossing acceleration; the 6 from $R_0=6c/H_0$). The open task is to derive $g_\dagger=c^2/R_0$ from the connecton equations of motion — confirming the crossing-rate acceleration equals the closure's relaxation scale — replacing the dimensional argument with a dynamical one (T14 §Open Items).
- **Transport kernel:** The RAR closure shape is derived from a relaxation-time ansatz; replacing it with a full Boltzmann derivation is the deepening task (T14).
- **Attractor convergence:** Does the Lorentz filter genuinely concentrate the surviving population at $r_t$ at all radii? A dynamical-systems proof is the binding open item (T14, T17).
- **Epoch dependence:** If $a_0\propto c(t)H_0(t)$, galaxy rotation curves at high $z$ should show a lower MOND threshold — testable with JWST/IFU kinematic surveys (T15). Since $M_\text{BH}\propto\sigma^4=GM_\text{bary}\,a_0$ (T17), the BTFR zero-point and the M-σ normalization must co-evolve in lockstep, computable parameter-free from the model's own $c(u)$ and $H^\text{hor}(u)$ — a locked co-evolution no ΛCDM+DM model predicts; testable now with JWST/ALMA high-$z$ dynamical masses paired with high-$z$ AGN masses (T17).
- See T15 for the RAR as a discriminating test and T14 for the full mechanism and coefficient derivation.
