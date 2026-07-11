# Session Log — 2026-07-11

*Running log for cdot-7 work, appended per-prompt, per this project's convention. A new
calendar date gets a new file; continues from `SessionLog-2026-07-10.md`. Times in SAST
(UTC+2), approximate to the ten-minute mark as in prior logs.*

---

## Entry 1 — Challenging the radiation-era counting law (2026-07-11, ~09:5x SAST)

**Prompt (verbatim):**
> Consider the most recent update in the project, on RadiationEraClosure, which is the
> first attempt at solving a major outstanding issue in Foundation. The session
> producing this document went quite well, and I'm encouraged that it finds much better
> correspondance with standard radiation era models than earlier attempts have done.
> But I'm concerned about some assumptions, particularly about how it counts radiation
> relative to matter. The counting law seems like an arbitrary choice, still it works
> out reasonably well. I would have preferred to have a more better justified counting
> law. The premise is that the local speed of light is defined entirely in a Machian
> sense, so by a count of all that exists within an observers local causality horizon
> at a given time. Since the horizon always expands with c this count is always
> increasing. The question is what to count when mass and energy varies with c. The
> system has shown good results in recent epocs by just counting mass or massive
> particles, but in the radiation era things get complicated. Please assess plausible
> counting laws and advice.

**Summary:** Located the freedom precisely: under conserved coordinate number densities
every pure count scales as $R_h^3$, so the counting law is really the per-entity weight
function $w_i(c)$, and the entire radiation-era structure lives in the weights'
$c$-scaling. Surveyed candidates: rest-mass-only, unweighted-number, entropy, and mode
counts all fail (no crossover; the latter three photon-dominated by $10^9$ at every
epoch); energy vs. mass-equivalent censuses coincide once dimensionless; Tolman
($\eta=2$) weighting survives only as a systematic pending item 7. Recommended
restating the counting law as the **Planck-unit census** $\mathcal N=\sum E_i/E_P(t)$,
$M_h=\mathcal N m_P$: arithmetically identical to the adopted law, but (i) genuinely
dimensionless (an actual count), (ii) reducing to particle-counting for matter *because
of* premise 3 ($m/m_P=\sqrt{\alpha_G}$ invariant — the same symmetry that fixed
$s=\tfrac12$ fixes the counting law), (iii) forcing the photon weight, (iv) making
$\eta=1$ principled (an inventory has no pressure), (v) forcing the missing neutrino
third term via relativistic dispersion with conserved coordinate $k$, and (vi)
replacing per-species number conservation with census continuity through
energy-conserving conversions. Flagged caveats (post-diction; $\eta=2$ lurking;
continuity as an assumption for item 10; binding energy uncounted; closure form
untouched) and one numeric discrepancy to check: the 07-10 update's
$z_{\nu,\text{nr}}\approx2733$, suspected (incorrectly, as Entry 2 found) to be a
$\Sigma m_\nu$-for-per-state slip. Offered to verify, compute, and write up.

**Status at this point:** conceptual only; no files.

---

## Entry 2 — Verification, the census neutrino term, and the write-up (2026-07-11, ~10:0x–10:3x SAST)

**Prompt (verbatim):**
> Very well! Please proceed.

**Summary of work performed:**

1. **Independent verification of the 07-10 update (from documented equations alone;
   the original `radiation_closure.py` is not in the project knowledge and was not
   consulted).** Reimplemented the two-fluid closure end-to-end
   (`census_closure.py`, Part 1). Every headline number reproduces: fixed points
   $1.7222/3.4443$ (ratio exactly 2, $\mu$-independent); $z_\text{eq}$ per convention
   $1465/2060/2278/2654$ ($\eta{=}1$) and $732$–$1327$ ($\eta{=}2$); trajectory
   recovery to the matter fixed point by $z\sim10$; $x(1100)\in[2.14,2.37]$ at
   $\eta{=}1$, max $2.68$ at $\eta{=}2$ (update said "up to 2.67" — rounding);
   settling at $3.44$ by $z\sim10^5$–$10^6$. §16's numbers are now double-checked,
   not single-sourced.

2. **Census identity checks.** Algebraic term-by-term identity with the adopted law
   confirmed; matter census weight $=\sqrt{\alpha_G}$, epoch-invariant by premise 3 —
   the counting law, the $s=\tfrac12$ derivation, and LLR safety shown to be the same
   dimensionless statement (link to ResearchNotes §7).

3. **The neutrino third term, built (was 07-10 item 5(b), "not attempted").** Census
   weight $\sqrt{(m_\nu c^2)^2+(\hbar kc)^2}/c^2$ with conserved coordinate $k$
   (premise 1 Noether, same as photons) and $m_\nu\propto c^{1/2}$; shown via the
   dictionary to equal the standard massive-neutrino relativistic Fermi–Dirac energy
   density in local units exactly. FD integral validated at both limits to 7 digits.
   With the four-term fit's own $\Sigma m_\nu=1.374$ eV:
   $\Omega_\nu^\text{census}(0)=0.0298$, and
   $\Omega_b+\Omega_\nu^\text{census}=0.0740$ — matching the closure's demanded
   $0.074$ to $0.1\%$, unprompted.

4. **Three-component integration.** Identical to the two-fluid trajectory to 4 digits
   at $z\le10$ (four-term fit untouched, checked, not assumed); deviates $>1\%$ only
   above $z\approx190$; both fixed points exactly unchanged. Revisions:
   radiation-like$=$matter-like crossing at $z\approx1080$ (essentially at
   recombination; two-fluid had $1466$); $x(1100)=2.61$ primary, $[2.32,2.61]$ across
   conventions, $2.67$ standard $\mu$ — a systematic $+10\%$ over the two-fluid
   $[2.14,2.37]$. Neutrinos are mid-transition at recombination ($40\%$ of their
   census energy kinetic), confirming and now exactly resolving the 07-10 flag.

5. **$z_{\nu,\text{nr}}$ discrepancy resolved — and Entry 1's suspicion retracted.**
   The 07-10 marker $2733$ is the $T_\nu=m_\nu$ convention with the *correct*
   per-state mass (reproduced: $2731$), not a $\Sigma m_\nu$ slip. Physically weighted
   markers: $\langle p\rangle=m_\nu c$ at $z\approx866$; census kinetic$=$rest at
   $z\approx1445$. The census's smooth weight supersedes all threshold markers.

6. **Write-up.** `Update-CountingLaw-PlanckCensus-2026-07-11.md` produced (Parts 0/A/B:
   candidate survey; Foundation §2.1 restated as the census, §2.3 amendments with the
   forced neutrino term and revised numbers; §6 items 4/5/9/10 amendments;
   ResearchNotes §17 derivation trail with caveats ledger). Figure
   `census_trajectory.svg`/`.png` generated. Merge dependency on the still-unmerged
   07-10 update stated explicitly in the document header.

**Files produced:** `Update-CountingLaw-PlanckCensus-2026-07-11.md`,
`SessionLog-2026-07-11.md` (this file), `census_closure.py`,
`census_trajectory.svg`, `census_trajectory.png`.

**Open items handed forward, not silently dropped:** census-form $e^+e^-$/QCD
re-weighting kinks (now well-posed, uncomputed); $N_\text{eff}=3.044$ refinement;
folding the census $\Omega_\nu$ into a four-term-fit rerun; the census-continuity
assumption on item 10's desk; $\eta=2$ systematic carried in two-fluid form only.
