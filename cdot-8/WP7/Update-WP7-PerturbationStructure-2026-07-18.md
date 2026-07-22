# Update — WP7: Structural First Installment — Linear Perturbation Machinery Imported, the Genuinely New (Horizon-Scale) Question Posed

*Companion: `SessionLog-2026-07-18.md` and its per-day continuations
`SessionLog-2026-07-19.md`, `-20.md`, `-21.md` (split by calendar day
2026-07-21; entry numbering runs continuously across all four files).
Proceeds under
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

## 23. §22 Part 2 was a dictionary-transplant error — corrected; $\Omega_s$ answered: it clusters

`Advisory-WP7-OmegaSClusteringAdjudicated-2026-07-19.md` +
`omega_s_clustering_adjudication.py`. **Reproduced the script before
accepting anything** — every number matches (the $R_h$ spot-check to
the digit; the two-route $c_\text{ad}^2$ table; the budget shares).

**§18 confirmed, jointly owned.** The $s\equiv\ln(c/c_0)$ correction is
confirmed directly from the machinery's own $z$-map ($1+z=e^{-1.5s}$
combined with WP1's $1+z=(c_0/c)^{3/2}$ gives $c=c_0e^s$ — coefficient
one, exactly). The advisor notes their own "independent" reproduction
(§13) had copied my integrand's convention reading rather than
re-deriving from WP2's definition, while their *own* `wp7_structure.py`
correctly used $d\ln a=1.5\,ds$ elsewhere — an inconsistency inside
their own toolchain, never cross-checked, which is exactly how the bug
survived three rounds. New K6-class rule, accepted: convention factors
get re-derived from the defining document at first use in every new
script, never copied from a prior one, including one's own.

**§19–20 accepted**, with one cosmetic addition: table entries in §19
slightly exceeding 1 are real, not typos — $W$'s first negative lobe
(minimum $\approx-0.086$ near $kR_h\approx5.8$) makes $(1-W)$ peak
slightly above unity there.

**§22 Part 2 was a genuine error of mine — a dictionary transplant, not
a disagreement.** $c_\text{ad}^2=F_Q/(QF_{QQ})$ is exact *for AeST's own
map* $(8\pi\tilde G\rho,8\pi\tilde GP)=(QK_Q-K,\,K)$ — Part 1's symbolic
validation is correct, and stands, for that map. But **cdot-8's own
dictionary is $\rho_s=\tfrac12QF_Q-\tfrac13F$** (the Friedmann-constraint
combination this whole session has used and inline-verified against the
invoice to $10^{-4}$ since §2a) — a genuinely *different* combination of
$\{QF_Q,F\}$, not a rescaled version of AeST's own map. **Checked this
precisely, not just asserted**: writing $K=-\tfrac12F$ (the paper's own
stated identification) gives AeST's $\rho\propto-\tfrac12QF_Q+\tfrac12F$
— coefficient ratio $QF_Q\!:\!F=-1$ — against cdot-8's own ratio
$\tfrac12\!:\!(-\tfrac13)=-\tfrac32$. **These are not proportional**
(confirmed symbolically), so "invariant under $K\to cK$" — true, and the
basis of my own Part 1 validation — was answering the wrong question:
the transplant changed the *map*, not merely the scale, and invariance
under rescaling doesn't protect against that.

**The correct, map-independent computation**: $c_\text{ad}^2\equiv
\dot P/\dot\rho=w+\dfrac{dw/ds}{d\ln\rho_s/ds}$ — the standard adiabatic
sound-speed identity, using cdot-8's *own* already-validated $w(a)$ and
$\rho_s(a)=\Omega_s(a)$ trajectories directly, with no assumption about
the underlying $K(Q)$-type structure at all. Reproduced:

| $z$ | $w$ | $c_\text{ad}^2$ (cdot-8's own dictionary) | $c_\text{ad}^2$ (§22's transplanted formula) |
|---:|---:|---:|---:|
| 100 | $-0.030$ | $-0.041$ | $1.33$ |
| 30 | $-0.009$ | $-0.012$ | $1.28$ |
| 10 | $-0.006$ | $-0.004$ | $1.29$ |
| 3 | $-0.048$ | $-0.006$ | $1.45$ |

**The two routes disagree by two orders of magnitude in the matter era,
and the correct one is small, not $O(1)$–$O(4)$.** §22's de-escalation
*inverts*: cdot-8's scalar meets AeST's own founding-paper dust-like
clustering criteria ($\Pi\to0$, small $w$ *and* small $c_\text{ad}^2$)
almost exactly where structure actually forms.

**§21's blocker now answers structurally, not just numerically**: (i)
the budget leaves nothing else to cluster with — $\sim4.4\%$ baryons,
$\sim3\%$ massive neutrinos, $\sim77$–$92\%$ scalar from $z=50$ to today
(matching §21's own numbers exactly, unaffected by this correction); a
non-clustering $\Omega_s$ would mean no structure formation at all; (ii)
$w\approx0$ *and* $c_\text{ad}^2\approx0$ through the matter era, on the
corrected, map-independent computation; (iii) AeST's $Q$-sector was
*designed* to cluster like CDM — that is its entire dark-matter
mechanism, imported by cdot-8 wholesale. **$\Omega_s$ clusters,
dust-like, through the matter era.** My original ISW attempt's implicit
"smooth quintessence" assumption (§21) was wrong in the *opposite*
direction from §22's own attempted de-escalation — not a minor
refinement either way, but the resolution is now on solid, verified
ground: not reporting the mis-specified $1.15\times$ ISW ratio in §21
was the right call.

**The growth system is now fully specified, directive accepted**: dust-
like scalar clustering (via the imported $\Pi\to0$ evolution,
$\dot\delta_s=3\dot\Phi-\tfrac{k^2}{a^2}\theta_s$, $\dot\theta_s=\Psi$)
alongside baryons and massive neutrinos, plus the M5 coupled-era source
(§18's coefficient) with each mode's own exit history (§19), plus the
late-time $w\to$ negative transition where the same component turns
dark-energy-like — a unified DM$\to$DE component with a calculable
growth history. The field-variable care through the crossover (§7)
stands unchanged: the dust-like fluid form is licensed only where
$|\Omega_s|=O(1)$ and $w,c_\text{ad}^2$ are small — the matter era,
exactly where growth happens.

**Filed as a new worker-side entry in
`ErrataAndMethodologyLog-2026-07-18.md`**: a dictionary-transplant
error, K6-class lesson — a formula's validation certifies it for the
specific $(\rho,P)(Q)$ map it was validated on; transplanting it to a
theory with a different map requires re-deriving, not reusing, even
when the formula "looks" convention-invariant. Next: build the growth
system per the specification above — first sanity target, $\delta_s$
tracking $\delta_b$ in the matter era as the dustlike limit requires,
*then* add the M5 term and mode-exit structure. Gate 1(b)'s caveat
carried throughout. Nothing in `cdot-7/` was touched.

## 24. The growth system, built properly — sanity target passes; the M5 modification recomputed on a correctly-specified baseline, with one honest caveat carried forward

**Built `wp7_growth_system.py`** (saved to `cdot-8/WP7/`), implementing
§23's specification: since dust-like components ($w,c_\text{ad}^2$
small) share *identical* $\delta,\theta$ evolution equations with no
relative pressure support, $\delta_s=\delta_b$ for matched initial
conditions — collapsing to one growth equation sourced by
$\Omega_\text{eff}(a)=\Omega_b(a)+\Omega_s(a)$.

**Stage 1 — the sanity target, per the accepted advisory's own words**:

| $z$ | $\Omega_b$ | $\Omega_s$ | $\Omega_\text{eff}$ |
|---:|---:|---:|---:|
| 1090 | 0.169 | 0.430 | 0.599 |
| 100 | 0.138 | 0.753 | 0.890 |
| 50 | 0.134 | 0.767 | 0.901 |
| 10 | 0.131 | 0.779 | 0.910 |
| 1 | 0.102 | 0.829 | 0.931 |
| 0 | 0.044 | 0.926 | 0.970 |

**$\Omega_\text{eff}$ sits at $0.89$–$0.97$ throughout — the $\Omega_m(z{=}50)
=0.13$ symptom is gone**, exactly the resolution §23 predicted. Solved
the growth equation with this source: $\Phi$ stays close to constant
through the deep matter era ($z=100$ to $z\sim3$, ratio $0.94$–$1.01$),
the qualitatively correct behavior — a real, working baseline where the
earlier (mis-specified) attempt gave nonsense.

**Stage 2 — the M5 modification, recomputed on this corrected
baseline**: added §18's coupled-era coefficient, windowed by $W(kR_h(a))$
per §19's mode-exit profile, for the same representative $k(\ell=2,5,10)$:

| $\ell$ | $k$ [Mpc$^{-1}$] | $\Phi_\text{today}$ shift | ISW-kernel power ratio $P_\text{M5}/P_\text{std}$ |
|---:|---:|---:|---:|
| 2 | $1.08\times10^{-3}$ | $-82.4\%$ | $0.568$ |
| 5 | $2.71\times10^{-3}$ | $-80.1\%$ | $0.582$ |
| 10 | $5.41\times10^{-3}$ | $-77.4\%$ | $0.596$ |

**One honest caveat, carried forward rather than papered over**: $\Phi$
in the *baseline* (no-M5) system does not merely decay at low $z$ as
expected — it grows sharply ($\Phi/\Phi_i$ reaching $2.4$ at $z=0$),
which is *not* a sensible ISW-era potential-decay profile. This is not
a new bug: it is exactly the limitation the accepted advisory itself
named — "the dust-like fluid form is licensed only where $|\Omega_s|=
O(1)$ and $w,c_\text{ad}^2$ are small — the matter era." At low $z$,
$\Omega_s$'s own $w$ departs from zero (already established, $w\to
-0.68$ today) and the simple dust-treatment of $\Omega_s$ as a
pressureless source is no longer licensed — exactly the regime §7
already flagged as needing the field-variable ($\chi,\mathcal E_\alpha$)
system, not a fluid extension. **The Stage 2 numbers above therefore
carry this caveat directly**: they are a genuine improvement over §21's
completely mis-specified attempt (a properly-sourced baseline, at
least through the era where the dust approximation is licensed), but
the low-$z$ portion of the kernel — which is also where §19 found the
M5 term itself turns on — sits partly in the same regime where the
fluid treatment of $\Omega_s$ itself is not yet licensed. **Not treated
as a final number.**

**Status, stated honestly**: the sanity target passes cleanly (Stage 1);
the M5 modification is now computed on a correctly-specified matter-era
baseline rather than a broken one, giving $P_\text{M5}/P_\text{std}
\approx0.57$–$0.60$ as the current best estimate — but this still
needs the field-variable treatment through the low-$z$/ISW-relevant
range before being quoted as settled, since that is precisely where the
fluid approximation for $\Omega_s$ itself (not just the M5 term)
requires the more careful treatment §7 already called for. Recommending
this specific next step — replacing the low-$z$ fluid extension with
the actual $\chi,\mathcal E_\alpha$ field equations — before the ISW
$\Delta C_\ell$ number is treated as final. Gate 1(b)'s caveat carried
throughout. Nothing in `cdot-7/` was touched.

## 25. Attempting the general ($w,c_\text{ad}^2,\Pi$) system — the right equations found and verified from primary source; my own implementation broke, checkpointed honestly rather than patched

