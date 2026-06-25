# Static Machian VSL Cosmology — Open Problems

*Companion to Core_Principles.md. Each entry is self-contained: it states what the
prior session claimed, identifies exactly where the reasoning broke, and sketches
what a clean resolution must supply. An entry can be handed to a fresh working
session in isolation, together with the core document, without needing the others.*

*Priority ordering is rough. OP-1 is now **resolved** (see below). OP-3 is the
recommended next target: it gates OP-2 entirely and shares its central
$GM = \text{const}$ question with the others. OP-4 is independent.*

---

## OP-1 — Time frames and the age of the universe — **RESOLVED**

*Status: resolved. The two time frames are now rigorously separated, the horizon
ODE is solved correctly, and the proper age is finite and calculable. The
resolution kills the prior "infinitely stretched past" claim but reopens the
stellar-age question as a genuine quantitative constraint (see the flag at the
end).*

### The two time frames

The model has two clocks, and the prior session conflated them.

- **Coordinate (map) time** $t$. This is the GPS-style time of the static map: a
  real "now" that all observers can agree on via a shared time standard, with
  distant galaxies fixed in place (bar true proper motion, which is separately
  measurable against the CMB rest frame). The horizon law lives here:
  $dR/dt = c(t)$.
- **Proper atomic time** $\tau$. This is what a physical clock counts, defined by
  atomic frequency. Because $\nu \propto c^{3}$ (derived below), the atomic tick
  rate relative to map time is
  $$\frac{d\tau}{dt} = \left(\frac{c(t)}{c_\text{now}}\right)^{3}.$$
  Clocks ran *slower* in the past (lower $c$), so they accumulated *fewer* atomic
  seconds per unit map time. There are no stable clocks and no rigid rods, but
  everything is calculable in a homogeneous universe via the CMB thermometer: an
  observer measures $T_\text{CMB}$, infers $c_\text{emit}/c_\text{now}$, and thereby
  fixes their position in cosmic history.

### Correct solution of the horizon ODE

Solving $dR/dt = kR^{3}$ exactly (let $u = t_\text{now} - t \ge 0$ be coordinate
lookback):
$$R^{-2}(u) = R_0^{-2} + 2k\,u,
\qquad
c(u) = \frac{c_0}{\left(1 + 2kR_0^{2}\,u\right)^{3/2}},
\qquad
H(u) = \frac{\dot c}{c} = \frac{H_0}{1 + 2kR_0^{2}\,u},$$
with $H_0 = 3kR_0^{2}$.

**Two structural facts follow immediately:**

1. **There is no finite origin in coordinate time.** $c \to 0$ only as
   $u \to \infty$. Run backward, $R \to 0$ is reached only infinitely far in the
   past. The model has *no Big Bang in map time* — only an asymptotic approach to
   $c = 0$. The prior session's "$c \propto t^{-3/2}$ with a singular start at
   $t=0$" had the sign wrong and invented a singularity the ODE does not have.

2. **"$t_0 = 3/(2H_0)$" is not an age.** It is the characteristic horizon timescale
   $1/(2kR_0^{2})$. Since the coordinate past is infinite, it cannot be an age. The
   label "metric age" must be struck wherever it appears (core doc and prior
   summary). Call it the **horizon timescale** and nothing more.

Note that $H$ is strongly time-dependent — it was far larger in the past and
asymptotes to its present value $H_0$. Expressing results in units of $1/H_0$ is
legitimate because $H_0$ is a single fixed number (the present value); the full
variation of $H(u)$ across history is carried inside $c(u)$, which is what gets
integrated. No time-varying quantity is ever pulled outside an integral.

### The frequency power: $\nu \propto c^{3}$

Built from the Rydberg energy $\nu = E_\text{Ryd}/h$,
$E_\text{Ryd} = m_e e^{4}/(8\epsilon_0^{2}h^{2})$, under the premises:
$e, h$ invariant (premise 4); $m_e \propto c$ (premise 3); and symmetric PV scaling
$\epsilon_0 \propto K \propto c^{-1}$, so $1/\epsilon_0^{2} \propto c^{2}$. Hence
$$\nu \propto m_e \cdot \epsilon_0^{-2} \propto c \cdot c^{2} = c^{3}.$$
Confirmed three ways: directly; via rest energy $E_\text{rest} = m_e c^{2} \propto c^{3}$;
and via $E_\text{Ryd} = \tfrac12 \alpha^{2} m_e c^{2} \propto c^{3}$ with $\alpha$
classically invariant. The prior session's $\nu \propto c^{1}$ was wrong — it
omitted the $\epsilon_0$ scaling and the $c^{2}$ in the rest energy.

