# T20 — The White Dwarf Population and the Chandrasekhar-Mass Ceiling

*Status: new topic, proposed for merge. Renumbered from T19 → T20 (T19 already in use).
Cross-references T1 (age/lookback-time formulas), T4 (origin of the
$M_\text{Ch}\propto c^{3/2}$ result), T8 (invariant $G$), T12 (relational principle),
T21 (strong/weak sector coupling — source of the §E cooling-age correction).
Session dates: 2026-07-01 (initial), 2026-07-01 (follow-up revision after
clarification questions on Gaia data and population counts), 2026-07-01 (correction:
formation-epoch definition refined to account for binary mass-transfer/accretion
history), 2026-07-01 (§E added: cooling-age-overstatement correction from T21's
plasmon-decay result, with revised Verdict).*

---

## Physical Concept

T4 already establishes that under invariant $G$, invariant $\hbar$, and invariant $m_p$,
the Chandrasekhar mass scales as $M_\text{Ch}\propto c^{3/2}$, and that because $c$ was
smaller in the past, high-redshift SNe Ia detonate at lower mass and are intrinsically
fainter — a systematic that competes with the model's $q_0=+1/6$ kinematic signature on
the Hubble diagram.

This document asks a different, and in some ways much sharper, question: **standard
candles are not the only Chandrasekhar-mass objects in the sky. Every white dwarf near
the top of the mass distribution is one.** If $M_\text{Ch}$ was lower in the past, then no
stable white dwarf, anywhere, at any time, could have formed with a mass exceeding the
value of $M_\text{Ch}$ that prevailed at its own formation epoch. Since $c(t)$ is a
monotonically increasing function of cosmic time in this model, this creates a **hard
ceiling on how old a massive white dwarf is allowed to be**, purely as a function of its
mass — independent of composition, formation channel (single-star or double-degenerate
merger), and independent of all the unresolved SN-specific physics in T4 (the sign of
$q$, the Phillips-relation absorption, the $^{56}$Ni yield/opacity argument).

A direct corollary, and the one this revision focuses on: the model predicts that
**massive white dwarfs should be systematically rarer than ordinary stellar-evolution
population synthesis predicts, specifically among the ones old enough to have cooled** —
i.e. a *deficit*, not merely a spread of individual outliers. This is the sharper and more
falsifiable form of the claim, and it is the one directly tested in the revised §B below.

**Why the formation channel does not matter — and what "formation epoch" precisely
means (corrected).** A single star's degenerate core cannot exceed $M_\text{Ch}(t)$ at
the time it stops growing. A double-degenerate merger remnant cannot exceed
$M_\text{Ch}(t)$ at the time of the merger either — if the combined mass exceeds the
ceiling at that epoch, the standard expectation is a thermonuclear explosion (SN Ia),
not a stable merger remnant. **A third channel must be added to this list, and it
changes what "$\tau$" is allowed to mean:** a white dwarf that is, or has been, in a
mass-transferring binary — a cataclysmic variable (CV) accreting from a
main-sequence/subgiant donor, a nova system, or a detached remnant that has fully
accreted or engulfed a low-mass (dM or brown-dwarf) companion — can grow *after* its own
original formation, and is bound by $M_\text{Ch}(t)$ only at the epoch its mass last
changed, not at its original (single-star) birth. So the correct, general statement is:
$$M \le M_\text{Ch}(\tau_\text{last mass-set}),$$
where $\tau_\text{last mass-set}$ is the lookback time to the star's most recent
significant mass-changing event of *any* kind (core-growth completion, merger, or
cessation of binary accretion) — not necessarily its birth. The ceiling itself is still
channel-independent (the physics constraining $M_\text{Ch}(t)$ doesn't care how the mass
was assembled), but it is no longer safe to equate "the object's mass" with "its
single-star formation epoch" without checking the object's binary history.