**Went back to the founding paper directly** rather than reconstruct
from memory or extend §24's ad hoc dust treatment further: quoted and
verified (arXiv:2007.00082, primary source, not the special-case
$\Pi\to0$ limit already imported in §1) the theory's **general** linear
fluid equations, valid for any $w,c_\text{ad}^2$:
$$\dot\delta=3H(w\delta-\Pi)+(1+w)\Big(3\dot\Phi-\frac{k^2}{a^2}\theta\Big),
\qquad\dot\theta=3c_\text{ad}^2H\theta+\frac{\Pi}{1+w}+\Psi,$$
$$\Pi=c_\text{ad}^2\delta-\frac{c_\text{ad}^2}{8\pi\tilde Ga^2\bar\rho}
\nabla^2\big[\mathcal K_BE_\alpha+(2-\mathcal K_B)\chi\big],\qquad
\mathcal K_B(\dot E_\alpha+HE_\alpha)=\frac{d\mathcal K}{d\mathcal Q}\chi
-(2-\mathcal K_B)\Big[\ldots\Big].$$
These are the genuine, general-$w$ replacement for §24's naive "always
dust" approximation, using cdot-8's own real $w(a),c_\text{ad}^2(a)$
(§23's corrected, map-independent formula) rather than assuming $w=0$
at all $z$.

**Attempted a first implementation, approximating $\Pi\approx
c_\text{ad}^2\delta_s$** (dropping the explicit $\chi,E_\alpha$
gradient term as a first, leading-order step — a standard approximation
on large/near-horizon scales in the dark-energy-perturbation
literature, not yet the full closure) **and it broke**: $\delta_b$ (the
*baryon* density contrast, which should stay positive and grow
monotonically in the matter era) went **negative** by $z\sim30$.
**Diagnosed rather than patched or hidden**: traced to an over-hasty
quasi-static/"drop $k$" shortcut in my own implementation, which
discarded the $k^2\theta/a^2$ and $\dot\Phi$ terms in a way that breaks
the equations' physical character entirely — not a subtlety in the
theory, a bug in this attempt's own simplification.

**Checkpointed honestly rather than pushed through with an unverified
fix.** This specific implementation is **not reported as a result** —
only §24's Stage 1/2 numbers stand as the current best (explicitly
caveated) figures. **What this round *did* establish, and what's
carried forward**: the correct general equations, verified against the
primary source rather than reconstructed from memory — a real
foundation for the next attempt, which needs to keep genuine
$k$-dependence and $\Phi$'s own dynamical (Poisson-sourced) evolution
rather than a quasi-static shortcut, and ideally close $\Pi$ properly
via $\chi,E_\alpha$ rather than the leading-order $c_\text{ad}^2\delta_s$
approximation. **Recommending this be staged as dedicated, careful next
work** — building the coupled $(\delta_b,\theta_b,\delta_s,\theta_s,
\Phi)$ system with actual $k$-dependence, matching this program's own
established discipline (WP3's LapseBackreaction round, WP6's staged PPN
derivation) of not forcing a shaky multi-variable derivation through
under time pressure. Gate 1(b)'s caveat carried throughout. Nothing in
`cdot-7/` was touched.

## 26. Advisor accepted on both issues; the field-variable system attempted a second time with a careful closure — it also failed, and this is now real signal, not bad luck

`Advisory-WP6WP7-Q2AndGrowthSnag-2026-07-19.md`, Issue 2 (Issue 1
assessed and recorded in `Update-WP6-TensorSpeedStructure-2026-07-18.md`
and `ConsolidationLog-2026-07-12.md` Item 16).

**The sharpened diagnosis, accepted in full.** §25's own $\Pi\approx
c_\text{ad}^2\delta_s$ shortcut was wrong on more than the dropped-$k$
count I'd flagged: (i) cdot-8's matter-era $c_\text{ad}^2$ is
*negative* ($-0.004$ to $-0.04$, §23) — an adiabatic closure with
$c_\text{ad}^2<0$ has an imaginary effective sound speed and manufactures
instability by construction, plausibly the primary cause of the
$\delta_b<0$ pathology, not merely a secondary numerical shortcut; (ii)
the standard dark-energy-literature approximation uses the *rest-frame*
sound speed $c_s^2$, not the *adiabatic* $c_\text{ad}^2$ — these differ
for field components precisely because $c_\text{ad}^2$ characterizes
the background trajectory's $P(\rho)$ history, while $c_s^2$ is set by
the field's own kinetic structure; transplanting the adiabatic form is
a structural cousin of §23's own dictionary error, correctly identified
as such; (iii) most decisively, the founding paper's own $\Pi$ formula
makes the $\nabla^2[\mathcal K_BE_\alpha+(2-\mathcal K_B)\chi]$ term
**the closure itself, not a correction to it** — dropping it, as §25
did, converts the field into exactly the pathological adiabatic fluid
it's supposed to avoid.

**Attempted the field-variable system a second time, with the closure
worked out carefully first** (unlike §25's rushed attempt): identified
that $\delta,\theta$ have their own *direct* evolution equations (no
need to invert their defining relations for $\gamma$ at all); $\chi=
\bar Q(\theta+\alpha)$ is algebraic once $\theta,\alpha$ are known;
$\alpha$ integrates via $\dot\alpha=E_\alpha-\Psi$; $E_\alpha$ via its
own quoted equation, using $F_Q$ (the *bare field equation's* own
coefficient, confirmed the right identification — this is what governs
$\nabla_\mu(F_QA^\mu)=0$ at every order per §7/§11/§13's own established
facts, genuinely different from $\rho_s$'s M5-modified Friedmann
combination, and correctly *not* repeating §23's dictionary error this
time); $\Phi$ via the momentum constraint (real $k$-dependence, no
quasi-static shortcut). **This closure is more careful than §25's, and
it still failed** — the solver broke down entirely (step size collapse,
invalid values), worse than §25's merely-wrong-sign result.

**Not patched a third time under pressure.** Two independent, carefully-
reasoned attempts failing at the same wall, each for a different
proximate reason, is exactly the pattern the accepted advisory warned
this system would show — direct, unambiguous confirmation of its own
recommendation to stage this properly rather than force it. **§24's
Stage 1/2 numbers remain the current best, explicitly caveated
figures.** Recommending this now genuinely be the dedicated, WP3-rhythm
round the advisory names — ideally with advisor cross-checking at each
stage rather than solo attempts, given two solo passes have both failed
in ways that took real effort to even diagnose. Not a kill of anything;
the structural understanding (the correct general equations, the
correct closure logic, the correct $F_Q$ vs. $\rho_s$ dictionary
distinction) is real, verified progress even though the numerical
system built on it isn't working yet. Gate 1(b)'s caveat carried
throughout. Nothing in `cdot-7/` was touched.

## 27. Stage 0 of the staged round, delivered by the advisor: the double failure diagnosed, and a genuine discovery — the scalar's own tachyonic, Hubble-tracking effective mass is the clustering mechanism

`Advisory-WP7-StiffnessAuditAndClusteringMechanism-2026-07-19.md` +
`wp7_stiffness_audit.py`. **Reproduced the script before accepting
anything**, and independently checked the closed-form algebra by hand.

**§26 accepted; the joint, WP3-rhythm staged round confirmed**, advisor
cross-checking at each stage, as requested. To start that round from
knowledge rather than a third blind attempt, its Stage 0 (a stiffness
audit) is delivered here.

**Three candidate killers audited, verdicts checked directly**:

- **K1 (effective-mass stiffness) — exonerated.** $\mu_\text{eff}^2=
  -\mathcal Q^2F_{QQ}/(2(2-\mathcal K_B))$ along the trajectory gives
  $|\mu_\text{eff}|/H\lesssim1$ at every epoch — no fast oscillator, the
  physical system is not intrinsically stiff if formulated in regular
  variables.
- **K2 (singular-factor map) — confirmed as the prime suspect, checked
  against my own §26 record directly**: the effective-fluid $\delta,
  \theta$ *definitions* carry $1/\rho_s$, $c_\text{ad}^2$, and
  $1/(1+w)$ factors ($|1/c_\text{ad}^2|\sim20$–$230$ throughout the
  matter era, not just at the crossing). **My own §26 state vector was
  literally $(\delta_b,\theta_b,\delta_s,\theta_s,\alpha,E_\alpha,
  \Phi)$** — exactly the flagged pattern. Standing rule accepted for
  the next attempt: state variables are $(\chi\text{ or }\gamma,\alpha,
  E_\alpha,\delta_b,\theta_b,\Phi)$ only — nothing whose *definition*
  contains $\rho_s,c_\text{ad}^2,$ or $1/(1+w)$; the effective-fluid
  quantities become output diagnostics computed afterward, not state.
- **K3 (units contract) — accepted as a co-suspect, sensible
  precaution.** $|F_Q|$ spans $4473$ ($z_*$) to $1.85$ (today) in
  $H_0^2$ units; the founding paper's own $dK/dQ$ lives in its own
  normalization. Accepted: write one dictionary line per imported
  equation before any code in the next attempt, pre-empting rather than
  re-discovering this class of error a third time.

**The discovery, verified independently before accepting**: in the
matter era, $F\propto\mathcal Q^{9/5}$ (already established), giving
$\mathcal Q^2F_{QQ}=n(n-1)F$ with $n=\tfrac95$ — **checked by hand**:
$n(n-1)=\tfrac95\cdot\tfrac45=\tfrac{36}{25}$, exactly matching the
advisory's own closed form. Combined with the established matter-era
attractor $F/\Omega_s\to30/17$ (WP3):
$$\frac{\mu^2}{H^2}=-1.271\,\frac{f_s}{2-\mathcal K_B}\approx-0.5\text{
to }-1\quad(\text{using }f_s\approx0.78\text{--}0.83,\ \mathcal K_B=
0.4355),$$
**a negative, Hubble-tracking effective mass, constant in ratio through
the matter era** — checked two ways (closed form vs. interior spline,
agreement to 1.6% at $z=10$: $889$ vs. $875$) — flipping to the
already-established stable sign ($F_{QQ}(0)=-0.696<0$) near today.

**Physical reading, accepted**: a tachyonic mass with $|\mu|<H$ is not
a Minkowski-stability pathology — it is a Jeans-class, Hubble-rate
growing mode, i.e. **the actual mechanism destabilizing the smooth
solution and making the scalar cluster**, switching off exactly when
the component turns dark-energy-like. This gives §23's structural
"$\Omega_s$ clusters, dust-like" conclusion a genuine *dynamical*
mechanism, not just a small-$c_\text{ad}^2$ diagnostic — and it is
$F_{QQ}(\mathcal Q_0)$'s **fourth** independent load-bearing appearance
in this program (condensate mass, stability sign, perturbed-constraint
feedback, now structure formation), the strongest coherence signal yet
for the zero-adjustable-parameters claim.

**Caveats carried forward, not resolved here**: the sign-flip epoch
needs a properly-splined (not endpoint/double-gradient) $F_{QQ}(z)$;
sub-horizon stability needs the full dispersion $\omega^2=c_s^2k^2+
\mu^2(z)$ with the $\mathcal Y$-sector's own $c_s^2$ (healthy at today's
anchor per SZ, epoch-dependence not yet checked); consistency with SZ's
own Minkowski stability conditions holds by scope (anchored at today's
point, where the sign is stable) but isn't a full check across epochs.

