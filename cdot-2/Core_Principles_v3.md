# Static VSL Cosmology — Core Principles

*Clean reference document. Contains only the results that follow rigorously from
the stated premises. Disputed or unresolved derivations (the $a_0$ factor, the
rotation-curve normalization, the $\dot\alpha$ drift, the origin of the mass law and
of the $G$-scaling) are tracked separately in the open-problems document and are
deliberately excluded here.*

*What this model is. A genuine rival theory to standard cosmology, not a reframing of
it — a real variable-$c$ cosmology, not GR in disguise. (An earlier "conformal
projection of FLRW" hypothesis was explored; the Etherington-based **refutation** of it
was later **withdrawn** when the units error it rested on was corrected — the model in
fact sits *on* the Etherington line, differing from FLRW in the implied decelerating
$H(z)$, OP-9. So the model is a rival, but the SN tension is milder than once thought.)
Its firm distinctive results: a finite proper age ($\approx10.5$ Gyr), the squared
redshift law, orbital expansion $r\propto c^2$, and a structural **deceleration**
$q_0=1/(nP)>0$ — the model **cannot** mimic apparent cosmic acceleration for any
power-law horizon (OP-5), so it lives or dies on whether acceleration is real and
standard-candle-clean. Note: the rotation-curve "$1/d$ retardation" mechanism that
earlier drafts treated as a success has been **demoted** — it fails at galactic scale
by $\sim10^6$ (OP-3); dark-matter-free rotation curves are an open problem, not a
result.*

*Note on naming: earlier drafts were titled "Static **Machian** VSL Cosmology" and
used a Machian mass-generation rule $M\propto c$. That mass rule has been removed — it
breaks supernova distances and contracts orbits (OP-7, OP-8). The current core uses
**cosmologically invariant rest mass**. But the **Machian character is central, not
loose**: the model is Machian about the *speed of light* (relational origin of $c$ in
the cosmic matter content, premise 2) rather than about inertial mass (Sciama). This
relational principle — the global matter content sets $c$, and $c$ sets every physical
scale — is the model's deepest organizing idea (§0, OP-15).*

---

## 0. The Relational Principle (foundational)

The model's premises are facets of a single relational (Machian) principle:

> **The global matter content of the universe sets the speed of light $c$; and $c$
> sets every energy, length, time, and coupling. Therefore all physical scales are
> referred to the cosmic matter content.**

This is *counting*-Machianism (relational about $c$), distinct from Sciama's
*potential*-Machianism (relational about inertial mass, which this model does **not**
adopt — and cannot, since it would drift the mass as $c^{-10/3}$ and break invariant
mass; OP-12, OP-15). The principle runs through the whole structure: it is the root of
premise 2 ($N$ or $M_u$ sets $c$), it makes redshift a comparison of a fixed photon
energy against a now-larger atomic reference (§2), it sets clock rates
($\nu\propto c^2$, §5a), and it makes a moving particle's energy referable to the
growing matter
content (§6a). One principle in many arenas.

**Conservation laws — the symmetric flip from standard cosmology.** The map is the
*conjugate frame* to standard cosmology: standard cosmology conserves rest energy and
lets photon energy drop (redshift = energy loss); the map **conserves photon energy**
and lets rest energy change. From the symmetries of the static map (homogeneous,
isotropic, but $c=c(t)$ breaks time-translation), by Noether:
- **Linear momentum conserved** (space homogeneity);
- **Angular momentum conserved** (isotropy);
- **Energy not conserved** (time-translation broken by $c(t)$).

Energy is precisely the quantity allowed to change — the defining feature of the map
frame. The *interpretation* of that energy change (connecton exchange vs. pure
$c$-scaling vs. relational-to-$N$) is an open modelling choice; the relational reading
above is preferred but not asserted as derived (OP-15).

**Inertia.** Inertial mass is invariant and axiomatic (premise 3). What is relational
is the *arena* ($c$), not the mass: "$c\to0$ for a lone particle" means dynamics become
vacuous (no clocks, rulers, propagation), not that inertia vanishes. The model does not
derive the magnitude of $m$ — a standing limitation (OP-15).

---

## 1. Foundational Premises