**Caveat (stated, not buried):** $\epsilon_0 \propto c^{-1}$ rests on the
*symmetric* PV split $\epsilon_0, \mu_0 \propto K$. This is a choice in Puthoff's
framework, but it is the same choice that makes $\alpha$ classically invariant, so
the two are linked. An asymmetric convention would shift the power and the
coefficient below.

### The proper age (finite, convergent)

The total proper atomic time elapsed since $c = 0$ ($u: 0 \to \infty$):
$$\tau_\text{total} = \int_0^{\infty}\left(\frac{c(u)}{c_0}\right)^{3} du
= \frac{1}{7kR_0^{2}} = \frac{3}{7H_0}.$$
The integral **converges** because the integrand falls as $(1 + \dots)^{-9/2}$ — the
deep past contributes almost nothing in proper time, precisely because clocks
freeze as $c \to 0$. The general result for $\nu \propto c^{p}$ is
$\tau_\text{total} = \frac{3}{(3p-2)H_0}$:
$p=1 \to 3/H_0$, $p=2 \to 3/(4H_0)$, $p=3 \to 3/(7H_0)$.

Numerically, with $H_0 = 70$ km/s/Mpc ($1/H_0 \approx 13.97$ Gyr, present-epoch
seconds):
$$\tau_\text{total} = \frac{3}{7H_0} \approx 0.43\,H_0^{-1} \approx 6.0\ \text{billion atomic years.}$$
This is *lived* atomic time measured in today's seconds — the meaningful "age."

### What this overturns from the prior session

- "Infinitely stretched past" → **false**. The proper past is *compressed*, not
  stretched; it is finite (~6 Gyr).
- "$t_0 = 3/(2H_0) \approx 21$ Gyr metric age" → **not an age**; it is the horizon
  timescale. The coordinate past is infinite.
- "$t_0 = 1/(3H_0) \approx 4.6$ Gyr" → **struck as an error** (no valid derivation
  ever existed).
- $\nu \propto c$ → corrected to $\nu \propto c^{3}$.

### New flag (hand to a future session)

The ~6 Gyr proper age **reopens the stellar-age question as a real constraint.**
It comfortably fits the Sun (4.6 Gyr) but is short for the oldest observed stars
(~13 Gyr) and the full sequence of stellar generations. Because the proper-time
integrand is dominated by the recent, high-$c$ era, high-redshift stellar
populations occupy a thin proper-time slice. Whether this is fatal depends on what
proper age an observer would *locally infer* for a high-$z$ population using
epoch-dependent atomic physics — this has not been worked and is the natural
next sub-problem. It is no longer a free win; it is a constraint the model must
answer.

---

## OP-2 — The MOND acceleration constant and the factor of $2\pi$

**The honest intermediate result.** From the time-gradient mechanism (OP-3), the
flat-curve velocity floor takes the form $v_\text{edge}^4 = G^2 M^2 H_0^2 / c^2$.
Matching the Baryonic Tully-Fisher relation $v_\text{edge}^4 = G M a_0$ gives
$$a_0 = \frac{G M H_0^2}{c^2}.$$
Promoting $M$ to a cosmic mass via the Hubble-sphere relation
$M_\text{univ} = \tfrac12 c^3/(G H_0)$ (this part is a clean, correct calculation —
volume $\times$ critical density, with $\pi$ genuinely cancelling) leaves
$$a_0 \sim c H_0.$$

**The numbers.**
- $a_0 = cH_0 \approx 6.8\times10^{-10}\ \text{m/s}^2$.
- $a_0 = cH_0/2 \approx 3.4\times10^{-10}\ \text{m/s}^2$.
- $a_0 = cH_0/(2\pi) \approx 1.08\times10^{-10}\ \text{m/s}^2$.
- Observed MOND $a_0 \approx 1.2\times10^{-10}\ \text{m/s}^2$.

