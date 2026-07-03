# Session Log — T7: First-Order QED Treatment of $\alpha$ Running (Variable-$c$ Vacuum)

**Date:** 2026-07-03
**Session window (UTC):** ~09:15 – 09:30 (continuation of the research-priorities and
Tier-1.3 scoping conversation)
**Scope:** Attempt the first-order QED treatment flagged in T7 and the Project Summary
(§5 item 2): does one-loop vacuum polarization produce observable $\alpha$ drift when $c$
varies cosmologically, given $\epsilon_0\propto\mu_0\propto c^{-1}$ and invariant
$m_e,e,\hbar$? Compare to ESPRESSO ($|\Delta\alpha/\alpha|\lesssim 1$–$2$ ppm at
$z\sim 1.15$) and the naive T7 estimate ($\sim 500$ ppm at $z\sim 1$).
**Outputs:** Update_2026-07-03_T7_QED_Alpha_Running.md; this log
**Session classification:** Constructive (open threat discharged at first order; one
diagnosed error in naive estimate; status upgrades proposed for T7 and Core §7)

---

## User Prompts

**[2026-07-03 ~09:15 UTC] Prompt 1 (prior turn):**

> Please examine the latest project branch and consider the most important topics for
> further research.

*(Tier-1.3 identified: QED running of $\alpha$, naive $\sim 500$ ppm vs ESPRESSO.)*

**[2026-07-03 ~09:20 UTC] Prompt 2:**

> Let's make an attempt at Tier 1.3, and the first-order QED treatment.

**[2026-07-03 ~09:26 UTC] Prompt 3:**

> Please write this up as a Change request document, with a corresponding Session log,
> using the same style as in e.g cdot-4/new_tests. Ask to create a folder in cdot-4 with
> title "T7_QED_treatment" and place the documents there.

**[2026-07-03 ~09:28 UTC] Prompt 4:**

> Ok. please create the two files.

---

## Session Activity (timestamps UTC, approximate)

- **09:20** — Read T7, Core §2 (EM-forced $\epsilon_0\propto c^{-1}$), Project Summary
  §5 item 2, and observational test-battery cross-references. Established the MM
  observable: $\Delta\alpha/\alpha$ from spectral line ratios with sensitivity coefficients
  $K_i$, not tree-level $\alpha$ alone.
- **09:22** — Wrote one-loop vacuum-polarization structure: $\alpha_\text{eff}(q^2)$ depends
  on dimensionless $\mathcal{R}=q^2\hbar^2/(m_e^2 c^4)=(q/(m_e c))^2$; vertices through
  $\alpha_0$ only; fermion mass shell uses invariant $m_e$.
- **09:23** — Reproduced naive T7 estimate: $q\sim m_e c$ gives $\mathcal{R}=1$,
  $\Delta\ln\mathcal{R}=\ln 2$ from $z=1$ to now, $\Delta\alpha/\alpha\sim(\alpha_0/3\pi)\ln 2
  \approx 540$ ppm — confirms the documented naive magnitude but flags wrong probe scale.
- **09:24** — Identified physical atomic scale from hydrogenic binding:
  $p_n\sim\alpha m_e c$, hence $\mathcal{R}\sim\alpha^2$ (or $(Z_\text{eff}\alpha)^2 f(n,\ell)$)
  — **epoch-independent**. Corrected result: $\Delta\alpha/\alpha=0$ at one loop for MM.
- **09:25** — Checked structural consistency: $E_\text{Ryd}/(m_e c^2)$, $a_B/\lambda_C$,
  $r_e/a_B$ all $c$-independent under cdot scaling; Lamb shift $\propto\alpha^5 m_e c^2\ln(1/\alpha^2)$
  scales as $c^2$ like all atomic energies — no extra drift.
- **09:26** — Drafted order-of-magnitude table (naive vs atomic scale); predicted
  $\Delta\alpha/\alpha(z)=0$ curve; honest ledger (asymmetric $\epsilon_0/\mu_0$ split,
  analysis systematics, optional line-by-line MM ion check remain open/separate).
- **09:28** — Prepared change-request update and this session log in `new_tests` style;
  proposed folder `cdot-4/T7_QED_treatment/` and six-item merge list (T7, Core §7, Project
  Summary, Test Battery cross-notes).
- **09:29** — Created `cdot-4/T7_QED_treatment/` with Update and Session Log files.

## Results Summary

1. **Tier-1.3 discharged at first order.** The QED $\alpha$-drift threat identified as the
   highest-leverage unfinished theory calculation in the Project Summary is resolved:
   $\Delta\alpha/\alpha=0$ for the MM observable at one-loop vacuum polarization.
2. **Naive 500 ppm estimate diagnosed.** T7's speculative estimate used $q\sim m_e c$
   (Compton scale) instead of $q\sim\alpha m_e c$ (Bohr/atomic scale). The "additive vs
   multiplicative" confusion noted in T7 is the multiplicative factor $\alpha$ in
   $q/(m_e c)$.
3. **Tree-level invariance extended.** Relational $c$-scaling moves the renormalization
   point with the atomic scale; $\mathcal{R}$ is epoch-independent at the physical probe
   scale. ESPRESSO is a **passed** consistency check, not a pending exclusion.
4. **Six-item edit list** (update doc §8): T7 major correction + status upgrade; Core §7
   table row; Project Summary cross-note; Test Battery cross-note.

## Merge Recommendation

The algebra is elementary (hydrogenic momentum assignment + one-loop log argument); edits
1–4 can be merged after a quick numerical spot-check of $\mathcal{R}=\alpha^2\approx 5.3\times
10^{-5}$ and confirmation that T7's naive $\ln 2$ step is explicitly marked superseded.
Optional follow-up: line-by-line MM ion check (Fe II / Mg II) to pin $Z_\text{eff}\alpha$
factors — confirmatory, not load-bearing. No core premise changes.