**The staged round's plan, now informed**: Stage 0 done (this audit);
Stage 1, a robust $F_{QQ}(z)$ and the dispersion relation (the growth
*rate* is now a genuine, checkable target); Stage 2, the units
contract; Stage 3, the pure field-variable system built on K2's rule,
an implicit solver as insurance, §24's Stage 1 as the regression target,
both anchors as brackets; Stage 4, the M5 term, mode exits, and the ISW
$\Delta C_\ell$. Each stage to be cross-checked before the next. Gate
1(b)'s caveat carried throughout. Nothing in `cdot-7/` was touched.

## 28. Stage 1: a robust $F_{QQ}(z)$ — and a significant, previously-unnoticed correction to an established anchor number, flagged for advisor review before propagating

**Built `wp7_stage1_FQQ_robust.py`** (saved to `cdot-8/WP7/`), per the
advisory's own directive. Rather than smooth the existing double-finite-
difference chain (F$\to$F_Q via one numerical derivative, F_Q$\to$F_QQ
via a second), **derived $F_Q,F_{QQ}$ analytically from the defining
quadrature integral**, removing a derivative from the chain entirely:
since $F(s)=\mathcal Q(s)^{2/3}G(s)$ with $dG/ds=-5\mathcal Q^{-2/3}
\Omega_s$ exact by the fundamental theorem of calculus (no finite
difference at all), and $d\mathcal Q/ds=-2.5\mathcal Q$ exact,
$$F_Q=\frac23\frac F{\mathcal Q}+2\frac{\Omega_s}{\mathcal Q},\qquad
F_{QQ}=-\frac29\frac F{\mathcal Q^2}-\frac23\frac{\Omega_s}{\mathcal Q^2}
-\frac45\frac{d\Omega_s/ds}{\mathcal Q^2}$$
— only *one* numerical derivative anywhere in the chain (of $\Omega_s$,
a smooth quantity), not two chained ones. **Cross-checked against the
old method away from the boundary**: agrees to 4+ significant figures
everywhere from $z=9640$ down to $z\sim1$.

**A significant discrepancy surfaced right at $z=0$, and it does not
resolve as expected.** The old method gives $F_{QQ}(0)=-0.696$ (the
figure already cited in three places in this program: WP5's condensate
mass, the SZ stability check, and §27's own tachyonic-mass finding); the
new analytic method gave $+0.43$ at the literal $z=0$ grid point —
disagreeing in *sign*. **Diagnosed rather than picked a side**:
$s=0$ ($z=0$) is not just noisy, it is the *literal edge* of the
integration domain (`solve_ivp` starts its integration at $s=0$ and
runs backward) — no differentiation scheme, old or new, is reliable
exactly at a domain boundary. **Fixed at the root**: extended the
integration slightly past $s=0$ (into $z<0$, mathematically fine for a
smooth ODE) so that $z=0$ becomes a genuine *interior* point. **Three
independent methods then agree closely**: the analytic formula above
($-0.1692$), a centered finite difference on the same analytically-
computed $F_Q$ ($-0.1675$), and a plain double finite difference
applied directly to $F$ on the now-extended domain ($-0.1671$) — all
within 1% of each other.

**Conclusion: $F_{QQ}(\mathcal Q_0,\text{today})\approx-0.17$, not
$-0.696$.** The previously-established $-0.696$ figure was a domain-
boundary numerical artifact (computing a derivative at the literal edge
of a numerically-solved ODE), not an independent, robust result — it
was reproduced identically by the *same* method in a second script
(`meff_skeleton.py`), which is reproducibility of a shared artifact, not
independent verification.

**What this does and does not change, stated carefully**:

- **The SZ stability conclusion is unaffected**: $F_{QQ}$'s *sign*
  survives ($-0.17<0$, same as $-0.696<0$), so $\mathcal K_2=-\tfrac14
  F_{QQ}>0$ still holds — the stability condition is still satisfied,
  just with a smaller margin than previously stated.
- **WP5's condensate-mass numbers ($\mu^{-1}\approx5$–$10$ Gpc,
  $r_c\approx64$–$100$ Mpc) need revision**, but very likely in the
  *reinforcing* direction: $\mu^2\propto|F_{QQ}|$, so a $\sim4\times$
  smaller $|F_{QQ}|$ gives a $\sim2\times$ smaller $\mu$, i.e. an even
  *larger* Compton wavelength — the "condensate negligible at every
  observationally accessible scale" conclusion should survive and
  strengthen, not weaken, but the specific numbers are now flagged as
  provisional pending recomputation.
- **§27's own tachyonic-mass finding is refined, not overturned**: with
  the robust $F_{QQ}(z)$, $\mu^2/H^2$ still runs negative through most
  of the matter era ($\approx-0.6$ near $z\sim10$, matching §27's
  closed-form estimate closely) but **the sign-flip epoch is now
  precisely $z\approx0.13$–$0.15$** (not loosely "near today" as
  originally read), with $\mu^2/H^2(0)\approx+0.05$ — small and
  positive, a much narrower stable margin today than §27's language
  suggested.

**The dispersion relation, a first estimate**: using $c_s^2=1$
(canonical, from the $\mathcal Y$-sector's own established healthy-mode
structure, WP6) and the corrected $\mu^2(z)$, the comoving Jeans
wavelength for this tachyonic instability comes out at
$\sim5\times10^4$–$1.7\times10^5$ Mpc across $z=0.2$–$3$ — **an order of
magnitude *larger* than the Hubble radius today** ($c_0/H_0\approx4283$
Mpc), comparable to or larger than the $\ell\sim2$ CMB scale itself
($k\sim1.5\times10^{-4}$ Mpc$^{-1}$ at $z_*$, from §19's own table).
**This refines the physical picture significantly**: the tachyonic
growing-mode mechanism, if it operates at all on scales relevant to
observation, does so only at the very lowest CMB multipoles
($\ell\lesssim2$–$3$, narrower than the $\ell\lesssim10$ window already
established for the M5 term), **not at sub-horizon, galaxy-formation
scales** — ordinary structure formation (galaxies, clusters) must still
be explained by the scalar tracking baryons gravitationally (the
$\delta_s\approx\delta_b$ argument, §24), not by this intrinsic
instability. **Stated honestly as a first, order-of-magnitude estimate**:
$c_s^2$'s actual epoch-dependence (vs. assumed canonical/constant) has
not been checked, and this Jeans-scale figure should be treated as
illustrative pending that check.

**Recommending explicit advisor review of the $F_{QQ}(0)$ correction
before it is propagated into WP5's own numbers or Foundation.md's
citations** — this revises a figure used in three places across the
program, even though every qualitative conclusion built on it appears
to survive. Not treated as settled until cross-checked. Gate 1(b)'s
caveat carried throughout. Nothing in `cdot-7/` was touched.

## 29. §28 confirmed by the secondary advisor (Fable 5 unavailable on
token limits) — accepted, with one propagation detail corrected before use

`Advisory-WP7-FQQCorrectionConfirmed-2026-07-20.md` +
`wp7_fqq_correction_crosscheck.py`, from the secondary advisor (Opus
4.8), routed here per the program's own escalation practice while the
primary advisor is unavailable. **Reproduced the script myself before
accepting anything** — all four checks ran exactly as reported (Check 1:
$-0.6962$, reproducing the edge artifact precisely; Checks 2–3: $-0.1692$
/ $-0.1675$, agreeing with the old method to $0.0001$–$0.01\%$ away from
the boundary).

**The core confirmation is solid and independently re-derived, not just
re-run**: the secondary advisor rebuilt the $s\leftrightarrow z$
convention and the $F(\mathcal Q)$ quadrature from `Foundation.md`
directly rather than copying either prior script (correctly applying the
K12 convention-re-derivation rule), and independently re-derived the
analytic $F_{QQ}$ formula term-for-term by hand. $F_{QQ}(\mathcal Q_0,
\text{today})\approx-0.169$ is now confirmed by three independent
implementations (mine, twice over, and the secondary advisor's), not
two. **Accepted outright.**

**One propagation detail in the secondary advisor's Check 4 needed
correcting before use, caught by checking against the actual source of
WP5's quoted numbers rather than trusting the check's own framing.**
Check 4 propagated the correction using `meff_skeleton.py`'s simplified
condensate-mass formula (which implicitly fixes $2-\mathcal K_B=1$,
i.e. $\mathcal K_B=1$ only) — but WP5's actually-quoted band
($\mu^{-1}\approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc) was computed by
`meff_exact_dictionary.py`, scanning $\mathcal K_B$ over AeST's full
stable range $(0.1$–$1.5)$, not a single value. **Checked directly**:
Check 4's own "old" figure ($1/\mu_\text{eff}=7260$ Mpc) exactly
reproduces the $\mathcal K_B=1.0$ row of the original scan — confirming
it used only one point of the required range, not the range itself.
**Recomputed properly** (same exact-dictionary formula, same
$\mathcal K_B$ scan, corrected $F_{QQ}\approx-0.169$):
$$\mu^{-1}\approx10\text{--}20\text{ Gpc},\qquad r_c\approx100\text{--}
160\text{ Mpc}$$
— roughly $2\times$ and $1.6\times$ the original band, not the
"$14700$–$14800$ Mpc, $129$–$130$ Mpc" Check 4 reported (which was one
$\mathcal K_B$ value's worth of the correct new band, not the band
itself). The secondary advisor's *qualitative* claim ("the condensate
conclusion strengthens") is exactly right; only the specific quoted
range needed the correct formula's full $\mathcal K_B$ scan to be
accurate. This is a understandable gap for a secondary advisor without
the full session record (which script generated which quoted number is
exactly the kind of detail that lives in session history, not in
`Foundation.md`/`Progress.md` alone) — not a substantive error in the
core physics.

**Propagated**: `Foundation.md` §7/§8 and `Update-WP5-
WeakFieldStructure-2026-07-17.md` now carry the corrected $F_{QQ}(0)
\approx-0.169$ and the correctly-rescanned condensate-mass band. §27's
sign-flip epoch ($z\approx0.13$–$0.15$, $\mu^2/H^2(0)\approx+0.05$) is
confirmed as stated, independently re-derived by the secondary advisor
from their own Check-2 output. `ErrataAndMethodologyLog` K14 marked
confirmed (§ next). Gate 1(b)'s caveat carried throughout; the
$\Omega_s$-clusters-dust-like conclusion is unaffected (it rests on
three independent arguments, none of which touch $F_{QQ}(0)$
specifically — the tachyonic mechanism is a fourth, supporting line, not
the basis). Nothing in `cdot-7/` was touched.

## 30. Stage 2 — the units contract, written before any code, per the accepted advisory's own directive

Per K3/the accepted staging plan: one written dictionary line per
imported equation, resolved and cross-checked *before* attempting Stage
3's implementation, precisely to pre-empt a third failure of the same
class that broke both prior attempts.

**Contract line 1 — time variable.** The founding paper's dots are
**cosmic-time** derivatives: confirmed directly from primary source
($H\equiv\dot a/a$, dot notation used consistently throughout their
perturbation section, not conformal-time primes). Both prior attempts
integrated in **e-fold time** $N=\ln a$. Since $dN/dt=H$ exactly,
$$\dot X=H\,\frac{dX}{dN}\quad\text{for any quantity }X$$
— every imported cosmic-time equation must be divided through by $H$
before use as a $d/dN$ evolution equation. **Checked this was actually
done consistently in both prior attempts — it was not stated as an
explicit contract line either time**, which is itself informative:
neither attempt's failure mode (§25's sign-wrong result; §26's solver
collapse) can be blamed on this specific step alone, since both scripts
did include *some* $H$-division, but neither had it written down and
checked as a standalone item — exactly the gap this contract line
closes.

