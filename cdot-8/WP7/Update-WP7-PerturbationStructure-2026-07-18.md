# Update — WP7: Structural First Installment — Linear Perturbation Machinery Imported, the Genuinely New (Horizon-Scale) Question Posed

*Companion: `SessionLog-2026-07-18.md` (to be created). Proceeds under
Gate 1(b)'s explicit provisional-failure caveat
(`cdot-8/proposal/DecisionGates-2026-07-18.md`): WP4a's 27% crossover-era
$\theta_*$ miss is not resolved, and the author's own sequencing
instruction is to complete the analysis through WP7 on the *current*
radiation-era assumptions before revisiting them — this work does not
presuppose or claim that miss is fixed. Also carries WP6's own standing
items (sub-task 2's exact $\alpha_1,\alpha_2$ closure, flagged future
work) without conflating them with WP7's own scope.*

---

## 1. What's already established in AeST's own literature — import, don't re-derive

Following the rhythm WP5/WP6 established: check what the chassis theory
already provides before deriving anything new. **Read the founding paper
(arXiv:2007.00082, already archived) for its own cosmological
perturbation-theory section** — a full linear system, remarkably compact,
not merely asserted:

Newtonian gauge ($g_{00}=-(1+2\Psi)$, $g_{0i}=0$, $g_{ij}=a^2(1-2\Phi)
\gamma_{ij}$), scalar perturbed as $\phi=\bar\phi+\varphi$, vector as
$A_\mu=\{-1-\Psi,\nabla_i\alpha\}$. Defining $\chi\equiv\varphi+\dot{\bar
\phi}\alpha$, $\gamma\equiv\dot\varphi-\dot{\bar\phi}\Psi$, $\mathcal E_
\alpha\equiv\dot\alpha+\Psi$, and an *effective* density contrast and
velocity divergence
$$\delta\equiv\frac{1+w}{\dot{\bar\phi}c_\text{ad}^2}\gamma+\frac1{8\pi
\tilde Ga^2\bar\rho}\nabla^2\big[K_B\mathcal E_\alpha+(2-K_B)\chi\big],
\qquad\theta\equiv\frac{\varphi}{\dot{\bar\phi}},$$
**the Einstein equations take exactly GR's standard fluid form**
($\delta G^0_0=8\pi G\sum_I\bar\rho_I\delta_I$, etc.), with the scalar-
vector sector folded entirely into one additional "fluid" species obeying
the *same* continuity/Euler equations as ordinary matter, but with a
**nonstandard pressure contrast**
$$\Pi=c_\text{ad}^2\delta-\frac{c_\text{ad}^2}{8\pi\tilde Ga^2\bar\rho}
\nabla^2\big[K_B\mathcal E_\alpha+(2-K_B)\chi\big],$$
and $\mathcal E_\alpha$ obeying its own evolution equation sourced by
$\chi$ and $\frac{dK}{dQ}$. **This is not a dark fluid** (Π doesn't close
under the fluid variables alone — it depends on the vector perturbations
directly) but reduces to one whenever $\Pi\to0$.

**The key simplification the founding paper itself reports**: "for a wide
range of parameters, this... theory is consistent with the CMB
measurements from Planck. This happens because $c_\text{ad}^2$ and $w$
are small enough so that $\Pi\to0$ and we get dustlike evolution" —
$\dot\delta=3\dot\Phi-\frac{k^2}{a^2}\theta$, $\dot\theta=\Psi$, vector
field decoupling entirely. **This is AeST's own native cosmology**
(their free $K(Q)$ function, chosen to mimic dark matter) — explicitly
**not** cdot-8's, which replaces $K(Q)$/$F(Q)$ wholesale with the
census/M5-quadrature result. Whether cdot-8's own $F(Q)$ similarly drives
$\Pi\to0$ is a genuine, open, checkable question — not yet checked here,
flagged for the next installment.

## 2. The genuinely new (cdot-8-specific) question: does M5 disturb the perturbed equations, not just the background?

