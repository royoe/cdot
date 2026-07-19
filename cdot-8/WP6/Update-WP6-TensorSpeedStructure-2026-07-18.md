# Update — WP6: Structural First Installment — Tensor Speed Imported, PPN/Binary-Pulsar Sector Scoped

*Companion: `SessionLog-2026-07-18.md` (this directory, to be created).
Proceeds under Gate 1's explicit provisional-failure caveat
(`cdot-8/proposal/DecisionGates-2026-07-18.md`): WP4a's 27% crossover-era
$\theta_*$ miss is a **not-yet-viable, unresolved** finding, not a cleared
one — this WP6 work is legitimate parallel/sequential work under that
caveat, per the author's explicit sequencing instruction (complete through
WP7 before revisiting radiation-era assumptions), not a claim that the
background problem is solved.*

---

## 1. What's already established in AeST's own literature — import, don't re-derive

Following WP5's rhythm: check what the chassis theory already guarantees
before deriving anything new.

**Tensor-mode speed $c_\text{gw}=c_\gamma$ is a deliberate, foundational
design requirement of AeST, not an accident or a fine-tuned limit.**
Fetched the founding paper (Skordis & Złośnik, "A new relativistic theory
for Modified Newtonian Dynamics," PRL 127, 161302 / arXiv:2007.00082) and
confirmed directly: the paper states GW170817/GRB170817A "strongly
constrains the GW tensor mode speed to be effectively equal to that of
light," notes that "TeVeS has been shown to be incompatible with the
LIGO-Virgo observations for any choice of parameters," and states AeST was
designed specifically to satisfy "requirement (v): propagate tensor mode
gravitational waves (GWs) at the speed of light" — achieved through the
$\{g_{\mu\nu},B_\mu\}$ field content such that "the tensor mode speed
equals the speed of light in all situations" (their own emphasis, not
paraphrased). The companion stability paper (already used in WP5, PRD 106,
104041) independently confirms this at the perturbative level: tensor
modes "propagate at the speed of light," citing a more general result for
the whole class of theories AeST belongs to. **This is a structural,
by-construction property of the chassis, exactly like WP5's imported
$\Psi=\Phi$ — not something WP6 needs to re-derive from scratch.**

**PPN preferred-frame parameters ($\alpha_1,\alpha_2$) are NOT addressed
anywhere in AeST's own literature** — checked both the founding paper and
the stability paper directly; neither mentions PPN parameters at all.
This matches WP0's own finding (2026-07-11): binary-pulsar testing of AeST
specifically is "confirmed still fully open" — no paper anywhere applies
binary-pulsar timing to AeST, though the parallel Einstein-æther/
khronometric pulsar-constraint literature is mature (Yagi, Blas, Barausse &
Yunes 2014, arXiv:1311.7144; Vaglio et al. 2026, arXiv:2605.01436, the most
recent and stringent single-system bound, PSR J1738+0333) and structurally
adaptable, since both theories are unit-timelike-vector (aether)
constructions in the same technical family. WP0 named this the concrete
path for WP6, not starting from scratch.

## 2. The genuinely new (cdot-8-specific) question: does M5 disturb the tensor sector?

WP5's central structural question was whether M5's census/closure
constraint — which lives entirely in the scalar sector, modifying only how
$F(Q)$ is determined (quadrature-fixed vs. AeST's native free, shift-
symmetric choice) — reaches into the *local, non-scalar* sectors of the
theory. WP5 answered this for the quasistatic vector/scalar (lensing,
weak-field) sector via the local-decoupling argument (M5 constrains only
the background $Q_0(t)$; local physics runs on standard AeST at whatever
$a_0(t)$ the background sets) and, independently, via the SZ stability
paper's own quadratic-order sector-additivity result (the $Q$-sector and
$Y$-sector separate at second order — already load-bearing for WP5's
$m_\text{eff}$ result, §6c).

**The same additivity argument applies here, more directly.** cdot-8's
charter modification touches *only* the free function's $Q$-dependence —
it does not touch the Einstein-Hilbert term, the aether's kinetic
coefficients ($K_B$ and friends), or the $\phi$–$A$ coupling $Q_0$. The
tensor-mode dispersion relation, per both AeST papers checked in §1, is
fixed entirely by the metric/aether kinetic sector — nowhere does $F(Q)$
or its derivatives enter the tensor-mode calculation in either source.
**Named assumption (flagged, not yet independently re-derived at the
perturbation-theory level myself)**: since $F(Q)$ enters the action only
in the scalar/$Q$-sector, and cdot-8 changes nothing about the tensor
sector's own field content or kinetic terms, $c_\text{gw}=c_\gamma$
survives in cdot-8 exactly as in vanilla AeST, "in all situations" per the
founding paper's own claim, independent of the M5 modification. This is
lower-risk than WP5's decoupling argument was (WP5 had to construct the
horizon-integral argument from scratch; here the sector-additivity result
is already established and already used once, successfully, in WP5's
$m_\text{eff}$ derivation) — but flagged as an assumption pending its own
explicit check, not asserted as proven, per this program's standing
discipline.

## 2a. Advisory response — the named assumption discharged, tensor import strengthened, sub-task 1 reframed before a known result got re-discovered

`Advisory-WP6-FirstInstallment-2026-07-18.md` + `mu_swap_exposure.py`.
**Checked every load-bearing claim against the primary source myself
rather than accept the advisory's confidence** — this is where the
session's standing discipline earned its keep again, in both directions.

