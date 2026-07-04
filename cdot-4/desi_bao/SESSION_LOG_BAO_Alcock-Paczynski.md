# SESSION LOG — BAO / Alcock–Paczynski Shape Test

**Topic:** Deciding which part of the core must change to save the model, given
CMB-peak and BAO problems; testing whether the horizon-count model must go and
whether a Machian mass-count route can give a non-horizon-determined $D_p(z)$.
**Date:** 2026-07-04 (UTC)
**Outcome:** Constructive — decisive parameter-free result. One update document produced.

---

## Timeline

**2026-07-04T07:4x UTC — User prompt 1**
> The files in this project are stored in github, including a Core Principles
> document, and a series of numbered Topic documents together describing the
> model. The purpose of this project is to challenge and evolve the model in
> such a way that a coherent picture emerges. Be critical and constructive, and
> don't take prior results as authoritative. Sessions that produce results that
> challenge or improves the content in these files should present them as an
> update document [...] also produce a session log [...]. We have reached a
> critical point [...] after identifying problems with both the CMB peaks and
> the BAO tests. [...] The BAO tests point strongly towards a problem with the
> D_p z-relation. Any simple exponential law will give a poor fit to the DESI
> observations. [...] My hunch is that the horizon count model is the one that
> must go, and that a Machian model counting by mass that gives a non-horizon
> determined D_p relation is still a candidate. How can we set up such a test?

**Response 1 (design).** Read Core Principles, T16 (CMB), T12 (premise-2 fork),
T4 (counting-law variants), T3 (BAO/H(z)), T14 (connecton scales). Diagnosed
that the horizon-count model chains premise 2 ($c\propto R^n$) → horizon ODE →
$D_p=R_\text{now}-R_\text{emit}$ → single rigid shape $D_p=R_\text{now}[1-(1+z)^{-1/(nP)}]$,
so no exponent rescues the fit. Proposed a three-step falsification: (1) a
parameter-free Alcock–Paczynski ratio $F_\text{AP}=D_M/D_H$ shape cut (removes
$r_d$, $H_0$); (2) re-derive $M_u(z)$ for a mass-count variant with a
physically-fixed epoch-dependent $n(z)$ and re-solve; (3) SN/CMB/age
consistency cross-checks. Flagged T3's unresolved BAO clock choice as the gate
to settle first.

**2026-07-04T07:5x UTC — User prompt 2**
> Go ahead!

**Response 2 (execution).** Retrieved DESI DR2 BAO (six bins with both
$D_M/r_d$ and $D_H/r_d$). Built and validated the AP pipeline:
- ΛCDM ($\Omega_m=0.31$): $\chi^2\approx9$, $A\approx1.00$ — pass.
- $R_h=ct$: $\chi^2\approx53$ — correctly fails.
Established that in the static ($a=1$) construction $D_M=D_p$ and
$D_H=dD_p/dz$, so the AP ratio is **parameter-free** ($A=1$ forced) with
$F_\text{AP}(z)=\tfrac{1+z}{b}[(1+z)^b-1]$, $b=1/(nP)$ (verified $R_\text{now}$
cancels numerically).

**Key results:**
| Law | $b$ | $\chi^2$ (6 pts, 0 free) |
|---|---:|---:|
| Volume | 1/6 | 93.9 |
| Surface | 1/4 | 175.9 |
| Best single power (nP≈27) | 0.038 | 49.6 |
| ΛCDM (ref) | — | 9.0 |

Residual is S-shaped; worst single pull $+7.9\sigma$ at $z\approx0.93$.

**Findings / corrections during the session:**
- Initial shape-fit that allowed a free normalisation $A$ gave a misleadingly
  good $\chi^2\approx28$; recognised that the self-consistent construction
  forces $A=1$ (because $D_H=dD_p/dz$), which raises the honest parameter-free
  value to $\chi^2\approx94$. Recorded the corrected, forced-$A=1$ result.
- The clock ambiguity flagged in T3 does **not** arise in the honest
  construction: $D_H$ is derived, not chosen. Two-clock variants tested
  separately fared worse ($\chi^2\gtrsim300$). BAO failure is therefore not a
  clock artifact.

**Conclusion.** User's hunch confirmed and sharpened: the fault is the
structural lock $D_H=dD_p/dz$ (single $c(t)$ fixes both redshift and ruler),
not normalisation and not clock choice. Defined the target for the Machian
mass-count route: break the lock via $M_u\not\propto R^3$ from a
physically-fixed $n(z)$ (T12 radiation weighting or T13/T16 PBH freeze-out),
while preserving SN (T4), CMB first-peak self-similarity (T16), and 21 Gyr age
(T1).

---

## Artifacts produced
- `UPDATE_BAO_Alcock-Paczynski_Shape_Test.md` — proposed update for merge.
- `SESSION_LOG_BAO_Alcock-Paczynski.md` — this log.

## Data source
- DESI DR2 BAO, Table IV (values as tabulated in arXiv:2511.12017 Table I).

## Open next steps (for a following session)
1. Redo the AP fit with the full DESI $D_M$–$D_H$ covariance (will not rescue
   a $+7.9\sigma$ pull, but tightens the statement).
2. Derive $M_u(z)$ for the mass-count variant with $n(z)$ fixed by T12/T13,
   re-solve the modified horizon ODE, recompute $F_\text{AP}$.
3. Re-run SN (T4), CMB first-peak (T16), age (T1) consistency for any $n(z)$
   that improves BAO.
