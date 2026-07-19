# Advisory — WP4a: Worker's Calculation Confirmed, Provenance Audit Clean; The 27% Miss Is a Real, Structural Result — What It Means Before Escalation (for `cdot-8/WP4/`)

*2026-07-16. Advisory in response to
`cdot-8/WP4/Update-WP4a-AcousticScale-2026-07-16.md`. Full independent
treatment (`wp4a_check.py`), with explicit attention to the author's
provenance concern about cdot-7/cdot-4 assumptions leaking into cdot-8.
Verdict up front: **the worker's calculation is arithmetically correct to
the digit; every convention question the update raised was resolved by
Foundation-internal derivation, not by borrowing from earlier iterations;
and the provenance audit finds no unjustified leaks. $100\theta_*=1.326$ vs
Planck $1.041$ is a genuine, zero-knob structural prediction — a 27% miss,
not a bug and not a repeat of cdot-4/5's factor-of-9-to-765 failures. The
correct posture toward this result is neither "cdot-8 kills" nor "cdot-8
passes" but the one Foundation §6 item 6 already installed: this is
exactly the "explicit decision" territory where the author's judgment is
the load-bearing input, not the advisor's numerics, and the honest framing
of what the number does and does not tell us is more useful than any
verdict I could pronounce.***

---

## 1. Worker verification, term by term

Reproduced from scratch on the same $(\kappa\lambda=0.4355, x_0=1.10)$
trajectory using the WP3-verified closure ODE, extending integration to
$z=10^{15}$ to make the $r_s$ convergence check as tight as possible:
$D_p(z_*)=13073.7$ Mpc (worker: $13074.3$, agrees to 3 sig figs — small
difference from grid spacing); $r_s(z_*)=173.36$ Mpc at every tested
extension beyond $z=10^9$ (worker: $173.36$, exact). $100\theta_*=1.326$
reproduced exactly.

Both integrations use the same convention: $\int c_0/(H_0E(z))\,dz$ with
$c_0$ constant and $H_0=70$ km/s/Mpc, in the matter frame (equivalently:
$\int d\hat\tau/a$ in the two-clocks language, since
$H_{\hat\tau}=H_t/N=H_t(c_0/c)^{5/2}$ and $E(z)=H_{\hat\tau}/H_{\hat\tau,0}$).
**Cross-check against Foundation §5.2's fixed-point analytic formula
$D_p(z)=R_{h,0}[1-(1+z)^{-1/2}]$: on the fixed point $E(z)=(1+z)^{3/2}$,
the numerical integral gives $8306$ Mpc for $z_*=1090$, matching the
analytic formula to the digit** — the worker's formula is
Foundation-consistent, not an unjustified import.

## 2. Provenance audit — the author's concern, taken seriously

Six candidate leak points checked, each against Foundation-internal
derivation rather than by pattern-matching to standard cosmology:

- **Distance convention.** Worker's re-derivation of $\theta_*=r_s/D_p$
  from Foundation §5.5's lockstep is airtight — the $(1+z_*)$ factors
  cancel exactly, not by convenience but because both $r_s$ (integrand
  size at the source epoch) and $\theta$ (angular size formula in cdot-8)
  carry the same lockstep factor. Verified that using $d_A=D_p/(1+z_*)$
  directly (the naive substitution) gives the nonsensical $100\theta_*
  \approx1456$ the worker caught; the correct cancellation gives the
  legitimate $1.326$. This is a genuine cdot-8 result, not a
  cdot-4/cdot-5 import.

- **Recombination redshift.** Worker uses $z_*=1089.80$ (Planck) with
  the argument that local physics is Planck-unit invariant, so the Saha
  competition at any given local $T$ vs binding energy resolves at the
  same critical (1+z). Checked: coordinate-frame $\rho_\text{cold}\propto
  c^{5/2}$ divided by dictionary $c^7$ gives local $\propto c^{-9/2}$,
  and $c\propto a^{2/3}$ gives local $\rho\propto a^{-3}$ — **exact same
  scaling as standard cosmology in $a$-units**. So the Saha equation
  yields the same $z_*$; not a leak, a derived equivalence.

