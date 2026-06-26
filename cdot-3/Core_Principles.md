# Static VSL Cosmology — Core Principles

*Clean reference document. Contains the results that follow rigorously from the stated
premises. Disputed or unresolved derivations are tracked in the topic documents T1–T14.*

*What this model is. A genuine rival theory to standard cosmology — a real variable-$c$
cosmology, not GR in disguise. Its firm distinctive results: a finite proper age
($\approx 21$ Gyr), the squared redshift law, orbital expansion $r\propto c^2$, and a
structural **deceleration** $q_0=1/(nP)>0$ — the model cannot mimic apparent cosmic
acceleration for any power-law horizon (T4), so it lives or dies on whether acceleration
is real and standard-candle-clean. Note: the rotation-curve mechanism that earlier drafts
treated as a success has been demoted — it fails at galactic scale by $\sim10^6$ (T5);
dark-matter-free rotation curves are an open problem, not a result.*

*Note on naming: earlier drafts used a Machian mass-generation rule $M\propto c$. That
rule has been removed — it breaks supernova distances and contracts orbits (T4, T9). The
current core uses **cosmologically invariant rest mass**. The model is Machian about the
*speed of light* (relational origin of $c$ in the cosmic matter content, premise 2)
rather than about inertial mass (Sciama). This relational principle — the global matter
content sets $c$, and $c$ sets every physical scale — is the model's deepest organizing
idea (§0, T12).*

---

## 0. The Relational Principle (foundational)

The model's premises are facets of a single relational (Machian) principle:

> **The global matter content of the universe sets the speed of light $c$; and $c$
> sets every energy, length, time, and coupling. Therefore all physical scales are
> referred to the cosmic matter content.**

This is *counting*-Machianism (relational about $c$), distinct from Sciama's
*potential*-Machianism (relational about inertial mass, which this model does **not**
adopt — and cannot, since it would drift the mass as $c^{-10/3}$ and break invariant
mass; T12). The principle runs through the whole structure: it is the root of
premise 2 ($N$ or $M_u$ sets $c$), it makes redshift a comparison of a fixed photon
energy against a now-larger atomic reference (§2), it sets clock rates
($\nu\propto c^2$, §5a), and it makes a moving particle's energy referable to the
growing matter content (§6a). One principle in many arenas.

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
above is preferred but not asserted as derived (T11, T12).

**Inertia.** Inertial mass is invariant and axiomatic (premise 3). What is relational
is the *arena* ($c$), not the mass: "$c\to0$ for a lone particle" means dynamics become
vacuous (no clocks, rulers, propagation), not that inertia vanishes. The model does not
derive the magnitude of $m$ — a standing limitation (T12).

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
   this counting is itself open — see T4; the core uses the volume law
   $c\propto R^3$ as baseline. There is also a **premise-level fork**: the classical
   Machian form $c\propto M_u$ (rest mass of the universe) coincides with $c\propto N$
   for invariant $m$ in the present epoch but diverges at the temporal extremes —
   T12. The fork is kept open.)*

3. **Invariant rest mass.** Particle rest mass is a local invariant, independent of
   the cosmological vacuum state: $m \propto c^{0}$. The supernova Hubble diagram and
   orbital evolution favour a near-invariant mass; $s=0$ is the natural symmetric
   point, and the squared redshift law commits to it (T4, T9). It is also required
   for the conservation-law structure of §0 (a drifting mass would break the symmetric
   flip). *Why mass is invariant rather than following the PV self-energy law
   ($m\propto c^{-3/2}$) is open (T8).*

4. **Local quantization preservation.** Elementary charge $e$ and Planck's constant
   $h$ are strictly invariant. A photon in flight loses no energy: its frequency
   $\nu$ is constant from emission to observation.

A fifth scaling, **$G \propto c^{-2}$**, is required downstream (it makes stellar
flux constant under orbital expansion, reproduces GR weak-field as the PV/Dicke-native
value, and fits SN distances — T8, T9). It is currently *selected* by these
constraints rather than derived from a principle, so it is noted here but flagged as a
standing debt, not a premise.

---

## 2. Redshift Mechanics

### Two anchors that fix the vacuum scaling

