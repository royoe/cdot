# Update — New Observational Test Battery (Proposed T22) and a T15 Sign Correction (2026-07-02)

*Session type: constructive. Prompted by the question: given the current state of standard
cosmology, which further observational results can challenge the model? Beyond compiling
a prioritized test battery, this session produced three new quantitative results (the
model's redshift-drift law, its effective radial expansion rate / Alcock–Paczyński
prediction, and its CMB temperature–redshift law) and found one sign error in T15.
Context: DESI DR2 (2025–2026) now provides percent-level BAO distance ratios with a
dataset-dependent 2.3–4σ preference for evolving dark energy and unresolved CMB/BAO/SN
cross-tensions — the standard model itself is under strain, which raises the value of
calibration-light geometric tests.*

---

## Part 1 — New Derivations (proposed for merge into a new T22, with cross-edits)

### 1.1 Redshift drift (Sandage–Loeb test): a sign-opposite, decisive prediction

For a source at fixed distance $D=\int_{t_e}^{t_0}c\,dt$, differentiating with respect
to observer time gives $dt_e/dt_0 = c_0/c_e = (1+z)^{1/2}$. With $1+z=(c_0/c_e)^2$ and
$H^\text{hor}(z)=H_0^\text{hor}(1+z)^{-1/3}$:
$$\dot z = 2(1+z)\Big[H_0^\text{hor} - H^\text{hor}(z)\,(1+z)^{1/2}\Big]
= H_0^\text{obs}\,(1+z)\Big[1-(1+z)^{1/6}\Big].$$

**$\dot z < 0$ at every redshift** — monotone, no zero crossing. ΛCDM instead has
$\dot z = H_0[(1+z)-E(z)] > 0$ for $z\lesssim2$, crossing zero near $z\approx2.5$.
Numerically (spectroscopic velocity drift $\dot v = c\dot z/(1+z)$, $H_0=70$):

| $z$ | model $\dot z/H_0$ | model $\dot v$ (cm/s/yr) | ΛCDM $\dot z/H_0$ | ΛCDM $\dot v$ (cm/s/yr) |
|---:|---:|---:|---:|---:|
| 0.5 | $-0.105$ | $-0.15$ | $+0.191$ | $+0.27$ |
| 1.0 | $-0.245$ | $-0.26$ | $+0.239$ | $+0.26$ |
| 2.0 | $-0.603$ | $-0.43$ | $+0.034$ | $+0.02$ |
| 4.0 | $-1.538$ | $-0.66$ | $-1.181$ | $-0.51$ |

The prediction is **opposite in sign** to ΛCDM over the entire $z\lesssim2$ range and
~30% larger in magnitude at ELT-ANDES's Lyman-α target range ($z\sim3$–5). ANDES
forecasts $\sim$few cm/s sensitivity over a 20-year baseline — this is a clean,
parameter-free, candle-free, calibration-free discriminator, and arguably the single
best future test of the model. CHIME/HIRAX-type 21 cm drift experiments target the
$z\lesssim2$ window where the sign flip is maximal. *Timeline: 2030s–2040s; the
prediction should be registered now.*

### 1.2 Effective radial expansion rate and the Alcock–Paczyński test (DESI-facing)

The radial redshift-to-distance Jacobian is an observable independent of any standard
ruler calibration. From $D_p(z)=R_0[1-(1+z)^{-1/6}]$:
$$H_\text{eff}(z) \equiv \frac{c}{dD_p/dz} = H_0^\text{obs}\,(1+z)^{7/6}.$$
This — not the proper-time clock rate $\propto(1+z)^{2/3}$ tabulated in T3, and not the
coordinate rate $\propto(1+z)^{-1/3}$ — is the quantity that BAO radial measurements
($D_H/r_d$) probe. Comparison ($\Omega_m=0.3$ ΛCDM):

| $z$ | model $H_\text{eff}/H_0$ | ΛCDM $E(z)$ | ratio |
|---:|---:|---:|---:|
| 0.30 | 1.358 | 1.166 | 1.17 |
| 0.51 | 1.617 | 1.316 | 1.23 |
| 1.00 | 2.245 | 1.761 | 1.28 |
| 2.33 | 4.069 | 3.432 | 1.19 |

A constant offset could hide in the (uncomputed) sound-horizon normalization $r_d$, but
the **shape** varies by ~10% across DESI's range against ~1% data. Sharper still, the
**Alcock–Paczyński parameter** $F_\text{AP}=D_M H/c$ is $r_d$-free:

| $z$ | model | ΛCDM | difference |
|---:|---:|---:|---:|
| 0.51 | 0.644 | 0.591 | $+9.1\%$ |
| 1.00 | 1.470 | 1.358 | $+8.2\%$ |
| 1.50 | 2.475 | 2.365 | $+4.6\%$ |
| 2.33 | 4.436 | 4.506 | $-1.6\%$ |

A $z$-dependent, sign-changing 2–9% anisotropy signal versus 1–2% DESI DR2 precision.
**Caveats before declaring this decisive:** (i) the AP test assumes an intrinsically
isotropic clustering scale exists in the model — the model has no computed BAO feature
(T16), though statistical isotropy of *any* tracer correlation function suffices in
principle; (ii) redshift-space distortions must be marginalized within the model's own
peculiar-velocity theory ($u\approx$ const, T11), not ΛCDM's; (iii) the radial ruler in
a static universe is a frozen *proper* length — the mapping is stated here for the first
time and should be cross-checked. Subject to those, this is the most immediately
data-rich threat to the model after the SN Hubble diagram, and it is *independent* of
the standard-candle assumption that gates T4.

### 1.3 The CMB temperature–redshift relation: the model passes, non-trivially

Observations constrain $T(z)=T_0(1+z)^{1-\beta}$ with $\beta=0.022\pm0.018$ (SZ
clusters to $z\sim1$; quasar-absorber fine-structure/rotational excitation to $z\sim3$,
e.g. $T=7.9\pm1.0$ K at $z=1.97$). Naively fatal for a static cosmology (no adiabatic
cooling). In this model it is passed *exactly*, by the same mechanism as redshift:

- Photons conserve frequency in flight (premise 4): the CMB spectrum remains Planck at
  a constant absolute temperature $T_\text{abs}$ in fixed energy units. (FIRAS measures
  today's spectrum: $T_0 = T_\text{abs} = 2.725$ K. No spectral distortion is generated
  — there is no photon production/destruction, evading the Chluba 2014 objection that
  non-standard TRR scalings imply FIRAS-visible distortions.)
- An absorber at redshift $z$ has transition energies lower by $(1+z)^{-1}$
  ($E\propto c^2$). Its level populations equilibrate to the photon occupation at its
  *own* transition frequency $\nu_z = \nu_0/(1+z)$, giving excitation ratio
  $x = h\nu_z/kT_\text{abs}$. The observer converts $x$ back to a temperature using the
  laboratory value $\nu_0$: $T_\text{reported} = h\nu_0/(kx) = (1+z)\,T_\text{abs}$.

$$\boxed{T_\text{reported}(z) = T_0\,(1+z)\quad\text{exactly}\ (\beta=0).}$$

The absorber channel is therefore an automatic pass — a non-trivial consistency success
that should be recorded (proposed T22 §; cross-reference T2, T16). **Open sub-check:**
the SZ channel is physically distinct (Compton scattering off hot intracluster
electrons at epoch $z$); the $c$-scalings of $\sigma_T\propto c^{-2}$, electron thermal
energies, and the frequency-dependence of $\Delta I$ must be propagated to confirm the
same $(1+z)$ emerges. Assigned as an open question.

### 1.4 T15 sign correction: the MOND regime *shrinks* at high $z$ (and that may be a success)