**Contract line 2 — a second, previously-unexamined normalization
subtlety in the imported $\mathcal E_\alpha$ equation specifically,
found while writing this contract.** The founding paper's own
$dK/dQ$ notation in the $\mathcal E_\alpha$ evolution equation is
*not* the same object as the bulk-current coefficient $F_Q$ already
used (correctly, and independently cross-checked against WP6's PPN
work to machine precision, §20) in the $-F_QA^\mu$ term. **Checked
directly from primary source**: the paper defines $K(\bar Q)\equiv
-\tfrac12F(0,\bar Q)$ specifically so their illustrative "sculpted
FRW" toy action (its own $1/(8\pi\tilde G)$ normalization) reproduces
the *same* physics as the full covariant action (its own $1/(16\pi
\tilde G)$ normalization) — the factor of $-\tfrac12$ exactly
compensates the $8\pi$-vs-$16\pi$ prefactor mismatch between the toy
model and the real action, algebraically confirmed
($\tfrac1{8\pi\tilde G}K=\tfrac1{8\pi\tilde G}(-\tfrac12F)=-
\tfrac1{16\pi\tilde G}F$, matching the real action's own term exactly).
The $\mathcal E_\alpha$ equation's "$dK/dQ$" is background-only
($Y=0$) notational shorthand for $-\tfrac12F_Q(\text{background})$,
reused from the toy-model section — **not** the same object as the
field equation's own bulk current coefficient (which comes from
varying the *full* covariant action directly, confirmed by direct
variation: $\partial\mathcal L/\partial(\nabla_\mu\phi)\supset-F_Q
A^\mu$ on an FRW background with $\mathcal Y=0$, $J^\mu=0$,
$\hat F_{\mu\nu}=0$ — genuinely $F_Q$, not $-F_Q/2$).

**Cross-checked independently before trusting this distinction**:
WP5's own, separately-established condensate-mass relation $\mathcal
K_2=-\tfrac14F_{QQ}(\mathcal Q_0)$ is *only* consistent with $K=-
\tfrac12F$ (giving $d^2K/dQ^2=-\tfrac12F_{QQ}$, hence $\mathcal K_2=
\tfrac12(d^2K/dQ^2)=-\tfrac14F_{QQ}$ — matching WP5's own relation
exactly). This is an independent confirmation, not just an algebraic
consistency check on my own new claim: **the $\mathcal E_\alpha$
equation's coefficient must be $-\tfrac12F_Q$, not $F_Q$** — a genuine
correction to both prior implementation attempts, which used bare
$F_Q$ there.

**Contract line 3 — the gradient/$k$-normalization.** $k$ in the
imported equations is a physical comoving wavenumber (Mpc$^{-1}$); the
natural dimensionless combination for the $H_0$-unit convention used
throughout this program is $\kappa\equiv(k/(aH_0))^2$, with the
$k^2\theta/a^2$-type terms becoming $\kappa H_0^2\theta/E(z)^2\times
E(z)^2=\kappa\theta$ after full non-dimensionalization consistently
with $H\to E(z)$, $a\to e^N$ (checked: this recovers the already-
validated $\kappa=k^2/(a^2H_c^2)$ form used in §24's own working
script for the analogous term).

**Contract line 4 — background identifications, already established
and reused unchanged**: $\dot{\bar\phi}=\mathcal Q(t)$ (cdot-8's own
established $\mathcal Q(s)=e^{-2.5s}$ trajectory, matching directly,
no rescaling); $\rho_s,w,c_\text{ad}^2$ in the already-validated
$\Omega$-normalized, $H_0^2$-unit convention (§18, §23, §24); the
Poisson/momentum-constraint normalization matching $8\pi G\rho_I/
(3H_0^2)=\Omega_I$, the same convention §24's Stage-1 sanity check
already validated (giving $\Omega_\text{eff}\approx0.89$–$0.97$, $\Phi$
roughly constant in the matter era).

**Status**: the units contract is now written and cross-checked term
by term, with one genuine, previously-unexamined error caught and
corrected (contract line 2, the $\mathcal E_\alpha$ coefficient) before
any further code is attempted — precisely the outcome Stage 2 was
designed to produce. Ready for Stage 3 (the pure field-variable
rebuild under K2's state-variable rule), recommended to be attempted
with this contract checked against the advisor before coding, per the
accepted staging discipline. Gate 1(b)'s caveat carried throughout.
Nothing in `cdot-7/` was touched.

## 31. Stage 2 confirmed directly against primary source — cleared for Stage 3

`Advisory-WP7-Stage2UnitsContractConfirmed-2026-07-20.md`, secondary
advisor. **Verified independently before accepting**: checked every
quoted line directly against the archived primary source
(`references/arXiv.2007.00082/newRMONDLett.tex`) myself — $\mathcal K(
\bar Q)=-\tfrac12\mathcal F(0,\bar Q)$ (line 355), the toy action's
$\tfrac1{8\pi\tilde G}$ vs. the full action's $\tfrac{\sqrt{-g}}
{16\pi\tilde G}$ prefactors, the $\mathcal K_2(\bar Q-\mathcal Q_0)^2$
expansion definition, and the $\mathcal E_\alpha$ equation's exact
parenthesization ($\mathcal K_B(\dot{\mathcal E}_\alpha+H\mathcal
E_\alpha)=\ldots$) — all match exactly, word for word.

**Contract Line 2 is now confirmed by direct textual match, not just
internal algebraic consistency** — the strongest verification available
short of an independent field-theory re-derivation, and not needed here
since the paper states the result directly: the coefficient is
literally written as $d\mathcal K/d\mathcal Q$, the paper's own toy-model
symbol, confirming $-\tfrac12\mathcal F_Q(\text{background})$ is correct
for this specific equation, distinct from the bulk-current $\mathcal
F_Q$ used elsewhere. Both prior implementation attempts (§25, §26) used
the wrong one.

**The secondary advisor also owned their own §29 Check-4 error outright**
— no correction needed on my side, already resolved in §29.

**One methodology note worth keeping**: the secondary advisor initially
re-checked this via a fresh `WebFetch`/`pdftotext` extraction of the
arXiv PDF, which lost the $\mathcal E_\alpha$ equation's parenthesization
and left the question genuinely ambiguous, before finding and using the
already-archived `.tex` source instead. Good general lesson, now
recorded in `references/arXiv.2007.00082.md`'s own status note: check
`references/` for an already-archived primary source before fetching a
fresh copy of a paper already in this program's citation list.

**Status: Stage 2 fully cleared, by both the worker's and a second,
independent primary-source check.** Ready to proceed to Stage 3 — the
pure field-variable rebuild under K2's state-variable rule
($\chi\text{ or }\gamma,\alpha,\mathcal E_\alpha,\delta_b,\theta_b,\Phi$
only), using $d\mathcal K/d\mathcal Q=-\tfrac12\mathcal F_Q$ in the
$\mathcal E_\alpha$ equation specifically and bare $\mathcal F_Q$ only in
the bulk-current/field-equation term. Gate 1(b)'s caveat, the $Q_2$/EFE
sequencing decision, and the KATRIN watch item are all unchanged.
Nothing in `cdot-7/` was touched.

## 32. Stage 3 attempted — real progress on the dust sector, a genuine new instability found and localized to the vector sector, checkpointed rather than forced

**Worked out the closure carefully before coding**: $\theta\equiv\delta
\phi/\dot{\bar\phi}$ means $\delta\phi=\dot{\bar\phi}\theta$, so $\chi\equiv\delta
\phi+\dot{\bar\phi}\alpha=\dot{\bar\phi}(\theta+\alpha)$ — **recoverable from
$\theta,\alpha$ alone, no $\gamma$ needed** — resolving an apparent gap
in K2's own state-variable list (which names only "$\chi$ or $\gamma$,"
not both). This makes $(\delta_b,\theta_b,\delta_s,\theta_s,\alpha,
\mathcal E_\alpha)$ a valid, complete 6-variable state (matching the
system's actual 4 vector-scalar + 2 baryon degrees of freedom), with
$\Phi$ treated algebraically via the sub-horizon Poisson equation
(matching §24's own convention; the momentum-constraint/super-horizon
refinement deferred to Stage 4, where the M5/mode-exit machinery lives
anyway). $\Pi$ computed via the **full** formula (not the
$c_\text{ad}^2\delta_s$-only approximation that broke §26), using
$\chi=\mathcal Q(\theta_s+\alpha)$ and the confirmed $d\mathcal K/d
\mathcal Q=-\tfrac12F_Q$ coefficient in the $\mathcal E_\alpha$
equation.

**Regression check against §24 (Stage 1), per the advisor's own
recommendation**: with $\Pi$ forced to zero (vector sector artificially
decoupled), the dust-sector system now gives $\Phi$ staying at
$0.94$–$1.00$ through the matter era, **decaying smoothly to
$\Phi/\Phi_i=0.50$ by $z=0$** — genuinely *better* than §24's own
regression target (which had $\Phi$ pathologically *growing* to $2.4
\times$ at low $z$): keeping $w(z)$'s actual transition in the
$\delta_s$ equation, rather than §24's "always dust" shortcut, gives the
qualitatively correct ISW-type decay. **This part is solid.**

**The full system, with $\Pi$ properly included, blows up** — and not
from the numerical-conditioning issue it first looked like. Tried a
$10\times$ smaller $k$ to reduce the dynamic range of $\kappa=(k/(aH_0)
)^2$ (which spans $\sim10^5$ to $\sim10$ from $z=100$ to today for
$k=10^{-3}\,\text{Mpc}^{-1}$) — this reduced the blowup's overall scale
by many orders of magnitude but did **not** fix it: values are already
$10^{10}$–$10^{18}$ just one integration step past $z=100$, a fast-onset
instability, not a slow numerical drift. **This localizes the problem**:
Stage 0's own stiffness audit only checked the *scalar* condensate
sector's effective mass ($\mu_\text{eff}^2\propto F_{QQ}$) and found it
safe ($|\mu_\text{eff}|/H<1$ everywhere) — **it never audited the
vector/$\mathcal E_\alpha$ sector's own dynamics**, which is exactly
where this new attempt's instability appears to live.

**Checkpointed rather than forced further.** Two genuine pieces of
progress stand: the dust-sector regression not only reproduces but
*improves on* §24's own target, and the closure gap (whether $\chi$ or
$\gamma$ is needed) is now resolved cleanly. The concrete, narrow next
step — **not yet attempted, and different in kind from Stage 0's own
scalar-sector audit** — is a dedicated stiffness/stability audit of the
$\mathcal E_\alpha$/$\alpha$ (vector) sector specifically: what is this
system's own effective oscillation/growth rate, independent of the
scalar condensate mass already cleared? Recommending this as the next
dedicated, advisor-cross-checked step, per the same staging discipline
that has served this program well twice already (§25, §26) rather than
a further solo patch attempt. Gate 1(b)'s caveat carried throughout.
Nothing in `cdot-7/` was touched.

## 33. §32's instability diagnosed by the secondary advisor: a genuine, large real eigenvalue in the untested vector sector, switched on by the $\Pi$-feedback term — confirmed independently, plus one additional cross-check found in the primary source

