# Static VSL Cosmology — Open Problems

*Companion to Core_Principles.md. Each entry is self-contained: it states what the
prior session claimed, identifies exactly where the reasoning broke, and sketches
what a clean resolution must supply. An entry can be handed to a fresh working
session in isolation, together with the core document, without needing the others.*

*Status overview. **Resolved:** OP-1 (time frames / age), OP-3 (rotation-curve
mechanism), OP-7 (mass-relation exponent), OP-8 (invariant-mass branch). **Refuted:**
OP-9 (conformal-projection hypothesis — the model is a genuine rival to FLRW, not a
reframing; this also explains the SN over-dimming as a real departure). **Open:**
OP-2 ($a_0$ numerical value + $2\pi$), OP-4 ($\dot\alpha$ drift), OP-5 ($c$-sourcing,
volume vs surface), OP-6 (genesis / asymmetry). **Central open problem after OP-9:**
the model is a rival theory whose distance relation conflicts with supernova data
(see OP-9 "the fork", Branch A). The model pivoted from Machian mass ($M\propto c$)
to invariant mass + $G\propto c^{-2}$; entries predating that pivot note it inline.*

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

*Update (post-OP-3 resolution):* the rotation-curve mechanism is now derived under
the invariant-mass branch, and the floor has a **derived coefficient**:
$v_\text{floor}^2 = |g|\,GMH_0/c = 2\,GMH_0/c$ for $g=-2$ (OP-3, OP-8). So the
$v_\text{edge}^4$ form below should be re-derived from this $v^2$ floor (giving
$v_\text{edge}^4 = 4G^2M^2H_0^2/c^2$, a factor 4 from the squared coefficient), and
the "implicit coefficient 1" the prior session used is superseded. The $2\pi$
question itself remains open. The historical analysis below is retained for context
but should be recomputed with the coefficient-2 floor.

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

## OP-3 — Rotation curves from retarded gravity — **largely resolved**

