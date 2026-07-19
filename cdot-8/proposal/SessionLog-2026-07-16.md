# Session Log — cdot-8/WP4 (2026-07-16)

*Continues `SessionLog-2026-07-15.md` (three entries: WP3 step-5 resolution,
retraction/frame test, coefficient/no-lapse resolution). Shared,
single-writer-at-a-time log per the Entry-9 process rule (2026-07-12).
This file opens for cdot-8's first data confrontation beyond WP3.
Times in SAST (UTC+2).*

---

## Entry 1 — WP4a assessment: worker's calculation confirmed, provenance clean, 27% miss routed to author per Foundation §6 item 6 (advisor session, 2026-07-16, ~09:1x SAST)

**Prompt (verbatim):**
> First touch-point on WP4. The worker has pulled some details from the
> closed cdot-7 and cdot-4, which had different premises than cdot-8, so
> please check the details carefully.
> [uploaded: `Update-WP4a-AcousticScale-2026-07-16.md` — worker computes
> $100\theta_*=1.326$ from $r_s(z_*)=173.36$ Mpc and $D_p(z_*)=13074.3$ Mpc,
> reports 27% high vs Planck $1.041$, honors Foundation §6 item 6's
> "explicit decision" clause, escalates without pronouncing pass or kill.]

**Summary (advisor):** **Worker's calculation reproduced to the digit;
provenance audit clean.** Six leak-point checks conducted against
Foundation-internal derivation rather than pattern-matching to standard
cosmology: distance convention ($\theta_*=r_s/D_p$ re-derived from §5.5
lockstep, $(1+z_*)$ factors cancel exactly by cdot-8's own formalism);
$z_*=1089.80$ (Planck-unit invariance makes Saha equation identical to
standard in $a$-units, verified by direct dictionary substitution — local
$\rho_\text{cold}\propto a^{-3}$ exactly); $c_s$ formula (local physics,
invariant per K1); $\Omega_G$ (unambiguous, clocks coincide today); $\Omega_b$
(census gives 0.0442, matches BBN-independent 0.0457 to 3% — a mild point
in the theory's favor); $E(z)$ (from WP3-verified closure, ratio 0.79 vs
$\Lambda$CDM at recombination as previously flagged). Cross-check: fixed-point
$D_p$ integral matches Foundation §5.2's analytic $R_{h,0}[1-(1+z)^{-1/2}]=
8306$ Mpc to the digit, confirming the worker's integrator uses cdot-8
conventions correctly.

**Self-caught during audit:** briefly worried that the worker's fitted
$D_p=13074$ Mpc violated Foundation §5.2's 8.6 Gpc "asymptote" — actually
that value is the fixed-point $z\to\infty$ limit, not a trajectory-wide
bound; fitted (accelerating) trajectories legitimately exceed it, exactly
as $\Lambda$CDM's $D_M(z_*)\approx13.9$ Gpc exceeds an equivalent EdS
value. Nearly a sixth error avoided by check-before-write.

**The 27% miss is real and structural**: zero-knob, traceable to
(i) census $\Omega_b=0.044$ inflating $r_s$ by $\sim20\%$ vs $\Lambda$CDM
via lower baryon-photon ratio $R$, plus (ii) fitted $E(z_*)/E_{\Lambda\text{CDM}}
=0.79$ contracting $D_p$ by $\sim6\%$ and further inflating $r_s$.
Qualitatively "$\Lambda$CDM without CDM"-shaped. First peak would shift
from $\ell\sim220$ observed to $\ell\sim173$ predicted.

**Verdict routing per Foundation §6 item 6**: this is exactly the "explicit
decision" territory reserved for author judgment given cdot-4/cdot-5's
history. Three natural readings laid out (soft miss / provisional
structural failure / decisive kill), each with what would justify it,
without advisor preference. **The 27% miss is qualitatively different
from cdot-4/cdot-5's factor-of-9-to-765 misses** but was not required to
be, per the standing rule. Whichever way the decision goes, cdot-7's
data-facing claims remain untouched — that separation was the whole
point of the proposal's charter.

**Framing K6 rule added (sixth advisor error framing, self-noted):**
earlier rounds called WP4a "cheap, immediate" — retrospectively that
understated its weight. "Cheap and decisive" are compatible framings;
"immediate" implies routine execution and preempts the assessment
structure Foundation §6 item 6 already installed. New K6 pattern:
**when a test's outcome can end a work package, framing is "priority"
not "quick"; author decision invited, not preempted.**

**Files produced (Entry 1):**
`Advisory-WP4a-AcousticScale-Assessment-2026-07-16.md`, `wp4a_check.py`,
`SessionLog-2026-07-16.md` (this file).

**Open items handed forward:** **author decision on WP4a routing** —
soft miss, provisional structural failure, or decisive kill — per
Foundation §6 item 6; sign-errata propagation on two `BackreactionMagnitude`
documents (07-13, still outstanding); consolidation log entry for five
(now six with framing) advisor errors and five (now six with priority
framing) K6 pattern rules; WP4b (BBN) queue-status unchanged, gated on
$e^+e^-$/QCD census kinks regardless of WP4a decision; worker
log-numbering reconciliation (standing); all cdot-7 consolidation-log
handoffs unchanged; **the KATRIN clock remains the program's most
time-critical item.**

---

## Entry 2 — WP4a discrepancy hunt: the miss localizes entirely in $E(z)$; $\Omega_b$ exonerated (in fact vindicated); levers found reach ~5%, not 27% (advisor session, 2026-07-16, ~11:0x–11:4x SAST)

**Prompt (verbatim):**
> Let's try one more time with extra effort to look for possible causes of
> the discrepancy. BBN already have known issues such as the lithium
> discrepancy that hints that something is wrong in the assumptions. Are we
> missing something important?

**Summary (advisor; full treatment in `theta_star_diagnosis.py`):** One new
result, one closed escape route, one structural connection. **(1) The
worker's §4 attribution corrected — swap experiments**: cdot-8's $E$ with
$\Lambda$CDM $\Omega_b$ gives $100\theta_*=1.307$ ($\Omega_b$ lever: ~1%);
$\Lambda$CDM $E$ with the census $\Omega_b=0.0442$ gives **1.042 — matching
Planck's 1.041 almost exactly**. The census baryon fraction is not merely
innocent, it is spot-on ($\omega_b$ only 3% below Planck; the worker's ~20%
attribution came from comparing $\Omega$'s at inconsistent implicit $h$).
**The entire miss lives in $E(z)$ over $z_*\to\text{few}\times10^4$** —
cdot-8 expands 15–21% slow there, trough exactly at recombination because
the census crossover ($z_\text{eq}\approx1080$, heavy-$\nu$-set) coincides
with $z_*$. **(2) Census $\nu$-convention freedom: closed** — the census
law is the exact massive-FD dispersion, convention-free; the 07-11
"convention range" was diagnostic markers only, not a physical uncertainty
in $E$; recorded so it is not re-hunted. **(3) The $\nu$-mass lever, probed**
(derivative probe, fit not redone): $\Sigma m_\nu$ 1.374→0.06 eV with
option-iii cold makeup moves $\theta_*$ 1.321→1.253 — right direction,
**same direction KATRIN presses** (two independent confrontations on the
same parameter, recorded as a structural note) — but ~5% of the needed 27%.
**(4) Stage-2 mapping caveat bounded**: AQUAL active at recombination
($x(1100)=2.61$, $\mu=0.72$) but MOND-type effects move peak heights/driving,
not spacing, beyond few-% phase shifts; pre-registered so it cannot become
the indefinitely-deferred rescue. **(5) The BBN/lithium angle (author's
hint), examined**: cdot-8's own BBN signature ($H\approx0.93$–$0.96\times$,
$\omega_b$ −3%) leans the right way — $Y_p$ down ~0.007 (mildly favorable),
Li-7 down ~10–15% (toward the observed deficit, far from resolving it), D/H
net ~−2% (within errors) — a genuine WP4b motivation, but BBN cracks cannot
absorb a geometric 0.03%-precision $\theta_*$ miss at a different epoch.
**Honest summary**: nothing missing at background level; the miss is real,
zero-knob, and localized in the framework's most *derived* sector (census +
closure through the radiation era) — the worst news for survivability, the
best news for the program's integrity: WP4a tested the actual theory.
Decision remains the author's under Foundation §6 item 6, with the
sharpened localization as input.