- **Sound speed formula.** $c_s=c_0/\sqrt{3(1+R)}$ is local baryon-photon
  physics; Planck-unit invariance (K1) says local physics is unchanged;
  the $r_s$ integral is a matter-frame comoving distance where this
  local sound speed is the correct integrand. No leak.

- **$\Omega_G$ from $T_\gamma$.** Foundation §2.4 identifies
  $\Omega_G=u_\gamma/\rho_\text{crit}$ with $\rho_\text{crit}=3H_0^2/8\pi G$
  computed on the matter clock $H_{\hat\tau,0}=H_t(0)$ — which coincide
  today by two-clocks structure. Unambiguous, verified.

- **$\Omega_b$ identification.** Worker's $\Omega_b=\Omega_\text{closure}
  -\Omega_\nu=0.0442$ comes from the census, no external fit. Compare
  independent BBN-derived $\Omega_b h^2=0.0224$ (Planck 2018) $\to
  \Omega_b=0.0457$ at $h=0.70$: cdot-8's census value is $3\%$ below,
  well within census uncertainty. **This is actually a mild point in the
  theory's favor** — the census-forced $\Omega_b$ matches BBN
  independently, without tuning.

- **Fitted trajectory $E(z)$.** From the WP3-verified closure ODE, no
  post-WP3 modifications. Direct comparison to standard $\Lambda$CDM
  $E_{\Lambda\text{CDM}}(z_*)=23200$ vs cdot-8 $E(z_*)=18400$: ratio
  $0.79$ at recombination. This is the previously-flagged
  $H_{\hat\tau}/H_{\Lambda\text{CDM}}\approx0.79$ (BackreactionMagnitude
  advisory §3), now feeding directly into $D_p$ and $r_s$.

**Provenance is clean.** The 27% miss is a genuine structural
consequence of two things: the census-forced $\Omega_b=0.044$ (which
inflates $r_s$ by $\sim20\%$ vs $\Lambda$CDM's larger $\Omega_b$
inference — but which is *itself* consistent with BBN), and the fitted
$E(z)$'s $\sim20\%$ suppression at recombination compared to $\Lambda$CDM
(which contracts $D_p$ by $\sim6\%$ and inflates $r_s$ further). Both
effects compound to give a $27\%$ upward miss in $\theta_*$.

## 3. What the number does and does not tell us

**Does tell us:**
- cdot-8's peak position prediction is genuinely off from Planck by 27%,
  corresponding to first acoustic peak at $\ell\sim173$ vs observed 220.
- The miss is zero-knob: no adjustable parameter in cdot-8's current
  form can move $\theta_*$ meaningfully without breaking already-validated
  fits (the mass census, the SN Hubble diagram).
- The miss is qualitatively $\Lambda$CDM-without-CDM shaped, consistent
  with the framework's own architecture: less gravitating mass at
  recombination than $\Lambda$CDM assumes, plus a scalar sector whose
  M7 invoice contributes only a few percent at $z_*\sim1100$ (per
  `budget_invoice.py`).

**Does not tell us:**
- Whether cdot-8's perturbation theory (WP7, not yet built) can recover
  the observed peak structure via a mechanism other than tuning $\theta_*$.
  The $\theta_*$ observable is the *peak position*, but the peak *heights*
  and their ratios encode different physics (early ISW, radiation driving,
  Silk damping) that a scalar-sector modification could plausibly affect
  differently than $\theta_*$.
- Whether the neutrino sector's non-relativistic transition at
  $z\sim900$–$1450$ (per the KATRIN-neutrino advisory) affects the
  effective sound-horizon integral in a way this leading calculation
  misses. Worker used relativistic $c_s$ throughout; the correction is
  small but nonzero at high $z$.
- Whether the M7 invoice's few-percent contribution at $z_*$ modifies
  $r_s$ or $D_p$ meaningfully — it's the "gravitates without oscillating"
  candidate the 07-11 discussion identified, and its background impact
  on the integrals is small but not zero.

