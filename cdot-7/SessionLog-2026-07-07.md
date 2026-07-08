# Session Log — 2026-07-07

*Running log for cdot-7 work, appended per-prompt. Continues the same calendar date as
`cdot-6/SessionLog-2026-07-07.md`, which is now closed out (its final entry records the
handoff). A new date gets a new file (`SessionLog-<date>.md`).*

---

## Entry 1 — cdot-7 founded

**Prompt (verbatim):**
> Ok. It is time to step away from Atkinson then. Let's go with your suggestion of using the 'spirit of AQUAL'. Please rewrite the Foundation into cdot-7, and start building everything again. I think we can settle on s=+1/2 exactly and write the equations under the premise that all local physics must scale the same way with c.

**Summary:** Built cdot-7 from scratch. Kept from cdot-6 only what never depended on
Atkinson: the horizon/mass-radius machinery (§2.1–2.2), the relational (not measured)
status of $c_0,c_z$ (§2.3), and the general LLR-exponent formula. Dropped Atkinson's
local closure entirely. New premise 3: universal local mass scaling, $m\propto c^{1/2}$,
$G$ exactly invariant — adopted as a premise, explicitly flagged as a standing
theoretical debt rather than derived. Worked out the consequences: atomic radius and
orbital radius both scale as $c^{-3/2}$ (exact lockstep, by construction), giving exact
($E=0$) LLR safety at every epoch, not just today; redshift exponent becomes $5/2$
(since $\nu\propto c^{5/2}$ now, not $c^2$); age is unchanged at $\approx13.97$ Gyr
(shown to be independent of the redshift exponent); particle horizon grows to
$\approx10.7$ Gpc (larger than cdot-6's $\approx8.6$ Gpc, since the redshift-$c$
relation is shallower). New premise 4: AQUAL's modified Poisson equation, adopted
wholesale (cited: Bekenstein & Milgrom 1984) rather than derived, with $a_0\equiv\lambda
c_0H_0^\text{hor}$ tying the acceleration scale to this framework's own cosmological
content; $\lambda=1$ gives $a_0\approx2.7\times10^{-10}$ m/s², a factor $\approx2.3$
above the empirical value — the same order-of-magnitude tension this project has always
had for $a_0\sim cH_0$, not a new one. Flagged plainly that this framework currently
makes no relativistic-level predictions at all (a real scope reduction from cdot-6,
which reproduced GR exactly via Atkinson) and that the mass-scaling premise is not
obviously consistent with the electromagnetic-sector assumption ($\epsilon_0\propto
c^{-1}$) also in use — "all local physics scales the same way" is not yet actually true
across both sectors, flagged as an open item rather than glossed over. Wrote
`Foundation.md`, `ResearchNotes.md` (recording the cdot-6 pivot and its rationale), and
added a superseded-status header to `cdot-6/Foundation.md` pointing here.

**Files updated:** `cdot-7/Foundation.md` (created), `cdot-7/ResearchNotes.md` (created),
`cdot-7/SessionLog-2026-07-07.md` (created), `cdot-6/Foundation.md` (superseded header
added), `cdot-6/SessionLog-2026-07-07.md` (closing entry added).

---

## Entry 2

**Prompt (verbatim):**
> Let's give open items #1 a first attempt.

**Summary:** Attempted to derive (rather than adopt) premise 3's $s=+\frac12$ mass
scaling. Tried two Sciama-type self-binding mechanisms (particle bound to horizon mass
at its own Compton wavelength: gives $m\propto c^{-2}$, wrong; at its own gravitational
radius: dimensionally degenerate, not a real candidate) — both dead ends, recorded so
they aren't retried. A third attempt found something more useful than a clean
derivation: premise 2's "mass neither created nor destroyed" is ambiguous once premise 3
allows individual particle mass to vary — it could mean particle number is conserved
(density rises with $m(t)$) or mass density itself is flat (current reading; particle
number silently falls). Rebuilding premise 2's Sciama closure under the number-conserved
reading gives $\dot c\propto c^{1+s/2}$ (reproduces the current exponential exactly at
$s=0$, confirming the setup), but at $s=+\frac12$ gives $c^{-1/4}\propto(t_*-t)$ — a
finite-future coordinate singularity, not the current exponential. Noted this has
precedent (cdot-5's own connectivity-counting cosmology had the same feature, resolved
by showing proper time to reach it diverges) but did not chase that check here. Net
result: $s=+\frac12$ remains adopted, not derived, but the theoretical debt is now a
concrete fork (which reading of mass conservation is correct) rather than an open-ended
one. Updated `Foundation.md` §2.1, §3.4, and §6 item 1 to record this as a load-bearing
dependency; full derivation working kept in `ResearchNotes.md` §6.