**Confirmed, independently, via direct re-fetch of the stability paper**:
Eq. 20's tensor action is exactly GR's (quoted precisely: "$S^{(T)}=\int
d^4x\{\dot H^{ij}\dot H_{ij}-\bar\nabla^kH^{ij}\bar\nabla_kH_{ij}+32\pi
\tilde G\Sigma^{ij}_LH_{ij}\}$"), citing Skordis & Złośnik 2019 (PRD 100,
104013) for the general class-level result. This closes the "named
assumption" from §2 cleanly: $H_{ij}$ enters neither $Q$ nor $\mathcal Y$
at linear order (both built from $A_\mu,\phi$, which carry no tensor
part), so $\delta^2F$ contains no $H_{ij}$ regardless of $F$'s functional
form — cdot-8's modification cannot reach the tensor sector through $F(Q)$
by construction, not merely by assumption. The advisory's further point —
that M5's own multiplier term is *also* tensor-blind at linear order
(the background $\bar Q$ is a scalar functional with no tensor part;
tensor-mode backreaction on $\mathcal N_\text{tot}$ is second-order, GW
energy density, horizon-diluted) — is standard scalar/vector/tensor
cosmological-perturbation-theory reasoning (a scalar constraint cannot
source tensor perturbations at linear order in an FRW background) and I
accept it on that basis. **Verdict, now solid rather than merely
plausible: $c_\text{gw}=c_\gamma$ holds in cdot-8 "in all situations,"
carrying only Gate 1(b)'s background caveat, which this sector is
independent of.** The added standard-siren prediction ($d_L^\text{GW}/
d_L^\text{EM}=1$, from the constant bare $\tilde G$ prefactor and no
running Planck mass) is a direct, low-risk corollary — accepted, and
worth registering as a future-facing prediction per Gate 2's stated aim.

**Confirmed, independently, by reproducing the script**: `mu_swap_exposure.py`
runs exactly as claimed (24–41% Cassini-safe-family offset at the
working points $x=1.10/1.72/2.61/3.44$). The reframing is correct and
important: this program's own closure has used $\mu(x)=x/(1+x)$ — the
simple function — since WP2 (visible in every trajectory script this
session has touched, e.g. `mu0 = X0/(1+X0)` in `meff_skeleton.py`), and
its slow high-$x$ return is exactly what `cdot-4/T22` already excluded by
$\sim2800\times$ against Cassini ranging. Running sub-task 1 naively
against the naked $\mu$ would have "discovered" a known result, not a new
cdot-8 finding — the advisory caught this before it happened, correctly.
**Sub-task 1 is reframed**: the actual Cassini-testable object is AeST's
own screening sector (not the bare interpolating-function tail), and the
closure's own exposure to a Cassini-safe $\mu$-swap (a tens-of-percent
$\kappa\lambda/x_0$ refit) is a real, externally-forced candidate for
Gate 1(b)'s post-WP7 options review — quantified, not executed, per the
author's explicit sequencing instruction.

**One claim did NOT survive my check, and I'm not accepting it.** The
advisory's Entry 2 (added directly to the session log, not through me)
claims my Brouwer-quote correction from the WP5 round was itself wrong —
that the "single most severe limitation" quote "appears verbatim... in
the PUBLISHED journal version (A&A 650, A113)." **I checked this a third
time, directly against the paper's own page on the publisher's site**
(aanda.org), not just arXiv — the quote is not there either. The closest
passage (§4.3, the BAHAMAS missing-baryons discussion) discusses the
uncertainty at length but does not use this or comparably emphatic
severity language, in either the arXiv or the published version, checked
independently twice more. **Holding my original correction**: the quote
as attributed to Brouwer et al. is not supported by the primary source in
any version I can access. This doesn't touch the design's substance
(missing baryons is still a real, discussed, common-mode systematic in
that paper — just not stated with the specific severity wording claimed),
but a ledger correction that itself doesn't check out shouldn't be
accepted just because it arrived with confidence — same rule applied to
the advisory as to myself throughout this program.

**The KATRIN specifics added in the same log entry, checked live**:
confirmed via web search — KATRIN's published bound is $m_\beta<0.45$ eV
(90% CL, Science, April 2025, DOI 10.1126/science.adq9592), based on 259
days of data (of 1000 days total, concluded end-2025). This part of the
advisory's housekeeping content is accurate.

## 3. Scoping the remaining WP6 work

Three concrete, separately-scoped tasks, in the order WP0 recommended:

1. **Cassini/ephemeris-level interpolating-function test** — cheapest,
   nearest-term. Reuses `cdot-4/T22`'s already-built machinery (which
   excluded MOND's *simple* interpolating function by $\sim2800\times$
   against Cassini-era Saturn ranging, mirroring Hees et al. 2014/2016)
   against whichever specific interpolating-function shape cdot-8's own
   quasistatic limit settles into — not yet checked which shape that is;
   first sub-task.
2. **PPN $\alpha_1,\alpha_2$** — requires working out AeST's
   preferred-frame parameters directly (not available in the literature),
   informed by the Einstein-æther PPN machinery (the aether sector is
   structurally the same unit-timelike-vector object).
3. **Binary-pulsar confrontation** — the actual data test, gated on #2;
   adapts the Yagi et al. 2014 / Vaglio et al. 2026 sensitivity-
   function/orbital-decay machinery, per WP0's identified concrete path.

## 4. Sub-task 1, executed under the reframed protocol: a model-independent screening bound, not a μ pass/fail

Per §2a's accepted reframing — the Cassini-testable object is AeST's own
large-gradient completion (screening/tracking), not the naked simple
$\mu(x)=x/(1+x)$ this program's closure has always used for cosmological
fitting.

