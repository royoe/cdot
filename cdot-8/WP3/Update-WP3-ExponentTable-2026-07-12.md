# Update — WP3: The Exponent Table Finds a Future-Directed Instability, Not a Past One

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 11. Executes the
directives from `Advisory-WP3-AnchorAndC1-2026-07-12.md` and
`Addendum-FifthRound-C1RowExact-2026-07-12.md`: verify the $C_1$-exactness claims,
then build the per-era homogeneous-mode exponent table for $p_{\mathcal N}$ before
touching the quadrature. The $C_1$ claims check out. The exponent table surfaces a
real problem — but in the opposite direction from where every prior round looked.*

---

## 1. $C_1$-exactness claims verified

Re-derived, independent of both advisories: WP1's $a=(c/c_0)^{3/2}$ and the two-clock
$N=(c/c_0)^{5/2}$ give $Q=1/N=a^{-5/3}=(1+z)^{5/3}$ **exactly, for any $c$**, not a
fixed-point approximation — checked numerically at five values of $c/c_0$ spanning
$0.3$–$3.0$, exact match every point (caught and corrected one of my own algebra slips
in the process — briefly used WP1's exponent inverted, re-derived properly before
trusting the result). $a^3=Q^{-9/5}$ confirmed on the same grid. The addendum's
$F$-sector cross-check ($\Delta(F-QF_Q)=-\tfrac9{14}C_1Q^{14/5}$) reproduced by hand.
**$C_1=0$ via past regularity is confirmed as exact and era-independent, not
conditional on the radiation-era clock exponent as the stand-in's directive 3 worried**
— the addendum's strike of that contingency is correct.

---

## 2. The exponent table — built on the actual fitted trajectory, not just the two
fixed points

$p_{\mathcal N}$'s homogeneous mode satisfies $d\ln p_{\mathcal N}/ds=-g(s)$ with
$g=(p-\tfrac52)+3\kappa\lambda x(s)$ ($s=\ln(c/c_0)$), evaluated along the actual
census-closed trajectory (same machinery as `budget_invoice.py`, integrated both
backward — matter fixed point toward the radiation fixed point — and **forward**,
which none of the prior sign checks had done).

**Backward (past) direction — matches the well-posedness advisory's own sign check,
extended across the full crossover, not just the two endpoints:**

| $z$ | $x(s)$ | $g_\text{matter}$ | $g_\text{rad}$ |
|---|---|---|---|
| $0$ | $1.10$ | $1.44$ | $-0.063$ |
| $1$ | $1.55$ | $2.03$ | $+0.53$ |
| $10$ | $1.73$ | $2.26$ | $+0.76$ |
| $100$–$10^6$ | $1.81\to3.44$ | $2.37\to4.50$ | $0.87\to3.00$ |

Positive throughout once $z\gtrsim0.3$ (matching the advisory's fixed-point-only
check), confirming the past-directed mode decays going backward — **except right at
$z=0$, where $g_\text{rad}$ is slightly negative** ($x_0=1.10$ sits just below the
critical value $x=1.148$ where $g_\text{rad}=0$).

**Forward (future) direction — not previously checked by anyone in this program:**
integrating the same $g_\text{rad}(s)$ forward, $x(s)$ *decreases* toward the deep-
MOND future (the physical, $\delta_0<0$ branch's own documented behavior, not the
$\delta_0>0$ runaway), so $g_\text{rad}=-\tfrac32+3\kappa\lambda x\to-\tfrac32$
asymptotically — **staying negative and growing more negative all the way into the
future**:

| $s$ (future) | $x(s)$ | $g_\text{rad}$ | $\ln(p_{\mathcal N,\text{rad}}^\text{hom}(s)/p^\text{hom}(0))$ |
|---|---|---|---|
| $0.5$ | $0.54$ | $-0.79$ | $+0.23$ |
| $1.0$ | $0.24$ | $-1.18$ | $+0.73$ |
| $2.0$ | $0.05$ | $-1.43$ | $+2.07$ |
| $2.9$ | $0.02$ | $-1.49$ | $+3.39$, still climbing linearly |

**The radiation-weighted homogeneous mode grows without bound toward the future**,
asymptotically as $e^{+1.5s}$ — it does not decay. The matter-weighted mode, checked
the same way, *does* decay forward ($\ln$ ratio saturates at $-0.96$, bounded).

---

## 3. What this means

This is the "MM's inflationary counter-example is the standing warning" scenario
both advisories anticipated — but it lands in a different place than either
predicted. The well-posedness advisory's own sign check (matter and radiation fixed
points only) and the anchor-and-$C_1$ advisory's framing both focused past-regularity
concern on the *eternal past*; the actual problem found here is future-directed, and
specific to the radiation-species piece. **Past regularity (forcing $p_{\mathcal
N,\text{rad}}^\text{hom}\to0$ as an initial condition, deep in the past or at a finite
deep-RD anchor per the Maggiore-Mancarella method) does not, by itself, protect the
construction from this mode reappearing and growing without bound arbitrarily far into
the future** — a nonzero mode, however small, injected by any later perturbation or
numerical residual, is not damped; it is amplified, and unboundedly so on the
eternal future this framework is built to have.

**Mitigating consideration, not yet a resolution**: this is specifically the
*radiation*-weighted piece, whose physical amplitude ($\mathcal N_\text{rad}$'s own
contribution to the total census) becomes utterly negligible at low $z$ and even more
so into the deep-MOND future — so the practical question is whether this growing
mode, multiplied by whatever tiny coefficient the past-regularity condition leaves it,
stays numerically negligible for all physically relevant (though not all
mathematically eternal) future time, or whether it is a genuine, first-principles
problem with treating radiation as a separately-multiplied census sector at all once
it is dynamically irrelevant. This has not been resolved here.

---

## 4. Status — escalating, not resolving alone

This is a new finding, not anticipated by either advisory, found by doing exactly what
was asked (build the table, don't assume stability by analogy, check the full
trajectory rather than the endpoints) — and it goes in a direction (future, not past;
radiation-specific, not generic) that changes where the open problem sits. Given the
pattern of this program (four rounds of a specific technical claim needing a
correction from a second read), and given this finding could be either a real,
first-principles obstruction to the species-resolved construction or a artifact of
treating radiation's own multiplier as significant long after radiation itself has
become dynamically irrelevant, this is reported for review before the quadrature redo
proceeds — redoing it while this is unresolved would risk building on an unstable
foundation twice over.
