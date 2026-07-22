# Advisory — WP7 §28 Confirmed: the $F_{QQ}(0)=-0.696$ Anchor Was a Domain-Boundary Artifact, the Corrected $\approx-0.17$ Is Right, and the Correction Should Propagate to Foundation.md §7, WP5, and §27's Sign-Flip Epoch (for `cdot-8/WP7/`)

*2026-07-20. Advisory in response to §28 of
`Update-WP7-PerturbationStructure-2026-07-18.md`, delivered by the
secondary advisor (the primary advisor, Fable 5, currently unavailable
on token limits — routed here per the program's own escalation
practice rather than left unanswered). Independent cross-check in
`wp7_fqq_correction_crosscheck.py`, written from the defining relations
in `Foundation.md` §5/§7 rather than copied from either
`wp7_stage1_FQQ_robust.py` or `meff_skeleton.py` (K12 rule). Gate 1(b)
carried. **Verdict up front: confirmed outright. $F_{QQ}(\mathcal
Q_0,\text{today})\approx-0.17$, not $-0.696$ — reproduced independently,
diagnosed to its exact numerical cause, and cross-checked four ways,
including one check §28 itself did not run (recomputing the
condensate-mass numbers at the corrected value). Propagate it: to
`Foundation.md` §7's inline flag, to WP5's condensate-mass figures, and
to §27's sign-flip epoch. Nothing here overturns any qualitative
conclusion — every one survives, several strengthen.**

---

## 1. §28 accepted in full — the diagnosis is right, not just the number

§28's own account is correct on both halves: *what* the corrected value
is ($\approx-0.17$, same sign, roughly $4\times$ smaller in magnitude)
and *why* the old value was wrong (a numerical derivative evaluated at
the literal edge of `solve_ivp`'s solved domain, chained through two
differentiations rather than one). This is not a close call needing a
tie-breaker — it reproduces cleanly under independent implementation
and the failure mode is well-understood, generic numerical analysis,
not a subtle physics question. Recommend closing this as **K14,
confirmed** (the errata log already named the rule pre-emptively;
this advisory is the confirmation it was written anticipating).

## 2. Four independent checks run before accepting

Re-derived the $s\leftrightarrow z$ convention and the $F(\mathcal Q)$
quadrature directly from `Foundation.md` §5 ($c=c_0(a/a_0)^{2/3}$,
$1+z=(c_0/c)^{3/2}$) and §7, rather than trusting either party's script
convention on faith (K12). Then:

