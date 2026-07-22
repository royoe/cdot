# Update — WP7: Recourse Investigation for the Paused ISW/Growth Track (R0, R1, R2)

*Companion: `SessionLog-2026-07-21.md` (entries 41–44) and
`Update-WP7-PerturbationStructure-2026-07-18.md` (§1–§43, the main WP7
arc this document continues from). Split into its own file 2026-07-21
once the main document grew unwieldy — this covers only the recourse-
ladder diagnostic work done **after** Gate 4 paused WP7's ISW/growth
track (`cdot-8/proposal/DecisionGates-2026-07-18.md`), triggered by the
main document's own §42–§43: the vector-sector instability that Stage
3f/g validated at $k=10^{-4}\,\text{Mpc}^{-1}$ turns out to never
resolve at the wavenumbers the ISW estimate actually needs
($\ell=2$–$10$). Proceeds under the same standing caveats as the main
document (Gate 1(b)'s provisional-failure ruling on WP4a's 27%
$\theta_*$ miss; Gate 4's own paused status, unchanged by anything
here — this is diagnostic work informing a possible future recourse,
not a resumption).*

---

## 1. R0 attempted — the main advisor's recourse ladder: both diagnostic questions answered

**Advisory**: `Advisory-WP7-InstabilityRecourses-2026-07-21.md` (main
advisor, woken specifically for this). Confirms the mechanism as the
anti-Jeans branch of the already-accepted $c_\text{ad}^2<0$ sign (rate
$\sim|c_\text{ad}|k/aH$, checked against the reported eigenvalues — same
order, right $k$-scaling, right $z$-trend). Flags one required
correction independent of any recourse (§42's assembly cited §7's
all-$k$ field-equation cancellation, which was later superseded at
finite $k$ by an unmodeled $-F_Q(1-W(kR_h))$ term that activates at
$z\lesssim1$–$3$ — squarely the ISW window — not the cause of the
instability but owed in any rebuild). Proposes a recourse ladder: **R0**
(an audit, cheap, mandatory first, two sub-questions) → **R1** (an
$\mathcal F(\mathcal Y,\mathcal Q)$ small-gradient completion,
$F_{\mathcal Y}(0,Q)$, the leading physical recourse, reachable only if
R0 says so) → R2 (AeST-native cross-check) → R3 (re-closure) → R4
(nonlinear saturation, a fallback interpretation, not a fix).

**Attempted R0, both parts, with direct evidence rather than argument
from analogy:**

**R0(a) — was AeST's own stability guarantee derived assuming
$F_\mathcal Q(\text{background})=0$?** Checked the primary source
directly (not from memory). The founding paper's own "Stability and
waves" section (Minkowski-background analysis, the basis for its claim
that the scalar/vector sector is healthy, $\omega^2=\frac{2-\mathcal
K_B}{\mathcal K_2\mathcal K_B}(1+\tfrac12\mathcal K_B\lambda_s)k^2+
\mathcal M^2$ with a manifestly positive $k^2$ coefficient) states
explicitly: *"where we have used the desired late Universe limit for
which $\partial^2\bar{\mathcal F}/\partial\mathcal Q^2\to-2d^2\mathcal
K/d\mathcal Q^2=-4\mathcal K_2$ and $\partial\mathcal F/\partial\mathcal
Q=\bar{\mathcal F}=0$."* **Confirmed: yes, exactly this assumption is
made, in so many words.** The first identity ($\partial^2\bar{\mathcal
F}/\partial\mathcal Q^2=-4\mathcal K_2$) is not an approximation — it's
the already-established $\mathcal K=-\tfrac12F(0,\mathcal Q)$ identity
(Stage 2, confirmed against this same source) — but $\partial\mathcal
F/\partial\mathcal Q=F_\mathcal Q(\text{background})=0$ **is** a genuine
simplification, valid at AeST's own intended operating point (near
$\mathcal K$'s minimum, its whole reason for choosing $\mathcal K(\bar
{\mathcal Q})$ to have a minimum at all, stated earlier in the same
paper) but **emphatically not cdot-8's**: $F_\mathcal Q$ on cdot-8's own
trajectory ranges from $\approx4473$ (recombination) down to
$\approx1.85$ (today) — never within orders of magnitude of zero.
**Important, precise qualifier**: this does *not* mean the imported
cosmological (FRW, Newtonian-gauge) equations of motion themselves are
wrong or incomplete — Stage 2 already independently confirmed the
$\mathcal E_\alpha$ equation's own $d\mathcal K/d\mathcal Q$ coefficient
is kept fully general in that system, not assumed zero. What this
finding establishes is narrower and just as important: **the founding
paper's own basis for asserting this sector is "healthy" was never
established away from $F_\mathcal Q=0$** — cdot-8 has moved into a part
of the theory's parameter space the paper's own stability argument
simply doesn't cover, which is exactly why an instability the founding
paper never flags shows up once $F_\mathcal Q$ is large.

**R0(b) — where does the negative effective pressure net from, given
the bare $(2-\mathcal K_B)\mathcal Y$ term is a positive-definite
floor?** Answered directly from the already machine-precision-validated
coefficients (`wp7_r0_instability_source_audit.py`, new, `cdot-8/WP7/`)
rather than a fresh re-derivation risking a new error: $\partial\dot{
\mathcal E}_\alpha/\partial\alpha$ decomposes into exactly four additive
pieces, and **only one** carries any $\kappa$-dependence at all (via
$\text{kap3}=c_\text{ad}^2\kappa/3\Omega_s$ — the $\Pi$-feedback term).
At every redshift checked ($z=100,10,1,0.5$, $k=2.71\times
10^{-3}\,\text{Mpc}^{-1}$), this single term dominates the total by
one to two orders of magnitude and is uniformly **positive**
(destabilizing); the three $\kappa$-independent pieces together are
modest and **negative**. **The negative effective pressure nets
entirely from $\Pi$'s own $\kappa$-linear piece, sourced by
$c_\text{ad}^2<0$** — confirmed by decomposition, not conjecture.

**What this means for R1's feasibility, per the advisory's own framing**:
since the unstable direction is carried by a term that is *linear in
$\kappa$* — structurally a gradient-squared ("sound-speed"-type) term —
and AeST's own $\mathcal Y$ ($=q^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi$,
quadratic in perturbation gradients, exactly zero on the FRW background)
is exactly the kind of object whose $F_\mathcal Y(0,\mathcal Q)$
completion enters the linearized equations as another $\kappa$-linear
term, **R0(b)'s answer is a positive result for R1**: the unstable
direction sits in precisely the functional slot a small-gradient
completion of $\mathcal F(\mathcal Y,\mathcal Q)$ would renormalize.
This does not yet demonstrate R1 *works* (that requires an admissible
$F_\mathcal Y(0,Q(z))$ actually supplying $c_\text{eff}^2\gtrsim0$ at
these gradients while respecting the deep-Newtonian/T22 and
transition/$Q_2$ constraints already on this same completion family —
not attempted here), only that it is not structurally blocked.

**Status: R0 complete, both questions answered, favorable to R1's
feasibility.** Per the advisory's own recommended sequencing (R0+R2 as
one short round before any recovery attempt), R2 (the AeST-native
cross-check) has not yet been run. Gate 1(b)'s caveat, Q2/EFE
sequencing, KATRIN watch, and Gate 4's paused status all unchanged —
this is diagnostic work informing a possible future recourse, not itself
a resumption of the ISW/growth track. Nothing in `cdot-7/` was touched.

## 2. R2 — the AeST-native cross-check: clean, opposite result, confirming the pathology is cdot-8-specific

**Method**: rather than argue by analogy, built the founding paper's own
tuned "Higgs-like" $\mathcal K(\mathcal Q)=\tfrac{\mathcal K_2}{4
\mathcal Q_0^2}(\bar{\mathcal Q}^2-\mathcal Q_0^2)^2$ background directly,
using its own quoted parameters — read numerically off the paper's own
figure (`Cl_TT_EE_with_residuals.pdf`, not available as text in the
`.tex` source): $\mathcal K_B=0.3$, $\mathcal Q_0=1\,\text{Mpc}^{-1}$,
$\mathcal K_2=8.5\times10^8$ (`wp7_r2_aest_native_crosscheck.py`, new,
`cdot-8/WP7/`).

