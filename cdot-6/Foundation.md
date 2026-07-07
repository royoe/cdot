# Foundation — A Static-Euclidean, Machian Framework for Variable-$c$ Dynamics

*Status: superseded (2026-07-07). §3.6 and §4 of this document found that Atkinson's
local closure cannot produce MOND-like dynamics under any combination of local and
cosmological $\psi$ tried, or under any smooth combining function at all — a general,
not merely case-specific, result. `cdot-7/Foundation.md` acts on that finding directly:
it drops Atkinson's closure for an AQUAL-spirit modified-gravity postulate, and adopts
$s=+1/2$ (universal local mass scaling) as an exact premise rather than a fitted number.
See `cdot-7/ResearchNotes.md` §1 for the full account. This document is retained
unedited below as the record of how that finding was reached.*

*Original status note: foundational, in active construction. This document states the
premises of cdot-6 and their immediately-derivable consequences only. It does not yet
contain a derivation of MOND-like dynamics, the Radial Acceleration Relation, or the
M-σ relation — those are the framework's target phenomenology, not yet reached. This
document is self-contained: it can be read, and used as task-agent input, with no
reference to any earlier iteration of this project. The path that led here — including
everything ruled out along the way — is recorded separately in `ResearchNotes.md`.*

---

## 0. Purpose and Scope

This is a minimal foundation for a physical theory in which the speed of light $c$ is
not a universal constant but a locally- and cosmologically-determined quantity, sourced
by mass in a Machian sense: the presence of mass, both nearby and across the whole
observable universe, sets the local value of $c$ that governs light propagation, particle
dynamics, and clock rates at that point. The goal is a framework capable of producing
MOND-like modified dynamics (flat rotation curves, the radial acceleration relation,
the M-σ relation) from the same variable-$c$ structure that governs cosmology, without a
separate dark-matter sector.

This document commits to only three premises (§1–§3) and derives their immediate
consequences. Where a consequence is not yet derivable — most importantly, the MOND
mechanism itself — this is stated plainly as an open problem (§5), not glossed over.

**A methodological note on scope.** This framework is built on the working assumption
that some canonical correspondence exists between an ordinary expanding, constant-$c$
description of the universe and this one — static, Euclidean, variable-$c$ — the way two
different coordinate descriptions of the same physics always correspond. That
correspondence's exact form is deliberately *not* constructed here. The point of working
out this framework's own internal consistency requirements first — what a mass, clock, or
gravitational-coupling law has to do to survive contact with local data, and what it takes
to produce MOND-like dynamics — is that whatever ingredient turns out to be *necessary*
on this side is, via the assumed correspondence, a candidate for whatever ingredient the
standard expanding-universe picture is *missing* to produce MOND without a separate
dark-matter sector. Since MOND phenomenology itself is evidence that something is
missing from that standard picture, searching for the full correspondence before knowing
what that missing ingredient looks like would be solving the easier, better-understood
side of the problem while leaving the actual target unexamined. The correspondence is
future work, contingent on this section's findings — not a prerequisite for them.

---

## 1. Premise 1 — The Geometric Arena: Static Euclidean Space, Independent Time

Space is flat, three-dimensional, and Euclidean. Time $t$ is an independent variable,
the same everywhere, not a fourth coordinate mixed with space by a metric. There is no
spacetime curvature, no metric expansion, and no scale factor $a(t)$.

This is not a claim that curved-spacetime General Relativity is wrong as a predictive
theory — the opposite: it is a claim, following a known and rigorous result (Atkinson
1963 [^1]), that every local prediction of GR for the motion of test particles and light
around a mass can be
**reproduced exactly** in a strictly Euclidean space with an independent time, provided
the *local* value of the speed of light and the *local* value of a test particle's rest
mass are allowed to depend on position, according to fixed rules (§2). Curvature is
traded for position-dependent local physics; nothing about the observable predictions
changes locally. What differs is the global picture: space itself never curves, expands,
or contracts. All of cosmology, on this premise, must be expressed as a statement about
how these local quantities change from place to place and epoch to epoch — not as a
statement about the geometry of space itself.

