# Session Log — cdot-8/WP4b (2026-07-16)

*New work package, new file. WP4a's numerical result stands (confirmed
twice, verdict routed to author per Foundation §6 item 6); WP4b proceeds in
parallel per the standing queue, gated on the e+e-/QCD census kinks per
Foundation §6 item 5(a).*

*(Note: this file was accidentally overwritten mid-session by a misplaced
upload and rewritten from memory below on 2026-07-17; the substance of
Entry 1 is reconstructed as faithfully as possible from the corresponding
Update document and the conversation record, not re-run from scratch.)*

---

## Entry 1 — The e+e- census kink derived; leading-order BBN estimate (2026-07-16)

**Prompt (verbatim):**
> Ok. At some point we need to make the plot of the power spectrum showing
> where our model lies with respect to the observations. It would be good at
> that point if we could calculate the standard lCDM models fit as well with
> the same machinery so that we can show that we can reproduce it. For now,
> continue with WP4.

**Summary of work performed:**

1. **Confirmed the QCD transition is irrelevant to BBN** — more than two
   orders of magnitude in temperature earlier, already frozen into standard
   $g_*$ bookkeeping by the time BBN's physics runs.

2. **Attempted the e+e- census kink twice — first attempt wrong, caught
   before use.** Following the same massive-FD structure that correctly
   describes neutrinos ($m\propto c^{1/2}$, conserved coordinate wavenumber)
   gave $u_{e^\pm}/u_\gamma$ *growing* with $A=m_e/T$ instead of
   Boltzmann-suppressing — because that structure assumes a frozen, decoupled
   distribution (correct for neutrinos, which free-stream after decoupling)
   and is wrong for $e^\pm$, which stay in full thermal+chemical equilibrium
   and genuinely annihilate (comoving number not conserved). Caught by the
   sign of the numerical trend, not asserted correct because it resembled an
   established pattern.

3. **Second attempt believed correct at the time**: the true equilibrium FD
   energy density, energy (not momentum) in the exponent — verified it
   reduces to the relativistic limit and Boltzmann-suppresses properly.
   (Later found, 2026-07-17 round: the relativistic-limit ratio was itself
   miscomputed by a factor of 2 — see Entry 2.)

4. **Separately checked the already-used photon-temperature boost
   $(4/11)^{1/3}$** against this framework's own stated "energy-conserving
   conversions" principle — found naive coordinate-energy conservation gives
   the wrong exponent, $(11/4)^{1/4}$ not $(11/4)^{1/3}$; entropy
   conservation (a distinct, and for bulk many-body conversions the correct,
   principle) is needed and does give the standard, already-used result.
   This finding is unaffected by Entry 2's correction.

5. **Computed a resulting $H(z)$ deficit at BBN**: $H_{\hat\tau}/H_\text{SBBN}
   \approx0.93$–$0.96$ across the relevant temperature range, converted to
   an effective $\Delta N_\text{eff}\approx-0.7$, with leading-order
   abundance estimates $Y_p\approx0.238$, D/H$\approx2.47\times10^{-5}$.
   **These numbers were withdrawn in Entry 2** after the underlying $e^\pm$
   ratio and the neutrino-temperature treatment were both found to be wrong.

**Files produced:** `Update-WP4b-BBN-2026-07-16.md`; this entry (rewritten
2026-07-17 after an accidental overwrite of the original).

**Status at the time**: presented as a leading-order result, not a full BBN
confrontation, with two genuine conceptual errors already caught and fixed
in-round (frozen vs. equilibrium distribution; energy vs. entropy
conservation for the temperature boost). A third and fourth issue were found
in the following round's advisory review — see Entry 2.

---

## Entry 2 — Advisor review finds two further confirmed bugs; correction requires more than a patch (2026-07-16/17)

**Prompt (verbatim; advisor round):**
> WP4a and WP4b are now done. Any advice before we proceed?