The model is a flat, coordinate-static cosmology. There is no metric expansion;
all cosmological dynamics are carried by a time-varying speed of light $c(t)$ and a
time-varying gravitational coupling $G(t)$. Rest mass is invariant. Four premises
define it:

1. **Static geometry.** Physical coordinate space is flat, absolute, and static:
   $\dot a = 0$, $a(t) = 1$. No recessional motion, no spatial curvature.

2. **Horizon counting**, $c \propto N$. The local speed of light is
   proportional to the number of particles $N$ within the growing causal horizon.
   The universe is a uniform static particle sea of constant number density $n$,
   so $N \propto R^3$ where $R$ is the horizon radius. *(The bulk-vs-surface form of
   this counting is itself open — see OP-5; the core uses the volume law
   $c\propto R^3$ as baseline. There is also a **premise-level fork**: the classical
   Machian form $c\propto M_u$ (rest mass of the universe) coincides with $c\propto N$
   for invariant $m$ in the present epoch but diverges at the temporal extremes —
   OP-16. The fork is kept open.)*

3. **Invariant rest mass.** Particle rest mass is a local invariant, independent of
   the cosmological vacuum state: $m \propto c^{0}$. This replaces the discarded
   Machian rule $M\propto c$. The supernova Hubble diagram and orbital evolution
   favour a near-invariant mass; $s=0$ is the natural symmetric point, and the squared
   redshift law commits to it (OP-7, OP-8). It is also required for the conservation-law
   structure of §0 (a drifting mass would break the symmetric flip). *Why mass is
   invariant rather than following the PV self-energy law ($m\propto c^{-3/2}$) is open
   (OP-8). (Note: the rotation-curve mechanism no longer provides independent support —
   it has been demoted, OP-3.)*

4. **Local quantization preservation.** Elementary charge $e$ and Planck's constant
   $h$ are strictly invariant. A photon in flight loses no energy: its frequency
   $\nu$ is constant from emission to observation.

A fifth scaling, **$G \propto c^{-2}$**, is required downstream (it makes stellar
flux constant under orbital expansion, reproduces GR weak-field as the PV/Dicke-native
value, and fits SN distances — OP-8/OP-11). It is currently *selected* by these
constraints rather than derived from a principle, so it is noted here but flagged as a
standing debt, not a premise.



---

## 2. Redshift Mechanics

*This section was substantially corrected. Earlier drafts used
$1+z = c_\text{now}/c_\text{emit}$ (linear). That was an unaudited assumption: it implicitly
took the emitted atomic frequency to be epoch-independent, which is false once the
atomic energy scale is tracked. The corrected law is derived below. (See Open
Problems OP-11 for the full audit and the retirement of the linear law.)*

### Two anchors that fix the vacuum scaling

Electromagnetism is exact at every epoch:
$$c = \frac{1}{\sqrt{\epsilon_0\,\mu_0}}\quad\text{(all epochs)}.$$
And $\epsilon_0,\mu_0$ must scale **identically** — otherwise the impedance of free
space $Z_0=\sqrt{\mu_0/\epsilon_0}$ would drift and polarization structure could not
survive propagation across cosmological distances (Puthoff's argument from observed
aligned polarization). Writing $\epsilon_0\propto\mu_0\propto K$ for a single vacuum
index $K$ gives $c = c_0/K$, hence
$$\epsilon_0 \propto \mu_0 \propto K \propto c^{-1}.$$
This is **forced by electromagnetism**, not a model assumption. It makes $Z_0$
constant and (with $e,h$ invariant) makes the fine-structure constant $\alpha$
invariant.

### The atomic energy scale is epoch-dependent

With $e,h$ invariant (premise 4), invariant mass (premise 3), and the EM-forced
$\epsilon_0\propto c^{-1}$, the Rydberg energy and atomic transition frequency scale
as
$$E_\text{Ryd} = \frac{m e^4}{8\epsilon_0^2 h^2} \propto c^{2},
\qquad \nu_\text{atomic} = E_\text{Ryd}/h \propto c^{2}.$$
So an atom at an earlier epoch (lower $c$) emitted a transition at a **genuinely
lower frequency** than the same atom today. This is the factor the old linear
derivation dropped.

### Redshift, applied once (no double-count)