**Files produced (Entry 2):** `Advisory-WP4a-DiscrepancyHunt-2026-07-16.md`,
`theta_star_diagnosis.py`, `SessionLog-2026-07-16.md` (this file, two
entries).

**Open items handed forward:** author decision on WP4a (Foundation §6 item
6), now with the localization and lever bounds as input; worker §4
attribution correction + census-$\Omega_b$ positive result to ledger;
$\nu$/KATRIN alignment note to consolidation log; census-convention
non-freedom recorded; WP4b motivation strengthened (lithium lean), still
gated on census kinks; sign-errata and five-error consolidation entries
still outstanding; **the KATRIN clock remains the program's most
time-critical item — now formally coupled to the $\theta_*$ tension.**

---

## Entry 3 — WP4a closure endorsed with two adopted refinements; WP4b reviewed: two flags (one potentially table-invalidating), not yet done; pre-decision checklist issued (advisor session, 2026-07-16, ~14:0x SAST)

**Prompt (verbatim):**
> WP4a and WP4b are now done. Any advice before we proceed?
> [uploaded: `Update-WP4a-DiscrepancyHuntAssessment-2026-07-16.md` (worker
> owns §4 attribution error via controlled swap; raises circularity caveat
> on the "vindication" framing), `Update-WP4a-ReviewClosure-2026-07-16.md`
> (worker closes the c(z)-in-D_p loose thread the advisor's script left
> dangling), `Update-WP4a-AcousticScale-2026-07-16.md` (original, for
> reference), `Update-WP4b-BBN-2026-07-16.md` (new: e+e- census kink derived,
> QCD ruled irrelevant, entropy-vs-energy distinction, H/H_std table
> 0.93–0.96, ΔN_eff≈−0.7, Y_p≈0.238, D/H≈2.47e-5).]

