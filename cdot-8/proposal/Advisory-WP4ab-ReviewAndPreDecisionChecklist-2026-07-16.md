# Advisory — WP4a Closed Cleanly; WP4b Not Yet Done: One Prose Slip and One Potentially Table-Invalidating Gap to Resolve; and the Pre-Decision Checklist (for `cdot-8/WP4/`)

*2026-07-16. Advisory in response to
`Update-WP4a-DiscrepancyHuntAssessment-2026-07-16.md`,
`Update-WP4a-ReviewClosure-2026-07-16.md`, and
`Update-WP4b-BBN-2026-07-16.md`. Verification in `wp4b_check.py`. Verdict up
front: **WP4a is genuinely done — both closure rounds verified, and two
worker refinements adopted into the ledger. WP4b is not done: its physics
architecture is sound and two of its self-caught errors are exactly right,
but its headline $H/H_\text{std}$ table rests on an unconfirmed assumption
about the neutrino temperature at $T>m_e$ that, if wrong, carries a ~20%
method error into a ~5% signal. One bounded confirmation/re-run resolves it.
Advice before proceeding: close WP3 formally (still open), finish WP4b's one
item, batch the consolidation entries, and then the Foundation §6 item 6
decision — for which the combined decision input is stated compactly in §4
below — is the actual gate.***

---

## 1. WP4a closure rounds — endorsed, two refinements adopted