Following the discipline of gravitational redshift in GR — where the clock-rate
difference *is* the redshift, applied once, not multiplied by a separate
wavelength-stretch — the single physical fact here is that the atomic energy scale
differs between epochs. A spectrograph compares the photon's wavelength to a local
reference line for the same transition, both measured now (common $c_\text{now}$
cancels):
$$1 + z = \frac{\lambda_\text{obs}}{\lambda_\text{ref}}
= \frac{\nu_\text{ref}}{\nu_\text{phot}}
= \frac{c_\text{now}^{2}}{c_\text{emit}^{2}}
= \left(\frac{c_\text{now}}{c_\text{emit}}\right)^{2},$$
using that the photon's frequency is conserved in flight (premise 4, the
energy-conserving map frame) and the emitted frequency carried
$\nu_\text{emit}\propto c_\text{emit}^2$. Equivalently, in terms of the vacuum index
$K=c_0/c_z$:
$$\boxed{\,1+z = \left(\frac{c_\text{now}}{c_\text{emit}}\right)^{2}
\;\Longleftrightarrow\; \frac{c_\text{emit}}{c_\text{now}} = (1+z)^{-1/2}
\;\Longleftrightarrow\; K = (1+z)^{1/2}.\,}$$

For a galaxy at $z=1$: $c_\text{emit} = c_\text{now}/\sqrt{2} \approx 0.707\,c_\text{now}$
(not $0.5\,c_\text{now}$ as the old linear law gave).

### General form and the redshift–mass link

For a general mass scaling $m\propto c^{s}$, the atomic frequency is
$\nu\propto c^{s+2}$, and the same derivation gives
$$1+z = \left(\frac{c_\text{now}}{c_\text{emit}}\right)^{s+2}.$$
**The redshift power and the mass scaling are the same degree of freedom.** Invariant
mass ($s=0$) $\Leftrightarrow$ squared redshift; PV mass ($s=-3/2$) $\Leftrightarrow$
$\sqrt{\,}$-redshift; the discarded linear law corresponds to $s=-1$, which is
neither — confirming it was never a chosen premise. The current model commits to
$s=0$ (squared redshift); the supernova fit (OP-7) effectively measures $s$ and can
confirm or revise this. Redshift is a clock on the historical value of $c$, not a
measure of recession.

---

## 3. Horizon Evolution Law

The horizon grows into the static particle sea at the instantaneous light speed:
$$\frac{dR}{dt} = c(t).$$

With $c \propto N \propto R^3$, write $c(t) = k\,R(t)^3$. Substituting:
$$\frac{dR}{dt} = k R^3.$$

Solving exactly (let $u = t_\text{now} - t \ge 0$ be coordinate lookback time):
$$R^{-2}(u) = R_0^{-2} + 2k\,u,
\qquad
c(u) = \frac{c_0}{\left(1 + 2kR_0^{2}\,u\right)^{3/2}}.$$

Two consequences are structural and worth stating up front:

- **No finite origin in coordinate time.** $c \to 0$ (equivalently $R \to 0$) only
  as $u \to \infty$. There is no Big Bang in map time — only an asymptotic approach
  to $c = 0$ infinitely far in the past.
- **The quantity $\dfrac{1}{2kR_0^{2}}$ is a timescale, not an age.** It equals
  $\tfrac{3}{2}H_0^{-1}$ (using $H_0 = 3kR_0^{2}$ from §5) and sets the
  characteristic horizon scale. It must **not** be read as the age of the universe;
  the coordinate age is infinite, and the *proper* (atomic) age is finite and
  computed separately. With invariant mass the atomic frequency power is
  $\nu\propto c^2$ (see §5a), giving proper age
  $\tau_\text{total} = \tfrac{3}{4}H_0^{-1} \approx 10.5$ Gyr
  (Open Problems OP-1, general result $\tfrac{3}{3p-2}H_0^{-1}$).
  Earlier drafts that called $3/(2H_0)$ a "metric age" were in error.

---

## 4. Distance to a Source

Space is static, so the distance to a galaxy is simply the proper path length the
photon traversed:
$$D = \int_{t_\text{emit}}^{t_\text{now}} c(t)\,dt
    = \int_{R_\text{emit}}^{R_\text{now}} dR
    = R_\text{now} - R_\text{emit},$$