*Status: the mechanism now has a sound derivation under the invariant-mass branch
($s=0$, $G\propto c^{-2}$, OP-8). The flat floor emerges not from a near/far mass
bookkeeping (the prior session's fragile framing) but from a structural conversion
of the force law from $1/d^2$ to $1/d$ under retardation. One rigor gap remains: a
complete Liénard–Wiechert treatment to confirm no comparable term was dropped.*

### The correct framing (full superposition breakdown)

The Newtonian shell theorem has two parts, both relying on superposition over a
symmetric distribution: interior mass acts as if at the center, and a symmetric
exterior shell exerts zero net force. **Finite gravity speed breaks the symmetry
that *both* parts depend on** — so the exterior cancellation fails just as the
interior concentration does. The prior session only perturbed the interior mass;
the correct treatment perturbs every element, interior and exterior.

Work in the star's own frame (the correct one). Each disk element at distance $d$
from the star is felt as it was at lookback $\Delta t = d/c$. With invariant mass
($m$ fixed) and $G\propto c^{g}$, the gravitating strength of a fixed element seen
at lookback $\Delta t$ is
$$(Gm)_\text{ret} = (Gm)_0\left(1 - g\,\tfrac{\dot c}{c}\,\Delta t\right)
 = (Gm)_0\left(1 + |g|\,\tfrac{H_0}{c}\,d\right),\qquad g=-2.$$
Because $c$ was smaller in the past and $G\propto c^{-2}$, distant (earlier-epoch)
elements pull *harder* — and on the far side this does not cancel the near side.

### The key structural result: $1/d^2 \to 1/d$

Inserting this into the radial force integral:
$$F_r = \underbrace{\int (Gm)_0\,\frac{\hat d_r}{d^2}\,d^2r'}_{\text{Newtonian}}
 \;+\; |g|\frac{H_0}{c}\int (Gm)_0\,\frac{\hat d_r}{d^2}\cdot d\;d^2r'
 = F_r^\text{Newton} + |g|\frac{H_0}{c}\int (Gm)_0\,\frac{\hat d_r}{d}\,d^2r'.$$
The extra factor of $d$ turns one power of $1/d^2$ into **$1/d$**. A $1/d$ force per
unit mass is precisely the isothermal / logarithmic-potential law that produces flat
rotation curves — the same mathematics as a dark-matter halo, but sourced here by
the retardation of ordinary baryonic mass, not by invisible matter. Your objection
(the exterior breakdown) is not a problem: the $1/d$ falloff is exactly what makes
the distant exterior mass contribute the flat floor instead of cancelling.

### The floor (two independent confirmations)

*Point-mass limit (analytic).* For central mass $M$ at distance $r_0$:
$$F_\text{corr} = -|g|\frac{H_0}{c}\frac{GM}{r_0}
\;\Longrightarrow\;
v_\text{floor}^2 = -F_\text{corr}\,r_0 = |g|\,\frac{GM H_0}{c} = \frac{2GM H_0}{c}.$$
$r_0$-independent — a flat floor, coefficient $|g|=2$, matching OP-8's
$(s=0,g=-2)$ prediction.

*Extended exponential disk (numerical).* Integrating the correction force over a
razor-thin exponential disk confirms $v_\text{corr}^2$ converges to a constant at
large $r_0$ (verified to converge to a fixed value as $r_0$ runs out to $\sim$20
scale lengths), establishing the floor is not an artifact of the point-mass
idealization. The Newtonian term separately falls off as expected, so the flat
outer curve is carried entirely by the retardation term.

### Why this resolves the prior breakdowns

- The **minor/major-axis objection (7e)** is moot: this is not a line-of-sight
  Doppler/viewing effect at all. It is a dynamical force computed in the star's
  frame, independent of how Earth views the galaxy.
- The **sign problem (7e)** is resolved cleanly: with $g=-2$, distant elements pull
  harder and the correction term is unambiguously positive (outward-deepening
  potential → positive $v^2$ floor). No asserted sign-flip needed.
- The **$GM=\text{const}$ collapse** that killed the Machian version is exactly why
  Machian mass had to go: at $(s=1,g=-1)$, $g+s=0$ and the correction vanishes. The
  invariant-mass branch has $g+s=-2\neq0$, so the mechanism lives. (See OP-7/OP-8.)

### Remaining rigor gap

The retardation expansion used is the leading *source-strength* term,
$(Gm)_\text{ret}=(Gm)_0(1+|g|\tfrac{H_0}{c}d)$. A complete derivation should set up
the full retarded (Liénard–Wiechert-type) gravitational potential and confirm that
no comparable first-order term — e.g. from source velocity, or from the
time-derivative of the field itself — was dropped. The leading term is almost
certainly dominant (the others carry extra factors of $v/c$ for disk motions, which
are $\ll1$), but this has not been shown rigorously. This is the one place not to
repeat the prior session's habit of waving through a convenient term.

### What remains (handoff)

1. Liénard–Wiechert confirmation of the leading term (above).
2. The numerical $a_0$ and the factor-of-$2\pi$ question now move to OP-2, with the
   floor $v_\text{floor}^2 = 2GMH_0/c$ as the corrected starting point (coefficient
   2, not the prior session's implicit 1).
3. Recompute under $c\propto R^{2/3}$ (variant S′) if that branch is pursued; the
   $1/d\to$ flat-floor structure is generic but the coefficient may shift.

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
   drift (~1858 ppm). The user objected (8f): if
   $\alpha_\text{eff} = \text{const} + \text{perturbation}$, the fractional change
   cannot come out proportional to $\alpha_0$ that way.
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

**S (fixed thickness).** If $\Delta R$ is a fixed physical length,
$N_\text{shell} \propto R^2$ gives $c \propto R^2$. Horizon solution
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
$$c \propto R^2 \Delta R \propto R^2 c^{-2} \quad\Longrightarrow\quad c^3 \propto R^2 \quad\Longrightarrow\quad c \propto R^{2/3}.$$
This is qualitatively different from both others. The horizon solution gives
$$R^{1/3}(u) = R_0^{1/3} - \tfrac{k}{3}\,u,$$
so $R \to 0$ at finite lookback $u_\text{origin} = 3R_0^{1/3}/k = 2/H_0$.
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

### S′ downstream results (computed)

Recomputed under $c \propto R^{2/3}$. Key relations, with $c_0, H_0$ present-epoch
values:

- **Present horizon radius:** $R_0 = \tfrac{2}{3}\,c_0/H_0$ (vs. $R_0 = 3c_0/H_0$ in V).
- **Redshift–radius:** $R_\text{emit}/R_\text{now} = (1+z)^{-3/2}$ (vs. $(1+z)^{-1/3}$ in V).
- **Distance–redshift:** $D(z) = R_0\left[\,1 - (1+z)^{-3/2}\,\right]$.
- **Distance to $z=1$:** $D_{z=1} = 0.6465\,R_0$ (vs. $0.2063\,R_0$ in V) — a factor
  of ~3 larger fraction of the horizon.
- **Maximum distance:** $D(z\to\infty) = R_0 = \tfrac{2}{3}c_0/H_0$, finite. Because
  $c_\text{emit}\to 0$ at the origin, redshift is *unbounded* while distance
  *saturates* at $R_0$.
- **Time-dependent $H$:** $H(u) = H_0 /\left(1 - \tfrac{k}{3}R_0^{-1/3}u\right)$,
  diverging at the finite origin.

**Two findings of note:**

1. **Low-$z$ Hubble law is identical to V.** Series expansion gives
   $D(z) \approx (c_0/H_0)\,z$ at leading order for *both* V and S′. The two laws
   (and ΛCDM) are observationally indistinguishable nearby; the exponent choice is
   invisible at low $z$ and only shows up at high $z$. This is a reassuring
   consistency check — switching to S′ does not break the Hubble law.

2. **High-$z$ pile-up against a finite edge — a genuine distinguishing observable.**
   The $(1+z)^{-3/2}$ falloff is far steeper than V's $(1+z)^{-1/3}$, so high-$z$
   sources are compressed into a thin shell near $R_0$. At $z=1$, S′ places a source
   at $0.65R_0$ vs. V's $0.21R_0$ — a ~3× difference in inferred distance at equal
   redshift. The $D(z)$ relation beyond $z\sim1$ therefore differs sharply between
   V, S′, and ΛCDM, and is the natural place to confront the model with a real
   distance ladder (standard candles / BAO). This is the first concrete observational
   discriminator the project has produced.

What remains uncomputed for S′: the OP-2 $a_0$ derivation (deferred until OP-3's
mechanism question is settled, since $a_0$ rests on it) and the luminosity-distance /
surface-brightness scaling (needed for an actual supernova comparison).

### S′ luminosity distance and the supernova test (computed)

The flux bookkeeping in this static VSL model differs from FLRW and must be done
from scratch. Working in coordinate time and converting at the endpoints, with
$x = c_\text{emit}/c_\text{now} = 1/(1+z)$:

- **Photon energy deficit $(1+z)^{-3}$.** Frequency is fixed in flight (premise 4),
  so a detected photon carries its emission-epoch energy $h\nu_\text{emit}$. Since
  atomic $\nu \propto c^3$ (OP-1),
  $\nu_\text{emit}/\nu_\text{now} = (c_\text{emit}/c_\text{now})^3 = (1+z)^{-3}$
  relative to the same transition today.
- **Arrival-interval contraction $(1+z)^{-1}$.** Two-photon light-travel argument in
  static space: with fixed map distance $D = \int c\,dt$, two photons emitted
  $\delta t_e$ apart arrive $\delta t_o = (c_\text{emit}/c_\text{now})\,\delta t_e$
  apart, i.e. *bunched* by $1/(1+z)$ in coordinate time. (The observer is at the
  present epoch, so observer proper time = coordinate time.)
- **Source-clock conversion $(1+z)^{+3}$.** Luminosity is energy per *source-local*
  second, and one source-local (atomic) second equals $(1+z)^3$ coordinate seconds
  (from $dt = d\tau\,(c_0/c)^3$).

Combining via $D_L^2 = L/(4\pi F)$ in static space (sphere area $4\pi D_\text{proper}^2$,
photon number conserved):
$$\frac{D_L^2}{D_\text{proper}^2} = \frac{(1+z)^{+3}}{(1+z)^{-2}} = (1+z)^5
\quad\Longrightarrow\quad D_L = (1+z)^{5/2}\,D_\text{proper}.$$
With $D_\text{proper} = \tfrac{2}{3}\tfrac{c_0}{H_0}\left[1-(1+z)^{-3/2}\right]$:
$$D_L(z) = \frac{2}{3}\frac{c_0}{H_0}\,(1+z)\left[(1+z)^{3/2} - 1\right].$$

**Low-$z$ behaviour.** $D_L \approx \tfrac{c_0}{H_0}\left(z + \tfrac{5}{4}z^2 + \dots\right)$,
giving an effective deceleration parameter $q_0 = -3/2$ — i.e. S′ *mimics
acceleration* at low $z$ with no dark energy, which superficially resembles the
supernova result. This is the encouraging part.

**High-$z$ verdict (the real test).** Computing the distance modulus difference
$\Delta\mu = \mu_{\text{S}'} - \mu_{\Lambda\text{CDM}}$ (flat $\Omega_m=0.3$,
$H_0=70$):

| $z$ | $\Delta\mu$ (mag) |
|---|---|
| 0.1 | $+0.10$ |
| 0.3 | $+0.31$ |
| 0.5 | $+0.51$ |
| 1.0 | $+0.99$ |
| 1.5 | $+1.43$ |
| 2.0 | $+1.82$ |

S′ predicts supernovae **far fainter** than observed beyond $z\sim0.3$. Modern SN
samples constrain $\mu$ to $\sim0.05$–$0.1$ mag; a discrepancy of $\sim1$ mag at
$z=1$ and nearly $2$ mag at $z=2$ is **wildly excluded** by existing data. The
$(1+z)^{5/2}$ dimming is simply too steep.

**Verdict for S′:** the low-$z$ mimicry of acceleration is appealing, but the
high-$z$ luminosity distance is decisively wrong. As it stands, **S′ is falsified by
the supernova Hubble diagram.** This is the first hard observational collision in the
project, and it is a real one — not a coefficient dispute.

**Caveats before declaring S′ dead:**
1. The $(1+z)^{-3}$ energy factor and $(1+z)^{+3}$ clock factor both rest on
   $\nu \propto c^3$, which itself rests on symmetric PV (OP-1 caveat). A different
   frequency power changes the exponent in $D_L = (1+z)^{p'}D_\text{proper}$.
2. The bolometric-vs-passband (K-correction) treatment here is schematic; a real
   comparison needs the spectral energy distribution shifted properly. This can
   shift $\Delta\mu$ by tenths of a mag, not the ~1–2 mag needed to rescue it.
3. The same calculation should be run for variant **V** ($c\propto R^3$) before
   concluding VSL-static is dead in general — V has a different $D_\text{proper}(z)$
   and may dim differently. **Done — see below.**

**Variant V comparison (computed).** The $(1+z)^{5/2}$ factor is *generic* — it
depends only on $\nu\propto c^3$ and static space, not on the $c\propto R^n$
exponent. Only $D_\text{proper}(z)$ differs. Running the same distance-modulus test
for V ($c\propto R^3$, $D_\text{proper}=R_0[1-(1+z)^{-1/3}]$, $R_0=3c_0/H_0$):

| $z$ | $\Delta\mu$ (V) | $\Delta\mu$ (S′) |
|---|---|---|
| 0.1 | $+0.22$ | $+0.10$ |
| 0.3 | $+0.63$ | $+0.31$ |
| 0.5 | $+0.99$ | $+0.51$ |
| 1.0 | $+1.78$ | $+0.99$ |
| 2.0 | $+2.98$ | $+1.82$ |

V is *worse*: effective $q_0 = +1.0$ (looks strongly decelerating, not
accelerating), then over-dims even harder at high $z$. **Both variants are excluded
by the SN Hubble diagram; V more severely than S′.** The static-VSL framework, with
the photon bookkeeping as derived here, cannot reproduce the observed
distance–redshift relation in either variant.

### What a resolution must supply

1. A principled reason to choose the contributing set (bulk vs. boundary) — ideally
   the pilot-wave argument made quantitative, or a holographic-bound justification
   for the surface law.
2. The remaining S′ downstream pieces: luminosity distance / surface-brightness
   scaling, and (after OP-3) the $a_0$ derivation under $c\propto R^{2/3}$.
3. Resolve whether the Compton-thickness feedback ($\lambda_C \propto c^{-2}$) is
   the right self-consistency condition, or whether a different invariant length
   (Planck length, fixed comoving scale) is more defensible — each gives a different
   exponent.

**Decision recorded:** core stays on **V** ($c\propto R^3$) for now. **S′** is the
leading alternative and the most interesting — finite origin in both time frames,
and now a concrete high-$z$ distance-relation signature that could discriminate it
observationally. Core-level distance/age relations have been computed (above);
promote S′ to core after the luminosity-distance scaling and a first distance-ladder
sanity check.

---

## OP-6 — Primordial matter genesis and the self-bootstrapping origin

*Status: open, speculative, but with a real logical spine. This entry depends on
variant S′ of OP-5 ($c \propto R^{2/3}$, with finite coordinate origin), where the
Compton wavelength diverges at $t=0$. It proposes that the model's posited Machian
premise ($c \propto N$) is not an external assumption but the fixed point of a
self-consistent matter-creation process. Several pieces are conjectural and flagged
as such; the matter/antimatter asymmetry is unsolved.*

### The early-time regime (established)

In S′, $c \propto R^{2/3}$ and
$\lambda_C = \hbar/(mc) \propto c^{-2} \propto R^{-4/3}$. Relative to the horizon,
$\lambda_C/R \propto R^{-7/3}$, which **diverges
as $R \to 0$.** So at the earliest epochs every particle is delocalized over a
region larger than the entire causal universe. Localization does not exist; the
early universe is a single coherent quantum object. (This is also the ideal regime
for the pilot-wave framing: the guiding wave genuinely spans everything.)

Two further scalings, established by direct computation:
- **Pair lifetime diverges.** Pair rest energy $E \sim mc^2 \propto c^3$, so the
  time–energy uncertainty bound permits a lifetime
  $\Delta t \sim \hbar/E \propto c^{-3} \to \infty$ as $c \to 0$. Pairs created at
  the origin need never annihilate;
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

## OP-7 — The mass-relation exponent is over-constrained

*Status: open, central. This entry isolates a single lever — the power $s$ in
$m \propto c^{s}$ — and shows that three independent requirements (the supernova
Hubble diagram, orbital stability, and the genesis bootstrap) each pin it to a
different value, with no overlap. Until the origin of mass in this framework is
understood, $s$ cannot be predicted; but the data already constrain it.*

### The single lever

Under symmetric PV ($\epsilon_0 \propto c^{-1}$, with $e, h$ invariant), the atomic
transition frequency is $\nu \propto m\,c^{2}$, so a mass law $m \propto c^{s}$ fixes
the frequency power $p = s + 2$ in $\nu \propto c^{p}$. The generic static-VSL
luminosity distance (derived in OP-5) is
$$D_L = (1+z)^{(2p-1)/2}\,D_\text{proper} = (1+z)^{(2s+3)/2}\,D_\text{proper}.$$
So $s$ controls everything downstream: the clock rate, the proper age, the SN
dimming, and (through $G$-scaling) orbital stability.

### Three requirements, three different values of $s$

| Requirement | Demands | $s$ ($m\propto c^s$) | $p$ ($\nu\propto c^p$) |
|---|---|---|---|
| **SN Hubble diagram** | $D_L$ matches observed $\mu(z)$ | $s \approx 0$ (near-invariant) | $p \approx 2$ |
| **Machian orbital lock** (core §6) | $GM$ time-independent so $c$ cancels in $v^2=GM/r$ | $s = +1$ | $p = 3$ |
| **PV self-energy** (Puthoff local) | $m$ from local vacuum energy | $s = -3/2$ | $p = 1/2$ |
| **S′ genesis bootstrap** (OP-6) | $\lambda_C \propto c^{-2}$ for super-horizon Compton wavelength | $s = +1$ | $p = 3$ |

The SN-preferred value and the orbital/genesis-preferred value **do not coincide.**

### The supernova window (computed, with caveat)

Fitting $p$ against a ΛCDM ($\Omega_m=0.3$) distance modulus over $0.05 < z < 1.5$,
with a free absolute-magnitude offset:

- **V ($c\propto R^3$):** best-fit $p \approx 1.76$ ($s \approx -0.24$), residual
  RMS $\approx 0.023$ mag.
- **S′ ($c\propto R^{2/3}$):** best-fit $p \approx 2.26$ ($s \approx +0.26$),
  residual RMS $\approx 0.034$ mag.

Both straddle $p = 2$ ($s = 0$, **cosmologically invariant mass**), which is the
natural symmetric point viable for both horizon laws. With invariant mass,
$D_L = (1+z)^{3/2}D_\text{proper}$ — between the excluded Machian $(1+z)^{5/2}$ and
PV $(1+z)^{0}$ endpoints, and a good match to observed distances.

**So: a near-invariant mass works for the SN test.** This is the most appealing
point on the axis — "rest mass is a local invariant, not coupled to the cosmological
vacuum state" is the least exotic of the three assumptions.

**Caveat (important).** The fit uses ΛCDM as a proxy for SN data. A one-parameter
smooth curve matching another smooth curve over a limited $z$ range to ~0.03 mag is
*suggestive, not confirmatory* — the model was given a free $p$ and a free offset.
The robust conclusion is qualitative: **the data demand a low power,
$|s| \lesssim 0.3$, near zero.** The precise value (and whether V's slightly-negative
or S′'s slightly-positive is favored) requires the real Pantheon+ compilation with
covariance and $z \to 2$ leverage. Logged for a future session.

### The tension

- **SNe want $s \approx 0$.** Invariant or near-invariant mass.
- **Orbital lock wants $s = +1$.** The whole point of the Machian rule (core §6) was
  that $G\propto c^{-1}$ and $M\propto c^{+1}$ cancel $c$ out of $v^2 = GM/r$. With
  $s=0$ this cancellation fails and planetary drift returns *unless* the $G$-scaling
  alone can stabilize orbits (untested — see OP-3, which must now also ask whether
  the variable-mass fix was even necessary).
- **Genesis wants $s = +1$.** The S′ finite origin and free-matter-creation story
  (OP-6) need $\lambda_C = \hbar/(mc) \propto c^{-2}$, i.e. $m \propto c$. With
  $s=0$, $\lambda_C \propto c^{-1}$ — still diverges as $c\to0$, so the qualitative
  genesis picture may survive, but the specific $c^{-2}$ scaling and the
  epoch-invariant $r_s/\lambda_C$ coincidence are lost.

### What a resolution must supply

1. **A theory of mass.** $s$ cannot be predicted until the origin of rest mass in
   this framework is understood. Setting $s=0$ because it fits the SN data is the
   free-parameter move the project is trying to avoid. The constraint "$|s|$ small"
   is a real input to the eventual mass theory, not a fitted dial.
2. **A real SN fit.** Replace the ΛCDM proxy with Pantheon+ (covariance, high-$z$).
   Determine whether $s=0$ exactly is favored or a small nonzero value.
3. **Reconciliation with orbits.** Does $G$-scaling alone stabilize orbits at $s=0$,
   or is some mass coupling unavoidable? This is now a prerequisite question for OP-3
   and may determine whether the Machian variable-mass fix was necessary at all.

**Cross-reference:** this directly motivates re-opening OP-3 (rotation curves /
orbital stability) without assuming $M \propto c$. If orbits are stable and rotation
curves work at $s=0$, the variable-mass machinery — and much of OP-6 — was an
unnecessary detour.

---

## OP-8 — The invariant-mass / $G\propto c^{-2}$ branch (recommended core)

*Status: leading model. This branch drops the Machian $M\propto c$ rule entirely
(shown to be a bad fix — see below) in favour of cosmologically invariant rest mass
($s=0$) together with $G\propto c^{-2}$. At the point $(s=0,\,g=-2)$, four
independent astrophysical tests are mutually consistent. The one unexplained input
is the value $g=-2$, which is currently selected by flux-constancy rather than
derived; but it is over-determined (it must satisfy three further constraints, and
does).*

### Notation

$m \propto c^{s}$ (rest-mass power), $G \propto c^{g}$ (gravitational-coupling
power). Under symmetric PV, atomic/nuclear frequency
$\nu \propto m\,c^2 \propto c^{p}$ with $p=s+2$.

### Why the Machian fix ($s=+1$) was bad

The prior session introduced $M\propto c$ to lock orbits. Worked properly, it fails
three ways at once:

1. **Rotation curves die.** The retarded-potential flat-curve floor is
   $v_\text{floor}^2 = -(g+s)\,GM\,H_0/c$. The Machian choice pairs $s=+1$ with
   $g=-1$ (core §6's $G\propto1/c$), giving $g+s=0$ — the floor vanishes. The same
   $GM=\text{const}$ that was meant to lock orbits exactly cancels the dark-matter
   mechanism. (This confirms the OP-3 tension flag.)
2. **Orbits shrink, not lock.** Done with angular-momentum conservation, the
   adiabatic circular orbit drifts as $r\propto c^{-(3s+g)}$. Machian gives
   $r\propto c^{-2}$ — the orbit *contracts* as $c$ grows. The prior "perfect lock"
   claim mishandled the momentum bookkeeping.
3. **SN over-dimming.** $p=3$ gives $D_L=(1+z)^{5/2}D_\text{proper}$, excluded by
   the Hubble diagram (OP-5).

### What orbital stability should mean here

Not "fixed $r$ on the map." Everything scales, so the Sun's luminosity rises over
cosmic time (photons from nuclear reactions gain energy as $c$ grows). The physical
requirement is **constant stellar flux at the planet** — habitability — which
*requires the orbit to expand* to compensate for brightening. We want drift, of a
specific rate.

### The four constraints as functions of $(s,g)$

| Test | Condition |
|---|---|
| **SN Hubble diagram** | $D_L=(1+z)^{(2p-1)/2}D_\text{proper}$ viable near $p\approx2$, i.e. $s\approx0$ (OP-7) |
| **Rotation-curve floor exists** | $g+s<0$ |
| **Orbit expands** (habitability direction) | $-(3s+g)>0$ |
| **Flux exactly constant** | $L\propto r^2$ with $L\propto c^{2p}=c^{2(s+2)}$ and $r\propto c^{-(3s+g)}$, giving $4s+g=-2$ |

### Luminosity scaling (derived)

$L\propto c^{2p}$. Chain: energy per fusion reaction $\propto c^{p}$ (nuclear binding
tracks the energy scale); reaction rate per nucleon is a stable dimensionless number
in proper units, but a proper second is $\propto c^{-p}$ in absolute units, so the
absolute rate $\propto c^{+p}$; baryon number fixed. Product $L\propto c^{2p}$.

*Caveat:* this uses the nuclear-rate-sets-luminosity picture. In standard
astrophysics luminosity is set by *radiative transport* (energy leakage), with the
core self-adjusting to match. Whether the leakage rate carries the same power needs
checking; it could shift the exponent. Same proper-time-bookkeeping family as the SN
caveat.

### The consistent point: $s=0$, $g=-2$

Solving flux-constancy $4s+g=-2$ at $s=0$ gives $g=-2$ ($G\propto c^{-2}$). Checking
all four tests there:

| Test | At $(s=0,g=-2)$ | Pass |
|---|---|---|
| SN distance | $p=2$, $D_L=(1+z)^{3/2}D_\text{proper}$ | ✓ (OP-7 viable case) |
| Rotation floor | $g+s=-2<0$, $v_\text{floor}^2=2\,GM\,H_0/c$ | ✓ |
| Orbit expansion | $r\propto c^{+2}$, expands | ✓ |
| Flux constancy | $L\propto c^4$, $r^2\propto c^4$, $L\propto r^2$ exactly | ✓ |

The faint-young-Sun problem and orbital evolution merge into one mechanism: the Sun
brightens as $c^4$, the orbit expands as $c^2$, and the flux holds constant
automatically. The rotation-curve mechanism is alive because $GM\propto c^{-2}$ is
genuinely time-dependent.

### Status of $g=-2$: selected, not yet derived

The core §6 derivation of $G\propto c^{-1}$ assumed growing mass ($M\propto c$); with
invariant mass that argument lapses, so $g$ is open. Flux-constancy *selects*
$g=-2$. This is not a free fit in the usual sense — the same value must (and does)
also give the right SN dimming, a live rotation floor, and the right drift
direction, so it is an over-determined dial. But it is not yet a derivation. A
principled origin for $G\propto c^{-2}$ is the main theoretical debt of this branch.

### Open pieces

1. **Why invariant mass, not PV?** The PV self-energy law gives $s=-3/2$, excluded by
   all of the above. We have not re-derived what the PV framework actually requires
   for the mass law, nor why a cosmological setting should override it with $s=0$.
   (Deferred per author; the original PV requirement is to be revisited.)
2. **Derive $g=-2$.** Find a field-equation / action principle that yields
   $G\propto c^{-2}$ under invariant mass, replacing the lapsed §6 argument.
3. **Radiative-transport check on $L\propto c^4$.** Confirm the luminosity power
   against energy-leakage physics, not just nuclear rate.
4. **Downstream of $G\propto c^{-2}$.** Stellar hydrostatic structure, the numerical
   $a_0$ (OP-2), and gravitational binding all shift under a steeper $G$-scaling and
   need rechecking.
5. **Real SN fit.** Replace the ΛCDM proxy with Pantheon+ to confirm $p=2$ (OP-7).

---

## OP-9 — The conformal-projection hypothesis (what the model *is*) — **REFUTED for the particle-counting model**

*Status: tested and refuted. The conformal-projection hypothesis is FALSE as long as
the particle-counting horizon law ($c\propto R^3$, premise 2) is retained. The static
model and FLRW agree on redshift by construction but disagree on luminosity distance,
and Etherington's reciprocity theorem proves a genuine conformal reframing cannot do
that. The model is therefore a genuine rival theory, not a reframing of standard
cosmology. The decisive consequence — the supernova over-dimming is a real physical
departure from FLRW, not a fixable bookkeeping artifact — is now established. The
original claim and its tests are preserved below for the record, followed by the
refutation.*

### The refutation (the test run)

**Etherington reciprocity theorem.** In *any* metric theory, photon-number
conservation along null geodesics forces
$$D_L = (1+z)^2 D_\text{angular} = (1+z)\,D_\text{comoving},$$
independent of the coordinate system. Conformal invariance of null geodesics means a
true conformal reframing of FLRW **cannot change $D_L$**. So if the static model were
FLRW in disguise, it would be obligated to reproduce the FLRW luminosity distance
exactly.

**The comparison.** For a matched Einstein–de Sitter cosmology, FLRW gives
$D_L^\text{EdS} = \tfrac{2c_0}{H_0}(1+z)\big(1 - (1+z)^{-1/2}\big) \cdot$ (i.e.
$D_L=(1+z)D_C$ with $D_C = \tfrac{2c_0}{H_0}[1-(1+z)^{-1/2}]$). The static model
(volume law, invariant mass, $p=2$) gives
$D_L^\text{static} = (1+z)^{3/2}\,R_0[1-(1+z)^{-1/3}]$ with $R_0=3c_0/H_0$. These
diverge:

| $z$ | $D_L^\text{EdS}$ | $D_L^\text{static}$ | ratio |
|---|---|---|---|
| 0.1 | 0.102 | 0.108 | 1.06 |
| 0.5 | 0.551 | 0.697 | 1.27 |
| 1.0 | 1.172 | 1.751 | 1.49 |
| 2.0 | 2.536 | 4.780 | 1.89 |

(in units of $c_0/H_0$). The discrepancy has the **same shape and magnitude** as the
supernova over-dimming (OP-5/OP-7).

### What this establishes

1. **OP-9 is false for the $c\propto R^3$ model.** The agreement on redshift is "by
   construction" (both give $1+z=a_0/a = c_\text{now}/c_\text{emit}$); the
   disagreement on $D_L$ is fatal to the conformality claim, because Etherington
   forbids it for a true reframing.
2. **The model is a genuine rival theory**, not a coordinate relabeling of GR. Its
   distinctive results (finite origin, genesis bootstrap, $1/d$ rotation-curve term)
   are predictions of a *non-standard* cosmology.
3. **The SN over-dimming is explained and is not fixable.** It is the model genuinely
   departing from FLRW. Etherington guarantees no alternative photon bookkeeping
   rescues it: any photon-conserving metric theory with this redshift relation is
   pinned to $D_L=(1+z)D_C$, and the model does not sit there. This retroactively
   settles the OP-5 caveat about the $(1+z)^{+3}$ clock factor — the over-dimming is
   real, not an artifact.

### The over-determination (why both desirable claims can't hold)

The model independently asserts two things that conflict:
- **Particle-counting law** $c\propto R^3$ (premise 2) → a specific, non-FLRW
  distance relation. Rival theory; falsified by SNe; but keeps all distinctive
  predictions.
- **Conformal identification** $c = c_0\,a(t)$ from FLRW (OP-9) → reproduces every
  FLRW observable including $D_L$, by construction; but premise 2 is abandoned, and
  with it the finite origin, genesis, and independent derivations. Adds nothing new.

**You can have either, not both.** In particular, the rotation-curve mechanism (OP-3)
lives in the *rival-theory* branch — the one that does **not** match FLRW. So it
cannot simultaneously be a hidden feature of standard cosmology. The capstone hope
(projection exact *and* flat curves back-project to GR) is exactly what is excluded.

### Original claim and tests (preserved for the record)

The claim was that, following Atkinson (1962), an expanding FLRW universe maps
conformally onto the static map with $c\propto a$, making the model a reframing
rather than a rival, with results back-projectable to standard cosmology — including
the striking consequence that standard cosmology should itself predict flat rotation
curves as a dropped retardation term, with dark matter as the cost of the
"bound systems decouple" approximation. The two decisive tests were (1) the
luminosity-distance coincidence and (2) dynamical conformal consistency. **Test 1 has
now been run and failed.** Test 2 is moot for the particle-counting model.

### Why the refutation is robust: kinematic vs. dynamical redshift (rigorous recheck)

A careful redo of the luminosity distance — counting conserved photons and tracking
energy-per-photon and arrival rate separately, with luminosity defined in the
source's proper units (the same discipline used for the stellar-flux calculation in
OP-8) — **reproduces the exponent exactly**: $D_L = (1+z)^{(2p-1)/2}D_\text{proper}$,
with no double-counting and no clock-factor ambiguity. So the departure is not a
bookkeeping artifact.

The recheck pinpoints the *physical* origin of the departure. Standard Etherington
gives $D_L^2/D_A^2 = (1+z)^4$ because in FLRW the photon-energy redshift and the time
dilation are each **kinematic** — from $a(t)$ — contributing one factor of $(1+z)$
apiece. In this model both factors instead come from the **atomic energy scale**
$\nu\propto c^p$ and contribute $(1+z)^p$ apiece. The model asserts that a given
atomic transition was emitted with genuinely *less energy* in the past (by
$(1+z)^{-p}$ versus a fixed lab standard); FLRW asserts it was emitted at the same
energy and stretched in flight. **Same observed redshift, fundamentally different
energy accounting.**

This is why Etherington cannot be "fixed": the theorem assumes the candle's absolute
output is epoch-independent, and this model violates that premise *as physics*. The
two coincide only at $2p-1=4$, i.e. $p=5/2$ ($m\propto c^{1/2}$) — not a physically
motivated value, and not the $p\approx2$ that OP-7/OP-8 independently favour.

**Corollary (a clean future test).** Because the departure is controlled entirely by
the energy-scale power $p$, supernova distances effectively *measure* $p$ —
independently of the mass-relation and orbital arguments. If a real SN fit returns a
$p$ inconsistent with the $p\approx2$ from OP-7/OP-8, that is a second internal
over-determination (distinct from the mass-vs-orbit one); if consistent, it is
corroboration.

### What remains (the fork)

The project must now choose its identity:
- **Branch A — rival theory (keep premise 2).** Accept that the model is not FLRW,
  accept the SN tension as a real (currently fatal) prediction, and ask whether *any*
  modification of the distance relation within the particle-counting framework can be
  reconciled with SNe. Distinctive predictions retained.
- **Branch B — exact reframing (drop premise 2).** Define $c=c_0 a$, inherit FLRW
  exactly, lose the distinctive content. Of interest only as a pedagogical
  restatement of GR, not a new cosmology.

Branch A is the only one with original content, and it is currently in conflict with
supernova data. That conflict — not the conformality dream — is the project's central
open problem. (The bonus hope of *deriving* $G\propto c^{-2}$ from conformal
consistency, OP-8, also dies with OP-9: there is no exact conformal consistency to
derive it from.)

---

## Cross-cutting note

OP-1 (proper-time integral), OP-3 (retarded gravity), and OP-4 (loop running) all
turned on the same structural feature: quantities *constant in lockstep* under a
coupling vs. quantities that vary along a *backward light cone*. This is now
understood. The Machian model's fatal flaw was that $GM=\text{const}$ (the very
thing that appeared to lock orbits) simultaneously zeroed the rotation-curve term.
The invariant-mass branch breaks that degeneracy ($g+s=-2\neq0$): $GM\propto c^{-2}$
varies along the light cone, reviving the rotation-curve floor (OP-3) while the
orbital dynamics give controlled expansion rather than a lock (OP-8). The elegance
and the problems were indeed two faces of one coupling — and swapping the coupling
resolved both at once.

OP-5 (what sources $c$) and OP-6 (genesis) are a second cluster, both rooted in the
underived first principle behind premises 2–3. They are most naturally pursued
together, and only under variant S′. A notable cross-link: the epoch-invariant
$r_s/\lambda_C$ ratio (OP-6) and the Compton-thickness feedback (OP-5 S′) are the
same $c^{-2}$ scaling appearing in two places, which is mild evidence the S′ branch
is internally coherent.