**Solved $\bar{\mathcal Q}(a)$ exactly** from the shift-symmetric
scalar's own conserved charge, $a^3F_\mathcal Q(\bar{\mathcal Q})=
\text{const}$ — the *complete* equation of motion here, since vanilla
AeST carries no M5 back-reaction to complicate it. **Caught and fixed a
genuine numerical trap before trusting any output**: tracking $\bar{
\mathcal Q}/\mathcal Q_0$ directly and subtracting $1$ loses all
precision once the field settles within $\sim10^{-10}$ of the minimum
(exactly what happens here); reformulated in $\delta\equiv\bar{\mathcal
Q}/\mathcal Q_0-1$ directly (solving the equivalent depressed cubic
$\delta^3+3\delta^2+2\delta+\epsilon/a^3=0$), which stays numerically
clean throughout. Used the **native** (non-M5) $\rho_s=\tfrac13
(\mathcal QF_\mathcal Q-F)$ coefficient, not cdot-8's own M5-modified
$\tfrac12$ one. Background $H(a)$ and the scalar's own CDM-mimicking
fraction were approximated by a standard flat $\Lambda$CDM stand-in
(stated honestly as an approximation — $w,c_\text{ad}^2$ themselves are
shape-only quantities and don't depend on this choice; only the
$\Pi$-term's own $\Omega_s$ normalization does).

**Result**: $c_\text{ad}^2$ is indeed negative for this native tuning
too (same sign as cdot-8's, confirming the anti-Jeans mechanism is
structurally generic to the imported machinery) — but **enormously
smaller**: $\approx-6.5\times10^{-4}$ at recombination, collapsing to
$\sim-10^{-10}$ by $z=10$ and $\sim-10^{-12}$ by today, versus cdot-8's
own $\sim-0.01$ to $-0.07$ persisting at that same order throughout.
**Running the identical vector-sector Jacobian, at the identical three
ISW wavenumbers ($\ell=2,5,10$), gives the opposite qualitative
result**: the fast eigenvalue resolves to comfortably stable
($\text{Re}(\lambda)<0$) by $z\approx100$ at the latest — a brief,
small, positive transient right at $z=1090$ for the two larger $k$'s
($2.6$ and $13.3$, nowhere near cdot-8's own thousands-to-millions at
comparable $z,k$) that resolves quickly and **stays stable all the way
to $z=0$**, unlike cdot-8's never-restabilizing result at these same
$k$'s.

**Verdict: R2 confirms the pathology belongs to cdot-8's own
census-forced, non-minimum-tracking $F(\mathcal Q)$, not to the
imported AeST field-perturbation machinery.** AeST's own native
solution stays anchored asymptotically at $\mathcal K$'s minimum with a
controlled, shrinking deviation — structurally different from cdot-8's
own $\mathcal Q\propto(1+z)^{5/3}$, which never approaches any
stationary point of the quadrature-determined $F(\mathcal Q)$ at all.
This is not merely "AeST's own $c_\text{ad}^2$ happens to be smaller" —
it is a genuine structural distinction between an oscillator-relaxing-
to-its-minimum solution (AeST's own design) and a monotonically-forced
trajectory with no such anchor (cdot-8's census/M5 closure). Together
with R0's finding (the instability nets from a $\kappa$-linear term in
exactly the slot an $F_\mathcal Y(0,\mathcal Q)$ small-gradient
completion would renormalize), this closes the "undiagnosed assembly
error vs. genuine physical consequence" question from both sides: **it
is a genuine, load-bearing consequence of cdot-8's own zero-freedom
$F(\mathcal Q)$**, not an error, and not an unavoidable feature of the
AeST chassis generically. Recommending this result be reported back to
the author/advisor alongside R0's, as the two together (per the
advisory's own sequencing) determine whether R1 is worth attempting.
Gate 4's paused status is unchanged — this remains diagnostic work.
Nothing in `cdot-7/` was touched.

## 3. R1 attempted — a genuine feasibility signal, with a serious, explicitly-flagged gap: no action-level derivation exists yet, and the mechanism's own sweet spot sits close to the theory's own stated healthy-range boundary

**What is rigorous, checked directly against the primary source, before
anything else was attempted**: the founding paper's own name for this
free sector is $F_\mathcal Y\equiv\partial\mathcal F/\partial\mathcal
Y=(2-\mathcal K_B)\lambda_s$ — already introduced by the paper itself as
"the necessary additional free parameter[s] to $\Lambda$CDM," already
used in its own Minkowski-background stability analysis, where the
vector mode's mass is $M^2=\frac{(2-\mathcal K_B)(1+\lambda_s)\mathcal
Q_0^2}{\mathcal K_B}$ and the scalar mode's $k^2$ coefficient is
$\frac{2-\mathcal K_B}{\mathcal K_2\mathcal K_B}(1+\tfrac12\mathcal
K_B\lambda_s)$, both requiring $\lambda_s>-1$ (strictly) for health.

**What is genuinely not yet done, stated plainly**: the founding paper's
own *cosmological* (FRW, Newtonian-gauge) perturbation system —
$\chi,\gamma,\alpha,\mathcal E_\alpha,\delta,\theta,\Pi$, the entire
machinery this WP7 arc has used since §1 — was derived with
$\mathcal Y\equiv0$ built in from the start (exactly zero on the FRW
background, never carried as a free completion anywhere in the imported
equations). **There is no existing derivation, in the primary literature
or anywhere in this program, of how a nonzero $F_\mathcal Y$ modifies
this specific system.** Deriving it properly requires re-varying the
action with a general $\mathcal F(\mathcal Y,\mathcal Q)$ kept through
the FRW perturbation expansion — a substantial, original piece of
theoretical work, not attempted here given the risk of introducing an
unverified error into exactly the class of calculation (coefficient/
normalization derivations) that has needed independent cross-checking
every single time it has arisen in this program.

**What was attempted instead, honestly scoped as a feasibility test, not
a fix**: `wp7_r1_gradient_completion_feasibility.py` (new,
`cdot-8/WP7/`) tests a *structural hypothesis* — motivated by, but not
derived from, the Minkowski dispersion relation's own $\lambda_s$
dependence — that $(2-\mathcal K_B)\to(2-\mathcal K_B)(1+\lambda_s)$
uniformly wherever $(2-\mathcal K_B)$ appears inside the $\mathcal
E_\alpha$ equation's own bracket (exactly where R0(b) isolated the
destabilizing $\Pi$-feedback term).

**Result**: moving $\lambda_s$ from $0$ (bare AeST default — cdot-8's
current implicit assumption) toward $-1$, while staying strictly inside
the paper's own healthy range $\lambda_s>-1$, suppresses the
instability **continuously and by many orders of magnitude** —
$\lambda_s=-0.999$ already reduces $\max\text{Re}(\lambda)$ at
$z=1090$ from $3.4\times10^8$ to $3.4\times10^5$ (three orders of
magnitude) and fully stabilizes $z=10,1,0$ outright; $\lambda_s=-1$
**exactly** gives clean, $k$-independent stability
($\text{Re}(\lambda)=-0.5$) at every redshift and every ISW wavenumber
tested simultaneously — because at that point the entire hypothesized
renormalized coefficient vanishes identically, removing the
$\kappa$-dependence from the $(\alpha,\mathcal E_\alpha)$ Jacobian
altogether, leaving a fixed, manifestly stable system.

**The serious tension, flagged not resolved**: $\lambda_s=-1$ is
*exactly* the founding paper's own stated healthy-range **boundary** —
the vector's own mass term $M^2\propto(1+\lambda_s)$ vanishes there
too. The mechanism that stabilizes the $(\alpha,\mathcal E_\alpha)$
system, at least under this hypothesis, wants to sit right at the edge
of validity the theory's own separate (Minkowski) stability analysis
requires, not safely inside it — a real, specific concern, not a
generic "fine-tuning" hand-wave. **The more encouraging finding is that
exact coincidence with the boundary is not required**: $\lambda_s$
comfortably inside the healthy range (e.g. $-0.99$ to $-0.999$) already
achieves most of the benefit, suggesting there may be room to stabilize
the ISW-relevant range without operating exactly at the dangerous
corner — but this trade-off (how close to $-1$ is actually needed once
the *real* action-level derivation is done, and whether the resulting
near-zero vector mass is otherwise phenomenologically safe, e.g.
against WP6's own PPN/pulsar bounds) has not been examined.

**Status: a genuine, quantitatively well-defined feasibility signal —
not a validated recourse.** Recommending this be reported back
alongside R0 and R2's findings, with an explicit request for the
proper action-level derivation (does $(2-\mathcal K_B)\to(2-\mathcal
K_B)(1+\lambda_s)$ actually hold in the FRW system, or does the true
derivation put the dangerous corner somewhere else — nearer, farther,
or removed entirely) before treating $\lambda_s$ near $-1$ as anything
more than a promising direction. Gate 4's paused status is unchanged —
this remains diagnostic work. Nothing in `cdot-7/` was touched.

**Cross-checked by the secondary advisor
(`Advisory-WP7-R0R1R2CrossCheck-2026-07-21.md`): R0, R1, R2 all
reproduce exactly, plus two refinements, both verified directly against
the primary source before accepting.** (1) R0(b)'s dominance is
$z$-dependent, not a flat "1–2 orders of magnitude" as stated above: at
$z=100$, $B\approx1.2\times10^9$ against $A+C+D\approx-4.0\times10^4$
— **four-and-a-half orders of magnitude**, not one to two; the smaller
figure holds only near $z\approx0.5$–$1$. Strengthens R0(b)'s
conclusion, doesn't change it. (2) **A second, previously-unflagged
condition in the same primary-source stability section**: immediately
after the dispersion relations quoted above, the paper states the
residual, non-propagating ($\omega=0$) vector mode's Hamiltonian is
"positive for momenta larger than $\sim\mu$ and otherwise negative,
also requiring that $\lambda_s>0$" (verified verbatim against
`newRMONDLett.tex`, lines 570–571) — **directly contradicting R1's own
favored suppression range** ($\lambda_s\to-1^-$, i.e. $\lambda_s<0$).
The paper's very next sentence frames the low-momentum piece as
"likely akin to Jeans-type instabilities," not a vacuum-stability
problem — so this may be tolerable rather than fatal, and (per the
advisor's own honest assessment) the compact PRL text alone doesn't
settle how binding it is; the cited Hamiltonian analysis lives in two
in-preparation companion papers, not available here. **This adds a
second, independent open question to R1's gap list**, alongside the
missing action-level FRW derivation: whether $\lambda_s>0$ survives,
relaxes, or doesn't transfer at all once the actual FRW (not
Minkowski-background) derivation is done is unknown, and belongs in
the record before $\lambda_s$ near $-1$ is treated as more than a
plausibility signal. Nothing in `cdot-7/` was touched.

## 4. Main advisor assesses the full R0/R1/R2 round: three additions, recommendation to commission the action-level derivation

**Advisory**: `Advisory-WP7-RecourseRoundAssessed-2026-07-21.md`
(main advisor; written before the secondary advisor's own cross-check
in §3 above, but processed here in sequence). Accepts R0/R1/R2 in full,
including both of the secondary advisor's refinements, and adds three
substantive readings before recommending a next step.