where the change of variable uses $dR = c\,dt$ directly.

Using $c\propto R^3$ together with the corrected redshift law
$c_\text{emit}/c_\text{now} = (1+z)^{-1/2}$ (§2) to fix the emission radius:
$$\left(\frac{R_\text{emit}}{R_\text{now}}\right)^3 = \frac{c_\text{emit}}{c_\text{now}}
 = (1+z)^{-1/2}
\quad\Longrightarrow\quad
\frac{R_\text{emit}}{R_\text{now}} = (1+z)^{-1/6}.$$
At $z=1$: $R_\text{emit}/R_\text{now} = 2^{-1/6} \approx 0.8909$, hence
$$D_{z=1} = R_\text{now} - 0.8909\,R_\text{now} = 0.1091\,R_\text{now}.$$

The distance to a $z=1$ source is about one ninth of the current horizon radius.
*(This supersedes the old value $0.2063\,R_\text{now}$, which used the discarded
linear redshift law. The full distance–redshift relation and all downstream numbers,
ages, and the SN comparison must be recomputed under the squared law — flagged as the
next major task; see OP-11.)* The value in light-years requires fixing $R_\text{now}$,
which is finite even though the coordinate past is infinite (§3).

---

## 4a. Transformation Reference: Observables vs. Redshift

This section collects the working formulae for converting a measured redshift into
the model's physical quantities, and tabulates them against standard $\Lambda$CDM.
Every future recomputation should start here to avoid unit errors. All results use
the **volume horizon law** ($c\propto R^3$) and **invariant mass** ($s=0$, so the
frequency/redshift power is $P = s+2 = 2$). For a general mass scaling, replace $2$
by $P = s+2$ throughout.

### The one subtlety that causes errors: two Hubble constants

There are **two distinct $H_0$'s** and conflating them mis-normalizes every distance:

- **Horizon rate** $H_0^{\text{hor}} \equiv (\dot c/c)_0 = 3kR_0^2$ — the fractional
  growth rate of $c$, internal to the horizon law (§5).
- **Observable Hubble constant** $H_0^{\text{obs}}$ — the low-$z$ slope of the
  redshift–distance relation that an astronomer actually fits.

Expanding the model's distance at low $z$ shows these differ by the power $P$:
$$H_0^{\text{obs}} = P\,H_0^{\text{hor}}.$$
When "$H_0 = 70$" is quoted, it is $H_0^{\text{obs}}$. The map horizon radius must
therefore be written $R_0 = 3c_0/H_0^{\text{hor}} = 3P\,c_0/H_0^{\text{obs}}$. Using
$H_0^{\text{obs}}$ directly in $R_0 = 3c_0/H_0$ understates distances by the factor
$P$ (a spurious $\approx -1.8$ mag offset at $P=2$). Below, $H_0$ means
$H_0^{\text{obs}} = 70$ km/s/Mpc unless stated, and
$1/H_0^{\text{obs}} \approx 13.97$ Gyr.

### Working formulae (volume law, $P = s+2$)

$$\text{Light-speed ratio:}\quad \frac{c_\text{emit}}{c_\text{now}} = (1+z)^{-1/P},
\qquad \text{vacuum index } K = \frac{c_0}{c_z} = (1+z)^{1/P}.$$
$$\text{Horizon radius at emission:}\quad \frac{R_\text{emit}}{R_\text{now}}
 = (1+z)^{-1/(3P)}.$$
$$\text{Proper (line-of-sight) distance:}\quad
 D_\text{p}(z) = R_\text{now}\left[1 - (1+z)^{-1/(3P)}\right],
 \quad R_\text{now} = \frac{3P\,c_0}{H_0^{\text{obs}}}.$$
$$\text{Luminosity distance (standard candle, OP-5):}\quad D_L = (1+z)\,D_\text{p},$$
$$\text{Angular-diameter distance:}\quad D_A = \frac{D_\text{p}}{1+z}
 = \frac{D_L}{(1+z)^2}\ \text{(Etherington, satisfied exactly).}$$
$$\text{Proper lookback time } (P=2):\quad
 \tau(z) = \frac{3}{4H_0^{\text{obs}}}\left[1 - (1+z)^{-2/3}\right],$$
