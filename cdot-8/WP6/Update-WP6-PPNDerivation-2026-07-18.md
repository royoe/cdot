# Update — WP6 Sub-task 2: The Full Covariant-Action PPN Derivation, Staged

*Companion: `SessionLog-2026-07-18.md`. Spun off from
`Update-WP6-TensorSpeedStructure-2026-07-18.md` §5d, where the attempt to
reuse Foster-Jacobson's existing $\alpha_1$ formula was found to fail
(their formula couples the spin-0 and spin-1 aether sectors together, so
AeST's regularized/healthy pieces can't simply be substituted in) — the
actual derivation needs to be redone from AeST's own covariant action,
following Foster-Jacobson's method but with the added scalar $\phi$.
Staged explicitly, per the author's instruction, rather than attempted in
one pass — mirroring WP3's own multi-round action-closure precedent.
Every result here inherits Gate 1(b)'s provisional-failure caveat on the
cosmological background.*

---

## Step 1 — The cross-paper sign/normalization dictionary, pinned down

**Why this comes first**: the advisor's own pre-registration flagged "the
$c_1\leftrightarrow K_B$ normalization... still unpinned" as needing
resolution before any number is quoted. Getting this wrong would corrupt
every downstream step, so it's worth doing carefully before anything
else, using the now-archived primary sources directly (`references/
arXiv.gr-qc.0509083`, `references/arXiv.2109.13287`) rather than
recollection.

**Checked the two papers' conventions side by side.** Both explicitly
cite Wald's curvature conventions (Foster-Jacobson: "we will follow the
conventions of [Wald]"; SZ: "curvature conventions of Wald") — removing
one whole axis of possible discrepancy (Riemann/Ricci sign convention).
They differ only in metric signature: Foster-Jacobson use $(+,-,-,-)$,
SZ/AeST use $(-,+,+,+)$.