**Files updated:** `cdot-7/Foundation.md` (§2.1 ambiguity flagged, new §3.4 added, §6
item 1 sharpened), `cdot-7/ResearchNotes.md` (new §6 added, old §5 renumbered to §7).

---

## Entry 3

**Prompt (verbatim):**
> Good point with the mass conservation inconsistency. It is back to Machian by number then, I suppose.

**Summary:** Adopted the particle-number-conserved reading of "mass neither created nor
destroyed" outright, resolving Entry 2's fork. Rebuilt §2's cosmological closure from
scratch under this reading: mass density now rises as $(c/c_0)^{1/2}$ (tracking
individual particle mass, §3) rather than staying flat, giving $M_h\propto R_h^3
(c/c_0)^{1/2}$ instead of $M_h\propto R_h^3$. Re-solved the Sciama self-consistency
equation: $c(t)=c_0(1-(t-t_0)/\tau)^{-4}$, $\tau=3R_{h,0}/c_0$ — genesis unaffected, but
a new finite-future coordinate-time singularity appears, resolved the same way cdot-5's
own analogous feature was (proper time to reach it diverges — explicitly verified here,
not just asserted by analogy). Caught and fixed a dimensional sign slip in an
intermediate constant during the derivation before trusting the final numbers. Found a
clean robustness result: $H_0^\text{hor}$ (today's instantaneous $\dot c/c$) and
therefore $a_0$ are *unchanged* by the closure rebuild, since they depend only on
today's local rate, not on the cosmological history — but age ($13.97\to15.5$ Gyr) and
the particle horizon ($10.7\to14.3$ Gpc) do change, since those are integrated,
history-dependent quantities. Redefined $H_0^\text{hor}$ as $(\dot c/c)|_{t_0}$ rather
than via $c_0/R_{h,0}$, since the two coincided only under the old exponential closure.
$s=+\frac12$ itself remains adopted, not derived — this resolved which cosmology it's
consistent with, not why it holds.

**Files updated:** `cdot-7/Foundation.md` (§2.1, §2.2 rewritten; §3.4, §5.2, §5.3, §6
item 1 updated to match), `cdot-7/ResearchNotes.md` (new §6.1 added with full derivation
trail).

---

## Entry 4 — Fable-1 session reviewed, verified, and merged

**Prompt (verbatim):**
> I had a very constructive session with Fable. All the update suggestions and logs are in cdot-7/Fable-1. Please read the whole progression chain carefully, and assess what should be incorporated into the Foundation and what needs further exploration.

**Summary:** Read all nine files in `cdot-7/Fable-1/` (five session-log entries, five
update documents, two Python scripts, one consolidation map) covering a full session
that found and fixed a real bug in this Foundation's redshift law, unified two
previously-separate scaling postulates into one invariance principle, found and
resolved a genuine inconsistency between premises 2 and 4, and built a working
cosmology with late-time acceleration from a single new constant. Verified rather than
trusted: independently re-derived the photon-sector redshift-law correction via both of
Fable's arguments (crest-transit kinematics, wave mechanics) and confirmed the resulting
exact-EdS luminosity distance and $q_0=+\frac12$ algebraically; independently re-derived
the $\alpha_G$↔LLR identity, the $a_0=\lambda\dot c$ identity, the deep-MOND orbit
exponents, and the $g_h=\frac34\dot c$ premise-2/4 inconsistency; ran both
`closure_dynamics.py` and `a0_confrontation.py` directly and confirmed every quoted
number reproduces exactly; independently verified via web search that both external
citations (MUSE-DARK III/Ciocan et al. 2026, *A&A* 709, L16; Vărăşteanu et al. 2025,
MIGHTEE-HI; and the DES time-dilation measurement, White et al. 2024, *MNRAS* 533,
3365) are real papers with the exact numbers quoted, not fabricated. Presented an
assessment (high-confidence/ready vs. genuine-progress-but-still-open vs.
needs-more-scrutiny) before merging, and confirmed the merge approach with the author.

**Merge executed in full**, per the session's own consolidation map: rewrote
`Foundation.md` §0 (methodological note: correspondence partially constructed,
falsifiable content localized to the $a_0=\lambda\dot c$ portal, radiation-era scope
limit added), §2 (closure rebuilt as an AQUAL-consistent dynamical system: fixed point,
instability, $\varepsilon_0$, working cosmology), §3 (reframed around the Planck-unit
invariance principle; corrected redshift law, $1+z=(c_0/c_z)^{3/2}$), §4 ($a_0(t)=
\lambda\dot c(t)$, epoch-dependent, portal framing), §5 (recomputed cosmological
quantities, new §5.5 covering the full flux/luminosity sector, candle invariance,
thermal sector, and the $\hat a_0(z)$ data confrontation), and §6 (open items rewritten
to the session's final list, with resolved items recorded rather than restated).
`ResearchNotes.md` gained five new sections (§6–§10: the photon-sector correction, the
invariance principle and LLR/$\alpha_G$ identity, the closure rebuild's full derivation
trail including the dead $\lambda$-derivation hope, the $\hat a_0(z)$ confrontation
with its chronology note, and the thermal sector) and a rewritten §11 separating
resolved threads from what's still genuinely open. Renumbered several stray
cross-references in `Foundation.md` that had drifted during earlier same-day edits
(caught while aligning citations to the new `ResearchNotes.md` structure).

**Net effect:** the framework now has a working cosmology (fixed point $\equiv$ exact
EdS; one new constant $\varepsilon_0=-0.0627$ gives $q_0=-0.68$, age 13.0 Gyr, and a
fit to a $\Lambda$CDM proxy curve to 0.015 mag rms) and a falsifiable, near-parameter-
free prediction ($\hat a_0(z)$) that already engages real, recent data at
$\approx85\%$ of the measured amplitude. Standing debts, stated plainly rather than
buried: $\lambda$, $\kappa$, and $\varepsilon_0$ are measured/fitted, not derived; the
SN fit is against a theoretical proxy, not a real compilation yet; there is no
radiation era, so nothing before $z\sim$ few is in scope; and the decisive joint
statistical fit (§6 item 1) has not been run.

**Files updated:** `cdot-7/Foundation.md` (§0, §2, §3, §4, §5, §6 substantially
rewritten), `cdot-7/ResearchNotes.md` (§6–§11 added/rewritten), this log entry.

---

## Entry 5 — Illustrative figures for the fitting results

**Prompt (verbatim):**
> Can we put some illustrative figures demonstrating the fitting results?

**Summary:** Wrote `cdot-7/make_figures.py`, built directly on the verified `Fable-1`
modules (imports `closure_dynamics.py` and `a0_confrontation.py` rather than
re-implementing anything), and generated two SVG figures into the project's shared
`figures/` directory, matching the existing cdot-3/4 convention (matplotlib SVG
backend, embedded via `![](../figures/...)`). Cross-checked the plotted data
numerically against previously-verified values before embedding (rms = 0.01509 mag,
matching the quoted 0.015; $\hat a_0(z)$ values at $z=0.33/0.85/1.00/1.44$ matching the
earlier-verified table to the digit) — did not just trust the script's own printout.
Figure 1 (`cdot7_hubble_diagram.svg`): Hubble-diagram residual vs. the $\Lambda$CDM
proxy, showing the unstable fixed point's EdS divergence against the fitted
trajectory's 0.015 mag rms track. Figure 2 (`cdot7_a0_evolution.svg`): the evolving
MOND scale, three hypotheses (constant, naive fixed-point, fitted trajectory) against
the MUSE-DARK III and MIGHTEE-HI data points. Embedded both in `Foundation.md` §2.2 and
§5.5 respectively, each with a caption in the project's established style.

**Files updated:** `cdot-7/make_figures.py` (created), `figures/cdot7_hubble_diagram.svg`
(created), `figures/cdot7_a0_evolution.svg` (created), `cdot-7/Foundation.md` (both
figures embedded with captions), this log entry.

---

## Entry 6 — Two new Fable-1 updates reviewed (joint fit, ε₀ seed); M-σ brought in

**Prompt (verbatim):**
> Two more updates in Fable-1. Please assess carefully. The joint fit with Pantheon+ looks very encouraging. I need to assess the Epsilon_0 seed analysis more carefully, so please provide any input you have to assist.

**Summary:** Reviewed `Update-JointFit-2026-07-07.md` and `Update-Epsilon0Seed-2026-07-07.md`
(Fable-2 sub-session). Ran `joint_fit.py` against the project's own real Pantheon+ data
(symlinked from `../data/`, not the SN sample previously used only as a $\Lambda$CDM
proxy) — every quoted number reproduced exactly, including an independent hand-check of
the "best free linear $a_0(z)$" reference $\chi^2=20.0$ (got 19.98). This is a genuine,
strong result: real data, full covariance, a validated pipeline. Ran `seed_analysis.py`
and found a real bug — its first scaling-symmetry check prints a nonsensical `1.91`
mismatch (should be $\approx0$), while a second, better-constructed check further down
the same file gives the claimed `1.5e-6`. Independently re-derived the scaling-symmetry
theorem and the radiation-scaling relations ($u_\gamma\propto c$, $\eta(z)=\eta_0(1+z)$)
by hand from already-verified thermal-sector results — both check out. Flagged the
"closure density problem" ($\Omega_\text{closure}=0.134$ vs. baryon census $0.049$,
factor 2.7) as under-weighted in the update's own framing — recommended treating it as
a potential structural threat (mass required by the cosmological closure itself,
echoing real MOND's own unresolved cluster-scale residual) rather than a byproduct,
and asked whether it's forced by the SN fit before taking the seed analysis further.
Neither update has been merged into `Foundation.md` yet — pushback sent back to the
Fable-1 session for consideration.

**M-σ scoping and derivation.** Addressed the author's concern that premise 2's
uniformity assumption might conflict with using AQUAL on anisotropic, structured
systems: resolved by distinguishing equilibrium-dynamics tests (RAR, BTFR, M-σ — take
$a_0(z)$ as an external given) from structure-formation/perturbation-theory questions
(BAO, CMB anisotropies — require explaining how structure grows on top of the
homogeneous background); only the latter is the deliberately-deferred, historically
fatal territory. Recorded this as a standing scope test in `Foundation.md` §0. Checked
cdot-4's own prior M-σ mechanism (`cdot-4/T17_Galaxy_Morphology_and_MSigma.md`) via a
sub-agent to separate what was generic AQUAL physics (the core $\sigma^4\sim\Gamma
GMa_0$ virial relation, with $M_\text{BH}$ an external correlate of $M_\text{bulge}$,
not a MOND-determined quantity) from what was specific to the now-abandoned
connecton/Lorentz-filter mechanism (the coherence factor, the stripping picture — none
of it needed). Derived cdot-7's own version, explicitly flagging $\Gamma=O(1)$ as
undetermined (unlike BTFR's exact $\Gamma=1$). Searched the literature for a
confrontation and found an important distinction: the dramatic, real $M_\text{BH}$-
$\sigma$ evolution reported at $z\sim1$–2 (JWST/ALMA, black holes up to $10\times$
overmassive) is on the black-hole channel, outside this framework's scope (standard
interpretation: black-hole assembly history, not bulge dynamics) — verified via search,
not assumed. The correct channel (stellar-mass-$\sigma$ for quiescent galaxies) shows
real but mild high-$z$ evolution that the existing literature already attributes to
ordinary galaxy size evolution — degenerate in sign with this framework's own
prediction, not yet separable from it with existing analyses. Verdict recorded plainly:
M-σ is safely in scope but its evidentiary status is honestly weaker than RAR's — right
shape, undetermined normalization, a real but not-yet-testable evolution channel — and
should not be presented with RAR's confidence.

**Files updated:** `cdot-7/Foundation.md` (§0: new scope-boundary principle added; §5.5:
M-σ section rewritten with the honest $\Gamma$ and confrontation-status caveats; §6
item 1 updated), `cdot-7/ResearchNotes.md` (new §11 added: full M-σ derivation trail and
literature check; old §11 renumbered to §12), this log entry. The joint-fit and seed
analysis numbers ($\kappa\lambda=0.307$, $\varepsilon_0=-0.068$, etc.) are **not yet**
merged into `Foundation.md` — that awaits the closure-density pushback being resolved.

---

## Entry 7 — Closure-density pushback resolved; four-term-fit spec written; full merge executed

**Prompt (verbatim):**
> [Three exchanges: (1) "A response to your pushback has been added to Fable-1" (initially misdirected — actually landed at the repo top level, not `Fable-1/`); (2) "Give me the precise details on what is needed to get the four-term fit running, and I will try one more time."; (3) "Ok. One more round of feedback in Fable-1 as per your request. Let's try to merge this in now."]

**Summary:** Located and reviewed `Update-ClosureDensity-2026-07-07.md` (top-level, not
`Fable-1/`) — verified its central formula and fixed-point specialization by independent
derivation (exact match), confirmed its qualitative conclusion (not reproducing
$\Lambda$CDM's matter budget, but robustly forced above baryons) via independent
numerical scan, and flagged the neutrino-escape arithmetic and the $\times2.5$–$2.9$
$\kappa$-forcing calculation as correct. Wrote a complete, verified-input implementation
spec for the four-term fit (parameterization, SPARC RAR source, BBN-based $\Omega_b$ —
verified via search: Cooke, Pettini & Steidel 2018 — current KATRIN bound — verified via
search: $m_\beta<0.45$ eV, 2025 — and the $H_0$-fixed/validation-first requirements) for
the author to hand to Fable-1.

Fable-1's response (`Update-OmegaReconciliation-2026-07-07.md`) correctly declined to
fake a four-term fit it couldn't run without the missing SPARC data, and instead
resolved the reconciliation analytically: verified (independently re-run,
`omega_reconciliation.py`) that all three prior $\Omega_\text{closure}$ values
(0.134/0.115/0.104) are the same formula under three explicit, previously-implicit
conventions, and derived a cleaner $H_0$-free form tying the required density directly
to $a_0^2/G$. Cross-checked one open nuance myself: using the joint fit's own
free-$A$-preferred local $a_0$ (1.39) instead of the SPARC anchor (1.20) shifts the
tension from $F=2.5$ to $F=2.9$ — not yet reconciled, recorded as such rather than
picked arbitrarily.

**Full merge executed.** `Foundation.md`: §0 (the "no dark matter" claim now stated as
conditional, not settled); §2.2 (real Pantheon+ joint-fit numbers replacing the
$\Lambda$CDM-proxy fit throughout — $\varepsilon_0=-0.0678$, $\kappa\lambda=0.307$,
pipeline-validated against the published $\Omega_m=0.331\pm0.018$); §4/§5.3 (the two
$a_0$-anchoring conventions stated explicitly, flagged as not yet reconciled); §5.5 (the
$\hat a_0(z)$ confrontation updated to the real joint-fit numbers, with a caveat that
this is now a joint description, not a blind check); new §5.6 (the closure density
problem, elevated to its own subsection with the full $F$-form derivation, the
resolution-space ranking, and a standing falsification condition tied to the KATRIN
neutrino-mass clock); M-σ renumbered to its own §5.7; §6 open items fully renumbered and
rewritten (joint-fit extension and closure-density now the top two priorities; seed
work explicitly frozen). Regenerated both figures (`make_figures.py` rewritten to build
on `joint_fit.py`'s real-data trajectory and actual binned Pantheon+ residuals, not the
proxy curve). `ResearchNotes.md` gained §13 (the real joint-fit derivation trail) and
§14 (the closure-density elevation, reconciliation, and the handed-off four-term-fit
spec); all stale `Foundation.md` §6 item cross-references throughout both documents
renumbered to match.

**Files updated:** `cdot-7/Foundation.md` (§0, §2.2, §4, §5.3, §5.5, new §5.6, §5.7,
§6 substantially rewritten; all item cross-references renumbered), `cdot-7/
ResearchNotes.md` (new §13, §14; open-threads section renumbered to §15; item
cross-references fixed), `cdot-7/make_figures.py` (rewritten for real data),
`figures/cdot7_hubble_diagram.svg` and `figures/cdot7_a0_evolution.svg` (regenerated),
this log entry.

---

## Entry 8 — Raw (non-residual) Hubble diagram added before the residual figure

**Prompt (verbatim):**
> Please add a figure of the Pantheon fit that is not in residual terms, and show that before the residual fit.

**Summary:** Extended `make_figures.py` with a `dl_shape_curve` helper that evaluates
the joint-fit trajectory's $5\log_{10}d_L$ on a smooth $z$ grid (the existing
`trajectory()` function in `joint_fit.py` only returns model values at the actual SN
redshifts, so this reuses the same integration to get a plottable curve). New figure
(`cdot7_hubble_diagram_data.svg`): binned real Pantheon+ magnitudes (offset by the same
fitted zero point used everywhere else) plotted directly against $z$, with the
joint-fit trajectory and exact-EdS curves overlaid — the raw Hubble diagram, not a
residual. Embedded in `Foundation.md` §2.2 immediately before the existing residual
figure, with captions cross-referencing each other (raw diagram notes the two curves
look close and points to the residual figure for where they actually differ).

**Files updated:** `cdot-7/make_figures.py` (new `dl_shape_curve` helper and Figure 0),
`figures/cdot7_hubble_diagram_data.svg` (created), `cdot-7/Foundation.md` (§2.2: new
figure embedded before the residual one, both captions updated), this log entry.

---

## Entry 9 — The decisive four-term fit: recommended, executed, and merged

**Prompt (verbatim):**
> Ok. What next? Attempt the four-term fit or try to bring in the MSigma relation?
> Ok, very well. Go ahead!
> Please merge it all in.

**Summary.** Asked to choose the next priority, recommended the four-term fit (SN +
$a_0(z)$ + local RAR + mass census, with $\Sigma m_\nu$ as a bounded nuisance
parameter) over pursuing M-σ, since it directly adjudicates the "closure density
problem" — whether the framework's core "no dark matter" claim survives contact with
its own mass budget. Told to go ahead, executed it directly rather than handing it to
Fable-1.

**Execution.** Downloaded the real SPARC RAR master table ("Data Behind Figure 2" of
McGaugh, Lelli & Schombert 2016, *PRL* 117, 201101 — 2693 points, 153 galaxies) from
`astroweb.case.edu/SPARC/RAR.mrt`. Built `four_term_fit.py` on top of `joint_fit.py`'s
SN/trajectory machinery, adding two new likelihood terms: the real RAR shape (with a
second, distinct inversion of $\mu$ — solving $\mu(x)x=y$ for the AQUAL force law,
not the closure-context inversion used elsewhere) and the mass-census term of §5.6,
downweighting RAR points by the point-to-galaxy ratio ($2693/153\approx17.6$) as an
approximate correction for their non-independence. Omega_b taken from BBN (Cooke,
Pettini & Steidel 2018), deliberately not the CMB/$\Lambda$CDM value, to avoid
circularity; $\Sigma m_\nu$ given a soft half-normal edge at the KATRIN bound
($m_\beta<0.45$ eV, 2025, converted via $\Sigma m_\nu\approx3m_\beta$).

**A real bug, caught by the validation discipline.** The first run's built-in check —
switching the two new terms off must exactly reproduce the previously-verified
three-term result — failed badly ($\varepsilon_0=-0.0295,\ \kappa\lambda=0.146$ instead
of the expected $-0.0678,\ 0.307$). Traced to an independent redefinition of the
$a_0$-at-$\lambda=1$ constant using the wrong coefficient ($\tfrac32c_0H_0$ instead of
$\tfrac23c_0H_0$, since $a_0=\lambda\dot c_0$ needs $\dot c_0=\tfrac23c_0H_0^\text{obs}$,
not $\tfrac32$). Fixed, re-validated exactly, then re-ran the four-term optimization.
Robustness checked before trusting any number: four widely different starting points
converged to the identical optimum.

**Result (simple $\mu$, preferred over standard by $\Delta\chi^2\approx13$):**
$\varepsilon_0=-0.0909,\ \kappa\lambda=0.4355,\ \lambda=0.3056$ ($\kappa\approx1.43$),
$\Sigma m_\nu=1.374$ eV, $a_0(0)=1.386\times10^{-10}$ m/s², $q_0=-0.44$, age $=12.9$
Gyr. $\chi^2$: SN $=1405.7$, $a_0(z)=11.45$, RAR $=163.0$, mass $=0.06$, total
$=1580.2$. Two honest tensions reported alongside the headline result rather than
hidden: (i) RAR data alone prefers $a_0\approx1.26\times10^{-10}$ — forcing it to the
joint value costs $\Delta\chi^2\approx13$; (ii) the mass budget only closes by placing
$\Sigma m_\nu$ essentially at the current KATRIN laboratory edge — a real,
externally-adjudicated, near-term falsification condition, not a comfortable margin.

**Full merge executed.** `Foundation.md`: §0 (dark-matter claim now cites $\Sigma
m_\nu\approx1.37$ eV at the KATRIN edge specifically); §2.2 (three-term result kept as
an explicitly-superseded "first pass," four-term result presented as the working
cosmology, with the RAR-tension and point-estimate caveats stated inline); §4 and §5.3
(the two-$a_0$-convention split resolved by the single fitted $\lambda$); §5.5 ($\hat
a_0(z)$ ratios and figure updated to the four-term numbers, both the SPARC anchor and
the fit's own predicted $a_0(0)$ shown as distinct markers since they now visibly
differ); §5.6 (comprehensively rewritten: the actual resolution, the RAR tension as a
second independent finding, all caveats, a sharpened falsification condition tied to
the KATRIN bound); §6 (items 1–2 rewritten from "attempt the fit" to "tighten the fit
that now exists"); a stale, still-unqualified three-term "working cosmology" paragraph
found in §5.5 during a final consistency sweep and updated to the four-term numbers.
All three figures (`cdot7_hubble_diagram_data.svg`, `cdot7_hubble_diagram.svg`,
`cdot7_a0_evolution.svg`) regenerated with `make_figures.py` updated to the four-term
parameters. `ResearchNotes.md` gained new §14 (the full derivation trail: RAR
acquisition, the mass-census term and the CH0 bug, the fit and its diagnostics, what it
supersedes). Along the way, discovered and fixed a section-numbering gap (§12 missing
in both documents, traced to an earlier renumbering pass) via a scripted remap
(13→12, 14→13, 16→14, 17→15) applied to both files with placeholder substitution to
avoid double-transformation; verified clean 1–15 numbering and correct cross-references
by grep afterward.

**Files updated:** `cdot-7/Fable-1/four_term_fit.py` (created), `cdot-7/Fable-1/data/
RAR.mrt` (downloaded), `cdot-7/make_figures.py` (four-term parameters, dual $a_0$
markers), `figures/cdot7_hubble_diagram_data.svg`, `figures/cdot7_hubble_diagram.svg`,
`figures/cdot7_a0_evolution.svg` (regenerated), `cdot-7/Foundation.md` (§0, §2.2, §4,
§5.3, §5.5, §5.6, §6 rewritten; full section renumbering 13→12/14→13/16→14/17→15),
`cdot-7/ResearchNotes.md` (new §14; same renumbering applied), this log entry.

---

## Entry 10 — M-σ: the first real discriminating test against data

**Prompt (verbatim):**
> Let's make an attempt at adding MSigma now.
> Before trying to get the data, what is the current approach for comparing the M-sigma relation to the current model?
> So this has not been attempted in the literature before?
> Ok, you have convinced me. Go for (b) and continue to probe available data.

**Summary.** Before gathering any data, explained the standing approach (Foundation.md
§5.7): a derived relation $\sigma^4\sim\Gamma GMa_0$ with $\Gamma$ left explicitly
undetermined, one clean $\Gamma$-independent prediction (a $\tfrac14$-power zero-point
evolution with $a_0(z)$), and zero contact with real data. Asked whether this had been
tried before in the literature; answered honestly that the raw ingredients (σ, M, R_e
evolution for quiescent galaxies) are well-studied, but the *specific* comparison this
framework needs — its size-independent, $a_0(z)$-driven prediction against the standard
Newtonian, size-driven explanation — could not have been attempted by anyone else,
since it tests a premise unique to this project (a cosmologically evolving $a_0$).
Given the choice between a smaller local-only calibration and the harder discriminating
test, was told to attempt the harder one.

**Finding real data.** Delegated a literature search requiring every URL to be verified
by actual fetch, not recalled from training. Confirmed real and downloadable: ATLAS3D
(Cappellari et al. 2013a/b + 2011a for distances, 258 usable $z\approx0$ early-type
galaxies) as the local anchor, and three independent high-z compilations — van de Sande
et al. 2013 (73 galaxies, VizieR), Belli, Newman & Ellis 2014 (56 galaxies) and 2017
(24 galaxies with real σ, per the paper's own note that the rest are placeholders) —
covering $z=0.82$–$2.44$. Two real download near-misses caught by checking file sizes
rather than trusting HTTP 200: the ATLAS3D site had moved domains (old URLs redirected
to a frameset index, not the actual table), and the Belli IOP suppdata URLs needed the
journal's `0004-637X` path segment plus a `?doi=` query parameter — the initially
recalled URLs returned empty 200 responses.

**Two real parsing bugs caught before they became silent errors.** Van de Sande's
Table 4 has blank optional columns (axis ratio) for many rows; naive whitespace
splitting silently shifts later columns for exactly those rows — refetched as
tab-delimited TSV instead, where blank fields survive as empty tokens. Cross-matched
all three high-z catalogs by position (3") and found 18 duplicate objects between van
de Sande and Belli's tables (shared COSMOS/EGS/UDS fields); kept the more recent Belli
measurements, leaving 135 unique galaxies.

**A regime check that changed the calculation.** Computed the characteristic
acceleration $g=\sigma^2/R_e$ for both samples relative to $a_0$: median $g/a_0\approx
1.7$ (anchor) and $\approx3.0$ (high-z) — these are transition-regime systems, not
deep-MOND. The naive asymptotic formula from Foundation.md §5.7 would not be
self-consistent here. Reused the RAR fit's own AQUAL force-law inversion
(`mu_force_inv`) to compute the true interpolated $g_\text{obs}$ at any regime, and
calibrated a geometry constant $\Gamma_\text{geo}=0.211$ from the ATLAS3D anchor
(0.120 dex scatter — tighter locally than either the naive deep-MOND formula, 0.333
dex, or a pure-Newtonian virial constant, 0.148 dex).

**Result: real, bootstrap-robust, modest.** Applying the calibrated full-AQUAL model
(with this session's own fitted $a_0(z)$ trajectory) to the 135-galaxy high-z sample
gives smaller scatter (0.1266 dex) than a pure-Newtonian virial model (0.1345 dex) — a
gap a 2000-resample bootstrap puts at $+0.0078\pm0.0015$ dex, 100% of resamples
favoring AQUAL, robust in both redshift halves separately (not driven by the small
high-z tail). One puzzle reported rather than hidden: the naive, regime-inappropriate
asymptotic formula actually gives the single lowest raw scatter of the three models
tried (0.1185 dex) — an unresolved non-robustness, not swept under the rug. Real,
uncorrected caveats stated plainly: no IMF cross-check between ATLAS3D and the SED-fit
high-z masses; three heterogeneous surveys; unweighted local calibration.

**Also found and fixed, incidentally**: a leftover bug from an earlier renumbering
pass — §13 and §14's subsection headings were still labeled "14.1–14.3" and
"16.1–16.4" respectively (the renumbering script had only matched top-level `##`
headings, not `###` subsections). Fixed to "13.1–13.3" and "14.1–14.4". Also fixed two
stale `§5.5` cross-references to M-σ (now correctly §5.7).

**Full merge executed.** `Foundation.md` §5.7 rewritten in full with the real result,
caveats, and the open puzzle; §6 item 1's M-σ line updated to reflect the completed
first pass; two stale `§5.5→§5.7` cross-references fixed elsewhere. `ResearchNotes.md`
gained new §15 (the full derivation trail: data provenance, parsing pitfalls, the
regime check, the result, the puzzle) inserted before "Open Threads" (renumbered
§15→16, following this project's established convention of keeping that section last).

**Files updated:** `cdot-7/Fable-1/msigma_fit.py` (created), `cdot-7/Fable-1/data/
msigma/` (ATLAS3D, van de Sande, Belli 2014/2017 tables downloaded), `cdot-7/
Foundation.md` (§0, §5.7, §6 rewritten; two stale cross-references fixed),
`cdot-7/ResearchNotes.md` (new §15; Open Threads renumbered to §16; §13/§14 subsection
numbering bug fixed), this log entry.