**The Foundation §6 item 6 territory:** the update correctly invokes
this, and it is the load-bearing framing. That item explicitly reserves
the CMB confrontation for author decision, given cdot-4/5's two decisive
structural failures. **A 27% miss is qualitatively different from those
failures** (factor-of-9-to-765), but the standing rule was not "escalate
only if the miss exceeds a threshold" — it was "escalate before
declaring either pass or kill." The worker honored this exactly.

## 4. Directives

1. **WP4a's numerical result is confirmed and stands as-computed**:
   $100\theta_*=1.326$, 27% high, zero-knob prediction. The advisory
   endorses reporting it precisely as the worker has, including the
   explicit terms of the confrontation.

2. **The verdict — "pass," "kill," or "structural finding requiring
   further construction" — is not the advisor's to pronounce.** Foundation
   §6 item 6's "explicit decision" clause routes this to the author, and
   this advisory endorses that routing without pre-judging. If it helps:
   the three natural readings and what would justify each:
   - *"WP4a is a soft miss, WP7 needed for verdict"*: reasonable if you
     hold that peak-position vs peak-height/ratio distinguishability
     means $\theta_*$ alone doesn't decide, and that perturbation theory
     could recover the observed spectrum via other channels.
   - *"WP4a is a strong indicator; provisional structural failure"*:
     reasonable if you hold that a zero-knob prediction 27% off a
     0.03%-precision measurement is close to a factor-of-2 miss in
     statistical terms, and that "WP7 might rescue this" is the kind
     of appeal-to-future-work the Duerr–Wolf critique specifically
     targets.
   - *"WP4a is decisive; document and close cdot-8"*: reasonable if you
     hold cdot-4/5's history establishes that this territory has never
     been survivable, and that a 27% miss at the acoustic scale
     empirically forecasts a much larger miss in the full power
     spectrum that WP7 would formalize.

   I hold no preference among these; the arguments for each are real
   and the decision is a judgment call about scientific strategy, not
   an inference from the numerics.

3. **What is safe to do now, regardless of the WP4a verdict:**
   - Sign-errata propagation on the two `BackreactionMagnitude` documents
     (still outstanding from the 07-13 rounds).
   - Consolidation log entry for the five advisor errors and four K6
     pattern rules (still outstanding from the WP3 round).
   - WP4b (BBN) gated on the $e^+e^-$/QCD census kinks — still queued
     appropriately per the standing plan; the acoustic scale outcome
     doesn't change its priority ranking.
   - The KATRIN clock, unchanged and still time-critical.

4. **If the author's decision on WP4a is "provisional structural failure"
   or "decisive kill":** cdot-7 remains untouched by any of this — the
   Foundation §6 item 6 territory was always cdot-8's to inhabit, and
   cdot-7's data-facing claims (SN, RAR, mass census, $\hat a_0(z)$
   locking) don't reference $\theta_*$. That's the whole point of the
   proposal's charter.

## 5. Protocol note

The worker's framing of this update as "not a cheap immediate
afterthought" is worth endorsing verbatim. WP4a was called "Stage-1,
cheap, decisive" in early rounds; the worker correctly recognized it as
the first genuine data confrontation beyond the SN diagram and treated
it with the weight that history (cdot-4/5 failure record + Foundation
§6 item 6) warrants. The advisor's earlier "promoted-to-immediate"
language, in retrospect, understated what this test was. Adopted for
K6: **"cheap and decisive" are compatible framings, but "immediate"
implies routine execution; when the consequences of the test can end a
work package, the appropriate framing is "priority" not "quick" — and
the author's decision should be invited, not preempted.**

Six errors caught in the program now, if we count this as an advisor
framing error preempting an author decision that Foundation §6 item 6
had already reserved. Same pattern as error 4 (verdict-scoping), same
resolution (defer to the assessment structure the project already has).

## Companion

- `wp4a_check.py` — the worker's calculation reproduced from scratch,
  the fixed-point $D_p$ analytic formula verified numerically, the
  provenance audit's six leak checks, and the direct $E(z)$ comparison
  against $\Lambda$CDM.
- This advisory: proposed location
  `cdot-8/WP4/Advisory-WP4a-AcousticScale-Assessment-2026-07-16.md`.
