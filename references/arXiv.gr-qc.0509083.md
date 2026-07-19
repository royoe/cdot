# Foster & Jacobson (2006) — "Post-Newtonian parameters and constraints on Einstein-aether theory"

**Citation:** B. Z. Foster & T. Jacobson, Phys. Rev. D 73, 064015 (2006); arXiv:gr-qc/0509083.
**Source stored:** `arXiv.gr-qc.0509083/ppn0208.tex` (single-file source, no separate bib).

## What this is, for cdot-8

The classic reference PPN derivation for Einstein-æther theory — WP6's
starting point for sub-task 2 (PPN $\alpha_1,\alpha_2$ for AeST/cdot-8),
used both for its final formulas and, more importantly, for the
order-by-order *method* by which they're derived.

## Aspects load-bearing for cdot-8

- **Eq. 1–2**: the general Einstein-æther action and kinetic tensor
  $K^{ab}_{mn}=c_1g^{ab}g_{mn}+c_2\delta^a_m\delta^b_n+c_3\delta^a_n
  \delta^b_m+c_4u^au^bg_{mn}$ — the basis WP6 mapped AeST's own Maxwell-
  type aether kinetic term ($-\frac{K_B}2F^{\mu\nu}F_{\mu\nu}$) onto,
  finding $c_2=c_4=0,\ c_3=-c_1$.
- **Eq. (10)–(11)** (as cited in WP6): the exact $\alpha_1,\alpha_2$
  formulas in terms of $c_1,c_2,c_3,c_4$ (with shorthand $c_{13}=c_1+c_3$,
  $c_{14}=c_1+c_4$, $c_{123}=c_1+c_2+c_3$). Applying AeST's restriction
  gives $\alpha_1=-4c_1$ (finite) but **$\alpha_2$ diverges identically**
  at $c_{123}=0$ — verified symbolically (sympy) in WP6, not by hand
  algebra alone.
- **The physical derivation method** (fetched in detail for WP6's own 1PN
  attempt): solve the aether constraint for $u^0$ at $O(1)$, the static
  metric sector, then the aether field equation for the spatial component
  $u^i$ at $O(1.5)$ — sourced by matter's momentum flux $\rho v^i$ — then
  the $g_{0i}$ Einstein equation at the same order, reading off
  $\alpha_1,\alpha_2$ from the resulting $V_i,W_i$-potential coefficients.
  This order-by-order structure is what WP6 is attempting to replicate
  (with an added scalar field $\phi$) for AeST/cdot-8, and is exactly why
  a prose-only attempt was judged too risky to trust without the same
  systematic bookkeeping.
- $u^i$'s own formula (their Eq. 6) has $c_{123}$ in a denominator too —
  confirms the **aether's own momentum-flux response is independently
  singular** at AeST's kinetic-term point, prior to and consistent with
  the $\alpha_2$-formula divergence.
- **$c_{123}=0$ is independently documented** (cross-checked against the
  wider Einstein-æther literature, not just this paper) as the condition
  under which the theory's own spin-0 (scalar) aether mode becomes
  non-propagating — the physical reading behind WP6's finding that AeST's
  restricted aether has no native scalar dynamics of its own, which is
  *why* the explicit field $\phi$ exists in AeST at all.

## Status in cdot-8's record

Central to WP6 §5–5b (sub-task 2). The $c_{123}=0$ degeneracy finding is,
so far, the single most significant unresolved technical question in
WP6 — whether cdot-8's scalar $\phi$ regularizes this degeneracy (per the
advisory's pre-registered expectation) or whether it stands as a genuine
problem for AeST's Maxwell-only aether choice remains **open**, flagged
for dedicated, order-by-order resolution rather than prose reasoning.