**Advisory**: `Advisory-WP7-Stage3VectorInstabilityDiagnosed-2026-07-20.md`
+ `wp7_stage3_vector_stiffness_audit.py`. Built the local $2\times2$
Jacobian of $(\alpha,\mathcal E_\alpha)$ alone (freezing $\delta_s,
\theta_s,\Phi$ as slowly-varying external sources — the standard way to
audit a fast subsystem independent of the slow one it's embedded in),
reusing §32's own trajectory and the confirmed Stage-2 $d\mathcal K/d
\mathcal Q=-\tfrac12F_Q$ coefficient directly. Found: a genuine large
**positive real** eigenvalue at high $z$/large $\kappa$ (e.g.
$\{-13.2,+485\}$ at $z=100$, $k=10^{-4}\,\text{Mpc}^{-1}$ — exactly
reproducing §32's actual blowup), settling into a stable, damped complex
pair by $z\sim10$; setting $\kappa=0$ gives a stable complex pair at
every epoch, so the instability is switched on entirely by the
$\Pi$-feedback term; a clean critical $\kappa(z)$ bifurcation exists,
with the corresponding critical comoving $k$ tiny ($\sim10^{-7}$ to
$\sim10^{-4}\,\text{Mpc}^{-1}$ from $z=1090$ to $z=10$) — essentially
every cosmologically relevant $k$ sits on the unstable side once
$z\gtrsim$ a few tens.

**Independently reproduced, not accepted on say-so**: ran
`wp7_stage3_vector_stiffness_audit.py` myself end to end — every number
in the advisory reproduced exactly (eigenvalues, the $\kappa=0$ stable
pair, the critical-$\kappa$ scan). Also checked the advisory's own
analytic-trace cross-check (the dominant $\partial\dot{\mathcal
E}_\alpha/\partial\alpha$ term, $-(2-\mathcal K_B)^2c_\text{ad}^2\kappa
\bar{\mathcal Q}^2/[\mathcal K_BH_c(1+w)]$) against the coded Jacobian's
own entry at $z=100$: formula gives $3.72\times10^6$, the coded entry is
$3.68\times10^6$ — matches to $\sim1\%$. Separately verified the
Jacobian construction itself is a faithful linearization of
`wp7_stage3_field_variable.py`'s actual `rhs()` (differentiated $\Pi$,
$\chi$, and the $\mathcal E_\alpha$ equation by hand term-by-term against
the coded partials) — this is not a from-scratch reconstruction that
happens to agree, it is the same equations. **Diagnosis accepted.**

**One open item, honestly flagged by the advisor and not adjudicated**:
the $\Pi$-formula's own Fourier/Laplacian normalization
($\nabla^2\to{-k^2}$ vs $-k^2/a^2$ inside the $8\pi\tilde Ga^2\bar\rho$
prefactor) is the one sub-term Stage 2's units contract never itemized,
and two hand-worked conventions disagreed with each other and neither
tamed the instability. **Checked the primary source directly on this
specific point before leaving it open**: `newRMONDLett.tex` line 456
defines $\Pi$ with the identical bracket
$\nabla^2[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ that
**also appears verbatim in the paper's own $\delta$ definition**, eq.
(`delta_field_relation`, line 437) — the same $1/(8\pi\tilde Ga^2
\bar\rho)\nabla^2[\ldots]$ term, not just a similar one. This means
whatever Fourier convention is eventually adopted for $\Pi$ **must be
identical to whatever convention $\delta$'s own definition uses** — a
second, independent constraint on the same unknown, not previously
noticed. Given the metric convention stated just above these equations
($g_{ij}=a^2(1-2\Phi)\gamma_{ij}$, i.e. $\nabla$ acts on *comoving*
coordinates), the natural reading is $\nabla^2\to-k^2$ with $k$ the bare
comoving wavenumber (no extra $a$), with the $a^2$-dependence entering
*only* through the already-explicit $a^2$ in the $8\pi\tilde Ga^2
\bar\rho$ prefactor — matching the advisor's own "comoving-Laplacian"
option, not the "physical-Laplacian" one. This is a plausibility
argument from the paper's stated gauge, not a full independent
derivation, and does not by itself explain why the code's current
coefficient and that reading reportedly differ by an $O(1)$ factor
($1/(3\Omega_s)$-shaped) — **left for Stage 3b**, not resolved here.

**Status**: the instability is real, precisely characterized, and not a
numerical artifact — confirmed independently. Whether it survives after
the $\Pi$-normalization is nailed down is still open. **Recommending
Stage 3b** (a dedicated, narrowly-scoped units-contract addendum for the
$\Pi$-formula's Laplacian convention, cross-checked against both the
$\delta$-definition constraint found here and, ideally, the advisor's
own independent route) as the next step, before any further
explicit-ODE attempt or a quasi-static/slaved-closure redesign. Gate
1(b)'s caveat, Q2/EFE sequencing (Gate 3), KATRIN watch all unchanged.
Nothing in `cdot-7/` was touched.

## 34. Stage 3b — the $\Pi$-formula's Laplacian convention worked out; the instability survives every reading tried, so it is very likely real physics, not a units artifact

**Script**: `wp7_stage3b_pi_normalization_check.py` (new, `cdot-8/WP7/`).

**Re-derived the convention directly from primary source**
(`newRMONDLett.tex` line 456), using the internal self-consistency of
the formula itself as the deciding argument: $\Pi$'s own prefactor
already carries an *explicit* $a^2$ multiplying $\bar\rho$
($8\pi\tilde Ga^2\bar\rho$). If $\nabla^2$ in this same formula already
meant the "physical" ($1/a^2$-including) Laplacian, that explicit $a^2$
would double-count the conversion — an unlikely authorial choice in a
compact PRL that writes no redundant factors elsewhere. The natural,
minimal reading is therefore $\nabla^2\to-k^2$ (bare comoving $k$), with
$8\pi\tilde G\bar\rho_s(a)=3H_0^2\Omega_s(a)$ (the plain density
definition, no extra $a^2$ folded in separately) — giving

$$\Pi = c_\text{ad}^2\delta_s + \frac{c_\text{ad}^2\kappa}{3\Omega_s(a)}\big[K_B\mathcal E_\alpha+(2-K_B)\chi\big]$$

This matches this program's own already-validated Poisson-equation
convention exactly (cross-checked: $\Phi=-1.5\,\Omega(a)\delta/\kappa$,
the same $8\pi G\bar\rho=3H_0^2\Omega(a)$ identification, no separate
$a^2$). **This also surfaces a genuine, separate bug**: the *coded*
$\Pi$ term in `wp7_stage3_field_variable.py` uses bare $\kappa$ with
**no $\Omega_s(a)$ division at all** — missing the $1/(3\Omega_s(a))$
normalization entirely, under either Laplacian convention.

**Tested numerically whether resolving this changes the verdict**: ran
all three readings (the code's current bare-$\kappa$, the derived
"comoving" $\kappa/(3\Omega_s)$, and the advisor's alternate "physical"
$\kappa/(3a^2\Omega_s)$) through the vector-sector Jacobian. **Result:
the growing real eigenvalue survives under all three** — the comoving
reading roughly *halves* the eigenvalue's magnitude at fixed $z$ (e.g.
$485\to221$ at $z=100$) but does not remove it; the physical reading
makes it dramatically worse. **The instability's existence is robust to
this normalization choice** — nailing down the exact convention shifts
the threshold's scale by an $O(1)$–$O(10)$ factor, not by the
$10^2$–$10^6$ needed to erase it.

**Conclusion**: this is evidence, not proof, that the instability is a
genuine physical feature of the theory — sourced by the same negative
$c_\text{ad}^2$ that already made the scalar sector tachyonic/clustering
(§23, §27, §28), now apparently destabilizing the vector sector's
explicit evolution too — rather than a units bug hiding the real
answer. Given how many times this exact class of normalization
derivation has produced subtle errors elsewhere in this program (the
$F_{QQ}(0)$ domain artifact, the bare-vs-$-\tfrac12$ $F_Q$ coefficient,
several WP3-era factor-of-few slips), **this conclusion is offered with
appropriate humility and flagged for advisor cross-check before
committing to a redesign**, rather than treated as fully settled on my
derivation alone.

**Recommendation**: (1) fix the coded $\Pi$ term to include the
$1/(3\Omega_s(a))$ factor regardless of the outcome below, since it is
wrong either way; (2) request advisor review of this specific
derivation (the "explicit-$a^2$-implies-comoving-Laplacian" argument) before
treating the instability as settled-real; (3) if confirmed, design a
quasi-static/slaved closure for $(\alpha,\mathcal E_\alpha)$ above
$\kappa_\text{crit}(z)$ (§33's own recommendation) as Stage 4's
prerequisite, rather than a fourth explicit-ODE attempt. Gate 1(b)'s
caveat, Q2/EFE sequencing, KATRIN watch all unchanged. Nothing in
`cdot-7/` was touched.

## 35. Advisory accepted — Stage 3b confirmed independently, on firmer ground than internal consistency alone

**Advisory**: `Advisory-WP7-Stage3bConfirmed-2026-07-20.md`. Reran
`wp7_stage3b_pi_normalization_check.py` directly and reproduced every
number exactly. Adds a second, independent argument for the
comoving-Laplacian reading beyond this program's own internal
no-double-counting logic: it is the **standard convention throughout
the cosmological-perturbation-theory literature** (e.g. Ma &
Bertschinger's own Poisson equation, $k^2\Phi=-4\pi Ga^2\sum\bar\rho_i
\delta_i$ — bare comoving $k^2$, all $a$-dependence carried explicitly
in the source term, precisely so $k$ stays an unambiguous
redshift-independent label) — retroactively explaining why this
program's own Poisson equation already worked without anyone having to
resolve this ambiguity explicitly. Confirms the missing
$1/(3\Omega_s(a))$ factor is a real, separate bug, right to fix
regardless. Confirms the instability survives under every reading
tried and reads the partial ($\sim2\times$), not total, shift under the
corrected normalization as exactly the expected signature of a genuine
physical effect being corrected by an O(1) unit fix, not erased by one.
**Accepted.** Optional (not blocking) suggestion: check whether AeST's
own native $K(Q)$ examples (Cosh/Exp/Higgs-like, whose $C_\ell^{TT}/P(k)$
match Planck per the founding paper) show the same instability — not
attempted here, flagged for later if useful. Recommends fixing the
$1/(3\Omega_s(a))$ bug and proceeding to design the quasi-static/slaved
closure.

## 36. Stage 3c attempted — quasi-static closure designed and coded; a genuine coordinate singularity found at the fast/slow transition, checkpointed rather than patched

**Script**: `wp7_stage3c_quasistatic_closure.py` (new, `cdot-8/WP7/`).
Implemented both recommended fixes: the corrected $\Pi$ normalization
($\text{Pi}=c_\text{ad}^2\delta_s+\frac{c_\text{ad}^2\kappa}{3\Omega_s(a)}
[K_B\mathcal E_\alpha+(2-K_B)\chi]$), and an algebraic elimination of
$\mathcal E_\alpha$ — solving $d\mathcal E_\alpha/dN=0$ for $\mathcal
E_\alpha(\alpha,\delta_s,\theta_s)$ in closed form (substituting the
corrected $\Pi$ formula and solving the resulting linear equation) —
leaving $\alpha$ as the only vector-sector ODE state (not itself
fast — its own equation carries no large coefficient).

**Regression (kappa$\to0$, vector term negligible)**: sensible, $\Phi$
decaying smoothly to $0.59\times$ by $z=0$ — same order and shape as
§32's own full-$\Pi$ regression ($0.50\times$), reassuring.

**Main test ($k=10^{-4}\,\text{Mpc}^{-1}$, the case that blew up in
§32) FAILED** — the ODE solver choked ("required step size less than
spacing between numbers"). **Diagnosed rather than brute-forced**:
traced the elimination's own denominator,
$\text{coef}_E=K_B H_c+(2-K_B)K_B\bar{\mathcal Q}/(1+w)\cdot
c_\text{ad}^2\kappa/(3\Omega_s)$, and found (algebraically, then
confirmed numerically) that $\text{coef}_E\equiv-K_BH_c\,\partial
\dot{\mathcal E}_\alpha/\partial\mathcal E_\alpha$ — **exactly the
$(2,2)$ Jacobian entry §33's stiffness audit already computed**. Along
this trajectory it crosses zero between $z=30$ ($-146.3$) and $z=10$
($+7.66$) — i.e. **exactly where $\kappa$ crosses $\kappa_\text{crit}(z)$
and the eigenvalue pair transitions from real (one large positive) to
complex (stable)**. The algebraic slaving relation has a genuine pole
right at this crossover — not a numerical artifact, a structural
feature of adiabatic elimination near a bifurcation, where the
fast/slow timescale separation the whole method relies on necessarily
breaks down.

**A second test (applying the same closure unconditionally at very
small comoving $k=10^{-6}\,\text{Mpc}^{-1}$, i.e. $\kappa$ safely
*below* threshold everywhere) also failed physically** — $\delta_s$
flips sign and $\alpha$ diverges to $-74$ by $z=0$. This is the
expected failure mode of applying an adiabatic-elimination formula
outside its regime of validity: below $\kappa_\text{crit}$ there is no
large/fast eigenvalue to eliminate, so forcing $\mathcal E_\alpha$ onto
the algebraic "fixed point" is simply the wrong physics there — the
true dynamics has $(\alpha,\mathcal E_\alpha)$ genuinely co-evolving on
the $H$-timescale, not slaved.

**Conclusion**: the quasi-static closure is right in spirit (confirmed
sound deep in the super-critical regime, and its failure modes are both
*understood*, not mysterious) but **cannot be applied as a single
global substitution** — it needs to be regime-gated (explicit
$(\alpha,\mathcal E_\alpha)$ ODE pair for $\kappa\lesssim
\kappa_\text{crit}(z)$, algebraic slaving only once safely above it),
with a deliberate treatment of the transition zone where the
elimination denominator itself vanishes — not yet designed. This is
structurally reminiscent of WP3's own homogeneous-mode/kernel-constant
difficulties (a bounded-solution selection principle that works cleanly
far from a marginal point, but needs explicit care exactly at one).
**Checkpointed rather than patched with an ad hoc regularization.**
Recommending advisor review of this specific transition-zone design
before implementing a hard or smoothed switch, given how often this
program's own normalization/matching derivations have needed a second
pair of eyes. Gate 1(b)'s caveat, Q2/EFE sequencing, KATRIN watch all
unchanged. Nothing in `cdot-7/` was touched.

## 37. Advisory accepted, correcting my own transition-zone diagnosis — the hybrid switch built to spec, but a deeper, WP3-shaped issue found: this is a boundary-condition selection, not a relaxation, and the naive initial condition breaks it

**Advisory**: `Advisory-WP7-Stage3cTransitionZoneReview-2026-07-20.md`.
**Correction accepted**: my own §36 misidentified the switch point as the
discriminant's zero ($z\approx29$–$30$, real$\to$complex). The advisor
built the full $\text{tr}(J)$/$\det(J)$/eigenvalue table and showed the
system is *still unstable* (a growing complex spiral, $\text{Re}(\lambda)
>0$) all the way down to $z\approx18$–$20$ — the true stability boundary
is $\text{Re}(\lambda_\text{max})=0$, i.e. $\text{tr}(J)=\text{coef}_E=0$,
a distinct and lower threshold. Since $J_{11}=0$ identically in this
system, $\text{tr}(J)=J_{22}=\text{coef}_E/(-K_BH_c)$ exactly, so this
isn't a numerical coincidence — the elimination's own pole is *exactly*
the point the fast/slow separation itself vanishes. **Independently
reconstructed the full table myself** (script inline, reusing the
Stage-3b-corrected Jacobian): confirmed the discriminant's zero at
$z\approx29$–$30$ and $\text{tr}(J)=0$ separately at $z\approx18.5$–$19$
— matching the advisor's bracketing exactly. Recommended design: a
**hard, criterion-based switch** at $\text{tr}(J)=0$ with a small safety
margin (not a smoothed blend, since the intervening region is
dynamically non-uniform), mirroring how Boltzmann codes switch tight
coupling rather than blend it.

**Built the hybrid closure exactly as specified**:
`wp7_stage3d_hybrid_closure.py` (new, `cdot-8/WP7/`) — quasi-static
slaving above $z_\text{switch}(k)+\text{margin}$, full explicit
$(\alpha,\mathcal E_\alpha)$ ODE below $z_\text{switch}(k)-\text{margin}$,
matched at the boundary. **The switch redshift reproduces the advisor's
bracket exactly**: $z_\text{switch}(10^{-4}\,\text{Mpc}^{-1})=18.54$.

**But the hybrid result itself is not stable, and fails the advisor's
own recommended robustness check dramatically**: $\delta_b(z=0)$ ranges
from $+0.14$ to $-1.8\times10^7$ across safety margins of $0.2$ to
$0.02$ e-folds — many orders of magnitude of sensitivity to an
arbitrary choice that should not matter if the design were sound.
**Diagnosed rather than reported as a bare failure**: traced it to the
very first evaluation point. At $z=100$ (the arbitrary starting
condition inherited from §32/§36, $\delta_b=\theta_b=\delta_s=\theta_s=
d_0$, $\alpha=0$), $\chi=\bar{\mathcal Q}(\theta_s+\alpha)\approx21.7$ —
**not small**, because $\bar{\mathcal Q}\approx2190$ is large at $z=100$
even though $\theta_s$ itself is small. The slaved algebraic $\mathcal
E_\alpha$ at this point is $\approx-76.4$ — wildly different from the
true system's own initial condition $\mathcal E_\alpha=0$. **This
mismatch does not decay: it is amplified**, because in the
$z>z_\text{switch}$ regime the mode being "eliminated" is the *growing*
one ($\text{Re}(\lambda)>0$), not a decaying one.

**This exposes something the closure's design, though correctly
motivated, had not accounted for**: standard quasi-static/tight-coupling
elimination works because the eliminated mode *decays*, so any initial
mismatch with the algebraic value is forgotten almost immediately,
making the choice of starting point safe. Here the eliminated mode
*grows*, so the algebraic relation is not a dynamical attractor but a
**boundary-condition selection** — structurally the *same* kind of
problem as WP3's own past-regularity/$C_1$-determination saga (select
the one solution that does not blow up, by imposing a condition, not by
waiting for relaxation). An arbitrary starting condition at $z=100$ is
not guaranteed to already sit on the selected (non-runaway) trajectory,
and forcing the algebraic relation there does not fix that — it just
relocates the mismatch, which then grows because we are, by
construction, in the unstable regime.

**Status: genuine progress on the switch criterion (confirmed, useful,
keeps), but the closure as built is not yet trustworthy** — the
remaining problem is not the switch location but the **initial/boundary
condition** for the quasi-static phase itself, which likely needs to be
determined by a consistency requirement (matching known deep-past
behavior, or a shooting method enforcing boundedness across the whole
$z>z_\text{switch}$ range) rather than inherited unmodified from the
earlier explicit-ODE convention. **Checkpointed, not forced.** Given how
closely this echoes WP3's own hardest historical difficulty, recommend
routing this specific point (how should the quasi-static phase's own
initial/boundary condition be chosen, given the eliminated mode is
growing, not decaying) to the advisor before attempting a fix. Gate
1(b)'s caveat, Q2/EFE sequencing, KATRIN watch all unchanged. Nothing in
`cdot-7/` was touched.

## 38. Advisor endorses the diagnosis and adds a compounding finding; independent check surfaces a further, un-flagged subtlety in the proposed fix itself

**Advisory**: `Advisory-WP7-Stage3dBoundaryConditionProblem-2026-07-20.md`.
**Endorses §37's diagnosis in full**: this is a boundary-condition/
stable-manifold selection problem (WP3's own past-regularity/$C_1$
shape), not a relaxation, precisely because the eliminated mode grows.
**Adds a genuine, independently-checked finding**: the quasi-static
approximation's own adiabaticity ($|\lambda_\text{max}|\gg1$ per
e-fold, the natural unit since $N$ is the ODE's own clock) is only good
for $z\gtrsim50$–$60$ and already marginal by $z\approx25$–$30$ — a
full ten-plus e-folds in redshift *above* the switch itself, meaning
"just fix the $z=100$ initial condition" cannot be the whole story even
once solved. Reproduced the advisor's table exactly (e.g. $z=100$:
$221.0$; $z=50$: $28.4$; $z=30$: $3.4$; $z=25$: $0.75$; $z=20$: $0.13$).
**Recommendation**: a Riccati/stable-subspace continuation — express
$\mathcal E_\alpha=\mu(N)\alpha+\nu(N)$ and evolve $\mu,\nu$ via their
own consistency equations (derived, not frozen-coefficient re-solves),
seeded deep in the well-separated regime ($z\gtrsim60$) — the standard
technique for tracking a stable branch through a marginal zone. Also
honestly flagged, not asserted: a rough finite-difference check hinted
at a possible *second* unstable direction in the full 6-variable system
(tentatively gravitational-Jeans-like, from the $(\delta_b,\theta_b)/
\Phi$ coupling), not confirmed, recommended for a careful follow-up
check.

**Derived the Riccati equations myself before treating the
recommendation as ready to implement**: writing $\mathcal E_\alpha=
\mu\alpha+\nu$ and requiring consistency with both the true $\mathcal
E_\alpha$-equation and $\alpha$'s own equation gives
$$\mu'=\frac{d\mathcal E_\alpha}{d\mathcal E_\alpha}\Big|_{\text{coef}}
\mu+\frac{d\mathcal E_\alpha}{d\alpha}\Big|_{\text{coef}}-\mu^2/H_c$$
— a genuine Riccati equation, with the naive frozen-coefficient slaving
recovered exactly as its fixed point ($\mu'=0$). **Checking where this
fixed-point quadratic itself has real roots surfaced a finding the
advisory did not flag**: its discriminant, $(H_c\,\partial\dot{\mathcal
E}_\alpha/\partial\mathcal E_\alpha)^2+4H_c\,\partial\dot{\mathcal
E}_\alpha/\partial\alpha$, is proportional to the *original* $2\times2$
Jacobian's own discriminant and **vanishes at the same $z\approx29$–$30$
point** (confirmed numerically: e.g. $+1.2\times10^4$ at $z=29.5$,
$-8.2\times10^4$ at $z=29$) — **not** at the switch ($z\approx18.5$).
**This means the real-valued slope $\mu$ itself stops existing as a
real number ten-plus e-folds before reaching $z_\text{switch}$** — once
the Jacobian's eigenvalues turn complex ($z\lesssim29$–$30$), there is
no longer a single real stable eigendirection to track by a real
Riccati slope at all; every real initial condition in that spiral zone
grows at the same rate $\text{Re}(\lambda)$ (a genuinely 2D unstable
regime, not a 1D-unstable-plus-1D-stable split). **The proposed method,
taken literally as a real-valued continuation, cannot be carried through
the $z\approx18.5$–$29.5$ spiral zone at all** — it needs a complex- or
matrix-valued (Riccati-matrix) generalization there, a further
derivation beyond what either the advisor or I have done.

**Status: advisory's core diagnosis and adiabaticity finding both
independently confirmed and accepted; the concrete method proposed
needs a real extension before it can be implemented, and this is a
genuinely new wrinkle, not previously surfaced by either party.**
Checkpointed rather than attempting a complex-Riccati derivation
un-reviewed. Recommending this specific point — how to generalize the
stable-subspace continuation through a genuinely complex-eigenvalue
(spiral) region — be put to the advisor next, alongside their own
still-open item (whether a second unstable direction exists in the full
system). Gate 1(b)'s caveat, Q2/EFE sequencing, KATRIN watch all
unchanged. Nothing in `cdot-7/` was touched.

## 39. Advisory accepted — no complex generalization needed, one handoff suffices; implementing it surfaces a further, well-diagnosed numerical obstruction: the stable branch's forward-$N$ Riccati flow is itself repelling

**Advisory**: `Advisory-WP7-Stage3eRiccatiSpiralResolution-2026-07-20.md`.
**Accepted, and re-derived independently before trusting**: in a
complex-eigenvalue (spiral) regime every real direction shares the same
growth envelope $\text{Re}(\lambda)$ — there is no preferred direction
to select, so the $z\approx18.5$–$29.5$ zone needs no elimination method
at all, real or complex. Verified the key algebraic claim myself,
$D_\mu=H_c^2D_J$ **exactly** (not approximately): with $\mu=H_c\lambda$
(the standard eigenvector-slope identity for this $2\times2$ form), the
Riccati fixed-point quadratic's discriminant is literally $H_c^2$ times
the original Jacobian's, confirmed symbolically and to 5 figures
numerically. **Design accepted**: real Riccati continuation seeded at
$z\gtrsim60$, propagated down to a *single* handoff at $z\approx29$–$30$
(comfortably inside the real-eigenvalue region, not at $z_\text{switch}=
18.5$), then one continuous explicit $(\alpha,\mathcal E_\alpha)$
integration for everything below — covering both the spiral zone and
the later stable zone without further special handling.

**Implemented exactly this**: `wp7_stage3e_riccati_handoff.py` (new,
`cdot-8/WP7/`). Caught and fixed my own sign error before trusting any
output — the fixed-point quadratic has two roots ($\mu=H_c\lambda_
\text{stable}$ and $\mu=H_c\lambda_\text{unstable}$); an initial
implementation used the wrong (unstable) branch as the seed, caught by
checking against the already-known eigenvalues at $z\approx100$/$60$
before running anything further.

**The corrected run still failed** — same solver error as §36
("required step size less than spacing between numbers"), now
localized to the Riccati phase itself, at every handoff redshift tried
($35$, $32$, $30.5$, $29.8$), including deep inside the supposedly-safe
real-eigenvalue region. **Diagnosed rather than reported as a bare
failure**: linearizing the $\mu$-Riccati equation around its own stable
fixed point gives $d(\delta\mu)/dN=(\lambda_\text{unstable}-\lambda_
\text{stable})\,\delta\mu$ — since $\lambda_\text{unstable}>\lambda_
\text{stable}$ always in this region, this coefficient is **always
positive**: forward-$N$ propagation of the physically-correct (stable)
root is itself a repelling flow, amplifying any mismatch, however
small. **Confirmed numerically, cleanly**: seeding at the *exact*
analytic stable-root value at $z=60$ and integrating forward just
$\Delta N=0.01$ already drifts from $-2479.3$ to $-2500.0$ purely from
truncation error; perturbing the seed by $10^{-6}$ or $10^{-9}$ causes
the solver to blow past the trajectory's own tabulated domain within a
handful of adaptive steps. **This is a known phenomenon in Riccati/
shooting-method numerics**: the stable-manifold branch of a Riccati
equation is generically a repeller under forward time integration
(exactly the reason real shooting/compound-matrix codes for stiff
two-point problems integrate such equations *backward*, from a
well-posed terminal condition, or track an unnormalized direction
vector instead of the scalar ratio $\mu$ directly, rather than
forward-integrating the ratio itself).

**Status: the advisory's conceptual resolution (one handoff, no
complex generalization) is accepted and stands; the concrete numerical
implementation needs a different integration strategy** — most likely
backward-$N$ propagation from a well-posed point near the handoff, or a
compound/unnormalized-vector formulation, neither yet attempted.
Checkpointed rather than forcing a fix without review, given this is
now the fifth consecutive round on this single sub-problem and each
round has surfaced a genuine, non-obvious mathematical subtlety the
previous one didn't anticipate. Recommending this specific numerical
question (correct integration direction/formulation for the Riccati
continuation) be put to the advisor next. Gate 1(b)'s caveat, Q2/EFE
sequencing, KATRIN watch all unchanged. Nothing in `cdot-7/` was
touched.

## 40. Stage 3f — resolved: the Riccati apparatus is unnecessary; Stage 3c's original pointwise slaving works perfectly once handed off comfortably above $z\approx30$, not at $z_\text{switch}=18.5$

**Advisory**: `Advisory-WP7-Stage3fPointwiseFixWorks-2026-07-21.md` +
`wp7_stage3f_pointwise_conservative_handoff.py`. **Confirms §39's
repelling-flow diagnosis precisely** (the linearized rate at $\mu_
\text{stable}$ is exactly $\lambda_\text{unstable}-\lambda_\text{stable}$,
unconditionally positive, verified both analytically and by finite
difference at seven redshifts) — then, rather than fixing the Riccati
machinery, **drops it entirely**. Stage 3c's original pointwise
algebraic slaving (re-solve the frozen-coefficient fixed point fresh at
every RHS call, propagating no $\mu(N)$ state at all) was never the
problem — there is nothing for a repelling flow to act on if nothing is
being propagated. **Stage 3d's catastrophic sensitivity came entirely
from choosing the wrong handoff redshift** ($z_\text{switch}=18.5$,
identified in §37 as deep inside the already-marginal/spiral zone) —
not from any flaw in pointwise slaving itself, which is an excellent
approximation throughout $z\gtrsim30$–$40$ (§38's own adiabaticity
table: $|\lambda|\sim3$–$220$ there).

**Ran the companion script myself and reproduced every number
exactly**: handoff redshifts from $45$ down to $30.2$ (right at the
edge of the real-eigenvalue region) give smooth, monotonically
convergent results — $\delta_b(z=0)$ from $0.436$ at $z_\text{handoff}=
45$ to $0.374$ at $z_\text{handoff}=30.2$, a $\lesssim15\%$ spread,
nothing like Stage 3d's eight-order-of-magnitude sensitivity. No
blow-up anywhere in the tested range.

**Adopted as the standard closure going forward**: Stage 3c's pointwise
slaving with a handoff at $z\approx35$ (comfortable margin, per the
advisor's own recommendation) to full explicit $(\alpha,\mathcal
E_\alpha)$ integration for the remainder of the run. The Riccati-ODE
approach (§38–§39) is retired as a working method, though its
discriminant identity ($D_\mu=H_c^2D_J$) and the repelling-flow finding
remain correct and worth keeping on record — they're what correctly
ruled out the wrong fix and pointed at the right one. **This closes the
long chain from §32's original blow-up through §33–§39**: the vector
sector's fast/unstable mode is real physics (§33–§34), its Π-term
normalization is now correct (§34/§35), and it can be safely and
robustly eliminated above $z\approx35$ with a simple, cheap, pointwise
algebraic substitution — no exotic machinery needed after all.

**Still open, not yet checked**: the possible second unstable direction
in the full 6-variable system (flagged in §38, not confirmed) — the
advisor recommends this be checked with a careful (symbolic or
carefully-scaled) Jacobian before treating this closure as fully
validated, since a second growing direction would need its own
selection condition alongside this one. Gate 1(b)'s caveat, Q2/EFE
sequencing, KATRIN watch all unchanged. Nothing in `cdot-7/` was
touched.

## 41. Stage 3g — the full 6-variable stability audit, done analytically: no second unstable direction; the low-$z$ growth is the already-known scalar tachyonic mechanism, not new physics

**Script**: `wp7_stage3g_full_system_stability_audit.py` (new,
`cdot-8/WP7/`). Addresses the item both the advisor and I have flagged
repeatedly but never confirmed: does the full 6-variable system have
any growing direction beyond the already-audited vector-sector one? The
advisor's own attempt used a rough finite difference and explicitly
flagged it as too imprecise to trust, given this system's huge
coefficient range ($\bar{\mathcal Q}\sim10^3$, $\kappa\sim10^0$–$10^5$).

**Built the $6\times6$ Jacobian analytically instead** (the system is
linear in the state at fixed $N$, so every entry can be written down
exactly — no finite-difference error possible) — caught and fixed one
transcription slip of my own first (a missing $1/H_c$ on the
$\Pi/(1+w)$ term in row 3, exactly matching the coded `rhs_full`'s own
parenthesization) by comparing against a real finite difference, then
**validated the corrected analytic Jacobian against complex-step
differentiation** (exact to machine precision, immune to the
cancellation error real finite differences suffer here) — residuals
$\sim10^{-16}$ at every redshift checked, from $z=100$ to $z=0$.

**Scanned the full spectrum from $z=100$ to $z=0$**: confirmed the
$(\alpha,\mathcal E_\alpha)$ sub-block of the full Jacobian exactly
reproduces the earlier reduced $2\times2$ analysis (a consistency
check, not a new result) — but the **full coupled system's actual
largest eigenvalue is smaller in magnitude than the isolated
$2\times2$'s** throughout the high-$z$ regime (e.g. $60.0$ vs $221.0$ at
$z=100$; $23.6$ vs $47.7$ at $z=60$) — the back-coupling to the slow
sector measurably damps the effective growth rate relative to the
frozen-slow-variable idealization, a real but non-alarming effect (if
anything, it means the earlier analysis was mildly conservative, not
mildly wrong-in-the-dangerous-direction). **No independent growing
direction was found in the high-$z$/vector-sector regime** — every
large eigenvalue there traces back to the same mode already identified
and worked through in §33–§40.

