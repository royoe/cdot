# Update — WP3: Two Findings Behind the Retraction — a Missing Factor of 3 Since the First Closed-Action Round, and the Retraction's Own Test Target May Be Wrong Too

*Companion: `SessionLog-2026-07-13.md` (this directory), new entry below.
Responds to `Advisory-WP3-Step5Retraction-FrameTest-2026-07-15.md` and
`census_scheme_check.py`. Reproduced the delivered numbers exactly (the
orders-of-magnitude mismatch against $(1+z)^4$ is real, confirmed). Went one
step further per the advisory's own §4 assignment — compute $g_i$ unambiguously
from the covariant definition — and found something more basic than either
party's framing anticipated.*

---

## 1. Reproduced the retraction's numbers exactly

Ran `census_scheme_check.py`: scheme A saturates at $d\ln\mathcal
N_\text{rad}/ds=-2.25$, scheme B decays to zero, neither approaches the
advisory's target of $-6$ — matched to the digit. No arithmetic disagreement
with what was delivered.

## 2. But the target itself needs checking first — and it's not $(1+z)^4$

$\mathcal N_\text{rad}$ is not the same object as $\Omega_\text{rad}(z)=
\Omega_{G,0}(1+z)^4$. WP2's own definition (§1 of `Update-WP2-
CovariantCensus-2026-07-12.md`) is $\mathcal N\propto[\rho_{E,\text{coord}}/E_P]
\times R_h^3$ — a horizon-mass-over-Planck-mass count, not a density fraction.
Computed $\mathcal N_\text{rad}(s)$ **algebraically**, directly from this
definition on the actual fitted trajectory ($\rho_\text{coord}\propto c^{p}$,
$p=1$; $E_P\propto c^{5/2}$; $R_h=r(s)\times R_{h,0}$ from the already-solved
closure ODE — no $g_i$, no scheme, no ODE integration of the census sector at
all):
$$\frac{d\ln\mathcal N_\text{rad}}{ds}=-\frac32+3\frac{d\ln r}{ds}.$$
This is **positive and growing into the past** ($-0.06$ at $z=0$ rising to
$+2.99$ at $z=10^5$) — nowhere near $-6$, and not because anything is broken:
$\mathcal N_\text{rad}$ genuinely is not expected to dilute like $(1+z)^4$,
because it carries the $E_P^{-1}\propto c^{-5/2}$ normalization and the
$R_h^3$ horizon-growth factor on top of the raw density. **Comparing
$\mathcal N_\text{rad}$'s evolution to $(1+z)^4$ was comparing two different
physical quantities that were never supposed to agree.** This doesn't yet mean
the retraction's headline conclusion is wrong — but the specific number it
quoted as "the target" needs replacing before the test means what it's being
read to mean.

## 3. The actual bug: my closed-action $g_i$ is missing WP2's factor of 3

Checked the algebraic result above against WP2's own original evolution
equation, evaluated at $N=1$ with the correct shell-sweep coefficient:
$$\frac{d\ln\mathcal N_\text{rad}}{ds}\Big|_{N=1}=-\frac32+3\frac{d\ln
r}{ds}$$
**matches the algebraic definition to $7\times10^{-12}$ at every point
checked** — WP2's formula, taken at face value with its stated coefficient of
$3$, is exactly correct; no surprise there, since it was derived by direct
differentiation of the same definition.

**But `Update-WP3-ClosedActionCouplingAudit-2026-07-13.md`'s closed-action
$g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+Nc/R_h$ carries coefficient $1$ on the
shell-sweep term, not $3$.** This is not a scheme question (A vs. B) — it is a
plain arithmetic slip in transcribing WP2's own already-established formula
into the first closed-action document, three rounds of advisories and two of
my own updates ago, never caught because nobody checked $g_i$ against WP2's
original formula directly until now. Scheme A with the coefficient corrected
to $3$: $g_\text{rad}^{A,\text{fixed}}=-\tfrac32\dot c/c+\tfrac{3Nc}{R_h}$,
which reduces exactly to the verified algebraic result at $N=1$ (by
construction) — but away from $N=1$, still requires knowing whether *any*
lapse factor belongs on this term at all, which is the deeper question below.

## 4. The open question underneath both bugs: does the census/horizon sector need a lapse at all?

Both $R_h$'s defining relation ($\dot R_h=c$) and the census evolution
equation are, in their original WP2 form, stated **entirely in terms of the
coordinate time that already defines the foliation $\Sigma_t$** — no
reference to matter's proper time appears anywhere in their derivation
(unlike the matter stress-energy and the $\phi$/M5 sector, where $N$ enters
because those genuinely care about proper vs. coordinate time). This raises
the possibility that the entire "promote $g_i$ to general $N$" step from the
first closed-action round was an unnecessary addition — that the physically
correct census/horizon action terms carry **no $N$ at all**, matching WP2
verbatim, and that $\delta S_{\mathcal N}/\delta N=\delta S_{R_h}/\delta N=0$
identically. If so, $D\equiv0$ and the entire back-reaction/$C_2$-swing
question dissolves as an artifact of an unjustified modeling choice made
before either scheme A or B was ever written down.

**I have not resolved this and am not asserting it as the answer.** A quick
check of how $\dot c/c$ transforms under a general time-coordinate change
suggests $g_i$ *does* need to scale as a density under reparametrization for
the action to be well-posed for arbitrary $N$ — which would argue against the
"no $N$ at all" resolution — but I am not confident in that check either,
given how many hand-derivation errors (mine and the advisor's) this specific
question has already produced this session. **This needs the actual
first-principles derivation the retraction assigned in its §4** — vary the
covariant foliation-integral definition directly under a general
reparametrization, not guess plausible completions of the already-simplified
formula and test them against each other or against the wrong target.

## 5. Status

Two concrete, verified findings this round: (1) the retraction's own test
target ($(1+z)^4$) is very likely the wrong comparison for $\mathcal
N_\text{rad}$, which is a different physical quantity by construction; (2) my
own closed-action $g_i$ has carried a missing factor of 3 since the very
first round, independent of the scheme A/B question. Neither finding by
itself resolves whether $D$ is gauge, zero, or physical — they mean the
retraction's specific numerical demonstration doesn't yet establish what it
claims to, in either direction. **Recommend**: before anything else, redo the
census/horizon sector's reparametrization-invariant completion directly from
the covariant definition (§4), with the factor of 3 restored throughout, and
check *that* result — not scheme A, not scheme B, not $(1+z)^4$ — against the
algebraic $\mathcal N_i(s)$ computed here. This is now a well-defined,
bounded calculation. WP4a promotion: agree with holding it, on different
grounds than the retraction's stated reasoning (not because $D$'s status is
unresolved as bookkeeping-gauge-or-physical, but because the underlying
$g_i$ formula every $D$ calculation has used is independently confirmed
wrong by a stronger check than the scheme test). WP2 discharge: hold, in
full, as directed. The KATRIN clock remains the program's most time-critical
item; nothing in `cdot-7/` was touched.
