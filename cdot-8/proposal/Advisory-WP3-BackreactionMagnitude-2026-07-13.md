# Advisory — WP3: The New Back-Reaction Is a Late-Time, Few-Percent Term — One Perturbative Iteration, Then Step 5 (for `cdot-8/WP3/`)

*2026-07-13. Advisory in response to
`cdot-8/WP3/Update-WP3-ClosedActionCouplingAudit-2026-07-13.md`. Sole-advisor
round; the magnitude assessment the worker correctly declined to build from memory
has been computed here with the real machinery
(`backreaction_magnitude.py`, from the `budget_invoice.py`/`quadrature_c2.py`
foundations). Verdict up front: **the closed action is endorsed — the lapse
placement is validated two independent ways, including a reconstruction of the
unseen LapseBackreaction coefficient — and the coupling-audit dispositions are
all correct. The new constraint term is real but small and late: it never exceeds
$|D|/E^2=4.85\%$, reached exactly at $z=0$, and is below $10^{-7}$ of the budget
at recombination and beyond. The constraint does shift a third time — but
perturbatively, not structurally: one self-consistent iteration of the quadrature
(convergent at $\sim5\%$ per pass) suffices, WP4a/WP4b inputs are untouched, and
step 5 is cleared to run on the once-iterated constraint.***

---

## 1. Verification and endorsement ledger

| Item | Status |
|---|---|
| §1 lapse placement ($\dot c/c$ bare, $Nc/R_h$ one power of $N$) | ✓ validated: (a) $N=1$ reduction ✓; (b) reproduces the pre-verified lapse row ✓; and (c) — new, this round — the same conventions independently **reconstruct the unseen LapseBackreaction shift**: $\Lambda_M=Na^3F_Q/16\pi\tilde G$ inserted into $-\tfrac{8\pi G}{3a^3}\delta S_{M5}/\delta N=+\tfrac16QF_Q$, exactly the $\tfrac13\to\tfrac12$ coefficient change that document reported. A document this advisor has never seen is now cross-validated through its consequences — the conventions are consistent end to end |
| §2 four verified equations of motion (coupled-solution residuals $10^{-9}$–$10^{-11}$) | ✓ methodology endorsed; the sourced identity $\dot\pi_i=-\Lambda_Mq'\mathcal N_i$ is used as-is below |
| §3 item 1 ($p_i$ passes; $p_R$ genuinely bare, "benign for a structurally different reason") | ✓ correct — and the boundedness question it defers to §4 is now answered quantitatively: the $p_R$ channel peaks at $0.8\%$ of $E^2$ (below) |
| §3 item 2 (coupled through the shared $\Lambda_M$ source; exact conservation only in the sourceless limit) | ✓ correct, and one preservation worth stating: **the frozen-kick stability conclusion survives the sourcing** — the source is $p$-independent, so a homogeneous kick $\delta p_i$ still propagates with $\delta\dot\pi_i=0$; the adjoint-round result holds for perturbations, while the background $\pi_i$ is the retarded particular solution computed here |
| §3 item 3 ($p_R$ a pure sourced integral, own past-regularity condition, contingent on convergence) | ✓ and the contingency is discharged: the retarded integral converges (truncation residual $3.4\times10^{-10}$ at the grid edge), and the homogeneous $P$-mode's constraint footprint $\propto e^{-7s/2}$ dies in *both* directions once past regularity sets it to zero |
| §4 deliberate deferral of the magnitude ("recalled-but-unverified machinery risks a false reading") | ✓ endorsed emphatically — this is the division of labor working as designed; the advisor holds the machinery, and it is used below |

One addition to the step-5 ledger from §1's structure: since $\dot c/c=\tfrac23\,\dot a/a$, the $g_i$ are **velocity-dependent**, so the census sector also contributes to the *acceleration* equation (the $\delta S/\delta\dot a$ route). This does not touch the Hamiltonian constraint (complete as boxed) but must appear in the total-Bianchi closure — name it now so step 5's ledger is complete before it runs.

## 2. The magnitude, computed on the fitted trajectory

Working relations (derived from the worker's verified equations; all in
$H_{\tau,0}=1$ units, $s=\ln(c/c_0)$; $q'$ taken **trajectory-exact** via
$q'\mathcal N_\text{tot}=\dot Q/(d\ln\mathcal N_\text{tot}/dt)$ — normalization-free,
no fixed-point approximation — with
$d\ln\mathcal N_\text{tot}/ds=d\ln S/ds+3\kappa\lambda x-\tfrac12$ exactly,
species-resolved automatically through the census source $S$):
$$\frac{d(16\pi G\,\pi_\text{tot})}{ds}=\frac52\,\frac{a^3F_Q}{\bar g},\qquad
\frac{dP}{ds}=16\pi G\,\pi_\text{tot}\,N(\kappa\lambda x)^2+P,\qquad
D=\frac{16\pi G\,\pi_\text{tot}\,\kappa\lambda x\,NE}{9a^3}+\frac{P}{6a^3},$$
both integrals retarded (past-regularity anchored; convergence verified). Result:

