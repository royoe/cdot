# Session Log — White Dwarf Population vs. the Chandrasekhar-Mass Ceiling

**Topic produced:** T20 — The White Dwarf Population and the Chandrasekhar-Mass Ceiling
*(renumbered from T19 → T20 during the follow-up round, since T19 is already in progress
elsewhere in the repository)*
**Related existing topics:** T1 (Age of the Universe), T4 (Supernovae and Cosmic
Acceleration), T8 (Gravitational Constant), T12 (Origin of the Speed of Light)
**Dates:** 2026-07-01 (initial session), 2026-07-01 (follow-up / revision session)

---

## PART 1 — Initial Session

### User Prompt 1 (verbatim)

> The files stored in this project are a snapshot from a github repoistory. There is a
> Core Principles document that should always be kept in context, as well as a series of
> numbered Topic documents, providing the current state of each topic.
>
> The purpose of this project is to challenge and evolve the model in such a way that a
> coherent picture emerges. Be critical and constructive, and don't take prior results as
> authoritative.
>
> Any sessions that produce results that challenge or improves the content in these files
> should present them as an update document, that will then be cross-checked and merged
> into the repository. At the conclusion of a session, after creating the update
> documents, also produce a session log named with the relevant topic including all user
> prompts and session results with timestamps, and finally presenting download links for
> the update documents and session log.
>
> In this project we have attempted to compare the SN luminosity function to predictions
> of how they evolve under a variable speed of light. We trivially found that standard
> candles are not standard since the Chandrasekhar mass is a function of c, and therefore
> was lower in the past. This has real consequences for the white dwarf population since
> high-mass white dwarfs can only be of recent origin. Please calculate how the
> predictions of the current model compares with the observed massive WD population.

### Actions and Findings (chronological)

**[step 1]** Searched project knowledge for existing treatment of the Chandrasekhar mass
and white dwarfs. Found the relevant result already established in
`T4_Supernovae_and_Cosmic_Acceleration.md` ($M_\text{Ch}\propto c^{3/2}$ under invariant
$G$, $\hbar$, $m_p$), the redshift/lookback-time machinery in
`T1_Age_of_the_Universe.md`, and the invariant-$G$ adoption rationale in
`T8_Gravitational_Constant.md`.

**[step 2]** Derived $M_\text{Ch}(\tau)/M_{\text{Ch},0}=(1-\tau/\tau_\infty)^{9/8}$ and the
inverse age ceiling $\tau_\text{ceiling}(M)=\tau_\infty[1-(M/M_{\text{Ch},0})^{8/9}]$,
directly from T1's and T4's existing results. Verified algebraic consistency with T1's
$z$-based formulas. Established that the ceiling binds single-star and merger-remnant
formation channels equally.

**[step 3]** Web-searched and compiled observational data: Camisassa et al. (2019, A&A,
arXiv:1807.03894) 44-object ultra-massive WD mass/age table; Fleury, Caiazzo & Heyl
(2022, MNRAS 511, 5984, arXiv:2110.00598) Gaia EDR3 population study; Bhattacharya et al.
(2022, ApJ) merger-remnant reconstructions for SDSS J2211+1136 and ZTF J1901+1458;
Cummings et al. (2018) IFMR; globular-cluster age literature for 47 Tuc, M4, NGC 6397.

**[step 4]** Computed $\tau_\text{ceiling}(M)$ numerically (`/home/claude/wd_calc.py`) for
$M_{\text{Ch},0}\in\{1.40,1.44\}\,M_\odot$ and compared against all 44 Camisassa et al.
objects. Result at the time: 15/44 (34%, $M_{\text{Ch},0}=1.40$) to 8/44 (18%,
$M_{\text{Ch},0}=1.44$) individually exceeded the ceiling.

**[step 5–8]** Cross-checked against Fleury/Caiazzo/Heyl population result and the two
merger benchmark objects; performed the globular-cluster check; assembled caveats; wrote
up the result as topic document T19 (later renumbered T20 — see Part 2) with a
"Framing 1 / Framing 2" verdict weighted toward "a second, largely independent empirical
strike on the model."

### Summary of Part 1 Result (superseded — see Part 2)