(Reference: `Advisory-WP4ab-ReviewAndPreDecisionChecklist-2026-07-16.md` +
`wp4b_check.py` — advisor endorsed WP4a's closure with two adopted
refinements; found WP4b **not done**: Flag 1, the $u_{e^\pm}/u_\gamma\to3.5$
claim is a factor-2 slip (correct ratio $1.75$, since $3.5$ is the
$g_*$-units contribution, not the ratio to photon); Flag 2,
potentially table-invalidating — the census machinery's neutrino term
carries the post-annihilation $T_\nu=(4/11)^{1/3}T_\gamma$ at all $z$,
wrong in WP4b's own window where $T\gtrsim m_e$ requires $T_\nu=T_\gamma$;
Flag 3, D/H provenance unstated. Also flagged WP3 as formally still open
pending a re-confirmation of $D\equiv0$, and issued a pre-decision checklist
routing the combined WP4a+WP4b picture to the author's Foundation §6 item 6
decision.)

**Summary of work performed:**

1. **Confirmed Flag 1 directly**: my own code's `(7/8)*4*Feq(A)/F0` returns
   $3.5$ at $A=0$ and this value was used *as* $u_{e^\pm}/u_\gamma$ — the
   correct ratio is $3.5/2=1.75$ (photon carries $g=2$, not $g=1$, in these
   units). A genuine factor-of-2 bug in the code, not merely in the prose
   describing it.

2. **Confirmed Flag 2 directly**: at $T_\gamma=1$ MeV, the neutrino term
   assumed $T_\nu\approx0.714\,T_\gamma$ (the post-annihilation ratio) where
   physically $T_\nu=T_\gamma$ at this epoch. Reproduced the advisory's
   $g_*(1\text{ MeV})=10.75$ (correct) vs. $6.86$ (machinery) exactly.

3. **Fixed both and recomputed** — found the correction is not a simple
   local patch: the $e^\pm$ term feeds into the AQUAL closure's own source
   function, which reshapes the whole solved trajectory, not just the BBN-
   epoch energy budget locally. A hard switch between the pre/post neutrino
   treatments caused genuine numerical breakdown in the closure ODE;
   smoothed over roughly a decade in temperature to resolve it.

4. **Recomputed $E(z)/E_\text{std}$ with both fixes**, comparing against a
   standard reference built with the same $e^\pm$/$\nu$ treatment for
   fairness: **ratio $\approx0.19$–$0.27$ across the BBN range**, not the
   previously reported $0.93$–$0.96$ — roughly four times the previously
   reported deficit. Checked sensitivity to the arbitrary transition-width
   choice (switch temperature $1$–$5$ MeV): ratio moves between $0.22$ and
   $0.26$ at $T=0.7$ MeV — a real finding, not a one-choice artifact, but not
   yet a converged, precise number either.

5. **Closed the WP3 checklist item cheaply**: symbolic confirmation that
   $\partial g_i/\partial N=0$ and $\partial(\dot R_h-c)/\partial N=0$
   exactly (both expressions contain no $N$ at all) — $D\equiv0$ is an
   identity, not a numerical coincidence needing an iterative re-run. WP3
   formally closed.

**Files produced:** `Update-WP4b-BBN-Correction-2026-07-16.md`, this entry
(session log rewritten in full after the original file was accidentally
overwritten by a misplaced upload — reconstructed from the conversation
record and the corresponding Update documents).

**Status: WP4b's previously reported numbers are withdrawn.** Both flags
were real, confirmed bugs, not just plausible concerns; fixing them properly
surfaced a larger, closure-feedback-driven correction than either flag
predicted alone. Not yet finalized: a properly converged (transition-width-
independent) recalculation and the resulting abundance estimates — this is
now the actual remaining content of WP4b. What stands unaffected: QCD
irrelevance, the frozen-vs-equilibrium distinction, and the entropy-vs-energy
finding for the photon-temperature boost. The KATRIN clock remains the
program's most time-critical item; nothing in `cdot-7/` was touched.

---

## Entry 3 — Converged result: much larger deficit than either prior estimate, verified as far as possible, escalated (2026-07-17)

**Prompt (verbatim):**
> Please proceed with the calculations.

**Summary of work performed:**