**Where it broke.** The $cH_0/(2\pi)$ form matches observation to ~90%, but the
$2\pi$ was *reverse-engineered*. Prompt 7d's rigorous mass calculation produces a
factor of $\tfrac12$, giving $a_0 = cH_0/2$ — which is the defensible result. The
extra $1/\pi$ was then introduced by appeal to "angular integration of retarded
potentials across a full $2\pi$ rotation," with no integration actually performed.
The agreement is curve-fitting to a known answer.

**What a resolution must supply.**
1. Treat $a_0 \approx cH_0$ as the model's honest order-of-magnitude prediction.
   This is a real and known numerical coincidence in cosmology (the observed $a_0$
   sits within a factor of $\sim 2\pi$ of $cH_0$); the model reproducing it at all
   is mildly interesting and should be stated *without* inflated precision.
2. If a factor is to be claimed, derive it. Either:
   (a) show the $\tfrac12$ from the mass relation is the correct and final
       coefficient, and accept the ~2.8× miss; or
   (b) actually perform the retarded-potential disc integration and show what
       geometric factor genuinely falls out. Do not assert $2\pi$ in advance.
3. Note that $a_0$ depends entirely on OP-3 being valid. If the rotation-curve
   mechanism fails, this entry is moot.

---

## OP-3 — The rotation-curve / retarded-potential mechanism

**The claim.** Flat galaxy rotation curves arise with no dark matter, because the
finite speed of gravity means an orbiting star feels the galaxy's interior mass as
it was at an earlier (lighter, since $M \propto c$) epoch. The radius-dependent
apparent mass produces a velocity floor
$$v_\text{edge} = \left(\frac{G M_\text{core} H_0}{c}\right)^{1/4} = \text{const}.$$

**Where it broke — twice.**

*First geometry (Prompts 1-summary, 7b).* Framed the effect as Earth viewing a
tilted galaxy front-to-back, with near edge heavier than far edge. The user
correctly objected (7e): the maximum Doppler signal is on the *major axis*, where
rotational velocity is along the line of sight; the near/far edges lie on the
*minor axis* and carry zero rotational Doppler shift. The front-to-back framing
cannot explain the velocity measured on the major axis.

*Second geometry (Prompt 7e).* Re-framed as the *star itself* looking back in time
at its own galactic core. This produces
$$v^2 = \frac{G M_\text{core today}}{r} - \frac{G M_\text{core today} H_0}{c},$$
i.e. the cosmic term enters with a **minus** sign, giving an imaginary velocity at
large $r$. The fix offered was that $G$ was larger in the past
($G \propto 1/c$), and the retarded $G$ flips the sign back to positive. This sign
flip was asserted, not computed. The derivation ends unresolved.

**What a resolution must supply.**
1. Pick one well-defined frame — almost certainly the star's local frame — and set
   up the retarded gravitational potential honestly, including *both* the retarded
   $M(t_\text{ret})$ and the retarded $G(t_\text{ret})$, since the model makes both
   time-dependent.
2. Carry the signs through symbolically. The central question is whether
   $\frac{d}{dt}[G(t)M(t)]$ along the backward light cone produces a net positive,
   $r$-independent additive term in $v^2$. With $G \propto c^{-1}$ and
   $M \propto c$, the product $GM$ is *constant in time* — which on its face means
   the leading retardation correction to $GM$ vanishes, and the whole mechanism may
   collapse. This is the crux and must be checked first, before any $a_0$ matching.
3. If $GM = \text{const}$ kills the first-order effect, identify whether any
   second-order or gradient term survives, or concede that the Machian coupling
   (which so elegantly stabilizes orbits in the core) simultaneously removes the
   dark-matter mechanism. These may be the same cancellation viewed twice.

**Flag.** OP-3 and the core orbital-lock result may be in tension. The orbital lock
works *because* $GM$ is time-independent. The rotation-curve mechanism needs $GM$
(or its retarded value) to vary with lookback time. Both cannot hold in their
current form. Resolving this tension is the single most important task in the model.

---

## OP-4 — Fine-structure constant drift $\dot\alpha$

**The setup (clean).** The classical $\alpha = e^2/(4\pi\epsilon_0\hbar c)$ is
invariant under the PV scaling $\epsilon_0 \to \epsilon_0 K$, $c \to c_0/K$: the
$K$'s cancel exactly, so $\dot\alpha = 0$ at the classical level. This part is
correct and not in dispute.