**The circularity caveat (worker's assessment §2): adopted in full.** The
worker is right that the second swap ($\Lambda$CDM $E$ + census $\Omega_b\to
1.042$) carries less independent weight than my "vindicated/spot-on" framing
gave it — $\Lambda$CDM's $E(z)$ was calibrated on data including $\theta_*$,
so landing near $1.041$ partially confirms $\Lambda$CDM against itself. The
non-circular content stands on its own two legs: (i) the first swap (cdot-8's
own $E$, $\Omega_b$ swapped, moves 1%) localizes the miss without reference
to $\Lambda$CDM's calibration; (ii) the census $\omega_b=0.0217$ vs Planck's
independently-measured $0.0224$ (3% agreement, zero tuning) is real
regardless of what it's plugged into. Ledger: **advisor framing overweight,
worker-caught — recorded as a framing caution alongside the WP4a "immediate"
caution, not inflating the hard-error tally (which stands at five).** The
localization conclusion itself is unchanged and now rests only on the
non-circular half.

**The loose-thread closure (worker's review §1): endorsed, and the hygiene
rule is adopted.** My `wp4a_check.py` carried an unresolved trailing worry
(whether $D_p$ needs a $c(z)$ factor) that the advisory prose never
addressed — the fixed-point cross-check *was* the answer, but the connection
went unstated, leaving an admitted-but-dropped concern in a delivered
artifact. The worker closed it correctly (constant-$c_0$ form verified
against Foundation §5.2's independently-derived formula, residual
$1.9\times10^{-6}$). **New K6 hygiene rule: a delivered script must not
contain open questions the accompanying prose neither resolves nor flags;
trailing worries are either answered, promoted to the advisory text, or
deleted before delivery.**

## 2. WP4b — verified items

- **QCD irrelevance to BBN**: correct ($T\sim150$–$200$ MeV vs BBN's
  $0.05$–$1$ MeV); properly scoped.
- **The frozen-vs-equilibrium distinction** (their first-attempt error,
  self-caught): exactly right, and the catch is the important part — the
  census massive-FD law from the 07-11 round is *for decoupled species with
  conserved comoving $k$* (neutrinos); species in chemical equilibrium
  (e$^\pm$) must be counted with the equilibrium distribution. This
  distinction should be recorded in the census documentation as a scope
  statement on the census law itself, not just as a WP4b footnote.
- **Boltzmann limit** of their $F_\text{eq}$: reproduced
  ($F_\text{eq}(50)/F_\text{eq}(0)=8\times10^{-19}$).
- **Entropy-vs-energy conservation** (their §3): endorsed, with one
  refinement for the record. Energy *is* conserved at each annihilation
  event; what fails in the naive $gT^4$ balance is treating an extended,
  expansion-interleaved process as an instantaneous conversion. The correct
  invariant across the extended adiabatic transition is comoving entropy —
  which is why $(11/4)^{1/3}$, not $(11/4)^{1/4}$. Suggested amendment to
  the census-continuity language: *instantaneous conversions conserve
  coordinate energy; extended adiabatic transitions conserve comoving
  entropy; the $e^\pm$ dump is the latter.* Both are standard invariant
  local physics under K1 — import-not-rebuild, as the worker says.
- **$\Delta N_\text{eff}$ arithmetic**: their $-0.7$ from
  $H/H_\text{std}=0.94$ checks exactly ($\Delta g_*=-1.25$ of $10.75$;
  $\div1.75$ per $\nu$ species $=-0.72$).
- **$Y_p=0.238$**: reproduced from standard sensitivity coefficients — and
  quantified: vs observed $0.2453\pm0.0034$ this is a **2.3σ undershoot**.
  "Mild, not dramatic" should carry the number; 2.3σ is a genuine tension
  of the same order as the ones cosmology takes seriously elsewhere.

## 3. WP4b — two flags, one addition; not yet done

**Flag 1 (prose, likely benign, needs confirmation).** "$u_{e^\pm}/u_\gamma
\to\tfrac78\cdot4=3.5$" is a factor-2 slip *as a ratio*: 3.5 is the
$g_*$-units contribution (photons count 2 in the same units); the ratio is
$7/4=1.75$. If the code adds $e^\pm$ in $g_*$-units alongside photons' 2,
it's right and only the sentence is wrong. Confirm which; the
closed-form-check K6 rule applies (an inline $A\to0$ ratio assertion in the
script settles it permanently).

**Flag 2 (potentially table-invalidating — the reason WP4b is not done).**
The census machinery's neutrino term (`REL`$\,\cdot\,$FD-interp) carries the
**post-annihilation** $T_\nu=(4/11)^{1/3}T_\gamma$ scaling at *all* $z$.
That is correct for every epoch WP4a touches ($r_s$ is converged below
$z\sim10^9$). But WP4b's window ($T=2\to0.05$ MeV, $z\sim10^{10}\to
2\times10^8$) straddles annihilation, and at $T\gtrsim m_e$ the physical
neutrinos share the photon temperature: correct $g_*(1\,\text{MeV})=10.75$,
while machinery-scaled neutrinos give $6.86$-equivalent — **a 36%
underestimate of $u$, i.e. ~20% in $H$, at exactly the epochs where the
table's 4–7% signal is being read.** If the WP4b run inherited the
machinery's $\nu$ scaling, the $0.96/0.95/0.93/0.94$ column and the derived
$\Delta N_\text{eff}=-0.7$ are unreliable; if the worker's code implemented
$T_\nu=T_\gamma$ pre-annihilation, the table stands. **Required: confirm
which, and if the former, re-run with the corrected $\nu$ temperature
(sharp switch at annihilation is adequate at this order). Everything
downstream of the table — $\Delta N_\text{eff}$, $Y_p$, D/H — inherits the
answer.**

**Flag 3 (provenance statement).** The D/H number ($-2.4\%$) cannot be
reproduced from the $N_\text{eff}$ sensitivity alone (which gives
$\sim-10\%$); it is consistent with the $\omega_b$ lever having been folded
in ($+5\%$, partially canceling). If so, state the coefficients and the
$\omega_b$ inclusion explicitly — the number is fine, its provenance is
currently unstated.

**Addition.** Li-7 at the same leading order: $\Delta N_\text{eff}=-0.7$
plus $\omega_b$ 3% low gives $\sim-35\%$ vs SBBN — direction favorable
(observed deficit needs $-65$ to $-70\%$), magnitude about half. Worth one
line in the WP4b record since the lithium lean was part of this
confrontation's motivation.

## 4. Advice before proceeding — the checklist, in order

1. **WP3 is still formally open.** The coefficient/no-lapse advisory's
   directives 1–2 (worker verification of the covariant $g_i$ derivation;
   the $D\equiv0$ re-run under the corrected formula) were never delivered —
   the program jumped to WP4a on the strength of an expected-but-unconfirmed
   $D\equiv0$. The expectation is well-founded ($\partial g_i/\partial N=0$
   identically), but the record must not show WP4 built on an unclosed WP3.
   One bounded delivery closes it.
2. **WP4b: resolve §3's Flag 2** (and confirm Flag 1, state Flag 3). Until
   then, WP4a is done; WP4b is *leading-order pending one verification*.
3. **Batch the consolidation entries into one delivery now**: the sign
   errata (two BackreactionMagnitude documents), the five-hard-error tally
   with the framing cautions, the K6 rules (closed-form check; sign-flip
   iteration; verdict scoping; inherited conventions; priority-not-quick;
   loose-thread hygiene), the ν/KATRIN alignment note, the
   census-convention non-freedom, the worker's §4 attribution correction
   plus the circularity caveat, and the census-law scope statement from
   §2 above. The record should be clean at the decision point.
4. **Then the actual gate: the Foundation §6 item 6 decision.** The
   combined decision input, compactly: **one structural cause — the
   radiation-era expansion deficit of the census+closure — faces two
   confrontations. It fails the acoustic scale hard (27% against a 0.03%
   measurement, zero knobs, localized in the framework's most derived
   sector) and sits borderline at BBN (leading-order: $Y_p$ $-2.3\sigma$,
   D/H comfortable, Li-7 leaning favorably).** These are correlated
   outcomes of the same $E(z)$, not independent tests. The identified
   levers (lighter $\nu$ + option-iii, KATRIN-aligned; Stage-2 mapping)
   reach 5–10% of the 27% combined. The three readings from the assessment
   advisory stand unchanged; the choice among them determines everything
   downstream (refit-or-not, WP5+, whether cdot-8's charter continues or
   closes with cdot-7 intact), and it is the author's.
5. **KATRIN**: unchanged, most time-critical, now doubly coupled (census
   $\Sigma m_\nu$ enters both the $\theta_*$ localization and the BBN
   window's matter content).

## 5. Protocol note

The two WP4a closure rounds are the program's review discipline running at
full function in both directions at once: the worker corrected their own
attribution by controlled experiment, then corrected the advisor's framing
by an epistemics argument, then closed a thread the advisor's own script
had left dangling — and all three moves were right. WP4b's two self-caught
errors (frozen-vs-equilibrium; energy-vs-entropy) are the same discipline
applied prospectively. The one gap flagged in §3 is exactly the kind of
inherited-convention issue the K6 rule from the coefficient round exists
for: the machinery's $\nu$ scaling was correct for every prior use and
silently wrong for this new window. That is not a criticism of the worker;
it is the rule demonstrating why it exists.

## Companion

- `wp4b_check.py` — the ratio check, $\Delta N_\text{eff}$ arithmetic, D/H
  decomposition, $Y_p$ σ-quantification, Li-7 estimate, and the
  $\nu$-temperature gap quantification.
- This advisory: proposed location
  `cdot-8/WP4/Advisory-WP4ab-ReviewAndPreDecisionChecklist-2026-07-16.md`.