**Worked out how each term transforms under this signature flip** ($g_{
\mu\nu}\to-g_{\mu\nu}$, a relabeling, not a physical transformation):
Christoffel symbols are invariant (the two sign flips inside $\Gamma=
\frac12g^{-1}\partial g$ cancel), hence the Riemann and Ricci *tensors*
are invariant, but the Ricci *scalar* $R=g^{\mu\nu}R_{\mu\nu}$ — one
explicit inverse-metric contraction — flips sign. The vector kinetic
terms ($c_1,c_2,c_3,c_4$-structures, and AeST's $F^{\mu\nu}F_{\mu\nu}$)
each have an *even* number of explicit metric contractions (rank-2
objects contracted with themselves), so they do **not** flip sign.

**Consequence**: Foster-Jacobson's action $S=-\frac1{16\pi G}\int\sqrt{-g}
\{R+K^{ab}_{mn}\nabla_au^m\nabla_bu^n+\lambda(u^2-1)\}$ (their own
prefactor, confirmed against the archived source, line 151), translated
to AeST's signature, becomes $\frac1{16\pi G}\int\sqrt{-g}\{R-K^{ab}_{mn}
\nabla_au^m\nabla_bu^n-\lambda(u^2-1)\}$ — matching SZ's own action
($\frac1{16\pi\tilde G}\int\{R-2\Lambda-\frac{K_B}2F^2+\ldots-\lambda
(A^2+1)\}$) term-for-term, **with the same overall prefactor** ($G
\leftrightarrow\tilde G$, the bare gravitational coupling, not the
renormalized Newton's constant either theory separately derives).

**Matching the vector kinetic term specifically**: $F^{\mu\nu}F_{\mu\nu}
=2[(\nabla_\mu A_\nu\nabla^\mu A^\nu)-(\nabla_\mu A_\nu\nabla^\nu A^\mu)]$
— built only from the $c_1$-structure ($g^{ab}g_{mn}$) and $c_3$-structure
($\delta^a_n\delta^b_m$) in Foster-Jacobson's basis, with coefficient
ratio exactly $+1:-1$. Matching $\frac{K_B}2F^2=K_B[(c_1\text{-str})-
(c_3\text{-str})]$ against $-K^{ab}_{mn}\nabla u\nabla u$ (the sign found
above) gives, **exactly, not just proportionally**:
$$\boxed{c_1=K_B,\quad c_2=0,\quad c_3=-K_B,\quad c_4=0}$$

**Confidence, stated plainly**: the logical steps (Wald conventions on
both sides; Christoffel/Ricci-tensor invariance under signature flip;
Ricci-scalar sign flip; even-vs-odd metric-contraction counting for the
vector terms) are each individually standard and low-risk, and I checked
them by explicit reasoning rather than by analogy. But this is exactly
the class of cross-convention matching that has produced real errors
elsewhere this session (WP4b's normalization saga) — recording this as
**high confidence, not certainty**, and flagging it as worth a second,
independent check before it's used to quote a final numerical bound,
consistent with the advisor's own caution about this exact step.

**What this resolves**: the previously-"unpinned" normalization is now
pinned, not just estimated — $c_1=K_B$ exactly, with no unknown
proportionality constant. Combined with §5c/§5d's findings this session
($c_{13}=0$ giving exact $c_\text{gw}=c_\gamma$; $c_{123}=0$ giving the
degenerate, $\phi$-replaced spin-0 mode; the healthy $c_1=K_B$-normalized
spin-1 mode with speed$^2=1$, energy $\propto2K_B$), AeST's aether sector
is now **fully characterized** in Foster-Jacobson's own language, with
every relevant combination evaluated.

## Step 1a — Cross-checked and corrected; endgame now explicit

`Advisory-WP6-DictionaryCrossCheck-2026-07-18.md` +
`dictionary_crosscheck.py`, saved to `WP6/advisory/`. **Reproduced the
whole script myself before accepting anything.**

**One real correction, accepted**: my blanket claim ("each vector-kinetic
term has an even number of explicit metric contractions") is false for
the $c_4$-structure. Checked this myself directly: $c_4u^au^bg_{mn}
\nabla_au^m\nabla_bu^n$ contracts $a,b$ directly against $u^a,u^b$ (a
metric-free contraction, since $\nabla_au^m$ is a mixed (1,1) tensor and
$u^a$ is upper-index by definition) — leaving exactly **one** explicit
$g_{mn}$ to close the $m,n$ contraction. Odd count — this term **flips
sign** under the signature relabeling, unlike $c_1,c_2,c_3$ (checked
similarly: 2, 0, and 0 explicit metrics respectively, all even). Harmless
to the boxed result today ($c_4=0$ for AeST's pure-Maxwell term either
way), but the dictionary must now carry $c_4^{\text{FJ}}\leftrightarrow
-c_4^{(-+++)}$ into Step 2, since a $\phi$-completion could plausibly
induce effective $u^au^b$-type terms whose matching would otherwise
inherit a silent sign error.

**Independent physical cross-check, not just a re-audit of the same
reasoning**: fed the dictionary into Foster-Jacobson's own mode-speed
formulas — spin-1 speed$^2\to1$ exactly (matching my own §5d result,
derived independently in SZ's own mostly-plus convention) and the spin-0
speed$^2$ numerator $c_{123}(2-c_{14})\to0$ (matching the $\phi$-replaced
non-dynamical aether scalar). Mode speeds are physical, convention-
independent quantities — agreement here validates the dictionary
end-to-end, not just its derivation steps. This discharges the "worth an
independent second check" flag from Step 1.

**Endgame made explicit, verified**: with $c_{14}=K_B$ exact, the general
identity $\alpha_1=-4c_{14}$ (already proven for any $c_{13}=0$ theory,
§5d) gives the æther-only limit $\alpha_1=-4K_B$. **Checked the quoted
pulsar-class bound $|\alpha_1|\lesssim10^{-5}$ against current
literature** (not just the archived 2006 paper, which quotes a looser
$\lesssim10^{-4}$ from lunar laser ranging alone) — confirmed via live
search: LLR gives $\alpha_1=(-7\pm9)\times10^{-5}$, while binary-pulsar
constraints tighten this by roughly an order of magnitude to $|\alpha_1|
\lesssim10^{-5}$. The $10^{-5}$ figure is real and current, giving
$K_B\lesssim2.5\times10^{-6}$ *if* the leading æther-only form survives
the $\phi$-completion — which is precisely Step 2/3's job to determine,
not assumed here. Noted, not asserted as final: the $K_B\to0$ corner this
would imply is benign for everything already built this session ($\mu_
\text{eff}$ sits at the already-quoted band's own endpoint; $m_\times\to
\infty$ dissolves the two-quasistatic-limit question by parameter squeeze
rather than by argument; the spin-1 sector simply decouples; SZ stability
holds smoothly as $K_B\to0^+$) — consequences-if-the-squeeze-lands, not
claims, exactly as the advisory frames it.

**Guidance adopted for Step 2**: solve the $\delta\phi/A_\parallel$
sector in the $U_i$ (equivalently $\chi=\varphi+Q_0\alpha$) variable
established in the fork-resolution round, not in raw $(\delta\phi,A_i)$
components — solving in the raw variables would reproduce vanilla
æther's spurious inversion of a non-existent mode, the same artifact
already diagnosed in §5c.

## Step 2 — The general covariant $\phi$ field equation, derived and cross-checked against two already-established results

**Goal**: before attempting the O(1.5)/momentum-flux perturbative
expansion (Step 3), get the *general*, unperturbed $\phi$ field equation
right — none of the archived sources write it down explicitly (SZ's
stability paper works directly in the linearized Minkowski expansion;
Mistele's paper starts from the already-reduced static action), so this
is a genuine derivation, not a lookup.

**Varied the action's $\phi$-dependent piece** ($2(2-K_B)J^\mu\nabla_\mu
\phi-(2-K_B)\mathcal Y-\mathcal F(\mathcal Y,\mathcal Q)$, with $J^\mu=
A^\nu\nabla_\nu A^\mu$ independent of $\phi$) with respect to $\nabla_\mu
\phi$ (standard Euler-Lagrange for a Lagrangian depending only on
gradients, not $\phi$ itself), defining $U^\mu\equiv(g^{\mu\nu}+A^\mu
A^\nu)\nabla_\nu\phi$ (the covariant generalization of Mistele's static
$U=\nabla\varphi+Q_0\vec A$). Result:
$$\nabla_\mu\Big\{2(2-K_B)J^\mu-2\big[(2-K_B)+F_Y\big]U^\mu+F_QA^\mu\Big\}=0$$
where $F_Y\equiv\partial\mathcal F/\partial\mathcal Y$, $F_Q\equiv
\partial\mathcal F/\partial\mathcal Q$. **Checked the quadratic-in-
gradient bookkeeping symbolically** (sympy) before trusting the factor of
2 on the $U^\mu$ term — confirmed against the standard $d(g^{ab}X_aX_b)/
dX_c=2g^{cb}X_b$ identity.

**Cross-check 1 — the cosmological background**: on flat FRW ($A^\mu=
(1,0,0,0)$, $\phi=\bar\phi(t)$), $\mathcal Y\to0$ and $J^\mu\to0$
($A^\mu$ is exactly geodesic/aligned, no acceleration), so $U^\mu\to0$
identically too (the projector kills the purely-time gradient). The
equation collapses to $\nabla_\mu(F_QA^\mu)=0$, and on flat FRW ($\sqrt{-g}
=a^3$) this is exactly $\frac{d}{dt}(a^3F_Q)=0$ — **the identical free
shift-current conservation law already established and repeatedly
verified in WP3** (`Update-WP3-ActionLevelAttempt-2026-07-12.md` and
every round descending from it). This is a genuine, independent
confirmation: the general covariant equation derived here reproduces an
already-validated result as an exact special case, not by construction.

**Cross-check 2 — the static quasistatic limit**: for a static aether
tilt $A^i(x)$ (no time dependence) and $\phi=Q_0t+\varphi(x)$, $J^\mu\to0$
again (no acceleration for a genuinely static configuration — consistent
with this term's absence from Mistele's static action, not an
inconsistency), and direct evaluation of the projector gives $U^i=
(g^{ij}+A^iA^j)\nabla_j\phi\to\partial_i\varphi+Q_0A^i$ to linear order —
**exactly Mistele's own $U\equiv\nabla\varphi+Q_0\vec A$** (Eq. 2 of
arXiv:2305.07742, archived). The leading spatial-divergence structure of
the equation, $\nabla_i\{[(2-K_B)+F_Y]U^i\}\approx0$ (matter/$\Phi$-cross
terms aside), matches the AQUAL-type $\nabla\cdot[\mu(|U|)\vec U]$
structure already used throughout WP5. **Two independent, non-trivial
checks passed** — this general equation is now trusted for the
perturbative expansion.

## Step 2a — A structural clarification from Mistele's own paper that reshapes Step 3

Before perturbing to $O(1.5)$, went back to Mistele's paper (already
archived) for its own treatment of $\vec A$ directly, rather than assume
the fork-resolution round's rank-1 structure was the whole story.
**Found something load-bearing, quoted precisely rather than
paraphrased**: Mistele shows explicitly that setting $\vec A=0$ is
*inconsistent in general* (only valid in special cases like spherical
symmetry) — but **the inconsistency is entirely in $\vec A$'s *curl*
part.** Via a Helmholtz split $\vec A=\nabla\alpha_A+\nabla\times\vec
\beta_A$, the *gradient* part $\nabla\alpha_A$ is shown to be exactly
gauge-equivalent to zero — absorbable into $\nabla\varphi$ via $\chi
\equiv\varphi+Q_0\alpha_A$ — while the curl part $\vec\beta_A$ is
genuinely independent and cannot be removed for non-spherically-
symmetric sources. **This confirms, from an entirely different angle,
the fork-resolution round's rank-1 finding**: only one combination of
$\delta\phi$ and $A$'s longitudinal part is dynamical (here: $\chi$,
there: $U_i$) — the same fact, reached independently by Mistele from the
gauge/symmetry side and by the direct $\mathcal Y$-expansion here.

**Also extracted Mistele's own static $\vec A$ equation of motion (their
Eq. Aeom), quoted exactly**:
$$\vec\nabla\Phi-\frac1{2m_\times^2}\vec\nabla\times\vec\nabla\times(Q_0
\vec A)=(\vec\nabla\varphi+Q_0\vec A)\Big(1+\tilde\mu\big(|\vec\nabla
\varphi+Q_0\vec A|/a_0\big)\Big),$$
and the $A=0$ matter-sourced equations (their Eq. eomA0): $\Delta\hat\Phi
=f_G\cdot4\pi G_N(\rho_b+\rho_c)$, $\nabla\cdot[\tilde\mu(|\nabla\varphi|/
a_0)\nabla\varphi]=f_G\cdot4\pi G_N(\rho_b+\rho_c)$ — consistent with,
and a useful independent anchor for, Step 2's general $\phi$ equation
once the matter coupling is restored.