**Verified independently before accepting**
(`r1_viability_additions.py`, companion script, run directly): (1) the
$\mu\approx10^{-4}\,\text{Mpc}^{-1}$ (today's condensate/Compton scale,
from WP5's own $\mu^{-1}\approx10$–$20\,\text{Gpc}$ band) sits
**11–56$\times$ below** the ISW instability band
($1.1$–$5.4\times10^{-3}\,\text{Mpc}^{-1}$) — reproduced exactly. (2)
the vector mass $M^2=(2-\mathcal K_B)(1+\lambda_s)\mathcal Q_0^2/
\mathcal K_B$, evaluated at WP6's own pulsar-squeezed envelope
($\mathcal K_B\lesssim2.5\times10^{-6}$), gives $M^2/\mathcal Q_0^2
\approx8$ even at $(1+\lambda_s)=10^{-5}$ — reproduced exactly.

**Three additions, each a genuine reframing, not just restatement**:

**(a) What $\lambda_s\to-1$ physically is.** At that endpoint the
hypothesized total small-gradient coefficient $(2-\mathcal K_B)(1+
\lambda_s)$ vanishes — the scalar sector's own cosmological sound speed
$c_s^2\to0$. A zero-sound-speed component is what "dust" *means*: R1's
mechanism isn't suppressing an inconvenient term, it's the completion
under which cdot-8's scalar becomes **honest dust at linear
cosmological order**, while the separate, $\lambda_s$-untouched,
census-fixed $\mu^2\approx-0.5H^2$ driver keeps supplying the
scale-free clustering. The pathology was $c_\text{eff}^2<0$; CDM has
$c_s^2=0$; the recourse approaches zero from the correct side. This
reframes "a parameter pushed to a boundary" as "the component being
asked to be what the census budget already requires it to be" —
worth carrying to any report to the author.

**(b) The $\lambda_s>0$ tension has a scale structure, not just an
unresolved status.** The flagged Hamiltonian condition concerns the
*residual* ($\omega=0$) mode specifically, with its own positivity
boundary at $k\sim\mu$ — **11–56$\times$ below** where stabilization is
actually needed. The paper's own reading of the low-$k$ zone ("likely
akin to Jeans-type instabilities") is arguably a *feature* in a
DM-mimicking theory (the clustering sector itself), not obviously the
same physics as the higher-$k$ band R1 needs to fix. **Not dissolved —
located**: whether $\lambda_s<0$ also threatens the higher-$k$ band
remains exactly what the FRW derivation must settle, but it now has a
concrete scale map to check against, not a blank ambiguity.

**(c) The "dangerous corner" is parametrically protected by WP6's own
$\mathcal K_B$ squeeze.** Since $M^2\propto(1+\lambda_s)/\mathcal K_B$,
the same pulsar-derived smallness of $\mathcal K_B$ that was previously
pure cost (WP6 sub-task 2) *rescues* the vector mass as $\lambda_s\to
-1$ — the corner is dangerous only at $O(1)\,\mathcal K_B$, a regime
cdot-8 was independently squeezed out of already. Two previously
unrelated results now support each other.

**Recommendation: commission the action-level FRW derivation** (general
$\mathcal F(\mathcal Y,\mathcal Q)$ kept throughout the perturbation
expansion — the single piece of missing theory everything else on this
track now waits on), with a five-item target list: (1) does $(2-
\mathcal K_B)\to(2-\mathcal K_B)(1+\lambda_s)$ actually hold in the FRW
system, and where is the true stability boundary; (2) the fate of the
$\lambda_s>0$ condition on FRW, derived rather than cited to the
unavailable companion papers; (3) the function-valued completion
$\lambda_s^\text{eff}(\mathcal Y,\mathcal Q)$ across its cosmological
and galaxy-gradient ends (the same family T22/$Q_2$ already constrain);
(4) the vector mass along the actual trajectory under the $\mathcal K_B$
squeeze, made quantitative; (5) only then, the ISW system rebuilt with
derived coefficients plus the still-owed $-F_\mathcal Q(1-\mathcal W)$
field-side correction (§2 of the main document) and both exact anchors.

**Status: assessment accepted, not yet acted on.** This is a
recommendation to the author to commission a substantial, well-scoped
piece of original theoretical work — not something to start
unilaterally. If the derivation confirms the feasibility signal, WP7's
central deliverable comes back into reach; if not, the honest options
narrow to R3/R4 with real information in hand either way. Gate 4
remains paused. Nothing in `cdot-7/` was touched.

## 5. The commissioned derivation begins — item 1's first piece: $\mathcal Y$'s exact quadratic-order form, rigorously established (a bug caught and fixed along the way)

**Author authorized proceeding with the action-level FRW derivation
(§4's recommendation).** Starting with target-list item 1: does
$(2-\mathcal K_B)\to(2-\mathcal K_B)(1+\lambda_s)$ actually hold in the
FRW system? The necessary first step is working out $\mathcal Y=q^{\mu
\nu}\nabla_\mu\phi\nabla_\nu\phi$ itself to quadratic order in
Newtonian-gauge perturbations — never previously derived anywhere in
this program (the imported $\chi,\gamma,\alpha,\mathcal E_\alpha,\delta,
\theta,\Pi$ system was built with $\mathcal Y\equiv0$ from the start).

**Result, symbolically verified** (`wp7_derivation_Y_identity.py`, new,
`cdot-8/WP7/`):
$$\mathcal Y = \frac1{a^2}(\nabla\chi)^2$$
to quadratic order — governed *entirely* by $\chi\equiv\varphi+\dot{
\bar\phi}\alpha$, exactly the combination already central to every
equation in this program's imported system, not some other mixture.
This isn't a coincidence: an exact algebraic identity ($D_\mu\phi\equiv
\nabla_\mu\phi+A_\mu\mathcal Q$ is the $A$-orthogonal projection of
$\nabla_\mu\phi$, and $\mathcal Y=g^{\mu\nu}D_\mu\phi D_\nu\phi$
identically, using only $A^\mu A_\mu=-1$) shows $\chi$ *is* the natural
object $\mathcal Y$ is built from — $D_i\phi=\partial_i\chi$ falls out
directly.

**Direct action-level consequence**: expanding $\mathcal F(\mathcal Y,
\mathcal Q)=F(0,\mathcal Q)+F_\mathcal Y(0,\mathcal Q)\mathcal Y+
O(\mathcal Y^2)$ around $\mathcal Y=0$ (exact on the background) and
using the result above, the quadratic-in-perturbations action picks up
$$S\supset-\int d^4x\,\frac a{16\pi\tilde G}\big[(2-\mathcal K_B)+
F_\mathcal Y(0,\bar{\mathcal Q})\big](\nabla\chi)^2$$
— confirming, **rigorously, for this isolated piece**, the R1
hypothesis' core claim: $(2-\mathcal K_B)\to(2-\mathcal K_B)+F_\mathcal
Y(0,\bar{\mathcal Q})$ is exactly the coefficient of $\chi$'s own
gradient-squared term.

**A genuine bug caught and fixed before trusting this**, recorded
honestly rather than smoothed over: the first attempt used the founding
paper's own *stated* (linear-order) ansatz $A_\mu=(-1-\Psi,\nabla_i
\alpha)$ literally, deriving $A^0$ (upper) from the unit constraint
while treating $A_0$ (lower) as exactly $-1-\Psi$ with no further term.
Computing $\mathcal Y$ two independent ways (a direct sum vs. the
$D_\mu\phi$-projection identity) gave **different** answers — not
resolved by picking whichever looked more plausible, but traced to its
root cause: the unit-timelike constraint, combined with metric-
consistent index raising, requires a genuine **second-order correction**
to $A_0$ itself ($\delta_2=\tfrac12\Psi^2-\tfrac1{2a^2}(\nabla\alpha)^2$,
matching the expected $A_0\to-\sqrt{-g_{00}}$ generalization) that the
paper's own linear-order-only ansatz never needed to state, since it
only works to linear order. Including it makes both methods of
computing $\mathcal Y$ agree exactly. **This is exactly the class of
subtlety this program has repeatedly warned about** (cf. R0(a)'s own
finding that the founding paper's stability section works in a
regime cdot-8 doesn't occupy) — caught here by cross-checking two
independent routes to the same quantity, not by trusting either one.

**What remains for item 1, stated plainly**: this establishes $\mathcal
Y$'s own form and its *isolated* contribution from the $\mathcal F(
\mathcal Y,\mathcal Q)$ term of the action alone. It does **not** yet
show how this propagates into $\Pi$'s already-established formula or
the $\mathcal E_\alpha$ equation specifically — those were derived from
the *full*, coupled Einstein+scalar+vector system, and the base action
also carries a **separate** term, $2(2-\mathcal K_B)\hat J^\mu\nabla_\mu
\phi$ (built from the aether's own covariant acceleration $\hat J_\mu
\equiv A^\alpha\nabla_\alpha A_\mu$, not from $\mathcal Y$), which
shares the *same* bare $(2-\mathcal K_B)$ coefficient but is **not**
modified by $F_\mathcal Y$ at all (it belongs to the base action, not
to $\mathcal F(\mathcal Y,\mathcal Q)$). Distinguishing which specific
occurrences of $(2-\mathcal K_B)$ in $\Pi$/$\mathcal E_\alpha$ trace to
$\mathcal Y$ (hence get corrected) versus $\hat J^\mu\nabla_\mu\phi$
(hence don't) is exactly the harder remaining piece of item 1 — this
means the "uniform substitution" used in R1's own feasibility scan was
a reasonable first hypothesis but is now known to be **too crude** to
be the final answer.

**Status: genuine, verified progress on item 1; not yet complete.**
Checkpointing here rather than pushing further without review, given
how many subtle, easy-to-miss corrections this exact class of
derivation has produced throughout this program (this round included).
Recommending this specific finding — $\mathcal Y=a^{-2}(\nabla\chi)^2$,
its direct action-level consequence, and the open $\hat J^\mu\nabla_\mu
\phi$-vs-$\mathcal Y$ attribution question — be cross-checked before
continuing to the harder remaining step (the full coupled variation).
Gate 4 remains paused. Nothing in `cdot-7/` was touched.

## 6. Secondary advisor confirms §5 and sharpens the attribution problem; applying the sharpening reveals a stark, must-report divergence

**Advisory**: `Advisory-WP7-YIdentityDerivationReviewed-2026-07-21.md`.
Confirms §5's symbolic result exactly (independent rerun) and the
bug-fix's diagnosis. **Independently confirms, directly from the
primary source** (`newRMONDLett.tex` lines 336–347, quoted verbatim),
that $(2-\mathcal K_B)$ appears in (at least) three structurally
distinct places in the bare action — the $-(2-\mathcal K_B)\mathcal Y$
term (gets the $F_\mathcal Y$ correction), the separate $2(2-\mathcal
K_B)\hat J^\mu\nabla_\mu\phi$ term (does not), and implicit background
pieces inside $F(0,\mathcal Q)$ (already correctly handled, not a new
concern) — confirming §5's caution is *structurally guaranteed*, not
merely plausible. **A useful negative result**: the paper's own linear-
perturbation section is built with $\mathcal Y\equiv0$ from its very
first line, so no shortcut exists by reading further in the primary
source — the attribution work is genuinely necessary. **A valid,
sharpened shortcut proposed**: since the new $F_\mathcal Y(0,\bar{
\mathcal Q})\mathcal Y$ term is *functionally identical* to the bare
$\mathcal Y$-term (same $\mathcal Y$, different coefficient — and no
higher-order Taylor correction enters, since $\mathcal Y$ itself starts
at quadratic order), its contribution to every field equation has
*exactly the same functional form* as the bare term's own contribution,
scaled by $\lambda_s$ alone. This narrows the task to: identify which
$(2-\mathcal K_B)$-proportional pieces in the *already-published*
$\chi,\Pi,\mathcal E_\alpha$ formulas trace to the bare $\mathcal Y$-term
specifically (get the $\lambda_s$ correction) versus $\hat J^\mu\nabla_\mu
\phi$ (don't) — bounded and checkable, not a full re-derivation.

**Applied this criterion**, using the physical character of each source
term: $\mathcal Y$ is a pure spatial-gradient-squared (Laplacian-type)
term, so its variation produces $\nabla^2$-type contributions —
matching exactly the $(2-\mathcal K_B)\chi$ piece *inside* $\Pi$'s own
$\nabla^2[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ bracket
(and $\delta$'s identical bracket). $\hat J^\mu\nabla_\mu\phi$ involves
the aether's own covariant *acceleration* — a Hubble-friction/mass-type
structure, no spatial Laplacian — matching the *outer* $(2-\mathcal
K_B)$ coefficient in the $\mathcal E_\alpha$ equation, which multiplies
a bracket built from $(H+\dot{\bar\phi})\chi$ and $3c_\text{ad}^2H\dot{
\bar\phi}\alpha$ (no $\nabla^2$ anywhere). Under this criterion: **only
the inner, $\Pi$-bracket occurrence of $(2-\mathcal K_B)$ gets $\to(2-
\mathcal K_B)(1+\lambda_s)$; the outer, $\mathcal E_\alpha$-equation
occurrence stays bare.**

**Result, and it is a stark reversal**: this makes the $\Pi$-feedback
term (R0(b)'s "$B$," previously found $\propto[(2-\mathcal K_B)+F_
\mathcal Y]^2$ under the cruder "uniform substitution" test) instead
$\propto(2-\mathcal K_B)^2(1+\lambda_s)$ — **linear**, not quadratic, in
$(1+\lambda_s)$. But re-running the full eigenvalue scan under this
refined attribution shows **the instability barely responds to
$\lambda_s$ at all** — at $z=1090$, $\max\text{Re}(\lambda)$ moves from
$3.3559\times10^8$ ($\lambda_s=0$) to $3.3559\times10^8$
($\lambda_s=-2$), unchanged to 4 significant figures. **Diagnosed, not
just observed**: the Jacobian's *trace* ($a_{EE}$, i.e. $\partial\dot{
\mathcal E}_\alpha/\partial\mathcal E_\alpha$) itself is enormous
($\approx3.36\times10^8$ at $z=1090$) and, under this refined
attribution, is driven entirely by the $\mathcal K_B\mathcal E_\alpha$
piece of $\Pi$ (which carries no $(2-\mathcal K_B)$ at all) multiplied
by the *outer*, uncorrected $(2-\mathcal K_B)$ — **untouched by
$\lambda_s$ under this hypothesis**. A large, fixed, positive trace
alone forces at least one large positive eigenvalue, regardless of what
$a_{\mathcal E_\alpha,\alpha}$ (which *does* respond strongly to
$\lambda_s$, confirmed: $1.39\times10^{14}\to-3.33\times10^6\to-1.39
\times10^{14}$ across $\lambda_s=0,-1,-2$) does on its own.

**This is a must-report divergence, not a resolved answer.** The
"uniform substitution" test (§46/R1's original scan) and this "refined
attribution" test are **both** structurally motivated, **neither**
rigorously derived from the action, and they give **opposite**
conclusions: the first says $\lambda_s\to-1$ stabilizes the ISW band
comfortably; the second says the dominant high-$z$ driver isn't even
touched by $\lambda_s$ at all. **This sharpens, rather than resolves,
why the actual coupled-variation derivation is essential** — the
attribution question isn't an academic nicety, it determines whether R1
has any chance of working, and guessing between two plausible-looking
hypotheses is exactly the kind of shortcut this program's own history
warns against. Not treating either result as final. Recommending this
specific divergence be the focus of the next review round, before any
further numerical exploration under either hypothesis. Gate 4 remains
paused. Nothing in `cdot-7/` was touched.

## 7. Advisory confirms §6's arithmetic and identifies a specific, checkable weak point in the attribution criterion — independently verified and sharpened into an exact identity

**Advisory**: `Advisory-WP7-RefinedAttributionAssessed-2026-07-21.md`.
Reran §6 directly, confirming both numbers exactly. **Independently
re-derives the "large fixed trace dominates" claim** (not just re-runs
it): for this system's $2\times2$ Jacobian, $\lambda_\pm=\tfrac12(a_{EE}
\pm\sqrt{a_{EE}^2+4a_{\mathcal E_\alpha,\alpha}/H})$, and at $z=1090$
the discriminant term is seven orders of magnitude smaller than
$a_{EE}^2$ — **verified independently, exactly**: $a_{EE}^2\approx
1.126\times10^{17}$ against $4a_{\mathcal E_\alpha,\alpha}/H$ ranging
$\pm3.0\times10^{10}$, ratio $\approx3.7\times10^6$.

**Identifies a specific, checkable weak point in the attribution
criterion itself**: the "friction/mass-type, no spatial Laplacian"
half of §6's dichotomy (used to argue the *outer* $(2-\mathcal K_B)$
traces to $\hat J^\mu\nabla_\mu\phi$, not $\mathcal Y$) assumes $\hat
J_\mu$'s spatial component carries no gradient structure. The advisor
argues this is not obviously true, since $\hat J_i$ is built from
time-derivatives of $\partial_i\alpha$ — itself already a spatial
gradient.