The initial write-up concluded that a nontrivial fraction of resolved massive white
dwarfs and an independent population-level study both exceeded the model's predicted age
ceiling, constituting a fairly clean, largely parameter-free tension. **This conclusion
was revised in the follow-up session below after the user asked two clarifying
questions that exposed an important, previously unchecked systematic.**

---

## PART 2 — Follow-up / Revision Session

### User Prompt 2 (verbatim)

> Please update the created document by changing T19 to T20 as T19 is already in
> progress. Also update the document according to the following clarification questions.
> I would check that the discrepant SDSS stars do not have more recent data from Gaia
> that relaxes the conflict. But I would particularly like an assessment on the observed
> numbers, because the model clearly predicts that massive white dwarfs should sparser
> than stellar evolution predicts, at least for the ones that have had time to cool. Is
> there sufficient data on massive white dwarfs in the literature to shed light on this
> question?

### Actions and Findings (chronological)

**[step 1]** Renamed the topic and all files from T19 to T20 throughout, per the user's
instruction (T19 is already in progress elsewhere in the repository).

**[step 2 — checking for updated Gaia data on the discrepant SDSS stars]** Searched for
Gaia-era re-derivations of the specific objects flagged as ceiling violations in the
original §A comparison. Found that essentially all 44 objects in the Camisassa et al.
(2019) compilation derive from **pure spectroscopic** (parallax-free) SDSS fits
(Kleinman et al. 2013; Kepler et al. 2015/2016; Curd et al. 2017; Nitta et al. 2016;
Gianninas et al. 2011; Mukadam et al. 2004). Found multiple independent, well-documented
sources establishing that this method runs systematically high relative to
Gaia-parallax-based photometric masses:
  - Genest-Beaulieu & Bergeron (2019, ApJ, arXiv:1901.01857): direct spectroscopic vs.
    photometric comparison for SDSS+Gaia DA/DB white dwarfs, identifying line-broadening
    model problems responsible for the discrepancy.
  - A 2026 DESI DR1 white dwarf model-atmosphere analysis (IOPscience DOI
    10.3847/1538-4357/ae43ee): explicit systematic offset of $0.05$–$0.06\,M_\odot$
    (spectroscopic high) for DA white dwarfs.
  - **Concrete individual downward revisions found for objects in or adjacent to our
    sample:** GD 518 ($1.20\to1.114\pm0.006\,M_\odot$, Kilic et al. 2025); BPM 37093
    ($1.097\to1.037\pm0.008\,M_\odot$, O'Brien et al. 2024, though other recent work still
    quotes $\sim1.13$); **SDSS J084021.23+522217.4, an object in our original 44-object
    table** ($1.139\to0.98\pm0.04\,M_\odot$, Vincent et al. 2024) — a $0.159\,M_\odot$
    downward revision large enough to remove the object from the ultra-massive category
    entirely.
  - Conclusion: the original individual-object "34%/18% violate the ceiling" result is
    **not currently trustworthy** and has been retracted as primary evidence in the
    revised document, pending a proper Gaia DR3 photometric re-derivation of the specific
    flagged objects (not performed in this session — flagged as the top open question).
  - Identified one promising exception: WD J004917.14$-$252556.81 ("J0049$-$2525," Kilic
    et al. 2023, MNRAS 522, 2181), whose mass ($1.26$–$1.31\,M_\odot$) is cross-validated
    by *both* spectroscopic and photometric methods in agreement, and which shows no
    merger signature — flagged as the best available modern single-object benchmark,
    though its precise cooling age is not yet found published.