**Understood AeST's own mechanism first, from the primary source.**
Fetched the stability paper (PRD 106, 104041) directly for the "two ways
GR can be restored" passage: $\lambda_s$ enters the effective Newton
constant ($G_N=\frac{1+1/\lambda_s}{1-K_B/2}\tilde G$) and the deep-MOND
free-function piece ($\mathcal F\to\frac{2\lambda_s}{3(1+\lambda_s)a_0}
|\mathcal Y|^{3/2}$); **screening** is described as additional terms
$\mathcal J\sim\mathcal Y^p$ ($p>3/2$) or Galileon-type terms that dominate
at large field gradients, suppressing MOND deviations in the solar
system; **tracking** is the alternative regime where $\lambda_s\varphi$
becomes proportional to the Newtonian potential directly. **The paper
gives the mechanism class but no unique functional form or normalization
and no quantitative solar-system bound** — confirmed by direct check, not
just WP0's earlier finding: this is a genuine, still-open gap, not
something with a citable number to import.

**Set up the confrontation on `cdot-4/T22`'s own already-validated
numbers** (no new derivation risk in this part): $g_\dagger=1.13\times
10^{-10}$ m/s² (the naked-simple asymptote, T22's own figure), Cassini
bound on anomalous constant acceleration at Saturn $\approx4\times
10^{-14}$ m/s², $y_\text{Saturn}\equiv g_\text{bar}/g_\dagger=755^2=
570{,}025$ (T22 quotes $\sqrt y=755$). **Re-derived T22's own $\sim2800
\times$ figure independently** (caught and fixed a wrong first attempt of
my own — conflated the correction term with the leading term before
re-checking against T22's exact quoted asymptote): solving $\mu(u)u=y$ for
the naked simple $\mu$ at $y_\text{Saturn}$ gives $g_x\to g_\dagger$
*exactly, as a constant, not a decaying tail* — the anomaly does not
shrink with $g_\text{bar}$ at leading order, which is exactly why it is
excluded so cleanly: $g_\dagger/(\text{Cassini bound})=2825\times$,
reproducing T22's number to the reported precision, confirming the setup
before using it.

**The actual sub-task-1 result**: solved the same $\mu(u)u=y$ relation for
two illustrative fast-tail completions (the "standard"/RAR form $\mu(u)=
u/\sqrt{1+u^2}$, already used in §2a's $\mu$-swap exposure; an exponential
MLS-type form $\mu(u)=1-e^{-u}$) at the identical Saturn point:

| completion | $g_x$ [m/s²] | $g_x/\text{Cassini bound}$ |
|---|---:|---:|
| naked simple | $1.13\times10^{-10}$ | $2825\times$ **(excluded)** |
| standard/RAR | $9.9\times10^{-17}$ | $2.5\times10^{-3}$ **(passes by $\sim400\times$)** |
| exponential | $\sim0$ | $\sim0$ **(passes trivially)** |

**Conclusion, model-independent**: whatever large-gradient completion
AeST's/cdot-8's screening or tracking sector actually settles into must
suppress the Saturn anomaly by $\gtrsim2800\times$ relative to the naked
tail — and this is satisfied by *enormous* margin (2–286+ orders of
magnitude, not a marginal pass) by any completion that isn't the literal
unmodified simple tail. **This confirms the advisory's expected outcome
(a) directly, by calculation rather than by citing the expectation**:
AeST's screened quasistatic limit passes Cassini/ephemeris bounds
comfortably; the naive $2800\times$ exclusion is a property of the naked
simple function used only for this program's own cosmological-closure
convenience, not a threat to the theory's actual local-gravity sector.

**What this does NOT establish, stated plainly**: a precise numerical
bound on AeST's own $(\lambda_s,p)$ parameters, or a specific screening
onset scale, from Cassini data — the literature doesn't fix a unique
completion function (only the mechanism class), so pinning that down
would mean choosing a specific ansatz not yet derived from cdot-8's own
first principles, which risks presenting invented physics input as an
extracted constraint. That further derivation (deriving the actual
screening completion from cdot-8's own quadrature/M5 machinery, the way
$F(Q)$ was derived for the $Q$-sector) is separate, real work, not yet
attempted — flagged honestly rather than filled with a plausible-looking
number.

**Status: sub-task 1 closed as scoped.** cdot-8 inherits AeST's screening
machinery unchanged (per §2a's sector-additivity result — cdot-8 never
touches the $Y$-sector), and that machinery comfortably passes Cassini
once any reasonable completion is used instead of the naked closure-
fitting $\mu$. Next: sub-task 2 (PPN $\alpha_1,\alpha_2$), the program's
real remaining WP6 work, per the advisory's own framing that the
æ-theory literature is scaffold, not answer, here.

## 5. Sub-task 2, first step: why the æ-theory PPN formulas are not just imprecise but formally singular for AeST's aether alone — and what that implies

Started from the standard Einstein-æther PPN result (Foster & Jacobson,
PRD 73, 064015 / gr-qc/0509083, fetched and quoted directly, not from
memory) rather than the more restrictive Vaglio et al. 2026 pulsar paper,
since $\alpha_1,\alpha_2$ are defined at the level of the general
kinetic tensor $K^{ab}_{mn}=c_1g^{ab}g_{mn}+c_2\delta^a_m\delta^b_n+
c_3\delta^a_n\delta^b_m+c_4u^au^bg_{mn}$, their own Eq. (2):
$$\alpha_1=\frac{-8(c_3^2+c_1c_4)}{2c_1-c_1^2+c_3^2},\qquad
\alpha_2=\frac{(2c_{13}-c_{14})^2}{c_{123}(2-c_{14})}-\frac{12c_3c_{13}+
2c_1c_{14}(1-2c_{14})+(c_1^2-c_3^2)(4-6c_{13}+7c_{14})}{(2-c_{14})
(2c_1-c_1^2+c_3^2)}$$
with $c_{13}=c_1+c_3,\ c_{14}=c_1+c_4,\ c_{123}=c_1+c_2+c_3$.

**Mapped AeST's own vector kinetic term onto this basis.** AeST's action
(§1) carries $-\frac{K_B}{2}F^{\mu\nu}F_{\mu\nu}$ for the aether, a
purely Maxwell-type (antisymmetrized) term: $F^{\mu\nu}F_{\mu\nu}=2[(\nabla_\mu
A_\nu\nabla^\mu A^\nu)-(\nabla_\mu A_\nu\nabla^\nu A^\mu)]$, built *only*
from the $c_1$- and $c_3$-structures in Foster-Jacobson's basis, with
none of the $c_2$ (divergence-squared) or $c_4$ (radial/acceleration)
structures present. **This fixes $c_2=c_4=0,\ c_3=-c_1$** — a relation
convention-independent of the overall sign/normalization match between
the two papers' actions (not separately pinned down here, and flagged as
needing an explicit check before any numerical value is quoted).

**Checked symbolically (sympy, not hand algebra) rather than risk an
arithmetic slip**: substituting $c_2=c_4=0,\ c_3=-c_1$ gives $c_{13}=0$,
$c_{14}=c_1$, $c_{123}=0$, and $\alpha_1=-4c_1$ — a clean, finite result.
**But $\alpha_2$'s first term has $c_{123}$ in the denominator, and
$c_{123}=0$ identically for this restricted class — the formula
diverges** ($c_1^2/[0\times(2-c_1)]$), for any $c_1\neq0$.

**Verified this is not an artifact of the mapping, but a known,
independently-documented degeneracy of Einstein-æther theory itself**:
searched the wider æ-theory literature and confirmed the spin-0
(scalar) aether mode's propagation speed is $\propto c_{123}(2-c_{14})/
[\ldots]$ — vanishing identically at $c_{123}=0$, i.e. **the aether's own
would-be scalar mode is non-dynamical exactly on the line AeST's kinetic
term sits on.** This is not a coincidence worth worrying about — it is
the physically sensible reason AeST is built the way it is: AeST supplies
its MOND scalar via an *explicit* dynamical field $\phi$ (with its own
kinetic term $F(Q)$/$\mathcal J(\mathcal Y)$) precisely because the
aether alone, restricted to a pure Maxwell kinetic term, carries no
scalar dynamics of its own to repurpose. The design choice and the PPN
degeneracy are two faces of the same fact.

**What this establishes, and what it doesn't.** It **sharpens** the
advisory's caution ("æ-theory formulas cannot be lifted directly") from a
general warning into an explicit, checkable demonstration: naively
plugging AeST's $K_B$ into Foster-Jacobson's $\alpha_2$ formula doesn't
give an imprecise number — it gives $\infty$, because the formula
implicitly assumes the aether carries its own propagating spin-0 mode,
which AeST's aether, by construction, does not. **The actual PPN
$\alpha_1,\alpha_2$ for AeST/cdot-8 must be derived with the scalar field
$\phi$ and its $Q_0$-coupling to $A_\mu$ (the $\chi=\varphi+Q_0\alpha$
mixing) included from the start** — this is not optional scaffolding on
top of a pure-aether baseline; it is the object that supplies the
otherwise-absent scalar dynamics the PPN formula needs to stay finite.
**This is genuinely substantial, original derivation work — effectively
redoing Foster-Jacobson's own multi-stage PPN calculation with an
additional coupled scalar field** — and is not completed in this pass.
Given the stakes of a wrong PPN verdict in either direction (a false
pass would misrepresent a real constraint; a false kill would wrongly
end a structurally sound line of the program), this is exactly the kind
of hard, novel calculation this program has historically staged across
several checkpointed rounds (WP3's action-closure work) or handed to a
touch point, rather than forced to a number in one pass.

## 5a. Advisory checkpoint — verified to the digit, two structural additions accepted

`Advisory-WP6-CheckpointVerified-2026-07-18.md` + `wp6_verification.py`.
**Reproduced the whole verification script myself** (Saturn table exact;
PPN algebra exact) before accepting anything built on it.

**Addition 1, accepted — the flagged "further derivation" of a screening
completion from cdot-8's own machinery is not just future work, it's
impossible in principle.** The quadrature (§4's F(Q) derivation, and every
prior WP3 round it descends from) is built entirely on the homogeneous
FRW background, where $\mathcal Y\equiv0$ identically — there is no
regime in which the background trajectory has any support on the
$\mathcal Y$-sector, at any order. cdot-8's zero-freedom machinery
therefore structurally cannot determine the high-gradient completion; it
was never a hard-but-open derivation, it's a category the quadrature
doesn't reach. **Accepted, and worth stating plainly for the charter**:
"zero adjustable elements" is a claim about the $Q$-sector alone. The
$\mathcal Y$-sector (MOND shape, screening/tracking completion) is, and
remains, AeST-inherited functional freedom, bounded by data from both
ends — a limitation shared with every relativistic MOND completion, not a
cdot-8-specific gap, but one the program should state itself rather than
leave for a referee to point out.

**Addition 2, accepted with a caveat on my own §4 framing** — the
closure's cosmological $\mu$ (Q-sector, entering through fitted $E(z)\to$
invoice $\to F(Q)$) and the galaxy/solar-system interpolation (Y-sector)
are *formally distinct objects* in cdot-8's actual covariant construction,
even though cdot-7's simpler treatment used one function for both (the
"AQUAL economy"). This means a Cassini-safe Y-sector completion does
**not** automatically force sub-task 1's flagged 24–41% background refit
— that only follows if the single-$\mu$ identification is kept as an
explicit unifying principle, which is a real modeling choice, not yet
made. **Correcting my own §4**, which implicitly treated the two as one
function without flagging this as a choice: the "magnitude coincidence"
between the $\mu$-swap exposure and WP4a's 27% miss stands *conditionally*
— live only if the economy is retained — and the economy-vs-freedom
question itself is Gate-1-revisit material for the author, not a default
either of us should assume.