**The question (legitimate and sharp).** Does the first-order QED vacuum-
polarization correction — the running of the effective charge via virtual
electron-positron loops (Uehling) — survive the cancellation? The loop correction
depends on the electron Compton wavelength $\bar\lambda_e = \hbar/(m_e c)$, and
with $m_e \propto c$ this gives $\bar\lambda_e \propto c^{-2}$, which is *not*
scale-invariant. So a residual drift is plausible.

**Where it broke — repeatedly.** Three failed attempts:
1. *Multiplicative (Prompt 8d):* applied the rate $\dot\alpha/\alpha = \alpha_0 H_0$
   to the *whole* of $\alpha_0$, giving a cumulative ~4375 ppm to $z=1.15$. Wrong:
   treated the perturbation as if it scaled the entire constant.
2. *Additive, first try (8e):* wrote $\dot\alpha_\text{loop} = -\tfrac{4\alpha_0^2}{3\pi}H_0$,
   then divided by $\alpha_0$ and still got a factor $\alpha_0$ in the fractional
   drift (~1858 ppm). The user objected (8f): if $\alpha_\text{eff} = \text{const} +
   \text{perturbation}$, the fractional change cannot come out proportional to
   $\alpha_0$ that way.
3. *Additive, second try (8f):* conceded the error, then hand-waved that the drift
   "collapses to safely below the 1.3 ppm ESPRESSO floor" — with an unfounded
   "assume the perturbation changes by 10%" placeholder. No actual number.

**Observational target (current, worth confirming live when this is taken up).**
Modern null results are the constraint to beat:
- ESPRESSO laser-frequency-comb, HE 0515−4414 ($z=1.15$):
  $\Delta\alpha/\alpha = 1.3 \pm 1.3\ \text{(stat)} \pm 0.4\ \text{(sys)}$ ppm.
- JWST emission-line galaxies to high $z$: consistent with zero at the
  $10^{-4}$ level.
The earlier Webb/Murphy Keck/VLT "dipole" ($\sim$few ppm, $4.2\sigma$) is now
generally attributed to wavelength-calibration systematics.

**What a resolution must supply.**
1. Write $\alpha_\text{eff}(t) = \alpha_\text{bare} + \delta\alpha_\text{loop}(t)$
   with $\alpha_\text{bare}$ strictly constant. Then
   $\Delta\alpha/\alpha = \Delta(\delta\alpha_\text{loop})/\alpha_\text{bare}$ —
   the drift is the *change in the loop term only*, divided by the full constant.
2. Compute $\delta\alpha_\text{loop}$ from the Uehling correction at the atomic
   scale, with its explicit dependence on $\bar\lambda_e(t) \propto c^{-2}$.
   The correction enters through a *logarithm* of a scale ratio, so its time
   derivative depends on $\dot{(\ln c)} = H_0$ but the absolute magnitude is set by
   the QED coefficient $\sim \alpha_0^2/3\pi$, not $\alpha_0$.
3. Integrate to $z = 1.15$ and compare against 1.3 ppm. Get an actual number.
   The honest expected magnitude is small but must be *shown* to be small, since
   the logarithm is integrated over a large lookback time.
4. If it does exceed the bound, the proposed escape (a running bare charge
   $e^2 \propto K^{-1/2}$ that cancels the loop) needs to be checked for
   consistency with Maxwell / charge quantization (premise 4) — it likely conflicts
   with the invariance of $e$, so this may not be a free move.

---

## OP-5 — What sources $c$: volume law vs. surface (horizon-shell) law

*Status: open, foundational. This entry concerns the underived first principle
behind premises 2 and 3. The current core law $c \propto N \propto R^3$ is retained
as the working baseline; this entry documents a physically better-motivated
alternative and a third self-consistent variant that, strikingly, restores a finite
coordinate-time origin.*

### Motivation (not arbitrary)

Premises 2–3 ($c \propto N$, $M \propto N$) are posited, not derived. The physical
intuition: the polarizable vacuum is driven by quantum pair creation/annihilation
permitted by the uncertainty principle, but *nothing in standard physics fixes the
rate* of that pair generation — it is an observed value, numerically tied to the
local $c$. A pilot-wave picture (waves exploring all connections between every
particle and every point) motivates a dependence on the particle content of the
causal horizon. The open question is **which particles contribute**: the entire
enclosed bulk, or only those on the horizon boundary.