**Checked directly, not just accepted**: computed $\hat J_i\equiv\hat
A^\alpha\nabla_\alpha\hat A_i$ symbolically using the actual perturbed-
FRW Christoffel symbols (`wp7_derivation_Jhat_identity.py`, new,
`cdot-8/WP7/`), not asserted from general reasoning. **Result: $\hat
J_i=\partial_i(\Psi+\dot\alpha)=\partial_i\mathcal E_\alpha$ exactly**
— not merely "some gradient of $\alpha$" as the advisor's qualitative
argument suggested, but precisely the gradient of $\mathcal E_\alpha$,
the already-established variable. This confirms the weak point
rigorously and sharpens it into something usable: the spatial piece of
$2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi$ is
$$\propto\frac1{a^2}\partial_i\mathcal E_\alpha\,\partial_i\varphi$$
— a genuine gradient-*cross*-term between $\mathcal E_\alpha$ and
$\varphi$, structurally distinct from both $\mathcal Y=a^{-2}(\nabla
\chi)^2$ (a single field's gradient squared) and from a pure friction/
mass term (no gradient at all). **Neither of §6's two attribution
hypotheses captures this correctly** — it is not "purely $\mathcal Y$-
like" nor "purely friction-like," but a distinct cross-coupling that
would plausibly source *both* a $\nabla^2\mathcal E_\alpha$-type term in
$\varphi$'s equation and a $\nabla^2\varphi$-type term in $\mathcal
E_\alpha$'s own equation upon integration by parts — a structurally new
possibility neither prior test considered.

**Status: this precisely locates what the actual coupled-variation
derivation needs to account for; it does not yet complete it.** The
harder remaining step — properly varying $2(2-\mathcal K_B)\hat J^\mu
\nabla_\mu\phi$ (using this now-exact $\hat J_i=\partial_i\mathcal
E_\alpha$ identity) alongside $-F_\mathcal Y(0,\bar{\mathcal Q})
\mathcal Y$, and combining both into the actual modified $\Pi$/$\mathcal
E_\alpha$ equations — is substantial, original work, not yet attempted.
Checkpointing here, consistent with this program's standing discipline,
given how much genuine, easy-to-miss structure this single sub-problem
has surfaced across three consecutive rounds (§5, §6, this one).
Recommending this specific identity, and the concrete next derivation
step it enables, be reviewed before continuing. Gate 4 remains paused.
Nothing in `cdot-7/` was touched.

## 8. $\hat J_0=0$ exactly: the time component vanishes, so $\hat J^\mu\nabla_\mu\phi$ reduces entirely to its spatial piece

**Following the advisory's own recommended next step** (§7): before
attempting the full coupled variation of $2(2-\mathcal K_B)\hat J^\mu
\nabla_\mu\phi$ alongside $-F_\mathcal Y(0,\bar{\mathcal Q})\mathcal Y$,
characterized $\hat J_\mu$'s *remaining* component — $\hat J_0$ — using
the same machinery already validated for $\hat J_i$ in §7 (the actual
perturbed-FRW Christoffel symbols, not general reasoning).

**Result, symbolically verified**
(`wp7_derivation_Jhat_identity.py`, extended — same file as §7's
$\hat J_i$ derivation, `cdot-8/WP7/`): $\hat J_0=0$ exactly, to linear
order. **Independent consistency check, also confirmed exactly**: the
orthogonality identity $\hat A^\mu\hat J_\mu=0$ (expected on general
grounds — $\hat J_\mu$ is the covariant acceleration of a unit-norm
congruence, always orthogonal to the congruence itself) holds
identically once both $\hat J_0$ and $\hat J_i$ (§7) are combined with
$\hat A^\mu$ through the same self-consistent, second-order-corrected
$A_0$ ansatz §5 already established. This is not a new assumption
introduced to force the check to pass — it is the same machinery
already cross-validated twice (§5's two independent routes to
$\mathcal Y$, §7's $\hat J_i$ identity), now passing a third,
independent test.

**Direct consequence**: since $\hat J^0=g^{00}\hat J_0=0$ as well (no
$\hat J_0\to\hat J^0$ subtlety — $g^{00}$ is finite and nonzero), the
**entire** $\hat J^\mu\nabla_\mu\phi$ term reduces to just its spatial
piece — no separate time-component contribution to track through the
coupled variation at all:
$$\hat J^\mu\nabla_\mu\phi=\hat J^i\nabla_i\phi\approx\frac1{a^2}
\partial_i\mathcal E_\alpha\,\partial_i\varphi.$$
Combined with the advisory's own $\chi$-substitution ($\varphi=\chi-
\dot{\bar\phi}\alpha$, §7's advisory §3), this is
$$\hat J^i\nabla_i\phi\propto\frac1{a^2}\partial_i\mathcal E_\alpha
\Big(\partial_i\chi-\dot{\bar\phi}\,\partial_i\alpha\Big),$$
expressed entirely in the program's own three standing variables
($\chi,\alpha,\mathcal E_\alpha$), with no separate $\varphi$ or $\hat
J_0$ bookkeeping needed.

**Status: a genuine simplification, not a resolution of the attribution
question.** This does not by itself determine how $\hat J^\mu\nabla_\mu
\phi$'s cross-term structure propagates into the modified $\Pi$/$\mathcal
E_\alpha$ equations — that still requires the actual Euler-Lagrange
variation of the combined action (both this term and $-F_\mathcal Y(0,
\bar{\mathcal Q})\mathcal Y$ together), not yet attempted. What it does
establish: the variation only needs to be carried through in space, not
also in time for a separate $\hat J_0$ piece — one fewer moving part
in what is already a substantial derivation, and one more confirmation
that this class of check (compute the quantity exactly rather than
assume it) keeps surfacing real structure, this time in the reassuring
direction. Checkpointing here before attempting the full variation,
consistent with this program's standing discipline. Gate 4 remains
paused. Nothing in `cdot-7/` was touched.

## 9. First attempt at the actual coupled variation: a real methodological bug caught and fixed (validated), leading terms match, two residual mismatches honestly left open

**Attempted the harder remaining step directly**: assemble the full
$\alpha$-dependent quadratic-order Lagrangian (bare $\mathcal Y$ term,
the new $F_\mathcal Y(0,\bar{\mathcal Q})\mathcal Y$ completion, $2(2-
\mathcal K_B)\hat J^\mu\nabla_\mu\phi$, the Maxwell-like $\hat F^{\mu\nu}
\hat F_{\mu\nu}$ term, and $\mathcal F(\mathcal Y,\mathcal Q)$'s own
$\mathcal Q$-dependence), vary directly w.r.t. $\alpha$
(`wp7_derivation_coupled_variation_attempt.py`, new, `cdot-8/WP7/`),
sidestepping the attribution-guessing entirely as the advisories
recommended.

**A new building block computed along the way**: $\mathcal Q$'s own
second-order perturbation, extracted from `Qcal` in
`wp7_derivation_Y_identity.py` (already computed there but never
displayed): $\mathcal Q^{(1)}=\gamma$ exactly (no $\alpha$-dependence,
as expected), and $\mathcal Q^{(2)}=[(\partial\alpha)^2\dot{\bar\phi}+2
\partial\alpha\,\partial\varphi+\Psi\text{-only terms}]/(2a^2)$ — a
genuine $\alpha$-$\varphi$ **cross term inside $\mathcal Q$ itself**,
not previously computed anywhere in this program, entering the action
via $\mathcal F(\mathcal Y,\mathcal Q)$'s own $F_\mathcal Q\cdot\delta
\mathcal Q$ piece.

**A genuine methodological bug caught and fixed before trusting
anything**: the first attempt treated $\kappa=k^2/a^2$ as a *constant*
symbol when taking the Euler-Lagrange time derivative — wrong, since
$a(t)$ is manifestly time-dependent. This produced a spurious $3H$
friction coefficient for the Maxwell term *alone*, matching a canonical
**scalar** field's dilution rate, not a vector potential's. **Fixed by
keeping $\kappa=k^2/a(t)^2$ explicit; re-running the Maxwell term alone
then exactly reproduces $\mathcal K_B(\dot{\mathcal E}_\alpha+H\mathcal
E_\alpha)$** — a clean, validating cross-check, confirmed by direct
computation, not assumed.

**Result with the full Lagrangian**: the leading terms of the resulting
Euler-Lagrange equation match the published vector equation's structure
exactly — $\mathcal K_B(\dot{\mathcal E}_\alpha+H\mathcal E_\alpha)$
reproduced exactly; the $\chi$ coefficient's leading $(2-\mathcal K_B)H$
and $F_\mathcal Q$ ($\propto\!-2\,dK/d\mathcal Q$) pieces reproduced.
**Two residual mismatches remain, honestly left open, each precisely
located rather than vaguely flagged**:

1. The published $\chi$ coefficient carries an additional $(2-\mathcal
   K_B)\dot{\bar\phi}$ piece this derivation does not produce.
2. The derived $\alpha$-coefficient comes out proportional to
   $dK/d\mathcal Q\cdot\dot{\bar\phi}$ and $\ddot{\bar\phi}$ (the
   background scalar's own acceleration), not to $c_\text{ad}^2H\dot{
   \bar\phi}$ as in the published $-3(2-\mathcal K_B)c_\text{ad}^2H\dot{
   \bar\phi}\alpha$ term.

**Plausible, concrete (not yet verified) diagnosis for each**: (1) is
likely where $\Pi$/$\Psi$'s own separate origin re-enters — $\Pi$ is an
Einstein-momentum-constraint object (built from $\delta G^0_{\;i}$),
**not** a raw field-variation quantity, a structural distinction that
was already apparent going into this attempt — so a bare leftover
$\Psi$-dependent piece here is exactly what should show up where the
true equation instead carries $\Pi$, pending that separate constraint
derivation. (2) is likely resolved by substituting the background
scalar's own equation of motion ($\ddot{\bar\phi}$ in terms of
$F_\mathcal Q$, $F_{\mathcal Q\mathcal Q}$, $H$, via $a^3F_\mathcal Q=$
const) to convert this raw $F_\mathcal Q/F_{\mathcal Q\mathcal Q}$-
parametrized result into the paper's compact $c_\text{ad}^2$ notation —
not yet attempted.

**Status: genuine, partially-verified progress, not a completed
derivation.** The Maxwell-friction fix is a real, validated result on
its own (a clean, structural confirmation that this reduction method is
sound once the $\kappa(t)$ bug is fixed). The two residual mismatches
are reported honestly as open, each with a specific, checkable next
step — not resolved by guessing or forced through, consistent with this
program's standing discipline given how much this exact sub-problem
(the coupled $\mathcal Y$/$\hat J$ variation) has already surfaced
across five consecutive rounds (§5–§9). Recommending this be
cross-checked (the two proposed resolutions above, plus the separate
$\Pi$/momentum-constraint derivation this doesn't attempt) before
treating any coefficient conclusion as final. Gate 4 remains paused.
Nothing in `cdot-7/` was touched.

## 10. Advisor catches a real bug in §9's own convention ($\chi$ is not independent of $\alpha$); independently confirmed, extended, and residual mismatch (1) now traced exactly to $\Pi$'s own gamma-term

**Advisory**: `Advisory-WP7-CoupledVariationChiIndependenceCaught-2026-
07-21.md`. §8 reproduces exactly, no notes. §9's own numbers reproduce
exactly too. **But a check of §9's own stated convention — treating
$\chi$ as independent of $\alpha$ during the $\alpha$-variation — finds
a real bug**: $\chi\equiv\varphi+\dot{\bar\phi}\alpha$ is **not**
actually independent of $\alpha$; the genuinely independent fields are
$(\varphi,\alpha)$. Varying at fixed $\chi$ silently forces $\varphi$ to
co-vary to compensate — a different, incorrect variation. Redoing it at
fixed $\varphi$ (`wp7_chi_dependence_check.py`,
`cdot-8/WP7/advisory/`) and rewriting the result via $\chi$'s own
definition afterward (a pure relabeling, not a re-variation) gives a
corrected $\chi$-coefficient
$$(2-\mathcal K_B)H+(2-\mathcal K_B)\dot{\bar\phi}+\frac{F_\mathcal Q}2
+F_\mathcal Y\dot{\bar\phi}$$
— matching the published total *exactly*, plus one extra $F_\mathcal Y
\dot{\bar\phi}\chi$ term that is plausibly genuine new physics from the
completion itself (absent at $F_\mathcal Y=0$, as expected). **This
resolves §9's own reported mismatch (1) exactly, mechanically — not via
the not-yet-derived $\Pi$ contribution §9's own docstring
speculated.** A new, third open item surfaces in its place: a $(2-
\mathcal K_B)\dot\chi$-type term persists with no counterpart in the
published equation; mismatch (2) shifts rather than resolves.

**Independently re-ran `wp7_chi_dependence_check.py` before accepting
this**: reproduces the advisory's quoted coefficients exactly.

**Extended this further** (`wp7_derivation_coupled_variation_varphi_
fixed.py`, new, `cdot-8/WP7/`): redid the derivation directly in
$(\varphi,\alpha)$ — never introducing $\chi$ as a bookkeeping symbol,
to avoid the presentation ambiguity that made the "$\dot\chi$ term"
look like a mysterious new structure — and substituted the background
scalar's own equation of motion, derived cleanly from $a^3F_\mathcal
Q=$const: differentiating gives $3HF_\mathcal Q+F_{\mathcal Q\mathcal
Q}\ddot{\bar\phi}=0$, and using $c_\text{ad}^2=F_\mathcal Q/(\bar{
\mathcal Q}F_{\mathcal Q\mathcal Q})$ (the primary source's own
definition, line 405), this simplifies **exactly** to
$$\ddot{\bar\phi}=-3Hc_\text{ad}^2\dot{\bar\phi}$$
— an exact identity, not an approximation. With this substituted, the
residual (derived vector-EOM minus the published $\chi,\alpha,\mathcal
E_\alpha$-explicit terms, deliberately excluding $\Pi$ since it is a
separate momentum-constraint object) comes out to **exactly**
$$(2-\mathcal K_B)\dot\varphi + F_\mathcal Y\dot{\bar\phi}\chi -
(2-\mathcal K_B)(1-3c_\text{ad}^2)H\dot{\bar\phi}\alpha.$$
The middle term is the same expected new-physics piece as above. **The
first term was then checked directly against $\Pi$'s own definition**
(`Pi_delta_E_alpha`, using $\delta$'s leading $\gamma$-dependence,
$\gamma\equiv\dot\varphi-\dot{\bar\phi}\Psi$):
$$(2-\mathcal K_B)\frac{\dot{\bar\phi}}{1+w}\Big[\Pi\text{'s leading
$\gamma$-term}\Big]=(2-\mathcal K_B)\gamma=(2-\mathcal K_B)\dot\varphi-
(2-\mathcal K_B)\dot{\bar\phi}\Psi.$$
**The $(2-\mathcal K_B)\dot\varphi$ piece matches exactly** — confirmed
algebraically, not merely speculated as plausible (sharper than the
advisory's own framing, which left this as a plausible guess). **This
is a genuine, positive confirmation that $\Pi$'s momentum-constraint
origin is precisely what completes the vector equation's $\dot\varphi$-
dependence.**

**Still open, honestly reported**: $\Pi$'s own $\gamma$-term also
carries a $-(2-\mathcal K_B)\dot{\bar\phi}\Psi$ piece not present on
either side yet, and $\Pi$'s own $\kappa_3\cdot$bracket piece has not
been checked against the remaining $-(2-\mathcal K_B)(1-3c_\text{ad}^2)
H\dot{\bar\phi}\alpha$ residual — both require actually deriving $\Pi$
from the $0i$ Einstein/momentum constraint, the single missing piece
flagged since §8, still not attempted.

**Status: genuine forward progress on two fronts** — mismatch (1) is
now mechanically resolved (advisor's fix, independently confirmed), and
its remainder is now shown, not just guessed, to trace exactly to
$\Pi$'s own leading term. The path to closing the derivation is now
concrete: derive $\Pi$ from the actual momentum constraint next, with
strong reason (this section's own check) to expect it will close at
least the $\dot\varphi$-sourced piece of what remains. Recommending
this be reviewed before attempting that derivation. Gate 4 remains
paused. Nothing in `cdot-7/` was touched.

## 11. Advisory confirms §10 exactly and sharpens the open item into a precise prediction; first attempt at $\Pi$'s own momentum-constraint derivation — genuine partial progress, one real gap honestly left open

**Advisory**: `Advisory-WP7-PiGammaTermMatchConfirmed-2026-07-21.md`.
Every claimed result in §10 reproduces exactly, including the algebra
connecting them (checked by hand). **One precise, sharpened target
identified**: the residual currently carries *zero* net $\Psi$-
dependence, which requires $\Pi$'s own gradient ($\kappa_3$-bracket)
piece to supply a specific, calculable $\Psi$-term that exactly cancels
the leading $\gamma$-term's own $-(2-\mathcal K_B)\dot{\bar\phi}\Psi$
piece — a sharp, falsifiable check for once $\Pi$ is derived, not an
open-ended one. **Independently reran `wp7_derivation_coupled_
variation_varphi_fixed.py` before accepting** — reproduces exactly.

**Attempted $\Pi$'s own derivation directly**
(`wp7_derivation_momentum_constraint_attempt.py`, new, `cdot-8/WP7/`):
extended the perturbed-FRW metric with a genuine shift perturbation
$g_{01}=\epsilon B(t,x^1)$, extending the same Christoffel-symbol
machinery validated in §7/§8. $T^0_{\ i}$ (the momentum-density source
of the $0i$ Einstein constraint) is obtained, in the standard GR sense,
from $d(\text{quadratic action})/dB$ at $B=0$.

**Clean sub-results, each independently checked**: $\hat J_\mu$ (lower
index) has **no** $B$-dependence at linear order — verified directly.
$\hat J^0$ (upper index, via $g^{01}$ raising) **does** pick up a
genuine new $B$-linear term once contracted into $\hat J^\mu\nabla_\mu
\phi$: $B\dot{\bar\phi}\partial_1\mathcal E_\alpha/a^2$ — not present in
any prior round (which always had $B=0$). $\mathcal Q$'s own $B$-linear
piece: $B[\partial_1\alpha\,\dot{\bar\phi}-\partial_1\varphi]/a^2$.
$\mathcal Y$'s own $B$-linear piece: $2B\partial_1\alpha\,\dot{\bar
\phi}^2/a^2$. **The Maxwell term has exactly zero $B$-dependence at
this order** — checked directly, not assumed.

**Assembling these** gives a candidate $T^0_{\ 1}$-type quantity
containing the expected $\dot{\bar\phi}\partial_1\Psi$ piece (inside
$\mathcal E_\alpha$) that the advisory's own §4 prediction needs —
encouraging, not yet a full confirmation. **But it also contains a bare
$F_\mathcal Q\partial_1\chi$ piece with no direct counterpart in the
published $\delta$/$\Pi$ bracket** $[\mathcal K_B\mathcal E_\alpha+(2-
\mathcal K_B)\chi]$, which carries no separate $F_\mathcal Q$ (i.e.
$dK/d\mathcal Q$) term at all — a genuine, unresolved discrepancy.

**Status: genuine, partial progress, not a completed or fully verified
derivation of $\Pi$.** The clean sub-results (each independently
checkable) are reported with confidence; the assembled candidate does
not yet cleanly reproduce the published bracket. Plausible, not-yet-
checked candidates for the gap: an overall normalization/sign
convention not yet matched to eq. `Pi_delta_E_alpha`'s own $8\pi\tilde
G a^2\bar\rho$ factor; a missing cross-term from the Einstein-Hilbert
sector's own $B$-dependence (assumed, per the primary source, to reduce
to standard GR $G^0_{\ i}$, but not independently verified in this
extended setting); the $F(\mathcal Y,\mathcal Q)$ expansion's own
$\gamma^2$ term's $B$-cross-contribution, not included here.
Checkpointing here rather than pushing to an unverified conclusion,
consistent with this program's standing discipline, given this is now
the sixth consecutive round (§5–§11) surfacing genuine structure in
this one sub-derivation. Recommending review before attempting to close
the remaining gap. Gate 4 remains paused. Nothing in `cdot-7/` was
touched.

## 12. Advisor confirms §11's assembly independently and identifies a concrete, testable hypothesis for the "bare $F_\mathcal Q$" gap — confirmed exactly via an exact background identity

**Advisory**: `Advisory-WP7-MomentumConstraintAttemptAssessed-2026-07-
21.md`. Every sub-result reproduces exactly; going further, the
assembled candidate $T^0_{\ 1}$ was independently re-derived from the
five raw sub-results and matches the write-up's expression exactly,
confirming the assembly step itself, not just its inputs. **A
presentation correction, no computational error**: the isolated
"$F_\mathcal Q$" piece is actually $F_\mathcal Q(\partial_1\varphi-\dot{
\bar\phi}\partial_1\alpha)$, not $F_\mathcal Q\partial_1\chi$ as loosely
described — the underlying numbers were unaffected. **A concrete,
testable hypothesis offered**: this piece, built purely from $\varphi$
and $\alpha$ (not $\mathcal E_\alpha$ or $\chi$), may belong to the
**scalar** sector's own $\theta$-equation ($\theta\equiv\varphi/\dot{
\bar\phi}$, line 440) rather than to $\Pi$'s bracket at all — offered as
a cheap, checkable hypothesis, not a claimed resolution.

**Checked this directly**
(`wp7_derivation_theta_attribution_check.py`, new, `cdot-8/WP7/`): using
the already-established background identities ($8\pi\tilde G\bar\rho=
\bar{\mathcal Q}dK/d\mathcal Q-K$, $8\pi\tilde G\bar P=K$, $dK/d\mathcal
Q=-F_\mathcal Q/2$), verified
$$(1+w)\bar\rho\cdot16\pi\tilde G=-\dot{\bar\phi}F_\mathcal Q$$
**exactly** (zero symbolic difference) — not an approximation, a genuine
background identity. Since $\theta=\varphi/\dot{\bar\phi}$ so $\partial_1
\theta=\partial_1\varphi/\dot{\bar\phi}$, this means $-(1+w)\bar\rho\,
\partial_1\theta\cdot16\pi\tilde G=F_\mathcal Q\partial_1\varphi$ —
**matching the $\varphi$-part of the isolated piece exactly**. **The
advisor's hypothesis is confirmed, not merely plausible, for this
part.**

**Isolating the theta-matched piece and subtracting it from the full
§11 candidate** leaves a clean remainder, purely in $\alpha,\mathcal
E_\alpha$ (no $\varphi$ at all):
$$2(2-\mathcal K_B)\dot{\bar\phi}\partial_1\mathcal E_\alpha-2(2-\mathcal
K_B+F_\mathcal Y)\dot{\bar\phi}^2\partial_1\alpha.$$
This remainder — which must be what maps onto $\Pi$'s own $\kappa_3$-
bracket contribution — notably contains a genuine $F_\mathcal Y$-
proportional piece, $-2F_\mathcal Y\dot{\bar\phi}^2\partial_1\alpha$, an
expected new-physics contribution from the completion itself, the same
character as §10's own $F_\mathcal Y\dot{\bar\phi}\chi$ term.

**Status: genuine, confirmed partial resolution.** The "bare $F_\mathcal
Q$" gap is no longer an open mismatch — its $\varphi$-part is now
exactly identified as the standard fluid momentum source, verified via
an exact background identity, not assumed. The remaining $\alpha/
\mathcal E_\alpha$-only piece still needs to be checked against $\Pi$'s
own bracket structure (does a further spatial derivative of this
remainder reproduce $k^2[\mathcal K_B\mathcal E_\alpha+(2-\mathcal
K_B)\chi]$ up to normalization?) — not attempted here, the next
concrete, bounded step. Recommending review before attempting it. Gate
4 remains paused. Nothing in `cdot-7/` was touched.

## 13. The energy constraint, derived directly: an exact match to $\Pi$'s own bracket

**The natural parallel step**: rather than pursue the momentum-
constraint remainder further, derive the **energy** constraint (the
$00$ Einstein equation) directly by varying the already-assembled
action w.r.t. $\Psi$ — the lapse perturbation already present
throughout this program's machinery, no new field needed.
$\Psi$ is genuinely non-dynamical here (no $\dot\Psi$ appears anywhere
in the relevant terms — checked explicitly), so $d(\text{action})/d
\Psi=0$ **is** the energy constraint directly, exactly analogous to how
$d(\text{action})/dB$ gave the momentum constraint (§11) and $d(\text
{action})/d\alpha$ gave the vector equation (§9–§10).

**Method** (`wp7_derivation_energy_constraint_attempt.py`, new,
`cdot-8/WP7/`): $\mathcal Y$ has **no** $\Psi$-dependence at all (an
already-verified fact from §5, since the self-consistent $A_0$ ansatz
was built precisely to make this true) — so only $\mathcal F(\mathcal
Y,\mathcal Q)$'s own $\mathcal Q$-dependence (via $\gamma=\dot\varphi-
\dot{\bar\phi}\Psi$ and $\mathcal Q^{(2)}$'s own $\Psi$-terms,
re-derived here from `Qcal`) and the Maxwell/J terms (via $\mathcal
E_\alpha=\dot\alpha+\Psi$) carry $\Psi$-dependence. Assembled and
differentiated w.r.t. $\Psi$.

