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
but it fails by $\sim 10^3$–$10^6$ at galactic radii. So the dimensional coincidence
$a_0 \sim cH_0$ is real and tantalizing, but unaccompanied by a mechanism.

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
integration (T5) shows the actual force is many orders of magnitude too small.

**Conclusion: the $a_0 \sim cH_0$ coincidence is real but unexplained. Treat it as a
hint, not a prediction.**

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
   connecton field of this model (T14) is a candidate for such a vacuum medium, but
   the explicit connection to $a_0$ has not been worked out.

4. **Inertia modification.** Some MOND formulations (MILU, QI) modify inertia rather
   than gravity. This is not the framing of the present model, but the possibility is
   not excluded.

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
- Could the connecton mechanism (T14) provide a gravitational contribution at galactic
  scales that transitions from Newtonian at short range to MOND-like at long range?
- Is the coincidence $a_0 \sim cH_0$ exact in the sense that $a_0$ should vary with
  cosmic epoch as $c(t)H_0(t)$? If so, galaxy rotation curves at high $z$ should
  show a different $a_0$, which is observationally testable (Milgrom 1983 proposed this).
- The factor $1/(2\pi)$: does it arise from a geometric integration (surface area of
  the horizon sphere) or from some quantum-mechanical phase factor?
