# Foundation — Universal Scaling and AQUAL-Spirit Local Dynamics

*Status: foundational, active construction. This is the third premise-set attempted for
this variable-$c$ program (see `ResearchNotes.md` for why the first two were superseded).
This document is self-contained — no cross-references to earlier iterations. History and
cross-references live in `ResearchNotes.md`.*

---

## 0. Purpose and Scope

This is a minimal foundation for a physical theory in which the speed of light $c$ is
not a universal constant but a cosmologically-determined quantity, sourced by the mass
enclosed within an observer's horizon, and in which *all* local rest mass tracks that
same cosmological quantity by one universal power law. Local gravitational dynamics is
modified at low acceleration in the spirit of Bekenstein & Milgrom's AQUAL, with the
modification's characteristic acceleration scale tied to the same cosmological quantity.
The goal remains a framework capable of producing MOND-like dynamics (flat rotation
curves, the radial acceleration relation, the M-σ relation) without a separate
dark-matter sector.

**Scope reduction from earlier attempts, stated plainly.** This document does not
attempt to reproduce General Relativity's relativistic predictions (light deflection,
perihelion advance) exactly. That was a feature of an earlier, now-superseded local
closure; the mechanism adopted here is explicitly Newtonian-level, matching the AQUAL
program it draws from. A relativistic completion, if one is needed, is future work
(§6).

This document commits to three premises (§1–§3) and one adopted (not derived) dynamical
postulate (§4), and derives their immediate consequences. Every quantity that is
*adopted* rather than *derived* is flagged as such at the point it is introduced — this
framework has, at this stage, two standing theoretical debts (§6 items 1, 3), not zero.

**A methodological note on scope, carried over unchanged.** This framework assumes,
without constructing, a canonical correspondence between an ordinary expanding,
constant-$c$ description of the universe and this one. The point of working out this
framework's own internal consistency requirements — what a mass-scaling or
gravitational-modification law has to do to survive contact with local data and produce
MOND-like dynamics — is that whatever is *necessary* here is a candidate for whatever
the standard picture is *missing*. The correspondence itself is future work, contingent
on these findings, not a prerequisite for them.

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

---

## 2. Premise 2 — The Cosmological Machian Closure

The speed of light's cosmological value is set by the mass enclosed within the observer's
own horizon, in the Machian sense: $c$ is not fixed externally but is mutually consistent
with the horizon mass and radius that themselves depend on $c$'s history.

### 2.1 Horizon and enclosed mass — Machian by number

