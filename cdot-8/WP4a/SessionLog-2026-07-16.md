# Session Log — cdot-8/WP4a (2026-07-16)

*New work package, new file. WP3 closed 2026-07-15 (D≡0 confirmed, six
cumulative advisor errors caught, all by independent reconstruction/re-running
rather than trusting a written claim). Same per-prompt logging convention as
WP2/WP3.*

---

## Entry 1 — Survey, gating check, and the first WP4a computation (2026-07-16)

**Prompt (verbatim):**
> Excellent news! Please continue with WP4a

**Summary of work performed:**

1. **Surveyed existing CMB/recombination machinery before computing anything**
   (via a research agent, then independently re-read the key primary sources
   myself): cdot-4's and cdot-5's own CMB first-peak attempts, and — critically
   — cdot-7's `Foundation.md` §6 item 6, which explicitly states this exact
   territory is "not yet authorized, pending an explicit decision," citing
   **two prior decisive structural failures** in cdot-4/cdot-5 (ranging from a
   $9\times$ to $765\times$ shortfall, later corrected passes landing at
   $1.3$–$1.4\times$ overshoot, with the recombination redshift never resolved
   from first principles — swinging between $z\sim1240$ and $z\sim2\times10^6$
   depending on an unsettled kinetics assumption). Also found a live
   contradiction between stages: cdot-4/5 used $D_A\equiv D_p$ for the peak
   calculation; cdot-7's own §5.5 proves the opposite, $d_A=D_p/(1+z)$.

2. **Flagged this to the user before proceeding** — the cdot-8 proposal's
   characterization of WP4a as "immediate/cheap" doesn't match what cdot-7's
   own Foundation says about this territory's history. Given explicit
   direction to proceed carefully, first-principles only, treated WP4a with
   the same weight as Foundation's own gated item, not as a quick add-on.

3. **Resolved both historical ambiguities before computing**: (a) re-derived
   the correct $\theta_*$ formula from Foundation §5.5's own lockstep-ruler
   formalism applied to a size measured *at* recombination (not today),
   showing the $(1+z_*)$ factors cancel — $\theta_*=r_s(z_*)/D_p(z_*)$, not
   $r_s/D_A$ with the extra suppression (caught via a first, nonsensical
   numerical result, $100\theta_*\approx1456$, before accepting any formula);
   (b) established $z_*$ is standard, not re-derived, because recombination is
   local atomic physics and Foundation §3.1/§5.5 already establish that local
   atomic/binding-energy physics and the thermal sector ($\hat T(z)=\hat
   T_0(1+z)$) are exactly the standard relations in this framework — checked
   sensitivity to the exact $z_*$ value, $<1\%$ effect.