with total proper age $\tau_\infty = \tfrac34 (H_0^{\text{obs}})^{-1} \approx 10.5$
Gyr (§OP-1). The coordinate lookback is
$u(z) = \tfrac{3}{2H_0^{\text{hor}}}[(1+z)^{1/3}-1]$.

### Comparison table

Model (volume law, $P=2$, $H_0^{\text{obs}}=70$) vs. flat $\Lambda$CDM
($\Omega_m=0.3$, $\Omega_\Lambda=0.7$, $H_0=70$). Distances in Mpc, times in Gyr.
$\Delta\mu = 5\log_{10}(D_L^{\text{model}}/D_L^{\Lambda\text{CDM}})$ is the SN
distance-modulus difference.

| $z$ | $c_\text{emit}/c_\text{now}$ | $K$ | $D_\text{p}$ | $D_L$ | $D_A$ | $\tau$ | $D_L^{\Lambda\text{CDM}}$ | $D_A^{\Lambda\text{CDM}}$ | $\tau_{\Lambda\text{CDM}}$ | $\Delta\mu$ |
|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| 0.1 | 0.9535 | 1.049 | 405 | 445 | 368 | 0.64 | 460 | 380 | 1.30 | $-0.07$ |
| 0.5 | 0.8165 | 1.225 | 1679 | 2519 | 1119 | 2.48 | 2833 | 1259 | 5.04 | $-0.26$ |
| 1.0 | 0.7071 | 1.414 | 2804 | 5607 | 1402 | 3.88 | 6608 | 1652 | 7.72 | $-0.36$ |
| 2.0 | 0.5774 | 1.732 | 4299 | 12898 | 1433 | 5.44 | 15540 | 1727 | 10.24 | $-0.40$ |
| 5.0 | 0.4082 | 2.449 | 6634 | 39803 | 1106 | 7.30 | 46652 | 1296 | 12.31 | $-0.34$ |
| 10.0 | 0.3015 | 3.317 | 8466 | 93121 | 770 | 8.36 | 103843 | 858 | 13.00 | $-0.24$ |

### Reading the table

- **Light speed and $K$:** at $z=1$, light was emitted at
  $c_\text{emit} = 0.707\,c_\text{now}$ (vacuum index $K=\sqrt2$), not $0.5$ as the
  old linear law gave.
- **Distances** run smaller than $\Lambda$CDM, but only mildly once normalized
  correctly: the luminosity distance sits within $\sim 0.07$–$0.40$ mag of
  $\Lambda$CDM across $0.1 \le z \le 10$, peaking near $z\approx2$. There is **no
  gross over-dimming** — the earlier $(1+z)^{5/2}$ catastrophe was a units artifact
  (OP-5).
- **The residual is a shape, not an offset:** $\Delta\mu$ rises then falls,
  reflecting the model's $q_0 = 1/(3P) = +1/6 > 0$ (mild deceleration) against
  $\Lambda$CDM's acceleration. This curvature-sign difference is the genuine open SN
  tension (OP-5), not a normalization issue.
- **Angular-diameter distance** turns over (maximum near $z\approx2$) as in standard
  cosmology, but at a smaller peak value.
- **Lookback/age:** the model compresses cosmic history — total proper age
  $\approx 10.5$ Gyr vs $\Lambda$CDM's $\approx 13.5$ Gyr — a mild tension (OP-1),
  not the
  former "infinitely stretched past."

---

## 5. The Apparent Hubble Law

For nearby sources, Taylor-expand the past light speed over a short lookback
$\Delta t = D/c$:
$$z \approx \frac{\dot c}{c}\,\Delta t \approx \left(\frac{\dot c}{c^2}\right) D.$$

Defining an apparent recession velocity $v = cz$ recovers the Hubble form $v = HD$
with
$$\boxed{\,H \equiv \frac{\dot c}{c}\,}.$$

In this model the Hubble constant is the fractional growth rate of the speed of
light, not an expansion rate. Differentiating $c = kR^3$ and using $\dot R = c$:
$$\dot c = 3kR^2\dot R = 3kR^2 c,$$
so
$$H = \frac{\dot c}{c} = 3kR^2 = \frac{3c}{R}, \qquad H_0 = 3kR_0^2.$$