1. **Removed the ad hoc transition width entirely** by solving photon+$e^\pm$
   entropy conservation directly for $T_\gamma(a)$, rather than assuming
   $T_\gamma(z)=T_{\gamma,0}(1+z)$ throughout and smoothing over an arbitrary
   switch. Built the entropy density from the same equilibrium energy and
   pressure integrals, verified at $A=0$ to reproduce $s_{e^\pm}/s_\gamma=
   1.75$ (matching the energy ratio, as required in the relativistic limit).

2. **Found a third issue this way**: $T_\gamma(z)=T_{\gamma,0}(1+z)$ — used
   throughout this session's BBN-era work — is only exact *after* the
   $e^\pm$ transition completes. The corrected, entropy-conserving relation
   gives redshifts up to $\sim40\%$ higher than the naive relation at the
   deep-past end of the transition, converging to the naive relation by
   $T\sim0.02$ MeV — reproducing the standard $(11/4)^{1/3}$ boost from
   first principles rather than citing it.

3. **Verified before trusting it**: (a) regression check against WP4a — with
   all corrections applied, $E(z)$ at recombination-era redshifts
   reproduces the previously-validated numbers exactly, unchanged; (b)
   trajectory sanity — $x(s)$ at BBN redshifts sits properly near the
   radiation fixed point, no saturation or runaway; (c) stability — the
   ratio holds at $0.27$–$0.28$ across nearly two decades in temperature,
   with no residual dependence on modeling choices (genuine convergence,
   unlike the previous round's $0.19$–$0.27$ spread).

4. **Result: $H_{\hat\tau}/H_\text{SBBN}\approx0.276$, effective $\Delta
   N_\text{eff}\approx-5.7$** — roughly eight times the previously-withdrawn
   estimate, and far outside where standard linear sensitivity coefficients
   for $Y_p$/D/H mean anything. Deliberately did not compute abundance
   numbers from linear extrapolation at this magnitude — would manufacture
   false precision, not a real estimate.

**Files produced:** `Update-WP4b-Converged-2026-07-17.md`, this entry.

**Status: escalating, not finalizing.** No bug found in this calculation
after genuine effort to find one (regression check, trajectory sanity, and
first-principles reproduction of the standard boost factor are all clean),
but a result this severe, arriving after two already-confirmed bugs in
earlier rounds, warrants independent re-derivation before being treated as
settled — the same posture this program has used throughout. If it holds,
BBN is no longer "borderline" as framed earlier, but a severe, independent
tension, larger than the acoustic-scale miss. WP4a is unaffected (confirmed
by the regression check). The KATRIN clock remains the program's most
time-critical item; nothing in `cdot-7/` was touched.

---

## Entry 4 — The requested re-derivation's "refutation" contains a normalization bug; the severe result stands, confirmed (2026-07-17)

**Prompt (verbatim):**
> New update.

(Reference: `Advisory-WP4b-Rederivation-2026-07-17.md` +
`wp4b_rederivation.py` — advisor built an independent construction and
claimed the severe $0.276$ result is refuted: properly built, the ratio is
$0.965$–$1.007$, a mild $3.5\%$ deficit, not $72\%$; diagnosed the error as
living in my reference-side construction, "hypothesis-grade until [my] code
confirms"; issued a corrected "cdot-8 passes BBN" verdict.)

**Summary of work performed:**

Did not accept the refutation on the strength of its own confident framing.
Ran the delivered script — it reproduces exactly as claimed. But applied
the single most basic sanity check available: **any correctly normalized
comparison must give ratio $=1$ at $z=0$.** Evaluated their own formula
there: $E=1.0$ (correctly normalized), but their reference $\sqrt{u_\text
{hat\_of\_a}(1)}=0.272$, giving ratio $=3.67$, not $1$. **Their own script
fails the simplest check on itself.** Traced this to a missing division:
`u00 = u_hat_of_a(1.0) = 0.074` (the census $\Omega_\text{closure}$, not
$1$) is correctly used to normalize the closure's own source term, but the
final ratio printout uses the raw, undivided `u_hat_of_a(a)` — introducing
a spurious constant factor of $\sqrt{u_{00}}=0.272$ throughout their table.
Correcting for it (multiplying their reported ratios by $0.272$) reproduces
$0.26$–$0.27$ across the same temperature range — matching my escalated
$0.276$ finding, not refuting it.

**Files produced:** `Update-WP4b-RederivationRebuttal-2026-07-17.md`, this
entry.

**Status: the severe result stands, now confirmed by two independent
constructions once both are correctly normalized.** The advisory's shared
cdot-8-side machinery (entropy-conserving $T_\gamma(a)$, the $1.75$ limits,
the WP4a regression, trajectory sanity) was never in dispute and remains
correct — the disagreement was entirely in one dropped normalization on the
reference side of the *new* script, not the old one. The "cdot-8 passes
BBN" verdict and the "sharpened decision input" from this round are
withdrawn along with the ratio they were built on. Recommend the $z=0$
sanity check be added to the K6 pattern library for any future construction
of this kind of comparison. This is now escalated as a severe, not
borderline, BBN-side finding for the Foundation §6 item 6 decision. The
KATRIN clock remains the program's most time-critical item; nothing in
`cdot-7/` was touched.

---

## Entry 5 — Rebuttal withdrawn: the $z=0$ objection was a category error; "cdot-8 passes BBN" reinstated (2026-07-17)

**Prompt (verbatim):**
> Please check the update.

(Reference: `Advisory-WP4b-NormalizationAdjudication-2026-07-17.md` +
`normalization_adjudication.py` — advisor rejected the rebuttal, the first
worker correction declined in this program: the BBN reference is anchored
*absolutely* by $G$ and statistical mechanics, not by "today"; the $z=0$
value of the ratio ($3.67$) is the framework's own $\Omega_s$/invoice
structure showing through, not a bug; the census-normalized reference
(dividing by $u_{00}=0.074$) is the actual anatomy of the original severe
number; "cdot-8 passes BBN" reinstated.)

**Summary of work performed:**

Did not concede on the advisory's confidence — checked the reasoning
directly against this program's own established framework. Confirmed:
$u_\text{hat}(a)$ is only the matter+radiation census content, excluding
the scalar/dark-energy "invoice" ($\Omega_s$) that has been central to this
program since WP3; $E(z)^2=u_\text{hat}(z)+\Omega_s(z)$, with $\Omega_s(0)
\approx0.926$ today — so $E(0)/\sqrt{u_\text{hat}(0)}=3.67$ is correct,
expected physics, and the rebuttal's "must equal 1 at $z=0$" requirement
was a category error (asserting the scalar sector out of existence). At BBN
redshifts, $\Omega_s$ is established as small, so $E^2\approx u_\text{hat}$
there and the ratio naturally sits near $1$ with small deviations — exactly
the reported $0.965$–$1.02$ pattern, not a coincidental rescue. Also built
and then found flawed a follow-up "absolute anchor" check of my own
(constant $g_*=10.75$ against the textbook formula) — $g_*$ is not constant
through the $e^\pm$ transition, and using a fixed value manufactured an
artificial severe-looking drop at low $T$; replacing it with the properly
transitioning $u_\text{hat}(a(T))$ reproduces the advisory's numbers
exactly.

**Files produced:** `Update-WP4b-RebuttalWithdrawn-2026-07-17.md`, this
entry.

**Status: the rebuttal is withdrawn; "cdot-8 passes BBN at leading order"
is reinstated**, with $\Delta N_\text{eff}^\text{eff}\approx-0.3$,
$Y_p\approx0.243$ (within $1\sigma$), D/H $\sim-1\%$, Li-7 favorable-lean.
The decision-input localization stands: crossover-era failure (acoustic
scale), bracketed by passes below (SN) and above (BBN). This cost real
time and briefly asserted a severe finding that did not survive scrutiny —
recorded plainly rather than folded quietly. WP4a is unaffected throughout.
The KATRIN clock remains the program's most time-critical item; nothing in
`cdot-7/` was touched.