WP5 and WP6's central structural question, each time, was whether M5's
census/closure constraint — defined (WP2 §1) as a **horizon-wide
foliation integral** $\mathcal N(t)$ — reaches into sectors it wasn't
explicitly built for. Both times the answer was a qualified "no" (WP5's
local-decoupling argument, strengthened by an explicit variational
mechanism; WP6's tensor/vector-mode discharges). **That answer cannot be
assumed to carry over unchanged here.** WP5/WP6 dealt with strictly
*local* physics (solar-system, pulsar scales, $\ll R_h$) where a
horizon-integral quantity's own fluctuations are plausibly negligible —
exactly the argument that made local decoupling work. **Cosmological
perturbations are not local**: the scales relevant to the CMB and matter
power spectrum are a sizable fraction of the horizon, and some (the
lowest CMB multipoles) are *super*-horizon. A quantity literally defined
as an integral over the whole spatial slice is not obviously negligible
in its own perturbation at exactly these scales — the opposite regime
from where WP5's argument was strongest.

**The question, stated precisely, not yet answered**: does $\delta
\mathcal N$ (the perturbation of the horizon-integral census) source a
term in the perturbed Einstein/scalar/vector equations above, beyond
what already enters through the background quantities $\bar\rho$, $w$,
$c_\text{ad}^2$, $F(Q)$ that this system is already written in terms of?
If $\delta\mathcal N=0$ identically (e.g., because $\mathcal N$'s
perturbation integrates to zero by the same shell/gauge argument that
made the background's own $\dot{\mathcal N}$ term well-behaved in WP2),
the founding paper's system above can be imported directly, with only
$\bar\rho(a)$, $w(a)$, $F(Q)$ replaced by cdot-8's own census/quadrature
results — a clean, structurally analogous import to WP5/WP6's own
successful pattern. If $\delta\mathcal N\neq0$ and sources a genuinely
new term, WP7 needs an extension this founding-paper system does not
provide, and the M5-perturbation question becomes load-bearing rather
than a formality.

**Not yet resolved.** This is squarely the "genuinely new, not
literature-importable" question WP5 and WP6 each identified and answered
in their own regime — WP7's analog, in the regime where the answer is
least obviously safe. Recommending this be the first concrete derivation
task, before attempting to adapt the $\Pi$/dustlike-limit question to
cdot-8's own $F(Q)$, since it determines whether that adaptation is even
the right next step or whether a more fundamental extension is needed
first.

## 2a. Advisory response — $\delta\mathcal N$ resolved with a window function; the real finding is that the fluid form cannot cross the crossover

`Advisory-WP7-FirstInstallment-2026-07-18.md` + `wp7_structure.py`
(landed in three copies across `cdot-8/advisory/`, `WP6/advisory/`, and
the correct `WP7/advisory/` — noted, not chased further). **Reproduced
the script myself before accepting anything.**

**§2's question answered: $\delta\mathcal N\neq0$, with structure.** WP5's
local-decoupling argument does not extend to cosmological scales — a
$k$-mode couples to the horizon-volume census through the standard
spherical top-hat window $W(kR_h)=3j_1(kR_h)/(kR_h)$ (verified
independently: this is exactly the Fourier transform of a real-space
top-hat of radius $R_h$, the same window function used throughout
structure-formation theory, not something invented for this occasion).
Since M5 remains *one* constraint per time-slice, the force it exerts on
any individual mode carries this same window. Reproduced the table
exactly:

| $kR_h$ | $\lvert W\rvert$ | regime |
|---:|---:|---|
| 0.1 | 1.00 | super-horizon / SW plateau |
| 1 | 0.90 | horizon crossing |
| 6 | 0.084 | first acoustic peak scale |
| 20 | $2.7\times10^{-3}$ | higher peaks |
| $10^3$ | $1.7\times10^{-6}$ | matter power spectrum |

**Consequence**: the AeST perturbation system (§1) imports *cleanly* for
sub-horizon physics (matter power spectrum, higher acoustic peaks —
corrections $\lesssim10^{-6}$ at galaxy scales), but there is a **genuine,
unavoidable new M5 term at $kR_h\lesssim$ few** (low-$\ell$ CMB,
super-horizon evolution) — real new derivation work, not yet done, and
explicitly *not* to be read as support for any specific low-$\ell$
anomaly before that term is actually derived. The first-acoustic-peak
scale itself carries a non-negligible ($\sim8\%$) window and must be
carried through, not dropped. None of this touches WP4a's background
$\theta_*$ — a background vs. perturbation distinction, kept clean.

**The round's actual finding, surfaced while pre-computing for the
$\Pi\to0$ question**: computed cdot-8's own scalar-sector equation of
state $w(a)$ from the established quadrature, using $\rho_s=\tfrac12QF_Q-
\tfrac13F$ (the Friedmann-constraint combination the quadrature was built
to satisfy — checked inline against $\Omega_s$ directly, agreement to
$10^{-4}$, using the same long-validated closure trajectory machinery
this whole session has relied on). **$\Omega_s$ crosses zero at $z
\approx9640$** — the scalar's share runs from $+93\%$ today to $0$ to
$-7\%$ deep in radiation. At the crossing, $w$ and $c_\text{ad}^2$
formally diverge (a generic, well-understood feature of any fluid
decomposition whose energy density passes through zero — not exotic).
**The founding paper's fluid description of the scalar-vector sector
cannot be used through exactly this crossing**, while the underlying
field variables ($\chi,\mathcal E_\alpha$) stay perfectly regular there.

**Directive accepted for how WP7 must proceed**: run the crossover era
directly in field variables, switching to the imported fluid form only
where $|\Omega_s|=O(1)$ (safely true in the matter era, where the invoice
is dust-like by construction, and today). AeST's own native $\Pi\to0$
shortcut — the thing §1 flagged as needing a check for cdot-8's own
$F(Q)$ — **does not transfer through the crossing region regardless of
what it does elsewhere**, since the fluid variables it's stated in
break down exactly there.

**One more thing worth recording**: the advisory notes its own v1 script
failed an inline self-check (a wrong dictionary combination) before
delivery, catching two of its own errors (the $\rho_s$ formula; a
narrative conflation of two different numbers) — exactly the discipline
this program has practiced throughout, operating on the advisor's own
side this time, and it's what surfaced the zero-crossing finding in the
first place.

**Status of this installment**: the $\delta\mathcal N\neq0$ question is
now resolved *structurally* (the window function and its consequences
are established), though the actual coefficient of the new low-$\ell$/
super-horizon M5 term still needs deriving explicitly in Newtonian gauge
— the next concrete task. The crossover-era fluid-form breakdown is a
genuine, independently-verified structural finding that reshapes how the
$\Pi\to0$ question (§1) must be approached: not a simple check, but a
question that only has a clean answer away from the crossover, with the
crossover itself needing field-variable treatment. This is, notably, the
same crossover-era zone Gate 1(b) already flags as unresolved at the
background level — now shown to carry perturbation-level structure of
its own, coherently, not as new damage.

## 3. Status

**Structural first installment only**, matching this program's
established rhythm (WP3's action-level rounds; WP5 and WP6's own opening
installments). Imported AeST's established linear cosmological
perturbation system directly, verified by direct quotation from the
primary source, not reconstructed from the abstract's claims alone.
Posed, but did not resolve, the horizon-scale analog of WP5/WP6's
local-decoupling question — flagged as genuinely open, in the regime
where it is least safe to assume away by analogy. Every finding here
inherits Gate 1(b)'s provisional-failure caveat on the cosmological
background; this is legitimate work under that caveat, proceeding per
the author's explicit sequencing instruction, not a claim that WP4a's
miss is resolved or moot. Nothing in `cdot-7/` was touched.

**Updated after the advisory response (§2a)**: $\delta\mathcal N\neq0$
is now established, with a verified window-function structure —
sub-horizon import is clean, a genuine new M5 term exists at $kR_h
\lesssim$ few (not yet derived explicitly), and — the round's real
discovery — cdot-8's own scalar-sector fluid description breaks down at
a genuine $\Omega_s=0$ crossing at $z\approx9640$, inside the same
crossover zone Gate 1(b) already flags at the background level. WP7 must
run the crossover era in field variables, not the imported fluid form.
Next concrete tasks: (i) derive the low-$\ell$/super-horizon M5 term
explicitly in Newtonian gauge; (ii) set up the field-variable ($\chi,
\mathcal E_\alpha$) treatment through the crossover, falling back to the
fluid form only where $|\Omega_s|=O(1)$.

## 4. The M5 term, derived — grounded in WP3's own established action, not re-derived from scratch

**Went back to WP3's own record for the exact M5 action term**, rather
than reconstruct it from summary recollection, given how many
hard-won corrections that saga went through. Confirmed, quoted directly
(`Update-WP3-ClosedActionCouplingAudit-2026-07-13.md`):
$$S_{M5}=\int dt\,\Lambda_M\big[Q-q(\mathcal N_\text{tot})\big],\qquad
\mathcal N_\text{tot}=\sum_i\mathcal N_i,$$
with $\Lambda_M,Q$ single functions of time (the constraint is, by
construction, **one number per time-slice** — this is the already-settled
fact behind both WP5's local-decoupling argument and the advisory's own
"M5 remains one constraint per slice" framing) — and, independently
confirmed from the same WP3 record, the already-established identity
$$\Lambda_M(t)=\frac{Na^3F_Q(Q)}{16\pi\tilde G}$$
(from varying $Q$'s own field equation, $C_1=0$ already resolved by
past-regularity). **This is not a new derivation — it is the exact,
already-verified background relation this whole program has used
throughout**, now the key that lets the perturbative extension below be
expressed in already-computable quantities rather than fresh, unverified
ones.

**The perturbative extension**: promote $\mathcal N_i$ to its actual WP2
definition — a horizon-ball spatial integral, not a bare time function —
while $\Lambda_M,Q$ remain spatially uniform (M5 constrains only the
integrated total, never a specific location or mode — the same fact
§2a's window-function argument already rests on). Then $\mathcal
N_\text{tot}(t)=\bar{\mathcal N}_\text{tot}(t)+\delta\mathcal N_\text{tot}
(t)$, with $\delta\mathcal N_\text{tot}$ built from every matter species'
density and volume perturbations, each individual Fourier mode entering
with the window weight $W(kR_h)$ established in §2a.

**Varying the action with respect to a single mode's density
perturbation** (not with respect to $\Lambda_M$, which only returns the
global constraint) picks up a genuine, linear-order contribution from
$S_{M5}$, since $\mathcal N_\text{tot}$ — appearing inside $q(\mathcal
N_\text{tot})$ — depends on every mode through the horizon-ball integral:
$$\frac{\delta S_{M5}}{\delta\rho_k}=-\Lambda_M(t)\,q'\big(\bar{\mathcal
N}_\text{tot}\big)\times W(kR_h)\times[\text{species Planck-mass
weight}].$$
**This is a genuine, surviving, linear-order effect — not obviously
cancelled the way the background $D\equiv0$ finding cancelled the census/
horizon sector's own kinetic back-reaction.** That resolution zeroed a
*different* piece (the $p_i,p_R$ multiplier sector's own coupling to the
Hamiltonian constraint via an incorrectly lapse-dependent $g_i$); the
$\Lambda_M$-mediated coupling between $\mathcal N_\text{tot}$ and $Q$
is a separate part of the action, untouched by that resolution and
already load-bearing for the *background* Friedmann equation via the
same $\Lambda_M\propto F_Q$ identity. Checked this distinction explicitly
before assuming the new term survives, given this program's repeated
history of a "new term" turning out to be an artifact (WP3's own C2
saga, the D≡0 resolution itself) — this is a different piece of the
action from either of those, not a repeat of the same mistake.

**$q'(\bar{\mathcal N}_\text{tot})$, obtained without a new unknown**:
since the constraint holds identically on the background trajectory,
$\bar Q(t)=q(\bar{\mathcal N}_\text{tot}(t))$, the chain rule gives
$$q'(\bar{\mathcal N}_\text{tot})=\frac{\dot{\bar Q}}{\dot{\bar{\mathcal
N}}_\text{tot}},$$
both sides computable from trajectories already established (WP3's own
$Q(a)$ solution; WP2's own $\dot{\mathcal N}_i/\mathcal N_i=g_i$
evolution equation, quoted verbatim in §1's action). **No new background
input is required** — only assembly of quantities this program has
already computed and verified repeatedly.

**What this installment establishes, and what it doesn't yet**:
established — the M5 perturbation term's functional form, its window-
function scaling, and its coefficient's expression entirely in terms of
already-verified background quantities ($F_Q$, the $Q(a)$ and $\mathcal
N_i(a)$ trajectories). **Not yet done**: assembling this into the
specific perturbed Einstein equation ($\delta G^0_0$ vs. the momentum
constraint $\delta G^0_j$), working out the density-vs-volume-vs-
horizon-boundary decomposition of $\delta\mathcal N_\text{tot}$
explicitly (the three pieces §2a's advisory named), and computing the
actual numerical coefficient along cdot-8's own trajectory. This is
staged, deliberate progress — the structural piece done and checked
against the established record, the numerical assembly flagged as the
next concrete step, not rushed.

## 5. Assembly continued — the boundary question resolved from WP2's own text, and which equation the term enters

**Checked the "horizon-boundary piece" against WP2's own original
definition**, rather than assume a separate boundary-shift contribution
exists. Quoted directly (`Update-WP2-CovariantCensus-2026-07-12.md`):
the census integral's domain is "a comoving ball of **coordinate**
radius $R_h(t)$" satisfying $\dot R_h=c(t)$. **The integration boundary
is fixed in comoving coordinates — a pure background quantity, not
itself perturbed.** This resolves the question rather than leaving it
open: there is no separate boundary-shift term beyond the volume-element
piece already derived ($\sqrt h\propto1-3\Phi$ at fixed comoving
radius) — the "three pieces" the advisory named are the density and
volume pieces already in hand, plus $R_h(t)$'s own (background,
time-dependent, not perturbative) role in setting the window's argument
$kR_h(t)$ at each epoch. **Confirmed density+volume decomposition,
verified against the primary WP2 text rather than assumed**:
$$\delta\mathcal N_i(k,t)=\bar{\mathcal N}_i(t)\,W(kR_h(t))\,\big[\delta_i(k,t)-3\Phi(k,t)\big].$$

**Resolved which equation the new term enters, checked against WP3's own
"inviolable matter continuity" directive** (`Advisory-WP3-TouchPoint-
ExchangeTarget-2026-07-12.md`: "any construction that balances the
ledger by de-conserving matter... is a kill of that construction,"
established as a hard constraint from early in WP3). Matter couples to
the metric $g_{\mu\nu}$ alone (K1, no disformal coupling — WP1's own
finding); $\mathcal N_\text{tot}$'s dependence on matter density inside
$S_{M5}$ is the same kind of dependence $T_{\mu\nu}$ has on matter fields
when sourcing the ordinary Einstein equations, not a new, independent
coupling that would modify matter's *own* equation of motion. **The new
M5 term therefore enters the gravitational constraint equation
($\delta G^0_0$, the Poisson-type equation for $\Phi$), not matter's own
continuity equation** — consistent with, and checked against, the
directive rather than assumed compatible with it by default. Assembled:
$$\delta G^0_0(k)=8\pi G\sum_I\bar\rho_I\delta_I(k)+8\pi G\,\Lambda_M\,
q'(\bar{\mathcal N}_\text{tot})\,W(kR_h)\big[\delta_\text{tot}(k)-3\Phi(k)\big],$$
with $\delta_\text{tot}$ the appropriately $\mathcal N_i$-weighted total
density contrast (species weights matching WP2's own established $p^\text{sp}$
exponents) and $\Lambda_Mq'(\bar{\mathcal N}_\text{tot})$ from §4, in
already-established background quantities.

**What remains, stated honestly**: the overall numerical prefactor above
has *not* been independently cross-checked — the natural check is
whether this term, evaluated at $k\to0$ (super-horizon, $W\to1$), is
consistent with the already-established background contribution of M5
to the Friedmann equation (the $\tfrac12QF_Q$ term already in $H_{\hat
\tau}^2$). This is exactly the kind of normalization cross-check this
program has repeatedly needed and repeatedly gotten right only on a
second, independent pass (WP4b's saga; WP6's PPN dictionary) — flagging
it explicitly as the next verification step rather than asserting the
prefactor above is final without it.

## 6. The flagged check fires — the assembled term was incomplete, corrected

`Advisory-WP7-SeparateUniverseCheck-2026-07-18.md` +
`m5_separate_universe_check.py`, run per the flagged next step above
before proceeding further. **Verified the load-bearing identity by hand,
independently of the script, before accepting the correction.**

**The check**: at $k\to0$ ($W\to1$), a uniform perturbation is a shifted
background (the standard separate-universe argument) — so the M5 source
must equal the derivative, along the constraint $Q=q(\mathcal N_\text{tot})$,
of the background's own $-\tfrac F3+\tfrac{QF_Q}2$ contribution to
$H_{\hat\tau}^2$:
$$\frac{d}{dQ}\Big[-\frac F3+\frac{QF_Q}2\Big]=-\frac{F_Q}3+\frac{F_Q+
QF_{QQ}}2=\frac{F_Q}6+\frac{QF_{QQ}}2.$$
**Confirmed this by direct differentiation myself** — a two-line
calculus check, not something requiring the script to trust. §5's
assembled term carried only $\tfrac{F_Q}2\,q'$ (the $\Lambda_Mq'$
channel) — **the check fires**: $\tfrac{F_Q}2\neq\tfrac{F_Q}6+\tfrac{
QF_{QQ}}2$ in general.