$H$ is **not constant in time.** In terms of coordinate lookback $u$ (from §3),
$$H(u) = \frac{H_0}{1 + 2kR_0^2\,u},$$
so $H$ was far larger in the past and asymptotes to $H_0$ today. $H_0$ denotes
specifically the present-epoch value — a single fixed number — which is why results
may legitimately be expressed in units of $1/H_0$.

---

## 5a. Atomic Frequency Scaling

Atomic and nuclear transition frequencies set the rate of physical clocks and the
energy of emitted photons. Built from the Rydberg energy $\nu = E_\text{Ryd}/h$ with
$E_\text{Ryd} = m_e e^4/(8\epsilon_0^2 h^2)$, under the premises ($e,h$ invariant;
$m_e$ invariant, premise 3; symmetric PV $\epsilon_0 \propto c^{-1}$):
$$\nu \propto m_e\,\epsilon_0^{-2} \propto c^{0}\cdot c^{2} = c^{2}.$$
So $\nu \propto c^2$ under invariant mass. (The general rule is $\nu\propto c^{p}$
with $p = s+2$ for $m\propto c^s$; the discarded Machian $s=1$ gave $p=3$.)

This power governs the proper/coordinate time relation $d\tau/dt = (c/c_0)^{2}$, the
finite proper age $\tfrac{3}{4}H_0^{-1}$ (§3), the photon-energy factor in luminosity
distance, and the stellar luminosity scaling $L\propto c^{2p}=c^{4}$ (OP-8).

**Caveat:** $\epsilon_0\propto c^{-1}$ rests on the symmetric PV split
$\epsilon_0,\mu_0\propto K$, the same choice that keeps $\alpha$ classically
invariant (OP-4). An asymmetric convention would change $p$.

---

## 6. Orbital Evolution and Constant Stellar Flux

*This section replaces the discarded "Machian orbital lock." The Machian rule
$M\propto c$ was introduced to freeze orbits, but worked properly it contracts them
($r\propto c^{-2}$) and simultaneously brightens stars — a habitability disaster —
besides breaking the rotation-curve mechanism and SN distances (OP-7, OP-8). With
invariant mass the correct requirement is not a frozen orbit but a **constant
stellar flux** at the planet, which the dynamics deliver via controlled expansion.*

The relevant stability is radiative, not geometric. As $c$ rises, nuclear-reaction
photons gain energy and stellar luminosity climbs as $L\propto c^{2p}=c^4$ (§5a,
OP-8). For the flux $F=L/4\pi r^2$ at a planet to stay constant, the orbit must
expand as $r\propto c^{2}$.

The orbital dynamics deliver exactly this. For an adiabatic circular orbit with
$G\propto c^{g}$ and orbiting/central mass $\propto c^{s}$, angular-momentum
conservation ($mvr=\text{const}$) together with force balance ($v^2=GM/r$) gives
$$r \propto c^{-(3s+g)}.$$
With invariant mass ($s=0$) and $G\propto c^{-2}$ ($g=-2$):
$$r \propto c^{+2},$$
matching the flux-constancy requirement $L\propto r^2$ identically (since
$L\propto c^4$ and $r^2\propto c^4$).

**Result:** bound systems are *not* frozen — they expand as $r\propto c^2$, and this
expansion exactly compensates for stellar brightening, holding the flux on a planet
constant over cosmic time. The faint-young-Sun problem and orbital evolution are the
same mechanism. This requires $G\propto c^{-2}$, which is currently selected by this
and three other constraints rather than derived (see the premises note and OP-8).

---

## 6a. Free-Particle Dynamics

For an *unbound* particle in free flight, linear momentum is conserved (space
homogeneity, §0) while energy is not. With $p=p_0$ fixed and $m$ invariant:
$$\frac{u}{c} = \frac{p_0}{\sqrt{p_0^2 + m^2c^2}}\ \ (\text{decreases as }c\text{ grows}),
\qquad E = c\sqrt{p_0^2 + m^2c^2}\ \ (\text{grows}).$$
So a free massive particle **decelerates relative to $c$** as the universe ages (its
fixed momentum buys an ever-smaller fraction of the growing $c$), while its energy
grows — the symmetric flip (standard cosmology would hold the energy fixed and let the
momentum decay). This is the model's analogue of **peculiar-velocity damping**:
$u/c\propto(1+z)^{1/2}$, versus standard FLRW's $(1+z)^1$ — same direction, comparable
rate, a consistency success with no scale catastrophe.

