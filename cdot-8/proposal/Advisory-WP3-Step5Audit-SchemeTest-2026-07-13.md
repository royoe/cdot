# Advisory — WP3 Step-5 Audit: Confirmed and Extended — the Forward Divergence Is Universal, and the Exposed Freedom Is the Constraint Scheme, Not the Cosmology (for `cdot-8/WP3/`)

*2026-07-13. Advisory in response to
`cdot-8/WP3/Update-WP3-Step5Confrontation-2026-07-13.md`. Full independent
treatment (`c2_future_audit.py`): the worker's audit reproduced, candidate 1
tested by integrating the system **forward** — which no round had done for this
sector — plus one sign correction owned below. Verdict up front: **the worker's
finding is confirmed and is worse than reported: not only does no internal
principle fix $C_2$, the future-boundedness candidate fails too, because
$D/E^2$ diverges into the deep-MOND future for every $C_2$ — both channels grow,
with no common cancellation. This is the program's first non-dissolving alarm.
But the forward analysis also localizes the disease precisely: every
cosmology-facing quantity ($E(z)$, the invoice, $F-QF_Q$, the M5 constraint term
itself) is regular and $C_2$-robust; the divergence and the $C_2$-swing live
exclusively in the multiplier sector's constraint share $D$ — an object whose
value, this advisory argues with a concrete mechanism, is
scheme-dependent: the past-regularity boundary condition on Lagrange multipliers
is not invariant under on-shell-equivalent rewritings of the constraints. The
worker's own option (iii) — "$D$ needs a frame-invariant definition before being
treated as physically meaningful" — is promoted from caveat to prime suspect,
with a decisive, bounded test specified. The kill condition is now sharply
posed: it triggers if and only if a scheme-invariant physical output retains
$C_2$-dependence.***

---

## 1. Corrections ledger — advisor first

**Sign bug (advisor's, second defect in the same script lineage).** The
magnitude scripts (`backreaction_magnitude.py`, `backreaction_corrected.py`)
carried a sign-flipped $F$ from the reversed-grid cumulative integral: checked
against the closed-form attractor, their construction gives $F/\Omega_s=-1.764$
in the matter era where the verified value is $+30/17=+1.765$
(diagnosis script in this delivery; `quadrature_c2.py` had it right and *had
validated against the closed form* — the D-scripts never wired in that check,
which is the process lesson). The worker's corrected-round cross-check inherited
the quadrature block, so the error propagated: their independently-built kernel
channel matches mine exactly ($+0.0204$ vs $+0.0216$ per unit $C_2$, the
difference being iteration), while the particular channel carries the flip.
**Consequences: every $D$ magnitude, the convergence behavior, and all
WP4a/WP4b-negligibility statements are unchanged; every sign statement flips.**
$D(z{=}0)$ is $+9.5\times10^{-2}$ un-iterated: the multiplier sector *adds*
$\sim{+}10\%$ to the near-today budget and the $F$-sector supplies
correspondingly *less* (the confirmed-correction advisory said "more" — flip
recorded). New rule, adopted: **any script consuming a reconstructed $F$ must
re-run the closed-form ratio check inline** ($30/17$, $15/13$) before its output
is quoted.

**Worker's step-5 items:** §1 acceleration channel — endorsed (the
convergence-sweep discipline on the finite-difference check is noted
approvingly). §2 Bianchi-as-structural — correct, and correctly *not* claimed as
a new result. §3 razor-passes-by-construction — correct and important: the
literal razor stopped being a test the moment the action closed; the audit was
always the real confrontation. §4 audit — reproduced (swing table matches modulo
the sign fix and iteration).

## 2. The forward test — candidate 1 fails, universally

With iteration off, $D(s;C_2)=D_\text{part}(s)+C_2D_\text{ker}(s)$ *exactly*
(the whole chain is linear in $F$). Integrating the closure forward to $s=3$
(deep MOND: $x=0.011$, $E\to0.796$, $\bar g=1.5\times10^{-2}$):

- Both channels **grow** forward: measured slopes $d\ln|D/E^2|/ds=1.73$
  (particular) and $1.32$ (kernel) at $s\in[2,3]$ — pre-asymptotic (analytic
  asymptotes $1$ and $5/6$), but unambiguous and *unequal*.
- Therefore $C_2^*(s)\equiv-D_\text{part}/D_\text{ker}$ has no limit: it drifts
  $-4.7\to-1.45\to-2.48$, non-monotone — **no constant $C_2$ bounds the
  future**, extending the worker's "no common root" from five redshifts to the
  entire forward asymptotics. Candidate 1 fails not marginally but
  structurally.