---

## 2. Premise 2 — The Local Machian Closure

*This entire section (§2.1–§2.3) is R. d'E. Atkinson's 1963 result [^1], for a single
static mass — stated here exactly as he derived it, not re-derived independently. The
extension to a cosmological, self-referential context (§3) is this document's own and
is not in Atkinson's paper.*

### 2.1 The scalar potential parameter

Near any concentration of mass $M$, define a dimensionless potential parameter at
distance $r$:
$$\psi \equiv \frac{GM}{2rc^2},$$
using the locally-measured (asymptotic, far-field) speed of light $c$ and Newton's
constant $G$, both treated as fixed reference values for the purpose of this section.
$\psi\to0$ as $r\to\infty$ ($c_r\to c$, the fixed reference value — not to zero: $\psi$
enters $c_r$ only through the rational function of §2.2, which is finite and equal to 1
at $\psi=0$). $\psi\to1$ at $r=GM/2c^2$ — this is the Schwarzschild horizon, but note it
is a quarter of the more commonly quoted $2GM/c^2$: that latter figure is the horizon's
location in the *Schwarzschild* coordinate $r_1$, whereas $r$ here is the *isotropic*
coordinate, related by $r_1=r(1+\psi)^2$; the two coordinates agree far from the mass but
not at the horizon itself.

### 2.2 The two closure postulates

Two rules, taken directly from Atkinson (1963, eqs. 21 and 35) [^1] — not derived from
anything more fundamental there either; he labels them *ad hoc*, adopted because they
are the unique choice that reproduces every local relativistic prediction for a single
mass at rest, checked below — fix how light speed and test-particle rest mass vary with
$\psi$:

$$\boxed{\,c_r = c\,\frac{1-\psi}{(1+\psi)^3}\,}\qquad\text{(local light speed at }r\text{)}$$

$$\boxed{\,\mu_r = \mu\,\frac{(1+\psi)^5}{1-\psi}\,}\qquad\text{(rest mass of a test particle at rest at }r\text{, given mass }\mu\text{ at }\psi=0\text{)}$$

Both $c$ and $\mu$ here are the values at $\psi=0$ (far from the mass) — reference
constants, not variable quantities in this local, single-mass, single-epoch context.

### 2.3 What follows, exactly, without approximation

Treating $c_r$ as the true local speed of light and $\mu_r$ as the true local rest mass,
and applying ordinary special-relativistic dynamics **locally** (a free particle's total
energy is $H=\mu_r c_r^2(1-v^2/c_r^2)^{-1/2}$, its momentum $\mathbf p=\mu_r\mathbf
v(1-v^2/c_r^2)^{-1/2}$, angular momentum and energy conserved along a trajectory since
nothing here breaks time-translation or rotational symmetry locally), the resulting
equations of motion for a test particle, and Snell's-law-based light bending using $c_r$
as a spherically-stratified refractive index, are **identical** — not merely
approximately, but term for term, to all orders in $\psi$ — to the geodesic equations of
Schwarzschild spacetime. This reproduces, exactly:
- Light deflection by a mass, to the full relativistic value (not just the Newtonian
  half).
- Gravitational redshift, $\nu_r/\nu=(1-\psi)/(1+\psi)$ (Atkinson eq. 17).
- Perihelion advance, to the same order every standard treatment reaches.
- The Newtonian inverse-square law as the leading term, with no separate assumption
  about the force law — it falls out of postulates about $c_r$ and $\mu_r$ alone.

**This equivalence is not adopted on faith — it is a checked mathematical fact about
these two specific functional forms**, verified by Atkinson via direct substitution into
the Lagrangian and geodesic equations [^1]. He also shows (his §3, p. 70) that other
exponents (a generalized $c_r=c(1+\psi)^j(1-\psi)^k$, $\mu_r=\mu(1+\psi)^l(1-\psi)^p$)
reduce to Newtonian gravity at leading order regardless of $j,k,l,p$ — the
inverse-square law is not sensitive to these choices — but only the specific
combination above reproduces the full relativistic corrections (light bending to the
correct coefficient, and the correct perihelion advance) as well.

