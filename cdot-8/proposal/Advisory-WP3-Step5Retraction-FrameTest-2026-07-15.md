# Advisory — WP3 Does Not Close Yet: The Closed-Action $g_i$ Is Frame-Implicit — Retraction of the Positive Verdict and Reordered Directives (for `cdot-8/WP3/`)

*2026-07-15. Advisory in response to
`cdot-8/WP3/Update-WP3-Step5ResolutionAssessment-2026-07-15.md`. The worker's §3
test executed here on the actual fitted trajectory
(`census_scheme_check.py`). Verdict up front: **the worker's caution was
correct and their proposed test surfaces something larger than either party
anticipated. Neither scheme's $g_\text{rad}(t)$, integrated with the real
$N(t)$ along the fitted trajectory, reproduces the physical
$(1+z)^4$ radiation dilution — not by a small margin, but by many orders of
magnitude. This means the "closed action" written in the coupling-audit round
carries a hidden $N=1$ assumption inside the kinematic identification of $g_i$
itself, not just in the scheme-freedom the invariance test located. WP3's
positive verdict is hereby retracted; a fourth advisor error is owned — the
"closes with positive verdict" language was premature — and WP4a's promotion
is held. The observable-level statement of §1 of my prior advisory
(scheme-independence of $E$, invoice, $F$, WP4a inputs) survives intact for
the reasons that advisory listed. But the $D$-is-gauge argument rests on a
closed action whose kinematic self-consistency has just failed a bounded
test, and the failure has to be understood before either "gauge" or "kill" is
the right characterization.***

---

## 1. What the worker's §3 test actually reveals

Running $\dot{\mathcal N}_\text{rad}/\mathcal N_\text{rad}=g_\text{rad}^X(t)$
on the real $N(t)$, anchored today, both schemes:

| $z$ | $d\ln\mathcal N_\text{rad}/ds$ (A) | (B) | target $-6$ | integrated ratio A | ratio B |
|---:|---:|---:|---:|---:|---:|
| $0$      | $-1.53$ | $-1.53$ | $-6.00$ | — | — |
| $1$      | $-1.93$ | $-0.39$ | $-6.00$ | $1.4\times10^{-1}$ | $9.2\times10^{-2}$ |
| $10$     | $-2.23$ | $-0.02$ | $-6.00$ | $1.7\times10^{-3}$ | $1.1\times10^{-4}$ |
| $100$    | $-2.25$ | $-5\times10^{-4}$ | $-6.00$ | $6.7\times10^{-6}$ | $1.6\times10^{-8}$ |
| $10^5$   | $-2.25$ | $\to0$ | $-6.00$ | $2.2\times10^{-13}$ | $\to0$ |

Scheme A saturates at $d\ln\mathcal N_\text{rad}/ds=-9/4$ (asymptotically to
the radiation fixed point where $\kappa\lambda x N=3/2$ minus the $-3/2$
weight-drift gives $0$… no, let me be precise: $g_\text{rad}^A/\dot s=(-3/2h+Nc/R_h)/\dot s$
$=(-3/2+\kappa\lambda xN)/((2/3)N)\to(3/2 N-3/2)/((2/3)N)\to9/4$ as
$N\to\infty$). Scheme B decays to zero faster. **Neither approaches $-6$
anywhere**; the target is not merely mismatched at a percent level or off by a
factor, it is off by factors of $10^{13}$ at high redshift. This is a genuine
kinematic failure of the closed action's $g_i$ against the physical
$(1+z)^4$ scaling, which is an independent, well-tested fact (BBN,
photon-baryon acoustic physics, and CMB thermodynamics all rely on it).