The horizon grows at the local light speed: $\dot R_h=c(t)$, equivalently, in integral
form, $R_h(t)=\int_{-\infty}^t c(t')\,dt'$ — the accumulated light-travel distance since
genesis. The two forms are the same statement (fundamental theorem of calculus), not
separate claims.

**Mass conservation is stated at the level of particle number, not mass density —
this is a decision, not the only reading available (§6 item 1 records why).** Particle
number density $n$ is homogeneous and constant (assumed, not derived — §6 item 5): the
enclosed particle count is $N_h(t)=\frac43\pi R_h(t)^3 n$. Combined with premise 3's
universal mass law, the enclosed *mass* is
$$M_h(t) = N_h(t)\,m(t) = \frac43\pi R_h(t)^3\, n\, m_0\!\left(\frac{c(t)}{c_0}\right)^{1/2} = \frac43\pi R_h(t)^3\,\rho_0\!\left(\frac{c(t)}{c_0}\right)^{1/2},$$
where $\rho_0\equiv nm_0$ is today's mass density. Mass density itself is *not* flat —
it rises as $c(t)$ does, since it is built from a fixed particle count times a rising
per-particle mass. This is adopted specifically because it is the more literal reading
of "mass neither created nor destroyed" once premise 3 allows individual rest mass to
vary — the alternative (density flat, particle count silently falling) would require an
unexplained coalescence process, not simple non-creation.

### 2.2 The working closure: Sciama-type scaling, rebuilt for a rising density

The leading Machian relation, $c^2\propto GM_h/R_h$, with $M_h(t)\propto R_h(t)^3(c/c_0)^{1/2}$
(§2.1, not the flat-density $M_h\propto R_h^3$ of a mass-conserved reading) gives
$$c^2\propto R_h^2\left(\frac{c}{c_0}\right)^{1/2}\quad\Rightarrow\quad R_h\propto c^{3/4}.$$
Combined with the kinematic $\dot R_h=c$: writing $R_h=Ac^{3/4}$, $\dot R_h=A\cdot\frac34
c^{-1/4}\dot c=c$ gives the ODE $\dot c=\frac{4}{3A}c^{5/4}$, with solution
$$c(t) = c_0\left(1-\frac{t-t_0}{\tau}\right)^{-4},\qquad \tau\equiv\frac{3R_{h,0}}{c_0}.$$
As a check: at $s=0$ (flat density, premise 3 switched off) this same derivation
collapses back to $\dot c\propto c$, the pure exponential of an earlier attempt — so this
is a genuine generalization, not a different calculation (`ResearchNotes.md` §6).

**Genesis is unaffected**: with lookback time $w\equiv t_0-t>0$, $c(w)=c_0(1+w/\tau)^{-4}
\to0$ smoothly as $w\to\infty$, exactly as required.

**A new feature: a finite future coordinate-time singularity, and why it is not
physically reached.** As $t\to t_0+\tau$, $c(t)\to\infty$ — a genuine consequence of this
closure, not a flaw to patch around. But the *proper* time (accumulated local clock time,
using premise 3's own $\nu\propto c^{5/2}$) needed to get there diverges:
$$\Delta\tau_\text{proper}(U) = \int_0^U\left(1-\frac uτ\right)^{-10}du = \frac\tau9\left[\left(1-\frac U\tau\right)^{-9}-1\right]\ \xrightarrow{U\to\tau^-}\ \infty.$$
A clock never actually reaches it, exactly mirroring genesis from the other direction
(finite coordinate time to the past singularity's edge, infinite proper time; here,
finite coordinate time to the future one, infinite proper time). This structure — finite
proper past, infinite proper future — recurs independently elsewhere in this project's
history (`ResearchNotes.md` §6), which is some reassurance it is not an artifact specific
to this derivation.

**$H_0^\text{hor}$ is redefined as an instantaneous rate, not a global ratio.** Under the
old (flat-density) exponential closure, $\dot c/c$ was exactly constant and equal to
$c_0/R_{h,0}$ everywhere — the two were the same thing. Under this closure they are not:
$\dot c/c$ varies with epoch ($\propto c^{1/4}$), so $H_0^\text{hor}$ is now defined as
its value *today*: $H_0^\text{hor}\equiv(\dot c/c)|_{t_0}=4/\tau$. This is the definition
used throughout §5.

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

## 3. Premise 3 — Universal Local Scaling

**Adopted, not derived.** All rest mass — every particle's, and by composition every
body's — scales with the same cosmological $c(t)$ by one universal power law:
$$m(t) = m_0\left(\frac{c(t)}{c_0}\right)^{1/2},$$
exactly, with no exceptions and no position-dependence (unlike an earlier, now-abandoned
attempt at a *local*, position-dependent mass law — §6, `ResearchNotes.md` §3). Newton's
constant $G$ is exactly invariant: $G(t)=G_0$.

This is a postulate, checked below against high-precision data (§5), not derived from a
deeper mechanism. Providing that derivation is this framework's first standing
theoretical debt (§6 item 1).

**Auxiliary assumption, carried over and made explicit.** Electric charge $e$ and
Planck's constant $\hbar$ are invariant; the vacuum permittivity $\epsilon_0\propto
c^{-1}$, forced by requiring the fine-structure constant $\alpha=e^2/(4\pi\epsilon_0\hbar
c)$ to be invariant. This is a separate assumption from premise 3's mass law — it
constrains the electromagnetic sector, not the mass sector — and the two are not
obviously required to be consistent with a single notion of "all local physics scaling
the same way." This tension is flagged, not resolved (§6 item 7).

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
(`ResearchNotes.md` §7 records how it was found), not a coincidence discovered after the
fact.

### 3.3 Immediate consequence: the redshift law

Comparing a photon's conserved frequency against the local atomic standard $\nu\propto
c^{5/2}$ (§3.1) at reception:
$$1+z = \frac{\nu_0}{\nu(t_z)} = \left(\frac{c_0}{c_z}\right)^{5/2}\quad\Rightarrow\quad c_z = c_0(1+z)^{-2/5}.$$

### 3.4 The mass-conservation fork is resolved; $s=+\frac12$ itself is still adopted, not derived

Two direct mechanisms for deriving $s=+\frac12$ were tried and failed (full working in
`ResearchNotes.md` §6): a particle's rest energy self-sourced via Sciama-type binding to
the horizon mass, evaluated at its own Compton wavelength, gives $m\propto c^{-2}$; the
same idea evaluated at its own gravitational radius is dimensionally degenerate
($m=M_h/2$). Neither is a live candidate.

A third line of attack did not derive $s=+\frac12$ either, but forced a decision that
had been implicit and unexamined: whether "mass neither created nor destroyed" (§2.1)
means particle number is conserved or mass density is. **§2.1–2.2 now adopt the
number-conserved reading** — the more literal one, and the one that does not require an
unexplained coalescence process — with the consequence that §2.2's cosmological closure
is a rebuilt, non-exponential one rather than the simple exponential a flat-density
reading would give. This is a premise choice, checked for consistency (§2.2), not a
derivation of $s$ itself: item 1's theoretical debt is narrower now (why $+\frac12$
specifically, given number-conservation) but still open.

---

## 4. Premise 4 — AQUAL-Spirit Modified Local Dynamics

**Adopted, not derived.** Local gravitational dynamics follows a modified Poisson
equation, in the spirit of Bekenstein & Milgrom's AQUAL[^1]:
$$\nabla\cdot\left[\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right] = 4\pi G\rho,$$
with the interpolating function $\mu(x)\to1$ for $x\gg1$ (recovering ordinary Newtonian
gravity, hence §3.2's orbital-dynamics result in the strong-field regime) and $\mu(x)\to
x$ for $x\ll1$ (the deep-MOND regime, giving flat rotation curves, $v^4=GMa_0$). No
specific form of $\mu$ is fixed by this document yet (§6 item 6).

**Tying the acceleration scale to this framework's own cosmological content.** Rather
than importing $a_0$ as an unexplained empirical constant, it is set by the same
cosmological rate that governs $c(t)$'s own evolution (§2.2):
$$a_0 \equiv \lambda\, c_0 H_0^\text{hor},$$
for some dimensionless $\lambda=O(1)$. This keeps the modification's characteristic scale
tied to the same Machian content that determines everything else in this framework,
rather than treating it as a free import from outside. $\lambda$ is not yet derived
(§6 item 1, alongside premise 3's own justification) — §5 checks what value would be
needed to match the observed scale.

**What this does not yet do.** AQUAL is a non-relativistic theory. It does not, by
itself, guarantee correct relativistic-level predictions (light bending, redshift beyond
the leading kinematic effect of §2.2, PPN parameters) — a limitation shared with the
original AQUAL/MOND program, addressed there only by relativistic completions (e.g.
TeVeS) not attempted here (§6 item 4).

---

## 5. Consequences and Checks

### 5.1 LLR safety — checked exactly, by construction

Round-trip ranging time in coordinate time is $\Delta t_\text{coord}=2r/c(t)$. With
$r\propto c^{-3/2}$ (§3.2) and the atomic clock ticking at $\nu\propto c^{5/2}$ (§3.1):
$$\Delta t_\text{coord}\propto c^{-3/2-1}=c^{-5/2},\qquad \Delta\tau=\nu\,\Delta t_\text{coord}\propto c^{5/2}\cdot c^{-5/2}=c^0=\text{const}.$$
The number of clock ticks recorded for a round trip does not depend on $c(t)$ at all,
hence a data-reduction pipeline assuming constant $c,\nu$ infers a constant range:
$$\frac{\dot r_\text{LLR}}{r_\text{LLR}} = 0,\qquad\text{exactly, at every epoch.}$$
This is not a fitted cancellation checked once at today's epoch — the exponents cancel
identically, for the same reason at any $t$. (An earlier attempt found a family of
$(g,s)$ pairs achieving this only approximately, pinned to a thin numerical sliver by the
separately tight $\dot G/G$ bound; adopting $g=0,s=+1/2$ as exact premises removes the
approximation entirely, at the cost of no longer deriving these values — see §6 item 1.)

### 5.2 Cosmological quantities, recomputed for §2.2's rebuilt closure

Lookback time $w$ and redshift are related by matching §2.2's $c(w)=c_0(1+w/\tau)^{-4}$
against §3.3's $c_z=c_0(1+z)^{-2/5}$: $w(z)=\tau\left[(1+z)^{1/10}-1\right]$. The particle
distance, using $R_h(t_0-w)=R_{h,0}(1+w/\tau)^{-3}$ (from $R_h\propto c^{3/4}$, §2.2):
$$D_p(z) = R_{h,0}\left[1-(1+z)^{-3/10}\right],\qquad D_p(\infty)=R_{h,0}=\frac{\tau c_0}{3}.$$

**The low-$z$/today's-rate relations are unchanged from the earlier, simpler closure —
this is worth stating plainly, since it is not obvious in advance.** $H_0^\text{hor}
\equiv(\dot c/c)|_{t_0}=4/\tau$ (§2.2); the low-$z$ expansion of $D_p(z)$ above gives
$H_0^\text{obs}=10/\tau=\frac52H_0^\text{hor}$ — the *same* ratio ($n=5/2$) as under the
simpler exponential closure, because this ratio is fixed by the redshift exponent alone,
a purely local, today's-epoch statement, not by the global history of $c(t)$. With
$H_0^\text{obs}=70$ km/s/Mpc, $H_0^\text{hor}\approx2.86\times10^{-11}\,\text{yr}^{-1}$
and $\tau=10/H_0^\text{obs}\approx1.40\times10^{11}$ yr — **unchanged numerically** from
the value used before this closure was rebuilt.

**What does change is anything integrated over the full cosmological history.** The
proper age:
$$\tau_\infty=\int_0^\infty\left(1+\frac w\tau\right)^{-10}dw = \frac\tau9 = \frac{10}{9H_0^\text{obs}}\approx15.5\ \text{Gyr},$$
about 11% larger than the $\approx13.97$ Gyr found under the simpler closure — the
$\tau_\infty=1/H_0^\text{obs}$ identity there was itself a special feature of the pure
exponential, not a general result, and does not survive here. The particle horizon
$$D_p(\infty)=R_{h,0}=\frac{\tau c_0}{3}=\frac{10}{3}\cdot\frac{c_0}{H_0^\text{obs}}\approx14.3\ \text{Gpc},$$
larger than the earlier closure's $\approx10.7$ Gpc.

Higher-order cosmographic quantities (the deceleration parameter, the luminosity-distance
relation) are not yet derived — they require a flux/luminosity treatment not yet built
for this framework (§6 item 2), and would need to be built against *this* closure, not
the earlier, simpler one.

### 5.3 The acceleration scale, numerically — robust to the closure rebuild

$a_0\equiv\lambda c_0H_0^\text{hor}$ depends only on $H_0^\text{hor}$'s value *today*,
which §5.2 just showed is unchanged by rebuilding §2.2's closure. So
$a_0\approx(3\times10^8\,\text{m/s})\times(9.08\times10^{-19}\,\text{s}^{-1})
\approx2.7\times10^{-10}\,\text{m/s}^2$ for $\lambda=1$ stands as before, versus the
empirically fitted MOND value $a_0\approx1.2\times10^{-10}\,\text{m/s}^2$ — the same
factor $\approx2.3$ tension. $\lambda\approx0.44$ would match exactly, but nothing here
derives that value; it is a fitted number, flagged as such (§6 item 1). This specific
tension (the right order of magnitude for $a_0\sim cH_0$, without an exact, derived
prefactor) is a long-standing feature of this line of research, not new to this
document.

### 5.4 A testable directional prediction

Since $r\propto c^{-3/2}$ and $c(t)$ increases with cosmic time, orbital separations and
atomic radii were *larger* in the past and have been shrinking together, in lockstep,
ever since — not merely today, at every epoch. This is a genuine consequence of §3, not
yet checked against any specific dataset (§6 item 8).

---

## 6. Status and Open Items, In Priority

1. **Derive, rather than adopt, premise 3's universal scaling law and premise 4's
   $\lambda$.** A first attempt (§3.4, `ResearchNotes.md` §6) did not find a derivation
   of $s=+\frac12$ itself, but resolved a prior ambiguity: "mass neither created nor
   destroyed" (§2.1) is now read as particle-number conservation, with §2.2's
   cosmological closure rebuilt accordingly (finite future coordinate-time singularity,
   infinite proper time to reach it — not physically reached). That choice is
   independently motivated (the more literal reading) but not forced — the alternative
   (flat mass density, particle count silently falling) was not disproven, only judged
   less natural. The debt is now specifically: derive $s=+\frac12$ given
   number-conservation, and derive $\lambda$.
2. **Build the flux/luminosity sector** needed to derive the deceleration parameter,
   luminosity distance, and other higher-order cosmographic quantities — against §2.2's
   rebuilt closure, not the earlier simpler one.
3. **Fix the interpolating function $\mu(x)$'s specific form** and check it against the
   observed radial acceleration relation, not just its two asymptotic limits.
4. **Relativistic completion.** This framework currently makes no relativistic-level
   predictions (light bending, PPN parameters, perihelion advance) at all — a real
   scope reduction from an earlier iteration, not yet addressed.
5. **Justify or replace the homogeneity assumption** (§2.1: particle number density $n$
   constant, not mass density $\rho$) — restated to match §2.1's current reading, still
   an assumption either way.
6. Fix the interpolating function's specific form (duplicate of item 3 at the level of
   choosing a specific $\mu$, e.g. matching Milgrom's simple or standard forms) —
   retained as a separate line item since fixing the functional *family* and fixing its
   *free parameters* against data are different tasks.
7. **Resolve the tension between premise 3's universal mass scaling and the auxiliary
   electromagnetic-sector assumption** ($\epsilon_0\propto c^{-1}$, a different power of
   $c$) — "all local physics scales the same way" is not yet actually true across both
   sectors as stated, and this needs either a principled reconciliation or an honest
   restriction of scope.
8. Check the directional prediction of §5.4 (orbits and atomic radii shrinking together
   over cosmic time) against any dataset sensitive to it.

[^1]: J. D. Bekenstein and M. Milgrom, "Does the missing mass problem signal the breakdown
of Newtonian gravity?" *Astrophysical Journal* 286, 7–14 (1984). AQUAL's modified Poisson
equation is public, well-established physics; no reproduction concern applies here the
way it did for the scanned Atkinson (1963) source used in an earlier iteration.