### 2.4 What this section does not assume

Nothing here says how $\psi$ arises from a general mass distribution beyond the single
central mass $M$; nothing here says whether $G$ or $\mu$ (or $c$, the $\psi=0$ reference
value) themselves change with cosmic time. This section is a **local, single-epoch**
closure only. It says nothing about cosmology.

---

## 3. Premise 3 — The Cosmological Machian Closure

### 3.1 The hypothesis

The same relation that fixes light speed near a *local* mass concentration also fixes
the *background* value of $c$ that plays the role of "$c$ at $\psi=0$" in §2 — the value
every local observer would extrapolate to at large distance from any specific nearby
mass. This background value is set by the mass enclosed within the observer's own
cosmological horizon: replace the local mass $M$ and radius $r$ in §2.1's $\psi$ with the
enclosed horizon mass $M_h(t)$ and horizon radius $R_h(t)$,
$$\psi_h(t)\equiv\frac{GM_h(t)}{2R_h(t)c(t)^2}.$$
This is self-referential — $\psi_h(t)$ depends on $c(t)^2$, which will in turn need to
depend on $\psi_h(t)$ — reflecting the genuinely Machian character of the postulate: the
horizon mass and the horizon's own light speed must be mutually consistent, not fixed by
an external reference the way §2's single-mass problem was. Throughout this document,
$c_0$ denotes our own reference value (at $z=0$) and $c_z$ the corresponding value
associated with redshift $z$. There is no separate "reference speed at infinity" — every
value of $c$ in this framework belongs to some redshift $z$.

**$c_0$ and $c_z$ are not locally measured quantities — this needs to be stated
precisely, not glossed over.** Under the SI convention, the second is fixed by a cycle
count of a specific atomic transition, and the metre is defined as the distance light
travels in a fixed fraction of that second. Given that, $c$'s numerical value is a
tautology: any observer, at any epoch, who calibrates units the same way — their own
local atomic transition fixing their own second, their own local light-travel-time
fixing their own metre — gets the identical number, always. Length and time are both
built from the same local light-speed/atomic-transition physics, so no self-consistently
calibrated local observer can ever measure their own $c$ to differ from anyone else's.
**What $c_0$ and $c_z$ denote here is a cross-epoch relational quantity, not an
instrument reading** — exactly the same kind of quantity redshift $z$ itself is built
from, and for the same reason: $z$ compares a received photon's fixed, conserved
frequency against the *receiving* observer's own local reference frequency, not against
some universal standard, so two different observers intercepting the *same* photons (say,
along their path to becoming what we call the CMB) at two different epochs would infer
two different values of $z$ for them — not because the photons changed, and not because
either observer's own local $c$ reads differently on their own instruments (it never
does), but because the local reference each compares against differs. $c_z$ is
bookkeeping for exactly this cross-comparison, the same role Atkinson's own $c_r$ plays
in §2: it is not what a local observer *at* $r$ reads off their own rulers and clocks (his
own §4 is an extended treatment of exactly this difficulty) — it is the quantity that
governs what a *different*, comparing observer sees.

### 3.2 The horizon and its mass