This matters because a boundary (surface-area) law connects naturally to
holographic / entropic-gravity reasoning (degrees of freedom $\propto$ area, not
volume), which would give the model a far stronger first-principles footing than
"every enclosed particle contributes equally."

### Three variants

Let the horizon shell at radius $R$ have thickness $\Delta R$ and particle count
$N_\text{shell} \propto R^2 \Delta R$. The scaling of $c$ depends entirely on
$\Delta R$:

| Variant | Thickness $\Delta R$ | Law | $H_0$ | Coordinate origin | Proper age ($\nu\propto c^3$) |
|---|---|---|---|---|---|
| **V (volume)** — current core | bulk count $\propto R^3$ | $c \propto R^3$ | $3kR_0^2$ | infinite past | $\tfrac{3}{7}H_0^{-1} \approx 6.0$ Gyr |
| **S (surface, fixed)** | constant length | $c \propto R^2$ | $2kR_0$ | infinite past | $\tfrac{2}{5}H_0^{-1} \approx 5.6$ Gyr |
| **S′ (surface, Compton)** | $\lambda_C = \hbar/(mc) \propto c^{-2}$ | $c \propto R^{2/3}$ | $\tfrac{2k}{3}R_0^{-1/3}$ | **finite!** | $\tfrac{2}{7}H_0^{-1} \approx 4.0$ Gyr |

### What each variant does

**S (fixed thickness).** If $\Delta R$ is a fixed physical length, $N_\text{shell}
\propto R^2$ gives $c \propto R^2$. Horizon solution
$c(u)/c_0 = (1 + kR_0 u)^{-2}$, with $H_0 = 2kR_0$. Still beginningless in
coordinate time ($c\to0$ only as $u\to\infty$). Proper age $\tfrac{2}{5}H_0^{-1}$ —
essentially unchanged from V. **Conclusion: the surface law alone does NOT rescue
the stellar-age tension.** Both V and S give ~6 Gyr because the proper age is
dominated by the recent high-$c$ era regardless of the bulk exponent.

**S′ (self-consistent Compton thickness).** The pilot-wave-natural choice is
$\Delta R = \lambda_C$, the Compton wavelength of the horizon particles. But in this
model $\lambda_C = \hbar/(mc)$ with $\hbar$ invariant and $m \propto c$, so
$\lambda_C \propto c^{-2}$ — the thickness is *itself $c$-dependent*. Self-consistency
then requires
$$c \propto R^2 \Delta R \propto R^2 c^{-2} \;\Rightarrow\; c^3 \propto R^2
\;\Rightarrow\; c \propto R^{2/3}.$$
This is qualitatively different from both others:
$$R^{1/3}(u) = R_0^{1/3} - \tfrac{k}{3}u
\;\Rightarrow\; R \to 0 \text{ at } u_\text{origin} = \frac{3R_0^{1/3}}{k}
= \frac{2}{H_0}\ \text{(finite!)}.$$
**S′ has a genuine finite coordinate-time origin — a real Big Bang at coordinate
age $2/H_0$.** Proper age $\tfrac{2}{7}H_0^{-1} \approx 4.0$ Gyr. This is the only
variant in which "the age of the universe" is a finite number in *both* time frames.

### Why this is worth pursuing

- S′ removes the conceptually awkward beginningless coordinate past of V and S, at
  no extra cost — the finite origin falls out of a *more* physically motivated
  thickness choice, not a less one.
- The exponent $c \propto R^{2/3}$ propagates into **every** downstream result:
  redshift-distance ($D_{z=1}$ changes), the $H$–$R$ relation, the $a_0$ derivation
  (OP-2), and the proper-age integral. None of these have been recomputed for S or
  S′ beyond the ages above.
- S′ still gives a short proper age (~4 Gyr), so the stellar-age constraint
  (OP-1 flag) **persists or worsens** across all three variants. This strongly
  suggests the stellar-age issue is structural to $c\propto R^n$ with $n>0$, not an
  artifact of the volume law, and must be addressed on its own terms (e.g. via
  locally-inferred ages) rather than by tuning $n$.

### What a resolution must supply

1. A principled reason to choose the contributing set (bulk vs. boundary) — ideally
   the pilot-wave argument made quantitative, or a holographic-bound justification
   for the surface law.
2. If S′ is adopted: recompute $D_{z=1}$, the distance ladder, OP-2's $a_0$, and the
   OP-1 proper age under $c\propto R^{2/3}$. The finite origin may change the
   character of the redshift-distance relation noticeably.
