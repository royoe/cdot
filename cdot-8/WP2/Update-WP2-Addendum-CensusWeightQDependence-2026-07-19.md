# Addendum — WP2: Do the Census Weights ($E_P$, $p_i^\text{sp}$) Depend on Local $Q$? Decided: No, by the Existing Definitions

*Companion: `cdot-8/WP7/SessionLog-2026-07-18.md`. Answers the channel
flagged by the advisory in `Advisory-WP7-QDefinitionAdjudicated-2026-07-18.md`
§4, directive 2: "the census weights ($E_P$, the $p_i^\text{sp}$ exponents)
may themselves depend on the local $Q$, giving a $\delta Q$-proportional
piece of $\delta\mathcal N$... Decide it on the WP2 record, in writing, not
silently." This addendum is that decision.*

---

## 1. The question, stated precisely

WP7 §5 (`Update-WP7-PerturbationStructure-2026-07-18.md`) confirmed the
perturbed census decomposes into density and volume pieces only:
$$\delta\mathcal N_i(k,t)=\bar{\mathcal N}_i(t)\,W(kR_h(t))\,\big[\delta_i(k,t)-3\Phi(k,t)\big].$$
This assumed the *weights* multiplying $\delta_i,\Phi$ — the Planck-energy
normalization $E_P(t)$ and each species' coordinate-energy exponent
$p_i^\text{sp}$, both entering $\mathcal N_i$'s definition — are themselves
unperturbed background quantities. **Not yet explicitly checked**: does a
local, perturbed $\delta Q(x,t)$ feed into $E_P$ or $p_i^\text{sp}$
directly, adding a third, $\delta Q$-proportional piece to $\delta\mathcal
N_i$ alongside the density and volume pieces already derived?

## 2. Checked against the actual definitions, not assumed either way

**$E_P(t)$**: WP2's own foliation-integral definition (§1 of the main
document) writes
$$\mathcal N(t)\equiv\int_{\Sigma_t\cap\{\chi\le\chi_h(t)\}}
\frac{\rho_{E,\text{coord}}(x,t)}{E_P(t)}\sqrt q\,d^3x,\qquad
E_P(t)=\sqrt{\hbar c(t)^5/G}.$$
**$E_P$ is written with argument $(t)$ only — outside the spatial
integral, alongside $\rho_{E,\text{coord}}(x,t)$'s own $(x,t)$-dependence.**
This is not an approximation or a homogeneous-sector simplification later
generalized; it is how the object was defined from the start, as a single
time-slice normalization, exactly the same status as $\Lambda_M(t)$ and
$Q(t)$ in $S_{M5}$ (WP7 §4) — "one number per slice." $c(t)$ itself is
WP1's purely kinematic redshift-law relation $c(t)=c_0(a(t)/a_0)^{2/3}$,
a background quantity derived before $Q$ or $F(Q)$ enter the program at
all (WP1, §4) — it carries no $x$-dependence and no $Q$-dependence by
construction.