**[step 3 — assessing whether sufficient population/number-count data exist]** Fetched
the full text of Fleury, Caiazzo & Heyl (2022, arXiv:2110.00598) to properly characterize
their population-level finding (previously only partially quoted from search snippets).
Established precisely that:
  - For $0.95$–$1.15\,M_\odot$: cooling-age distribution matches the independently known
    Mor et al. (2019) star-formation-rate history with no anomaly.
  - For $1.15$–$1.25\,M_\odot$ (closest to where the model's ceiling becomes
    restrictive): distribution is inconsistent with pure single-star/SFR-tracing
    formation, but is well explained (down to $\chi^2_\nu=1.4$) by a
    single-star + double-degenerate-merger combination, using an independently
    estimated (Cheng et al. 2020) merger delay-time distribution, extending to 4 Gyr of
    cooling age.
  - The authors' explicit conclusion: "we find no evidence for a substantial cooling
    delay in the numbers of massive white dwarfs detected in Gaia EDR3" — i.e., no
    suppression/deficit is needed or seen; ordinary formation-channel astrophysics
    already accounts for the numbers throughout the cooling-age range tested.
  - This directly answers the user's question: yes, sufficient population-level data
    exist (a volume-complete, completeness-corrected, Gaia-photometric — not
    spectroscopic — sample) to test the "sparser" prediction in the $1.15$–$1.25\,M_\odot$
    / up-to-4-Gyr regime, and the answer found is that **no deficit is present** —
    evidence against the model's central prediction for this topic, in the one regime
    where a proper test currently exists.
  - Noted the important scope limitation: this study does not extend above
    $1.25\,M_\odot$ or beyond $\sim4$ Gyr, which is precisely where the model's predicted
    exclusion becomes sharp and unambiguous (vs. ordinary astrophysics), so this is
    suggestive but not yet a complete/decisive test.

**[step 4]** Substantially revised the topic document: renamed T19→T20; reframed §A as
retracted/non-primary evidence with the systematic explained in detail; rewrote §B as
the new primary line of evidence with the corrected, precise characterization of the
Fleury et al. result; added WD J0049$-$2525 to §C as a new modern benchmark candidate;
reordered and expanded the Caveats section to lead with the spectroscopic/photometric
mass systematic; rewrote the Verdict to reflect the corrected balance of evidence
(population-level test leans against the model; individual-object test is currently
uninformative); reprioritized Open Questions around the two concrete, actionable next
steps (re-derive the flagged objects with Gaia photometric masses; extend the
Fleury-et-al.-style analysis to $1.25$–$1.40\,M_\odot$ and $>4$ Gyr).

### Summary of Part 2 Result

The follow-up round substantially changed the document's conclusions in a
self-critical direction: the original individual-object evidence for a ceiling
violation is likely an artifact of well-documented pre-Gaia spectroscopic mass biases
(demonstrated concretely for one object in the original sample, and for two closely
related benchmark objects) and has been retracted as primary evidence. In its place, a
properly volume-complete, Gaia-photometric population study (Fleury, Caiazzo & Heyl
2022) was identified and read in full; it shows **no deficit** of old massive white
dwarfs in the one mass/age regime it covers ($1.15$–$1.25\,M_\odot$, up to $\sim4$ Gyr),
which is itself a genuine, if partial and not yet fully decisive, piece of evidence
against the model's central "massive white dwarfs should be sparser" prediction. The
single most valuable concrete next step identified is extending this same
population-level methodology to $1.25$–$1.40\,M_\odot$ and to cooling ages beyond
4–5 Gyr, where the model's predicted exclusion is sharpest and most distinguishable
from ordinary astrophysics.

## Suggested Follow-up Edits (not applied in this session)

- `Core_Principles.md`: update the "T1–T17" range reference once T20 (and any other
  in-progress topics through T19) are merged.
- `T4_Supernovae_and_Cosmic_Acceleration.md`: add a cross-reference from the
  Chandrasekhar-Mass Candle Systematic section to T20 as a complementary,
  non-SN-specific test of the same $M_\text{Ch}\propto c^{3/2}$ consequence.

---

## PART 4 — Cross-Reference Note: T20 Updated from the T21 Investigation

In a separate but related line of work within this same session (logged in full in
`Session_Log_T21_Chandrasekhar_Strong_Weak_Sector_Coupling.md`), an investigation into
how nuclear/weak physics couples to $c$ (prompted by a concern about T4's
$M_\text{Ch}\propto c^{3/2}$ scaling) led to a result directly relevant to this document:
plasmon decay, the dominant neutrino-cooling process in degenerate WD cores, was shown
to scale as $\Gamma\propto c^{-1}$ at fixed density — meaning neutrino cooling was more
efficient in the past. Worked through to its consequence, this implies **standard,
no-time-variation WD cooling ages (used throughout this document's §A–§D) systematically
overstate true ages**, by an estimated few percent up to $\sim10$–$20\%$ depending on
mass and age.

This document was updated accordingly: a new §E summarizes the finding and its
cross-check against this document's flagged ceiling violations (plausibly resolves the
marginal cases, meaningfully reduces the larger ones); a new caveat (§9) notes the same
correction weakens §B's population-level "no deficit" finding, since it also relies on
standard cooling ages; and the Verdict and Open Questions were revised to reflect that
both of this document's original lines of evidence against the model now carry
independent, quantified reasons for skepticism. Full derivation and reasoning is in
T21 Part 5; see that document's session log for the complete step-by-step record.

