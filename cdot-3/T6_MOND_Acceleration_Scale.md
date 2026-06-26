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
$$a_0 \approx \frac{cH_0}{2\pi} \approx \frac{cH_0}{6} \approx 1.2 \times 10^{-10}\ \text{m/s}^2.$$
Using $H_0 = 70$ km/s/Mpc $= 2.27 \times 10^{-18}$ s$^{-1}$:
$$\frac{cH_0}{2\pi} = \frac{3 \times 10^8 \times 2.27 \times 10^{-18}}{2\pi} \approx 1.08 \times 10^{-10}\ \text{m/s}^2,$$
which is within $\sim 10\%$ of the observed $a_0$. This cosmological–galactic connection
has been noted by multiple authors (Milgrom 1983; Joss 1986; various) and strongly
suggests that whatever sets the MOND scale is related to the large-scale structure of
the universe.

---

## The Model's Relationship to MOND

### What the model has

This model naturally contains the scale $cH_0$. The Hubble constant enters as
$H_0 = \dot{c}/c$, and $c$ is the fundamental kinematic quantity of the theory. Their
product $cH_0 = c \cdot (\dot{c}/c) = \dot{c}$ is the rate of change of $c$ — a
physically meaningful quantity with dimensions of acceleration. So
$$a_0 \sim cH_0 = \dot{c}_0 \approx 6.8 \times 10^{-10}\ \text{m/s}^2.$$
The model "knows" the MOND scale dimensionally. This is encouraging and non-trivial —
most theories do not naturally generate an acceleration of this magnitude.

### What the model does not have

The model does not currently have a **working force law** that produces MOND-like
behaviour at galactic scales. The retardation mechanism (T5) was the attempted bridge,
but it fails by $\sim 10^3$–$10^6$ at galactic radii — and not merely quantitatively:
it is structurally the wrong type of mechanism (distance-keyed, not acceleration-keyed,
T5). The dimensional coincidence $a_0 \sim cH_0$ is real and tantalizing, but
unaccompanied by a mechanism.

### The $a_0$ derivation from the demoted mechanism

For completeness: the earlier (now demoted) derivation proceeded as follows. The
rotation floor $v_\text{flat}^4 = 4G^2M^2H_0^2/c^2$ was claimed from the retardation
mechanism. Matching this to the BTFR $v^4 = GMa_0$:
$$a_0 = \frac{4GM H_0^2}{c^2}.$$
Substituting the "Machian" universal mass $M_\text{univ} = c^3/(2GH_0)$ (derived from
the Sciama relation, also now problematic — T12), one gets:
$$a_0 = 2cH_0.$$
With a geometric factor of $1/(2\pi)$, this gives $a_0 = cH_0/\pi \approx
2.2 \times 10^{-10}$ m/s$^2$ — an 80% overshoot of the observed value. Matching
precisely requires an additional $1/4\pi$ factor that was never derived from first
principles.

The correct diagnosis: this derivation is a chain of dimensional reasoning, each step
of which gives the only combination of $c$, $G$, $H_0$ with the right dimensions. It
cannot fail to give $a_0 \sim cH_0$ regardless of the physics. The explicit ring
integration shows the actual force is $\sim10^6$ too small (T5).

**Conclusion: the $a_0 \sim cH_0$ coincidence is real but unexplained. Treat it as a
hint, not a prediction.**

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
shared by MOND and all cosmologically motivated proposals. The challenge is the
functional form and order-one magnitude — for which no mechanism currently exists.

See T15 for the full RAR discussion. The three OP-2/OP-3/OP-17 problems (MOND
constant, rotation curves, RAR) **stand or fall together**: solving any one solves
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

**General diagnosis:** the scale $\sim cH_0$ keeps matching (dimensional,
linear-friendly) while the functional form keeps failing (needs $\sqrt{M}$, hence
nonlinearity). The MOND form requires a **nonlinear source coupling** that none of the
model's natural linear mechanisms supply. See T14 for the detailed GEM-additive
analysis, the catalytic-cycle calculation (negative result), and the live candidate
directions (Lorentz-form $v\times B_c$, criticality-as-license).

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
   $1/r$ through diffusion, and the background gradient of the cosmic sea provides a
   natural scale $\sim cH_0$ for a transition. Whether the MOND functional form follows
   is the open question (T14).

4. **Inertia modification.** Some MOND formulations (MILU, QI) modify inertia rather
   than gravity. This is not the framing of the present model, but the possibility is
   not excluded.

---

## The Connecton Sea: Current Best Candidate (Not Yet MOND)