Electromagnetism is exact at every epoch:
$$c = \frac{1}{\sqrt{\epsilon_0\,\mu_0}}\quad\text{(all epochs)}.$$
And $\epsilon_0,\mu_0$ must scale **identically** — otherwise the impedance of free
space $Z_0=\sqrt{\mu_0/\epsilon_0}$ would drift and polarization structure could not
survive propagation across cosmological distances. Writing $\epsilon_0\propto\mu_0\propto K$
for a single vacuum index $K$ gives $c = c_0/K$, hence
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
lower frequency** than the same atom today.

### The squared redshift law

Following the discipline of gravitational redshift in GR — where the clock-rate
difference *is* the redshift, applied once — the single physical fact here is that the
atomic energy scale differs between epochs. A spectrograph compares the photon's
wavelength to a local reference line for the same transition, both measured now (common
$c_\text{now}$ cancels):
$$1 + z = \frac{\lambda_\text{obs}}{\lambda_\text{ref}}
= \frac{\nu_\text{ref}}{\nu_\text{phot}}
= \frac{c_\text{now}^{2}}{c_\text{emit}^{2}}
= \left(\frac{c_\text{now}}{c_\text{emit}}\right)^{2},$$
using that the photon's frequency is conserved in flight (premise 4) and the emitted
frequency carried $\nu_\text{emit}\propto c_\text{emit}^2$. Equivalently:
$$\boxed{\,1+z = \left(\frac{c_\text{now}}{c_\text{emit}}\right)^{2}
\;\Longleftrightarrow\; \frac{c_\text{emit}}{c_\text{now}} = (1+z)^{-1/2}
\;\Longleftrightarrow\; K = (1+z)^{1/2}.\,}$$

For a galaxy at $z=1$: $c_\text{emit} = c_\text{now}/\sqrt{2} \approx 0.707\,c_\text{now}$.

### General form and the redshift–mass link

For a general mass scaling $m\propto c^{s}$, the atomic frequency is
$\nu\propto c^{s+2}$, and the same derivation gives
$$1+z = \left(\frac{c_\text{now}}{c_\text{emit}}\right)^{s+2}.$$
**The redshift power and the mass scaling are the same degree of freedom.** Invariant
mass ($s=0$) $\Leftrightarrow$ squared redshift. Redshift is a clock on the historical
value of $c$, not a measure of recession.

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

Two consequences are structural:

- **No finite origin in coordinate time.** $c \to 0$ only as $u \to \infty$. There is
  no Big Bang in map time — only an asymptotic approach to $c = 0$ infinitely far in
  the past. *(The S′ variant of premise 2 gives a finite coordinate origin — see T4.)*
- **The coordinate age is infinite; the proper age is finite.** With $\nu\propto c^2$
  (§5a), the proper age is
  $\tau_\text{total} = 3/(2H_0^{\text{obs}}) \approx 21$ Gyr (T1).

---

## 4. Distance to a Source

Space is static, so the distance to a galaxy is the proper path length the photon
traversed:
$$D = \int_{t_\text{emit}}^{t_\text{now}} c(t)\,dt
    = R_\text{now} - R_\text{emit},$$
where $dR = c\,dt$.

Using $c\propto R^3$ together with $c_\text{emit}/c_\text{now} = (1+z)^{-1/2}$:
$$\left(\frac{R_\text{emit}}{R_\text{now}}\right)^3 = (1+z)^{-1/2}
\quad\Longrightarrow\quad
\frac{R_\text{emit}}{R_\text{now}} = (1+z)^{-1/6}.$$
At $z=1$: $D_{z=1} = R_\text{now}[1 - 2^{-1/6}] \approx 0.1091\,R_\text{now}$.

---

## 4a. Transformation Reference: Observables vs. Redshift

### The two Hubble constants (avoid the trap)

- **Horizon rate** $H_0^{\text{hor}} \equiv (\dot c/c)_0 = 3kR_0^2$
- **Observable Hubble constant** $H_0^{\text{obs}}$ — the low-$z$ slope of the
  redshift–distance relation

These differ by the power $P = s+2$:
$$H_0^{\text{obs}} = P\,H_0^{\text{hor}}.$$
When "$H_0 = 70$" is quoted, it is $H_0^{\text{obs}}$. The map horizon radius is
$R_0 = 3P\,c_0/H_0^{\text{obs}}$. Below, $H_0$ means $H_0^{\text{obs}} = 70$ km/s/Mpc.

### Working formulae (volume law, $P = s+2$)