**Why this matters for the cooling-age comparisons in this document.** Every
comparison in §A–§D infers $\tau$ from the star's present $T_\text{eff}/\log g$ via a
*passive-cooling* model track — implicitly assuming the star has simply cooled,
undisturbed, since a single mass-setting event. This assumption is safe for isolated
single-star-evolution products and is a reasonable approximation for merger remnants
(with the caveat, already noted by Temmink et al. 2020 and discussed under §B, that
naive single-star cooling models tend to *underestimate* a merger remnant's true age).
It is **not** safe for an object with a history of binary accretion: ongoing or recent
mass transfer thermally rejuvenates the white dwarf (accretion/compressional heating),
so a naive cooling-age fit to such an object is not a reliable measure of time since its
mass was last set, and the direction of the resulting bias is not obviously the same as
the merger case. Actively accreting CVs are generally easy to exclude — they show
disk emission lines, orbital photometric variability, and colours off the single-WD
cooling track, and are not the kind of object that would enter the SDSS DA/DB or Gaia
EDR3 "isolated white dwarf" catalogues used throughout this document. The genuinely hard
case is a **detached post-mass-transfer object** — a former nova/CV or common-envelope
system whose donor has been fully consumed or has itself become a much fainter remnant —
which can relax back onto what looks exactly like an ordinary single-WD cooling track
with no surviving observational signature of its accretion history. Such an object would
pass every selection cut used in §A–§D while having a "formation epoch," in the sense
relevant to this ceiling, that is set by *when accretion stopped* rather than by its
progenitor's birth. This is flagged as an unresolved caveat below and does not currently
have a quantified size.

---

## Derivation

### From $c(\tau)$ to $M_\text{Ch}(\tau)$

T1 gives the coordinate-lookback solution (Core Principles §3, volume law):
$$\frac{c(u)}{c_0} = \big(1+2kR_0^2\,u\big)^{-3/2}, \qquad
\frac{d\tau}{dt} = \left(\frac{c(t)}{c_0}\right)^2,$$
where $u$ is coordinate lookback time and $\tau$ is proper (atomic-clock) lookback time.
Writing $y \equiv 1+2kR_0^2 u$ and integrating as in T1's derivation of $\tau_\text{total}$:
$$\tau(u) = \tau_\infty\left[1-y^{-2}\right], \qquad \tau_\infty \equiv \frac{3}{2H_0^\text{obs}} \approx 20.95\ \text{Gyr (}H_0=70\text{)}.$$
Inverting for $y$ and substituting back into $c(u)/c_0 = y^{-3/2}$:
$$\boxed{\frac{c(\tau)}{c_0} = \left(1-\frac{\tau}{\tau_\infty}\right)^{3/4}}$$
This is an exact restatement of the same $c$–$\tau$ map already used throughout T1–T4; no
new premise is introduced. Combining with T4's $M_\text{Ch}\propto c^{3/2}$:
$$\boxed{\frac{M_\text{Ch}(\tau)}{M_{\text{Ch},0}} = \left(1-\frac{\tau}{\tau_\infty}\right)^{9/8}}$$
i.e. the maximum possible white-dwarf mass **falls off slightly faster than linearly**
with lookback time. Inverting, the **age ceiling** for a white dwarf of mass $M$ is:
$$\boxed{\tau_\text{ceiling}(M) = \tau_\infty\left[1-\left(\frac{M}{M_{\text{Ch},0}}\right)^{8/9}\right]}$$
This uses only premises already adopted in Core Principles (invariant $G,\hbar,m_p$; the
volume-law $c(t)$; $P=2$) and T1's own lookback-time solution — no new free parameter,
and (unlike T4) no dependence on the unresolved sign of $q$.

### Reference tables ($H_0=70$ km/s/Mpc, $\tau_\infty=20.95$ Gyr)

Two brackets for $M_{\text{Ch},0}$ are carried throughout: $1.40\,M_\odot$ (textbook
$\mu_e=2$ value) and $1.44\,M_\odot$ (the larger, GR/finite-temperature corrected value
sometimes quoted).

**Maximum stable WD mass as a function of age $\tau$:**

| $\tau$ (Gyr) | $M_\text{max}$ ($M_{\text{Ch},0}=1.40$) | $M_\text{max}$ ($M_{\text{Ch},0}=1.44$) |
|---:|---:|---:|
| 0.5 | 1.362 | 1.401 |
| 1 | 1.325 | 1.363 |
| 2 | 1.251 | 1.286 |
| 3 | 1.177 | 1.210 |
| 4 | 1.103 | 1.135 |
| 5 | 1.030 | 1.060 |
| 8 | 0.815 | 0.838 |
| 10 | 0.675 | 0.694 |
| 12 | 0.538 | 0.553 |
| 13 | 0.471 | 0.484 |
| 13.4 | 0.444 | 0.457 |

**Age ceiling as a function of mass $M$:**

| $M\ (M_\odot)$ | ceiling (Gyr), $M_{\text{Ch},0}=1.40$ | ceiling (Gyr), $M_{\text{Ch},0}=1.44$ |
|---:|---:|---:|
| 0.60 | 11.09 | 11.33 |
| 0.80 | 8.21 | 8.53 |
| 1.00 | 5.42 | 5.80 |
| 1.10 | 4.04 | 4.46 |
| 1.15 | 3.36 | 3.80 |
| 1.20 | 2.68 | 3.14 |
| 1.25 | 2.01 | 2.48 |
| 1.27 | 1.74 | 2.21 |
| 1.30 | 1.34 | 1.82 |
| 1.33 | 0.93 | 1.43 |
| 1.35 | 0.67 | 1.17 |
| 1.38 | 0.27 | 0.78 |
| 1.40 | 0.00 | 0.52 |

Raising $H_0$ to the local distance-ladder value ($73$ km/s/Mpc, $\tau_\infty\approx20.1$
Gyr) shrinks every entry by a further $\sim4\%$, i.e. it **tightens**, not relaxes, the
ceilings.

---

## Confrontation with Data

### A. Individual field ultra-massive white dwarfs — retracted as primary evidence pending Gaia re-derivation

The initial version of this document compared 44 literature ultra-massive white dwarfs
(compiled in Camisassa et al. 2019, A&A, "The evolution of ultra-massive white dwarfs,"
arXiv:1807.03894) against $\tau_\text{ceiling}(M)$ and found 15/44 (34%, $M_{\text{Ch},0}=1.40$)
to 8/44 (18%, $M_{\text{Ch},0}=1.44$) individual objects exceeding the ceiling.

**This comparison has a serious, specific problem that was not checked in the initial
pass: nearly every mass in that table comes from *pure spectroscopic* fits (SDSS
Kleinman et al. 2013, Kepler et al. 2015/2016, Curd et al. 2017, Nitta et al. 2016,
Gianninas et al. 2011, Mukadam et al. 2004) — i.e. model-atmosphere fits to $\log g$ and
$T_\text{eff}$ from spectroscopy alone, with no distance/parallax information.** A large
and well-documented body of post-Gaia work has shown that this method carries a
systematic bias, particularly severe for the highest-$\log g$ (most massive) objects:

- Genest-Beaulieu & Bergeron (2019, ApJ, arXiv:1901.01857) directly compared SDSS
  spectroscopic masses to Gaia-parallax-based photometric masses for the same DA/DB
  stars and found systematic discrepancies traceable to line-broadening physics in the
  spectroscopic models.
- A 2026 DESI DR1 model-atmosphere analysis (IOPscience, DOI 10.3847/1538-4357/ae43ee)
  found "a significant discrepancy between the photometric and spectroscopic masses for
  DA white dwarfs (**a systematic offset of 0.05–0.06 $M_\odot$**), indicating problems
  with the broad hydrogen line profiles in [pure] spectroscopy data," with photometric
  fits instead consistent with the canonical $0.6\,M_\odot$ peak.
- **Concrete individual examples, several involving objects in or adjacent to our own
  sample:**
  - **GD 518**: spectroscopic mass $1.20\,M_\odot$ (Gianninas et al. 2011; used in our
    original table) → **$1.114\pm0.006\,M_\odot$** once refit with Gaia parallax + the
    Bergeron et al. (2019) photometric method (Kilic et al. 2025). A downward revision
    of $0.086\,M_\odot$.
  - **BPM 37093**: $1.097\,M_\odot$ (Nitta et al. 2016; used in our original table) →
    **$1.037\pm0.008\,M_\odot$** (O'Brien et al. 2024), though other recent compilations
    still quote $\sim1.13\,M_\odot$ (Bédard et al. 2017) — the spread between recent
    determinations ($1.04$–$1.13\,M_\odot$) is itself informative about the size of
    current systematic uncertainty for this object class.
  - **SDSS J084021.23+522217.4** (in our original table at $M=1.139\,M_\odot$, Curd et
    al. 2017, spectroscopic): revised down to **$0.98\pm0.04\,M_\odot$** by Vincent et
    al. (2024) using the photometric method — a $0.159\,M_\odot$ downward revision that
    would remove it from the "ultra-massive" category entirely.

**Assessment.** Since essentially every object in the original 44-object table shares the
exact data provenance (pre-Gaia, pure-spectroscopic SDSS fits) that has now been shown,
in multiple independent studies and in at least three concrete individual cases, to
overestimate mass by typically $0.05$–$0.16\,M_\odot$ — an amount comparable to or larger
than what is needed to move most of the flagged "violations" back under the ceiling (the
ceiling is a steep function of mass in this regime: e.g. dropping $M$ from $1.242$ to
$1.18\,M_\odot$ raises the $M_{\text{Ch},0}=1.40$ ceiling from $2.12$ to roughly $3.3$
Gyr) — **the individual-object test as originally constructed is not currently reliable
evidence either for or against the model.** It is retracted as a primary line of
evidence pending a proper re-derivation of the specific flagged objects' masses using
Gaia DR3 astrometry and the photometric method (Bergeron et al. 2019 technique), which
has not been done here. This is listed as the top item in Open Questions below. The
original table is retained for reference in the session log, clearly flagged as
superseded.

**One promising modern exception.** WD J004917.14$-$252556.81 ("J0049$-$2525," Kilic et
al. 2023, MNRAS 522, 2181) is a $1.26$–$1.31\,M_\odot$ ($T_\text{eff}=13{,}020$ K,
$\log g = 9.34$) ultramassive DA white dwarf whose parameters were cross-validated by
*both* the spectroscopic and Gaia-parallax photometric methods, which agree within
errors — unlike the objects above. It shows no kinematic, magnetic, or rotational
signature of a merger origin, so it is very likely a genuine single-star (ONe or CO
core) product. It is $>99\%$ crystallized. Its precise cooling age has not yet been
published in the literature reviewed here; based on its $T_\text{eff}$ and crystallized
fraction it plausibly falls in the $\sim1.5$–$2.5$ Gyr range by comparison with the
Camisassa et al. (2019) cooling tracks for similar mass, which would place it close to
or modestly above the model's ceiling ($1.3$–$2.0$ Gyr for $M_{\text{Ch},0}=1.40$;
$1.8$–$2.5$ Gyr for $M_{\text{Ch},0}=1.44$, at this mass) — i.e. right at the boundary,
not a clean call either way. Obtaining a firm published cooling age for this object is
flagged as a priority open question: it is currently the single best individual
benchmark available (modern data, dual-method mass validation, single-star origin
established), superior to anything in the original Camisassa-compiled table.

### B. Population-level number counts — the direct test of "sparser," and the primary evidence in this revision

This is the test the model actually needs to pass: **not** "is any individual object's
point-estimate mass/age pair inconsistent," but "does the *number* of massive white
dwarfs, as a function of cooling age, fall off faster than ordinary (non-VSL) stellar
population synthesis predicts, once cooling age approaches the model's ceiling."

Fleury, Caiazzo & Heyl (2022, MNRAS 511, 5984, arXiv:2110.00598) performed almost
exactly this measurement, using a volume-complete (200 pc), Gaia EDR3 photometric
(not spectroscopic) sample, with an explicit incompleteness correction (Schmidt
$V/V_\text{max}$-style weighting) as a function of absolute magnitude. This sidesteps
both the SDSS spectroscopic-mass bias in §A and the more basic worry that a
flux-limited sample under-represents old, faint objects. Their findings, precisely
stated:

- For $0.95$–$1.15\,M_\odot$ (two lightest of their three mass bins): the cumulative
  cooling-age distribution **is** statistically consistent with the independently known,
  time-varying Milky Way star-formation rate (Mor et al. 2019, from Gaia DR2 main-sequence
  stars) — including reproducing the $2$–$3$ Gyr-old star-formation burst as a genuine
  pile-up of WDs at the corresponding cooling age. **No anomaly, no deficit, no excess.**
- For $1.15$–$1.25\,M_\odot$ (their heaviest bin — closest to the mass range where the
  model's ceiling becomes restrictive, $\tau_\text{ceiling}\approx2.0$–$3.8$ Gyr across
  this bin): the cumulative distribution is **inconsistent** with pure single-star
  formation tracing the SFR (KS-test $p<10^{-4}$ for every cooling-model choice tested).
  Instead, the cooling-age distribution is close to **uniform** over $1$–$2.5$ Gyr
  (KS $p=0.25$–$0.98$ against a uniform distribution, depending on the cooling model),
  and is well fit (down to $\chi^2_\nu=1.4$) by a combination of single-star formation
  plus double-white-dwarf merger products, extending the fitted histogram out to $4$ Gyr
  of cooling age, with $\sim$40–50% of the bin's WDs formed over the last 4 Gyr estimated
  to be merger products (rising to 70–80% for those forming today).
- The authors' own stated conclusion: **"we find no evidence for a substantial cooling
  delay in the numbers of massive white dwarfs detected in Gaia EDR3 when one takes the
  star formation history of the Galaxy into consideration."** I.e., ordinary
  astrophysics (a known SFR history convolved with a known, independently-estimated
  double-degenerate merger delay-time distribution, Cheng et al. 2020) is *sufficient* to
  explain the observed counts at every cooling age tested, with no missing suppression
  and no extra mass ceiling required.

**Reading this against the model's prediction.** The model predicts that the number
density of, say, $1.20\,M_\odot$ single-star-formed white dwarfs should fall to
essentially **zero** beyond $\tau_\text{ceiling}(1.20)\approx2.7$–$3.1$ Gyr (and, per the
formation-channel argument above, this applies to *any* surviving stable remnant of that
mass regardless of channel — a $1.20\,M_\odot$ merger product formed via merger events
more than $\sim3$ Gyr ago should be equally forbidden, since $M_\text{Ch}$ at that earlier
epoch was itself below $1.20\,M_\odot$). What is actually observed, in a
completeness-corrected, Gaia-photometric (not spectroscopic) sample, is a population that
continues smoothly — with no visible cutoff, dip, or deficit — right through this range
and fits well when extended to 4 Gyr, using only ordinary formation-channel physics. **This
is a real, if partial, piece of evidence against the model's central prediction for this
topic.** It is more trustworthy than the individual-object comparison in §A because (i)
it uses the photometric method throughout, avoiding the spectroscopic mass bias, and (ii)
it is explicitly volume/completeness-corrected rather than a hand-collected literature
sample, and (iii) — importantly, given the formation-epoch correction above — **it is a
raw number-count comparison, not an attribution of individual objects to a channel**, so
it is unaffected by the single-degenerate/CV-accretion complication discussed in the
Physical Concept section: whatever mix of single-star, merger, and (unmodelled by Fleury
et al.) single-degenerate-accretion channels actually produced these objects, the
observed *count* of them at each cooling age is what it is, and that count shows no
deficit. (The single-degenerate channel, if present at a non-negligible rate, would if
anything make the "no deficit" finding *more* robust, since a WD that gradually grows to
$1.2\,M_\odot$ via accretion ending recently is fully permitted by the model at any
cooling age — its true $\tau_\text{last mass-set}$ is small — so this channel cannot be
invoked to rescue the model's prediction of an observed deficit; it can only ever add to
the observed count, never subtract from it. See the additional Physical Concept
paragraph above for how it does complicate the individual-object tests in §A/§C — where
the specific *cooling age* assigned to any one object, not just its existence, is being
compared to the ceiling — because a formerly-accreting object may retain no observable
mass-transfer signature.)

**Important scope limitation.** Fleury, Caiazzo & Heyl stopped at $1.25\,M_\odot$ and at
a 4 Gyr cooling-age ceiling for their histogram fit (beyond which their own
incompleteness weighting becomes unreliable, by their own statement). The model's
prediction becomes most dramatic — a near-total, sharp exclusion — only above
$\sim1.3\,M_\odot$ and/or beyond $\sim3$–$4$ Gyr, precisely the regime their published
analysis does not cleanly probe. So while this is genuine, relevant, and currently the
best available population-level evidence, **it is not yet a complete test of the
model's sharpest claim**, which lives at higges masses and/or longer cooling ages than
this specific study covers. A dedicated extension of the same volume-complete,
completeness-corrected methodology to $1.25$–$1.40\,M_\odot$ and to cooling ages beyond
4–5 Gyr does not appear to exist yet in the literature reviewed here, and is the single
most valuable concrete follow-up identified in this session (see Open Questions).

### C. Merger-remnant magnetic WDs: a useful contrast (unchanged from initial version, still relevant)

Two well-studied high-field magnetic ultra-massive WDs, reconstructed as likely
double-degenerate merger products by Bhattacharya et al. (2022, ApJ, DOI
10.3847/1538-4357/aca015):

- **ZTF J1901+1458** ($1.327$–$1.365\,M_\odot$, cooling age $10$–$100$ Myr under a
  single-star clock): **consistent** with the model — comfortably young enough regardless
  of the $M_{\text{Ch},0}$ bracket used ($0.9$–$1.4$ Gyr ceiling at this mass).
- **SDSS J2211+1136** ($1.27\,M_\odot$, cooling age $2.61$–$2.85$ Gyr): ceiling is
  $1.74$ Gyr ($M_{\text{Ch},0}=1.40$) or $2.21$ Gyr ($M_{\text{Ch},0}=1.44$) —
  marginal-to-violating by 18–64%. As with §A, this object's mass and cooling age derive
  from spectroscopic/photometric methods that have not been explicitly checked here
  against the Gaia-recalibration concerns raised above, so this single-object comparison
  should also be treated with the same caution as §A pending independent confirmation.

The qualitative pattern (the most extreme-mass object is essentially newborn, exactly as
required; tension appears specifically among slightly less extreme but *older* massive
objects) is still a sensible fit to the mechanism, but per the §A findings — and per the
binary mass-transfer caveat in the Physical Concept section and Caveat 2 below — none of
these individual point-estimates should be treated as decisive on their own. Both
benchmark objects here happen to be merger candidates specifically *because* they show
independent merger signatures (magnetism, rapid rotation); a hidden single-degenerate
accretion history, by contrast, need leave no such signature, so it cannot be ruled out
for either object without dedicated follow-up.

### D. Second-tier check: globular-cluster CO white dwarf masses (unchanged)

| Cluster | Age (Gyr) | Typical CO WD mass | Model $M_\text{max}$ (1.40 / 1.44) |
|---|---:|---:|---:|
| 47 Tucanae | $11.8\pm0.5$ | $\approx0.53\,M_\odot$ | $0.54$ / $0.56$ |
| M4 (NGC 6121) | $11.6$–$12.7$ | $\approx0.54\,M_\odot$ (Cummings et al. 2018) | $0.53$–$0.47$ / $0.55$–$0.49$ |
| NGC 6397 | $12.8$–$13.0$ | $\approx0.53\,M_\odot$ | $0.47$–$0.48$ / $0.48$–$0.49$ |

Still inconclusive: 47 Tuc and M4 sit at or just inside the ceiling; NGC 6397 sits
mildly ($\sim10$–$15\%$) above it. Given age uncertainties ($\pm0.5$–$0.7$ Gyr) and mass
uncertainties ($\sim0.02$–$0.03\,M_\odot$), this neither rescues nor worsens the picture.

### E. A candidate resolution for the remaining violations: standard cooling ages may overstate true ages (new, cross-referenced from T21)

A companion investigation (T21) into how nuclear and weak-interaction physics couple to
$c$ — prompted by the concern that a naive $M_\text{Ch}\propto c^{3/2}$ might not be the
whole story — worked out the $c$-scaling of **plasmon decay**, the dominant neutrino
cooling process in a degenerate white-dwarf core, and found $\Gamma_\text{plasmon}
\propto c^{-1}$ at fixed density: neutrino cooling was *more* efficient in the past.

This has a direct, favorable consequence for every age used in §A–§D above. All of
those ages come from **standard cooling models that assume no time variation in the
underlying physics**. If early-time neutrino cooling was really enhanced, a real white
dwarf is fainter, at any true age, than those standard models predict for that age —
and since standard models are inverted (luminosity → age) as a decreasing function,
**standard cooling ages systematically overstate the true age**. T21's order-of-magnitude
estimate (energy-budget argument via the Mestel cooling law, with one admittedly
uncertain input, $f_\nu(M)$, bounded from real cooling-model literature) suggests
corrections of order a few percent up to $\sim10$–$20\%$ of the reported age, growing
with both age and mass.

Applied directly to this document's §A/§C violations: the **marginal cases** (ratios
$1.03$–$1.15$: SDSS J110054.91, J232257.27, J093710.25, J102553.68) fall well within
what this mechanism alone could plausibly explain — meaning §A's already-flagged
retraction (for Gaia mass-bias reasons) may not even be necessary for these specific
objects; a mundane, real physical effect could fully account for them. The **larger
violations** (SDSS J234044.83 at $53\%$ over, SDSS J100944.29 at $37\%$ over) are only
partly addressed (roughly half the gap, under generous assumptions) — these still most
plausibly need the Gaia mass-revision issue (§A) to close the rest.

