# T20 — The White Dwarf Population and the Chandrasekhar-Mass Ceiling

*Status: speculative, cross-checked against observation, as in cdot-4. Cross-references
T1 (age/lookback-time formulas), T4 (origin of the $M_\text{Ch}\propto c^{3/2}$ result,
unaffected by the counting-law change), T8 (invariant $G$), T21 (strong/weak sector
coupling — source of the §E cooling-age correction), T23 (the percolation break that
now bounds this document's validity range). **This document depends directly on cosmic
history — the mapping from a white dwarf's age to the value of $c$ at its formation
epoch — which is exactly the piece the counting-law change alters.** It is redone in
full below using cdot-5's exact $c(\tau)$ relation (T1), which turns out to be simpler
(exactly linear) than cdot-4's $3/4$-power law. The resulting reference tables are, by
a numerical coincidence tied to the model's calibration, close to cdot-4's — but a
genuinely new complication appears: **this document's own derivation is provisional
only for lookback times below $\tau(z_*)\approx9.1$ Gyr**, the proper-time location of
the percolation break (T23). This retires §D (globular-cluster CO white dwarfs, ages
$11.6$–$13$ Gyr) as currently uncomputable, and flags the low-mass end of both
reference tables as extrapolation into an undetermined regime.*

---

## Physical Concept

T4 establishes that under invariant $G$, invariant $\hbar$, and invariant $m_p$ — all
premises unchanged from cdot-4 to cdot-5 — the Chandrasekhar mass scales as
$M_\text{Ch}\propto c^{3/2}$, and that because $c$ was smaller in the past, high-redshift
SNe Ia detonate at lower mass and are intrinsically fainter. This is a **present-value**
scaling (how $M_\text{Ch}$ depends on the instantaneous $c$) and does not reference the
counting law at all — it survives unchanged.

This document asks a different question: **standard candles are not the only
Chandrasekhar-mass objects in the sky. Every white dwarf near the top of the mass
distribution is one.** If $M_\text{Ch}$ was lower in the past, then no stable white
dwarf, anywhere, at any time, could have formed with a mass exceeding the value of
$M_\text{Ch}$ that prevailed at its own formation epoch. Since $c(t)$ is a monotonically
increasing function of cosmic time in this model (unchanged in direction under
connectivity counting — only the functional form of the increase changed, T23), this
creates a **hard ceiling on how old a massive white dwarf is allowed to be**, purely as
a function of its mass — independent of composition, formation channel, and independent
of all the unresolved SN-specific physics in T4.

The sharpest, most falsifiable form of the claim, unchanged from cdot-4: the model
predicts that **massive white dwarfs should be systematically rarer than ordinary
stellar-evolution population synthesis predicts, specifically among the ones old enough
to have cooled** — a *deficit*, not merely a spread of individual outliers.

**Why the formation channel does not matter — and what "formation epoch" precisely
means.** Unchanged from cdot-4. A single star's degenerate core cannot exceed
$M_\text{Ch}(t)$ at the time it stops growing; a double-degenerate merger remnant cannot
exceed it at the time of merger; and an object with a history of binary mass transfer
(a former cataclysmic variable, nova system, or engulfment remnant) is bound by
$M_\text{Ch}(t)$ only at the epoch its mass last changed, not at its single-star birth:
$$M \le M_\text{Ch}(\tau_\text{last mass-set}).$$
The ceiling is channel-independent; it is not safe to equate "the object's mass" with
"its single-star formation epoch" without checking its binary history. As in cdot-4,
every comparison below infers $\tau$ from a *passive-cooling* model track, which
understates the age of any object with a hidden accretion history — flagged as an
unresolved caveat, unquantified.

---

## Derivation

### From $c(\tau)$ to $M_\text{Ch}(\tau)$ — redone with the exact linear relation

cdot-4 obtained $c(\tau)/c_0=(1-\tau/\tau_\infty)^{3/4}$ from the occupancy (volume) law.
T1's cdot-5 rewrite derives a genuinely different, and simpler, relation for the
post-percolation branch, directly from the redshift law (T2, $1+z=(c_0/c_e)^2$,
unaffected by the counting-law change) combined with the connectivity horizon law's
lookback solution (Core Principles §3/§4a):
$$\boxed{\,\frac{c(\tau)}{c_0} = 1-\frac{\tau}{\tau_\infty}\,},\qquad
\tau_\infty=\frac{2}{H_0^\text{obs}}\approx27.9\ \text{Gyr (}H_0=70\text{)}.$$
This is **exactly linear** in $\tau$, not a power law — no new premise beyond what T1
already establishes; it is that same relation, restated here. Combining with T4's
$M_\text{Ch}\propto c^{3/2}$ (unaffected by the counting-law change):
$$\boxed{\frac{M_\text{Ch}(\tau)}{M_{\text{Ch},0}} = \left(1-\frac{\tau}{\tau_\infty}\right)^{3/2}}$$
— a **cleaner exponent** ($3/2$) than cdot-4's $9/8$, because the underlying $c(\tau)$
relation itself simplified from a $3/4$-power law to a linear one. Inverting, the **age
ceiling** for a white dwarf of mass $M$ is:
$$\boxed{\tau_\text{ceiling}(M) = \tau_\infty\left[1-\left(\frac{M}{M_{\text{Ch},0}}\right)^{2/3}\right]}$$
(cdot-4's exponent was $8/9$). This uses only premises already adopted in Core
Principles (invariant $G,\hbar,m_p$; the post-percolation horizon law; $P=2$) and T1's
own lookback-time solution.

### The validity boundary — new, load-bearing

**Both formulas above hold only within the post-percolation branch, $z<z_*\approx1.201$
(T23) — equivalently, proper lookback times**
$$\tau < \tau(z_*) = \tau_\infty\left[1-(1+z_*)^{-1/2}\right] \approx 27.94\times0.326
\approx 9.1\ \text{Gyr}.$$
Beyond this, the network is subcritical (T23) and $c(\tau)$ follows whatever the
pre-percolation (occupancy) branch's own dynamics give — a relation that is fit
empirically at the DESI redshift bins but **not yet derived in closed form**, and
certainly not yet integrated into a $\tau(z)$ mapping (flagged as an open item in Core
Principles §3 and T1's own Open Questions, not resolved here). **Every entry in the
tables below that falls at $\tau>9.1$ Gyr (equivalently, at the corresponding low-mass
end) is accordingly extrapolation beyond the derived regime**, not a consequence of the
model as currently derived. This is a strictly new complication relative to cdot-4, which
had no such break and could extrapolate its single power law to any age.

### Reference tables ($H_0=70$ km/s/Mpc, $\tau_\infty=27.94$ Gyr)

Two brackets for $M_{\text{Ch},0}$ are carried throughout, as in cdot-4:
$1.40\,M_\odot$ (textbook $\mu_e=2$ value) and $1.44\,M_\odot$ (the larger,
GR/finite-temperature corrected value sometimes quoted).

**Maximum stable WD mass as a function of age $\tau$:**

| $\tau$ (Gyr) | $M_\text{max}$ ($M_{\text{Ch},0}=1.40$) | $M_\text{max}$ ($M_{\text{Ch},0}=1.44$) | Regime |
|---:|---:|---:|---|
| 0.5 | 1.363 | 1.402 | valid |
| 1 | 1.326 | 1.363 | valid |
| 2 | 1.252 | 1.288 | valid |
| 3 | 1.181 | 1.215 | valid |
| 4 | 1.110 | 1.142 | valid |
| 5 | 1.042 | 1.071 | valid |
| 8 | 0.844 | 0.868 | valid |
| **9.1 ($z_*$)** | **0.774** | **0.796** | **boundary** |
| 10 | 0.720 | 0.741 | *extrapolated* |
| 12 | 0.604 | 0.621 | *extrapolated* |
| 13 | 0.548 | 0.563 | *extrapolated* |
| 13.4 | 0.526 | 0.541 | *extrapolated* |

**Age ceiling as a function of mass $M$:**

| $M\ (M_\odot)$ | ceiling (Gyr), $M_{\text{Ch},0}=1.40$ | ceiling (Gyr), $M_{\text{Ch},0}=1.44$ | Regime |
|---:|---:|---:|---|
| 0.60 | 12.06 | 12.35 | *extrapolated* |
| 0.80 | 8.70 | 9.06 | valid / borderline |
| 1.00 | 5.61 | 6.03 | valid |
| 1.10 | 4.15 | 4.59 | valid |
| 1.15 | 3.43 | 3.89 | valid |
| 1.20 | 2.73 | 3.20 | valid |
| 1.25 | 2.03 | 2.51 | valid |
| 1.27 | 1.76 | 2.25 | valid |
| 1.30 | 1.35 | 1.84 | valid |
| 1.33 | 0.94 | 1.44 | valid |
| 1.35 | 0.67 | 1.18 | valid |
| 1.38 | 0.27 | 0.78 | valid |
| 1.40 | 0.00 | 0.52 | valid |

**These numbers are, by coincidence, close to cdot-4's** (e.g. $M=1.00$: cdot-4 gave
$5.42$/$5.80$ Gyr vs. cdot-5's $5.61$/$6.03$ Gyr; $M=1.30$: cdot-4's $1.34$/$1.82$ vs.
cdot-5's $1.35$/$1.84$) — the different exponent ($3/2$ vs. $9/8$) and the different
$\tau_\infty$ ($27.9$ vs. $21$ Gyr) partially compensate. **This means the confrontation
with data in §A–§C below, which uses masses and ages mostly at or below $\sim5$ Gyr,
carries over with almost no numerical change** from cdot-4 — but only because those
specific rows happen to sit inside the newly-identified valid regime, not because the
underlying physics is somehow independent of the break.

Raising $H_0$ to the local distance-ladder value ($73$ km/s/Mpc, $\tau_\infty\approx26.8$
Gyr) shrinks every entry by a further $\sim4\%$ and shrinks the validity boundary
correspondingly, i.e. it **tightens**, not relaxes, the ceilings (unchanged pattern from
cdot-4).

---

## Confrontation with Data

### A. Individual field ultra-massive white dwarfs — not currently reliable evidence

Unchanged from cdot-4 in every respect that does not depend on the model's tables: an
initial pass compared 44 literature ultra-massive white dwarfs (Camisassa et al. 2019,
A&A, arXiv:1807.03894) against $\tau_\text{ceiling}(M)$ and found 15/44 (34%,
$M_{\text{Ch},0}=1.40$) to 8/44 (18%, $M_{\text{Ch},0}=1.44$) individual objects
exceeding the ceiling — using the cdot-4 table, whose entries are close enough to the
cdot-5 table above (§"Derivation") that this headline percentage does not change
materially under the recomputation.

**The same, serious, specific problem stands: nearly every mass in that table comes from
pure spectroscopic fits**, now documented in multiple independent studies to run high by
$0.05$–$0.16\,M_\odot$ relative to Gaia-parallax-based photometric masses — comparable to
or larger than what is needed to move most flagged "violations" back under the ceiling.
Unaffected by the counting-law change, since this is a data-systematics argument, not a
model calculation:

- Genest-Beaulieu & Bergeron (2019, ApJ, arXiv:1901.01857): systematic SDSS/Gaia
  discrepancy traced to line-broadening physics.
- A 2026 DESI DR1 model-atmosphere analysis (DOI 10.3847/1538-4357/ae43ee): $0.05$–
  $0.06\,M_\odot$ systematic offset (spectroscopic high).
- **GD 518**: $1.20\,M_\odot$ (spectroscopic) → $1.114\pm0.006\,M_\odot$ (Gaia-parallax,
  Kilic et al. 2025).
- **BPM 37093**: $1.097\,M_\odot$ (Nitta et al. 2016) → $1.037\pm0.008\,M_\odot$
  (O'Brien et al. 2024), spread $1.04$–$1.13\,M_\odot$ across compilations.
- **SDSS J084021.23+522217.4**: $1.139\,M_\odot$ (spectroscopic) → $0.98\pm0.04\,M_\odot$
  (Vincent et al. 2024, photometric) — removed from the ultra-massive category entirely.

**Assessment — unchanged.** The individual-object test as originally constructed is
**not currently reliable evidence either for or against the model**. Retracted as a
primary line of evidence pending Gaia DR3 re-derivation of the specific flagged objects
(top Open Question).

**One promising modern exception — unchanged.** WD J004917.14$-$252556.81
("J0049$-$2525," Kilic et al. 2023) is a $1.26$–$1.31\,M_\odot$ ultramassive DA white
dwarf, dual-method mass-validated, single-star origin established, plausibly
$\sim1.5$–$2.5$ Gyr old — placing it close to or modestly above cdot-5's ceiling
($1.35$–$2.03$ Gyr for $M_{\text{Ch},0}=1.40$; $1.84$–$2.51$ Gyr for
$M_{\text{Ch},0}=1.44$, reading off the table above at $M=1.27$–$1.30$), essentially the
same boundary tension as cdot-4 found ($1.3$–$2.0$ / $1.8$–$2.5$ Gyr there). At this
age, $\tau\approx1.5$–$2.5$ Gyr, safely within the valid ($\tau<9.1$ Gyr) regime.

### B. Population-level number counts — the direct test, still the primary evidence

Unchanged from cdot-4. Fleury, Caiazzo & Heyl (2022, MNRAS 511, 5984, arXiv:2110.00598)
measured the cumulative cooling-age distribution of Gaia EDR3 white dwarfs in three mass
bins, volume-complete to 200 pc with an explicit incompleteness correction:

- $0.95$–$1.15\,M_\odot$: consistent with the Milky Way SFR (Mor et al. 2019). No
  anomaly.
- $1.15$–$1.25\,M_\odot$ (closest to where cdot-5's ceiling becomes restrictive —
  reading the table above, $\tau_\text{ceiling}\approx2.0$–$3.9$ Gyr across this bin,
  essentially the same range cdot-4 found, $2.0$–$3.8$ Gyr): inconsistent with pure
  single-star formation ($p<10^{-4}$); well fit ($\chi^2_\nu=1.4$) by single-star
  formation plus double-white-dwarf mergers out to $4$ Gyr cooling age, $\sim$40–50% of
  the bin's WDs estimated to be merger products over the last 4 Gyr.
- Authors' conclusion: **"no evidence for a substantial cooling delay... when one takes
  the star formation history of the Galaxy into consideration."**

**Reading this against cdot-5's prediction — unaffected in substance, since both the
model's ceiling and Fleury et al.'s tested range ($\le4$ Gyr) sit comfortably inside the
validated $\tau<9.1$ Gyr regime.** The model predicts $1.20\,M_\odot$ single-star-formed
white dwarfs should vanish beyond $\tau_\text{ceiling}(1.20)\approx2.7$–$3.2$ Gyr; the
data show smooth, undiminished counts through and past this range out to 4 Gyr, fit by
ordinary channel physics with no missing suppression. **This remains a real, if partial,
piece of evidence against the model's central prediction**, exactly as in cdot-4, now
confirmed to sit entirely within the range this document can actually compute — unlike
§D below.

**Scope limitation — unchanged.** Fleury, Caiazzo & Heyl stopped at $1.25\,M_\odot$ and
4 Gyr. The model's sharpest claim (near-total exclusion above $\sim1.3\,M_\odot$ and/or
beyond $\sim3$–$4$ Gyr) is not cleanly probed by their published analysis — still the
single most valuable concrete follow-up.

### C. Merger-remnant magnetic WDs: a useful contrast

Unchanged from cdot-4, both objects' ages sit well inside the valid regime:

- **ZTF J1901+1458** ($1.327$–$1.365\,M_\odot$, cooling age $10$–$100$ Myr): **consistent**
  — comfortably young regardless of bracket (ceiling $\sim0.9$–$1.4$ Gyr at this mass,
  reading the table above).
- **SDSS J2211+1136** ($1.27\,M_\odot$, cooling age $2.61$–$2.85$ Gyr): ceiling is
  $1.76$ Gyr ($M_{\text{Ch},0}=1.40$) or $2.25$ Gyr ($M_{\text{Ch},0}=1.44$) —
  marginal-to-violating by 16–62% (essentially the same tension cdot-4 found, 18–64%).
  As with §A, subject to the same Gaia-recalibration caution.

### D. Second-tier check: globular-cluster CO white dwarf masses — now uncomputable, not merely inconclusive

**This is the section where the counting-law change matters most.** cdot-4 compared
47 Tucanae, M4, and NGC 6397 (ages $11.6$–$13.0$ Gyr) against its own $M_\text{max}(\tau)$
table and found the comparison "inconclusive" (masses sitting at, just inside, or mildly
above the model's ceiling). **Under cdot-5, every one of these ages — $11.6$ to $13.0$
Gyr — falls past the validated boundary, $\tau(z_*)\approx9.1$ Gyr.** The table entries
this document would need (rows at $\tau=11.6$–$13.0$ in the "Maximum stable WD mass"
table above) are explicitly marked *extrapolated*: they use the post-percolation formula
outside its derived domain, on the assumption that the exponential connectivity law
continues unbroken past $z_*\approx1.2$, which T23 explicitly says it does *not* — the
network is subcritical there and the true $c(\tau)$ relation is a different, not-yet-derived
function.

**Consequence.** §D cannot currently be evaluated as either support for or evidence
against the model. This is a genuine loss of a (weak) test relative to cdot-4, not a
gain — cdot-4's "inconclusive" reading was at least a real (if uninformative) comparison
against its own model; cdot-5's equivalent comparison rests on an extrapolation the
model's own author document (T23) flags as unjustified. **Resolving the pre-percolation
$c(\tau)$ relation would immediately make this section computable again** — it is now
the single most direct reason (beyond T23's own stated open items) to prioritize that
derivation, since a real ultra-old open-cluster/globular-cluster WD mass comparison is
exactly the kind of clean, existing dataset that could discriminate once the pre-
percolation branch exists.

*(For completeness, the observed values — 47 Tuc: age $11.8\pm0.5$ Gyr, mass
$\approx0.53\,M_\odot$; M4: age $11.6$–$12.7$ Gyr, mass $\approx0.54\,M_\odot$; NGC 6397:
age $12.8$–$13.0$ Gyr, mass $\approx0.53\,M_\odot$ — are unchanged observational facts,
carried forward from cdot-4 for when the pre-percolation branch is available to compare
against them.)*

### E. Standard cooling ages may overstate true ages (cross-referenced from T21)

T21's investigation into the $c$-scaling of plasmon decay (the dominant neutrino cooling
process in a degenerate WD core) found $\Gamma_\text{plasmon}\propto c^{-1}$ at fixed
density — a **present-value scaling**, unaffected by the counting-law change (T21). What
*is* affected is the conversion of this rate enhancement into an actual age correction,
which needs $c_0/c(\tau)-1$ at the star's formation epoch — exactly the piece redone
above. Using cdot-5's exact linear relation:
$$\frac{c_0}{c(\tau)}-1 = \frac{\tau/\tau_\infty}{1-\tau/\tau_\infty}.$$

| Age $\tau$ (Gyr) | $c(\tau)/c_0$ | Plasmon enhancement, $c_0/c(\tau)-1$ |
|---:|---:|---:|
| 0.5 | 0.982 | 1.8% |
| 1 | 0.964 | 3.7% |
| 2 | 0.928 | 7.7% |
| 3 | 0.893 | 12.0% |
| 4 | 0.857 | 16.7% |
| 5 | 0.821 | 21.8% |
| 6 | 0.785 | 27.4% |
| 8 | 0.714 | 40.1% |

**These are, again, close to cdot-4's table** (1.8%, 3.7%, 7.8%, 12.3%, 17.2%, 22.7%,
28.8%, 43.5%) — the same near-coincidence as the $M_\text{Ch}$ tables above, and for the
same reason (a different exponent and a different $\tau_\infty$ that partially cancel).
**T21's Part 5 conclusion accordingly carries forward essentially unchanged**: the
marginal ceiling-violating objects flagged in §A/§C ($1.03$–$1.15\times$ over) sit at
ages ($\sim1.8$–$4.6$ Gyr, all within the valid regime) where a plausible
$f_\nu\sim0.1$–$0.3$ gives $\Delta A/A$ of order $3$–$13\%$ — enough to fully explain
these on its own; the larger violations ($1.37$–$1.53\times$ over) are only partly
addressed (roughly half the gap). See T21 Part 5 for the full derivation and the honest
accounting of what is solid versus estimated.

**Net effect: unchanged from cdot-4** — this further weakens the case that §A/§C's
original violations reflect genuine tension with the model, on top of the Gaia
mass-systematic. This entire section's ages are all within the validated $\tau<9.1$ Gyr
regime, so it is unaffected by the new percolation caveat (unlike §D).

---

## Caveats and Systematics (ordered by importance)

1. **New: the percolation-break validity boundary (§"Derivation," above).** Every
   result in this document is derived from the post-percolation branch and is only
   established for $\tau\lesssim9.1$ Gyr ($z\lesssim z_*\approx1.2$). This retires §D
   and flags the low-mass rows of both reference tables as extrapolation. It does **not**
   affect §A, §B, §C, or §E, whose objects' ages all sit within the valid range.
2. **Spectroscopic vs. photometric mass systematics (primary caveat for §A/§C).**
   Unchanged from cdot-4 — a data-systematics argument, independent of the counting law.
3. **Binary mass-transfer history (primary caveat specifically for §A/§C, not for §B).**
   Unchanged from cdot-4.
4. **Cooling-age model dependence.** Unchanged: Camisassa et al.'s Table 1 gives, for
   the same $1.10\,M_\odot$ sequence, $8.2$ Gyr (H-rich) vs. $4.6$ Gyr (H-deficient) —
   a factor of $\sim1.8$ from atmosphere composition alone.
5. **Core-composition assumption (CO vs. ONe).** Unchanged.
6. **Un-modeled delayed-cooling physics.** Unchanged.
7. **The Cunningham et al. (2024) Gaia-recalibrated IFMR.** Unchanged.
8. **Selection effects.** Unchanged — §B's volume-complete sample largely addresses
   this; §A and §C do not.
9. **Normalization sensitivity** ($M_{\text{Ch},0}=1.40$ vs. $1.44\,M_\odot$; $H_0=70$
   vs. $73$ km/s/Mpc). Unchanged in kind; the specific shifted values are given in the
   tables above.
10. **The §E cooling-age correction applies to §B as well as §A/§C.** Unchanged from
    cdot-4 — Fleury, Caiazzo & Heyl's cooling ages are standard, no-time-variation
    estimates and could themselves overstate the true ages entering §B's "no deficit"
    finding.

---

## Verdict

**What the evidence shows — largely unchanged from cdot-4, with one section removed.**
The individual-object "34%/18% violate the ceiling" headline (§A) remains untrustworthy
for the same Gaia spectroscopic-mass-bias reasons as in cdot-4, and the numbers barely
move under the recomputed cdot-5 tables. T21's cooling-age correction (§E) is likewise
essentially unchanged and continues to plausibly resolve the marginal violations and cut
the larger ones roughly in half. §B, the population-level test, remains the best
available evidence and remains **currently inconclusive rather than a clean strike
against the model** for the same reason as before (the cooling-age systematic, §E/caveat
10), with its specific numbers essentially unchanged by the counting-law switch since it
operates entirely within the validated regime.

**What changed: §D is gone, and that is itself informative.** cdot-4 could offer a
weak, if inconclusive, comparison against globular-cluster white dwarf ages because its
single power law had no domain boundary. cdot-5's connectivity law has one — the
percolation transition at $z_*\approx1.2$ — and the oldest, most age-informative white
dwarfs in the Galaxy (globular-cluster members, $11.6$–$13.0$ Gyr) sit *past* it. This
is not a defect specific to this topic; it is the same gap Core Principles §7 and T1's
own Open Questions already flag as the most consequential unfinished derivation in the
current model (the pre-percolation $c(\tau)$ relation) — T20 is simply the topic where
that gap has the sharpest observational consequence, since it is precisely the oldest
objects that would test the ceiling most stringently.

**Framing 1 (pessimistic for the model, but not decisively so).** Even after the
cooling-age correction, §B's raw finding (no deficit in the data as currently aged)
still stands as the best available population test in the regime this document can
compute, and should be treated as suggestive evidence against the model, not decisive,
until redone with corrected ages.

**Framing 2 (honest and open).** Two lines of evidence against the model (§A, §B) carry
real, quantified reasons for skepticism (Gaia mass bias, cooling-age overstatement); a
third potential line (§D) has been removed from consideration entirely, pending a
derivation this document does not attempt. The appropriately hedged statement: **the
model's sharpest, most falsifiable prediction for this topic — a population deficit of
old, massive white dwarfs — has neither been confirmed nor cleanly refuted, and the one
dataset (globular clusters) old enough to test it most directly is now explicitly
outside what the current model can predict.**

---

## Open Questions

1. **[Highest priority, new]** Derive the pre-percolation ($z>z_*$) branch's $c(\tau)$
   relation (T23's own top open item, now also this document's) — this is the single
   change that would make §D computable again and would extend the validity of every
   table in this document to arbitrarily old ages.
2. **[Highest priority, actionable, unchanged from cdot-4]** Re-derive masses and
   cooling ages for the specific objects flagged as ceiling violations in §A, using Gaia
   DR3 astrometry and the photometric method, before treating any of them as evidence
   again.
3. **[Highest priority, actionable, unchanged from cdot-4]** Obtain a real, numerical
   value for T21's $f_\nu(M)$ by re-running a standard WD cooling code with the
   $c$-varying neutrino rate built in (now using cdot-5's exact linear $c(\tau)$ in place
   of cdot-4's power law), and use it to properly correct the cooling ages used
   throughout §A–§C.
4. **[Highest priority, most decisive, unchanged from cdot-4]** Extend the Fleury,
   Caiazzo & Heyl (2022) methodology to $1.25$–$1.40\,M_\odot$ and to cooling ages beyond
   4–5 Gyr — still entirely within the validated $\tau<9.1$ Gyr regime, so this remains
   fully computable and remains the single measurement most likely to settle this topic.
5. Quantify the plausible contamination of "isolated" massive-WD samples by detached
   post-mass-transfer objects — unchanged from cdot-4.
6. Obtain a firm, published cooling age for WD J0049$-$2525 — unchanged from cdot-4.
7. Fold the Cunningham et al. (2024) Gaia-recalibrated IFMR into the baseline — unchanged.
8. A rigorous population-synthesis calculation convolving $\tau_\text{ceiling}(M)$ with
   a realistic SFR, merger delay-time distribution, and accretion channel — unchanged in
   scope, now automatically restricted to $\tau<9.1$ Gyr predictions until item 1 is
   resolved.
9. Formal error propagation for future individual-object comparisons — unchanged.
10. SN Ia delay-time distribution cross-check — unchanged, intertwined with item 5.
11. Once item 1 is resolved, redo §D with the actual pre-percolation $\tau(z)$ mapping
    and the real globular-cluster ages/masses — the most direct payoff of resolving
    T23's own top open item.
12. Cluster age/mass refinement for a future §D using JWST-based cooling-sequence ages
    (e.g. Bedin et al. 2025 for M4) — unchanged from cdot-4, useful once item 1 makes
    the comparison meaningful again.