The connecton sea = quantum foam (T14) is the leading mechanism from this model for
addressing rotation curves. It:
- Resolves the ballistic/diffusive dilemma that previously blocked $1/r$ gravity.
- Gives diffusion everywhere (through the dense virtual $e^+e^-$ foam), restoring
  Newtonian $1/r$.
- Is not distance-keyed — it is a steady-state diffusion effect, free of the
  geometric $10^6$ (T5).
- Provides a cosmological background gradient $|\nabla\rho_\text{bg}| \sim
  \rho_\text{bg}H_0/c$ that is mass-independent, giving a universal transition scale
  $\sim cH_0$ when the mass's connecton gradient drops to this background level.

**The wall** (caveat 2 of OP-14/T14): reproducing the RAR functional form requires
the low-gradient diffusion to take the specific form $D \propto |\nabla\rho|$ — the
Bekenstein-Milgrom $\mu(x)\to x$ limit. No independent physical reason for this form
was found; the natural reading (small perturbation on the large background) gives
*linear* response = Newton, no enhancement. The foam-sea robustly delivers Newtonian
$1/r$; the MOND/RAR functional form does not fall out and is currently disfavored by
the natural reading.

### The target: a Lorentz-type two-component force

The target equation that could carry $\sqrt{M}$ is a velocity-dependent Lorentz-form
law:
$$\mathbf{g} = \mathbf{g}_\text{Newton} + \mathbf{v}_\text{star} \times \mathbf{B}_c,$$
where $\mathbf{B}_c$ is a magnetic-like component of the $c$-field. A flat rotation
curve requires $B_c \sim v/r$, i.e. $B_c \propto (GM a_0)^{1/4}/r$, which gives
$v \times B_c = \sqrt{GM a_0}/r$ — **carrying the correct $\sqrt{M}$** (deep-MOND +
Tully-Fisher). This repackages the difficulty onto the source scaling of $B_c$
($\propto M^{1/4}$, more non-analytic than $\sqrt{M}$), but it is the first framing
where velocity-dependence, the $\sqrt{M}$ requirement, and a universal $a_0$ coexist
without immediate contradiction.

### Criticality-as-license (speculative bridge)

All galaxies possess central black holes, which provide strong-field critical surfaces.
Two roles for this criticality are distinguished:
- **Role 1** (BH region *sources* the effect): ruled out — would make the amplitude
  $\propto M_\text{BH}$, destroying the universal $a_0$.
- **Role 2** (criticality is an *existence condition* that *licenses* the non-analytic
  coupling, while the horizon sets the scale $a_0 \sim cH_0$): survives. The BH
  criticality need only *exist* somewhere (not operate in the weak field) to permit a
  non-analytic $B_c$ source. Connecting the Lorentz form to this license is the live
  conjecture, unproven.

---

## Relation to the BTFR

If the model eventually produces a force law with a MOND-like regime, the BTFR
emerges automatically (it is a consequence of the MOND interpolation formula in the
deep-MOND limit). The tight observed scatter in the BTFR ($\lesssim 0.1$ dex, with no
residual dependence on galaxy size or surface brightness) strongly constrains the
mechanism: it must be baryonic mass alone that enters, with no other galaxy property.
Any mechanism that introduces a dependence on halo size, velocity dispersion, or
environment is disfavoured.

In the context of this model, where there is no dark matter halo (at least in the
intended dark-matter-free version), the baryons are the only source of gravity and
the BTFR is automatically baryonic — the challenge is only to produce the right
functional form and the correct scale.

---

## Open Questions

- Is there a first-principles derivation of $a_0 = cH_0 / (2\pi)$ or $cH_0 / (4\pi)$
  from the geometry of horizon counting, without reverse-engineering the coefficient?
- The connecton foam-sea (T14) gives Newtonian $1/r$: can a nonlinear extension
  (self-interaction, Lorentz-form $v\times B_c$, or criticality-licensed coupling)
  yield the RAR functional form and the $\sqrt{M}$ Tully-Fisher scaling?
- Is the coincidence $a_0 \sim cH_0$ exact in the sense that $a_0$ should vary with
  cosmic epoch as $c(t)H_0(t)$? If so, galaxy rotation curves at high $z$ should
  show a different $a_0$, which is observationally testable (Milgrom 1983 proposed this).
- The factor $1/(2\pi)$: does it arise from a geometric integration (surface area of
  the horizon sphere) or from some quantum-mechanical phase factor?
- See T15 for the RAR as a discriminating test and T14 for the full mechanism discussion.