**Net effect: this further weakens the case that §A/§C's original violations reflect
genuine tension with the model**, on top of the mass-systematic already discussed. See
T21 Part 5 for the full derivation, the honest accounting of what is solid (the plasmon
rate scaling) versus estimated ($f_\nu(M)$), and the recommended next step (a real
numerical cooling-model re-calculation).

---

## Caveats and Systematics (revised, reordered by importance)

1. **Spectroscopic vs. photometric mass systematics (primary caveat for §A/§C).** As
   detailed in §A, pure-spectroscopic SDSS masses for high-$\log g$ DA white dwarfs are
   now known to run systematically $0.05$–$0.16\,M_\odot$ high relative to
   Gaia-parallax-based photometric masses. Any comparison using the older literature
   values (which is most of the historical ultra-massive-WD catalogue) inherits this bias
   in the direction that *manufactures* apparent ceiling violations. This should be
   resolved before the individual-object test (§A) is used as evidence again.
2. **Binary mass-transfer history (new; primary caveat specifically for individual-object
   tests §A/§C, not for the population-count test §B).** As discussed in the Physical
   Concept section, the ceiling strictly bounds mass at the epoch of a star's *last*
   significant mass-changing event, which for a former cataclysmic variable, nova system,
   or common-envelope/engulfment remnant can be much more recent than the progenitor's
   birth. A detached post-mass-transfer object can relax onto an ordinary-looking
   single-WD cooling track with no retained observational signature of its accretion
   history, so it would not be excluded by any cut used in the literature cited here. This
   means any *individual* object's naive cooling-age fit (§A, §C) could in principle be
   too old relative to its true last-mass-set epoch, which would work in the direction of
   *manufacturing* apparent violations exactly as caveat 1 does — the two caveats compound
   rather than cancel for §A/§C. It does **not** affect the raw-number-count logic of §B
   (see the discussion inline in that section): a count of objects at a given cooling age
   is unaffected by which channel produced them, and this channel could not itself explain
   away an observed *deficit*, since it can only add to the count, never suppress it. The
   size of this effect (what fraction of apparently-isolated massive WDs have an
   undetected accretion history) is not currently quantified.