**Result: an exact match.** $d(\text{action})/d\Psi$ splits cleanly
into two pieces. The first,
$$2\kappa\big[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi\big],$$
is confirmed (zero symbolic difference after collecting) to be **exactly**
the published $\delta$/$\Pi$ bracket, appearing correctly multiplied by
$\kappa=k^2/a^2$ — matching the $\nabla^2[\ldots]$ structure exactly.
**This is the concrete confirmation the entire six-round derivation
(§5–§12) has been building toward.**

The second piece, $-(F_\mathcal Q+F_{\mathcal Q\mathcal Q}\dot{\bar
\phi})\dot\varphi+\Psi\dot{\bar\phi}(3F_\mathcal Q+F_{\mathcal Q
\mathcal Q}\dot{\bar\phi})$, is **not** yet matched to the standard
$\gamma$-proportional term in $\delta$'s own definition ($(1+w)/(\dot{
\bar\phi}c_\text{ad}^2)\gamma$) — substituting $c_\text{ad}^2=F_\mathcal
Q/(\dot{\bar\phi}F_{\mathcal Q\mathcal Q})$ does not obviously reduce it
to a bare multiple of $\gamma=\dot\varphi-\dot{\bar\phi}\Psi$; reported
honestly as unresolved, not forced to match.

**Status: a major, positive, verified result.** The bracket $[\mathcal
K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ — the single structure this
whole sub-derivation has circled since §7 — now falls directly out of
an independent action-level variation (w.r.t. $\Psi$, not guessed or
reverse-engineered from the published formula), with the exact
published coefficients and no adjustable normalization needed for the
*structure* to match. This confirms, at the level of the actual $0i$-
and $00$-constraint derivations now both attempted, that the program's
own established $(\chi,\alpha,\mathcal E_\alpha)$ variable set is
exactly what the base action naturally produces — a strong, independent
validation of the entire perturbation-variable framework this program
has used since §1, not just of the new $F_\mathcal Y$ completion. The
remaining unmatched $\gamma$-sector piece, and the momentum-constraint
remainder from §12, are not yet fully reconciled with the published
formulas' precise normalization — left open, honestly, for the next
round. Gate 4 remains paused; this is still diagnostic/derivation work.
Nothing in `cdot-7/` was touched.

## 14. Advisor confirms §12 exactly and §13's headline bracket-match result independently; finds a real sign inconsistency in §13's "second piece" (fixed, doesn't resolve the gap); a more careful hypothesis tried, also doesn't resolve it

**Advisory**: `Advisory-WP7-EnergyConstraintBracketConfirmed-2026-07-
21.md`. §12's $\theta$-attribution reproduces exactly — "the advisor's
own hypothesis from last round is now a checked fact, not a
plausibility claim." **§13's headline bracket-match result
independently reproduced and confirmed unaffected by anything below**:
differentiating just the Maxwell and $\hat J$-term pieces gives $2
\kappa[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ exactly,
with **zero dependence on $F_\mathcal Q$/$F_{\mathcal Q\mathcal Q}$ at
all** — so whatever happens with those terms, the headline result
stands on its own.

**A real sign inconsistency found**: §13's script assembled $L\supset+
F_\mathcal Q\mathcal Q^{(2)}+\tfrac12F_{\mathcal Q\mathcal Q}\gamma^2$
(a plus sign), inconsistent with §9/§10's own already-validated
convention (there, the equivalent terms equal $-F_\mathcal Q\times
\mathcal Q^{(2)}_{\alpha\text{-part}}$, matching the actual action's
$-\mathcal F(\mathcal Y,\mathcal Q)\supset-F_\mathcal Q\delta\mathcal
Q-\tfrac12F_{\mathcal Q\mathcal Q}(\delta\mathcal Q)^2$ structure).

**Independently verified and fixed**: compared the two conventions
directly (`wp7_derivation_energy_constraint_attempt.py`, sign
corrected) — confirmed §9/§10's minus-sign convention is the consistent
one, matches exactly. **Checked whether fixing this resolves the open
mismatch — it does not**: the corrected non-bracket piece is simply the
negative of the original; neither sign reduces to a clean multiple of
$\gamma$.

**Tried the advisor's more careful hypothesis**: compare against $8\pi
\tilde G\bar\rho\,\delta$'s own $\gamma$-term (using the established
identity $8\pi\tilde G\bar\rho(1+w)=-\dot{\bar\phi}F_\mathcal Q/2$,
rather than a bare $(1+w)$ comparison). Substituting $F_{\mathcal Q
\mathcal Q}=F_\mathcal Q/(\dot{\bar\phi}c_\text{ad}^2)$ and simplifying
gives exactly
$$F_\mathcal Q\Big(1+\frac1{c_\text{ad}^2}\Big)\gamma-2F_\mathcal Q\dot{
\bar\phi}\Psi$$
— **not** a clean multiple of $\gamma$ (the extra $-2F_\mathcal Q\dot{
\bar\phi}\Psi$ term persists). **This independently confirms the
advisor's own finding**: the hypothesis doesn't resolve the mismatch
either; the $\gamma$-sector piece remains genuinely open.

**Status: a real bug fixed (good for the program's internal
consistency across scripts), the headline §13 result reconfirmed
unaffected, and one more honest negative result on the remaining
gap.** The $(\chi,\alpha,\mathcal E_\alpha)$ variable set is now
independently validated at the level of both the vector equation and
the energy constraint's leading (bracket) structure — a genuinely
strong foundation, regardless of how the $\gamma$-sector piece
eventually resolves. Given this is now the **eighth** consecutive round
(§5–§14) on this one sub-derivation, and the piece still open (the
$\gamma$-sector normalization) concerns only the base ($F_\mathcal
Y=0$) theory's own bookkeeping — not the new completion itself, whose
two concrete new terms ($F_\mathcal Y\dot{\bar\phi}\chi$ in the vector
equation, §10; $-2F_\mathcal Y\dot{\bar\phi}^2\partial_1\alpha$ in the
momentum constraint, §12) are already cleanly isolated — recommending
this be weighed against whether closing the $\gamma$-sector gap is
still necessary for the R1 feasibility question specifically, or
whether it can be deferred as a standing item while the two identified
completion terms are used directly. Gate 4 remains paused. Nothing in
`cdot-7/` was touched.

## 15. One more careful shot at the $\gamma$-sector normalization, per the author's request — a genuine, precisely-characterized negative result

**Author asked for one more attempt at closing §13/§14's remaining
$\gamma$-sector mismatch.** Three independent checks performed, each
ruling out a plausible error source before accepting any residual as
genuine (`wp7_derivation_gamma_sector_normalization_attempt.py`, new,
`cdot-8/WP7/`):

1. **Fresh, bottom-up re-derivation** of the entire $\mathcal F(\mathcal
   Y,\mathcal Q)$ expansion's $O(\epsilon^2)$ piece — using
   independently-named symbols throughout, with no hand-assembled
   $\gamma,\mathcal Q^{(2)}$ substitutions carried over from earlier
   scripts — confirms §14's corrected $(-F_\mathcal Q,-F_{\mathcal Q
   \mathcal Q})$ convention exactly, term for term. No hand-assembly
   error found.