**Neither the worker nor I noticed this before because both scripts sidestep
it silently**: `budget_invoice.py` uses $\rho_\text{rad}\propto(1+z)^4$ from
the standard scaling; `scheme_species_test.py` (mine) does the same and
computes species weights as *Friedmann fractions* $w_i=u_i/u_\text{tot}$, not
by integrating the constraint's own $g_i$. The constraint's kinematics and the
scripts' physical inputs were never checked for mutual consistency; the audit
compared two versions of $D$ that both consumed the correct external
$\mathcal N_\text{rad}(z)$, so the audit did what it said (proved
$D$-decomposition depends on $g_i$'s internal $N$-placement), but *neither*
version's $D$ is definitively "the physical one" until the $g_i$ formula
itself is verified against the actual radiation history.

## 2. Advisor errors caught, cumulative count now four

- 07-13 numerical: $\dot s$-normalization in `backreaction_magnitude.py` —
  worker caught by independent construction.
- 07-13 numerical: sign flip in the reversed-grid quadrature — self-caught by
  the corrected round, then confirmed.
- 07-15 conceptual: "unique lapse convention" claim underjustified — worker
  caught by re-examining prior derivation.
- **07-15 conceptual, this round: "WP3 closes with positive verdict"
  premature** — the invariance theorem cited was *observable-level*, which is
  genuine (§1 of the prior advisory survives verbatim), but the framing "$D$
  is purely gauge, WP3 delivers what the proposal advertised" glossed over
  the assumption that both schemes' $\mathcal N_i(t)$ trajectories are the
  physical ones. That assumption is now bounded-testably wrong for both
  schemes.

The pattern is worth naming with more precision than "advisor error caught
by worker discipline": my error mode is *closing verdicts on partial
demonstrations* — the machinery I hold runs the specific test that was
asked, but the claim I frame from it exceeds the test's scope. The worker's
correction discipline consistently pulls the claim back to what the test
actually shows. This is a good division of labor but only if I stop
mistaking it for a bug in the worker's contribution and instead recognize
it as a bug in my scoping. Recording explicitly for K6 pattern library:
**advisor's verdict language must not exceed the specific test's
demonstrated scope; the worker's assessment role includes challenging
verdict framing, not just numerics.**

## 3. What survives, what does not

**Survives (unaffected by this finding):**
- $E(z)$, the fitted background, from the closure ODE.
- M7's invoice $\Omega_s(a)=E^2-\Omega_\text{census}$.
- The corrected quadrature $F(Q)$ against the $S_{M5}$-derived constraint.
- $\hat a_0(z)$, WP4a inputs, WP4b inputs — all data-facing predictions.
- The scheme-dependence result *within* the class of $g_i$ formulas that
  reduce to WP2 at $N=1$: order-unity swing of $D$ between schemes A and B,
  demonstrated numerically.
- The physical soundness of cdot-8 as a data-confronting theory in its
  current form — nothing here changes any observable.

**Does not survive as-stated:**
- "$D$ is purely gauge, full stop." The scheme A/B swing may still be
  gauge, but proving it requires either scheme's $g_i$ to be reconciled
  with $(1+z)^4$ physics first — otherwise "$D_A$ and $D_B$ are both wrong"
  is at least a possible reading, and the audit hasn't yet distinguished
  "both are equivalent gauge choices for the correct $\mathcal N_i$" from
  "both are subtly wrong versions of a formula that hasn't been written."
- "WP3 closes." The bookkeeping-consistency portion is not done.

## 4. Diagnosis: a hidden frame assumption inside $g_i$

The most likely explanation, from the $-9/4$ asymptote (scheme A): the
formula $g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+Nc/R_h$ was inherited from
WP2's original $N=1$-gauge statement, where the LHS was $\dot{\mathcal
N}_i/\mathcal N_i$ **on the coordinate clock $t$**. Promoting to general
$N$ replaced $\dot c/c$ with $\dot c/c$ (a log-derivative on the same clock
throughout, correctly unchanged) and $c/R_h$ with $Nc/R_h$ (adding one lapse
factor). But the LHS itself became $\dot{\mathcal N}/\mathcal N$ **on
whichever clock $\mathcal N$ is a density function of** — and the census
$\mathcal N$ is defined via a foliation integral, i.e. on the *matter clock*
$\hat\tau$ if $\mathcal N$ is what atoms see, or on $t$ if it's a
coordinate-frame count. WP2 conflated these at $N=1$ (they coincide there);
the two-clocks advisory forced them apart for the *background* but the
census sector was never revisited. **The $g_i$ formula is missing a
$dt/d\hat\tau=N^{-1}$ factor somewhere, or equivalently the LHS is a
$t$-derivative when it should be a $\hat\tau$-derivative, or vice versa.**
Neither scheme (A or B) can fix this alone; both are variations within a
frame-implicit family.