3. **Cooling-age model dependence.** Camisassa et al.'s own Table 1 gives, for the same
   $1.10\,M_\odot$ sequence, $8.2$ Gyr (H-rich) vs. $4.6$ Gyr (H-deficient) to reach the
   same low luminosity — a factor of $\sim1.8$ from atmosphere composition alone.
4. **Core-composition assumption (CO vs. ONe)** shifts both the inferred mass and cooling
   age at fixed $\log g/T_\text{eff}$, particularly above $\sim1.29\,M_\odot$.
5. **Un-modeled delayed-cooling physics** (crystallization latent heat and phase
   separation are already included in modern models; possible $^{22}$Ne sedimentation /
   distillation is not always included and, per Camisassa/Blouin/Bauer-type work, would
   generally *lengthen* cooling ages further — worsening rather than relieving any
   apparent tension for the population test in §B, and pulling in the *opposite* direction
   from caveat 1 for the individual-object test in §A).
6. **The Cunningham et al. (2024) Gaia-recalibrated initial-final mass relation** predicts
   *fewer* ultramassive ($\gtrsim1\,M_\odot$) white dwarfs from ordinary single-star
   evolution than the older Cummings et al. (2018) IFMR used implicitly in most of the
   literature cited here. This lowers the "ordinary astrophysics" baseline that any
   deficit would need to be measured against, and has not yet been folded into either
   §A or §B.
