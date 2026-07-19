# Update — WP4b: Both Flagged Bugs Confirmed Real; the Correction Is Bigger Than a Patch; Preliminary Recalculation Shows a Substantially Larger Deficit

*Companion: `SessionLog-2026-07-16.md` (this directory — being rewritten in
full this round after an accidental overwrite; see below). Responds to
`Advisory-WP4ab-ReviewAndPreDecisionChecklist-2026-07-16.md` and
`wp4b_check.py`. Also closes the checklist's WP3 item.*

---

## 1. WP3 formally closed

The checklist's concern (the covariant-$g_i$ verification and $D\equiv0$
conclusion were never independently re-confirmed) undersells what
`Update-WP3-NoLapseConfirmed-2026-07-15.md` already did — but the advisory's
underlying instinct (don't rest on an "expected but unconfirmed" identity) is
right, and the check is cheap. Symbolic confirmation: $g_i$ (no-lapse form)
and the $R_h$ constraint contain no $N$ anywhere, so $\partial g_i/\partial N
=0$ and $\partial(\dot R_h-c)/\partial N=0$ **exactly, by inspection**, not
merely expected. $D\equiv0$ is a mathematical identity here, not a numerical
coincidence requiring a re-run to fail or hold differently. WP3 is closed.

## 2. Both WP4b flags: confirmed real, not just plausible concerns

**Flag 1, confirmed as a code bug, not a prose slip.** Checked directly:
$F_\text{eq}(0)/F_0=1$, so my code's `(7/8)*4*Feq(A)/F0` returns $3.5$ at
$A=0$ and I used that number *as* $u_{e^\pm}/u_\gamma$. The correct ratio is
$3.5/2=1.75$ — photon carries $g=2$ in these units, not $g=1$ — confirmed by
direct recomputation. This is a factor-of-2 error in the actual
calculation, not merely in how I described it.

**Flag 2, confirmed as a real physics gap.** Checked directly: at
$T_\gamma=1$ MeV, my neutrino term used $T_\nu=(4/11)^{1/3}T_\gamma\approx
0.714\,T_\gamma$ — the post-annihilation ratio — when neutrinos at this
epoch haven't yet been affected by the (still-ongoing) annihilation and
physically share $T_\gamma$. Confirmed $g_*(1\text{ MeV})=10.75$ (correct)
vs. $6.86$ (what the unmodified machinery gives), matching the advisory's
numbers exactly.

## 3. Fixing both is not a simple patch — closure feedback changes the picture substantially

Implemented both fixes: the $e^\pm$ ratio corrected to $1.75$ at $A\to0$;
the neutrino term switched from sharing $T_\gamma$ (pre-annihilation) to the
standard $T_{\nu,0}(1+z)$ relation (post-annihilation), via a smooth
transition around $T\sim2$ MeV (a hard switch caused genuine numerical
breakdown in the closure ODE — the AQUAL source term $S(s)$ has $u_\text{hat}
(z)$ built into it, so a discontinuity there is not merely cosmetic; smoothing
it over roughly a decade in temperature resolved the instability).

**This surfaced something neither flag anticipated**: adding the corrected
$e^\pm$ term doesn't just locally correct the energy budget at BBN
temperatures — it changes the AQUAL closure's own source function $S(s)$ at
those epochs, which feeds back into $x(s)$ and hence the *entire* trajectory
the census machinery solves for. The correction is not a independent,
addable delta; it reshapes the same nonlinear system WP2/WP3's machinery
solves. Recomputing $E(z)/E_\text{std}$ with both fixes and this feedback
properly included (comparing against a standard reference built with the
*same* $e^\pm$/$\nu$ treatment, for a fair comparison) gives **a ratio of
roughly $0.19$–$0.27$ across the BBN-relevant temperature range** — not the
previously reported $0.93$–$0.96$. Checked for sensitivity to the arbitrary
transition-width choice (varying the switch temperature $1$–$5$ MeV): the
ratio moves between $0.22$ and $0.26$ at $T=0.7$ MeV — a real, if imprecise,
finding, not an artifact of one arbitrary choice, but not yet precise either.

## 4. Status — not finalizing a corrected table this round

**The previously reported $H/H_\text{std}\approx0.93$–$0.96$, $\Delta
N_\text{eff}\approx-0.7$, $Y_p\approx0.238$, and D/H figures are withdrawn** —
built on the two now-confirmed bugs, and the corrected calculation is
different enough (roughly a factor of 4 larger deficit) that recomputing
$Y_p$/D/H from it now, without settling the residual sensitivity to the
transition treatment, risks reporting a second unreliable number in the same
update. **Not done this round**: a properly converged, transition-width-
independent recalculation of $E(z)$ through the BBN epoch, and the resulting
abundance estimates. This is now flagged as the actual remaining content of
WP4b, not a finishing touch on an already-good table.

**What is solid**: both flags are confirmed real (not just plausible); the
qualitative conclusion — cdot-8's own census+closure genuinely expands slower
than standard BBN through this era, and by more than previously reported —
stands; QCD irrelevance, the frozen-vs-equilibrium distinction, and the
entropy-vs-energy finding for the temperature boost are all unaffected by
this correction and remain valid. Recommend: finish the transition-treatment
convergence check properly before this feeds the Foundation §6 item 6
decision input — a larger, not smaller, BBN-side deficit changes the
"borderline" framing the checklist used. The KATRIN clock remains the
program's most time-critical item; nothing in `cdot-7/` was touched.