**What this means for Step 3, concretely**: the momentum-flux/PPN
calculation is specifically about the **curl part of $\vec A$** —
$\vec\beta_A$ — since that's the piece with genuine independent
dynamics (the gradient part is redundant with $\chi$/$\varphi$, already
covered by Step 2's equation). This is *exactly* the same object as
vanilla æther's own $u^i$: sourced by non-spherically-symmetric
(rotating/moving) configurations, healthy (§5d's confirmed spin-1 mode,
speed$^2=1$, energy $\propto2K_B$), and — critically — **only this piece
inherits Foster-Jacobson's $u^i$ machinery directly; the gradient/$\chi$
piece must use Step 2's own equation, not FJ's aether-alone one**, which
is exactly why FJ's $\alpha_1$ formula (mixing both pieces together, §5d)
can't simply be reused. Step 3 now has a clear target: solve $\vec\beta_A$
sourced by the momentum-flux term in Eq. Aeom's generalization, and
$\chi$ sourced by Step 2's equation, separately, then combine for
$g_{0i}$.

## Step 3a — The divergence located precisely, in Foster-Jacobson's own $g_{0i}$ field equation, not just in an intermediate step

Went back to the archived source for FJ's *full* $O(1.5)$ derivation
(their $u^i$ solution §, then their $g_{0i}$ field equation §), rather
than work from their summarized final formula, since §5d already showed
that formula mixes sectors non-separably.

**Their exact $g_{0i}$ field equation** (quoted, not paraphrased):
$$\Big(1-\frac{c_-c_+}{2c_1}\Big)h_{0i,jj}=16\pi G\rho v_i+\Big(E+A\theta
-\tfrac12\Big)\chi_{,0ijj},$$
with $c_-=c_1-c_3$, $c_+=c_{13}=c_1+c_3$, $A=-\frac{2c_1+3c_2+c_3+c_4}
{2c_{123}}$ (the same $A$ whose $c_{123}$-denominator makes the theory's
own $u^i$ solution singular), $\theta$ the gauge parameter, and $E=
\frac1{4c_1}(c_1^2+3c_3^2+4c_1c_4-2c_-c_+A\theta)$. (Note: FJ's own
$\chi$ here is their PPN *superpotential*, $\chi=-G_N\int\rho|x-y|$ — an
unfortunate name collision with AeST's $\chi=\varphi+Q_0\alpha_A$; kept
distinct throughout, not conflated.)

**Evaluated every piece at AeST's point ($c_1=K_B,c_2=c_4=0,c_3=-K_B$),
checked symbolically**: $c_-=2K_B$, $c_+=c_{13}=0$ — and this single
fact is doing real work. The $h_{0i,jj}$ prefactor becomes $1-\frac{c_-c_+}
{2c_1}=1-0=\mathbf1$ **exactly** — the standard GR gravito-magnetic
normalization, entirely unmodified, no $K_B$-dependence at all. Inside
$E$, the one $A$-dependent piece ($-2c_-c_+A\theta$) is **automatically
killed by $c_+=0$, regardless of $A$'s own divergence** — giving $E=K_B$,
finite. $\theta=K_B/(2-K_B)$, also finite. **But the equation's own bare
$A\theta$ term is not multiplied by $c_+$, so it is not protected the
same way** — $A\to\infty$ (finite nonzero numerator over $c_{123}=0$)
while $\theta$ stays finite and nonzero, so $A\theta\to\infty$.

**This precisely localizes the entire remaining divergence to one
specific term** — the bare $A\theta$ inside the source-term coefficient
$(E+A\theta-\tfrac12)$ multiplying $\chi_{,0ijj}$ (the matter
superpotential's own gradient, not the metric) — not the $h_{0i,jj}$
normalization (exactly 1, clean), not $E$ (finite), not $\theta$ itself
(finite). **The remaining task is now sharply, concretely defined**:
derive AeST's new source contribution to this same equation (from
varying the $\phi$-coupling terms — $2(2-K_B)J^\mu\nabla_\mu\phi-(2-K_B)
\mathcal Y-\mathcal F(\mathcal Y,\mathcal Q)$ — with respect to $A^i$)
and show it cancels the bare $A\theta$ divergence, replacing it with a
finite, $\phi$-completed coefficient. **Attempted this variation directly
this round** (Euler-Lagrange on the $\mathcal Y,\mathcal Q$-dependent
pieces w.r.t. $A^\mu$, using $\mathcal Y=|\nabla\phi|^2_g+\mathcal Q^2$
as a cleaner equivalent form) but did **not** complete a fully-verified
result — the $J^\mu\nabla_\mu\phi$ term's variation requires an
integration-by-parts step with several index-contraction terms, and I
do not yet have an independent check (analogous to Step 2's two
cross-checks) to certify it before reporting a number. Flagging this
honestly rather than presenting a partially-verified multi-term tensor
result as settled.

## Step 3 — What comes next (not yet done), now sharpened by Step 2a

Per §2a, Step 3 splits cleanly into two coupled but separately-tractable
pieces rather than one monolithic system: **(i)** the curl part
$\vec\beta_A$, which is the genuine analog of Foster-Jacobson's own
$u^i$ — sourced by the momentum-flux ($\rho v^i$) generalization of
Eq. Aeom's right-hand side, and expected to inherit their $O(1.5)$
machinery close to directly, using AeST's own $(c_1,c_3)=(K_B,-K_B)$
values (§5d's confirmed-healthy spin-1 sector); **(ii)** the $\chi$
(equivalently $U_i$) piece, governed by Step 2's own general covariant
equation (not FJ's aether-alone one), which must be perturbed to the same
order for its own momentum-flux response. Both then feed the $g_{0i}$
Einstein equation together. This is more tractable than treating
$(\delta\phi,A_i)$ as one coupled 2-component system from scratch, since
the two pieces are now known to decouple structurally (rank-1 finding,
independently confirmed by Mistele's gauge argument) — but actually
carrying out the $O(1.5)$ perturbation of each piece, and combining them
correctly in the $g_{0i}$ equation, is still the substantial remaining
work, not yet attempted.

With the dictionary pinned, the broader remaining task is: extend
Foster-Jacobson's own field equations (their $S_{ab}$, aether field
equation, both quoted verbatim and archived in `references/
arXiv.gr-qc.0509083`) with AeST's additional scalar-sector terms ($2(2-K_B)
J^\mu\nabla_\mu\phi-(2-K_B)\mathcal Y-\mathcal F(\mathcal Y,\mathcal Q)$),
then re-run their exact 6-step solving procedure (constraint for $u^0$;
$g_{00}$ at $O(1)$; $g_{ij}$ at $O(1)$; the aether+scalar equations for
$u^i$ jointly with $\delta\phi$ at $O(1.5)$; $g_{0i}$ at $O(1.5)$; $g_{00}$
at $O(2)$) — using their own order-counting convention (confirmed from
the archived source: $\rho,\Pi,p/\rho,v^2\sim O(1)$; $h_{00}\sim O(1)+
O(2)$, $h_{ij}\sim O(1)$, $h_{0i}\sim O(1.5)$; $\delta u^0\sim O(1)$,
$\delta u^i\sim O(1.5)$; $\partial_t$ raises order by $\tfrac12$) rather
than a bespoke scheme of my own. This is Step 3 onward — not attempted
in this pass. Recording the plan explicitly so the next installment
starts from a stated target rather than an open-ended one.

## Step 3b — Attempted the cancellation; found a problem with the strategy itself, not just an unverified term

Completed the variation flagged as incomplete in §3a: the new source
term AeST's $\phi$-coupling adds to the aether field equation, from
varying $2(2-K_B)J^\mu\nabla_\mu\phi-(2-K_B)\mathcal Y-\mathcal F(
\mathcal Y,\mathcal Q)$ with respect to $A^\mu$ (treating $A^\nu$ and
$\nabla_\beta A^\alpha$ as independent variables for the partial
derivatives, standard field-theory practice, then integrating by parts).
**Re-derived it a second way** (direct functional-derivative bookkeeping,
not just re-reading the same algebra) and got the same result both
times:
$$\Delta_\alpha=2(2-K_B)\Big[2(\nabla_\alpha A^\mu)(\nabla_\mu\phi)-
(\nabla_\beta A^\beta)\nabla_\alpha\phi-\nabla_\alpha\mathcal Q\Big]-
\Big\{2\mathcal Q\big[(2-K_B)+F_Y\big]+F_Q\Big\}\nabla_\alpha\phi.$$
Getting the same answer twice by the same method checks the algebra, not
the physics — so I tried to verify it against Mistele's static Eq. Aeom,
the same way Step 2 was checked twice against independent results.

**Found something that isn't a missing check — it's a problem with the
whole strategy.** At leading static order (where $A^i$ and $\nabla\varphi$
are both "first order," so their products are second order and drop,
and $\mathcal Q\approx Q_0$ is a true constant so $\nabla_\alpha\mathcal
Q\to0$), $\Delta_i$ reduces to a term proportional to $\nabla_i\varphi$
**alone** — not to the full $U_i=\nabla_i\varphi+Q_0A_i$ that Mistele's
equation is built around. Tracing *why*: **Foster-Jacobson's entire
$O(1.5)$-only scheme for $\delta u^i$ is a proven fact about *vanilla*
æther specifically** — their own text states lower orders are
"disallowed by the field equations, given the above orders of $h_{ab}$"
for their theory. **That proof does not carry over to AeST.** Mistele's
own static analysis (§2a) shows AeST's $A^i$ (or at least its
longitudinal part, via $\chi$) genuinely has *leading*-order,
non-momentum-flux content — sourced by ordinary MOND physics, present
even for a perfectly static configuration. Directly grafting
Foster-Jacobson's "$\delta u^i\sim O(1.5)$ only" order scheme onto AeST
silently assumes away exactly the physics that makes AeST's aether
different from vanilla aether in the first place.

**This means Step 3 as planned — extend FJ's field equations, reuse
their order-counting, solve — rests on a false premise for AeST.** What's
actually needed is a genuine **two-scale expansion**: $\chi$ (or $U_i$)
must carry *both* a leading, static, MOND-order piece (already implicit
in Mistele's/WP5's work) *and* a subleading, momentum-flux-order
correction on top of it — and the O(1.5) PPN calculation is about that
*correction*, not about $U_i$ from scratch the way vanilla aether's
$u^i$ is. This is a real, structural finding, not a gap in verification —
and it is a substantially different (and harder) calculation than "add
new terms to FJ's equations and re-run their steps."

**Not resolved in this pass.** Given the depth of this — it changes the
shape of the whole remaining derivation, not just one term in it — this
is exactly the kind of finding this program has, throughout, chosen to
escalate or checkpoint rather than push through alone under time
pressure (WP3's several genuine mid-course corrections are the direct
precedent). Recommending a explicit pause here: either a dedicated,
careful re-planning of the two-scale expansion (real, further work, not
a quick fix), or a touch point given the stakes of building further on a
strategy just found to rest on an unexamined assumption.

## Status

**Step 1 is fully verified** (independent physical cross-check, one
correction absorbed — $c_4$'s sign under the signature flip). **Step 2
is done**: the general covariant $\phi$ field equation is derived and
passes two independent, non-trivial checks (the exact background
$\frac{d}{dt}(a^3F_Q)=0$ conservation law from WP3; Mistele's exact
static $U=\nabla\varphi+Q_0\vec A$ structure). **Step 2a adds a real
structural clarification**, found directly in Mistele's own paper rather
than assumed: only $\vec A$'s *curl* part is independently dynamical
(its gradient part is gauge-equivalent to zero, absorbed into $\chi$) —
confirming the fork-resolution round's rank-1 finding from a completely
different angle, and giving Step 3 a cleaner two-piece target (the curl
part as FJ's own $u^i$-analog; the $\chi$ part via Step 2's equation)
rather than one undifferentiated coupled system. The endgame remains
explicit from Step 1a: æther-only $\alpha_1=-4K_B$, giving $K_B\lesssim
2.5\times10^{-6}$ under a current, verified pulsar-class bound — *if*
this leading form survives the $\phi$-completion, which is exactly what
Step 3 must determine. **Step 3** (perturbing both pieces to $O(1.5)$
and combining in the $g_{0i}$ equation, following Foster-Jacobson's exact
order counting) is scoped, sharpened, but not started — genuine
remaining work, staged deliberately rather than compressed into this
pass. Every result here inherits Gate 1(b)'s caveat. Nothing in
`cdot-7/` was touched.

**Step 3a sharpens this further, precisely**: the entire remaining
divergence in FJ's own $g_{0i}$ field equation, evaluated at AeST's
point, localizes to one bare term ($A\theta$) in the source coefficient —
the $h_{0i,jj}$ normalization is exactly 1 (unmodified GR), and $E$ is
separately finite (its own $A$-dependence killed by $c_+=0$ automatically).
The remaining task is now a single, well-defined cancellation to
demonstrate: does AeST's $\phi$-sourced contribution to this same
equation exactly cancel the bare $A\theta$ divergence? Attempted the
underlying variation (the $\mathcal Y,\mathcal Q$-term EOM contribution
w.r.t. $A^\mu$) but did not complete a certified result this round — the
$J^\mu\nabla_\mu\phi$ term's variation has several index-contraction
terms and lacks an independent cross-check so far, unlike Step 2's
equation. Honestly incomplete, not asserted as done.

**Step 3b completed the variation, then found a structural problem with
the strategy itself, not just a missing check**: Foster-Jacobson's
$\delta u^i\sim O(1.5)$-only scheme is a proven fact specific to vanilla
æther, which does not carry over to AeST — Mistele's own static analysis
shows AeST's $A^i$/$\chi$ genuinely has leading, non-momentum-flux
content that vanilla æther's $u^i$ simply doesn't have. Directly
grafting FJ's order scheme onto AeST assumes away exactly this
difference. **The actual fix is a two-scale expansion** (a leading
static/MOND piece plus a subleading momentum-flux correction on
$U_i/\chi$), a materially different and harder calculation than "extend
FJ's equations and reuse their steps." **Recommending an explicit pause
for re-planning or a touch point** before continuing, given this changes
the shape of the remaining derivation, not just one term in it —
consistent with how this program has handled comparable mid-course
structural corrections in WP3.

**Housekeeping note**: this advisory round again requests the
consolidation/errata batch, apparently unaware it was already delivered
in the immediately preceding round (`ConsolidationLog-2026-07-12.md`
Items 11–15; `ErrataAndMethodologyLog-2026-07-18.md`) — most likely a
sync-timing gap (the advisor loop hasn't yet picked up that delivery),
not a real second gap. Noting explicitly so it isn't redelivered
needlessly: the batch is done; only this round's small addition (the
$c_4$ sign-flip dictionary entry) is new and worth folding in whenever
the next sync happens.

## Step 3c — Two corrections accepted, one independently re-verified by hand; the pause resolves to a controlled refinement, not a collapse

`Advisory-WP6-Step3bAdjudicated-2026-07-18.md` +
`step3b_crosscheck.py`, saved to `WP6/advisory/`. **Reproduced the script
and independently re-derived the load-bearing piece by hand before
accepting anything.**

**Correction 1, accepted — a real sign error, genuinely mine**: the
$\phi$-current's $F_Q$ term should be $-F_QA^\mu$ (from $\partial(-
\mathcal F)/\partial(\nabla_\mu\phi)\ni-F_Q\partial\mathcal Q/\partial(
\nabla_\mu\phi)=-F_QA^\mu$), not the $+F_QA^\mu$ Step 2 reported. **The
methodological point is worth keeping regardless of the specific
error**: both of my own cross-checks were structurally blind to this
term's sign — the FRW check reduces to a conservation law, insensitive
to its current's overall sign; the static check never exercises $F_Q$
since AeST sits at (or near) $F_Q(Q_0)=0$ in the regimes those checks
covered. **A passed check only certifies the terms it actually
exercises** — new K6 entry, earned the hard way, in the same round it
mattered.