7. **Selection effects** in flux-limited (non-volume-complete) samples bias against
   old, faint, massive WDs; §B's use of a volume/completeness-corrected sample largely
   addresses this, but §A and §C do not.
8. **Normalization sensitivity** ($M_{\text{Ch},0}=1.40$ vs. $1.44\,M_\odot$; $H_0=70$
   vs. $73$ km/s/Mpc) shifts every ceiling by a modest, quantified amount (see tables
   above) but does not change the qualitative picture.
9. **The §E cooling-age correction applies to §B as well as §A/§C.** Fleury, Caiazzo &
   Heyl's cooling ages (§B) are derived from the same class of standard, no-time-variation
   cooling models as §A/§C. If those ages overstate true ages by the amounts estimated in
   T21 Part 5, the true ages of the $1.15$–$1.25\,M_\odot$ population would skew younger
   than reported — meaning §B's "no deficit" finding, taken as evidence *against* the
   model, is itself weakened: some of the population currently read as "up to 4 Gyr old"
   could genuinely be younger and comfortably under the model's ceiling, without needing
   any merger-channel or SFR-based explanation at all. This does not overturn §B's
   qualitative finding (ordinary astrophysics fits the counts), but it means §B should
   not be treated as a clean, correction-free test either.

---

## Verdict (revised)