---

## PART 3 — Correction Round

### User Prompt 3 (verbatim)

> One minor correction to note to the introductory statement: "... could have formed
> with a mass exceeding the value of M_Ch that prevailed at its own formation epoch."
> This is only valid if it is not currently in a binary and actively accreting, or
> recently fully accreted a dM or BD companion, ie. it has been a Cataclysmic Variable
> in the past.

### Actions and Findings

**[step 1]** Accepted the correction as physically correct and important: the ceiling
argument as originally stated conflated "formation epoch" with "single-star birth,"
which silently assumes the white dwarf's mass was set once and never changed. A white
dwarf that has been a cataclysmic variable (accreting from a non-degenerate donor), a
nova system, or has fully accreted/engulfed a low-mass (dM or brown-dwarf) companion can
grow *after* its original formation, so the relevant epoch for the $M_\text{Ch}(\tau)$
check is the star's *last* significant mass-changing event, not necessarily its birth.

**[step 2]** Revised the Physical Concept section's "why the formation channel does not
matter" discussion to explicitly add binary mass-transfer/accretion as a third channel
(alongside single-star evolution and double-degenerate mergers), and to restate the
ceiling condition as $M\le M_\text{Ch}(\tau_\text{last mass-set})$. Added a new paragraph
explaining why this specifically threatens the *cooling-age* inference used throughout
the document: a detached post-mass-transfer object can relax onto an ordinary-looking
single-WD cooling track with no retained observational signature of its accretion
history, unlike an actively accreting CV (which is easily excluded by disk emission
lines, variability, and off-track colours).

**[step 3]** Determined that this correction affects the individual-object tests (§A,
§C) — where a specific object's cooling age is compared directly to the ceiling, and a
hidden accretion history could make an apparently-old object actually consistent (its
true last-mass-set epoch being more recent than its naive cooling age suggests) — but
does **not** undermine the population-level, raw-number-count test (§B): a channel that
can only add objects to an age bin (by resetting an old core to a young "reformation"
epoch) can never manufacture an apparent *deficit*, so it strengthens rather than
weakens confidence in the "no deficit found" reading of Fleury, Caiazzo & Heyl (2022).

**[step 4]** Added a new caveat (Caveat 2, "Binary mass-transfer history") explaining
that this compounds with the existing spectroscopic-mass-bias caveat for §A/§C — both
work in the same direction (making an object look more violating than it truly is) —
and added a new Open Question (item 3) calling for a quantified estimate of the
single-degenerate/post-CV contamination fraction in "isolated" massive-WD samples,
along with a note tying this to the classical single-degenerate SN Ia progenitor channel
and to open question 8 (SN Ia delay-time distribution cross-check). Added a short
cross-reference in §C noting that the two named merger-candidate benchmark objects were
flagged as such precisely because they show *positive* merger signatures (magnetism,
rapid rotation) — whereas a hidden accretion history leaves no comparable signature, so
it cannot be ruled out for any object by the same method.

### Summary of Part 3 Result

The correction is incorporated as a refinement of the ceiling's physical basis (the
"formation epoch" is properly the epoch of last mass change, of any origin) rather than
a change to the derivation itself, which remains an exact restatement of T1/T4 results.
Net effect on the document's conclusions: the already-retracted individual-object test
(§A) gains a second, independent reason for its unreliability (compounding with the
Gaia spectroscopic-mass-bias caveat), while the population-count evidence against the
model (§B) is, if anything, reinforced in its interpretation, since the accretion
channel identified by the user cannot be invoked to explain away an observed deficit —
only to add to an observed population, which is precisely what was and was not seen.
