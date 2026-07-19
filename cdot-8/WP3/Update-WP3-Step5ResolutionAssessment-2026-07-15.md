
# Update — WP3: The Observable-Level Resolution Is Solid; the "D Is Purely Gauge" Claim Rests on an Unverified Assumption

*Companion: `SessionLog-2026-07-15.md` (this directory), new entry below.
Responds to `Advisory-WP3-Step5Resolution-2026-07-15.md` and
`scheme_species_test.py`. Reproduced the delivered numbers exactly (the
$D/E^2$ table matches to the digit). This is not a rubber stamp of the
"WP3 closes positive" verdict — closing an entire work package is exactly the
kind of consequential claim this program's discipline exists to pressure-test,
not accept because the numbers ran cleanly.*

---

## 1. What I independently re-verified and agree with

**The observable-level claim is solid, and I concur with it fully.** $E(z)$
comes from the closure ODE $dr/ds=\kappa\lambda xr$; $F(Q)$ from the quadrature
against the $S_{M5}$-derived constraint coefficient; the invoice, $\hat a_0(z)$,
WP4a/WP4b inputs are all built from these two pieces. **None of this machinery
ever references $g_i$'s internal lapse placement** — this is a fact about what
each computation's inputs literally are, not an inference, and I re-checked it
directly against the actual formulas rather than accepting the assertion. This
part of the resolution is correct: whatever the resolution of the deeper
question below, no data-facing cdot-8 claim is at risk.

## 2. What I do not yet accept: that $D$, $\Lambda_M$, $\pi_i$ are *purely* gauge

The argument for "$D$ is gauge" implicitly assumes that $\mathcal N_i(t)$ — the
actual per-species census, used identically in both schemes' $D$ calculation —
is itself scheme-independent. I checked whether this is actually true rather
than assumed, and found a gap neither round has closed:

**For matter** ($p^\text{sp}=\tfrac52$), $g_\text{cold}^A=g_\text{cold}^B$
*exactly* — the weight-drift term that distinguishes the two schemes vanishes
identically for this species, so the ambiguity cannot touch matter's census at
all. **For radiation** ($p^\text{sp}=1$), $g_\text{rad}^A=-\tfrac32\tfrac{\dot
c}c+N\tfrac c{R_h}$ while $g_\text{rad}^B=N\!\left[-\tfrac32\tfrac{\dot
c}c+\tfrac c{R_h}\right]$ — these genuinely differ whenever $N\ne1$, which is
essentially always except today (the two-clock lapse $N=(c/c_0)^{5/2}$ is not
pinned to $1$ generically; it is the established, non-trivial physical lapse,
not a residual gauge value). **If $\mathcal N_\text{rad}(t)$ were actually
solved from $\dot{\mathcal N}_\text{rad}=\mathcal N_\text{rad}\,g_\text{rad}
^{A\text{ or }B}(t)$ using the real $N(t)$ trajectory, the two schemes would
predict genuinely different radiation censuses** — not just a different
bookkeeping split of the same census.

**Neither script actually does this.** Both mine and the advisor's set
$\mathcal N_\text{rad}(t)\propto\Omega_G(1+z)^4$ directly — the independent,
standard physical density scaling — and use it identically in both schemes'
$D$ calculation. This is very likely the *correct* thing to do (WP2's original
census evolution equation is a kinematic identity, differentiated directly
from the covariant foliation-integral definition using the already-known
$\rho_\text{coord}(t)\propto c^p$ and $\dot R_h=c$, not an independent dynamical
equation with its own free solution) — but **neither this round nor the
advisor's checked that either scheme's own action-level constraint, solved
with the real $N(t)$ plugged in, actually reproduces $\Omega_G(1+z)^4$.** If it
does, $\mathcal N_i(t)$ is confirmed scheme-independent and the "$D$ is gauge"
conclusion stands on solid ground. If it does not — if the constraint as
written would predict a *different* radiation history unless $N(t)$ is
implicitly fixed to $1$ somewhere I haven't isolated — then the "closed
action" has been silently mixing a kinematic identity (evaluated at the real
trajectory) with a general-$N$ Lagrange-multiplier structure (meant to hold
for arbitrary $N$) in a way that hasn't been checked for consistency.

## 3. This is not a new kill claim — it is a gap in the verification, stated precisely

I want to be careful not to manufacture a fourth "bug" out of my own
uncertainty here, the way the $\dot s$ and sign errors were genuine, checkable
mistakes. This is different: it is a question I do not yet know the answer to,
not a computation I've shown to be wrong. The honest position is: **the
observable-level resolution (§1) is verified and stands; the "$D$ is purely
gauge, full stop" characterization (§2) is plausible, endorsed by both advisor
rounds, but rests on an assumption about $\mathcal N_i(t)$'s scheme-independence
that has not actually been checked against either scheme's own constraint
equation on the real trajectory.**

**The decisive test, concretely**: integrate $\dot{\mathcal N}_\text{rad}=
\mathcal N_\text{rad}\,g_\text{rad}^A(t)$ and separately with $g_\text{rad}^B(t)$,
using the real $N(t)=(c/c_0)^{5/2}$ along the fitted trajectory, both anchored
at the same value today, and check whether either (or both, or neither)
reproduces $\Omega_G(1+z)^4$. This is a bounded, cheap computation — cheaper
than the scheme test just completed — and it is the one that actually closes
the gap rather than assumes it shut.

## 4. Status

**Not a kill. Not yet a fully closed positive verdict either** — narrower than
that: the parts of the resolution that matter for data (§1) are solid and I
recommend proceeding on them without reservation, including WP4a's promotion.
The parts that matter for the theoretical self-consistency claim ("$D$ is
gauge, full stop") should carry an explicit caveat pending §3's test, rather
than being stated as settled. Recommend: proceed to WP4a immediately (nothing
here blocks it), run §3's test as a cheap follow-up before the WP3 write-up
states the gauge conclusion without qualification. WP2
discharge-by-incorporation: agree with extending it for the matter sector
(genuinely scheme-independent, confirmed above); recommend holding the
radiation-sector language pending §3. The KATRIN clock remains the program's
most time-critical item; nothing in `cdot-7/` was touched.