**What changed in this revision.** The original individual-object "34%/18% violate the
ceiling" headline result is **not currently trustworthy** — essentially every flagged
object's mass comes from a measurement method now documented to run high by an amount
comparable to what is needed to erase the violation. This is a genuine, self-critical
correction, not a minor caveat: §A should not be cited as evidence until the specific
objects are redone with Gaia photometric masses. A second, independent effect (§E,
from the companion T21 investigation) points the same way: standard cooling ages
plausibly *overstate* true ages by a mass- and age-dependent amount (a few percent up
to $\sim10$–$20\%$), which on its own is enough to explain §A/§C's marginal violations
and meaningfully cuts into the larger ones.

**What the population-level evidence (§B) actually shows, and why it now carries less
unqualified weight than the previous revision suggested.** In the one mass/age regime
where a proper, systematics-aware, volume-complete measurement exists ($1.15$–
$1.25\,M_\odot$, cooling ages up to $\sim4$ Gyr), the data show **no deficit relative to
ordinary astrophysics**: a star-formation-rate-driven population at low mass, and a
well-understood merger-dominated population at the top of this range, together explain
the observed numbers with no need for — and no evidence of — any additional suppression
of the kind this model requires. This is still more credible than the retracted §A
result, because it does not share the *spectroscopic* mass-bias systematic. But it
*does* share the cooling-age systematic (§E/§9 above): if standard ages overstate true
ages, some of the population currently read as approaching the model's ceiling could in
reality sit comfortably under it. §B is therefore best read as **currently inconclusive
rather than a clean strike against the model** — a real, useful population-level test
whose age axis itself needs the same correction being investigated for §A.