**Addition 3, verified independently rather than accepted on statement**:
checked algebraically (symbolically, general $c_4$, not just at cdot-8's
specific $c_4=0$ point) that $\alpha_1=-4c_{14}$ holds identically
whenever $c_{13}=0$ — confirmed this is exactly zero as a polynomial
identity, not merely true at one substitution. Cross-checked against the
wider post-GW170817 Einstein-æther literature (Oost, Wang, Mukohyama-class
papers, arXiv:1802.04303 among them): the standard post-GW170817
parameter space is indeed organized on the $(c_1,c_{14})$- and
$(c_2,c_{14})$-planes precisely because $c_{13}\approx0$ is forced by the
tensor-speed bound — consistent with, though not a verbatim primary-source
quote for, the specific "$\alpha_1=-4c_{14}$" phrasing. **The unifying
point is real and worth keeping**: the same Maxwell-only kinetic choice
that gives AeST its exact $c_\text{gw}=c_\gamma$ ($c_{13}=0$) is what
kills the aether's own scalar mode ($c_{123}=0$) — requirement (v) and
the PPN singularity are one design fact, not two.

**Staged path for the actual derivation, accepted as the plan**: (i)
boost the already-established screened quasistatic system (Mistele's
Eq. 1, imported in WP5) to a source moving at $w$ relative to the aether
rest frame at 1PN — generates the $\alpha_1$ vector-potential sector; (ii)
the $\alpha_2$-generating anisotropic terms next; (iii) carry the
$\chi=\varphi+Q_0\alpha$ scalar-vector mixing throughout but not
condensate contamination, since WP5's $\mu_\text{eff}^{-1}\sim$ Gpc means
the condensate is irrelevant at pulsar/PPN scales. Pre-registered,
loosely-stated expectation: $\alpha_1$ takes the $-4c_{14}$ form completed
by $\phi$-sector terms in $(K_B,Q_0)$; $\alpha_2$ becomes finite once the
full (scalar+vector) system is used, since the SZ stability paper already
establishes the full spectrum is healthy — the divergence found in §5
belongs to the restricted, aether-only formula, not to the theory. **Not
yet executed** — genuinely new derivation work, staged per WP3's own
precedent for hard, consequential calculations.

