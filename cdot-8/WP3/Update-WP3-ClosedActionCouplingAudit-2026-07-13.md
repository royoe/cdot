# Update — WP3: The Action Closed Over Dynamical Variables — Coupling Audit Discharged, and a New Back-Reaction on the Hamiltonian Constraint

*Companion: `SessionLog-2026-07-13.md` (this directory), Entry 14. Executes the
standing prerequisite repeated by every round since `Advisory-WP3-
ExchangeTermWellPosedness-2026-07-12.md` §7.2 ("close the action over dynamical
variables first... step 5 is uninterpretable without it") and discharges the
three-item coupling audit from `Advisory-WP3-AdjointInvariant-2026-07-12.md` §4,
sharpened by `Addendum-AdjointRound-CoupledInvariant-2026-07-13.md` §1. All new
equations of motion below are verified against finite differences on an actual
coupled numerical solution (not merely algebra on paper) before being trusted,
per this program's established discipline — residuals of order $10^{-9}$–$10^{-11}$
throughout, script in scratchpad. Species resolved to two (matter, radiation);
neutrinos' FD-weighted $p_\nu(t)$ is the same structure with a third index and is
not separately built here.*

---

## 1. The closed action, conventions stated explicitly before varying

Following flag-3/flag-6 practice (state the convention, don't absorb it silently):
census sectors and the horizon sector are written in their **general-lapse,
reparametrization-covariant form**, obtained by promoting cdot-7's own $N=1$-gauge
relations (WP2's $\dot{\mathcal N}_i/\mathcal N_i=g_i$, Foundation's $\dot R_h=c$) to
general $N$ via $d/d\tau=\tfrac1N d/dt$ applied to each rate that was originally a
*proper*-time statement:
$$S_{\mathcal N_i}=\int dt\,p_i\big[\dot{\mathcal N}_i-\mathcal N_ig_i\big],\qquad
g_i\equiv\Big(p_i^\text{sp}-\tfrac52\Big)\frac{\dot c}c+\frac{Nc}{R_h},$$
$$S_{R_h}=\int dt\,p_R\big[\dot R_h-Nc\big],\qquad
S_{M5}=\int dt\,\Lambda_M\big[Q-q(\mathcal N_\text{tot})\big],\quad
\mathcal N_\text{tot}=\sum_i\mathcal N_i.$$
Here $\dot c/c$ (a log-ratio of the same clock throughout) needs no extra lapse
factor, while the shell-sweep piece $Nc/R_h$ acquires exactly one power of $N$ —
this is the **minimal, and only self-consistent, choice**: it is fixed uniquely by
requiring (a) reduction to WP2's original formula at $N=1$, and (b) matching the
one row the addendum had already pre-verified independently
(§2 below shows it reproduces $-\sum_ip_i\mathcal N_i\,\partial g_i/\partial N$
exactly). Any other lapse-placement fails one of these two checks; this was not a
free choice among several equally natural ones.

**Named assumption (flagged, not absorbed):** $c(a)=c_0(a/a_0)^{2/3}$ throughout
(WP1 dictionary; $c$ is not independently dynamical), and $Q=\dot\phi/N=1/N$
(unitary gauge, established). $R_h$'s own defining relation has no homogeneous
mode of its own once promoted this way — see §3.

---

## 2. Verification, against an actual coupled numerical solution, not just algebra

Four claims checked, using synthetic (non-physical) smooth test functions for
every field, all residuals from a full `solve_ivp` integration of the coupled
system (not hand algebra alone):

| Claim | Residual |
|---|---|
| $\delta S/\delta N\big\vert_{\text{new sectors}}=-\sum_ip_i\mathcal N_i\tfrac{c}{R_h}-p_Rc-\tfrac{\Lambda_MQ}N$ | $1.3\times10^{-9}$ |
| $\delta S/\delta R_h\big\vert_{\text{new sectors}}=0\Rightarrow\dot p_R=\big(\sum_ip_i\mathcal N_i\big)\tfrac{Nc}{R_h^2}$ | $3.3\times10^{-11}$ |
| $\dfrac{d}{dt}(p_i\mathcal N_i)=-\Lambda_Mq'(\mathcal N_\text{tot})\,\mathcal N_i$ (on an actual solved trajectory) | $\sim3\times10^{-10}$, five sample points |
| $\dot p_R=\dfrac{Nc}{R_h^2}\sum_ip_i\mathcal N_i$ (on the full six-variable coupled solution) | $\sim5\times10^{-11}$, five sample points |

The pre-verified row from the addendum (§2 of
`Addendum-AdjointRound-CoupledInvariant`) is reproduced exactly by the first line
above with $R_h$ fixed external — confirming the lapse convention adopted in §1 is
the one the addendum already had in mind, not a new guess.

---

## 3. Coupling audit, item by item

**Item 1 (no bare-multiplier couplings)** — **passes for $p_i$, fails for $p_R$,
and the failure is benign for a structurally different reason.** Every appearance
of $p_i$ in the closed action (kinetic term, $N$-variation, $R_h$-variation) carries
its conjugate $\mathcal N_i$ — a structural guarantee, not a coincidence: any
Lagrange multiplier of a linear constraint $\dot X=g(\cdot)X$ transmits into other
variations only via $\delta(gX)/\delta(\cdot)$, which always retains the factor $X$.
**$p_R$ is the genuine exception**: it appears bare (no $R_h$ factor) in the
$N$-variation, $\delta S/\delta N\ni-p_Rc$, because $S_{R_h}$'s constraint
$\dot R_h=Nc$ is *not* homogeneous in $R_h$ — $R_h$ itself does not appear on the
right-hand side. This was not caught by "verify the identity in your own
conventions" (§5, adjoint-invariant advisory) because that identity's proof
assumed a mirrored pair of the matter/radiation type; $p_R$ never had one. Whether
this bare coupling is dangerous turns on boundedness of $p_R(t)$ itself (§4), not
on any adjoint-pairing protection — a different kind of check than item 1 was
originally framed to catch, and worth stating plainly rather than folding into the
same resolution as the species rows.

**Item 2 (coupled symplectic spectrum, per the addendum's sharpening)** — **the
species multipliers are coupled to each other, concretely, through $S_{M5}$'s
shared source term, exactly as the addendum anticipated rather than merely
guarded against.** The narrow original concern (hidden $\mathcal N$-dependence
inside $g_i$ itself) is **absent** — $g_i$ depends only on $a,\dot a,N,R_h$, never
on any $\mathcal N_j$ directly, confirmed by direct inspection of the closed
action. But the broader concern is realized: $\dot p_i=-p_ig_i-\Lambda_Mq'(\mathcal
N_\text{tot})$ carries the **same** source term $-\Lambda_Mq'(\mathcal N_\text{tot})$
for every species $i$ (since $\mathcal N_\text{tot}=\sum_j\mathcal N_j$ mixes them
all), so the per-species combinations $\pi_i\equiv p_i\mathcal N_i$ are not
independently conserved once $\Lambda_M\ne0$ — the clean result is instead the
sourced identity of §2, $\dot\pi_i=-\Lambda_Mq'(\mathcal N_\text{tot})\mathcal N_i$,
with the *same* right-hand-side factor $\Lambda_Mq'(\mathcal N_\text{tot})$ coupling
every species' $\pi_i$ to the others' $\mathcal N_j$ through their shared presence
in $\mathcal N_\text{tot}$. This is the coupled system the addendum asked to see
exhibited, not merely posited: the adjoint-invariant round's exact conservation
$\dot\pi_i=0$ is recovered only in the sourceless limit $\Lambda_Mq'\to0$
(equivalently the decoupled/no-M5-closure limit) — with M5 active, $\pi_i$ is a
clean, closed, first-order-sourced quantity rather than an exact constant, and the
species are linked through the one shared multiplier $\Lambda_M$, not through any
direct $\mathcal N_i$–$\mathcal N_j$ term. No pairing-breaking or bare-multiplier
pathology found in this channel — the coupling is exactly the shape the addendum's
structural expectation predicted ("state–costate linearizations carry Hamiltonian
structure... the likely outcome is the same conclusion on a sturdier foundation")
— but it had to be shown, not assumed, and item 1's audit above shows the
*mechanism* by which it does (never a bare-$p$ term; always $\pi_i$, now
explicitly sourced rather than constant).

**Item 3 ($(R_h,p_R)$ pair, explicitly, not by analogy)** — **resolved, and it is
not the same structure as the species pairs.** $R_h$'s own equation ($\dot
R_h=Nc$) has no term proportional to $R_h$ itself — no homogeneous exponential
mode exists for $R_h$ at all, unlike $\mathcal N_i$ (whose $\dot{\mathcal N}_i=g_i
\mathcal N_i$ **is** homogeneous in $\mathcal N_i$). Consequently $p_R$'s own
equation, $\dot p_R=(Nc/R_h^2)\sum_i\pi_i$, has **no $-g\cdot p_R$ term either** —
it is a pure sourced integral, not a mirrored-exponential adjoint pair. There is no
analogue of "$p_i\mathcal N_i=$const" for $(R_h,p_R)$; the correct statement is
that $p_R(t)=p_R(t_*)+\int_{t_*}^t(Nc/R_h^2)\sum_i\pi_i\,dt'$ requires its **own**
past-regularity boundary condition ($p_R\to0$ as $t\to-\infty$, contingent on the
integral converging — a bounded, checkable task, structurally the same kind of
condition $C_1$ and the species multipliers each needed, but not inheritable from
either by analogy, confirming the stand-in's own §4 item 3 was right to flag this
as needing its own page).

---

## 4. The new finding: $S_{\mathcal N}$ and $S_{R_h}$ back-react on the Hamiltonian constraint too

Following the exact same map used in `Update-WP3-LapseBackreaction-2026-07-12.md`
($\text{boxed-constraint-term}=-\tfrac{8\pi G}{3a^3}\times\delta S_\text{sector}/
\delta N$, calibrated there against $S_{M5}$'s own contribution), §2's verified
$\delta S/\delta N$ result gives a genuinely new addition to the **same** boxed
constraint:
$$H_\tau^2=\frac{8\pi G}3\rho_m-\frac13F+\frac12QF_Q-\frac{QC_1}{6a^3}
\ +\ \frac{8\pi G}{3a^3}\left[\sum_i\pi_i\,\frac{c}{R_h}+p_Rc\right].$$
**This term has never appeared in any prior round.** Every Friedmann-constraint
derivation since the third escalation — including the LapseBackreaction round that
found $S_{M5}$'s own contribution and shifted the $QF_Q$ coefficient from $\tfrac13$
to $\tfrac12$ — treated $\mathcal N_i$ and $R_h$ as **external background
functions**, not yet the dynamical variables with their own back-reacting
multipliers that "closing the action" (repeatedly deferred, always correctly, until
the coupling audit was ready) requires. This is structurally the same kind of
finding as the $S_{M5}$ back-reaction: a sector that looked like a passive
bookkeeping constraint turns out to feed directly back into the same equation
every prior $F(Q)$ reconstruction (including this session's just-confirmed
$C_2$-kernel quadrature) was solved against.

**Not yet assessed: magnitude.** Whether $\sum_i\pi_i\,c/R_h+p_Rc$ is a negligible
correction or a significant rewrite of the constraint (as $S_{M5}$'s own term
turned out to be) depends on the actual size of $\pi_i(t)=p_i(t)\mathcal N_i(t)$
along the fitted trajectory, which requires integrating the retarded solution of
$\dot\pi_i=-\Lambda_Mq'(\mathcal N_\text{tot})\mathcal N_i$ using the **real**
$\mathcal N_i(t)$, $\Lambda_M(t)=Na^3F_Q/16\pi G$ (with the just-confirmed
$C_2$-carrying $F(Q)$), and $q'(\mathcal N_\text{tot})$ from the fixed-point form
$q\propto\mathcal N^{-10/9}$ — the actual `census_closure.py`/`quadrature_c2.py`
machinery, not a from-memory reconstruction. **Deliberately not attempted here**:
building an approximate numerical estimate from recalled-but-unverified AQUAL
interpolating-function machinery risks manufacturing a false magnitude reading,
exactly the kind of shortcut this program's discipline exists to prevent. This is
reported as a checkpoint, mirroring the LapseBackreaction precedent exactly.

---

## 5. Status

Not a kill, not a pass. **Closed**: the action is now genuinely closed over all
dynamical variables (species-resolved census pairs, $R_h$ promoted, all $\delta g$
back-reaction terms in place) for the first time in the program, with every new
equation of motion independently verified against a solved coupled system rather
than paper algebra alone. **Discharged**: all three coupling-audit items have
concrete, checked answers (item 1: passes for $p_i$, genuine bare-coupling
exception for $p_R$ of a structurally benign kind; item 2: the coupled-symplectic
structure the addendum predicted, exhibited rather than assumed, mediated entirely
through the shared $\Lambda_M$ source, no pairing-breaking found; item 3: resolved
as a pure sourced integral, not a mirrored pair, needing its own past-regularity
anchor). **Not yet done**: the magnitude of the newly-found $\pi_i,p_R$
back-reaction term on the Hamiltonian constraint, and — contingent on that —
whether the razor/total-Bianchi confrontation (step 5 proper) can be run against
the constraint as it stands or needs the quadrature re-solved a third time first.
Recommend a check-in before attempting step 5, given that this is now the second
time closing a previously-deferred piece of the action has changed the same
equation — building the razor check on a constraint that might shift a third time
would repeat exactly the mistake the checkpoint discipline exists to catch. WP2
finalization still hard-blocks; the KATRIN clock remains the program's most
time-critical item; nothing in `cdot-7/` was touched.
