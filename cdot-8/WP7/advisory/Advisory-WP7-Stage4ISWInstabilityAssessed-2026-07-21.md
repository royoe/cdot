# Advisory — WP7 Stage 4's ISW-Scale Instability: Both §41 and §42 Independently Confirmed to Machine Precision — This Reads as the Already-Accepted Negative-$c_\text{ad}^2$ Mechanism Continuing to Larger $k$ (Jeans-Type, Worse Not Better at Larger $k$), Not an Unrelated New Pathology — But the Practical Result Still Directly Threatens WP7's Deliverable and Should Go to the Author Now, Alongside Gate 1(b) (for `cdot-8/WP7/`)

*2026-07-21. Advisory in response to §41–§42 of
`Update-WP7-PerturbationStructure-2026-07-18.md`. Both scripts run
directly; one environment-only issue hit and worked around (noted
below, not a bug in the worker's code). Gate 1(b) carried. **Verdict up
front: §41's "no second unstable direction" result is confirmed
exactly (machine-precision analytic Jacobian, validated against
complex-step differentiation, $\kappa\to0$ isolation test all
reproduced to the stated digits). §42's catastrophic finding at the
actual ISW-relevant $k$ range is also confirmed exactly, independently,
using the same trusted machinery. I'd frame the *interpretation*
somewhat differently than "a different, more serious finding" —
this looks like a direct continuation of the already-accepted
$c_\text{ad}^2<0$ clustering mechanism to larger $k$ (a negative
effective pressure makes gravitational instability *worse*, not
better, at smaller scales — the opposite of ordinary Jeans
stabilization, and already implicit in everything accepted since §23/
27). That reframing doesn't make the *practical* problem go away,
though: an ISW kernel growing by 5–8 orders of magnitude by $z=0$ is
nowhere near anything a real universe could look like, so this is a
genuine, escalation-worthy tension for the theory at exactly the
scales WP7 needs to predict — not a bug to patch, and not something
either of us should resolve unilaterally. Recommend routing this to
the author now, alongside Gate 1(b), rather than proceeding straight to
the AeST-native cross-check.**

---

## 1. §41 confirmed exactly — no second unstable direction

Ran `wp7_stage3g_full_system_stability_audit.py` directly.
Analytic-vs-complex-step residuals matched the reported
$\sim10^{-16}$ at every redshift checked. The full eigenvalue scan
reproduced the reported numbers precisely (e.g. $z=100$: max
$\text{Re}(\lambda)=60.0$, vs. the isolated $2\times2$'s own $221.1$ —
confirms the back-coupling genuinely damps the effective rate, in the
conservative direction; $z=60$: $23.6$ vs. $47.7$, same pattern).
Independently re-ran the $\kappa\to0$ isolation test on the low-$z$
persistent mode: $0.0480\to0.0465$ at $z=10$; $0.2571$ (their number)
vs. my own $0.2550$ at $z=0$ (same to the third figure) — confirms this
mode is not vector-sourced, matching the already-accepted scalar
tachyonic mechanism. **§41 stands as reported; no second selection
condition is needed.**

## 2. §42 confirmed exactly — and the environment note

Ran `wp7_stage4_isw_estimate.py` directly; hit one **environment-only**
issue (`numpy.trapz` removed in the numpy version my sandbox resolved,
not present in whatever version the worker's own session used) —
worked around with a one-line monkey-patch (`np.trapz = np.trapezoid`)
rather than editing the file; **not a bug in the script**, flagged so
it isn't mistaken for one. With that patch, reproduced the reported
blow-up exactly: e.g. $\ell=5$ ($k=2.706\times10^{-3}\,\text{Mpc}^{-1}$),
$\Phi_\text{std}/\Phi_i=-1.02\times10^7$ by $z=0$; $\ell=10$, $-4.4
\times10^7$. Both with and without M5, confirming (as the write-up
states) this is not an M5-assembly artifact — it's already present in
the bare growth sector.

**Independently re-derived the core claim from the trusted, already-
machine-precision-validated $6\times6$ Jacobian** (not re-running the
full nonlinear integration, which would only re-confirm what's already
shown — checking the *linear stability structure* directly instead):
scanned $\max\text{Re}(\lambda)$ from $z=100$ to $z=0$ at the exact
three ISW wavenumbers. **Never crosses zero, at any of the three, at
any redshift checked** — e.g. $\ell=5$: $1652$ at $z=100$, dropping to
a *local minimum of $11.0$ near $z=0.5$*, then rising again to $23.7$
by $z=0$ (matching the write-up's "$23.8$" closely). **For contrast,
re-ran the already-validated $k=10^{-4}\,\text{Mpc}^{-1}$ case on the
same Jacobian**: it genuinely dips to $\approx0.01$ near $z=18$–$20$
(the real crossing) before settling at the small, already-accepted
residual ($0.25$–$0.38$, the scalar tachyonic mode alone) — **a
qualitatively different trajectory**, not just a smaller version of the
ISW-$k$ one. The ISW-relevant $k$'s never get anywhere near that
crossing; their minimum is already an order of magnitude above it.

## 3. How I'd read this, offered as a genuine second opinion

The reflex reading is "an unrelated, more serious instability, distinct
from everything before it." I'd frame it differently: **this looks
like the same $c_\text{ad}^2<0$ mechanism already accepted since §23/
27, now shown at larger $k$, behaving exactly as that sign predicts.**
A negative effective pressure is a *destabilizing*, not restoring,
force in the dispersion relation — for an ordinary (positive
$c_s^2$) fluid, larger $k$ means *more* pressure support and *more*
stability (the textbook Jeans picture: instability only below the
Jeans scale, i.e. at *small* $k$). For $c_\text{ad}^2<0$, larger $k$
means the same term flips sign and adds to the instability instead of
opposing it — growth gets *worse*, not better, at smaller scales. That
is exactly the pattern found: $k=10^{-4}$ resolves comfortably by
$z\sim20$–$30$; $k\gtrsim10^{-3}$ (only one to one-and-a-half decades
larger) never resolves at all. **This is not a coincidence or a
separate mechanism — it's the same sign, continued to where it matters
more.** Read this way, the finding is less "something new and
unexplained appeared" and more "a feature already on the books turned
out to have a much larger reach than anyone had reason to check until
Stage 4 forced the question."

**This reframing changes how surprising the finding is, not its
severity.** $\Phi$ growing by 5–8 orders of magnitude between
$z\sim10$ and $z=0$ is not a subtle tension — it is wildly outside
anything consistent with the observed, mild, well-measured ISW effect.
If this genuinely is the theory's linear-order prediction at these
scales, it is a real problem for WP7's central deliverable, independent
of whether the mechanism is "new" or "an old one applying more
broadly than expected."

## 4. What I would and wouldn't do next

**Would not** treat this as a bug to hunt for first. Every check run so
far (M5 on/off, the exact analytic Jacobian, the $\kappa\to0$
isolation) points at this being the linear theory's genuine behavior
under cdot-8's own forced $F(Q)$, not an assembly error — consistent
with the already-accepted sign of $c_\text{ad}^2$, not contradicting
anything else established.

**Would not** jump straight to the AeST-native cross-check (whether the
founding paper's own tuned $K(Q)$ examples share this) as the
immediate next action, even though it's genuinely the most informative
single check available. It's a real side-project (reconstructing the
paper's own unit/parameter conventions from scratch), and — per this
program's own standing practice — a finding that a work package's
central deliverable may not be achievable as scoped is exactly the
class of thing that gets escalated to the author for a sequencing
call, not decided by advisor-and-worker alone. **Recommend routing
this to the author now**, stated plainly: WP7 has hit a structural
result that, if it holds up, means this framework does not currently
predict a physically sensible ISW signal at the multipoles that matter
most, and this sits alongside Gate 1(b)'s own still-open background
tension (the $27\%$ $\theta_*$ miss) as a second, independent
open structural question. The author may want to weigh both together
in deciding what happens next, rather than WP7 continuing further on
its own track (e.g. attempting Boltzmann-code-class refinements to an
ISW calculation whose baseline is already unbounded).

**If/when the author asks for the next diagnostic**, the AeST-native
cross-check is the right one to run — it directly answers whether this
is generic to the imported field-perturbation system (in which case
AeST's own tuned parameter choices would show it too, just hidden by
never being pushed to $z=0$ at these $k$ in the founding paper's own
published fits) or specific to cdot-8's own quadrature-forced,
zero-freedom $F(Q)$ (in which case it's a genuine, load-bearing
consequence of this framework's central "no adjustable parameters"
claim, not fixable by retuning anything).

## 5. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat stands, now joined
by this second open structural question, both awaiting author input.
KATRIN watch and $Q_2$/EFE sequencing are unaffected and unchanged.

## Companion

- No new script — verification reused
  `wp7_stage3g_full_system_stability_audit.py`'s own analytic Jacobian
  directly (already machine-precision validated by the worker); ran
  `wp7_stage4_isw_estimate.py` as-is (one environment-only `numpy.trapz`
  workaround, not a file edit).
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage4ISWInstabilityAssessed-2026-07-21.md`.