2. **Re-derived $\delta_2$** (the $A_0$ second-order correction)
   directly from the unit constraint $\hat A^\mu\hat A_\mu=-1$, not
   trusted from memory — confirmed exactly correct, ruling out an error
   propagating from §5.

3. **Derived the normalization constant self-consistently, not
   guessed**: $d(\text{action})/d\Psi$'s own (already-confirmed) bracket
   piece is $+2\kappa[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)
   \chi]$; the primary source's $\delta$-formula has this same bracket
   inside $\nabla^2[\ldots]/(8\pi\tilde G a^2\bar\rho)$, and using the
   standard, unambiguous $\nabla^2\to-k^2$ Fourier convention, $8\pi
   \tilde G\bar\rho\delta$'s own bracket-piece is $-\kappa[\text{same
   bracket}]$. Equating these fixes $c_0=-2$ in $d(\text{action})/d\Psi
   =c_0\cdot8\pi\tilde G\bar\rho\delta$ — derived from the already-
   validated bracket match itself, not an independent guess.

**Result**: applying this self-consistent $c_0=-2$ to the $\gamma$-
sector piece gives a precise, clean residual:
$$F_\mathcal Q\big(\dot\varphi-3\dot{\bar\phi}\Psi\big)$$
— **not zero**, i.e. still not a clean multiple of $\gamma=\dot\varphi-
\dot{\bar\phi}\Psi$ (the $-1$ coefficient on $\Psi$ in $\gamma$ becomes
$-3$ here). This is a genuinely clean, simple form — not "close but off
by a stray sign" — suggesting either a genuinely missing term (a
background-level correction via $\mathcal Q$'s own $O(\epsilon^2)$
shift to $\rho,P$; or a piece from the Einstein-Hilbert sector's own
$\Psi$-coupling to matter that a pure matter-action variation cannot
see) or that comparing against $\delta$'s $\gamma$-term in isolation
is not the complete picture (it may need to be read alongside $\theta$'s
own separate equation of motion for full self-consistency) — neither
checked here.