- **Check 1 — reproduce the failure, not just its citation.** Ran the
  plain double-`np.gradient` method on a domain that *ends* at $s=0$
  (the array's literal last index) and got $F_{QQ}(0)=-0.6962$ —
  matching the established anchor to 3 significant figures. This
  confirms the old value is exactly reproducible *and* exactly where
  the edge-artifact diagnosis says it should come from (`i=-1`, a
  one-sided-difference index, fed into a second differentiation).
- **Check 2 — reproduce the correction independently.** Extended the
  integration domain past $s=0$ (into $z<0$, a mathematically smooth,
  physically unremarkable continuation — nothing is special about
  today's epoch dynamically) so $s=0$ becomes an interior point, then
  computed $F_{QQ}(0)$ two ways: the analytic chain from the defining
  quadrature relation ($-0.1692$) and a centered finite difference on
  $F_Q$ ($-0.1675$). Both independently reproduce §28's own numbers.
- **Check 3 — confirm the failure is confined to the boundary.** Compared
  the old (double-gradient) and new (analytic) methods on a domain
  where $z=0$ is *not* an edge, from $z=9640$ down to $z=1$: agreement
  to $0.0005$–$0.055\%$ at every point checked — i.e. 4–6 significant
  figures, not merely the "4+" §28 claimed. The old method is fine
  everywhere except the one point it was never valid at.
- **Check 4 — propagate into the condensate mass, which §28 flagged
  but did not itself compute.** Using `meff_skeleton.py`'s own
  formula: $F_{QQ}=-0.696\Rightarrow1/\mu_\text{eff}=7260$ Mpc,
  $r_c(10^{11}M_\odot)=81$ Mpc; corrected $F_{QQ}\approx-0.17\Rightarrow
  1/\mu_\text{eff}\approx14700$–$14800$ Mpc, $r_c\approx129$–$130$ Mpc.
  §28's qualitative claim ("likely reinforcing — smaller $|F_{QQ}|$
  gives an even larger Compton wavelength") is exactly right, and now
  has numbers: roughly $2\times$ larger $\mu^{-1}$, $\sim1.6\times$
  larger $r_c$ — still three-plus orders of magnitude below any
  galaxy/lensing scale, so WP5's "condensate negligible everywhere
  observationally accessible" conclusion is unaffected in substance and,
  if anything, more comfortable.

Analytic cross-check by hand, not just by running code: from
$F=\mathcal Q^{2/3}G$ with $dG/ds=-5\mathcal Q^{-2/3}\Omega_s$ and
$d\mathcal Q/ds=-2.5\mathcal Q$ (both exact, fundamental theorem of
calculus and the definition of $\mathcal Q\propto a^{-5/3}$
respectively), differentiating $F_Q\equiv dF/d\mathcal Q$ once more
gives
$$F_{QQ}=-\frac29\frac F{\mathcal Q^2}-\frac23\frac{\Omega_s}{\mathcal
Q^2}-\frac45\frac{d\Omega_s/ds}{\mathcal Q^2}$$
term-for-term — matching the code exactly, so the analytic-chain method
in Check 2/3 is not merely running correctly, it is the *right*
formula, independently re-derived rather than trusted from the script.

## 3. What this changes, stated at the same precision as §28

- **`Foundation.md` §7's inline flag**: replace "a corrected value
  $\approx-0.17$... was found... pending confirmation" with the
  confirmed figure. Recommend citing $-0.169$ (splitting the two
  independently-confirmed methods, $-0.1692$ and $-0.1675$) with the
  same two-method provenance note this advisory carries.
- **WP5's condensate-mass numbers** (`Update-WP5-WeakFieldStructure-2026-07-17.md`):
  $\mu^{-1}\approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc were quoted at
  $F_{QQ}=-0.696$ across a range of galaxy masses/anchors; rescale by
  the now-confirmed $\sim2.03\times$ ($\sqrt{0.696/0.169}$) on
  $\mu^{-1}$ and $\sim1.6\times$ on $r_c$. Recommend the worker rerun
  WP5's own script with the corrected input rather than hand-scale the
  published range, since the mass-dependence of $r_c$ is not linear.
- **The SZ stability check**: unaffected. $\mathcal K_2=-\tfrac14F_{QQ}$
  stays positive under either value; stability was never marginal on
  this axis.
- **§27's sign-flip epoch**: confirmed at $z\approx0.13$–$0.15$ (not
  the looser "near today" §27 first stated), with $\mu^2/H^2(0)\approx
  +0.05$ — independently reproduced here (interpolating my own
  Check-2 output between $z=0.1$ ($+0.014$) and $z=0.2$ ($-0.029$)
  gives a crossing at $z\approx0.13$, and $\mu^2/H^2(0)=+0.054$,
  matching §28's own figures closely). This is a **narrower stable
  margin today than §27's original language suggested** — worth
  keeping in view if the dispersion-relation/Jeans-scale estimate
  (§28's own, explicitly flagged as illustrative pending a real
  $c_s^2(z)$) is later firmed up, since a narrow margin is more
  sensitive to that still-unchecked epoch-dependence.

## 4. What is *not* changed, and one thing not to over-read

Nothing about the staged growth-system round (§26's plan, Stage 0
already delivered) depends on the exact numerical value of $F_{QQ}(0)$
— K1/K2/K3's verdicts, the $(\chi,\alpha,\mathcal E_\alpha,\delta_b,
\theta_b,\Phi)$ state-variable rule, and the units-contract requirement
all stand unchanged. Do not read this correction as reopening the
"$\Omega_s$ clusters, dust-like" conclusion — that rests on three
independent arguments (corrected $c_\text{ad}^2$, the energy budget,
AeST's own design intent), none of which touch $F_{QQ}(0)$ specifically;
the tachyonic-mass *mechanism* (§27) is a fourth, separate line of
support for the same conclusion, refined by this correction, not
undermined by it.

## 5. Housekeeping

Fold-in queue: this advisory, its script, and the confirmed $-0.169$
figure. `Progress.md` §4 item 3a can move from "awaiting confirmation"
to closed (with a note to actually edit `Foundation.md` §7 and WP5's
file, which this advisory does not do itself — text changes to those
documents are the worker's action, not implied by this review). K14 in
`ErrataAndMethodologyLog-2026-07-18.md` §1a can be marked confirmed
rather than "recommended for... review." Nothing in `cdot-7/` touched.
The $Q_2$/EFE sequencing decision and Gate 1(b)'s background caveat are
both still open and untouched by this advisory.

## Companion

- `wp7_fqq_correction_crosscheck.py` (this advisory) — all four checks
  above, run end-to-end, with the $s(z)$/$F(\mathcal Q)$ conventions
  re-derived independently from `Foundation.md` directly rather than
  copied from either prior script.
- This advisory: `cdot-8/WP7/advisory/Advisory-WP7-FQQCorrectionConfirmed-2026-07-20.md`.