For a *bound* orbit the relevant symmetry is isotropy, so **angular momentum** is
conserved (no torque from the isotropic vacuum) — this is what underlies the orbital
expansion $r\propto c^2$ of §6, and it is why bound systems behave differently from
free particles. (A photon conserves frequency/energy, not momentum; a massive particle
conserves momentum, not energy. These differ because a photon has no rest frame and
$E=pc$ locks the two — only its phase/frequency can be the invariant. Whether one
action enforces both consistently is open, OP-15.)

---

## 7. Status Summary

| Element | Status |
|---|---|
| Premises 1, 2, 4 (static geometry, $c\propto N$, quantization) | Core, stable |
| Premise 3 (invariant rest mass, $m\propto c^0$) | Core; origin open (OP-8) |
| Redshift $1+z = (c_\text{now}/c_\text{emit})^2$ (squared law) | Core, corrected (OP-11) |
| Horizon law $c(u) = c_0(1+2kR_0^2 u)^{-3/2}$ | Core, stable |
| Distance $D_{z=1} = 0.1091\,R_\text{now}$ (volume law, squared redshift) | Core, updated (OP-11) |
| $H \equiv \dot c/c$, $H(u) = H_0/(1+2kR_0^2 u)$ | Core, stable |
| Frequency scaling $\nu \propto c^2$ | Core; $\epsilon_0\propto c^{-1}$ EM-forced (OP-11) |
| Time frames + proper age $\tau = \tfrac34 H_0^{-1} \approx 10.5$ Gyr | Resolved (OP-1) |
| Orbital expansion $r\propto c^2$ = constant stellar flux | Core, given $G\propto c^{-2}$ (OP-8) |
| $G \propto c^{-2}$ scaling | PV/Dicke-native value (OP-11); debt largely discharged |
| Transformation table + observable vs horizon $H_0$ | Core §4a, stable |
| Conservation: momentum & ang. mom. yes, energy no (symmetric flip) | Core §0 (OP-15) |
| Free-particle peculiar-velocity damping $\propto(1+z)^{1/2}$ | Consistency success (OP-15) |
| Relational principle ($N{\to}c{\to}$ all scales); Machian about $c$ | Core §0, foundational (OP-12/15) |
| Deceleration $q_0=1/(nP)>0$; cannot mimic acceleration | Firm structural result (OP-5) |
| Rotation-curve mechanism (was $v^2{=}2GMH_0/c$) | **Demoted — fails at galactic scale $\sim10^6$** (OP-3) |
| Premise-2 fork: count $N$ vs classical Mach $M_u$ | **Open fork** (OP-16) |
| Mass law: why invariant, not PV $c^{-3/2}$ | **Open** (OP-8) |
| MOND constant $a_0$ numerical value and $2\pi$ | **Open** (OP-2) |
| Fine-structure drift $\dot\alpha$ | **Open** (OP-4) |
| SN Hubble diagram | Mild tension; $q_0>0$ firm; needs real Pantheon+ fit (OP-5/7) |
| $c$-sourcing: volume vs surface (S′ finite origin) | **Open** (OP-5) |
| Primordial genesis / matter-antimatter | **Open, speculative** (OP-6) |

The invariant-mass branch (premise 3 as stated, plus $G\propto c^{-2}$) is the
current recommended model: it makes the SN Hubble diagram (modulo the $q_0>0$ tension),
orbital evolution, and the faint-young-Sun problem mutually consistent. Its main
theoretical debts are the *origin of the mass law* (why $s=0$ and not the PV value) and
a *derivation of $G\propto c^{-2}$* (presently selected by agreeing constraints, not
derived), both tracked in OP-8; and, newly, **rotation curves without dark matter are
unsolved** (the retardation mechanism was demoted, OP-3). *This document was given a
surgical update after Session 3 (conservation laws, the relational principle, the OP-3
demotion, the $q_0$ result); a full reorganization around the relational principle of
§0 is flagged as a future task.*
