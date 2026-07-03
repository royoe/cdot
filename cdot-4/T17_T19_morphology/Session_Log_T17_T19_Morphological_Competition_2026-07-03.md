# Session Log — T17/T19: Morphological Competition Timescale Integration

**Date:** 2026-07-03
**Session window (UTC):** ~11:45 – 12:25 (continuation of research-priorities arc;
follows T7 QED and T14 PPN synthesis sessions)
**Scope:** Discharge audit structural tension #6 (§III.2): compute stripping-to-thinning
timescale ratio for a fiducial MW-like disk as a function of $r/r_t$ and $v_\phi/v_f$,
via orbit integration, before formal write-up.
**Outputs:** `orbit_integration.py`; `Update_2026-07-03_T17_T19_Morphological_Competition.md`;
this log
**Session classification:** Constructive (audit tension reconciled at population level;
one substantive open item on flat-curve vs $g_x$ equilibrium)

---

## User Prompts

**[2026-07-03 ~11:30 UTC] Prompt 1 (prior turn):**

> Ok

*(Acknowledgement to proceed with orbit integration before write-up, following Tier-2
§6 morphological-competition analysis.)*

**[2026-07-03 ~12:22 UTC] Prompt 2:**

> Ok

*(Acknowledgement to proceed with formal Update and Session log after integration
completed.)*

---

## Session Activity (timestamps UTC, approximate)

### Orbit integration (prior sub-session, resumed)

- **11:45** — Read audit §III.2, T17 Link 4 cross-caveat, T19 §6 cross-caveat. Confirmed
  required deliverable: RK4 integration of cylindrical ODEs with Lorentz stripping (T17)
  and vertical spring (T19).
- **11:50** — Created `cdot-4/T17_T19_morphology/orbit_integration.py`. Initial runs
  exposed three bugs: (i) $H_0$ Mpc conversion off by $10^3$; (ii) spurious $-\omega_z^2 z$
  in radial ODE; (iii) timestep too coarse for vertical motion ($\sim 17$ oscillations per
  RK4 step → overflow).
- **11:55** — Replaced spring strength with RAR-gated $(g_x/g_\text{bar})\,\omega_\text{grav}^2$.
  Replaced $\omega_\text{grav}^2 \sim v_f^2/(2r)$ with disk-scale estimate
  $\omega_\text{grav} = \sigma_z/h$ ($h=0.1 R_d$, $\sigma_z=0.2 v_f$).
- **12:00** — Tested velocity reference: flat-curve $v_f$ vs marginal $v_\text{marg}(r)$.
  Found $v_f/v_\text{marg} \approx 2.2$ at $r=10$ kpc when binding uses $g_x$.
- **12:05** — Switched radial binding to $g_x(r)$ (RAR closure). Marginal orbits
  ($\delta=0$ vs $v_\text{marg}$) stable over $5\,\tau_\text{dyn}$; flat-curve $u=1$
  escapes in $\sim 47$ Myr.
- **12:10** — Full $u$-sweep ($0.5$–$2.0$): crossover $u \approx 1.12$ where
  $t_\text{strip} = \tau_\text{vert} \approx 40$ Myr. Coupled 3D ($z_0=300$ pc,
  $\delta=0.05$ marginal): stable, $z_\text{amp}$ maintained.
- **12:12** — Cosmic adiabatic thinning estimate: $\sim 11\%$ $h$-compression
  $z=1\to0$; $\sim 46.5$ Gyr to halve $h$.

### Write-up (this sub-session)

- **12:20** — Drafted Update document with model specification, results tables, regime
  diagram, reconciliation, open items, and edit list.
- **12:25** — This session log.

---

## Key Results (fiducial $r_0 = 10$ kpc)

| Result | Value |
|---|---|
| $r_t$ | $8.6$ kpc |
| $v_f$ | $173$ km/s |
| $v_\text{marg}$ | $79$ km/s ($u_\text{marg} \approx 0.45$) |
| $\tau_\text{vert}$ | $40$ Myr |
| $t_\text{strip}$ at $u=1$ | $47$ Myr |
| Crossover $u$ | $\approx 1.12$ |
| $t_\text{halve}\,h$ (cosmic) | $\sim 47$ Gyr |

**Conclusion:** T17 and T19 are not in temporal conflict. They select different
velocity sub-populations on different timescales (Myr vs Gyr). Audit §III.2 is
reconciled at the population level.

---

## Open at Session End

1. **Flat-curve equilibrium:** $u=1$ is above $g_x$ marginal binding at $r>r_t$ in this
   closure — consistent with dynamical selection but not static equilibrium.
2. **Attractor convergence** (T14): orbit integration supports the picture but does not
   prove $B_c = v_f/r$ emerges from a realistic disk.
3. **Merge edits** (Update §7): not applied to T17, T19, audit, or Project Summary
   (awaiting user request).

---

## Files Touched

| File | Action |
|---|---|
| `cdot-4/T17_T19_morphology/orbit_integration.py` | Created, iterated, committed to repo |
| `cdot-4/T17_T19_morphology/Update_2026-07-03_T17_T19_Morphological_Competition.md` | Created |
| `cdot-4/T17_T19_morphology/Session_Log_T17_T19_Morphological_Competition_2026-07-03.md` | Created (this file) |