**Framing 1 (pessimistic for the model, but less confidently so than the previous
revision).** Even after both corrections above, the sharpest, most falsifiable form of
this topic's prediction — a population-level deficit of old massive white dwarfs — has
not been convincingly demonstrated to fail. §B's raw finding (no deficit in the data as
currently aged) still stands as the best available population test, and until it is
redone with corrected ages, it should be treated as suggestive evidence against the
model, not decisive.

**Framing 2 (increasingly honest and open).** Between the Gaia spectroscopic-mass-bias
issue (§A) and the cooling-age-overstatement issue (§E, from T21), both of this
document's two lines of evidence against the model — individual objects and the
population-level test — now carry real, quantified reasons for skepticism that did not
exist in the first version of this document. Neither correction has been applied
numerically to the underlying data (both require re-running real models: Gaia
photometric mass fits for §A, and a $c$-varying cooling code for §E) — this document
identifies the corrections and estimates their plausible size, but the underlying
literature values used throughout §A–§D have not themselves been revised.

**Framing 2 (increasingly honest and open).** Between the Gaia spectroscopic-mass-bias
issue (§A) and the cooling-age-overstatement issue (§E, from T21), both of this
document's two lines of evidence against the model — individual objects and the
population-level test — now carry real, quantified reasons for skepticism that did not
exist in the first version of this document. Neither correction has been applied
numerically to the underlying data (both require re-running real models: Gaia
photometric mass fits for §A, and a $c$-varying cooling code for §E) — this document
identifies the corrections and estimates their plausible size, but the underlying
literature values used throughout §A–§D have not themselves been revised. Separately,
§B's conclusion rests on a single published study covering only part of the relevant
parameter space ($M<1.25\,M_\odot$, $\tau<4$ Gyr — the regime where the model's ceiling
is *least* restrictive and hence *least* distinguishable from ordinary astrophysics).
The truly decisive regime — $M>1.3\,M_\odot$ and/or $\tau>4$–$5$ Gyr — has not yet been
checked with the same rigor, and the individual promising benchmark object
(WD J0049$-$2525) is not yet resolved. The appropriately hedged statement is: **the
two lines of evidence this document originally raised against the model have both
weakened under scrutiny, without yet fully disappearing; the decisive tests — in both
the mass-revision and cooling-age dimensions — have not yet been run.**