**Summary (advisor; verification in `wp4b_check.py`):** **WP4a: done.** Both
closure rounds verified. Circularity caveat adopted in full (the second
swap's "matches Planck" is partially ΛCDM-confirming-itself; the
non-circular content — first swap localization + census ω_b 3% agreement —
carries the conclusion alone); recorded as advisor framing overweight
(framing caution, hard-error tally stays at five). Loose-thread hygiene
rule adopted (delivered scripts must not contain silently-dropped open
questions). **WP4b: NOT done.** Verified: QCD irrelevance ✓;
frozen-vs-equilibrium distinction ✓ (recorded as a census-law scope
statement: the 07-11 law is for decoupled species; equilibrium species
count with equilibrium distributions); entropy-vs-energy ✓ with refinement
(instantaneous conversions conserve energy; extended adiabatic transitions
conserve comoving entropy); Boltzmann limit ✓; ΔN_eff arithmetic ✓ (−0.72
from H ratio 0.94); Y_p=0.238 reproduced and quantified at **2.3σ below
observed** (0.2453±0.0034). **Flag 1**: "u_e±/u_γ→3.5" is a factor-2 prose
slip (3.5 is g_*-units; ratio is 7/4) — code disposition needs confirming.
**Flag 2 (table-invalidating if confirmed)**: the census machinery's ν term
carries post-annihilation T_ν=(4/11)^{1/3}T_γ at ALL z — fine for WP4a
(r_s converged below z~10⁹) but wrong in WP4b's window (T≳m_e has T_ν=T_γ:
correct g_*(1 MeV)=10.75 vs machinery-scaled 6.86 — 36% in u, ~20% in H,
same order as the 4–7% signal). If the WP4b run inherited it, the
H/H_std table and everything downstream (ΔN_eff, Y_p, D/H) is unreliable;
requires confirmation and, if needed, re-run with a sharp annihilation
switch. **Flag 3**: D/H's −2.4% is only reproducible with the ω_b lever
folded in (+5% against N_eff's −10%) — provenance must be stated.
**Addition**: Li-7 leading order −35% vs SBBN (favorable direction, ~half
the needed shift). **Pre-decision checklist issued**: (1) WP3 formally
still open — the covariant-g_i verification + D≡0 re-run directives were
never delivered; close before the record is assessed; (2) WP4b Flag 2;
(3) batch ALL outstanding consolidation entries into one delivery (sign
errata, error tally + framing cautions, six K6 rules, ν/KATRIN note,
census-convention non-freedom, §4 correction + circularity caveat,
census-law scope statement); (4) then the Foundation §6 item 6 decision —
combined input: one structural cause (radiation-era E deficit), two
confrontations (θ* fails hard: 27% vs 0.03%, zero knobs; BBN borderline:
Y_p −2.3σ, D/H fine, Li leans right), correlated not independent; levers
reach 5–10% of 27%; three readings stand; the choice is the author's and
gates everything downstream. (5) KATRIN unchanged, now doubly coupled.

**Files produced (Entry 3):**
`Advisory-WP4ab-ReviewAndPreDecisionChecklist-2026-07-16.md`,
`wp4b_check.py`, `SessionLog-2026-07-16.md` (this file, three entries).

**Open items handed forward:** WP3 formal close (worker verification +
D≡0 re-run — outstanding); WP4b Flag 2 confirmation/re-run + Flag 1 code
confirmation + Flag 3 provenance statement + Li-7 line; the batched
consolidation delivery; **the author's Foundation §6 item 6 decision — the
gate for everything downstream**; worker log-numbering reconciliation
(standing); **the KATRIN clock remains the program's most time-critical
item, now coupled to both WP4 confrontations.**