3. Resolve whether the Compton-thickness feedback ($\lambda_C \propto c^{-2}$) is
   the right self-consistency condition, or whether a different invariant length
   (Planck length, fixed comoving scale) is more defensible — each gives a different
   exponent.

**Decision recorded:** core stays on **V** ($c\propto R^3$) for now; **S′** is the
leading alternative and the most interesting, because of the finite origin. Promote
S′ to core only after its downstream results (point 2) are worked and checked.

---

## OP-6 — Primordial matter genesis and the self-bootstrapping origin

*Status: open, speculative, but with a real logical spine. This entry depends on
variant S′ of OP-5 ($c \propto R^{2/3}$, with finite coordinate origin), where the
Compton wavelength diverges at $t=0$. It proposes that the model's posited Machian
premise ($c \propto N$) is not an external assumption but the fixed point of a
self-consistent matter-creation process. Several pieces are conjectural and flagged
as such; the matter/antimatter asymmetry is unsolved.*

### The early-time regime (established)

In S′, $c \propto R^{2/3}$ and $\lambda_C = \hbar/(mc) \propto c^{-2} \propto
R^{-4/3}$. Relative to the horizon, $\lambda_C/R \propto R^{-7/3}$, which **diverges
as $R \to 0$.** So at the earliest epochs every particle is delocalized over a
region larger than the entire causal universe. Localization does not exist; the
early universe is a single coherent quantum object. (This is also the ideal regime
for the pilot-wave framing: the guiding wave genuinely spans everything.)

Two further scalings, established by direct computation:
- **Pair lifetime diverges.** Pair rest energy $E \sim mc^2 \propto c^3$, so the
  time–energy uncertainty bound permits a lifetime $\Delta t \sim \hbar/E \propto
  c^{-3} \to \infty$ as $c \to 0$. Pairs created at the origin need never annihilate;
  matter creation is effectively free and permanent.
- **Schwarzschild radius tracks the Compton wavelength.** $r_s = 2GM/c^2$ with
  $G \propto c^{-1}$, $M \propto c$ gives $r_s \propto c^{-2}$ — *identical scaling
  to* $\lambda_C$. Hence $r_s/\lambda_C$ is **constant in time**: the
  quantum/black-hole boundary is epoch-invariant. In S′, $r_s/R \propto R^{-7/3}$,
  so a fixed object's Schwarzschild radius also exceeds the horizon at early times,
  in lockstep with its Compton wavelength.

### The self-bootstrapping loop (proposed mechanism)

The vacuum pair-creation rate is governed by the vacuum polarizability, i.e. by $c$.
But created matter adds to $N$, and $c \propto N$. This closes a loop:

> low $c$ → cheap, long-lived pairs → $N$ grows → $c$ rises → pairs become
> expensive and short-lived → creation shuts off.

The mechanism that *defines* $c$ is the same one that *populates* the universe with
the particles whose count defines $c$. On this reading the Machian premise stops
being posited and becomes the self-consistent fixed point of a genesis process: the
universe starts at $N \approx 0$, $c \approx 0$ and drives itself upward until rising
mass-energy chokes the process off.

### $c$ as a relational quantity (intended interpretation)

The intended reading (recorded per author): **$c$ is relational/emergent, not a
background property.** An empty universe is inherently unstable (the uncertainty
principle mandates fluctuation). The first pair created has infinite $\lambda_C$:
it has no location and exists everywhere on the map at once. One particle cannot
define $c$ — there are no relations, hence no directions or distances. As $N$ grows,
inter-particle relations make directions and distances definable, and the number of
distinguishable wavelengths that fit within a given map radius — the *resolution* —
becomes finite and grows. **$c$ is that resolution.** The rise of $c$ and the
acquisition of definable geometry are the same process. Space and $c$ are
constituted by the relations among particles, not a pre-existing stage on which
particles appear.

### The PBH cutoff (proposed resolution)

*Question this resolves:* with unbounded borrowable mass and unbounded lifetime,
what prevents the early universe from collapsing entirely into primordial black
holes at every scale?