---

## Open Questions (revised and reprioritized)

1. **[Highest priority, actionable]** Re-derive masses and cooling ages for the specific
   objects flagged as ceiling violations in the original §A table, using Gaia DR3
   astrometry and the photometric method (Bergeron et al. 2019 / Gentile Fusillo et al.
   2021 technique), before treating any of them as evidence again.
1b. **[Highest priority, actionable — new]** Obtain a real, numerical value for T21's
   $f_\nu(M)$ (the fraction of a white dwarf's thermal budget attributable to enhanced
   early-time plasmon-decay cooling) by re-running a standard WD cooling code with the
   $c$-varying neutrino rate built in, and use it to properly correct — rather than
   merely estimate — the cooling ages used throughout §A–§D. This is the single most
   consequential open item connecting T20 and T21.
2. **[Highest priority, most decisive]** Extend the Fleury, Caiazzo & Heyl (2022)
   volume-complete, completeness-corrected cooling-age-distribution methodology to the
   $1.25$–$1.40\,M_\odot$ range and to cooling ages beyond 4–5 Gyr — ideally re-derived
   with the corrected (item 1b) cooling ages rather than the standard ones. This is the
   single measurement that would most directly settle this topic: the model predicts a
   sharp, near-total cutoff in this specific mass/age window that ordinary astrophysics
   does not.
3. **[New]** Quantify the plausible contamination of "isolated" massive-WD samples by
   detached post-mass-transfer objects (former CVs/novae, or WDs that fully accreted or
   engulfed a dM/brown-dwarf companion) whose true last-mass-set epoch is more recent
   than their apparent single-star cooling age suggests. Relevant starting points: the
   known single-degenerate SN Ia progenitor literature (WD growth via stable/nova
   accretion toward $M_\text{Ch}$), the space density and duty cycle of CVs, and any
   kinematic/abundance signature (e.g. donor-derived surface pollution, orbital remnants,
   or a surviving faint companion) that could flag a *past* mass-transfer history in an
   otherwise-isolated-looking white dwarf. This directly affects how much confidence to
   place in any future individual-object test (§A, §C) but does not affect the
   raw-number-count logic of §B.
4. Obtain a firm, published cooling age for WD J004917.14$-$252556.81 (J0049$-$2525),
   currently the best-validated individual high-mass, single-star-origin benchmark
   available (no merger signature; would still need the check in item 3 above, though its
   established rapid-rotation/magnetism-free, single-star-consistent profile makes a
   hidden accretion history less likely than for a typical field object).
5. Fold the Cunningham et al. (2024) Gaia-recalibrated IFMR into the "ordinary
   astrophysics" baseline used for comparison, since it predicts fewer high-mass WDs to
   begin with than the IFMR implicitly used in most works cited here.
6. A rigorous population-synthesis calculation: convolve $\tau_\text{ceiling}(M)$
   directly with a realistic Milky Way star-formation history, the Cheng et al. (2020)
   merger delay-time distribution, **and an explicit single-degenerate/accretion channel**
   to produce a complete predicted mass–cooling-age distribution, for direct statistical
   comparison (e.g. via the same KS-test machinery already used by Fleury, Caiazzo &
   Heyl) against Gaia EDR3/DR3 data — rather than the qualitative "does a deficit appear"
   reading given here.
7. Formal error propagation for any future individual-object comparisons (not done for
   §A or §C in either version of this document).
8. SN Ia delay-time distribution cross-check (unchanged from the initial version): does
   the same $M_\text{Ch}(\tau)$ ceiling predict a deficit of old-delay-time SNe Ia at low
   $z$, and is this consistent with observed SN Ia delay-time distributions? (Note this
   question is itself intertwined with item 3 above, since the single-degenerate SN Ia
   channel is precisely a case of accretion-driven growth toward $M_\text{Ch}$.)
9. Extension to $M_u$-based (classical Mach) counting (T12 fork): verify the two
   premise-2 variants coincide closely enough at the relevant $0$–$13$ Gyr lookback
   window for this test's conclusions to be insensitive to the fork.
10. Cluster age/mass refinement for §D using the newest JWST-based cooling-sequence ages
    (e.g. Bedin et al. 2025 for M4) and updated eclipsing-binary-calibrated masses.