T15 §"Observational Discriminant" currently states that because
$g_\dagger(z)\propto(1+z)^{-5/6}$ was smaller in the past, "a larger fraction of the
disk [is] dynamically MOND-like at high $z$." **This is backwards.** The MOND regime is
$g_\text{bar} < g_\dagger$; with static orbits and invariant mass, $g_\text{bar}(r)$ of
a given galaxy is time-independent, so a *smaller* $g_\dagger$ means a *smaller* MOND
region. Equivalently $r_t=\sqrt{GM/g_\dagger}\propto(1+z)^{+5/12}$ is *larger* in the
past — exactly as T19 §6 already states ("Early ($r_t$ large): most radii sit inside
$r_t$ → Newtonian"). T19 is correct; T15's sentence must be flipped.

The corrected prediction: **high-$z$ disks are more Newtonian/baryonic, with more
steeply declining outer rotation curves and a lower BTFR zero-point at fixed
$M_\text{bar}$** ($v_f^4 = GM\,g_\dagger(z)$). This is qualitatively the direction of
the reported declining rotation curves of $z\sim1$–2.5 star-forming disks (Genzel et
al. 2017; Lang et al. 2017) — observations that constant-$a_0$ MOND finds awkward.
The model should claim this direction cautiously (pressure support / high gas
dispersions provide the mainstream explanation), but it converts a stale sentence into
a live, testable, ΛCDM-orthogonal signature; JWST/ELT IFU kinematics can measure the
RAR transition point as a function of $z$ directly. → Edits: T15 (flip the sentence and
its implication), T6 open-questions wording (neutral as written, add the corrected
direction), T17 epoch co-evolution test (direction unchanged, but cite corrected T15).

---

## Part 2 — The Prioritized Test Battery (proposed structure for T22)

### Tier 1 — decisive, data already exist, model can compute now
1. **BAO anisotropy / Alcock–Paczyński (DESI DR2/DR3).** §1.2. 2–9% predicted deviations
   vs 1–2% precision, calibration-light. The sharpest currently-available geometric test
   independent of the SN candle systematics gating T4.
2. **CMB temperature–redshift relation.** §1.3. Passed (absorber channel); SZ channel to
   verify. Merge as a recorded success.
3. **Solar-system PPN / light propagation.** Cassini gives $\gamma-1=(2.1\pm2.3)\times
   10^{-5}$; light deflection 1.75″; Shapiro delay. Connecton diffusion gravity has *no
   derived light-bending* (T14 open item 5). Any viable completion must hit PPN
   $\gamma=\beta=1$ at $10^{-5}$ — this is the tightest unaddressed constraint on the
   entire T14 program and should be promoted above the galactic-scale open items.
4. **Cluster-scale missing mass and the Bullet Cluster.** The derived RAR closure is
   baryon-sourced; MOND-identical phenomenology inherits MOND's factor ~2 cluster
   missing-mass problem and the lensing–baryon offset in merging clusters (1E 0657-56)
   — where lensing mass tracks the collisionless component, not the gas. For this model
   the offset *requires* the PBH component to dominate cluster potentials — which
   simultaneously sharpens and constrains audit item III.1 (PBHs must dominate clusters
   but not inner galaxy halos). A quantitative division-of-labour statement is now
   observationally forced, not optional. (Note: lensing statements are conditional on
   test 3 — the model must first predict light bending at all.)

### Tier 2 — decisive, requires model development first
5. **Redshift drift (ELT-ANDES, ~2030s).** §1.1. Prediction now derived and registered;
   opposite sign to ΛCDM for $z\lesssim2$.
6. **Precision D/H from BBN.** Deuterium is measured to ~1%; the model's BBN is
   unworked (T13) but T21 now supplies the weak-rate ($\Gamma\propto c^4$) and
   $Q$-value ($\propto c^2$) inputs. Elevate the BBN computation: it is the model's
   only probe of the $z\sim10^{10}$ regime and doubles as the count-vs-mass premise-fork
   discriminator (T12).
7. **Growth of structure: $f\sigma_8(z)$, RSD, cluster counts.** Entirely unworked. A
   static space with growing $c$ and conserved peculiar momentum ($u\approx$ const —
   *no* Hubble drag) plausibly predicts a very different growth history; ΛCDM-era RSD
   data at 3–5% may already be fatal or may be a discovery channel. Highest-uncertainty,
   highest-stakes gap after the CMB.
8. **Gravitational-wave standard sirens + propagation speed.** GW170817:
   $|c_\text{gw}-c|/c<10^{-15}$ — trivially satisfied *if* connectons/gravity propagate
   at the local $c(t)$ (should be stated as a premise-level check in T14). Sirens
   measure $D_L^\text{GW}(z)$ candle-free: the model must derive GW amplitude decay in
   static space with varying $c$ and confirm $D_L^\text{GW}=D_L^\text{EM}$ (any
   difference is measurable by LISA/ET at the few-% level; in ΛCDM-modified-gravity
   language this is the $\Xi_0$ parameter).
9. **Cosmic chronometers $H(z)$.** Differential ages of passive galaxies measure
   $dz/d\tau$ — in this model $H_\tau(z)=H_0^\text{obs}(1+z)^{2/3}$ *by clock*, which
   must first be reconciled with §1.2's $H_\text{eff}\propto(1+z)^{7/6}$ *by geometry*
   (they are different observables here, unlike FRW where they coincide — itself a
   distinctive, testable signature: **chronometer-$H$ and BAO-$H$ must disagree by
   $(1+z)^{1/2}$ in this model and agree in ΛCDM**). Current ~10–15% chronometer errors
   at $z\sim1$–2 are marginally sufficient; this internal-consistency comparison may be
   the model's most distinctive near-term signature and resolves audit item II.7's
   definitional ambiguity as a *feature*.

### Tier 3 — consistency checks and potential advantages
10. **$\mu=m_p/m_e$ and clock-comparison invariance.** All rest masses invariant → μ
    invariant; gross/fine/hyperfine transition energies all $\propto c^2$ → all clock
    ratios drift-free. Passes ammonia/methanol absorber bounds ($|\Delta\mu/\mu|<
    10^{-7}$) and optical-clock comparisons automatically. Record as passed (new doc or
    T7 appendix), noting this is *forced*, not tuned.
11. **Tolman surface brightness and cosmic-opacity/duality tests.** Etherington holds
    exactly (T4), so SB dims as $(1+z)^{-4}$ and $D_L$/$D_A$ duality tests are passed by
    construction — and are therefore *non-discriminating*. Record to prevent future
    wasted sessions.
12. **Cosmic dipoles / preferred frame.** The model has an absolute rest frame (the
    static sea). The CMB dipole and the matter (quasar/radio-source) number-count dipole
    must agree in direction and kinematic amplitude. The reported ~4–5σ excess of the
    quasar dipole over the kinematic expectation (Secrest et al.) is a ΛCDM anomaly; a
    static-frame model has more freedom here (e.g., intrinsic sea anisotropy) — a rare
    place the model could *outperform*. Speculative; low priority.
13. **A 21 Gyr universe's two-sided age test.** Any single object robustly dated
    $>14.5$ Gyr (white-dwarf cooling with T21's correction, r-process cosmochronometry,
    metal-poor subgiants) would falsify ΛCDM while *confirming* this model — the only
    probe where the model predicts a positive anomaly rather than defending against
    one. Conversely the model tolerates (does not require) their absence. Ties to T20
    item 3.
14. **High-$z$ rotation-curve decline / BTFR zero-point evolution.** §1.4's corrected
    direction; JWST/ELT IFU surveys. Also the T17 lockstep M-σ/BTFR co-evolution test
    (direction unchanged).
15. **FRB dispersion measures.** DM$(z)$ probes $\int n_e\,dl$ with the model's
    different path lengths and $n_e$ history; Macquart-relation data are growing
    rapidly. Requires the baryon-history model; medium priority.

### Explicitly non-discriminating (record to close them off)
- SN light-curve time dilation $(1+z)$ — derived in T4; recent DES confirmation is
  consistent with both models.
- Tolman SB and $D_L/D_A$ duality (see 11).
- Laboratory $\dot c$ searches: all locally measurable dimensionless combinations are
  invariant by construction; dimensionful drift is unobservable in principle. Should be
  stated once, in Core, to preempt the naive objection.

---

## Part 3 — Consolidated Edit/Action List

| # | Action | Target | Type |
|---|--------|--------|------|
| 1 | Create T22 (Observational Test Battery) from Parts 1–2 | new file | New topic |
| 2 | Flip the MOND-fraction sentence; add corrected declining-rotation-curve implication | T15 | Correction (sign error) |
| 3 | Cross-reference corrected direction | T6, T17 | Minor edit |
| 4 | Record redshift-drift law $\dot z = H_0^\text{obs}(1+z)[1-(1+z)^{1/6}]$ | T22 (+T3 pointer) | New result |
| 5 | Record $H_\text{eff}=H_0(1+z)^{7/6}$ and the chronometer-vs-BAO $(1+z)^{1/2}$ split; resolves T3's ambiguous table (audit II.7) | T3, T22 | New result + fix |
| 6 | Record $T(z)=T_0(1+z)$ derivation as a passed test; open SZ-channel sub-check | T22, cross-ref T2/T16 | New result |
| 7 | Promote PPN/light-bending to top of T14 open items | T14 | Priority change |
| 8 | Add cluster missing-mass / Bullet Cluster constraint to the III.1 PBH-vs-RAR resolution session | T5/T6/T15/T16 planning | Structural |
| 9 | State GW-speed premise and $D_L^\text{GW}$ task | T14 | New open item |
| 10 | Elevate BBN D/H computation priority (inputs now exist via T21) | T13 | Priority change |

**Bottom line.** The most dangerous near-term dataset is DESI's anisotropic BAO
(existing, percent-level, candle-free — predicted deviations 2–9%); the most dangerous
unworked theory sector is structure growth; the most distinctive falsifiable signatures
are the sign-opposite redshift drift and the predicted $(1+z)^{1/2}$ disagreement
between chronometer-$H$ and BAO-$H$; and the tightest ignored constraint on the
connecton program is solar-system PPN. The T(z) relation, μ-invariance, duality, and
time dilation are automatic passes that should be banked as successes.
