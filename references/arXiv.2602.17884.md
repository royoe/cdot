# Park, Hees, Famaey, Desmond & Durakovic (2026) — "Improved constraints on modified Newtonian gravity from Cassini radio tracking data"

**Citation:** arXiv:2602.17884 (2026).
**Source stored:** `arXiv.2602.17884/main.tex` (+ `.bbl`/figures).

## What this is, for cdot-8

An updated Cassini-based bound on the Solar System **quadrupole
parameter $Q_2$**, which encodes MOND's **External Field Effect (EFE)**
— the nonlinearity of the AQUAL/QUMOND Poisson equation means the
Milky Way's own external gravitational field leaks into and distorts
internal Solar System dynamics, breaking the strong equivalence
principle. Using the full DE440 ephemerides dataset (extending the
original Cassini analysis, Hees et al. 2014, through 2017), they find
$$Q_2=(1.6\pm1.8)\times10^{-27}\text{ s}^{-2}\quad(1\sigma),$$
a 40% improvement over the prior bound, consistent with zero. Combined
with SPARC galaxy rotation curves, this raises the tension between
Solar-System and galactic-scale MOND to **3–15σ** depending on mass
modeling, and independently rules out AQUAL/QUMOND at high significance
via Milky Way rotation-curve mass modeling alone (§ "Milky Way" section
in-text).

## Why this is a genuinely different test from anything already in cdot-8

WP6 sub-task 1 (`Update-WP6-TensorSpeedStructure-2026-07-18.md` §4)
already tests a **residual anomalous acceleration** bound at Saturn
(Hees et al. 2014/2016-class, ~$4\times10^{-14}$ m/s²) — a test of the
interpolating function's (IF's) behavior **far above** $a_0$ (Saturn's
own internal field), which any sufficiently sharp/screened large-
gradient completion trivially passes.

**$Q_2$ is different in kind**: the paper's own key point (attributed
to Desmond & Famaey's companion paper, "Desmond\_Cassini") is that
$Q_2$'s predicted value depends *solely* on the IF's shape at the
**external** field $e_N\equiv a_e^N/a_0$ (the Milky Way's Newtonian
field at the Sun's position) — which is $O(1)$–$O(2)$ in $a_0$ units,
i.e. squarely in the **MOND-Newtonian transition region**, not the deep
Newtonian tail. Making the IF sharper *above* $a_0$ does **not** reduce
$Q_2$. This means $Q_2$ probes exactly the same near-$a_0$ IF shape
that any AQUAL/QUMOND-class theory (including AeST's own quasistatic
Y-sector, which cdot-8 inherits unchanged) must use to fit galaxy
rotation curves — the "screening at large gradients" argument that
resolved WP6's original Cassini test does not obviously apply here.

## Key formulas (quoted directly, used in `wp6_q2_efe_check.py`)

IF families (their Eq. 6): $\nu_n(x)=\left[\frac{1+\sqrt{1+4x^{-n}}}2
\right]^{1/n}$ ("Simple" at $n=1$, "Standard" at $n=2$);
$\nu_\delta(x)=(1-e^{-x^{\delta/2}})^{-1/\delta}$ (RAR IF at $\delta=1$).
Quadrupole: $Q_2=-\frac{3a_0^{3/2}}{2\sqrt{GM_\odot}}q$, with
$q=\frac32\int_0^\infty dv\int_{-1}^1 d\xi\,(\nu-1)\big[e_N(3\xi-5\xi^3)
+v^2(1-3\xi^2)\big]$, $\nu$ evaluated at $\sqrt{e_N^2+v^4+2e_Nv^2\xi}$.
$e_N$ solves $\nu(e_N)e_N=a_e/a_0$ ($a_e=2.32\times10^{-10}$ m/s²,
Gaia-measured external field) — **not** simply $a_e/a_0$ (a distinction
that mattered: an initial naive calculation using $e_N=a_e/a_0$ directly
was caught and corrected before trusting the result, via a validation
cross-check against the paper's own quoted $e_N=1.643$, $Q_2=3.387
\times10^{-26}$ for their $\delta=1$ case — matched to 4 digits once
corrected).

## Status in cdot-8's record

Opened as WP6 sub-task, `Update-WP6-TensorSpeedStructure-2026-07-18.md`
§6 (new). cdot-7's own established, explicitly-preferred Simple IF
($\kappa=1$, $a_0=1.39\times10^{-10}$ m/s²) predicts
$Q_2\approx3.7\times10^{-26}$ s$^{-2}$ — **~23× the new bound's central
value, ~21σ in tension**; the RAR alternative (also explored by cdot-7,
with its own preferred $a_0\approx1.26\times10^{-10}$) gives essentially
the same tension (~23×, ~21σ), confirming this is not fixable by
switching IF family alone. A serious, escalated finding, not a
unilateral kill — see WP6 update and `ConsolidationLog` for the
cdot-7-relevant framing.
