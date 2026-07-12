# Update — WP3: The Inverse Reconstruction, and a Sharp Shape Mismatch

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 4. Executes directive 1
of `cdot-8/proposal/Advisory-WP3-BudgetInvoice-2026-07-12.md`: "inverse-function
reconstruction... your job... since a failed reconstruction moots the algebra." Before
using it, `budget_invoice.py`'s core formula was independently re-derived (not merely
re-run) from the two-clock dictionary and the closure ODE — confirmed exactly. The
reconstruction below then surfaces a specific, checkable tension. Escalating again, per
the established protocol: independently verified, no unilateral kill call.*

---

## 1. Independent re-derivation of `budget_invoice.py`'s $E(s)$ formula

From $H_\tau=H_t(c/c_0)^{-5/2}$ (WP1 addendum) and $H_t=\tfrac32\dot c/c$, using the
closure ODE ($\dot R_h=c$, $dr/ds=\kappa\lambda x r$, $s=\ln(c/c_0)$) to eliminate
$\dot c/c$ in terms of $r,x,s$: $H_\tau=\tfrac32(c_0/R_{h,0})e^{-3s/2}/(\kappa\lambda xr)$,
giving, at $s=0$: $H_{\tau,0}=\tfrac32(c_0/R_{h,0})/(\kappa\lambda x_0)$, hence
$$E(s)\equiv\frac{H_\tau}{H_{\tau,0}}=e^{-3s/2}\frac{x_0}{x(s)r(s)}$$
— matching the advisory's formula exactly, derived independently rather than accepted.
Fixed-point limits ($x=x_*$ const, $r\propto e^{\kappa\lambda x_*s}$, using
$\kappa\lambda x_*=3/4$ for matter): $E\propto e^{-(3/2+3/4)s}=a^{-3/2}$ — confirmed.

---

## 2. The reconstruction condition

$F_Q(a)=\xi a^{-3}$ (exact, model-independent) and Friedmann accounting $F(a)-Q(a)F_Q
(a)=-3H_0^2\Omega_s(a)$ must hold *simultaneously* for the same $F$. Differentiating the
second and requiring consistency with the first (i.e., that $F$, reconstructed along the
trajectory, is a genuine function of $Q$ and not merely of $a$) — the $\xi a^{-3}dQ/da$
terms cancel exactly, leaving
$$\boxed{\ \xi\,Q(a)=-H_0^2\,a^4\,\Omega_s'(a)\ }$$
**$Q(a)$'s shape is not free — it is fully fixed by the invoice curve's own shape**,
up to the one constant $\xi$. Validated against a synthetic test case before trusting
it on real data: constructed an arbitrary power-law $Q(a)=a^2$, $F(Q)=Q^{-1/2}$ (chosen
so $F_Q\propto a^{-3}$ by construction), forward-computed $\Omega_s(a)$, then applied
the boxed formula — recovered the *original* $Q(a)$ to $9\times10^{-7}$ relative error.

---

## 3. The test: does this forced $Q(a)$ match the independently-fit MOND scale?

$Q$ is not free to fit the cosmological sector alone — M2 identifies it with the same
scalar whose cosmological value sets the galactic MOND acceleration, already fit against
real RAR/lensing data (Foundation §5.5's $\hat a_0(z)$ evolution: $1.69,\,2.35,\,2.57,\,
3.30$ at $z=0.33,\,0.85,\,1.00,\,1.44$, relative to today). Computed $Q_\text{forced}(a)$
from the boxed formula along the actual fitted trajectory (same `budget_invoice.py`
machinery, independently re-run):

| $z$ | $\hat a_0(z)/\hat a_0(0)$ (fitted, Foundation §5.5) | $Q_\text{forced}(z)/Q_\text{forced}(0)$ |
|---|---|---|
| 0.33 | 1.690 | 0.948 |
| 0.85 | 2.350 | 0.911 |
| 1.00 | 2.570 | 0.906 |
| 1.44 | 3.300 | 0.895 |
| (2, 5, 10, 20, for shape) | (5.20, 14.70, 36.48, 96.23 — fixed-point $(1+z)^{3/2}$) | (0.888, 0.877, 0.871, 0.861) |

**$\hat a_0(z)$ grows by a factor of $\sim2$ by $z=1$ and continues growing steeply;
$Q_\text{forced}$ is nearly flat (varies by $<15\%$ out to $z=20$) — the two shapes
diverge sharply, not marginally.** The invoice curve's own internal consistency (exact
$F_Q\propto a^{-3}$, plus Friedmann accounting of the already-fitted expansion history)
determines what $Q(a)$'s shape *must* be — independent of any assumption about how $Q$
maps to $\hat a_0$ — and that shape does not track the independently-fit galactic MOND
evolution under the simplest, most natural reading of M2 ($\hat a_0\propto Q$).

---

## 4. What would rescue this, and why it's a narrow rescue

If $\hat a_0=g(\lambda_s,Q)$ for some function $g$ *other* than direct proportionality
(the proposal's own §3 wording — "$a_0$ is a parameter assembled from the free
function's normalization and the scalar's cosmological velocity" — leaves this open),
the mismatch could in principle be absorbed into $g$'s nonlinearity. Roughly: matching
a factor-of-$\sim2$ growth in $\hat a_0$ against a $<15\%$ growth in $Q_\text{forced}$
over the same range needs $g$ steep enough that $\hat a_0\propto Q^n$ with $n\gtrsim7$
— not impossible, but a specific, steep power not suggested by anything in AeST's own
literature (WP0's extraction found no closed form for $a_0$'s dependence on $Q$ beyond
the qualitative "assembled from... and..." description). This is a real escape route,
but it requires new, specific structure to be found and independently motivated, not
merely posited to make the numbers match — otherwise it is the same "selected because
it works, not derived" move this project has twice already flagged as an anti-pattern
in its own history (`cdot-8/ConsolidationLog-2026-07-12.md` item 4's underlying source
material; T8's $G\propto c^{-2}$; cdot-6's $s=+1/2$).

---

## 5. Verdict — escalating again, not deciding

Per the amended proposal's WP3 kill condition ("if no census-constrained $F(Q)$ family
reproduces the demanded curve... document and close"): under the simplest, most direct
reading of M2, **no such family exists** — the reconstruction is over-determined by the
invoice curve alone, and the resulting $Q(a)$ shape conflicts with independently-fit
data. Under a more permissive reading (an unconstrained, steep $g(\lambda_s,Q)$), the
kill condition does not obviously trigger, but nothing yet motivates the specific $g$
needed beyond curve-fitting. Given this project's established pattern — both prior WP3
escalations turned out to hinge on something the worker's setup had gotten subtly wrong,
not on a genuine dead end — this is flagged explicitly rather than assumed to be the
same kind of resolvable gap: it may be, but the algebra here has been checked as
carefully as this session can manage (independent re-derivation of $E(s)$; synthetic
validation of the reconstruction formula) without turning up an error. No file in
`cdot-7/` touched.