$$\frac{c_\text{emit}}{c_\text{now}} = (1+z)^{-1/P},
\qquad K = (1+z)^{1/P}.$$
$$D_\text{p}(z) = R_\text{now}\left[1 - (1+z)^{-1/(3P)}\right],
\quad R_\text{now} = \frac{3P\,c_0}{H_0^{\text{obs}}}.$$
$$D_L = (1+z)\,D_\text{p},\qquad D_A = \frac{D_L}{(1+z)^2}\quad\text{(Etherington, exact)}.$$
$$\tau(z) = \frac{3}{2H_0^{\text{obs}}}\left[1 - (1+z)^{-2/3}\right]\quad(P=2),
\qquad\tau_\infty = \frac{3}{2H_0^{\text{obs}}} \approx 21\ \text{Gyr}.$$
Deceleration parameter: $q_0 = 1/(3P) = +1/6 > 0$ (mild deceleration; see T4).

### Comparison table ($P=2$, $H_0=70$) vs. flat $\Lambda$CDM ($\Omega_m=0.3$, $\Omega_\Lambda=0.7$)

Distances in Mpc, times in Gyr. $\Delta\mu = 5\log_{10}(D_L/D_L^{\Lambda\text{CDM}})$.

| $z$ | $c_e/c_0$ | $D_\text{p}$ | $D_L$ | $\tau$ (Gyr) | $D_L^{\Lambda\text{CDM}}$ | $\Delta\mu$ |
|------:|------:|------:|------:|------:|------:|------:|
| 0.1 | 0.954 | 405 | 445 | 1.29 | 460 | $-0.07$ |
| 0.5 | 0.816 | 1679 | 2519 | 4.96 | 2833 | $-0.26$ |
| 1.0 | 0.707 | 2804 | 5607 | 7.75 | 6608 | $-0.36$ |
| 2.0 | 0.577 | 4299 | 12898 | 10.88 | 15540 | $-0.40$ |
| 5.0 | 0.408 | 6634 | 39803 | 14.60 | 46652 | $-0.34$ |
| 10.0 | 0.301 | 8466 | 93121 | 16.72 | 103843 | $-0.24$ |

The residual $\Delta\mu$ rises then falls — not a constant offset, but a shape reflecting
$q_0 = +1/6$ vs. $\Lambda$CDM's acceleration. See T4 for the SN implications.

---

## 5. The Apparent Hubble Law

For nearby sources, let $\Delta t \approx D/c_0$ be the photon travel time.
Using $1+z = (c_0/c_\text{emit})^P$ and expanding to first order in $\Delta t$:
$$c_\text{emit} \approx c_0 - \dot c_0\,\Delta t \implies \frac{c_0}{c_\text{emit}} \approx 1 + H_0^{\text{hor}}\,\Delta t,$$
so $(1+z) = (1+H_0^{\text{hor}}\Delta t)^P \approx 1 + P\,H_0^{\text{hor}}\,\Delta t$, giving:
$$z \approx P\,\frac{\dot c}{c^2}\,D = \frac{H_0^{\text{obs}}}{c_0}\,D.$$

This recovers Hubble's form $cz = H_0^{\text{obs}} D$ with
$$\boxed{\,H_0^{\text{obs}} = P\,H_0^{\text{hor}} = P\,\frac{\dot c}{c}\bigg|_0\,}.$$

The observable Hubble constant is $P$ times the fractional growth rate of $c$.
Differentiating $c = kR^3$ and using $\dot R = c$:
$$H^{\text{hor}} = \frac{\dot c}{c} = 3kR^2 = \frac{3c}{R}, \qquad H_0^{\text{hor}} = 3kR_0^2.$$

$H^{\text{hor}}$ was far larger in the past:
$$H^{\text{hor}}(u) = \frac{H_0^{\text{hor}}}{1 + 2kR_0^2\,u}.$$

---

## 5a. Atomic Frequency Scaling

From the Rydberg energy with $e,h$ invariant, $m_e$ invariant, and $\epsilon_0 \propto c^{-1}$:
$$\nu \propto m_e\,\epsilon_0^{-2} \propto c^{2}.$$
So $\nu \propto c^2$ under invariant mass. This power governs the proper/coordinate
time relation $d\tau/dt = (c/c_0)^{2}$, the finite proper age $3/(2H_0^{\text{obs}}) \approx 21$ Gyr (T1),
and the stellar luminosity scaling $L\propto c^{4}$ (T9).

---