**Correction 2, accepted after independent hand-verification, not just
reproduction**: the §3b "mismatch" (my $\Delta_i\propto\nabla_i\varphi$
alone vs. Mistele's full $U_i$) is an apples-to-oranges comparison, not
evidence of a broken strategy. My variation held all four $A^\mu$
components independent (correct for the Lagrange-multiplier method), but
Mistele's equation is already-reduced, with $A^0$ eliminated via the unit
constraint. **Worked the missing chain-rule term through myself**: from
$g_{\mu\nu}A^\mu A^\nu=-1$, $\partial A^0/\partial A^i\approx A_i$; from
$\mathcal Y=\mathcal Q^2+|\nabla\phi|^2_g$, $\partial\mathcal Y/\partial
A^0\approx2Q_0^2$ at leading order — giving exactly $\partial\mathcal Y/
\partial A^i\big|_\text{total}=2Q_0\partial_i\varphi+2Q_0^2A_i=2Q_0U_i$,
matching Mistele's structure precisely once this constraint-elimination
piece is included. Confirmed both by hand and by reproducing the script.
**This resolves the specific static-limit mismatch cleanly** — it was
missing bookkeeping, not a wrong equation.

**What survives, correctly not dismissed**: the order-counting caveat
itself is real — Foster-Jacobson's $\delta u^i\sim O(1.5)$-only scheme is
proven for vanilla æther specifically (static $u^i=0$ exactly there) and
does not hold for AeST, which genuinely has static $A^i$/$\chi$ content.
**But its severity is bounded, not open-ended**: in every actual PPN
environment (solar system $x\sim10^8$, pulsars $x\sim10^{12}$), that
static content is screening-suppressed — $U\sim\nabla\Phi/\tilde\mu_
\text{screened}$, a small parameter $\varepsilon=1/\tilde\mu_\text{screened}$
already implicit in sub-task 1's Cassini-safe completion and Cassini-
capped from above. **The "two-scale expansion" I worried about is just
the (PPN order)$\times\varepsilon$ double expansion already implicit in
the program's own results** — at $\varepsilon^0$, Foster-Jacobson's
counting is recovered outright (curl sector via their machinery at
$(K_B,-K_B)$; $\chi$ at its screened, suppressed magnitude); the
$O(\varepsilon)$ terms are the corrections already registered in the
fork-resolution round.

**Accepted: the pause is answered, not overridden.** This isn't "push
through despite the concern" — the concern was investigated, partly
correct (the order-scheme caveat is real) and partly a bookkeeping gap
(the static mismatch), and the surviving real part turns out to be
controlled by physics already established (screening), not open-ended.
Proceeding on the two-piece plan (curl sector via FJ machinery; $\chi$
via Step 2's corrected equation) with three carried requirements: the
$F_Q$ sign fixed; the $\lambda$/$A^0$ constraint force made explicit,
not implicit; every $\varepsilon$-truncation stated where made.

## Step 3d — The transverse (curl) sector solved exactly: clean GR, zero PPN content — all of $\alpha_1,\alpha_2$ lives in the longitudinal/$\chi$ channel

**Executed the curl-sector half of the two-piece plan.** Foster-
Jacobson's own $O(1.5)$ aether equation (AEQI, archived) splits cleanly
under a transverse/longitudinal projection *before* any AeST-specific
input is needed: the $\chi_{,i0}$ term (FJ's superpotential $\chi$,
still distinct from AeST's) is a pure gradient of a scalar — purely
longitudinal, zero transverse part, by construction — while the
remaining bracket is acted on only by $\nabla^2$, which preserves
transverse/longitudinal character. **The transverse projection therefore
drops the singular term entirely, before evaluating anything at AeST's
point**:
$$\big(c_1n_i^T+\tfrac{c_-}2h_{0i}^T\big)_{,jj}=0\ \Rightarrow\
u_i^T=\frac{c_-}{2c_1}h_{0i}^T,$$
which at AeST's values ($c_-=2K_B,c_1=K_B$) gives $u_i^T=h_{0i}^T$ —
finite, and not even $K_B$-dependent.

**Checked the same projection on FJ's $g_{0i}$ field equation** (already
quoted in §3a): the $\chi_{,0ijj}$ source term is likewise pure gradient
— zero transverse part regardless of its own $(E+A\theta-\tfrac12)$
coefficient. **The transverse equation is therefore exactly**:
$$h_{0i,jj}^T=16\pi G\rho v_i^T$$
— the $h_{0i,jj}$ prefactor is already 1 (§3a, from $c_{13}=0$), and
there is no $A\theta$, no $K_B$, no AeST-specific content anywhere in
this projection. **The transverse/curl sector of $g_{0i}$ is exactly
GR**, consistent with (and now shown to extend) the already-established
$c_{gw}=c_\gamma$ and $\gamma=1$ results.

**Consequence, checked not assumed**: since the singular term and every
AeST-specific modification live *entirely* in the longitudinal
projection, **the transverse sector contributes nothing to $\alpha_1,
\alpha_2$ at all** — the entire preferred-frame signal in cdot-8 must
come from the longitudinal/$\chi$ channel alone. This is a genuine
structural simplification: the two-piece plan doesn't need to combine a
modified-transverse and modified-longitudinal piece; only the
longitudinal piece carries any AeST content whatsoever.

**What remains**: the longitudinal $g_{0i}$ equation, sourced by the
longitudinal part of $\rho v_i$ (related to $\partial_t\rho$ via the
continuity equation, the standard PPN $V_i$-vs-$W_i$ split), with the
singular $A\theta$ coefficient replaced by AeST's $\chi$-completed
response — a genuine matter-sourced, momentum-flux-order extension of
Mistele's static $\nabla\Phi=U(1+\tilde\mu)$ relation (Eq. eomA0), not
yet derived. Given sub-task 1 established that $U$ itself is screening-
suppressed ($U\sim\nabla\Phi/\tilde\mu_\text{screened}$, small,
$O(\varepsilon)$) in every real PPN environment, the qualitative
expectation is that this momentum-flux response inherits the same
suppression — meaning the actual $\alpha_1$ may come out considerably
smaller than the naive unscreened æther-only $-4K_B$ estimate, not
merely equal to it. **This is an expectation, explicitly not yet a
derived result** — the actual momentum-flux-order, matter-sourced
longitudinal equation has not been derived, only motivated by analogy to
the static case. Genuine remaining work; not attempted further this
round.

## Step 3e — A parametric estimate for the longitudinal channel, explicitly not a certified derivation

**Attempted the full matter-sourced longitudinal equation** (extending
Mistele's static $\nabla\Phi=U(1+\tilde\mu)$ to the momentum-flux order,
replacing the singular $A\theta$ coefficient). Concluded a fully rigorous
closed-form derivation — solving Step 2's corrected equation for
$\delta U_i$ perturbatively *around the already-nonzero static
background* $U_i^{(0)}$ (screened, small, $O(\varepsilon)$), rather than
around zero as vanilla æther's single-scale expansion does — is a
genuinely harder calculation than anything completed so far in this
arc, and **did not complete it to the same standard as Steps 2–3d**
(no independent cross-check available for a result of this kind).
Recording the reasoning that stops short of a number, rather than
presenting an uncertain result as settled.

**The physical argument, stated as an expectation**: the screening
mechanism that suppresses the *static* $U$ ($U\sim\nabla\Phi/\tilde\mu_
\text{screened}$, established in sub-task 1) is the same effective
"stiffness" that would suppress a *driven* (momentum-flux-sourced)
response of the same field — a large effective kinetic coefficient
generically damps a field's reaction to any source, static or moving.
If this holds (not derived here), the longitudinal channel's
contribution to $\alpha_1$ should carry an *additional* suppression
factor $\sim\varepsilon=1/\tilde\mu_\text{screened}$ on top of whatever
$K_B$-dependence survives — meaning the physical $\alpha_1$ in cdot-8
could sit well below the naive unscreened æther-only estimate ($-4K_B$),
and the pulsar-derived bound on $K_B$ (§1a: $K_B\lesssim2.5\times
10^{-6}$ *if the unscreened form survives*) would relax accordingly,
potentially substantially, since it inherits the same screening that
already protects Cassini/solar-system tests (sub-task 1).

**Status, stated plainly**: this is a physically-motivated expectation,
not a derived result, and should not be quoted as a bound. Closing this
properly needs the actual perturbative solve around the nonzero screened
background — a distinct, harder calculation than a linearization around
zero, and beyond what can be responsibly completed via further hand
derivation without either dedicated additional effort of the same scale
as Steps 1–3d combined, or an independent (e.g. advisor) derivation to
cross-check against, given there is no longer an existing published
result (like Foster-Jacobson's) to lean on for this specific piece.

## Consolidated status of WP6 sub-task 2, this arc

**Solid, independently verified results** (each checked at least twice,
by different methods, before being trusted): the exact sign/normalization
dictionary $c_1=K_B,c_2=0,c_3=-K_B,c_4=0$ (Step 1, cross-checked
end-to-end via physical mode speeds); the general covariant $\phi$
equation, now with its sign corrected (Step 2/3c); the rank-1 $U_i$
structure, confirmed independently from two directions — direct
$\mathcal Y$-expansion and Mistele's own gauge argument (Step 2a); the
precise localization of vanilla æther's divergence to one bare term,
$A\theta$, in the $g_{0i}$ equation (Step 3a); the exact resolution of
the apparent static-limit mismatch via the unit-constraint chain rule
(Step 3c); and the exact, clean solution of the transverse/curl sector,
shown to contribute *nothing* to $\alpha_1,\alpha_2$ (Step 3d) — a real
structural simplification, not an assumption.

**What remains open**: the longitudinal channel's actual momentum-flux
response — the one piece that carries all of cdot-8's PPN preferred-
frame content — is not derived to the standard the rest of this arc has
held to. Step 3e's screening-suppression argument is physically
reasonable but unverified, and should be treated as a hypothesis to test,
not a result to cite.

**Errors caught along the way, for the record**: one in Step 2 (the
$F_Q$ sign, advisor-caught, self-confirmed), one in Step 3b's diagnosis
(advisor-corrected, self-confirmed), and one incorrect claim from an
external fetch caught before use (§5d's vector-mode-speed error). Every
one was caught before being used to assert a final number — the pattern
holding across this entire session.

**Recommendation**: this is a natural point to pause sub-task 2's exact
numerical closure. The qualitative picture — cdot-8's aether sector is
healthy in every mode checked (tensor, spin-1/vector), its one formal
degeneracy (spin-0) is resolved by construction via $\phi$, and its PPN
preferred-frame content is plausibly (not yet certainly) screening-
suppressed on top of whatever $K_B$-dependence survives — is a coherent,
defensible, and genuinely informative result in its own right, distinct
from and short of an exact $\alpha_1$ formula. Closing the gap needs
either substantially more dedicated derivation (comparable in scope to
everything in this document combined) or an independent derivation to
cross-check against, given there is no longer a published result to
lean on. Proceeding to sub-task 3 (binary-pulsar confrontation) with the
qualitative picture stated honestly, or continuing the exact derivation,
is an author call.

**Author decision, 2026-07-18: proceed to sub-task 3 now; sub-task 2's
exact closure flagged as pending the next advisory round, not dropped.**
Sub-task 3 proceeds using everything solid from this arc (the dictionary;
the healthy tensor/vector-mode results; the transverse-sector=GR result;
the qualitative screening-suppression expectation for $\alpha_1$, stated
as an expectation) while carrying forward, explicitly, that the exact
$\alpha_1,\alpha_2$ values remain open. Any binary-pulsar result that
depends on the precise, still-undetermined longitudinal coefficient will
itself be flagged as conditional, not quietly assumed resolved.

## Advisory request, open — sub-task 2's final piece

**What's needed**: the matter-sourced, momentum-flux-order longitudinal
equation for $\chi$ (equivalently $U_i^L$) — the extension of Mistele's
static $\nabla\Phi=U(1+\tilde\mu)$ relation (Eq. eomA0) to $O(1.5)$,
replacing the singular bare $A\theta$ term in Foster-Jacobson's $g_{0i}$
equation (§3a) with AeST's actual, finite response. This is the single
remaining piece needed to convert the qualitative picture already
established into an exact $\alpha_1,\alpha_2$.

**Why solo derivation stopped here**: this requires perturbing Step 2's
corrected equation *around the already-nonzero, screened static
background* $U_i^{(0)}$, not around zero as Foster-Jacobson's single-scale
expansion does for vanilla æther (§3b/§3d) — a harder calculation than
anything completed in this arc, with no independent cross-check available
of the kind that made Steps 1–3d trustworthy.

**What's already available to build on** (no need to re-derive): the
exact dictionary $c_1=K_B,c_2=0,c_3=-K_B,c_4=0$ (Step 1, cross-checked
three ways including via the pulsar-basis resolution); the corrected
general covariant $\phi$ equation (Step 2/3c, $F_Q$ sign fixed); the
rank-1 $U_i=\partial_i\delta\phi+Q_0A^i$ structure (confirmed twice,
independently); the exact, closed transverse-sector solution showing it
contributes nothing to $\alpha_1,\alpha_2$ (Step 3d); Mistele's own
static $\vec A$ equation of motion (§2a) as the $\varepsilon^0$ anchor
the momentum-flux correction should reduce to.

**The specific question**: does the momentum-flux correction to $U_i^{(0)}$
carry the same screening suppression ($\sim\varepsilon=1/\tilde\mu_
\text{screened}$) as the static piece itself (Step 3e's hypothesis), and
if so, what is the resulting $\alpha_1$ in terms of $K_B$ and the
screening completion — or does it not, in which case what does?

## Advisory response — Step 3e confirmed structurally; a directional self-correction accepted; a conservative envelope adopted, one number flagged

`Advisory-WP6-LongitudinalResponse-2026-07-18.md` +
`longitudinal_response.py`, saved to `WP6/advisory/`. **Reproduced the
script and checked the reasoning before accepting.**

**Accepted — Step 3e's hypothesis confirmed at the structural level**:
linearizing Step 2's corrected equation around the screened static
background gives a response operator whose eigenvalues (transverse and
longitudinal to $U^{(0)}$) are *both* large in the screened regime — no
soft direction, and none of the enumerated $O(1.5)$ sources is
$\tilde\mu$-enhanced. So the driven response really does inherit the
static suppression, $\delta U\sim\varepsilon\times O(1.5)$, because it's
the same stiff medium being driven either way. Physically reasonable and
internally consistent; the honest caveat carried with it (operator and
scaling derived, the $O(1)$ coefficient not) is the right level of
confidence to hold.

**Accepted — a genuine, welcome self-correction**: the advisor's *own*
earlier pre-registration ("strong screening recovers $\alpha_1\to
-4c_{14}$") is reversed, correctly. Since Step 3d already proved the
transverse sector is exactly GR at AeST's point, vanilla æ-theory's
$\alpha_1=-4c_1$ at this same point must be carried *entirely* by the
longitudinal channel AeST replaces — so screening doesn't restore that
value, it suppresses the one channel that produced it. Corrected
expectation: $\alpha_1(\text{cdot-8})=O(K_B\varepsilon)$, plus at most
one unsuppressed $O(K_B)$ piece (the "$E$-term," whose derivation
pre-substituted vanilla's now-replaced longitudinal solution) left as
the one remaining certified-derivation item. Recording an advisor's
reversed expectation, not just its errors, is the same ledger discipline
this program has applied to itself throughout.

**Accepted, methodologically — the conservative envelope**: since the
open $E$-term can only restore *at most* the vanilla magnitude under a
stiff operator, $|\alpha_1|\le4K_B$ is a legitimate (if conservative)
bound, not a claimed equality — giving $K_B\lesssim2.5\times10^{-6}$
under the pulsar bound, a number this session already independently
verified against current literature (§1a). **This unblocks sub-task 3
today on an explicitly conditional basis**, exactly the shape requested.

**One number checked and flagged, not silently passed through**: the
"provisional" $\alpha_2$ envelope uses a solar-spin-alignment bound of
$1.6\times10^{-9}$. A live check against the literature found the
commonly-cited value is $\sim2.4\times10^{-7}$ (Nordtvedt's classic
solar spin/orbit alignment argument) — roughly two orders of magnitude
looser than what's used here. This doesn't contradict the advisory's own
framing (already marked "provisional... do not quote as final"), but
gives a concrete reason for that caution beyond the $E$-term dependency:
**the $\alpha_2$-based $K_B\lesssim4\times10^{-10}$ figure should not be
used until the underlying bound itself is verified.** The $\alpha_1$
pulsar-based envelope is unaffected and is what sub-task 3 should
actually lean on for now.

**Status**: sub-task 2 closes, for now, on this conditional, honestly-
scoped basis — $\alpha_1(\text{cdot-8})=O(K_B\varepsilon)$ expected,
$|\alpha_1|\le4K_B$ quotable as a conservative envelope, exact closure
(the $E$-term re-derivation) left as explicit future work ("WP6b" if
ever commissioned). Proceeding to sub-task 3 on this basis.
