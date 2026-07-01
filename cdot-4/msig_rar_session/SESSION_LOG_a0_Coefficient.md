# SESSION LOG — Deriving the $a_0$ Coefficient (T14 / T6)

**Topics:** T14 (Connecton Gravity), T6 (MOND scale), Core Principles (horizon geometry)
**Date:** 2026-06-30
**Session type:** Derivation attempt — can the order-one coefficient in $a_0 = cH_0/k$ be
derived rather than fitted?

---

## Timeline

**[2026-06-30 14:21 UTC] — Prior session.**
Kinetic derivation of the RAR closure. Flagged the scale coefficient ($a_0\approx cH_0/2\pi$,
tied to the closure condition $4\pi GL\rho_\text{bg}/3\sigma=c$) as the biggest remaining
open item.

**[2026-06-30 14:33 UTC] — User prompt (verbatim):**
> This is encouraging. Can we give a shot at deriving the coefficient?

**[2026-06-30 14:33 UTC] — Work performed.**

1. Reality check on the empirical ratio: $cH_0/a_0 \approx 5.5$–$5.9$ (Planck–SH0ES), NOT
   $2\pi=6.28$. So the honest target is "coefficient ~5–6," and $2\pi$ is only a near-miss.
2. Forward derivation from T14's background-gradient form $g_\dagger=c^2|\nabla\rho|/\rho$.
   Leading local estimate $|\nabla\rho|/\rho\sim H_0/c$ gives coefficient 1 ($g_\dagger=cH_0$)
   — too large. The O(1) factor must come from horizon geometry.
3. Found the factor 6 already in the model: $R_0=3P c/H_0^\text{obs}=6c/H_0$ (T3, Core §4a),
   where 3 = horizon ODE ($H^\text{hor}=3c/R$) and $P=2$ = horizon/observable Hubble
   conversion.
4. Identified the key distinction (Core §4a, §5): $\dot c/c=H^\text{hor}$, and
   $H_0^\text{obs}=P H_0^\text{hor}$. The current T14 "$g_\dagger=\dot c=cH_0$" conflates the
   two rates, AND uses the temporal rate where the force is actually the spatial gradient.
5. Correct object: $g_\dagger = c^2/R_0 = cH_0^\text{obs}/6$. Note $\dot c=3g_\dagger$, so
   $g_\dagger=\dot c/3$.

**[2026-06-30 14:33 UTC] — Result.**

$a_0 = g_\dagger = c^2/R_0 = cH_0^\text{obs}/6$ (closure passes it through with coefficient 1,
verified). Numerical: 1.09e-10 (Planck) to 1.18e-10 (SH0ES); measured 1.20e-10
(±0.24 sys). Within $-0.5$ to $-0.1\,\sigma_\text{sys}$ across the range. Exact at H0=74.1.

Two corrections to T14:
- A: coefficient is exactly 6 (horizon geometry), not $2\pi$; 6 also fits better.
- B: $\dot c$ uses the horizon rate ($\dot c=cH_0^\text{obs}/2$), and is the wrong object —
  the force is the spatial gradient $c^2/R_0$, not the temporal rate $\dot c$; they differ by
  the horizon ODE factor 3.

**[2026-06-30 14:33 UTC] — Critical assessment.**

DERIVED: the factor 6 = 3P, fully from horizon geometry already in the model (T3/Core).
The Hubble-rate distinction is forced by Core §4a/§5.

CONTINGENT: one O(1) input — $|\nabla\ln\rho_\text{bg}|=1/R_0$ exactly (coefficient 1). The
data favor unity, so this is a mild use of the data, not a pure prediction. Closing it needs
the background density profile $\rho_\text{bg}(r)$ from horizon growth.

This is the connecton/gradient route; it supersedes (does not derive) the kinetic closure
condition $4\pi GL\rho_\text{bg}/3\sigma=c$. Depends on $P=2$ (coefficient = 3P).

**Verdict:** The coefficient is derived as $cH_0/6$ from horizon geometry — cleaner than and
superior to the old $2\pi$, and it corrects two errors in T14. One O(1) gradient coefficient
remains, reducible to a single density-profile calculation. The RAR now has shape (prior
session) + scale (this session) both substantially derived.

**[2026-06-30 14:33 UTC] — Visual produced.**
Predicted $a_0$ vs $H_0$ for coefficient 6 and $2\pi$, against the measured $a_0\pm$systematic
band, over the Planck–SH0ES range.

**[2026-06-30 14:33 UTC] — Deliverables.**
- `UPDATE_T14_a0_Coefficient_Horizon.md`
- `SESSION_LOG_a0_Coefficient.md` (this log)

**Next computation flagged:** derive $\rho_\text{bg}(r)$ from horizon growth, compute
$|\nabla\ln\rho_\text{bg}|$ directly; if = $1/R_0$ exactly, the coefficient is fully closed.
Also: search T6/T15 for stray $2\pi$ and correct to 6.