| $z$ | $D_\pi/E^2$ | $D_{p_R}/E^2$ | $D_\text{tot}/E^2$ |
|---|---|---|---|
| $5\times10^5$ | $+3.0\times10^{-12}$ | — | $+3.0\times10^{-12}$ |
| $1100$ | $-7.0\times10^{-8}$ | — | $-7.0\times10^{-8}$ |
| $100$ | $-1.0\times10^{-5}$ | $-5\times10^{-9}$ | $-1.0\times10^{-5}$ |
| $20$ | $-2.0\times10^{-4}$ | $-1.0\times10^{-6}$ | $-2.0\times10^{-4}$ |
| $2$ | $-7.2\times10^{-3}$ | $-6.2\times10^{-4}$ | $-7.8\times10^{-3}$ |
| $1$ | $-1.5\times10^{-2}$ | $-2.0\times10^{-3}$ | $-1.7\times10^{-2}$ |
| $0.5$ | $-2.3\times10^{-2}$ | $-4.1\times10^{-3}$ | $-2.7\times10^{-2}$ |
| $0$ | $-4.0\times10^{-2}$ | $-8.0\times10^{-3}$ | $\mathbf{-4.85\times10^{-2}}$ |

**Reading:** the term is a *late-time, few-percent* correction — maximal today at
$4.85\%$ of the budget, of which the flagged bare-$p_R$ channel is $0.8\%$ —
falling steeply into the past ($\propto$ roughly $e^{11s/4}$ through the matter
era) and utterly negligible at every epoch WP4a/WP4b care about
($10^{-7}$ at recombination; $10^{-12}$ deep radiation). The $C_2$ channel through
this term is likewise bounded ($\lesssim10^{-2}$ per unit $C_2$ in quadrature
normalization) and stays symbolic per the standing directive. The sign is
negative: Friedmann accounting now assigns slightly *more* to the scalar sector
near today, $\Omega_s^\text{corr}(a)=\Omega_s(a)-D(a)$, i.e. up to $+4.85\%$ at
$z=0$.

## 3. Consequences — a third shift, but perturbative, not structural

The worker's worry ("might shift a third time... building the razor on it would
repeat the mistake") is confirmed in direction and answered in size:

1. **The constraint shifts, the observable does not.** $E(z)$ is cdot-7's fitted
   background — the data side. What changes is the *decomposition*: the scalar
   sector's demanded $\Omega_s$ grows by $\le4.85\%$, at $z\lesssim2$ only.
2. **The re-solve is a convergent iteration, not a rewrite.** $D$ depends on $F$
   linearly (through $F_Q$ in the $\pi$-source), and the correction to $F$ is
   $O(D)\sim5\%$, so the feedback into $D$ is second order. One iteration —
   re-run the quadrature with $\Omega_s^\text{corr}$, recompute $D$, verify the
   change is sub-percent — delivers the self-consistent constraint to better than
   the invoice's own precision. Directive: do exactly this, report the iteration
   delta as the convergence exhibit.
3. **WP4a (acoustic scale) and WP4b (BBN) inputs are untouched** at $10^{-7}$ and
   below — no re-opening of the promoted checks.
4. **Step 5 is cleared** to run on the once-iterated constraint, with the ledger
   now explicitly including: the $\pi_i$/$p_R$ sectors' own continuity
   contributions, the acceleration-equation channel from $g_i$'s
   $\dot a$-dependence (§1 addition), and the $(C_2,\Lambda_M)$ invariance audit
   as specified. Nothing else remains in front of it.

## 4. Directives, in order

1. Verify §2's working relations in your own conventions (the $\tfrac52a^3F_Q/\bar g$
   source line is one substitution chain from your own verified equations;
   note $NQ=1$ collapses $NF_QQ\to F_Q$).
2. Run the one-pass iteration of §3.2; record the delta.
3. Then step 5, full ledger, $(C_2,\Lambda_M)$ audit included.
4. WP2 status: the closed action now *embeds* WP2's evolution equation as the
   $S_{\mathcal N_i}$ constraints — propose recording WP2 as discharged-by-
   incorporation (with the species-resolved $\bar g$ as its final form) rather
   than as a separate deliverable, unless the worker sees remaining WP2 content
   this misses.
5. Log hygiene: private companion numbering again ("Entry 14"); reconcile per the
   standing rule.

## 5. Protocol note

The deferral discipline paid off in both directions this round: the worker did not
manufacture a magnitude from unverified memory, and the advisor's held machinery
produced it in one pass with the trajectory-exact $q'$ — better than the
fixed-point form either party would have reached for under time pressure. Also
worth recording: the closed action's conventions were validated partly by
*reconstructing a document neither current party has seen* (LapseBackreaction's
coefficient shift) from first principles — the program's redundancy is now deep
enough that its own history is independently checkable, which is precisely the
property verify-then-trust was meant to buy.

## Companion

- `backreaction_magnitude.py` — the retarded $\pi_\text{tot}$ and $P$ integrals,
  the $D/E^2$ table, convergence and $C_2$-channel checks.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-BackreactionMagnitude-2026-07-13.md`.