**$p_i^\text{sp}$**: WP1 §5 derives these exponents directly from the
Planck-unit relabeling convention applied to each species' coordinate
energy: matter $E_{m,\text{coord}}=m_\text{coord}(t)c(t)^2\propto c^{5/2}$
($p=5/2$), radiation $E_{\gamma,\text{coord}}=\hbar k\,c(t)\propto c^1$
($p=1$) — checked directly against known physical dilution laws (matter
$a^{-3}$, radiation $a^{-4}$) and confirmed exact, not fit. **These
exponents are fixed structural labels of each species' mass/frequency
scaling under the $c(t)$ relabeling** (the same $m\propto c^{1/2}$,
$\nu\propto c^{5/2}$ kinematic exponents WP1 established for *all* of
cdot-7's dictionary, before WP2/WP3/M5 existed) — they carry no argument
of any kind that could be $Q$-dependent; there is nowhere in their
derivation for a local scalar-field value to enter.

## 3. Decision

**The census weights do *not* depend on local $Q$, under the existing,
unamended WP2/WP1 definitions.** Both $E_P(t)$ and each $p_i^\text{sp}$
are pure kinematic bookkeeping quantities, built from the background
$c(t)$ relabeling alone — the same status as $\Lambda_M(t)$, $Q(t)$
themselves in $S_{M5}$, not local fields with their own perturbation.
**Consequence**: the density+volume decomposition already derived in WP7
§5 is the *complete* linear-order decomposition of $\delta\mathcal N_i$ —
there is no missing third, $\delta Q$-proportional channel. This is a
decision *about the existing definitions as written*, not a new
assumption or a convention adopted to simplify the assembly: rereading
$E_P(t)$'s own argument list and $p_i^\text{sp}$'s own derivation settles
it directly.

**One thing this decision does *not* say**: that $Q$'s background
trajectory $\bar Q(t)$ is irrelevant to $\bar{\mathcal N}_i(t)$ — it
isn't; $\bar{\mathcal N}_i(t)$'s own time-evolution (WP2 §2) already
depends on the full background trajectory, including everything $\bar
Q(t)$ feeds into via $c(t)$'s own relation to the lapse ($N=1/\bar Q$,
WP3). That background dependence is already fully carried by
$\bar{\mathcal N}_i(t)$ itself in WP7's assembled term (§4, §6, §11) —
this addendum only rules out an *additional*, independently-perturbing,
$\delta Q$-sourced piece riding on top of the density/volume terms
already derived.

**Scope note, carried forward honestly**: this decision is scoped to
$E_P$ and $p_i^\text{sp}$ specifically, the two objects the advisory
named. It does not bear on the separate, still-open census-sector
covariantization-freedom item (WP7 §13: census gauge status, fiducial
center, $a^3\leftrightarrow R_h^3$ convention) — a different question
about how the ball/window itself covariantizes, not about whether these
two *weights* carry independent $Q$-dependence. Nothing in `cdot-7/` was
touched.

## 4. Amendment (advisor review, 2026-07-19, accepted) — the declined alternative is facet 4 of the freedom item, not outside it

`Advisory-WP2-AddendumReviewed-2026-07-19.md` +
`census_weight_review.py`. **Accepted, verified independently**: $E_P
\propto c^{5/2}$ is the standard Planck-energy scaling; the census
integrand $\rho_{E,\text{coord}}/E_P\propto c^{p_i-5/2}$ reproduces
WP2's own established $g_i=(p-\tfrac52)\dot c/c+3c/R_h$ structure
exactly ($p_\text{matter}-\tfrac52=0$, already fixed in WP1 §5, not a
new fact) — the core verdict above stands.

**The scope note above draws the line one notch too cleanly.** The
alternative it declines — a *locally*-normalized census, $E_P(x,t)$
built from a ball-smoothed local $c$ rather than the single per-slice
$c(t)$ — is not excluded by physics, only by the definitions as
currently built. That makes §3's "no" a *default choice* among
admissible covariantizations, not an independent, physics-forced fact
outside the freedom item. **Amendment accepted**: this alternative
files as **facet 4 of the census-sector covariantization freedom**
(alongside census gauge status, fiducial center, and the
$a^3\leftrightarrow R_h^3$ volume convention — WP7 §13), with this
addendum's §3 decision recorded as the *declared default*, not a
closed-off fact.

**Sharpening, verified**: the facet is bounded harder than generic. Since
the coupling under the local-$c$ alternative goes as $(p_i-\tfrac52)
\,\delta c/c$ per species, **matter is exactly immune** ($p_m=\tfrac52$
— the identical cancellation that zeroes $g_\text{matter}$'s $\dot c/c$
term on the background); only radiation-class censuses ($p-\tfrac52=
-\tfrac32$) can feel it. **Consequence for WP7**: the matter-era
low-$\ell$ structure is convention-free on facet 4 — this freedom
touches only the radiation-era/crossover end of the term, exactly where
the matter-era CMB physics does *not* live. A third untouchable item
joins the freedom's two physical anchors (§6's $k\to0$ continuity, WP5's
sub-horizon decoupling): matter-census invariance under facet 4.
Nothing in `cdot-7/` was touched.