The horizon grows at the local light speed, $\dot R_h=c(t)$ — this is what "horizon"
means in a static space with a finite, time-dependent light speed, not an additional
assumption. Equivalently, in integral form,
$$R_h(t) = \int_{-\infty}^{t} c(t')\,dt',$$
the accumulated light-travel distance since genesis, built from the *entire*
light-travel history, not "current $c$ times elapsed time." The differential and
integral forms are not two separate claims: differentiating an integral with a variable
upper limit returns the integrand there, so $\dot R_h=c(t)$ follows directly from the
integral definition, and solving the differential equation (§3.4 does this explicitly)
is mathematically identical to performing the integral. One consequence worth stating
outright: $D_p(z\to\infty)=R_h(t_0)-R_h(-\infty)=R_{h,0}$ — in this single-relation
picture, the total particle horizon and today's horizon radius are the *same*
quantity — a simplification worth keeping in mind if this relation is ever replaced
(§3.3, §5 item 2), since a more complex closure could easily make these two lengths
distinct again.

Mass is neither created nor destroyed (ordinary conservation), and space is
homogeneous (assumed, not yet derived — see §5): the enclosed mass is
$$M_h(t) = \frac{4}{3}\pi R_h(t)^3\rho,$$
with $\rho$ a genuine constant (uniform density, unchanging in time, since nothing
dilutes or concentrates it in a static, homogeneous space with conserved mass). Note
$\psi_h\propto R_h(t)^2/c(t)^2$: at genesis, $R_h\to0$, so $\psi_h\to0$ regardless of
what $c$ does there.

### 3.3 A direct substitution fails a basic consistency check — rejected

The most direct way to close §3.1 reuses §2.2's rational function unchanged, i.e. posits
$c(t)=c_\text{ref}\cdot(1-\psi_h(t))/(1+\psi_h(t))^3$ for some constant $c_\text{ref}$
(the value at $\psi_h=0$). This fails outright, by a short argument, not a numerical
subtlety: standard cosmological redshift requires $c_z\to0$ as $z\to\infty$ (genesis) —
this is the one thing already settled and not up for revision. But §3.2 shows genesis is
$\psi_h=0$, and evaluating the rational function there gives $c=c_\text{ref}\cdot1=
c_\text{ref}$ — a fixed, generically nonzero value, not zero. Requiring it to vanish
forces $c_\text{ref}=0$, which — since $c_\text{ref}$ multiplies the rational function
for *every* $t$, not just at genesis — collapses $c(t)\equiv0$ identically, for all
time. **This is a reductio, not an open item**: the genesis condition and this specific
closure cannot both hold with $c_\text{ref}\ne0$, so the direct substitution is
inconsistent and is rejected outright, independent of the further (numerical, see
`ResearchNotes.md` §4) finding that it also makes the horizon radius a non-monotonic,
bounded function of $\psi_h$.

**What must actually supply premise 3's closure, then, is not a reused copy of §2's
single-mass rational function** — some other relation between $c(t)$ and $\psi_h(t)$ is
needed, one that is well-behaved at $\psi_h=0$ (giving $c\to0$ there, not a nonzero
constant). This is restated as an open item in §5; nothing proposed there yet is more
than a placeholder.

### 3.4 A provisional working relation

Pending §3.3's resolution, a cruder version of the same Machian idea — using only the
leading Sciama-type scaling $c^2\propto GM_h/R_h$ directly, rather than Atkinson's full
rational function — gives a solvable, if less rigorously grounded, placeholder
cosmology, and it has the virtue of getting the genesis limit right by construction.
With $M_h\propto R_h^3$ (§3.2) this forces $c\propto R_h$, and with $\dot R_h=c$:
$$c(t)=c_0\,e^{H_0^\text{hor}(t-t_0)},\qquad H_0^\text{hor}\equiv\frac{c_0}{R_{h,0}}=\text{const (exactly, at all times)},$$
where $t_0,R_{h,0}$ are today's values, so $c(t_0)=c_0$ by construction. With lookback
time $u\equiv t_0-t$: $c(u)=c_0e^{-H_0^\text{hor}u}\to0$ as $u\to\infty$ — genesis is
reached only as $u\to\infty$ (coordinate time $t\to-\infty$), and $c\to0$ there smoothly,
with no separate condition needing to be imposed. Using the redshift relation for a
photon's frequency compared against a local atomic standard (not yet re-derived in this
framework from §2's own closure — imported provisionally as $1+z=(c_0/c_z)^2$, pending a
proper derivation from §2.2's $\mu_r$/atomic-scale relations) gives
$$c_z = c_0(1+z)^{-1/2},\qquad u(z)=\frac{\ln(1+z)}{2H_0^\text{hor}},$$
and a **finite** particle horizon:
$$D_p(z)=\frac{c_0}{H_0^\text{hor}}\left[1-(1+z)^{-1/2}\right],\qquad D_p(\infty)=\frac{c_0}{H_0^\text{hor}}.$$
Consequences, all straightforward to derive from this: $H_0^\text{obs}=2H_0^\text{hor}$
(low-$z$ expansion); proper age $\tau_\infty=1/H_0^\text{obs}\approx13.97$ Gyr
($H_0=70$); deceleration $q_0=+1/2$ at leading order in the luminosity distance.

**This relation is explicitly provisional** — it is offered as a placeholder that
produces a sensible, finite cosmology with the right genesis behavior while §3.3's
problem is worked out, not as a claim that it is the correct consequence of §3.1 (it
is not derived from $\psi_h$ or any rational-function closure at all — it bypasses §3.1's
closure question entirely by using only the mass-radius scaling of §3.2). It should
**not** be assumed to survive once §3.3 is resolved; whatever replaces it may give a
different redshift law, distance law, and age.

### 3.6 Local Systems Are Not Automatically Immune to Cosmological Drift

§2 treated $c$, $G$, and $\mu$ (the $\psi=0$ reference values) as fixed constants "for
the purpose of that section." This is safe as a *local* approximation only if the
cosmological evolution of $c(t)$ (§3) either does not reach local systems at all, or
reaches them too slowly to matter at the precision real measurements achieve. **Neither
has been checked yet, and this is not a formality** — a bound two-body system's orbit
and the clock used to measure it are exactly the kind of place a slow cosmological drift
would show up first, compounded over years of high-precision tracking, and this is
precisely the kind of check that has decided whether a variable-$c$ proposal survives
contact with data before.

Three questions, currently unanswered by §1–§3, gate whether §2's "fixed" language is
actually safe rather than merely convenient:

1. **Does $G$ track $c(t)$'s cosmological evolution, or is it strictly invariant?**
   Nothing here says either way. This is the single most sensitive channel: a bound
   orbit's radius, under angular-momentum conservation, depends on how $G$ (and $\mu$)
   behave together, so an undetermined $G(c)$ leaves the framework's local predictions
   undetermined too.
2. **Does the reference rest mass $\mu$ (at $\psi=0$) track $c(t)$'s cosmological
   evolution?** This is distinct from the *local*, position-dependent $\mu_r(\psi)$ of
   §2.2 (already an open, untested feature, §5) — this question is about whether the
   $\psi=0$ baseline itself drifts with cosmic time, not about position-dependence at
   fixed time.
3. **Does the *absolute*, cross-epoch atomic transition frequency depend on $c(t)$?**
   (Not "does a local clock's own tick rate drift" — per §3.1's clarification, that
   question is tautologically "no": a self-consistently-calibrated local clock always
   reads its own second as its own second. The real question is whether *two different
   locally-available clocks* — an atomic one and, say, one built from orbital dynamics,
   which depends on $G$ and $M$ rather than on atomic transitions — drift *relative to
   each other* over cosmic time. This is exactly what decided the LLR case referenced in
   `ResearchNotes.md` §6: not "does light speed read differently," but "do two
   independently-built local clocks disagree after enough time passes." Atkinson's own
   redshift result, §2.3, is about position at fixed time, not cosmic-time evolution, so
   it does not by itself answer this.)

**Why this cannot be deferred indefinitely.** If the answer to all three is "no
dependence," local systems are genuinely screened from the cosmological rate and §2's
idealization is exact, not approximate. If the answer to *any* of them is "yes," the
resulting secular drift must be computed explicitly and checked against real
high-precision bounds (laser ranging, pulsar timing, atomic clock comparisons) — not
assumed small. This is elevated to the top of §5's open items, not left as a footnote,
because getting it wrong is not a matter of imprecision — it is the kind of error that
falsifies a framework outright once checked.

**This has now been checked for one specific case, and it fails decisively.** Taking
$G$ and the reference mass $\mu$ as strictly invariant (so orbits are static,
$r_\text{EM}=$const — the answer to questions 1–2 most likely to work, by analogy) and
using the imported $\nu(t)=\nu_0(c(t)/c_0)^2$ clock relation from §3.4 (question 3, not
yet independently derived) for a two-body ranging system: the round-trip proper time
recorded is $\Delta\tau=(c(t)/c_0)^2\Delta t_\text{coord}$ with $\Delta t_\text{coord}=
2r_\text{EM}/c(t)$, and a data-reduction pipeline assuming constant $c,\nu$ infers
$r_\text{LLR}(t)=r_\text{EM}\cdot(c(t)/c_0)$, hence
$$\frac{\dot r_\text{LLR}}{r_\text{LLR}} = \frac{\dot c}{c} = H_0^\text{hor}.$$
Numerically ($H_0^\text{obs}=70$ km/s/Mpc, $r_\text{EM}\approx3.844\times10^{11}$ mm):
$\dot r_\text{LLR}\approx13.8$ mm/yr against a non-tidal bound of $<0.058$ mm/yr — a
**$\times238$ exclusion**, from the clock-rate channel alone, with $G$ and the orbit
already fixed. **Invariant $G$ is therefore necessary but not sufficient.**

**The problem is deeper than any one choice of clock or mass law — there is an
irreducible floor.** Strip the calculation to its bare minimum: invariant $G$, static
orbit, and an atomic clock rate held perfectly fixed too ($\nu=\nu_0$, no $c$-dependence
assumed at all). Even here, the round-trip light-travel time itself,
$\Delta t_\text{coord}=2r_\text{EM}/c(t)$, is genuinely different today than it was when
$r_\text{EM}$ was first calibrated, purely because $c(t)$ has changed — that is what
premise 3 asserts. Converting the resulting tick-count back into a distance with today's
fixed $c_0$ (which is what any ranging pipeline does) gives
$r_\text{LLR}(t)=r_\text{EM}\cdot(c_0/c(t))$, hence
$$\frac{\dot r_\text{LLR}}{r_\text{LLR}} = -\frac{\dot c}{c} = -H_0^\text{hor},$$
the same $\times238$-level signal, opposite sign, with *zero* assumption about how $G$,
mass, or atomic physics couple to $c(t)$. **Any scenario in which $c(t)$ genuinely,
physically differs from its value 50 years ago creates a signal at this floor,
unavoidably** — the only way to remove it is for whatever *locally* sets the
ranging-clock/light-speed relationship to track $c(t)$'s cosmological drift in exactly
the compensating way. Solving for the mass-scaling exponent that does this exactly
(holding $G$ invariant) gives a single value, $m\propto c^{+1/2}$ — mathematically real,
but the opposite sign from every physically-motivated mass law considered so far, not
implied by Atkinson's own postulates, and not motivated by anything else in this
document. Its only property is that it cancels the number; that is precisely the kind of
"selected because it works, not derived" move this framework has tried throughout to
avoid.

**This changes what §5 item 4 needs to deliver.** It is not enough for the redshift/
clock-rate derivation to avoid $\nu\propto c^2$ specifically — no candidate mechanism
tried so far survives, and the floor computed above shows the exposure is structural,
present even when every local-physics coupling is switched off. The live possibilities
are now: (a) this framework's premises are inconsistent with high-precision local
data and cannot be repaired by any choice of local mass/clock law, or (b) local systems
must be genuinely insulated from $c(t)$'s cosmological rate of change — not merely
"$G$ happens to be invariant," but the *local* value of $c$ actually used in ranging,
clocks, and orbital dynamics must not track the cosmological $c(t)$ of §3 at all, at any
order. Distinguishing these is now the framework's central open question, ahead of
everything else in §5.

---

## 4. The Target Mechanism for MOND-Like Dynamics (Conjecture, Not Yet Derived)

The framework's motivating goal is to produce a MOND-like modification to gravity at low
acceleration, without a separate closure imported from outside this document. The
natural candidate, not yet worked out in detail:

**Conjecture (original form).** A test particle at radius $r$ from a mass $M$
experiences *two* contributions to $\psi$ simultaneously — the local one,
$\psi_\text{loc}=GM/2rc^2$ (§2.1), and the cosmological background one, $\psi_h$ (§3.1),
which is present everywhere, not just near masses. Ordinary Newtonian/GR behavior (§2.3)
holds where $\psi_\text{loc}\gg\psi_h$; a qualitatively different regime should appear
where $\psi_\text{loc}\lesssim\psi_h$. This crossover condition, $GM/2rc^2\sim\psi_h$, is
dimensionally exactly the MOND transition condition — encouraging, but dimension-matching
is not derivation.

**Checked exactly, and rejected.** Atkinson's own two postulates combine into a closed
form for the rest-energy term with no approximation needed:
$$\mu_rc_r^2 = \mu_rc_r^2\Big|_{\psi} = \mu c^2\,\frac{1-\psi}{1+\psi}$$
(direct substitution of §2.2's postulates; this also reproduces §2.3's redshift factor
exactly, since $H=h\nu$ makes this the same statement). Substituting the additive
conjecture's own $\psi=\psi_\text{loc}(r)+\psi_h$, with $\psi_\text{loc}=k/r$,
$k\equiv GM/2c^2$, and taking $F=-dH_\text{rest}/dr$ as the Newtonian-level radial force
gives, exactly (not perturbatively):
$$F(r) = -\frac{GM\mu}{\big[(1+\psi_h)r+k\big]^2}.$$
At large $r$ — the regime relevant to rotation curves, where $k$ is negligible — this is
$F\propto -GM\mu/[(1+\psi_h)r]^2$: **ordinary $1/r^2$ gravity at every radius**, with only
a constant rescaling of the effective $G$ by $(1+\psi_h)^{-2}$. No transition, no
flattening, at any order. **The additive conjecture is rejected, not merely
unconfirmed** — simple addition inside Atkinson's rational structure can only shift
where a system sits on the same $1/r^2$ curve; it cannot change the curve's shape, because
$\psi_h$ only ever appears summed with $\psi_\text{loc}$, never in a form where their
*ratio* controls anything.

**A general result, not specific to the additive guess.** For *any* smooth function $f$
with $H_\text{rest}(r)=f(\psi_\text{loc}(r)+\psi_h)$, $\psi_\text{loc}=k/r$:
$$F(r) = -\frac{dH_\text{rest}}{dr} = f'(\psi_h+k/r)\cdot\frac{k}{r^2}\ \xrightarrow{r\to\infty}\ f'(\psi_h)\cdot\frac{k}{r^2}.$$
This is $1/r^2$ at large $r$ for *any* smooth $f$, not only Atkinson's specific rational
function, and regardless of whether $\psi_h$ is treated as small or order-unity: a local
mass's contribution to a summed potential always vanishes as $1/r$, and any smooth
function of a linearly-vanishing perturbation gives a quadratically-vanishing force.
**No closure of the form "$c_r,\mu_r$ depend on a single combined potential value" —
however that combination is constructed — can produce MOND.** This rules out an entire
class of fixes, not just the specific additive one.

**The likely resolution: MOND is a statement about the field, not the potential.**
Standard modified-gravity formulations modify the relation between mass density and
$|\nabla\Phi|$ (field strength/acceleration), not between mass and $\Phi$'s value.
$\psi_h$ is spatially uniform to extremely high precision at any local system's scale
(directly checked: the background contribution from a uniform density out to the
horizon varies as $r^2/R_h^2$ across a galactic-scale region, utterly negligible), so
$\nabla\psi_h\equiv0$ — it carries no spatial information a gradient-based closure could
use. What $\psi_h$ does carry is a *temporal* rate, $H_0^\text{hor}=c/R_h$ (§3.2, §3.4).
The natural division of roles: $\psi_\text{loc}$'s spatial gradient sets the local field
strength; $\psi_h$'s temporal rate sets the reference acceleration scale that field
strength is compared against — structurally the same shape as $a/a_0$ in standard MOND
formulations, but built from $\nabla\psi_\text{loc}$ and $H_0^\text{hor}$ rather than
from $\psi_\text{loc}+\psi_h$. Constructing this field-strength-based closure from
Atkinson's own postulates, and checking whether it actually interpolates, is now the
single most important open calculation in this framework, replacing both the additive
form and the ratio-of-potentials idea considered and superseded above.

---

## 5. Status and Open Items, In Priority

1. **[Gating, highest priority]** Answer §3.6's three questions — does $G$, does the
   reference mass $\mu$, or does an atomic clock's tick rate depend on the cosmological
   $c(t)$ — and if any answer is "yes," compute the resulting local secular drift and
   check it against real high-precision bounds (laser ranging, pulsar timing, atomic
   clock comparisons). This gates every other item below: nothing about §2's local
   closure can be trusted as safely "local" until this is resolved, and getting it wrong
   is the kind of error that falsifies a framework outright, not a minor correction.
   Item 5 (below) is a component of this question, restated for emphasis, not a
   separate item.
2. **[Gating]** Find the actual closure for premise 3 — a relation between $c(t)$ and
   $\psi_h(t)$ that gives $c\to0$ at genesis (§3.3 shows the direct reuse of §2's
   rational function cannot do this, and is rejected, not merely unresolved). Until this
   is found, §3.4's cosmology is a placeholder, and no claim about the framework's
   cosmological viability (age, redshift law, distance law) should be treated as
   established.
3. **[Gating for the actual goal]** Derive the combined local-plus-cosmological $\psi$
   equations of motion (§4) and check whether they produce MOND-like dynamics, the
   radial acceleration relation, or anything resembling the observed rotation-curve
   phenomenology. Nothing in this document yet demonstrates this — it is the reason the
   framework exists, and it is unproven.
4. Derive the redshift mechanism (how a photon's frequency, compared against a local
   atomic standard, behaves under this framework's own §2 closure) rather than importing
   the squared redshift law from outside this document, as §3.4 currently does. This is
   also the natural place to resolve item 1's third question (atomic clock rate vs.
   cosmological $c(t)$), since both concern how atomic/photon physics responds to $c(t)$.
5. Justify or replace the homogeneity assumption (§3.2) — is uniform density $\rho$
   actually forced by anything in §1–§2, or is it an additional, unexamined premise?
6. Determine whether $\mu$ (§2's $\psi=0$ reference rest mass) is itself fixed
   absolutely, or whether it needs a Machian/cosmological treatment — see item 1, which
   asks this same question about $\mu$ and about $G$. §2 treats $G,\mu$ as given
   constants for the local, single-mass problem; whether that is the right way to set
   up the cosmological problem too, or whether $\mu$ should itself be eliminated in
   favor of a purely relational statement (no fixed reference mass at all), is open.
7. Establish whether local (position-dependent, §2's $\mu_r$) mass variation near an
   ordinary body is empirically excluded by anything, or whether it remains a live,
   untested feature of this framework at solar-system scale. (Nothing has excluded it —
   this needs an honest confrontation with PPN/ephemeris data, not an assumption either
   way. Note this is a *different* question from item 1's: item 1 asks whether the
   $\psi=0$ baseline drifts with cosmic *time*; this item asks whether the local,
   position-dependent departure from that baseline, at fixed time, is excluded.)

---

[^1]: R. d'E. Atkinson, "General Relativity in Euclidean Terms," *Proc. Roy. Soc. Lond.
A* **272**, 60–78 (1963). Notes and equation-by-equation summary:
`references/Atkinson63.md`.