*Proposed resolution (recorded per author):* localization — and therefore black-hole
formation — is **forbidden while $r_s$ or $\lambda_C$ exceeds the horizon $R$.** A
fluctuation cannot be a black hole relative to an "outside" that does not causally
exist, and cannot localize at all while delocalized over super-horizon scales.
Therefore the earliest era necessarily produces a **delocalized coherent sea**, not
localized objects. PBH formation (and localization generally) switches on only once
$R$ has grown enough that $R > r_s$ for the relevant mass scale. This protects the
"uniform static particle sea" premise at the earliest times and makes PBHs a
*deferred, optional channel* rather than an early-universe runaway.

This reframes "borrowing mass" precisely: you may borrow unlimited mass, but you
cannot *localize* it into a black hole until the horizon outgrows the Schwarzschild
radius.

### Nucleosynthesis (expected normal, pending one check)

Argument (author): BBN depends only on the local thermodynamic sequence —
matter/radiation equilibrium while $kT$ exceeds particle rest energies, then
freeze-out as rest energies climb past the background, then fusion of free protons
and neutrons. This sequence is governed by local nuclear physics, which the model's
invariances ($\alpha$ constant, charge quantized, cross-section ratios preserved)
protect. So BBN should proceed as in the standard hot Big Bang **in proper time and
local energy units**.

**Logged check (the one place the cosmology leaks in):** standard BBN fixes the
helium fraction via the neutron–proton freeze-out, a race between the weak rate and
the cosmological *timer*. In ΛCDM that timer is the expansion rate $H$. Here the
analogue is $\dot c/c$, but **substituting $\dot c/c$ for $H$ in the BBN rate
equations may smuggle in assumptions** — the concept of "expansion rate" may not map
cleanly onto this model. $\dot c/c$ is well defined; its role as a freeze-out timer
is not yet established. Resolve before claiming BBN abundances match. (Logged for
later, low urgency.)

### The central unsolved problem: matter/antimatter asymmetry

Pair creation makes equal matter and antimatter. Individual pair *permanence* (long
$\Delta t$) does not by itself yield a matter excess — partners should still
mutually annihilate. **No solution exists yet** (author and analysis agree).

One unfinished thread: the super-horizon coherence at genesis might separate pair
partners causally before they can annihilate (partners cannot find each other across
a causally disconnected coherence volume). This is a conjecture about a possible
mechanism, not a mechanism.

Parked seed for later: **how would an antimatter black hole behave in this theory?**
Given the epoch-invariant $r_s/\lambda_C$ and the $G \propto c^{-1}$, $M \propto c$
scalings, it is not obvious the matter/antimatter distinction survives at the
black-hole level — possibly relevant to the asymmetry, possibly too hard to address
now. Flagged, not pursued.

### What a resolution must supply

1. **Quantitative bootstrap closure.** The lifetime diverges, but the pair-creation
   *rate* per unit volume and available phase space also scale with $c$ and may be
   suppressed as $c \to 0$. Show that $\int(\text{rate} \times \text{lifetime})$ over
   the early epoch produces enough $N$ to bootstrap, rather than a trickle. The
   qualitative loop is sound; quantitative closure is conjectural.
2. **A cutoff on $N$ created at $t=0^+$.** The relational/PBH-cutoff picture defers
   but does not eliminate the question of how many particles emerge before rising $c$
   chokes creation. Currently unsolved (author: "handwaving, needs work").
3. **The asymmetry.** The headline open problem. Either a separation mechanism from
   super-horizon coherence, an asymmetry input, or an argument that the
   matter/antimatter distinction is not fundamental in this framework.

---

## Cross-cutting note

OP-1 (proper-time integral), OP-3 (retarded $GM$), and OP-4 (loop running) all hinge
on the same structural feature: quantities that are *constant in lockstep* under the
Machian coupling vs. quantities that vary along a *backward light cone*. The model's
elegance (orbital lock, $\alpha$ classical invariance) and its problems (vanishing
rotation-curve term, residual loop drift) are two faces of the same coupling. It may
be most efficient to resolve OP-3's $GM = \text{const}$ question first, since the
answer likely informs the others.

OP-5 (what sources $c$) and OP-6 (genesis) are a second cluster, both rooted in the
underived first principle behind premises 2–3. They are most naturally pursued
together, and only under variant S′. A notable cross-link: the epoch-invariant
$r_s/\lambda_C$ ratio (OP-6) and the Compton-thickness feedback (OP-5 S′) are the
same $c^{-2}$ scaling appearing in two places, which is mild evidence the S′ branch
is internally coherent.
