# Static VSL Cosmology — Core Principles

*Clean reference document. Contains only the results that follow rigorously from
the stated premises. Disputed or unresolved derivations (the $a_0$ factor, the
rotation-curve normalization, the $\dot\alpha$ drift, the origin of the mass law and
of the $G$-scaling) are tracked separately in the open-problems document and are
deliberately excluded here.*

*What this model is (tested). The working hypothesis was that this is **not a rival
theory** but a **conformal projection of standard FLRW cosmology onto a static map**
($c\propto a$), in the spirit of Atkinson (1962). **This has now been tested and
refuted** (Open Problems OP-9): the static model and FLRW agree on redshift by
construction but disagree on luminosity distance, and Etherington's reciprocity
theorem proves a genuine conformal reframing cannot do that. **The model is therefore
a genuine rival theory to standard cosmology, not a reframing of it.** Its
distinctive results (finite origin, genesis bootstrap, the $1/d$ retardation
rotation-curve term) are predictions of a non-standard cosmology — but they cannot
also be hidden features of GR, and the model's luminosity distance currently
conflicts with supernova data (the same departure, viewed two ways). The central open
question is now whether the particle-counting framework can be reconciled with SN
distances at all (OP-9, Branch A). The label "VSL" is accurate after all: this is a
real variable-$c$ cosmology, not GR in disguise.*

*Note on naming: earlier drafts were titled "Static **Machian** VSL Cosmology" and
used a Machian mass-generation rule $M\propto c$. That rule has been removed — it was
shown to break supernova distances, kill the rotation-curve mechanism, and contract
orbits (see Open Problems OP-7, OP-8). The current core uses **cosmologically
invariant rest mass**. The word "Machian" is retained only loosely, for the
horizon-relational origin of $c$ itself (premise 2).*

---

## 1. Foundational Premises

The model is a flat, coordinate-static cosmology. There is no metric expansion;
all cosmological dynamics are carried by a time-varying speed of light $c(t)$ and a
time-varying gravitational coupling $G(t)$. Rest mass is invariant. Four premises
define it:

1. **Static geometry.** Physical coordinate space is flat, absolute, and static:
   $\dot a = 0$, $a(t) = 1$. No recessional motion, no spatial curvature.

2. **Horizon particle counting**, $c \propto N$. The local speed of light is
   proportional to the number of particles $N$ within the growing causal horizon.
   The universe is a uniform static particle sea of constant number density $n$,
   so $N \propto R^3$ where $R$ is the horizon radius. *(The bulk-vs-surface form of
   this counting is itself open — see OP-5; the core uses the volume law
   $c\propto R^3$ as baseline.)*

3. **Invariant rest mass.** Particle rest mass is a local invariant, independent of
   the cosmological vacuum state: $m \propto c^{0}$. This replaces the discarded
   Machian rule $M\propto c$. The supernova Hubble diagram, the rotation-curve
   mechanism, and orbital evolution all independently favour a near-invariant mass
   ($|s|\lesssim0.3$ for $m\propto c^s$); $s=0$ is the natural symmetric point (OP-7,
   OP-8). *Why mass is invariant rather than following the PV self-energy law
   ($m\propto c^{-3/2}$) is open (OP-8).*

4. **Local quantization preservation.** Elementary charge $e$ and Planck's constant
   $h$ are strictly invariant. A photon in flight loses no energy: its frequency
   $\nu$ is constant from emission to observation.

A fifth scaling, **$G \propto c^{-2}$**, is required downstream (it makes stellar
flux constant under orbital expansion, keeps the rotation-curve floor alive, and
fits SN distances — OP-8). It is currently *selected* by these constraints rather
than derived from a principle, so it is noted here but flagged as a standing debt,
not a premise.



---

## 2. Redshift Mechanics

Because $\nu$ is fixed in flight, the wavelength at any point is set entirely by the
local light speed there, via $\lambda = c/\nu$. The observed redshift therefore maps
directly to the ratio of present to emission light speed:
$$1 + z = \frac{\lambda_\text{obs}}{\lambda_\text{emit}} = \frac{c_\text{now}}{c_\text{emit}}.$$

For a galaxy at $z = 1$:
$$c_\text{emit} = \tfrac{1}{2}\, c_\text{now}.$$

This is the central observational hook of the model: redshift is a clock on the
historical value of $c$, not a measure of recession.

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

Using $c \propto R^3$ to fix the emission radius for $z=1$:
$$\frac{c_\text{emit}}{c_\text{now}}
  = \left(\frac{R_\text{emit}}{R_\text{now}}\right)^3 = \tfrac12
\quad\Longrightarrow\quad
R_\text{emit} = 2^{-1/3} R_\text{now} \approx 0.7937\,R_\text{now}.$$

Hence:
$$D_{z=1} = R_\text{now} - 0.7937\,R_\text{now} = 0.2063\,R_\text{now}.$$

The distance to a $z=1$ source is about one fifth of the current horizon radius.
(The value in light-years requires fixing $R_\text{now}$. Note that $R_\text{now}$
is finite even though the coordinate past is infinite — the horizon has a definite
present size; see §3 and Open Problems OP-1.)

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

## 7. Status Summary

| Element | Status |
|---|---|
| Premises 1, 2, 4 (static geometry, $c\propto N$, quantization) | Core, stable |
| Premise 3 (invariant rest mass, $m\propto c^0$) | Core; origin open (OP-8) |
| Redshift $1+z = c_\text{now}/c_\text{emit}$ | Core, stable |
| Horizon law $c(u) = c_0(1+2kR_0^2 u)^{-3/2}$ | Core, stable |
| Distance $D_{z=1} = 0.2063\,R_\text{now}$ (volume law) | Core, stable |
| $H \equiv \dot c/c$, $H(u) = H_0/(1+2kR_0^2 u)$ | Core, stable |
| Frequency scaling $\nu \propto c^2$ | Core (given symmetric PV) |
| Time frames + proper age $\tau = \tfrac34 H_0^{-1} \approx 10.5$ Gyr | Resolved (OP-1) |
| Orbital expansion $r\propto c^2$ = constant stellar flux | Core, given $G\propto c^{-2}$ (OP-8) |
| $G \propto c^{-2}$ scaling | **Selected, not derived** — standing debt (OP-8) |
| Rotation-curve floor $v^2 = 2GMH_0/c$ (exists at $s{=}0,g{=}{-}2$) | Mechanism works; normalization open (OP-2/3) |
| Mass law: why invariant, not PV $c^{-3/2}$ | **Open** (OP-8) |
| MOND constant $a_0$ numerical value and $2\pi$ | **Open** (OP-2) |
| Fine-structure drift $\dot\alpha$ | **Open** (OP-4) |
| SN Hubble diagram | Viable near $s=0$; needs real Pantheon+ fit (OP-7) |
| $c$-sourcing: volume vs surface (S′ finite origin) | **Open** (OP-5) |
| Primordial genesis / matter-antimatter | **Open, speculative** (OP-6) |

The invariant-mass branch (premise 3 as stated, plus $G\propto c^{-2}$) is the
current recommended model: it makes the SN Hubble diagram, rotation curves, orbital
evolution, and the faint-young-Sun problem mutually consistent. Its two main
theoretical debts are the *origin of the mass law* (why $s=0$ and not the PV value)
and a *derivation of $G\propto c^{-2}$* (presently selected by four agreeing
constraints, not derived). Both are tracked in OP-8.