**The bounded, decisive follow-up test** (assigning to the worker per
protocol, but the setup is small enough that either of us can do it): write
the census evolution equation *unambiguously* by starting from $\mathcal
N_i(t)\equiv\int_{\Sigma_t\cap\text{horizon}}(E_i/E_P^\text{coord})$ (M4's
own definition), taking a covariant $t$-derivative with $N(t)$ and $R_h(t)$
both explicit, and comparing the result to $g_i^A$ and $g_i^B$. Whichever
one matches (if either) is the correct closed-action form; if neither, the
correct form is the third one this exercise produces, and both scheme A and
scheme B were exercises in variations *outside* the physical class.

## 5. Directives, reordered

1. **Retract WP3's "closes positive" verdict** from the last advisory.
   Current status: **WP3 in progress; $D$'s status open pending §4's frame
   test**; observable-level scheme-invariance of $E,F,\hat a_0,\theta_*,\text{BBN}$
   confirmed and standing.
2. **Hold WP4a promotion.** The Stage-1 acoustic scale check is
   observably robust, but promoting it *while WP3 remains open* would send
   the wrong signal about the program's state to any consolidator or
   downstream reader. Queue WP4a immediately after §4's frame test
   resolves, not before.
3. **Run the frame test of §4.** Worker's call whether to run it themselves
   or hand it back for advisor machinery; either party can do it. The
   deliverable is a $g_i$ formula whose integration against the real $N(t)$
   reproduces $(1+z)^4$ for radiation and $(1+z)^3$ for cold matter
   (already known to hold automatically since $p^\text{sp}_\text{cold}=\tfrac52$
   makes $g_\text{cold}=Nc/R_h$ and the ambiguity vanishes for matter).
4. **Re-audit the scheme freedom** in the corrected $g_i$ once §4 is done.
   The A-vs-B swing may collapse to zero in the correct formulation (making
   $D$-decomposition genuinely unique, honest positive verdict), or it may
   persist as one gauge freedom within a corrected class (making $D$ gauge
   for the honest reason), or the corrected formulation may itself close
   the audit differently. All three outcomes route through the author.
5. **WP2 discharge held**, in full — including the matter sector, since
   the coupled-audit framing of "WP2 discharged by incorporation" was
   itself a downstream consequence of the closed action being
   frame-consistent.
6. **Consolidation log**: record all four advisor errors as a compact
   entry, with the K6 pattern updates (closed-form-check rule; sign-flip
   isn't a general iteration shortcut; verdict-scoping rule). The worker's
   K6 discipline is now provably load-bearing; the consolidation log
   should reflect that as a formal K6 update, not scattered notes.
7. **The KATRIN clock**: unchanged, still the program's most time-critical
   item. The frame test of §4 is bounded and should not delay it.

## 6. Protocol note

This is the correct outcome for the assessment round: the worker held on
insufficient evidence, ran a bounded test that the advisor's positive
framing had elided, and the test showed the framing was premature. That is
the assessment-round protocol working correctly. What did not work: my
verdict framing exceeded what my test demonstrated. The fix is not on the
worker's side (their §3 was exactly right); it is on mine, and the K6
verdict-scoping rule adopted this round is the concrete response.

The program's advertised bidirectional error-catching just caught its
fourth advisor error — a scoping error, not a numerical one — via the
worker holding at exactly the point where the numerics needed one more
independent confrontation. WP3 will close, but on the honest schedule §4
opens, not on the schedule of the last advisory's framing.

## Companion

- `census_scheme_check.py` — the worker's §3 test, run to completion:
  both schemes' $g_\text{rad}$ integrated against the real $N(t)$, compared
  to $(1+z)^4$, orders-of-magnitude failure demonstrated.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-Step5Retraction-FrameTest-2026-07-15.md`.