**Where the gap was, understood, not just patched**: §5 varied the $Q$
appearing *explicitly* inside the M5 constraint term at fixed $\Lambda_M$
— a legitimate partial derivative, but incomplete, because $\delta Q=
q'\delta\mathcal N$ propagates through *every* place $Q$ enters, not
just the constraint term: (i) $\Lambda_M=Na^3F_Q(Q)/16\pi\tilde G$ is
itself field-dependent, so $\delta\Lambda_M\propto a^3F_{QQ}\,\delta Q$
supplies an extra $+\tfrac{QF_{QQ}}2\,q'$; (ii) the scalar's own $-F/3$
background contribution responds as $-\tfrac{F_Q}3\,\delta Q$. Together:
$\tfrac{F_Q}2-\tfrac{F_Q}3+\tfrac{QF_{QQ}}2=\tfrac{F_Q}6+\tfrac{QF_{QQ}}2$
— exactly the required identity. **Nothing new needed — the same
$\delta Q=q'\delta\mathcal N$, carried consistently through every term
it touches, not just the one I varied first.**

**Corrected coefficient**:
$$\delta G^0_0(k)\supset8\pi G\Big[\frac{F_Q}6+\frac{QF_{QQ}}2\Big]\,q'\,
\bar{\mathcal N}_\text{tot}\,W(kR_h)\big[\delta_{\mathcal N}-3\Phi\big],$$
with $\delta_\mathcal N=\sum_i\bar{\mathcal N}_i/\bar{\mathcal N}_\text{tot}
\,[\delta_i-3\Phi]$-type weighting made explicit per the bookkeeping flag
below, rather than folded into an ambiguous "species weight." **The
$QF_{QQ}/2$ piece is $O(1)$ relative to $F_Q/6$** (with $F_{QQ}=-0.696$
already established from WP5's own condensate-mass calculation) —
omitting it would have been an order-one error in the new term, not a
minor refinement.

**Worth noting explicitly**: this is $F_{QQ}(Q_0)$'s *third* independent
load-bearing appearance in cdot-8 — WP5's condensate mass $\mu_\text{eff}$,
the SZ stability sign check, and now this perturbed-constraint feedback
all draw on the same quadrature curvature, with no new parameter
introduced anywhere. One determined function answering three unrelated
questions is exactly what a genuinely zero-adjustable-element $Q$-sector
should look like — a coherence check on the whole program, not just this
term.

**Two flags carried forward, not dismissed**: (i) a bookkeeping
precision — write $\delta\mathcal N_\text{tot}=\sum_i\bar{\mathcal N}_i
W(kR_h)[\delta_i-3\Phi]$ explicitly rather than leave the $\bar{\mathcal
N}_i$ weights implicit, so the identity can be checked numerically
without ambiguity; (ii) a genuine, not-yet-resolved gauge question — the
comoving-coordinate census domain (§5) makes $\delta\mathcal N$ itself a
Newtonian-gauge-specific object ($[\delta_i-3\Phi]$ would differ in
synchronous gauge); consistent for now since this whole system is being
assembled in Newtonian gauge throughout, but the covariant status of the
census domain at perturbative order is a genuine open question for this
program specifically, potentially $O(1)$ exactly at the $kR_h\lesssim1$
scales where this term lives — carried as a named flag, not resolved
here, not a blocker either.

## 7. The field-variable treatment through the crossover — a cleaner resolution than a patchwork

**Goal**: since §2a established that the fluid description ($\delta_s,
\theta_s,\Pi_s$ built from $w_s,c_{\text{ad},s}^2$) formally diverges at
the $\Omega_s=0$ crossing while the field variables ($\chi,\gamma,\alpha,
\mathcal E_\alpha$ — equivalently $\delta\phi,\delta\dot\phi,\alpha$
directly) stay regular, work out what evolving those field variables
*directly* through the crossover actually requires.

**First point, worth stating plainly**: $\Omega_s=0$ is not a physical
singularity of any kind — $F(Q),F_Q(Q),F_{QQ}(Q)$ are smooth, finite
functions of $Q$ straight through the crossing (nothing about the
quadrature itself does anything special there). The divergence in $w_s,
c_{\text{ad},s}^2$ is a coordinate-type artifact of describing a
perfectly regular field as a "fluid" via $w=p/\rho$-type ratios, which
are necessarily ill-behaved whenever the denominator crosses zero — a
completely generic fact about *any* field forced into a fluid
description, not something specific to cdot-8's scalar. **The correct
fix is not a special crossover-only patch and a fluid description
elsewhere — it's to never build the fluid description for this sector at
all**, evolving $\chi,\gamma$ (equivalently $\delta\phi,\delta\dot\phi$)
and $\alpha,\mathcal E_\alpha$ directly via their own field equations
throughout the *entire* cosmological history. This matches standard
practice in the literature for exactly this class of problem (evolving
the field directly rather than a fluid/sound-speed approximation, for
quintessence-type sectors whose energy density can change sign).

**Does M5 modify $\chi,\gamma$'s own evolution equation, on top of the
Einstein-equation term already derived (§4–§6)?** Checked this
explicitly rather than assume either way. $S_{M5}=\Lambda_M[Q-q(\mathcal
N_\text{tot})]$ depends on $Q=A^\mu\nabla_\mu\phi$ *explicitly*, so
varying it with respect to $\nabla_\mu\phi$ contributes an additional
$+\Lambda_MA^\mu$ to WP6 Step 2's general covariant $\phi$-equation
(`Update-WP6-PPNDerivation-2026-07-18.md`), which itself already carries
a $-F_QA^\mu$ term from the base AeST action. **These two terms are not
independent — $\Lambda_M$'s own value is *defined*, at every order, by
the already-established identity $\Lambda_M=Na^3F_Q/(16\pi\tilde G)$**
(quoted in §4, verified repeatedly throughout WP3's own record). Since
$\Lambda_M(t)$ carries no $k$-dependence of its own (M5 is one
constraint per time-slice — the structural fact §2a's window argument
and §4–§6 both already rest on), this identity holds not just for the
background but at every $k$: **the $-F_QA^\mu$ and $+\Lambda_MA^\mu$
contributions cancel identically, for every mode.** $\phi$'s (and, by
the same argument, $\alpha$'s) own perturbed field equation is therefore
**unmodified by M5** — the founding paper's $\chi,\gamma,\alpha,\mathcal
E_\alpha$ system (§1) can be used exactly as imported, with *zero* new
terms of its own.

**This is the same "M5 doesn't disturb local physics" finding WP5
established for solar-system/galaxy scales, now extended to cosmological
perturbations specifically** — not assumed to carry over by analogy
(§2a already showed that kind of assumption fails for the *Einstein*
equation), but checked directly and found to hold for the *scalar/vector
field equations* specifically, because the cancellation mechanism here
(exact equality of two terms via an independent, already-established
background identity) is different in kind from the reasoning that failed
for $\delta G^0_0$.

**The resulting system, complete**: evolve $\chi,\gamma,\alpha,\mathcal
E_\alpha$ via §1's unmodified equations (imported directly from the
founding paper, no crossover-specific patch needed, valid at every
epoch including the $\Omega_s=0$ crossing since nothing here references
$w_s$ or $c_{\text{ad},s}^2$ at all); solve the Einstein constraint
equation with the single M5-sourced addition derived in §6,
$8\pi G[\tfrac{F_Q}6+\tfrac{QF_{QQ}}2]q'\bar{\mathcal N}_\text{tot}
W(kR_h)[\delta_\mathcal N-3\Phi]$; never construct $\delta_s,\theta_s,
\Pi_s,w_s,c_{\text{ad},s}^2$ as intermediate quantities at all. This is
simpler than a patchwork (fluid away from the crossing, fields through
it) and avoids the coordinate singularity by construction rather than by
switching descriptions at a special epoch.

**Confidence, stated honestly**: the $k$-independence of $\Lambda_M$
(the key step enabling the exact, all-$k$ cancellation) rests on the
same structural fact used throughout §2a–§6, not a fresh assumption —
solid. The cancellation itself is algebraic once that's granted, low
risk. What hasn't been done is a direct numerical check of this specific
claim (analogous to the $k\to0$ separate-universe check that caught §5's
gap) — recommended as the natural verification before treating this as
fully closed, given this program's standing practice of not trusting a
structural argument of this kind without one.

## 8. WP7 status

Established, checked at the level this program has held itself to
throughout: the AeST perturbation system imports cleanly sub-horizon
(§1–§2a); a genuine new M5 term exists in the Einstein equation at
$kR_h\lesssim$ few, now derived, verified against a separate-universe
check, and corrected once as a result (§4–§6); the scalar/vector field
equations themselves are unmodified by M5, at every $k$ (§7), so the
crossover-era fluid breakdown (§2a) is resolved by never building the
fluid description at all, not by a special patch. **Not yet done**: the
recommended numerical cross-check of §7's all-$k$ cancellation claim;
assembling all of this into an actual numerical Boltzmann-style solve
for the power spectrum (the eventual deliverable). Every result here
inherits Gate 1(b)'s provisional-failure caveat — this crossover-era
structure is coherent with, not new damage beyond, WP4a's own
background-level miss in the same era. Nothing in `cdot-7/` was touched.

## 9. Attempting the recommended cross-check surfaced a genuine ambiguity, not yet in §7

**Set out to run the numerical cross-check §7 itself recommended**, and
in trying to state it precisely enough to actually check, found a real
conceptual gap underneath §7's argument — not a computational error, a
question of what's being computed at all.

**The gap**: $S_{M5}=\int dt\,\Lambda_M[Q-q(\mathcal N_\text{tot})]$, as
written throughout WP3's own record, is a *pure time integral* — no
$d^3x$, no $\sqrt{-g}$. That form is only unambiguous in the homogeneous
background WP3 built it for, where $Q(t)$ is a single number and there is
no spatial structure to integrate over. **§7 varied it against a specific
Fourier mode $\delta\phi_k$ as if $Q$ in the constraint were a well-defined
local field's value — but $S_{M5}$ was never actually written that way**,
and *how* to covariantize it to the perturbed case is a genuine choice,
not something already settled by the existing record:

- **If $Q(t)$ in the constraint means the true global (all-space) zero
  mode of $\dot\phi$**, then a single Fourier mode $k\neq0$ contributes
  *nothing* to it (Fourier orthogonality) — $S_{M5}$ doesn't source
  $\delta\phi_k$'s equation *at all*, trivially, not via a cancellation
  of two nonzero terms.
- **If $Q(t)$ means a horizon-ball average of the local $\dot\phi(x,t)$**
  — the natural reading given $\mathcal N_\text{tot}$ itself is
  explicitly a horizon-ball integral, not an all-space one (WP2 §1,
  quoted in §4) — then $\delta\phi_k$ *does* contribute, weighted by the
  same $W(kR_h)$ already established, and §7's cancellation argument
  applies essentially as written, just with the window factor made
  explicit on both sides of it.

**Checked whether WP2/WP3's own record already settles this — it
doesn't.** Confirmed directly: WP2's own text describes $\mathcal N$
as built "reducing to cdot-7's $M_h/m_P$ in the *symmetric sector* by
construction" — i.e., WP2 and everything built on it through WP6 only
ever needed the homogeneous system. **This is genuinely new territory,
not a question the existing record already answers one way or the
other.**

**Why this matters, stated plainly**: both readings plausibly give the
same *qualitative* conclusion (§7's "M5 doesn't modify $\phi$'s own
equation for $k\neq0$"), but for different reasons and with different
$k$-dependence of the coefficient — the trivial reading gives an exact
zero at all $k\neq0$ regardless of window scale, while the horizon-ball
reading gives a $W(kR_h)$-weighted cancellation that would only be exact
at all $k$ if the window factor genuinely appears symmetrically in both
the $-F_QA^\mu$ term and the $+\Lambda_MA^\mu$ term — which has *not*
been shown here, only asserted by analogy with §4–§6. **Not resolved in
this pass.** Given how foundational this choice is (it bears on how
$Q$ itself, not just $\mathcal N_\text{tot}$, is defined at perturbative
order — arguably prior to, not just alongside, the M5-term derivation
already done), recommending this be settled explicitly — likely worth an
advisor cross-check, given the stakes of building the rest of WP7 on
whichever reading turns out to be right, without yet knowing which one
is.

## 10. WP7 status, updated

Solid and unaffected by §9: the AeST perturbation system imports cleanly
sub-horizon; the $\delta\mathcal N$ window-function structure (§2a); the
Einstein-equation M5 term, derived and separate-universe-checked (§4–§6).
**Newly flagged, not yet resolved**: whether $Q$'s own perturbative
definition is a true global zero mode or a horizon-ball average
matching $\mathcal N_\text{tot}$'s — this decides whether §7's "$\phi$'s
equation is untouched by M5" conclusion is exactly right, trivially
right for a different reason, or needs revision. Recommending this
specific question be resolved (ideally cross-checked) before further
numerical assembly toward the power spectrum. Every result here
inherits Gate 1(b)'s provisional-failure caveat. Nothing in `cdot-7/`
was touched.

## 11. §9 adjudicated — reading (A) ruled out, (B) adopted; §7 corrected at finite $k$

`Advisory-WP7-QDefinitionAdjudicated-2026-07-18.md` +
`q_definition_adjudication.py`. **Reproduced the script myself before
accepting anything** — the magnitude table (`1-W(kR_h)` and the
$(aH/k)^2(1-W)$ scaling estimate) reran exactly as delivered.

**Reading (A) (global zero mode) ruled out, three independent grounds,
all checked rather than taken on assertion**: (i) non-Machian — an
all-space average is acausal, against the charter's own founding
principle that local $c$ is set by the *horizon* census, not a
whole-slice one; (ii) an incoherent pairing — one constraint equation
would relate an all-space average ($Q$) to a horizon-ball integral
($\mathcal N_\text{tot}$), mixing two different domains in the same
equation; (iii) internally inconsistent with this document's own §4–§6:
the *same* $S_{M5}$, varied against densities, was already shown to
produce a *windowed* $\delta\mathcal N$ — the $Q$-side of the identical
functional cannot consistently be windowless while the $\mathcal
N_\text{tot}$-side is windowed. Point (iii) is the sharpest of the
three: it isn't a new principle, it's a direct consistency check against
work already on the record in this same document, and it holds.

**Reading (B) (horizon-ball average, same ball as $\mathcal N$) is
therefore adopted.** The window symmetry §9 explicitly refused to assume
by analogy is now *derived*, not asserted: both sides of the constraint
are integrals of local fields over the *same* domain, so every mode's
contribution to each side carries the same $W(kR_h)$. **One caveat
carried forward, not resolved**: a ball needs a center: at perturbative
order the constraint is fiducial-observer-anchored (operationally *our*
ball for *our* observables), and translation invariance at this order
joins the census-gauge flag already carried from §6 as the same family
of open covariant-completion question.

**Consequence, checked**: under (B), $\Lambda_M=Na^3F_Q/(16\pi\tilde G)$
is extensive over the fiducial ball, so the M5 contribution to
$\delta\phi_k$'s equation is $+F_Q\,W(kR_h)\times(A\text{-structure})$ —
against the bulk current's windowless $-F_QA^\mu$ (a genuinely local,
pointwise term from the base action, no window). Net:
$$-F_Q\big(1-W(kR_h)\big)\times(A\text{-structure}).$$
At $k\to0$: $W\to1$, exact cancellation, reproducing the $k=0$ anchor
(the background identity $\Lambda_M=a^3NF_Q$) exactly as §7 already
established — **§7's own worked case survives unchanged**. At finite
$k$ the term survives, weighted $(1-W)$: sub-horizon it is
$(aH/k)^2$-suppressed (same PPN-familiar class as WP6 Step 2's own
$-F_QA^\mu$ term — negligible at galaxy/pulsar scales, $\sim10^{-6}$ or
smaller, consistent with WP5/WP6 untouched); at $kR_h\sim1$–$6$ (exactly
the low-$\ell$/horizon-crossing/first-acoustic-peak window) it is
$O(0.03$–$0.1)$ relative to the mode's own gradient term — **not
negligible**.

**§7's statement corrected for the record**: "$\phi$'s equation is
unmodified by M5" holds sub-horizon (to $(aH/k)^2$) and exactly at
$k=0$; at $kR_h\lesssim$ few it is modified by
$-F_Q(1-W(kR_h))\times(A\text{-structure})$ — a term that is *required*,
not optional, for the eventual low-$\ell$ derivation. The low-$\ell$
sector now has **both halves** of its M5 structure on the record: the
Einstein-side term (§6) and this field-side term, sharing one window
architecture and one $F_Q/F_{QQ}$-class coefficient family — the same
kind of coherence already noted for $F_{QQ}$'s three independent
appearances (§6).

**Directives accepted for the next assembly pass** (from the advisory,
endorsed): (1) rebuild §7's system with the field-side term included,
using the $k\to0$ cancellation as one exact anchor (residual = error)
alongside §6's separate-universe anchor — two independent exact checks
now bracket the assembly, not one; (2) one further channel flagged,
explicitly not yet decided either way: the census weights themselves
($E_P$, the $p_i^\text{sp}$ exponents) may depend on the local $Q$,
giving a $\delta Q$-proportional piece of $\delta\mathcal N$ with the
same window architecture but renormalized coefficients — to be included
or excluded *explicitly* on the WP2 record when the numerical assembly
is built, not silently defaulted either way; (3) the fiducial-center
caveat and the census-gauge flag (§6) are the same open item and belong
together in any future covariant-completion write-up.

**What this resolves and what it doesn't**: resolves §9's ambiguity
cleanly — (B) is the physically consistent reading, checked against
this document's own prior sections rather than decided by outside
principle alone. Does **not** yet resolve the still-open, previously
named items: the fiducial-center/translation-invariance question, the
census-weights-depend-on-$Q$ channel, and the still-outstanding
numerical cross-check of the corrected all-$k$ field equation (now a
two-anchor check: $k\to0$ exact cancellation, plus §6's separate-universe
identity). **The low-$\ell$ sector's structure is now believed complete
at the level of identifying every term** — deriving the actual
numerical coefficients and running the crossover-era field-variable
system is the next concrete task, unchanged in kind from §8/§10's own
framing, now with one more term correctly included. Every result here
inherits Gate 1(b)'s provisional-failure caveat. Nothing in `cdot-7/`
was touched.

## 12. Running the recommended cross-check surfaces a second, distinct covariantization gap — §11's normalization not yet secure

**Set out to run directive (1) from the accepted advisory** (rebuild
§7's system with the field-side term, verify the $k\to0$ cancellation
numerically alongside §6's separate-universe anchor) — and, in trying
to state the check precisely enough to run it, found a second
covariantization ambiguity, of the same *kind* as §9's but at a
different location, sitting underneath §11's accepted correction rather
than inside it.

**The gap**: §11's corrected field-equation term rests on one specific
step (Advisory §3): "$\Lambda_M=Na^3F_Q/(16\pi\tilde G)$ is *extensive
over the fiducial ball*, so $\Lambda_M\times(W/V_\text{ball})=F_Q
\text{-density}\times W$." This silently identifies the minisuperspace
$a^3$ appearing in $\Lambda_M$'s own definition with $\mathcal
N_\text{tot}$'s ball volume $(4\pi/3)R_h(t)^3$ (WP2 §1) — but these are
two objects built by two different routes: $a^3$ is the bare FRW
scale-factor cube from WP3's minisuperspace action
(`Update-WP3-ActionLevelAttempt-2026-07-12.md`: $d(a^3F_Q)/dt=0$ the
free conservation law, no $R_h$ anywhere in that derivation), while
$R_h(t)$ is built directly from integrating $\dot R_h=c(t)$ (WP2 §1).
**Nothing upstream states or derives that these track each other.**

**Checked, not assumed**: built `wp7_lambda_extensivity_check.py`
(saved to `cdot-8/WP7/`, reusing the exact validated trajectory
machinery from `wp7_structure.py` — same $E(s)$, same solved closure
ODE), integrated $R_h(s)$ from its own defining relation
$dR_h/ds=c_0e^{(2/3)s}/(H_0E(s))$ (past-regularity anchor, $R_h\to0$ as
$s\to-\infty$, the same convention this program uses for every other
such integral), and compared $R_h(t)/a(t)$ across epochs:

| $z$ | $d\ln R_h/ds$ | $d\ln a/ds$ | $R_h/[(c_0/H_0)e^s]$ |
|---:|---:|---:|---:|
| $10^6$ | 3.68 | 1 | $6.6\times10^{-10}$ |
| $10^4$ | 3.60 | 1 | $2.3\times10^{-6}$ |
| 9640 (crossing) | 3.60 | 1 | $2.4\times10^{-6}$ |
| 1090 ($z_*$) | 3.13 | 1 | $8.2\times10^{-5}$ |
| 30 | 2.89 | 1 | $7.5\times10^{-3}$ |
| 1 | 2.71 | 1 | 0.231 |
| 0 | 2.18 | 1 | 0.458 |

**$R_h(t)$ and $a(t)$ evolve at genuinely different, epoch-dependent
rates** — $R_h/a$ changes by nine orders of magnitude across this
table, not approximately constant in any regime checked, including
exactly at $z_*$ and the $\Omega_s$ crossing where the low-$\ell$ term
actually lives. So identifying $a^3$ with $(4\pi/3)R_h^3$ (up to a
fixed constant) is not automatically harmless anywhere in the regime
this term matters — it is a **modeling convention** (treat the M5
sector's own minisuperspace cell as *coinciding with* the horizon ball
— arguably natural, since M5 is "one constraint per slice" tied to the
same horizon census throughout, and reading (B) already made the
analogous choice for $Q$ itself), **not a derived fact**, and no
statement of this convention (nor its consequence for the term's actual
numerical prefactor) currently exists anywhere in this record.

**What this does and doesn't change**: does not overturn §11's
*qualitative* conclusion (a surviving, window-weighted term at
$kR_h\lesssim$ few, vanishing sub-horizon and at $k=0$) — the
$k\to0$ limit itself is unaffected, since at $k=0$ the ball-volume
question never arises (no local mode to normalize against). It **does**
mean the term's normalization at finite $k$ — the specific coefficient
that will feed the eventual numerical low-$\ell$ solve — is not yet
secure, pending an explicit statement (and justification) of the
$a^3\leftrightarrow(4\pi/3)R_h^3$ convention. **Not resolved here,
flagged rather than assumed away**: this is the same class of "genuinely
new, foundational, not already-answered-by-the-record" gap §9 was, now
found one step further into the assembly — recommending it be settled
(ideally cross-checked) before the coefficient in §11 is used
numerically, exactly as §9 itself was handled. Every result here
inherits Gate 1(b)'s provisional-failure caveat. Nothing in `cdot-7/`
was touched.

## 13. §12 conceded in full; two physical anchors pin the asymptotics regardless of the convention

`Advisory-WP7-CovariantizationFreedom-2026-07-18.md` +
`covariantization_adjudication.py`. **Reproduced the script before
accepting anything** — the $d\ln R_h/ds$ and $R_h/e^s$ values match
`wp7_lambda_extensivity_check.py`'s own output exactly (e.g. $z=0$:
$2.184$, $0.458$), independent confirmation, not a re-assertion of the
same number.

**The concession, precisely scoped**: §12's catch stands as reported —
$\Lambda_M$'s minisuperspace $a^3$ (the fixed comoving fiducial cell of
WP3's own action) and $\mathcal N_\text{tot}$'s ball, which genuinely
grows relative to it, are two distinct volume conventions; identifying
them was an unstated modeling choice inside what had been presented as
a coefficient-level derivation. Logged as this program's error #7 —
same *class* as the earlier cross-frame/sign-convention errors this
whole session has tallied, caught here by an independent runnable check
before the coefficient was used for anything, exactly the discipline
this program has held to throughout (in both directions).

**What survives, checked rather than taken on the advisory's word**:
two requirements *already independently established in this record* —
not new assumptions introduced to rescue the claim — bound any
admissible covariantization regardless of the volume-convention
question:

- **Anchor 1 (§6's own exact result)**: separate-universe continuity at
  $k\to0$ — a super-horizon mode is locally a shifted background, so
  the field-side term's ratio to the gradient term cannot diverge as
  $k\to0$. Checked directly: a *fully local/pointwise* reading (the M5
  constraint acting on $\delta\phi_k$ with no window suppression at
  all, i.e. cancellation factor $\equiv0$) gives ratio $(aH/k)^2$,
  which **diverges** as $k\to0$ — excluded, since it would mean a
  super-horizon mode feels an M5 force its own shifted-background
  physics cannot contain. This is a *different* alternative from
  reading (A) (§9) — a third, "fully local" reading, now also ruled
  out, independently.
- **Anchor 2 (WP5's own established local decoupling)**: the
  cancellation must die off sub-horizon, recovering the full,
  $(aH/k)^2$-suppressed sliding-condensate term already established in
  the PPN sector (WP6 Step 2) — a *fully enslaved/pointwise-constraint*
  reading violates this from the other side.

**Verdict, independently checked and accepted**: these two anchors pin
the field-side term's cancellation factor to $\to1$ at $k\to0$ and
$\to0$ at $kR_h\gg1$ for *any* admissible covariantization — this part
does not depend on the $a^3\leftrightarrow R_h^3$ question at all, since
both anchors are statements about ratios/limits, not about the specific
volume normalization. **What the §12 catch genuinely demotes is
narrower than the whole term**: only the *detailed crossover shape* at
$kR_h\sim1$ (top-hat $W$ vs. a smoothed alternative, and the
volume-convention bookkeeping inside it) — not the term's existence or
its pinned asymptotic behavior.

**Reformulation adopted**: the field-side term is now written
$$-F_Q\big(1-\mathcal W(kR_h)\big)\times(A\text{-structure}),\qquad
\mathcal W(0)=1\text{ (exact, Anchor 1)},\quad\mathcal W\to0\text{ as
}kR_h\to\infty\text{ (Anchor 2)},$$
with $\mathcal W=$ the top-hat $W$ adopted as the **stated default**
(matching the census ball's own geometry, volume-convention bookkeeping
made explicit rather than silent), and the eventual low-$\ell$
deliverable carrying an explicit **window-shape systematic band**
(e.g. a Gaussian-smoothed alternative), the same way the RAR deliverable
already carries its own theory band. **The flags now on record**
— census-gauge status (§6), the fiducial-center caveat (§11), this
volume convention (§12–13), and (§14 amendment) the census-normalization
locality choice — **are consolidated under one name, accepted**: *the
census-sector covariantization freedom*, WP7's analog of WP6's own
$\mathcal Y$-sector scope statement — a bounded functional freedom to be
declared up front, with two physical anchors (separate-universe
continuity at $k\to0$; WP5's sub-horizon decoupling) plus, per §14's
amendment, matter-census invariance under facet 4, stated as exactly
what it cannot touch.

**Status**: the low-$\ell$ M5 signature is now on secure footing at the
level that matters for a first deliverable — its *existence* and
*asymptotic pinning* are established independently of the conceded
convention, while its *detailed crossover shape* is honestly carried as
a named, bounded systematic rather than a false precision. This is the
same "concede cleanly, keep what's actually independent, name the
remaining freedom" pattern this program has used successfully before
(WP6's own scope statements). Next concrete steps, unchanged in kind:
run the two exact numerical anchors ($k\to0$; §6's separate-universe
identity) as the assembly's brackets (both convention-independent, per
the advisory's own point 4); decide the census-weight-$Q$-dependence
channel explicitly; then the full numerical low-$\ell$/power-spectrum
solve, carrying the window-shape band as a stated systematic throughout.
Every result here inherits Gate 1(b)'s provisional-failure caveat.
Nothing in `cdot-7/` was touched.

## 14. Census-weight-$Q$-dependence channel decided — no, on the WP2 record

Per the advisory's own directive 2 (§4 of
`Advisory-WP7-QDefinitionAdjudicated-2026-07-18.md`: "decide it on the
WP2 record, in writing, not silently"), checked whether $E_P(t)$ and the
species exponents $p_i^\text{sp}$ — the two "census weights" — carry any
independent local-$Q$-dependence beyond what's already in $\bar{\mathcal
N}_i(t)$'s background trajectory. **Decided in
`cdot-8/WP2/Update-WP2-Addendum-CensusWeightQDependence-2026-07-19.md`:
no.** $E_P(t)=\sqrt{\hbar c(t)^5/G}$ is written in WP2's own foliation
integral with argument $(t)$ only, outside the spatial integral — a
single time-slice normalization, the same status as $\Lambda_M(t),Q(t)$
themselves in $S_{M5}$; $p_i^\text{sp}$ are fixed kinematic exponents
derived directly from WP1's Planck-unit relabeling (matter $p=5/2$,
radiation $p=1$, checked against known dilution laws, not fit), with no
argument that could carry $Q$-dependence in the first place.

**Consequence**: §5's density+volume decomposition of $\delta\mathcal
N_i$,
$$\delta\mathcal N_i(k,t)=\bar{\mathcal N}_i(t)\,W(kR_h(t))\,
\big[\delta_i(k,t)-3\Phi(k,t)\big],$$
is the *complete* linear-order decomposition — there is no missing
third, $\delta Q$-proportional channel riding on top of it. This closes
the one remaining item from the original Q-definition advisory's
directive list that hadn't yet been addressed (directives 1, 3, 4 were
covered in §12–13).

**Scope, stated explicitly, amended after advisor review**: this
decision addresses whether $E_P,p_i^\text{sp}$ *themselves* carry
$Q$-dependence, and answers no, based on rereading their own existing
definitions rather than adopting a new convention. **Amendment
(`Advisory-WP2-AddendumReviewed-2026-07-19.md`, accepted)**: the
original framing — that this is independent of the census-sector
covariantization-freedom item (§13) — drew the line one notch too
cleanly. The declined alternative (a *locally*-normalized census,
$E_P(x,t)$ from a ball-smoothed local $c$) is excluded by the
definitions as built, not by physics — so it is properly **facet 4** of
the same freedom item (alongside census gauge status, fiducial center,
the $a^3\leftrightarrow R_h^3$ volume convention), with this section's
"no" recorded as the *declared default*, not an independent closed fact.
**Sharpened, verified**: the facet couples per species as
$(p_i-\tfrac52)\delta c/c$, so **matter is exactly immune**
($p_m-\tfrac52=0$, the same cancellation zeroing $g_\text{matter}$'s
background $\dot c/c$ term) — only radiation-class censuses feel it.
The matter-era low-$\ell$ structure is convention-free on facet 4; a
third untouchable item (matter-census invariance) joins the freedom's
two physical anchors. **All four items from the original advisory's directive
list are now addressed**: (1) two-anchor numerical cross-check — done
in §12–13 (the anchors themselves confirmed convention-independent;
the full numerical run is still queued, see status below); (2) census
weights — decided, this section; (3) fiducial-center/census-gauge
caveat — carried forward as part of the consolidated covariantization-
freedom item (§13); (4) write-up — this document. Every result here
inherits Gate 1(b)'s provisional-failure caveat. Nothing in `cdot-7/`
was touched.

## 15. WP7 status, updated

**Structurally complete, on record, subject to Gate 1(b) throughout**:
the AeST perturbation system imports cleanly sub-horizon (§1–§2a); the
scalar sector's crossover-era breakdown is resolved by evolving field
variables directly, never building a fluid description (§7); the
low-$\ell$ M5 signature has both its Einstein-side term (§4–§6,
separate-universe-checked) and field-side term (§11, corrected and
re-secured at the asymptotic level in §13) on the record, with the
detailed crossover shape honestly carried as a named, bounded systematic
(*the census-sector covariantization freedom*) rather than false
precision; the census-weight channel is closed (§14) with no missing
term. **Not yet done, the concrete remaining queue**: run the two
convention-independent exact anchors ($k\to0$ cancellation; §6's
separate-universe identity) as numerical brackets on the assembled
system; then the full numerical low-$\ell$/power-spectrum solve, with
the window-shape band carried as a stated systematic throughout. Nothing
in `cdot-7/` was touched.

## 16. Running the two anchors as numerical brackets — Anchor 1 confirmed; Anchor 2 surfaces a major, unescalated problem with the whole "low-$\ell$" picture

**Built `wp7_anchor_brackets.py`** (saved to `cdot-8/WP7/`, reusing the
established trajectory and $R_h(s)$ machinery) to run the two anchors
as actual numerical brackets, per the accepted advisory's own directive
("the two exact numerical anchors... remain the assembly's brackets,
unchanged").

**Anchor 1 (k→0 separate-universe identity), evaluated along the real
trajectory**: the algebraic identity $F_Q/6+QF_{QQ}/2$ (§6) was never in
doubt as an identity, but evaluating it numerically shows it stays
**finite and smooth through the $\Omega_s=0$ crossing itself** ($z
\approx9640$: coefficient $\approx-7976$, comparable in size to
neighboring epochs) — confirming, with actual numbers rather than a
general argument, that this coefficient does not inherit the fluid
variables' ($w,c_\text{ad}^2$) divergence at the crossing. **One
honest caveat**: the coefficient *does* grow large much further into
the deep past ($z\sim10^6$) — but this is the **already-known,
separately-tracked** $F(Q)$ deep-radiation divergence from
`Update-WP3-QuadratureRedo-2026-07-13.md` (confirmed there as a genuine
feature of the particular solution, not a numerical artifact, tied to
the invoice's own small-negative radiation-era value), not a new
crossing-specific problem. Anchor 1: **confirmed**.

**Anchor 2 (sub-horizon decoupling), checked with real numbers instead
of the illustrative placeholder**: computed $R_h(z_*)$ in physical Mpc
(via the same $R_h(s)$ integration as §12, converted using $c_0/H_0=
4282.7$ Mpc) and compared directly against WP4a's own already-established
$r_s(z_*)=173.36$ Mpc and $D_p(z_*)=13074.3$ Mpc
(`Update-WP4a-AcousticScale-2026-07-16.md`):
$$R_h(z_*)=3.32\times10^{-3}\text{ Mpc} — \text{smaller than }r_s(z_*)
\text{ by }5.2\times10^4\text{, smaller than }D_p(z_*)\text{ by
}3.9\times10^6.$$
**This is a serious problem, not a refinement.** Every currently
observable CMB multipole corresponds to $k=\ell/D_p(z_*)$, and for
*any* $\ell$ from the quadrupole up through the highest resolved peaks,
$kR_h(z_*)$ comes out at $10^{-7}$–$10^{-4}$ — i.e. **every
observationally accessible scale sits deep in the $kR_h\ll1$ regime**,
where $W\to1$ and the field-side term's $(1-W)$ factor is negligible
($\lesssim10^{-3}$ even at $\ell=2$, and falling further at higher
$\ell$). Tabulated:

| $\ell$ | $k$ [Mpc$^{-1}$] | $kR_h(z_*)$ | $1-W$ |
|---:|---:|---:|---:|
| 2 | $1.5\times10^{-4}$ | $5.1\times10^{-7}$ | $1.4\times10^{-3}$ |
| 10 | $7.6\times10^{-4}$ | $2.5\times10^{-6}$ | $\sim10^{-6}$ |
| 220 (first peak) | $1.7\times10^{-2}$ | $5.6\times10^{-5}$ | $\sim10^{-8}$ |
| 2500 | $0.19$ | $6.3\times10^{-4}$ | $\sim10^{-8}$ |

**This directly contradicts the "$kR_h\sim6$ at the first acoustic
peak" identification used illustratively since §2a**
(`wp7_structure.py` Part A's table, labels like "~first acoustic peak
scale at $z_*$" attached to the placeholder value $kR_h=6$) — **that
labeling was never actually checked against the real $R_h(z)$
trajectory until this section**, and checking it now shows it is off
by four to six orders of magnitude. $R_h(z)$, built from $\dot R_h=c(t)$
with $c(t)\propto(a/a_0)^{2/3}\to0$ in the deep past, grows far more
slowly at early times than a standard particle horizon (whose
$dt/a$-type integrand *diverges* as $a\to0$, the opposite behavior) —
this is a genuine, checkable consequence of the variable-$c$
construction, not a numerical slip (cross-checked: $R_h(t_0)\approx1961$
Mpc, $0.46\times c_0/H_0$, a sane order-of-magnitude "horizon today";
the smallness is specific to early times).

**What this means, stated as carefully as I can**: it does *not* kill
the Einstein-side or field-side M5 terms as *structures* — §4–§6, §11,
§13's derivations stand as algebraic results. What it threatens is the
entire practical framing built since §2a: **if $R_h(z)$ is the correct
length scale entering $W(kR_h)$, then the "genuine, unavoidable new
low-$\ell$ M5 signature" is not merely small sub-horizon and $O(0.1)$
at low $\ell$ — it is negligible at *every* observationally accessible
scale**, because no accessible $k$ ever reaches $kR_h\sim1$. This would
substantially deflate, not merely refine, the significance of §2a
through §15's low-$\ell$ narrative. **Not declared a kill, escalating
instead**: this could mean either (a) the physical conclusion really is
this deflationary, and the low-$\ell$ M5 term is real but practically
unobservable given cdot-8's own $R_h(z)$, or (b) $R_h(t)$ — a quantity
WP2 built specifically to make $\mathcal N(t)$ reduce correctly to
cdot-7's *background* $M_h/m_P$ — is simply the wrong length scale to
use as the window's smoothing radius at the *perturbative* level, and
some other, larger scale (e.g. the standard causal/Hubble horizon,
or a scale tied to $D_p$ rather than to $c(t)$'s own suppressed
early-time integral) is what the physics actually requires. **This is
squarely the kind of consequential, uncertain fork this program
escalates rather than guesses on.** Recommending explicit advisor
input before any further numerical low-$\ell$ assembly is built on the
current $R_h(z)$ convention. Gate 1(b)'s caveat carried throughout.
Nothing in `cdot-7/` was touched.

## 17. §16 conceded in full (advisor error #8) — the phenomenology map inverts rather than vanishes: the signature lives in the growth history, not the acoustic peaks

`Advisory-WP7-PhenomenologyMapInverted-2026-07-19.md` +
`wp7_phenomenology_map.py`. **Reproduced the script before accepting
anything** — $R_h(z_*)=3.318\times10^{-3}$ Mpc and $R_h(\text{today})=
1961$ Mpc match my own `wp7_anchor_brackets.py` output to the digit; the
"elasticity" values check against my own independently-computed
$d\ln R_h/ds$ (e.g. $z=0$: $3\times2.184=6.55\Rightarrow-2.5/6.55=
-0.382$, matching the delivered $-0.381$).

**§16's $R_h(z_*)$ number is confirmed, and conceded as advisor error
#8**: the "$kR_h\sim6$ first acoustic peak" entry, used illustratively
since §2a and allowed to harden into a quoted "$\sim8\%$ window" across
two subsequent advisories, was never checked against the actual
$R_h(t)$ and is wrong by five orders of magnitude — an external
($\Lambda$CDM comoving-horizon) value imported into a variable-$c$
trajectory without computing, exactly the error class this program
polices, this time on the advisor's side, caught by the literal WP2
definition.

**But the corrected conclusion inverts §16's reading rather than
confirming it.** §16 checked $kR_h$ *at a single fixed epoch* ($z_*$)
and concluded the term is negligible at every observable scale — this
missed that $R_h(t)$ is itself time-dependent, so a mode's coupling is
not fixed by its $kR_h$ at one epoch. Each mode $k$ has an **exit
history**: $W\approx1$ (fully coupled, separate-universe regime) while
$R_h(t)<1/k$, decoupling once $R_h(t)$ grows past it. Computed
$z_\text{exit}(k)$ where $R_h(t)=1/k$: $z_\text{exit}\approx6.5$ for the
first-peak $k$, $\approx16$ for $k=0.1\,\text{Mpc}^{-1}$, $\approx56$
for cluster scales — **every observable mode was fully M5-coupled
through recombination**, exiting only during the matter era; the lowest
multipoles ($\ell\lesssim10$) are still transitioning today. This does
not contradict my own $R_h(z_*)$ number (still exactly right, and I
checked the right *quantity* — $kR_h$ at $z_*$ — I simply didn't follow
it through the mode's whole history before drawing the "negligible
everywhere" conclusion).

**Three regimes replace §2a–§16's picture**:

1. **At recombination, every observable mode sits at $W\approx1$**: the
   field-side $(1-W)$ term genuinely vanishes there ($\sim10^{-12}$, not
   the $\sim8\%$ two prior advisories asserted — both now erratum'd),
   but the Einstein-side term (§4–§6) is at *full strength* there — and
   at $W=1$ this is exactly the separate-universe-consistent linear
   response the background Friedmann equation already carries (the same
   $Q$-drag). **Required for consistency, but carries no distinctive
   $k$-shape at $z_*$** — Anchor 1 (§16) was telling us this all along.
2. **The distinctive $W$-shape survives only as a late-time,
   $\ell\lesssim10$ feature** (ISW-era, where $kR_h(t_0)\sim1$ for the
   lowest multipoles) — relocated from the acoustic peaks to the very
   largest scales today, not erased.
3. **New central item — the growth history**: during each mode's
   coupled era, the M5 response modifies the effective Poisson source by
   $(F_Q/6+QF_{QQ}/2)\,q'\bar{\mathcal N}$, with elasticity $d\ln Q/d\ln
   \mathcal N\approx-0.29$ to $-0.38$ (computed: $d\ln Q/ds=-5/2$
   against the matter-class census engulfment rate $3\,d\ln R_h/ds$,
   both reusing already-validated trajectory machinery). **Verified the
   printed magnitude directly**: ratios of $-0.58$ to $-0.67$ relative
   to the matter source through $z=30\to0$ — an $O(0.6)$, order-one
   effect (matching the advisory's own markdown prose, though its
   script's inline comment says "$O(\text{few-10\%})$," inconsistent
   with its own printed table — a minor, self-contained slip, noted for
   the ledger, not load-bearing). **This is explicitly a first
   estimate**: matter-class engulfment only, radiation-class census
   contributions to $\bar{\mathcal N}_\text{tot}$'s own evolution not
   yet included (the advisory's own directive 2 names this).

**Re-scoped statement for the record, replacing §2a/§8's "clean
sub-horizon import"**: the AeST perturbation system imports cleanly for
each mode *after* its exit epoch; during the coupled era, the
separate-universe M5 response to the growth equation must be carried.
WP5/WP6 remain untouched ($kR_h(\text{today})\sim10^5$–$10^9$ for
quasistatic/galaxy scales — verified in the script).

**Status**: §16's number stands; its "negligible everywhere" conclusion
is superseded by this mode-history picture. The growth-history term is
now WP7's central phenomenological deliverable (a $\sigma_8$-class
observable), and — per Gate 1(b) framing, unchanged — its central risk.
Concrete next steps, per the advisory's own directives, accepted: (1)
errata the two advisories that carried the $8\%$-first-peak claim; (2)
build the coupled-era growth equation properly (radiation-class census
terms added to the estimate above) as the first real numerical target;
(3) the late-time $\ell\lesssim10$ derivation follows, carrying the
window-shape band and facet-4 band, now both confined to the
late/very-large-scale regime; (4) fold $z_\text{exit}(k)$ into the
toolchain alongside the $R_h(s)$ integration. Gate 1(b)'s caveat carried
throughout. Nothing in `cdot-7/` was touched.

## 18. Own bug caught before further use: $R_h(s)$'s exponent was wrong (worker error, inherited unchanged by two advisor rounds) — corrected; the growth equation built with the exact $d\ln\mathcal N_\text{tot}/ds$

**While building the coupled-era growth equation** (the concrete next
step directed in §17), rechecked `wp7_lambda_extensivity_check.py`'s
$R_h(s)$ integration before extending it, and found it used
$dR_h/ds\propto e^{(2/3)s}$ — correct only if $s\equiv\ln(a/a_0)$, but
WP2's own record (`Update-WP2-CovariantCensus-2026-07-12.md`, the
$r,s,x(r,s)$ definitions) fixes $s\equiv\ln(c/c_0)$ explicitly, under
which $c/c_0=e^s$ *by definition* (coefficient 1, not $2/3$), and
$dt/ds=3/(2H)$. **Correct integrand**: $dR_h/ds=\tfrac32(c_0/H_0)
e^s/E(s)$. **This is a worker-side error** — introduced in §12's script,
then reused unchanged in §13's and §17's own follow-ups
(`covariantization_adjudication.py`, `wp7_phenomenology_map.py`), never
independently re-derived by either side across three rounds.

**Consequence, checked directly rather than assumed**: the qualitative
conclusions survive, with modest ($O(1)$) numerical shifts. $R_h(z_*)$
moves from $3.32\times10^{-3}$ to $9.54\times10^{-4}$ Mpc — **still
5–6 orders of magnitude below $r_s(z_*),D_p(z_*)$**, §16's core finding
unaffected (if anything, slightly reinforced). $R_h(\text{today})$ moves
from $1961$ to $2598$ Mpc. The mode-exit epochs shift modestly
($z_\text{exit}\approx6.0$ for the first-peak $k$, vs. the earlier
$6.5$; $\approx42$ for cluster scales, vs. $56$) but the qualitative
picture — full coupling through recombination, decoupling during the
matter era, only the lowest multipoles still transitioning near today —
is **unchanged**.

**The growth equation, built properly** with both fixes applied
(corrected $R_h(s)$; the *exact* $d\ln\mathcal N_\text{tot}/ds$ derived
below, not the matter-only estimate §17 flagged as incomplete):
per-species, WP2's evolution equation combined with WP1's density map
gives $d\ln\mathcal N_i/ds=d\ln\rho_{i,\text{phys}}/ds+3+3\,d\ln R_h/ds$
— and since every species shares the identical $(c/c_0)^7/E_P(t)$
bookkeeping factor and census-ball volume, $\mathcal N_i/\mathcal
N_\text{tot}=\rho_{i,\text{phys}}/\rho_\text{tot,phys}$ *exactly*,
giving
$$d\ln\mathcal N_\text{tot}/ds=d\ln\hat u/ds+3+3\,d\ln R_h/ds,$$
with $\hat u(z)$ the already-established total ordinary-matter density
(matter+radiation+neutrino, ratio to critical density — *not* the
scalar invoice, since $\mathcal N$ counts particle species, not the
scalar/vector field). This is now exact, not an approximation valid
only where matter dominates. **Result**: the coupled-era Poisson-source
modification stays at $O(0.5$–$0.7)$ through the matter era ($z=1090\to
0$), matching §17's estimate to within $\sim15\%$ — **the order-one
growth-history conclusion is robust to both corrections**, not an
artifact of either the $R_h$ bug or the matter-only approximation.

**Filed**: this $R_h(s)$ exponent slip as a new worker-side entry in
`ErrataAndMethodologyLog-2026-07-18.md` §2 — distinct from, but adjacent
to, errors #7/#8 (same script, different bug), caught this time by the
worker re-deriving the formula from WP2's own definition before
extending it, rather than by the advisor. Saved
`wp7_growth_equation.py` (superseding the exponent in
`wp7_lambda_extensivity_check.py`/`wp7_anchor_brackets.py` for any
future reuse) to `cdot-8/WP7/`. Gate 1(b)'s caveat carried throughout.
Nothing in `cdot-7/` was touched.

## 19. The late-time $\ell\lesssim10$ signature — where the field-side term turns on, identified

**Built `wp7_late_time_signature.py`** (saved to `cdot-8/WP7/`, reusing
the corrected $R_h(z)$ from §18), per the accepted advisory's own
directive 3. Defined a coupling profile $g(z;\ell)=k(z,\ell)R_h(z)$,
with $k(z,\ell)=\ell/D_p(z)$ the standard flat-sky relation between a
multipole and the wavenumber dominating its line-of-sight contribution
from redshift $z$ ($D_p(z)$: comoving distance *from us* to $z$, same
convention and machinery as WP4a's $D_p(z_*)$, now built as a function
of $z$ rather than evaluated at one point). $(1-W(g(z;\ell)))$ then
tracks, epoch by epoch, how strongly the field-side M5 term is "on" for
the mode dominating multipole $\ell$'s contribution from redshift $z$.

**Result**:

| $z$ | $\ell=2$ | $\ell=5$ | $\ell=10$ |
|---:|---:|---:|---:|
| 0.1 | 1.02 | 1.00 | 1.00 |
| 0.3 | 0.63 | 1.02 | 0.99 |
| 0.5 | 0.18 | 0.79 | 1.04 |
| 1.0 | 0.02 | 0.12 | 0.43 |
| 2.0 | 0.002 | 0.010 | 0.039 |
| 5.0 | $\sim10^{-4}$ | $\sim2\times10^{-4}$ | $\sim9\times10^{-4}$ |

**The field-side term is negligible ($\lesssim1\%$) by $z\gtrsim2$–$3$
and turns on to $O(0.1$–$1)$ over $z\sim0.3$–$1$** for
$\ell=2$–$10$ — **squarely inside the standard dark-energy-domination
window that sources the ordinary ISW effect** in $\Lambda$CDM-like
cosmologies. This identifies *where* (in redshift, for each low
multipole) the late-time signature is sourced — a genuine, derived
structural result, consistent with and sharpening §17's qualitative
"ISW-era" framing into an actual epoch range.

**Cross-checked independently**: evaluating the same $g(z;\ell)$ formula
at $z=z_*=1090$ gives $(1-W)\sim10^{-15}$–$10^{-14}$ for
$\ell=2$–$10$ — full coupling, matching §16–18's recombination-era
finding via a completely different construction (a continuous
$z$-dependent profile, not the fixed-$z_*$ table built earlier) — two
independent routes, same conclusion.

**What this is and isn't**: this identifies *where* the field-side
signature turns on, not yet the actual ISW power-spectrum modification
itself — that requires weighting this coupling profile by the genuine
time-derivative of the Weyl potential along the line of sight (the full
Bessel-function/line-of-sight projection), the next, harder numerical
step, explicitly not attempted here. The near-$z=0$ behavior (where
$D_p(z)\to0$ makes $k=\ell/D_p$ and hence $g$ formally divergent) is a
known coordinate feature of the flat-sky $\ell=kD$ approximation itself,
not a physical divergence — a genuine treatment needs the same care
standard ISW calculations already take near the observer.

**WP7 status, consolidated**: all four items from §17's directive list
are now addressed — errata filed (§17 follow-up), the growth equation
built exactly (§18), and the late-time signature's sourcing epoch
identified (here). **Remaining, honestly**: the two convention-
independent numerical anchors folded into the corrected system; the
actual ISW $\Delta C_\ell$ computation; and the eventual full
Boltzmann-style power-spectrum solve — all explicitly next-stage work,
not rushed. Gate 1(b)'s caveat carried throughout every result here.
Nothing in `cdot-7/` was touched.

## 20. Folding the two exact anchors into the fully corrected assembly

**Built `wp7_folded_anchors.py`** (saved to `cdot-8/WP7/`), consolidating
§18's corrected $R_h(s)$ and exact $d\ln\mathcal N_\text{tot}/ds$ into
one pipeline and running both anchors on it together, per the accepted
advisory's own standing directive ("the two exact numerical anchors...
remain the assembly's brackets, unchanged").

**Anchor A (k→0 separate-universe identity), on the corrected
pipeline**: confirmed the assembly introduces no arithmetic
inconsistency when the corrected $R_h(s)$ and exact $q'$ are combined
(residual $=0$ to machine precision). **Stated honestly**: this is a
regression/assembly check, not a fresh derivation of the identity itself
— that was already proven by direct differentiation in §6. What's new
here is confirming the *combination* of the two independently-corrected
pieces (§18) didn't silently break it. The Einstein-side coefficient
remains finite and smooth at every epoch checked on the corrected
numbers, consistent with §16's finding.

**Anchor B (kR_h≫1 sub-horizon decoupling), checked more sharply than
before**: as $kR_h\to\infty$ ($W\to0$), the field-side term
$-F_Q(1-W)\times(A\text{-structure})$ converges **monotonically and
exactly** to $-F_Q(\text{today})=-1.8538$ — not merely the same *order*
as WP6 Step 2's static $-F_QA^\mu$ term, but literally the **same
symbol, same numerical value**, since both derivations differentiate
the identical action term at the identical background epoch. Verified
the convergence numerically: at $kR_h=10^2$ the field-side coefficient
is already $-1.854$ (matching $-F_Q$ to 3 decimals), at $kR_h=10^6$ to
machine precision. **At $kR_h(\text{today})\sim10^5$–$10^9$** (galaxy/
solar-system scales, §13/§17), $(1-W)$ is already 1 to $>15$ decimal
places — **WP5/WP6's PPN and pulsar results are recovered with zero
residual correction on the fully corrected pipeline**, not just on the
earlier (buggy) one §18 fixed.

**Consolidated bracket table**, both anchors on the same trajectory:

| $z$ | Einstein-side coeff. ($k\to0$ limit) | field-side coeff. ($kR_h\to\infty$ limit, $\to-F_Q$) |
|---:|---:|---:|
| 1090 | $-6.5\times10^7$ | $-4473$ |
| 30 | $-4179$ | $-79.9$ |
| 1 | $-1.28$ | $-2.89$ |
| 0 | $0.016$ | $-1.854$ |

**Status**: both anchors hold cleanly on the fully corrected assembly —
the k→0 and sub-horizon brackets are secure, and the sub-horizon one is
now shown to be an *exact* recovery of an already-established WP6
number, not just an order-of-magnitude consistency check. This
completes the anchor-folding task; the remaining work is the genuinely
new numerical content (the ISW $\Delta C_\ell$ line-of-sight projection;
the full Boltzmann-style solve), not further verification of what's
already in hand. Gate 1(b)'s caveat carried throughout. Nothing in
`cdot-7/` was touched.

## 21. Attempting the ISW estimate surfaces a foundational, prior gap: does $\Omega_s$ cluster?

**Attempted a first, leading-order ISW $\Delta C_\ell$ estimate**
(`wp7_isw_estimate.py`, saved to `cdot-8/WP7/`): solve the standard
sub-horizon growth equation for $\delta_m(N)$ sourced by $\Omega_m(a)$
alone (the usual $\Lambda$CDM-style approach, treating the dark-energy-
like component as smooth/non-clustering), add the M5 correction as a
fractional enhancement using §18's coefficient and §19's window profile,
and compare the resulting ISW kernels ($\propto d\Phi/d\eta$) with and
without the M5 term, for $\ell=2,5,10$.

**The output was not trustworthy, and checking why surfaced a deeper
problem than a script bug.** The standard-case growth solution gave
$\Omega_m(z=50)=0.13$ — nowhere near matter domination, and the "standard
ISW kernel" peaked near $z\approx27$, both physically implausible for an
ordinary $\Lambda$CDM-like calculation. **Checked directly, not patched**:
computed cdot-8's own $\Omega_m,\Omega_\text{rad},\Omega_s$ decomposition
across the same epochs used throughout this document, and found
$$\Omega_s(z=50)=0.767,\quad\Omega_s(z=1090)=0.430,\quad\Omega_s(z=9640)
\approx0,\quad\Omega_s(0)=0.926.$$
**$\Omega_s$ is 40–90\% of the total energy budget at essentially every
epoch from $z_*$ to today** — utterly unlike $\Lambda$CDM's dark energy,
which is negligible until $z\lesssim1$. My growth-equation attempt
implicitly assumed $\Omega_s$ is smooth (non-clustering, sourcing $H(a)$
only, not $\Phi$) exactly as $\Lambda$CDM's $\Lambda$ is — **an
unstated, almost certainly wrong assumption for this model**, not a
minor simplification: if $\Omega_s$ clusters at all (and §2a already
established it is "dust-like," $w\approx0$, through the matter era —
exactly the equation of state a *clustering* component would have), it
would dominate structure growth entirely, giving a growth history
nothing like the artificially matter-suppressed one my script produced.

**This is a foundational gap, prior to and larger in scope than the
M5-specific ISW estimate**: whether and how $\Omega_s$ participates in
structure growth — via its own perturbations sourcing $\Phi$ through the
already-imported field-variable system ($\chi,\gamma,\alpha,\mathcal
E_\alpha$, §1) — has not been addressed anywhere in this WP7 arc. All
prior $\Omega_s$-perturbation discussion (§2a, §7) concerned the
*background* crossover and the *fluid-vs-field* description problem, not
whether $\Omega_s$'s perturbations gravitate at all. Given $\Omega_s$'s
sheer weight in the budget, this is not a detail to patch — it is
*the* question a trustworthy growth/ISW/power-spectrum calculation must
answer first.

**Not resolved here, explicitly not patched with an unreliable number**:
the $1.15\times$ kernel-power ratio my script produced (suspiciously
identical across $\ell=2,5,10$, consistent with the growth equation
being dominated by this mis-modeled $\Omega_s$ treatment rather than
genuine $k$-dependent M5 physics) is **not reported as a result** — only
as the symptom that surfaced this gap. **Recommending this be resolved
before any further growth/ISW/power-spectrum numerics are attempted**:
does cdot-8's own $\chi,\mathcal E_\alpha$ system source $\Phi$ through
its own perturbed stress-energy (analogous to quintessence-class
clustering, expected to be weak on sub-horizon scales for a light,
slowly-rolling field, but $\Omega_s$ here is not obviously in that
regime given its unusual, large, redshift-dependent weight), or does
some structural feature of the AeST action make it exactly smooth
despite its large background weight? This is squarely the kind of
consequential, uncertain fork this program escalates rather than
guesses on. Gate 1(b)'s caveat carried throughout. Nothing in `cdot-7/`
was touched.

## 22. Exploring the $\Omega_s$-clustering question while the advisor is unavailable — machinery validated against plain AeST, then applied to cdot-8's own trajectory

**Self-directed exploration**, per the author's own instruction to
investigate possible causes and validate the machinery against plain
AeST (no cdot-8/census assumptions) while the advisor is offline.
Built `wp7_aest_native_check.py` (saved to `cdot-8/WP7/`), in two parts.

**Part 1 — validating the machinery against AeST's own published,
closed-form result, with no cdot-8 content at all.** The founding paper
(arXiv:2007.00082, already archived) gives, for its native "sculpted
FRW" toy model $K(\bar Q)=-2\Lambda+\mathcal K_2(\bar Q-\mathcal Q_0)^2$
(the mechanism that makes AeST's scalar mimic CDM+$\Lambda$): $8\pi
\tilde G\bar\rho=Q\,dK/dQ-K$, $8\pi\tilde GP=K$, and a **general,
convention-invariant** adiabatic sound speed
$$c_\text{ad}^2=\frac{dP}{d\rho}=\frac{dK/dQ}{Q\,d^2K/dQ^2}$$
(invariant under any rescaling $K\to cK$, so it applies unchanged to
cdot-8's own $F(Q)$ despite the different normalization convention).
**Checked symbolically (SymPy), not assumed**: for this $K(Q)$,
$c_\text{ad}^2=(Q-Q_0)/Q$ exactly — reducing to the paper's own
perturbative $c_\text{ad}^2\approx2w_0/a^3$ in the small-deviation limit
($Q\to Q_0$). Integrating the paper's own field equation
$dK/dQ=I_0/a^3$ gives $Q(a)=Q_0+I_0/(2\mathcal K_2a^3)$ — substituting
into $\rho(a)$ gives **exactly** a genuine $1/a^3$ (dust) term plus a
constant ($2\Lambda$) term, reproducing the paper's claimed dust+CC
decomposition exactly, symbolically, with zero cdot-8 input. **This
validates the general $\rho,P,c_\text{ad}^2$ machinery this whole
session has used, against an independent, published, closed-form
target** — the kind of check this program has repeatedly found valuable
(K6 rule 7, absolute-anchor rule) and hadn't yet applied to this
specific formula.

**Part 2 — applying the same, now-validated formula to cdot-8's own
trajectory.** Computed $c_\text{ad}^2=F_Q/(QF_{QQ})$ numerically along
the already-established quadrature-solved $F(Q)$ trajectory (same
machinery reused throughout §16–21):

| $z$ | $c_\text{ad}^2$ |
|---:|---:|
| 3000 | 2.65 |
| 1090 | 2.10 |
| 100 | 1.33 |
| 30 | 1.28 |
| 10 | 1.29 |
| 3 | 1.45 |
| 1 | 1.94 |
| 0.3 | 2.82 |
| 0.05 | 3.74 |

**Reading**: unlike AeST's own native $K(Q)$, which is *engineered* to
keep $c_\text{ad}^2$ small throughout the Higgs-phase validity range
(that is the entire point of the $\mathcal K_2(Q-Q_0)^2$ term, so the
scalar clusters like dust) — **cdot-8's own quadrature-solved $F(Q)$
was never built with any such constraint**; it was reconstructed purely
to match the invoice $\Omega_s(a)$ curve, with no design goal imposed
on its curvature ($F_{QQ}$) shape. The result: $c_\text{ad}^2$ is
$O(1)$–$O(4)$ throughout the entire growth-relevant range ($z=0$ to
$z\sim3000$) — **quintessence-like, not dust-like**. This is the first
time this quantity has been computed for cdot-8's own trajectory in
this program.

**One consistency check, not a new concern**: near the $\Omega_s=0$
crossing ($z\sim7000$–$12000$), $c_\text{ad}^2$ swings through both
signs and grows large in magnitude — but this is the **already-known,
already-explained** crossing-era fluid-description breakdown (§2a: "at
the crossing, $w$ and $c_\text{ad}^2$ formally diverge... a generic,
well-understood feature of any fluid decomposition whose energy density
passes through zero"), not a new artifact. Also noted: the last 2–3
grid points immediately at $z=0$ show erratic values ($-15.7$, $-2.7$
against a smooth trend of $\sim4.0$ just before) — a boundary
finite-difference artifact of `np.gradient` at the array's endpoint,
excluded from the table above.

**What this does and doesn't settle**: $c_\text{ad}^2=O(1)$–$O(4)$
substantially de-escalates §21's blocker — it disfavors the "$\Omega_s$
clusters like dust" scenario I worried about, and lends real (if
preliminary) support to the standard "quintessence-class components
barely cluster on sub-horizon scales" approximation my rough ISW
attempt used, without knowing whether it applied. **It does not fully
settle the question**: a large, roughly-constant $c_\text{ad}^2$
strongly suppresses clustering on small/sub-horizon scales (the standard
mechanism), but doesn't rule out $O(1)$ effects at the very large scales
this document's own low-$\ell$/ISW work already cares about, and the
approximation of treating $\Omega_s$'s perturbations via a simple fluid
$c_\text{ad}^2$ at all, right through the already-flagged crossing, is
exactly the same fluid-vs-field tension §7 raised — a full treatment
still wants the field-variable ($\chi,\mathcal E_\alpha$) system, not
a fluid $c_\text{ad}^2$ alone. **Recommending this as independent
supporting evidence for the advisor's eventual review, not a
substitute for it.** Gate 1(b)'s caveat carried throughout. Nothing in
`cdot-7/` was touched.