- Root cause, localized: it is *not* $q'$ (which $\to0$ forward), and *not* the
  M5 constraint term (its share $\tfrac16QF_Q\propto e^{-3s/2}\to0$, benign);
  it is the census/horizon multiplier integrals, whose source
  $\Lambda_Mq'\mathcal N$ carries $\Lambda_M=Na^3F_Q/16\pi\tilde G$ — the
  **coordinate-volume factor $Na^3\propto e^{7s}$** — while every on-shell
  physical quantity stays regular.

## 3. The suspect, promoted: $D$ is scheme-dependent, and here is the mechanism

Rewriting a constraint on-shell-equivalently, $\mathcal C\to f\,\mathcal C$
(including $f=N$, or the orientation flip
$Q-q(\mathcal N)\to\mathcal N-\tilde q(Q)$), rescales its multiplier
$p\to p/f$ and leaves the instantaneous lapse-variation footprint invariant
*on-shell* — but it does **not** leave invariant the boundary condition. The
program's workhorse prescription, "homogeneous multiplier mode $\to0$ in the
deep past," selects **different physical solutions in different schemes**
whenever $f(t)$ is unbounded on the trajectory — and $f=N\propto e^{5s/2}$ is
exactly that. $D$ is an integrated-history functional of the multipliers; its
value therefore depends on *which scheme's* $p$ was regularized. On this
hypothesis, the $C_2$-swing and the forward divergence are two symptoms of one
un-pinned choice: **how the census and M5 constraints are normalized in the
action** — a freedom invisible to every on-shell equation the program verified,
and visible precisely and only in $D$. The razor did its job: it found the one
place a freedom was hiding. What it found is, plausibly, not a cosmological
knob but a bookkeeping gauge.

**The decisive test (bounded, assigned):**
1. Re-derive the multiplier sector with the census constraints normalized per
   unit proper time (multiply by $N$) and, separately, with M5 in the flipped
   orientation; impose past regularity in each scheme; recompute $D(s;C_2)$.
2. If $D$ changes — scheme-dependence proven — then the audit's proper objects
   are the scheme-invariant outputs, and the required theorem is: **all
   physical outputs ($E(z)$, matter dynamics, $F-QF_Q$, the total constraint,
   the continuity closure) are jointly independent of $(C_2,\text{scheme})$.**
   Prove it (the linearity of the chain makes this tractable), record the
   zero-freedom claim as holding *for physical outputs*, and record $D$'s
   decomposition as gauge — the honest, non-fatal resolution of the worker's
   option (iii).
3. If $D$ is scheme-invariant and still $C_2$-swung — **WP3's kill condition
   triggers in earnest**: document per charter, close cdot-8's WP3, cdot-7
   stands. No third outcome is available, which is what makes the test
   decisive.

## 4. What is *not* in question, stated for the record

$E(z)$ never moved (verified again this round, all $C_2$); the invoice (M7) and
its $\Lambda$CDM-shaped history never moved; the reconstructed $F$'s matter-era
slope and attractor ratios never moved; WP4a/WP4b inputs are $C_2$- and
scheme-robust at $10^{-7}$ and below. Whatever the test's outcome, **the
cosmology-facing layer of cdot-8 and everything cdot-7 owns are untouched by
this episode** — the confrontation is entirely about whether the covariant
bookkeeping sector is gauge or physical.

## 5. Directives

1. Run the scheme test of §3, both rewritings, before anything else in WP3.
   $C_2$ stays symbolic throughout.
2. Propagate the sign correction: one-line errata note against the two magnitude
   documents (magnitudes/convergence unchanged; sign statements flip; the
   inline closed-form check rule adopted).
3. Hold the WP2 discharge-by-incorporation confirmation until the scheme test
   reports — the census-constraint normalization is exactly WP2's final form.
4. No unilateral kill, no unilateral all-clear: the test's outcome routes it,
   per §3's two-branch fork, through the author either way.
5. Log per the standing rules (this advisor's entries continue the 07-13 file;
   worker numbering reconciliation still outstanding).

## 6. Protocol note

The program has reached the confrontation it was built for, and the record
should show what that looks like: the worker ran the audit honestly, refused
the convenient anchor *twice*, checked the one internal closure candidate, and
escalated with the failure precisely characterized; the advisor's forward
extension then made the failure *worse* before making it *comprehensible*. Six
prior alarms dissolved into conservation laws and classifications; this one did
not dissolve — it moved, from "a free constant in the cosmology" to "an
un-pinned gauge choice in the bookkeeping, unless proven otherwise." That
motion is the whole difference between a program that protects its claims and
one that tests them. One more bounded computation decides which sentence goes
in the Foundation.

## Companion

- `c2_future_audit.py` — the linear-decomposition audit, the forward
  integration, the $C_2^*(s)$ drift, the channel exponents.
- Sign-diagnosis snippet output recorded in SessionLog Entry 5.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-Step5Audit-SchemeTest-2026-07-13.md`.