## 6. Orbital Evolution and Constant Stellar Flux

As $c$ rises, stellar luminosity climbs as $L\propto c^4$ (§5a). For the flux
$F=L/4\pi r^2$ at a planet to stay constant, the orbit must expand as $r\propto c^{2}$.

The orbital dynamics deliver exactly this. For an adiabatic circular orbit with
$G\propto c^{g}$ and invariant mass ($s=0$), angular-momentum conservation together
with force balance gives
$$r \propto c^{-(3s+g)}.$$
With $s=0$ and $G\propto c^{-2}$ ($g=-2$):
$$r \propto c^{+2},$$
matching the flux-constancy requirement identically ($L\propto c^4$ and $r^2\propto c^4$).

**Result:** bound systems expand as $r\propto c^2$, exactly compensating for stellar
brightening, holding the flux at a planet constant over cosmic time. See T9 for the
connection to the faint-young-Sun problem.

---

## 6a. Free-Particle Dynamics

For an unbound particle in free flight, linear momentum is conserved (space
homogeneity, §0) while energy is not. With $p=p_0$ fixed and $m$ invariant:
$$\frac{u}{c} = \frac{p_0}{\sqrt{p_0^2 + m^2c^2}}\ \ (\text{decreases as }c\text{ grows}),
\qquad E = c\sqrt{p_0^2 + m^2c^2}\ \ (\text{grows}).$$
A free massive particle **decelerates relative to $c$** as the universe ages (peculiar-
velocity damping $u/c\propto(1+z)^{1/2}$), while its energy grows — the symmetric flip.
For a *bound* orbit, isotropy means **angular momentum** is conserved (no torque from
the isotropic vacuum) — this is why bound systems behave differently from free particles.
See T11 for the full discussion.

---

## 7. Status Summary

| Element | Status |
|---|---|
| Premises 1, 2, 4 (static geometry, $c\propto N$, quantization) | Core, stable |
| Premise 3 (invariant rest mass, $m\propto c^0$) | Core; origin open (T8) |
| Redshift $1+z = (c_\text{now}/c_\text{emit})^2$ (squared law) | Core, derived (T2) |
| Horizon law $c(u) = c_0(1+2kR_0^2 u)^{-3/2}$ | Core, stable |
| Distance $D_{z=1} = 0.1091\,R_\text{now}$ | Core, stable |
| $H^{\text{hor}} \equiv \dot c/c$, $H^{\text{hor}}(u) = H_0^{\text{hor}}/(1+2kR_0^2 u)$ | Core, stable |
| Frequency scaling $\nu \propto c^2$ | Core; $\epsilon_0\propto c^{-1}$ EM-forced |
| Proper age $\tau = 3/(2H_0^{\text{obs}}) \approx 21$ Gyr | Resolved (T1) |
| Orbital expansion $r\propto c^2$ = constant stellar flux | Core, given $G\propto c^{-2}$ (T9) |
| $G \propto c^{-2}$ scaling | PV/Dicke-native; selected by constraints (T8) |
| Transformation table + two $H_0$'s | Core §4a, stable (T3) |
| Conservation: momentum yes, energy no (symmetric flip) | Core §0 (T11) |
| Free-particle peculiar-velocity damping $\propto(1+z)^{1/2}$ | Consistency success (T11) |
| Relational principle ($N{\to}c{\to}$ all scales); Machian about $c$ | Core §0, foundational (T12) |
| Deceleration $q_0=1/(nP)>0$; cannot mimic acceleration | Firm structural result (T4) |
| Galaxy size evolution $r\propto(1+z)^{-1}$ | Consistency success (T10) |
| Rotation-curve mechanism (retardation) | **Demoted — fails at galactic scale, geometric** (T5) |
| Radial Acceleration Relation / MOND functional form | **Open — scale matches, mechanism absent** (T15, T6, T14) |
| Premise-2 fork: count $N$ vs classical Mach $M_u$ | **Open fork** (T12) |
| Mass law: why invariant, not PV $c^{-3/2}$ | **Open** (T8) |
| MOND constant $a_0$ value | **Open** (T6) |
| Fine-structure drift $\dot\alpha$ | **Open** (T7) |
| SN Hubble diagram | Mild tension; $q_0>0$ firm; needs Pantheon+ fit (T4) |
| Primordial genesis / matter-antimatter | **Speculative** (T13) |
| Connecton gravity | **Speculative** (T14) |