4. **Computed $r_s(z_*)$ and $D_p(z_*)$** reusing the already-established,
   verified matter+radiation+neutrino census trajectory (same machinery as
   WP2/WP3's `census_closure.py`-style code), with the mass-census $\Omega_b=
   0.0442$ (zero additional knob) and standard sound-speed physics. Caught and
   fixed a convergence artifact in the $r_s$ integral (naive range to
   $z=10^7$ gave $174.5$ Mpc, contaminated by extrapolation past the solved
   trajectory; extended the integration range to $z\sim10^{10}$ and confirmed
   convergence to $173.36$ Mpc).

5. **Result**: $100\,\theta_*=1.326$ vs. Planck's $1.04109\pm0.00030$ — a
   $27\%$ overshoot. Traced the discrepancy to two identifiable, non-tunable
   sources (the census $\Omega_b$ running $\sim10\%$ low relative to standard,
   giving a larger sound horizon; cdot-8's own fitted $E(z)$ running
   $\sim6\%$ low in comoving distance relative to $\Lambda$CDM), both compounding
   in the same direction — not a knob that could be adjusted away without
   touching already-validated fits.

**Files produced:** `Update-WP4a-AcousticScale-2026-07-16.md`, this entry;
verification scripts in session scratchpad.

**Status: a real, honestly-reported first result, not a resolution.** $27\%$
is a genuine tension, not a pass — but also not the $9$–$765\times$ historical
failures Foundation's gating language warned about, and this time every
convention question (distance formula, recombination redshift) was resolved
rather than left ambiguous. Recommend escalating for review per Foundation's
own standing requirement that this territory needs an explicit decision,
rather than unilaterally declaring WP4a passed or failed. WP4b (BBN) remains
queued, gated on the $e^+e^-$/QCD census kinks. The KATRIN clock remains the
program's most time-critical item; nothing in `cdot-7/` was touched.

---

## Entry 2 — Advisor review confirms the calculation; a loose thread in their own script closed; the verdict routed to the author (2026-07-16)

**Prompt (verbatim):**
> Review uploaded.

(Reference: `Advisory-WP4a-AcousticScale-Assessment-2026-07-16.md` +
`wp4a_check.py` — advisor reproduced the calculation to the digit, ran a
six-point provenance audit (distance convention, $z_*$, sound speed, $\Omega_G$,
$\Omega_b$, $E(z)$) all clean, cross-checked $D_p$ against Foundation §5.2's
analytic fixed-point formula, and routed the pass/fail/kill verdict to the
author per Foundation §6 item 6, offering three readings with no preference.)

**Summary of work performed:**

Did not accept the "provenance is clean" conclusion without checking the
advisor's own script first. `wp4a_check.py` trails off (lines 100–112) into
an unresolved worry — whether the $D_p$ integral needs a $c(z)$ factor inside
it, given this is a varying-$c$ framework — that never appears in the
delivered advisory prose. Checked directly: the constant-$c_0$ integral
exactly reproduces Foundation §5.2's independently-derived analytic $D_p$
formula on the fixed point (residual $1.9\times10^{-6}$) — no missing factor.
The advisory's own reported cross-check already answered this, it just wasn't
connected back to the specific concern raised in the companion script;
closed that thread explicitly rather than leaving it silently dropped.
Everything else (term-by-term reproduction, the six-point audit, the
self-caught 8.6 Gpc asymptote question) re-checked and confirmed with no
disagreement.

**Files produced:** `Update-WP4a-ReviewClosure-2026-07-16.md`, this entry;
confirmed on disk.

**Status: the numerical result stands, confirmed independently twice now.**
The pass/provisional-failure/kill decision is the author's per Foundation §6
item 6 — presenting the three-way choice directly rather than narrowing it
further. WP4b, sign-errata propagation, and the consolidation-log entry
remain queued unaffected by which reading is chosen. The KATRIN clock remains
the program's most time-critical item; nothing in `cdot-7/` was touched.

---

## Entry 3 — Discrepancy hunt verified; own §4 attribution corrected; localization confirmed with one circularity caveat (2026-07-16)

**Prompt (verbatim):**
> I have had the advisor put in some more effort on this issue, and it came
> out good. Please read the new advice.

(Reference: `Advisory-WP4a-DiscrepancyHunt-2026-07-16.md` +
`theta_star_diagnosis.py` — advisor ran swap experiments localizing the 27%
miss almost entirely to $E(z)$ over $z_*$-to-few$\times10^4$, correcting the
worker's earlier hand-wave attribution of ~20% to $\Omega_b$ (controlled swap
shows $\Omega_b$ moves $\theta_*$ by only ~1% within cdot-8's own $E(z)$);
probed the neutrino-mass lever (~5% of the needed 27%, KATRIN-aligned
direction); closed the census-$\nu$-convention freedom; bounded the
Stage-2/BBN-lithium angles as insufficient rescues.)

**Summary of work performed:**

1. **Reproduced the swap-experiment table exactly** (one numpy-version
   compatibility fix, no effect on the numbers).

2. **Accepted the correction to my own earlier attribution**: my original
   WP4a update attributed ~20% of the $r_s$ excess to $\Omega_b$ by direct
   comparison of $\Omega_b$ values, not by a controlled experiment — the
   swap test shows this was wrong (only ~1% when actually isolated).
   Recorded as a correction to my own prior work, not the advisor's.

3. **Flagged one caveat on the "vindication" framing**: the more decisive
   half of the swap experiment (cdot-8's own $E$, standard $\Omega_b$ →
   barely moves) is genuinely independent evidence; the other half
   ($\Lambda$CDM's $E$, census $\Omega_b$ → matches Planck) is partly
   circular, since $\Lambda$CDM's $E(z)$ was itself calibrated against data
   including the CMB scale. The real, standalone result from that row is
   narrower but still genuine: census $\omega_b$ sits within 3% of Planck's
   independent BBN value.

4. Everything else (neutrino-mass table, census-convention closure, Stage-2
   and BBN-lithium bounding) reproduced/reviewed with no disagreement.

**Files produced:** `Update-WP4a-DiscrepancyHuntAssessment-2026-07-16.md`,
this entry; confirmed on disk.

**Status: the localization stands, on firmer ground, with the caveat
recorded.** The verdict decision remains exactly where both prior rounds left
it — the author's, under Foundation §6 item 6 — now informed by the sharper
localization but not narrowed further by either advisor round or this one.