**A separate, small, persistent real eigenvalue does exist from
$z\approx10$ down to $z=0$** (e.g. $\text{Re}(\lambda)\approx0.05$ at
$z=10$, peaking $\approx0.38$ near $z=0.5$, settling to $\approx0.26$ at
$z=0$) — this is exactly the kind of thing the advisor's rough check
might have flagged. **Checked directly whether this is vector-sourced**:
reran the full spectrum with $\kappa\to0$ (vector coupling forced off)
and the low-$z$ eigenvalue is **essentially unchanged**
($0.0465\to0.048$ at $z=10$; $0.2571\to0.255$ at $z=0$) — this mode is
**not sourced by the vector sector at all**. It is the already-known,
already-accepted scalar tachyonic-clustering mechanism (§23/§27:
$c_\text{ad}^2<0$ driving $\Omega_s$ to cluster dust-like through the
matter era, flipping sign near $z\approx0.13$–$0.15$), showing up
exactly where expected in this linear analysis, not a new instability
and not of the "gravitational-Jeans" character the advisor's own rough
check tentatively suggested.

**Verdict: no second unstable direction requiring its own selection
condition.** The full system has exactly two distinct growing
mechanisms, both previously identified and understood: the vector
sector's fast mode (real for $z\gtrsim29$–$30$, handled by Stage 3f's
pointwise-slaving-plus-handoff closure) and the scalar tachyonic
clustering mode (small, low-$z$, already a load-bearing, accepted
feature of the theory since §27, entirely independent of the vector
sector and not something this closure needs to touch). **The last open
item from Stage 3f is closed.** The vector-sector closure (§40) can now
be treated as fully validated. Gate 1(b)'s caveat, Q2/EFE sequencing,
KATRIN watch all unchanged. Nothing in `cdot-7/` was touched.