## 5b. Attempting the staged 1PN derivation — genuine progress, and one real, unresolved fork found before pushing further

**Verified the exact field content first, rather than work from
recollection** (a recollection that turned out to be wrong on one point):
fetched AeST's own covariant definitions directly — $\mathcal Q=A^\mu
\nabla_\mu\phi$, $\mathcal Y=(g^{\mu\nu}+A^\mu A^\nu)\nabla_\mu\phi\nabla_\nu
\phi$ (the projector orthogonal to $A$, spatial-gradient-squared on a
timelike-aligned background), and $J^\mu=A^\nu\nabla_\nu A^\mu$ — **the
aether's own acceleration vector**, not a scalar current as I loosely
described it in §1/§2a. This corrects the record before it propagated
further.

**Understood the physical setup Foster-Jacobson use, fetched directly
rather than assumed**: $\alpha_1,\alpha_2$ live in the metric's $g_{0i}$
sector, sourced at the PPN order where the aether's spatial component
$u^i$ (zero on a static, aligned background) is first generated by
matter's momentum flux $\rho v^i$ — solved order-by-order: $u^0$ and the
metric's static sector first, then $u^i$ from the aether's own field
equation sourced by $\rho v^i$, then fed into the $g_{0i}$ Einstein
equation to read off $\alpha_1,\alpha_2$. This is exactly the same
order-counting logic as §5's static-limit finding — **and reproduces it
as a special case**: vanilla aether's $u^i$ solution has $c_{123}$ in a
denominator (confirmed from the same source), so it is *itself* singular
at AeST's kinetic-term point, independent of and prior to the PPN
$\alpha_2$ formula's own divergence — consistent, not a new problem.

