# Session Log — CMB First-Peak Angular Scale Calculation

**Date:** 2026-07-03
**Scope:** Work out one of T16's open questions: "Can the self-similar baryon-photon
plasma (first peak) be computed numerically in the model's $c(t)$ background? Is the
predicted peak position consistent with $\ell_1\approx220$?"
**Outputs:** Update_2026-07-03_CMB_First_Peak_Angular_Scale.md; this log; edits to T16
**Session classification:** Destructive / falsification-relevant (a quantitative,
robust negative result; no fix found; narrows the model's viable claims on its own
self-declared hardest test)

---

## User Prompt

> Let's look at the T16 open questions and see if we can work out any of those.

Offered three candidates (PBH/RAR double-counting, first-peak angular scale, PBH
genesis crossover); user selected the first-peak angular-scale question.

---

## Session Activity

- Read T16, Core Principles, T2, T3, T13 to assemble every already-adopted formula
  needed: $D_p(z)$, $D_A(z)$, $R_\text{now}=6c_0/H_0$, the general $(n,P)$ exponent
  structure, and T16(C)'s self-similarity claim for $R\equiv3\rho_b/4\rho_\gamma$.
- **First pass:** computed $\theta_s=r_s/D_A$ at $z_\text{rec}=1090$ directly, using
  $r_s=(c_s/c)\times R_\text{rec}$ (sound horizon as proper distance travelled since
  genesis, exactly parallel to how $D_p$ is defined for light). Verified the distance
  formulas against Core's own worked table ($D_p(z{=}1)=2804$ Mpc reproduced exactly)
  before trusting the rest.
- Found $\theta_s\approx10.9$ rad for the volume-law branch — nonsensically large
  (physical angles must be $\ll1$ rad for a compact feature). Rather than accept this
  as a fluke, checked whether *some other* $z_\text{rec}$ would give a sane answer: the
  function $\theta_s(z)$ is U-shaped, with a genuine finite floor. Scanned
  $z=10^{-2}$–$10^{20}$ numerically to find that floor for each premise-2 branch
  ($n=3,2,2/3$).
- **Caught and corrected a framing error mid-session:** initially treated
  $R_\text{baryon}\to0$ (fastest sound speed) as the "best case" for reaching high
  $\ell_1$ — backwards. Since $\theta_s\propto1/\sqrt{1+R}$, *larger* $R$ (slower sound
  speed, smaller sound horizon) is what raises $\ell_1$. Redid the "best possible case"
  calculation correctly: hold $R$ fixed at the model's own self-similarity-implied value
  ($\approx680$, from today's real $\Omega_bh^2$, $T_0$ — not a free parameter), and
  optimize only over the genuinely unresolved quantity, $z_\text{rec}$.
- With that correction, found the honest floor: best achievable $\ell_1$ is 9.5
  (volume law), 15.0 (surface law), 67.1 (S$'$) — all still short of 220 by
  3.3$\times$–23$\times$, and the "best" $z$ in each case is unphysical ($z\sim2$–5,
  not a plausible recombination epoch).
- Checked whether tuning $R$ upward instead could close the gap: it would require
  $R\sim4\times10^8$ (volume law) to $5.5\times10^4$ (S$'$) at $z_\text{rec}=1090$ —
  many orders above the model's own implied value, and inconsistent with the BBN
  $\eta\approx6\times10^{-10}$ input already adopted (T13). Ruled out as an escape
  hatch.
- Separately verified the $R\approx680$ number itself is a problem independent of the
  geometry: $\Lambda$CDM needs $R\approx0.6$ at recombination specifically because
  $\rho_b\propto a^{-3}$, $\rho_\gamma\propto a^{-4}$ dilute at different rates; this
  model's static space has no dilution, so self-similarity pins $R$ at its *present-day*
  value for all time — a factor $\sim(1+z_\text{rec})$ too large by construction,
  not a coincidence.
- Wrote up the full derivation, the branch/robustness table, the foreclosed escape
  hatches, and the honest caveats (leading-order geometric argument only; $z_\text{rec}$
  circularity per T16 item A) into the update document.

## Results Summary

1. **T16's "first peak translates without dark matter" claim is half right.** The
   plasma-physics self-similarity argument (constant $R$, self-similar oscillator shape)
   stands. The angular-*position* half of the claim — needed for it to mean anything
   observationally — fails by 9$\times$ to 765$\times$ depending on premise-2 branch,
   using only formulas the model already treats as stable and derived.
2. **The result is robust**, not an artifact of one bad assumption: it survives (a)
   scanning across all three premise-2 branches, (b) granting the model total freedom
   over the unresolved recombination redshift, and (c) checking whether raising the
   baryon-loading parameter could rescue it (it cannot, without breaking the BBN input).
3. **Root cause identified**: the model's shallow $(1+z)^{-1/(nP)}$ distance law means
   recombination at $z\sim1090$ is not "early" in the model's own bookkeeping the way
   $a_\text{rec}/a_0\sim10^{-3}$ is early in $\Lambda$CDM — there isn't enough
   "distance budget" left between recombination and now to compress the sound horizon
   to a sub-degree angle.
4. **A self-caught error is documented**: the first version of the "best case" bound
   used $R\to0$, which is actually the *worst* case for reaching high $\ell_1$, not the
   best. The corrected calculation (fixed, empirically-grounded $R$, free $z_\text{rec}$)
   is what's reported.
5. **Not a full kill**: this is a leading-order geometric argument (no Boltzmann-code
   line-of-sight treatment), and it's possible the static-$c(t)$ framework needs a
   fundamentally different definition of "angular scale of an early-universe feature"
   rather than borrowing the FRW-style $D_A$/$D_p$ machinery wholesale — flagged as a
   new open question rather than a closed door.

## Merge Recommendation

Merge as a new section in T16 under (C), replacing the optimistic framing with the
derivation, table, and honest status change. Update Core's status-table CMB row and the
open-problems priority list to reflect that this is now a decisive, quantitative,
falsification-relevant tension on the model's self-declared hardest test — arguably
sharper than the T22 ephemeris tension already flagged as priority 0. Recommended next
session: investigate whether a static-space-appropriate redefinition of the
sound-horizon-to-angle mapping exists (the new open question in the update doc), before
treating this as a terminal result rather than a currently-unresolved one.
