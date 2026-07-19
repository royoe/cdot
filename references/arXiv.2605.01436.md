# Vaglio, et al. (2026) — Strong-Field Einstein-Æther Constraints from PSR J1738+0333

**Citation:** Vaglio et al., arXiv:2605.01436 (2026) — most recent, most
stringent single-binary-pulsar Einstein-æther bound as of this session.
**Source stored:** `arXiv.2605.01436/main.tex` (+ `refs.bib`, figures,
`00README.json`).

## What this is, for cdot-8

The most up-to-date binary-pulsar Einstein-æther analysis (Bayesian
timing pipeline on the full PSR J1738+0333 dataset), and WP6 sub-task
3's second literature anchor. Uses a **different but related** parameter
basis than Foster-Jacobson/Yagi's $(c_1,c_2,c_3,c_4)$ — the kinematic
decomposition $(c_\theta,c_\sigma,c_\omega,c_a)$ (expansion/shear/
vorticity/acceleration), then reduces to the PPN-facing set
$\{\alpha_1,\alpha_2,c_\omega\}$.

## Aspects load-bearing for cdot-8

- **Action (Eq. 1)**: $S=-\frac1{16\pi G}\int\{R+\frac13c_\theta\theta^2+
  c_\sigma\sigma_{\mu\nu}\sigma^{\mu\nu}+c_\omega\omega_{\mu\nu}
  \omega^{\mu\nu}+c_aA_\mu A^\mu+\lambda(U^2-1)\}+S_\text{mat}$, with
  $\theta=\nabla_\mu U^\mu$, $A_\mu=U^\nu\nabla_\nu U_\mu$, and
  $\sigma_{\mu\nu},\omega_{\mu\nu}$ the shear/vorticity of $\nabla U$.
- **Mode speeds** (Eqs. cT/cV/cS): $c_T^2=1/(1-c_\sigma)$; $c_V^2=
  (c_\sigma+c_\omega-c_\sigma c_\omega)/[2c_a(1-c_\sigma)]$; $c_S^2=
  (c_\theta+2c_\sigma)(1-c_a/2)/[3c_a(1-c_\sigma)(1+c_\theta/2)]$.
- **PPN-facing parameters** $\alpha_1\approx-4c_a$, $\alpha_2\approx
  \alpha_1/2+3c_a(1+c_a/c_\theta)/(2-c_a)$ — a cleaner, directly
  observationally-facing reduction than the raw four-parameter basis.
- **Solar-system bounds quoted**: $|\alpha_1|\lesssim10^{-4}$,
  $|\alpha_2|\lesssim10^{-7}$ — note $\alpha_2$'s bound is much tighter
  than $\alpha_1$'s; WP6's own derivation arc has so far only engaged
  with $\alpha_1$-class reasoning.
- Confirms GW170817 forces $c_\sigma\sim O(10^{-15})\approx0$, reducing
  the theory to 3 effectively independent parameters — consistent with,
  though a different-basis statement of, WP6's own $c_{13}=0$
  tensor-speed finding.

## A discrepancy found while cross-checking, then resolved

**Update 2026-07-18**: the discrepancy described below was fully
resolved. The dictionary error was a single entry: $c_a=c_1+c_4$
(the $c_1$ structure induces a genuine acceleration-squared term through
its $-u_aA_m$ piece, missed by matching only $c_4$'s explicit $A_\mu
A^\mu$ term), not $c_a=c_4$ alone. With this correction, Vaglio's own
$c_V^2$ formula gives exactly 1 at AeST's point, matching both
Foster-Jacobson's independently-verified spin-1 result and Vaglio's own
$c_T^2$ — a three-way agreement. Neither primary source was wrong.
AeST's aether is **vorticity plus acceleration**
($c_\omega=2K_B,c_a=K_B$), not pure vorticity — see
`cdot-8/WP6/Update-WP6-BinaryPulsar-2026-07-18.md` §2a for the full
resolution, verified independently before being accepted.

## The original discrepancy (superseded above, kept for the record)

Derived the $(c_\theta,c_\sigma,c_\omega,c_a)\leftrightarrow
(c_1,c_2,c_3,c_4)$ dictionary via the standard kinematic decomposition
of $\nabla_\mu U_\nu$ ($c_\sigma=c_1+c_3$, $c_\omega=c_1-c_3$,
$c_\theta=c_1+3c_2+c_3$, $c_a=c_4$ — the direct $c_a=c_4$ identification
is solid, since both multiply $A_\mu A^\mu$ identically in their
respective actions). At AeST's point ($c_1=K_B,c_2=0,c_3=-K_B,c_4=0$):
$c_\sigma=0$, $c_\omega=2K_B$, $c_\theta=0$, $c_a=0$ — a clean result,
**AeST's aether kinetic term is pure vorticity** in this basis (matches
the already-established finding that only the transverse/curl sector is
independently dynamical).

**But evaluating this paper's own $c_V^2$ formula at this point gives a
genuine pole** (finite nonzero numerator $2K_B$, zero denominator via
$c_a=0$) — apparently contradicting WP6's independently-verified result
(via Foster-Jacobson's own vector-mode formula, in their native basis)
that the vector/spin-1 mode speed is exactly 1 and healthy at this same
physical point. **This has not been resolved** — it is either a
translation error in the dictionary derived here, a genuine difference
in what the two papers' "$c_V$"/vector-mode formulas describe, or
something else not yet identified. Flagged explicitly rather than pushed
past, per this program's standing discipline; needs careful
reconciliation before any further sub-task-3 conclusion is drawn.

## Status in cdot-8's record

Read for its formalism; the parameter-basis translation to AeST's own
$K_B$ is only partially trustworthy pending the $c_V^2$ discrepancy's
resolution. See `WP6/Update-WP6-BinaryPulsar-2026-07-18.md` for the full
write-up.