**Status: a genuine, careful, multiply-cross-checked negative result.**
Three plausible error sources (hand-assembly, $\delta_2$, and the
normalization constant itself) have each been independently ruled out.
The residual is real and now precisely characterized, not an assembly
artifact. **Not resolved in this attempt.** The headline bracket-match
result (§13), unaffected throughout, stands as the program's confirmed
foundation regardless. Given three focused attempts across §13–§15
have each independently converged on the same well-defined,
un-closing $\gamma$-sector gap, recommending this now be treated as a
standing, documented open item (not re-attempted without new
information) while the two already-confirmed $F_\mathcal Y$-completion
terms (§10, §12) and the confirmed bracket structure (§13) are used
directly for the next step: assembling the actual modified $\Pi$/
$\mathcal E_\alpha$ system and re-running the stability scan. Gate 4
remains paused. Nothing in `cdot-7/` was touched.

## 16. The actual answer to R1's feasibility question: the derived completion does not stabilize the ISW band — target-list item 1 resolved

**Assembled the actually-derived modification directly**
(`wp7_r1_derived_completion.py`, new, `cdot-8/WP7/`), using only what
this eleven-round derivation has confirmed, not guessed:

- **§10 (independently verified twice)**: the $\mathcal E_\alpha$
  equation's $\chi$-coefficient gets exactly one new additive term,
  $F_\mathcal Y\dot{\bar\phi}\chi$ — contributing $-F_\mathcal Y\bar{
  \mathcal Q}^2/(\mathcal K_BH)$ to the $(\alpha,\mathcal E_\alpha)$
  Jacobian's off-diagonal entry, $a_{\mathcal E_\alpha,\alpha}$.