## 42. Stage 4 attempted — assembly straightforward, but a serious, escalation-worthy finding: the vector-sector instability never resolves at the $k$ scales the ISW estimate actually needs

**Assembled the two validated pieces**: the growth closure
(§32–§41 — $\chi,\gamma,\alpha,\mathcal E_\alpha$ unmodified by M5 per
§7's exact cancellation, evolved via the Stage-3f/g-validated pointwise-
slaving-plus-handoff design) and the M5 Einstein-constraint term
(§4–§6's corrected coefficient $8\pi G[\tfrac{F_Q}6+\tfrac{QF_{QQ}}2]q'
\bar{\mathcal N}_\text{tot}W(kR_h)[\delta_\mathcal N-3\Phi]$, no
re-derivation) into `wp7_stage4_isw_estimate.py` (new, `cdot-8/WP7/`),
solving the now-M5-augmented Poisson equation for $\Phi$ algebraically
(implicit in $\Phi$ via $\delta_\mathcal N-3\Phi$, closed-form solved).
One flagged, explicit approximation: $\delta_\mathcal N$ (the M5 term's
own census-weighted contrast) taken as $\delta_b$, matching §18–21's own
normalization convention — a genuine refinement, not attempted here.

**Running it at the actual ISW-relevant $k$ (per the established
$k=\ell/D_p(z=0.5)$ convention, $\ell=2,5,10\to k\approx1.1$–$5.4
\times10^{-3}\,\text{Mpc}^{-1}$) blew up catastrophically** — not the
tidy, bounded behavior Stage 3f validated. **Diagnosed rather than
patched around**: Stage 3f/g's entire vector-sector closure (the
pointwise-slaving/handoff design, the "$z\approx35$ handoff is safe"
finding, the full-system stability audit) was validated at exactly
**one** wavenumber, $k=10^{-4}\,\text{Mpc}^{-1}$ — a scale roughly
$10$–$50\times$ larger (physically, more super-horizon) than what
$\ell=2$–$10$ actually require. **Checked $z_\text{switch}(k)$ directly
across this range**: it *decreases* with increasing $k$ ($18.5\to8.5$
from $k=10^{-4}$ to $3\times10^{-4}\,\text{Mpc}^{-1}$, consistent with
$\kappa\propto k^2$ dominating $\kappa_\text{crit}(z)$'s much weaker $z$
dependence) — and **for $k\gtrsim10^{-3}\,\text{Mpc}^{-1}$, no
$z_\text{switch}$ exists in $z\in[0,2000]$ at all**: the $(\alpha,
\mathcal E_\alpha)$ subsystem's fast eigenvalue **stays real and
positive from $z=100$ all the way to $z=0$**, for every one of
$\ell=2,5,10$'s wavenumbers.