**Attempted to trace whether $\delta\phi$ can regularize this**, since
that's the pre-registered expectation. Traced the coupling channel
carefully: $\delta\mathcal Q$ at the relevant order picks up contributions
from $A^{i}\partial_i\phi_0$ (zero, since the background $\phi_0$ depends
only on cosmological time, not position) and from $A^\mu=g^{\mu\nu}A_\nu$
index-raising against the metric's *own* $g^{0i}$ — meaning $\phi$'s
source term can, in principle, feel the momentum-flux sector *indirectly*,
through the metric's frame-dragging-like potential, even before any
direct aether-$\phi$ coupling is invoked. **This is a real, non-obvious
fork I cannot respectably resolve by prose reasoning alone**: whether this
indirect channel is actually present and non-vanishing at the needed
order depends on details (gauge choice, whether $\delta\phi$ has a
consistent, non-trivial solution at this PN order at all, whether the
$J^\mu\nabla_\mu\phi$ coupling contributes a term here or only at even
orders) that Foster-Jacobson's own dedicated, order-by-order appendix
exists specifically to track correctly for the simpler pure-aether case.
Attempting this in prose, without the same systematic bookkeeping, risks
exactly the kind of subtle sign/order error this program has hit
repeatedly in comparable calculations (WP3's own multi-round history).

**Being explicit about the stakes of getting this wrong in either
direction**: if $\delta\phi$ does *not* participate at this order, AeST's
Maxwell-only aether choice may carry a genuine, unavoidable singularity in
its own preferred-frame sector — a real, potentially kill-relevant finding
quite different from the advisory's optimistic pre-registered expectation
(that $\phi$ completes $\alpha_1$ into a finite value). If it *does*
participate via the indirect channel, the pre-registered expectation
likely holds. **I do not yet know which, and asserting either would be
guessing dressed as a derivation.** Recommending this specific fork —
does $\delta\phi$ acquire a solution at the momentum-flux-sourced PPN
order, through the metric's own $g_{0i}$, or does the singular vanilla-
aether result stand unregularized — as the concrete next question,
ideally checked with the same order-by-order discipline Foster-Jacobson
used (ideally cross-checked independently, given a wrong answer here
could misrepresent a real problem as solved or dismiss a solid result as
broken).

## 6. Status

**Structural first installment and sub-task 1 both closed; sub-task 2
opened with a genuine, verified structural finding, not yet a number.**
Tensor speed imported and independently confirmed solid (§2a); the
genuinely new decoupling question named and discharged (§2a); sub-task 1
(Cassini/ephemeris) closed with a model-independent screening bound,
comfortably satisfied (§4). **Sub-task 2 (PPN $\alpha_1,\alpha_2$)**:
established, and independently checked both symbolically and against the
wider literature, that AeST's aether alone sits at Einstein-æther's
$c_{123}=0$ degeneracy — explaining precisely why the scalar-vector
mixing is mandatory input, not a refinement, and scoping the remaining
derivation honestly as substantial, original work, not yet attempted.
Sub-task 3 (binary-pulsar confrontation) remains gated on it. **Checkpoint
independently verified (§5a)**: the screening-completion derivation is
now understood to be impossible in principle (not just future work),
yielding a scope statement for the charter ("zero adjustable elements" is
a $Q$-sector claim only); the closure-$\mu$/galaxy-$\mu$ identification is
now flagged as an explicit, unmade modeling choice rather than an assumed
unification, with the $\mu$-swap's magnitude-coincidence conditional on
it; $c_{13}=0$ (tensor speed) and $c_{123}=0$ (PPN singularity) confirmed
to be the same design fact; a staged 1PN-boost derivation path is
pre-registered but not yet executed. Every finding here inherits Gate 1's
provisional-failure caveat on the cosmological background — not a
clean-foundation claim. The KATRIN clock's specific content is on record
(§2a: $m_\beta<0.45$ eV, 90% CL, Science 2025, 259/1000 days; final
sub-0.3 eV analysis pending). Nothing in `cdot-7/` was touched.

**The staged 1PN derivation was then attempted (§5b) and reached a
genuine, unresolved fork, honestly reported rather than forced past.**
Corrected $J^\mu=A^\nu\nabla_\nu A^\mu$ (the aether's own acceleration,
not a scalar current as earlier sections loosely described). Confirmed
vanilla aether's own momentum-flux-sourced $u^i$ is independently
singular at AeST's kinetic-term point. **The open question that decides
everything downstream**: does $\delta\phi$ acquire a solution at this
same PPN order — through a plausible but unconfirmed indirect channel via
the metric's own $g_{0i}$ — that regularizes $\alpha_1$ as pre-registered,
or does the singularity stand, a genuine problem for AeST's Maxwell-only
aether choice? **Not resolved in this pass** — flagged as needing the
same order-by-order rigor Foster-Jacobson's own derivation required, not
prose reasoning, given the real cost of guessing wrong in either
direction.

## 5c. The fork resolved — verified from first principles, not accepted on the advisory's presentation

`Advisory-WP6-ForkResolved-2026-07-18.md` + `ppn_fork_resolution.py`.
Claims: $\delta\phi$ participates via the *direct* combination $U_i=
\partial_i\delta\phi+Q_0A_i$ (not the conjectured indirect $g_{0i}$
channel), the $(\delta\phi,A_i)$ gradient matrix is rank 1 as a result,
and this is *why* vanilla æ-theory's $c_{123}=0$ singularity is an
artifact of inverting a mode AeST doesn't independently contain.

**Did not accept the rank-1 claim on the strength of the script's
linear algebra alone** — the script *posits* $\mathcal Y_\text{quad}
=c_\mathcal Y(\partial_i\delta\phi+Q_0A_i)^2$ and then observes
(correctly, but trivially) that any outer-product form has rank 1. The
substantive physics claim is whether $\mathcal Y$'s quadratic expansion
really collapses to exactly this form. **Derived it independently from
scratch** (sympy, exact unit-timelike constraint, not the linearized
approximation): with $A^\mu A_\mu=-1$ enforced exactly (so $(A^0)^2=1+
(A^i)^2$, not just $A^0\approx1$), expanding $\mathcal Y=(g^{\mu\nu}+
A^\mu A^\nu)\nabla_\mu\phi\nabla_\nu\phi$ to quadratic order in
$\{\delta\phi,A^i\}$ gives, exactly,
$$\mathcal Y_\text{quad}=(\partial_i\delta\phi+Q_0A^i)^2$$
— confirmed to be identically zero difference from the claimed form, not
an approximation. **This is a real, independently-verified result, not
an assumption**: the crucial $Q_0^2(A^i)^2$ piece — without which the
rank-1/outer-product structure wouldn't hold — comes specifically from
the unit constraint's second-order correction to $A^0$, a detail the
script's own presentation didn't show working but which checks out
exactly when derived from the primary definitions (arXiv:2109.13287's
own $\mathcal Q,\mathcal Y$ definitions, already on file in `references/`).

**What this confirms**: $\delta\phi$ and the aether's spatial tilt $A^i$
are not independent gradient-carrying degrees of freedom in AeST's
$\mathcal Y$-sector — they appear *only* through $U_i$, exactly as
Mistele's Eq. 1 (already load-bearing since WP5) already displayed in
the static limit. Vanilla æ-theory's singular $u^i$ solution inverts a
gradient operator for the *orthogonal* combination, which AeST simply
does not contain as a separate mode — the singularity is convincingly an
artifact of analyzing a truncation (aether alone) that removes the field
the design added.

**What I have not independently verified, stated plainly**: (i) that the
metric's own $g_{0i}$ enters *inside* the same $U_i$ combination rather
than as a genuinely separate channel — plausible, consistent with how
covariant derivatives generally mix into such projectors, but not
re-derived here with the same rigor as the $\delta\phi$-$A^i$ piece;
(ii) the "invertibility anchor" — that SZ's Minkowski stability spectrum
being non-degenerate implies the *stationary, sourced* elliptic system
has unique solutions. This is a standard, physically reasonable type of
inference (a non-degenerate kinetic operator's static Green's function is
generically well-posed) but is a bridging argument, not a theorem quoted
verbatim from the stability paper — I'd call it credible, not proven.

**Accepted conclusion, with that distinction kept**: the fork resolves in
the pre-registered direction — $\alpha_1,\alpha_2$ exist and are finite —
on solid ground for the *mechanism* (independently reproduced) and
reasonable-but-not-fully-certified ground for *rigorous finiteness*. The
actual **values** remain underived, exactly as the advisory itself states
("the fork is resolved; the derivation is not skipped") — the
order-by-order bookkeeping (unit-constraint elimination, second-class
sector, convective terms) is still the real, substantial work ahead, now
with a much better-motivated starting point than before this round.

**Housekeeping note**: the advisory flags the consolidation/errata batch
as requested across three consecutive rounds and asks that it be
delivered before the staged derivation continues. Noting this as a real,
accumulating item — not yet delivered, and worth prioritizing explicitly
with the author before pushing further into new derivation work.

*(Housekeeping delivered 2026-07-18 — see
`ConsolidationLog-2026-07-12.md` Items 11–15 and the new
`ErrataAndMethodologyLog-2026-07-18.md`. Resuming the staged derivation
below.)*

## 5d. Continuing the staged derivation: the aether's vector (spin-1) sector is independently healthy — and a genuine scope correction

Before attempting the coupled O(1.5) solve, checked whether AeST's
Maxwell-only kinetic term causes trouble in the aether's *other*
sector — the transverse (spin-1, "gravito-magnetic") vector mode, which
is structurally separate from the spin-0 mode §5b/§5c dealt with (the
transverse part of $A^i$ doesn't couple to $\phi$ at all: only $A^i$'s
longitudinal/curl-free part enters $\mathcal Y$'s cross term, since
$\int A^i\partial_i\delta\phi\,d^3x=-\int(\nabla\cdot A)\delta\phi\,d^3x$
picks out only $\nabla\cdot A$).

**Fetched Foster-Jacobson's vector-mode formulas directly** (their Eq.
15/17): speed$^2=(c_1-\frac12c_1^2+\frac12c_3^2)/[c_{14}(1-c_{13})]$,
energy $\propto(2c_1-c_1^2+c_3^2)/(1-c_{13})$. **The first fetch claimed
this becomes singular at $c_{13}=0$** — checked this myself symbolically
before accepting it, and it's **wrong**: at AeST's exact point ($c_3=
-c_1,c_4=0$), speed$^2=1$ exactly (light speed — consistent with the
tensor sector's own $c_{13}=0$ result) and the energy $\propto2c_1$,
finite and positive for $c_1>0$. **AeST's vector/spin-1 aether mode is
completely healthy at the theory's own kinetic point** — only the
spin-0 mode was degenerate, exactly the sector $\phi$ was built to
replace. Caught a wrong claim from a fetch before it entered the record —
the discipline paying off again, in the same round it mattered.

**Genuine scope correction, found while checking this**: Foster-Jacobson's
$\alpha_1$ formula shares its exact denominator polynomial ($2c_1-c_1^2+
c_3^2$) with the vector-mode's own energy-density expression — confirmed
symbolically, not by inspection. **This means $\alpha_1$ is not a
separable "spin-0 piece"; it is built from a derivation that couples
both the spin-0 and spin-1 aether sectors together.** Consequently,
AeST's regularized spin-0 sector ($U_i$, healthy via $\phi$) and healthy
spin-1 sector (confirmed above) **cannot simply be substituted into
Foster-Jacobson's existing formula piece-by-piece** — the formula itself
was derived for vanilla aether's specific coupled field content. Getting
AeST's actual $\alpha_1,\alpha_2$ requires redoing the coupled
derivation with AeST's field content from the covariant action, not
patching the existing result.

**Honest assessment of what this means for the timeline**: this is now
confirmed to be a full, from-scratch PPN derivation of the scale Foster-
Jacobson's own paper required — expand the covariant action (SZ Eq. 1)
to the necessary order with a moving source, solve the coupled
$(U_i,\,g_{0i})$ system together with the now-separately-confirmed-
healthy vector sector, and match to the PPN metric. This is genuine,
substantial, original theoretical work — not something a few more
symbolic spot-checks can responsibly complete. **Two real, verified
findings came out of this attempt** (the vector sector's health; the
non-separability of $\alpha_1$), which meaningfully sharpen the problem,
but the numerical value itself is further out than the pre-registration
assumed. Recommending this be explicitly staged across further dedicated
rounds — analogous to WP3's multi-round action-closure effort — rather
than pushed to a number this pass.

## New sub-task, opened 2026-07-19 — External Field Effect / Solar-System quadrupole $Q_2$: a serious, quantified tension, escalated

**Prompted by the user**, who supplied a specific, recently-published
(2026) citation and asked whether it had been included, then to open it
as a WP6 sub-task and check the fit: Park, Hees, Famaey, Desmond &
Durakovic 2026 (arXiv:2602.17884, archived: `references/arXiv.2602.17884/`
+ `.md` summary), an updated Cassini/DE440 bound on the Solar System
quadrupole $Q_2=(1.6\pm1.8)\times10^{-27}$ s$^{-2}$ ($1\sigma$), a 40%
improvement over the prior (Hees et al. 2014) estimate.

**Why this is a genuinely new test, not an update to sub-task 1**:
sub-task 1 (§4) tests a residual anomalous acceleration bound *far above*
$a_0$ (Saturn's own internal field), trivially passed by any sufficiently
screened large-gradient completion. **$Q_2$ is different in kind** — the
paper's own central point (attributed to a companion paper, "Desmond
Cassini") is that $Q_2$ depends *solely* on the interpolating function's
(IF's) shape at the **external** Milky Way field acting on the Sun,
$e_N\equiv a_e^N/a_0=O(1)$–$O(2)$ — squarely in the MOND-Newtonian
*transition* region, not the deep-Newtonian tail. **Sharpening the IF
above $a_0$ does not reduce $Q_2$.** This means $Q_2$ probes exactly the
same near-$a_0$ IF shape that any AQUAL/QUMOND-class theory — including
AeST's own quasistatic Y-sector, which cdot-8 inherits unchanged per
§2a's sector-additivity result — must use to fit galaxy rotation curves.
**The "screening at large gradients" argument that resolved sub-task 1
does not obviously apply here**, since WP6's own characterization of
AeST's screening mechanism (§4: "additional terms $\mathcal J\sim
\mathcal Y^p$, $p>3/2$, or Galileon-type terms that dominate at *large*
field gradients") is, by construction, subdominant near $a_0$ — the
near-$a_0$ shape is set by whatever reproduces galactic MOND
phenomenology, not by the large-gradient completion.

**Machinery validated against the paper's own published number before
trusting anything cdot-8-specific**: built `wp6_q2_efe_check.py`
(saved to `cdot-8/WP6/`), implementing the paper's own formulas exactly
($Q_2=-\frac{3a_0^{3/2}}{2\sqrt{GM_\odot}}q$, $q$ a double integral over
the IF; $e_N$ solving $\nu(e_N)e_N=a_e/a_0$, **not** $e_N=a_e/a_0$
directly — an initial naive attempt using the latter was caught and
corrected via this validation step). Reproducing the paper's own
$\delta=1$ RAR-IF case with their own $a_0=1.02\times10^{-10}$ m/s²:
$e_N=1.6433$ (paper quotes $1.643$), $Q_2=3.3869\times10^{-26}$ s$^{-2}$
(paper quotes $3.387\times10^{-26}$) — **matched to 4 significant
figures**.

**Applied to cdot-7's own established choices** (Foundation.md, checked
directly: the *Simple* interpolating function, $\kappa=1$, $\mu(x)=
x/(1+x)$, is explicitly stated as *preferred* over the standard one at
every fit stage quoted, $\Delta\chi^2\approx13$ at the four-term fit —
this is not the "naked simple used only for cosmological-fitting
convenience" framing from §4; Foundation.md states this is the
program's actual best-fit choice for the galaxy-scale RAR too):
$$a_0=1.39\times10^{-10}\text{ m/s}^2\ (\text{four-term fit}),\quad
e_N=1.0437,\quad Q_2\approx3.71\times10^{-26}\text{ s}^{-2}.$$
**This is $\sim23\times$ the new bound's central value, $\sim21\sigma$ in
naive tension.** Checked whether switching families helps (it doesn't,
materially): using cdot-7's own RAR-alone-preferred $a_0\approx1.26
\times10^{-10}$ m/s² with the $\delta=1$ RAR IF gives $Q_2\approx3.72
\times10^{-26}$ s$^{-2}$ — essentially the *same* tension ($\sim23\times$,
$\sim21\sigma$), confirming this is not a quirk of one specific IF family
but a generic feature of any shallow-transition ($\delta,\gamma,n\sim1$)
IF calibrated near $a_0\sim1.3\times10^{-10}$ m/s² — matching the paper's
own broader claim (3–15$\sigma$ tension across multiple SPARC mass
models and IF families).

**What this does and does not establish**: this is a real, quantified
tension between cdot-7's own established, best-fit interpolating-
function/$a_0$ choice and a recent, carefully-validated Solar-System
measurement — computed with a machinery independently checked against
the paper's own published number, not asserted. **It does not, by
itself, establish anything about AeST's or cdot-8's own *specific*
near-$a_0$ completion**, since that has never been derived from cdot-8's
own first principles (the same gap §4 already flagged: "the literature
gives the mechanism class but no unique functional form... pinning that
down would mean choosing a specific ansatz not yet derived"). If AeST's
quasistatic sector's near-$a_0$ shape is forced, by its own galaxy-fit
requirements, to closely resemble the Simple/RAR shape tested here (a
reasonable expectation, since that shape is precisely what reproduces
rotation curves), the tension likely transfers; if some structural
feature of AeST's own completion suppresses $Q_2$ specifically without
spoiling the galaxy fit, it might not — **this has not been checked and
would require deriving AeST's own quasistatic near-$a_0$ IF explicitly**,
not assumed either way.

**Not declared a kill, escalated per standing discipline.** This bears
directly on cdot-7's own established fit (the Simple IF, $a_0=1.39\times
10^{-10}$ m/s², is cdot-7's headline four-term-fit result, inherited by
cdot-8 unchanged) — **routed to `ConsolidationLog-2026-07-12.md` as a
candidate cdot-7-relevant finding**, per this program's standing
convention (cdot-7 itself untouched; findings routed through the
consolidation log for the author's own review). For cdot-8 specifically:
flagged as a new, open WP6 item, status **not resolved**, recommending
(1) deriving AeST's own quasistatic near-$a_0$ completion explicitly
before concluding whether it inherits this tension, and (2) author/
advisor review given the severity ($\sim20\sigma$-class, not a marginal
effect). Nothing in `cdot-7/` was touched — this section, the
`ConsolidationLog` entry, and `wp6_q2_efe_check.py` are the complete
record of this round.