- **§13 (independently verified, sign-corrected)**: $\Pi$/$\delta$'s
  own bracket $[\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi]$ is
  **confirmed $F_\mathcal Y$-independent** — $\mathcal Y$ has no $\Psi$-
  dependence (§5), so $F_\mathcal Y\mathcal Y$ cannot enter the energy
  constraint. **$\Pi$'s formula, and hence the Jacobian's trace,
  $a_{EE}$, is used completely unmodified.**

This directly answers the program's original target-list item 1 (does
$(2-\mathcal K_B)\to(2-\mathcal K_B)(1+\lambda_s)$ hold uniformly in the
FRW system?): **no — only the vector equation's off-diagonal term picks
up the completion; $\Pi$'s bracket, and the Jacobian's trace, do not.**

**Result: essentially no stabilization at the ISW band.** Scanning
$\lambda_s\in\{0,-0.5,-0.9,-0.99,-0.999,-1.0,-1.001,-1.5,1,10\}$ at
$k=2.71\times10^{-3}\,\text{Mpc}^{-1}$: $\max\text{Re}(\lambda)$ at
$z=1090$ is $3.35585\times10^8$ at every single $\lambda_s$ tested,
unchanged to 6 significant figures across the entire range, including
exactly at $\lambda_s=-1$ (where the earlier, crude "uniform
substitution" hypothesis had found *complete* stabilization). At lower
$z$ the response is present but negligible ($22.27\to22.66$ at $z=1$
across $\lambda_s=0\to-1$, a $\lesssim2\%$ shift). **This confirms —
now from an actual first-principles derivation, not a guess — the
qualitative conclusion §6's "refined attribution" heuristic reached by
structural argument**: the trace $a_{EE}$ (driven by $\Pi$'s own,
confirmed $F_\mathcal Y$-independent formula) dominates the instability
at every redshift and wavenumber checked, and $\lambda_s$'s effect (on
the now-confirmed-modified off-diagonal $a_{\mathcal E_\alpha,\alpha}$
alone) cannot touch it.

**Verdict on R1: not a viable recourse for the ISW/growth instability,
now established rather than merely suspected.** The completion this
whole derivation set out to test ($\mathcal F(\mathcal Y,\mathcal Q)$'s
free $F_\mathcal Y$ direction) genuinely modifies the theory exactly as
the founding paper's own parametrization suggests, but it modifies the
*wrong* piece of the vector-sector Jacobian to address this specific
pathology — the destabilizing term is $\Pi$'s own $\kappa_3$-bracket
contribution to the trace, structurally untouched by $\mathcal Y$'s own
free completion.

**One honest caveat, not resolved**: §12's momentum-constraint-sourced
$F_\mathcal Y$ term ($-2F_\mathcal Y\dot{\bar\phi}^2\partial_1\alpha$)
is **not** included in this scan — its precise placement in the coupled
6-variable system was not pinned down (unlike the vector equation's own
term, confirmed twice). Since this term structurally resembles another
off-diagonal-type contribution (not obviously trace-like), it is
unlikely to overturn the qualitative conclusion (the trace itself stays
confirmed $F_\mathcal Y$-independent regardless), but this is flagged
honestly, not asserted away.

**Status: the central R1 feasibility question is now answered,
derived rather than guessed, after eleven consecutive rounds (§5–§16)
of original derivation work.** Recommending this be reported to the
author/advisor as the resolution of the commissioned derivation's
primary question: R1 does not recover WP7's central deliverable at the
ISW-relevant wavenumbers. The honest options per the original recourse
ladder (`Advisory-WP7-InstabilityRecourses-2026-07-21.md`) narrow to
R3 (re-closure) or R4 (nonlinear-saturation reframing) — with real,
derived information in hand now, not a speculative bracket. Gate 4
remains paused; this diagnostic/derivation arc is now substantively
complete. Nothing in `cdot-7/` was touched.

**Advisory**: `Advisory-WP7-R1FeasibilityResolvedNotViable-2026-07-21.md`.
Confirms every result in §15 and §16 exactly, including an independent
by-hand trace of the new completion term back through §10's own
result, and independently confirms $\Pi$'s bracket is genuinely left
bare in the script (`dPi_dalpha` carries no $\lambda_s$-dependence),
matching §13. Explicitly notes the two durable results produced by this
arc regardless of R1's outcome — the validated $(\chi,\alpha,\mathcal
E_\alpha)$ variable set (§9–§13) and R1's now-settled feasibility
question — and recommends the recourse ladder move formally to R3 or
R4, an author-level sequencing decision. **Author chose R3.**

## 17. R3 (re-closure) — a first, bounded feasibility scan: a modest dent, not a resolution

**What R3 claims** (per `Advisory-WP7-InstabilityRecourses-2026-07-
21.md` §3): $c_\text{ad}^2(z)$ is a trajectory *output*, not a free
input — the matter-era $w$ sitting slightly below zero is what makes it
negative, and that offset moves under a changed census content or fit,
notably the low-$\Sigma m_\nu$ re-closure already flagged as the
KATRIN-aligned WP4a lever. **The advisory explicitly warns this
"cannot be tuned in isolation — the invoice is forced at fixed $E(z)$
and census"** — a full, rigorous R3 test requires the joint Q2/EFE
re-fit (Gate 3's own standing, deferred item), not attempted here.

**What was attempted instead, honestly scoped as a feasibility test,
not the full re-fit** (`wp7_r3_reclosure_feasibility.py`, new,
`cdot-8/WP7/`): held $\Omega_\text{closure}=0.074$ fixed (the one
number this program's census fit constrains directly) and varied only
the internal split between the neutrino and cold-matter pieces (lower
per-flavor neutrino mass $M_\nu$ shifts mass from the neutrino sector
into $\Omega_\text{cold}$, at fixed total), re-running the exact same
closure ODE machinery unmodified for each value — the narrower question
of whether the KATRIN-aligned direction shifts $c_\text{ad}^2(z)$ in the
needed direction *at all*, before committing to the full re-fit.

**Result**: scanning $M_\nu$ from the baseline $0.458\,\text{eV}$
($\Sigma m_\nu=1.374\,\text{eV}$) down to $0$ (an extreme, unphysical
end-point — real neutrinos have a known nonzero minimum mass from
oscillation experiments, $\Sigma m_\nu\gtrsim0.06\,\text{eV}$):
$c_\text{ad}^2(z{=}1090)$ moves from $-0.219$ to $-0.126$ — roughly
**halved**, a real, non-negligible response in the right direction —
but **stays firmly negative throughout the entire range, including at
the unphysical $M_\nu=0$ endpoint**. The resulting instability
($\max\text{Re}(\lambda)$ at the ISW $k$) drops correspondingly at
$z=1090$ (from $3.36\times10^8$ to $1.64\times10^8$, roughly halved)
but remains catastrophically large — nowhere close to stabilizing.
**At $z=10$ the instability actually *worsens slightly* as $M_\nu\to0$**
($131\to204$); at $z=1,0$ the response is negligible either way.

**Verdict on this narrow test of R3: informative, not sufficient.**
The neutrino/cold split, on its own, moves $c_\text{ad}^2$ in the
needed direction by a real but insufficient amount, and does not even
help monotonically across all redshifts — confirming, concretely, the
advisory's own caution that this lever "cannot be tuned in isolation."
This does **not** rule out the *full* R3 (a joint re-fit that also lets
$E(z)$ itself respond, not just the internal split at fixed total) —
that heavier, synergistic lever has not been attempted here and remains
the open question. **Status: R3's cheap, bounded first test is
negative on its own but does not close the door on the full re-fit.**
Recommending this be reported back before deciding whether to commission
the full joint Q2/EFE re-fit or move to R4. Gate 4 remains paused;
Gate 3's Q2/EFE sequencing remains the standing prerequisite for a
complete R3 test. Nothing in `cdot-7/` was touched.