**Confirmed this is not an artifact of the reduced $2\times2$ picture or
of pointwise slaving**: reran §41's exact, complex-step-validated
analytic $6\times6$ Jacobian at these same $k$ values. The large,
positive, real eigenvalue is present in the **full, machine-precision
Jacobian** at every redshift checked from $z=100$ to $z=0$ (e.g. at
$k=2.71\times10^{-3}\,\text{Mpc}^{-1}$: $\max\text{Re}(\lambda)=1655$ at
$z=100$, still $23.8$ at $z=0$ — never once crossing zero). Switching
to pure pointwise slaving throughout the entire run (no handoff at all,
since no stable regime exists to hand off into) avoids literal
numerical divergence, but $\Phi$ still grows by **5–8 orders of
magnitude** from $z=100$ to $z=0$ at all three $\ell$ values — utterly
unlike any physically sensible ISW source, and completely swamping any
$\sim O(0.1)$-scale M5 signature ($P_{M5}/P_\text{std}\approx0$ to the
precision reported, not because M5 is negligible but because the
non-M5 "baseline" itself is already dominated by this runaway).

**This is a different, more serious finding than anything in the
§32–§41 arc, which all concerned the single scale $k=10^{-4}\,
\text{Mpc}^{-1}$.** It appears the vector sector's instability, far
from being a high-$z$-only, resolves-by-$z\sim20$-$30$ phenomenon, gets
*worse* — not better — at smaller scales, and specifically afflicts the
exact wavenumber range the low-$\ell$ CMB/ISW observables actually
probe. Since §7 already established the field equations $(\chi,\gamma,
\alpha,\mathcal E_\alpha)$ are **unmodified by M5 at every $k$**, this
cannot be an artifact of the M5 assembly itself or fixed by adjusting
the M5 term — the instability is intrinsic to the imported AeST
field-perturbation system as applied to cdot-8's own (census-forced,
quadrature-determined) $F(Q)$ and its large, redshift-spanning
$\Omega_s$ weight.

**Not declaring a unilateral kill.** Two things are worth stating
plainly before any verdict: (1) this is the field-perturbation system's
behavior under cdot-8's *own* $F(Q)$ and background trajectory — it is
not a statement about AeST's native, CMB-fitting parameter choices,
which the founding paper's own text notes give $\Pi\to0$/dust-like
decoupling for "a wide range" of its native $K(Q)$ (§1; the still-open
optional cross-check flagged in Stage 3b's advisory — whether AeST's
own tuned examples share this instability — is now considerably more
urgent than "optional"); (2) nothing has been done yet to check whether
this reflects a genuine physical pathology of the theory at these
scales, or a still-undiagnosed error somewhere in this specific
assembly (the M5 term, the $\delta_\mathcal N\approx\delta_b$
approximation, or the field-equation import itself) — this program's
own track record (every WP3 finding, several WP7 ones) shows both are
live possibilities and neither should be assumed. **Recommending
advisor review of this finding specifically**, and the AeST-native
cross-check (does the founding paper's own tuned $K(Q)$ share this
instability at the same $k$ range?) as the most informative next
diagnostic, before any further ISW/power-spectrum numerics are
attempted. Gate 1(b)'s caveat carried, now joined by this new,
independently-serious concern. Nothing in `cdot-7/` was touched.

## 43. §42 confirmed and reframed by the advisor; a careful reassessment finds their core claim solid, plus one small, genuine correction to both our reported numbers

**Advisory**: `Advisory-WP7-Stage4ISWInstabilityAssessed-2026-07-21.md`.
Reran both §41 and §42's scripts directly, reproducing every reported
number to the stated precision (one environment-only `numpy.trapz`
workaround, not a code issue). **Reframes the finding, not its
severity**: rather than "a different, unrelated new pathology," this
reads as the *same*, already-accepted $c_\text{ad}^2<0$ mechanism
(§23/§27's tachyonic clustering sign) continuing to larger $k$ —
physically, a negative effective pressure is *destabilizing* rather
than restoring in the dispersion relation, so larger $k$ makes things
*worse*, the exact opposite of ordinary Jeans stabilization. This isn't
a new mechanism; it's the same sign the program already accepted,
finally pushed to a $k$ range large enough to matter. **The practical
severity is unchanged**: $\Phi$ growing $5$–$8$ orders of magnitude by
$z=0$ is nowhere near a physical ISW source regardless of how the
mechanism is framed. Recommends routing this to the author now,
alongside Gate 1(b), rather than the advisor and worker deciding
unilaterally to proceed to the AeST-native cross-check — this is a
"does WP7's central deliverable work as scoped" question, the same
class of call Foundation §6 already reserves for the author (cf.
WP4a's own three-way verdict fork).

**Asked to reassess carefully before drawing conclusions — did exactly
that, and found one genuine, worth-stating correction.** Independently
re-verified the advisor's "local minimum near $z\sim0.3$–$2$, then a
rise to $\sim24$ by $z=0$" claim with a finer scan, and it initially
reproduced ($9.0$ at $z=0.02\to23.7$ at $z=0$) — but tracing *why*
surfaced something neither of us had caught: **the sharp rise in the
last few grid points is a numerical artifact**, not physics. $c_\text{
ad}^2$'s trajectory is built via `np.gradient` (twice: once for $w$,
once more for $c_\text{ad}^2$ itself), and `np.gradient`'s default
one-sided boundary formula (`edge_order=1`) is measurably less accurate
right at an array's last few points — exactly where this scan was
looking. **Confirmed directly**: recomputing $w$ and $c_\text{ad}^2$
with `edge_order=2` (a more accurate boundary stencil) removes the jump
entirely — $c_\text{ad}^2$'s last six points go from $\{-0.0698,
-0.0699,-0.0698,-0.0699,-0.2215,-0.3734\}$ (the jump, `edge_order=1`)
to $\{-0.0698,-0.0698,-0.0699,-0.0699,-0.0698,-0.0696\}$ (smooth,
`edge_order=2`) — the underlying $\Omega_s(z)$ itself is perfectly
smooth there ($0.9305\to0.9260$, no feature), confirming the jump lived
entirely in the differentiation, not the trajectory.

**This does not change the substantive finding, and arguably
simplifies it**: with the artifact removed, $\max\text{Re}(\lambda)$
very likely continues its smooth decline toward $z=0$ rather than
diving down and spiking back up — settling near $8$–$9$ rather than
$\sim24$ at the literal endpoint. **Either way, it never approaches
zero anywhere from $z=100$ to $z=0$** at the ISW-relevant $k$'s — the
escalation-worthy conclusion is unaffected, and if anything more
straightforward than either of our first passes reported (no genuine
late-time upturn, just a monotonic floor). **Flagging this as a general
numerical-hygiene item** for any future use of this background
trajectory's derivative-built quantities ($w$, $c_\text{ad}^2$) very
close to $z=0$: use `edge_order=2` (or trim the last few points),
not a fresh derivation, needed to fix it.

**Status**: the advisor's reframing (same mechanism, larger reach) is
adopted — it's a better, more coherent account of *why* this happens,
without softening *how bad* it is. The z=0 endpoint correction is
real but minor and doesn't move the verdict. **Agreeing with the
advisor's recommendation: this goes to the author now**, alongside
Gate 1(b), as a second, independent open structural question, rather
than either of us picking the next diagnostic unilaterally. Nothing in
`cdot-7/` was touched.


---

**Continued in `Update-WP7-InstabilityRecourses-2026-07-21.md`** — this
document was split 2026-07-21 once it grew unwieldy. That companion
document covers the recourse-ladder diagnostic work (R0, R1, R2) done
after Gate 4 paused WP7's ISW/growth track here at §42–§43; nothing in
this document past this point is superseded, this is purely a file
split for length, not a content change.
