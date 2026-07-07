# Session Log — 2026-07-07

*Running log for cdot-6 work, appended per-prompt. One entry per user message from this
date; a new date gets a new file (`SessionLog-<date>.md`). Note: exact intraday
clock times are not available to the assistant — entries are ordered sequentially as
they occurred, not stamped to the minute. Discussion prior to this date (the DVFT and
EID paper reviews) is cdot-6-adjacent but not part of it, and is not logged here per the
author's instruction.*

---

## Entry 1

**Prompt (verbatim):**
> Good. That rules out a lot of distractions. Let's try a more minimalistic approach.  Instead of trying to solve everything, let's focus only on the minimal set of assumptions that we need to get the good results on MOND, RAR and MSigma in the context of a variable c. To get some foundation I suggest that we start from the foundation laid out in the Atkinson 1963 paper "General Relativity in Euclidian terms" and try to infer the minimum cosmological assumptions needed to establish tranformation equations that allows us  to change frame from our point of view with c_0 being the current value to c_z being the frame of an observer at z, under our assumption that the speed of light is entirely determined by the mass within the observers horizon. We'll take the connecton description as inspirational, but assume as little as possible about the specific connection, except that it is somehow Machian.

**Summary:** Researched Atkinson (1963) online (title, journal, PV lineage). Re-read
cdot-4's T22 (river/flow derivation, the withdrawn "Two-Regime Dictionary") and T11
(inertia, Sciama relation) to check for prior local-gravity work. Asked whether the new
framework should be required to fit DESI's BAO shape from the outset or defer that and
focus on local MOND/RAR/M-σ phenomenology first; author chose to defer DESI. Derived a
first, simple Machian cosmology (constant-density Sciama-type scaling, $c\propto
R_\text{horizon}$): redshift law unchanged, new finite-horizon distance law, proper age
$\approx13.97$ Gyr, a $g_\dagger$ candidate ($c_0H_0^\text{hor}$, $\approx2.8\times$ off
$a_0$, same ballpark as every earlier candidate), and a $q_0=+1/2$ flag for later. Noted
that cdot-4/5's RAR/M-σ results are already separable from the cosmological counting
law, so this new foundation doesn't change them by itself — the actual target (MOND from
this framework) is still undone.

**Files updated:** None (research and in-conversation derivation only).

---

## Entry 2

**Prompt (verbatim):**
> Let me add something here. Atkinson is the founding paper for PV, but it explisitly says nothing about gravity, which is something Puthoff added, and we have shown decisivly that LLR results excludes varying m and G in T8. With Atkinson foundational I think it is good to have that in scope. A copy of the paper is on disk: /mnt/data/roy/sync/docs/cosmology/Atkinson63.pdf, but it is a scanned journal version so pdftotext gives nothing. We may have to get it ocr'd.

**Summary:** Read `Atkinson63.pdf` directly via multimodal OCR (page images), since
`pdftotext` fails on the scan. Confirmed Atkinson's paper is narrower than Puthoff's
later Polarizable Vacuum extension: single stationary mass, no field equation sourcing
$c_r$ or $\mu_r$ from a mass distribution, no cosmological content, no time-dependence.
Checked cdot-4's T8 directly and found its LLR refutation is entirely about
*cosmological* $G\propto c^{-2}$ (a secular-drift test), not about Atkinson's *local*,
position-dependent, single-epoch postulates — meaning T22's earlier choice to also
forbid local mass-dressing was a parsimony choice, not something T8 independently
forced. This reopens Atkinson-style local dressing as a legitimate, never-actually-
refuted option for cdot-6.

**Files updated:** None (reading and analysis only).

---

## Entry 3

**Prompt (verbatim):**
> Since you have extracted the text from the Atkinson63 pdf, can you save that for later in references/Atkinson63.md

**Summary:** Flagged that Atkinson (1963) remains under copyright (UK term: life of
author + 70 years; Atkinson died 1982), so a full transcription would reproduce
essentially the whole paper. Proposed an alternative instead: a citation plus structured
notes (key equations, section-by-section paraphrase, page references), not a substitute
for the source. Asked the author to confirm before proceeding.

**Files updated:** None.

---

## Entry 4

**Prompt (verbatim):**
> Please do. Add also a summary of the most relevant parts of the paper. I just want to avoid re-scanning the print version of the paper, which is expensive.

**Summary:** Wrote the citation-and-notes file: full bibliographic citation, JSTOR link,
disk location of the source PDF, and a section-by-section summary (setup, the two ad hoc
postulates with their equations, the Lagrangian derivation, the redshift result, the
measuring-rod/clock-synchronization discussion, and a closing note on relevance to
cdot-6) — paraphrase throughout, with only the small number of equations needed for
technical reference quoted directly.

**Files updated:** `references/Atkinson63.md` (created).

---

## Entry 5

**Prompt (verbatim):**
> Let's start building a foundation document in cdot-6. We'll drop the Topic structure of the previous iterations for now, and just work towards the less ambitious goal of establishing the foundation principles for a cdot framework that can be used in the context of mondian physics. in addition to a new Foundation document, we can add a ResearchNotes documents that describes the path that led to the Foundation. I want the Foundation clean of all the cross references to earlier iterations so that it can stand on its own, while the cross references are preserved in the ResearchNotes.

**Summary:** Wrote `Foundation.md`: three premises (static Euclidean space with
independent time; Atkinson's local closure, stated exactly as he derived it; a
cosmological Machian extension replacing his single mass with the horizon's own enclosed
mass, self-consistently) plus a §4 conjecture for the MOND mechanism (not yet derived)
and a prioritized §5 open-items list — fully self-contained, no references to cdot-1
through cdot-5. Wrote `ResearchNotes.md` in parallel: why cdot-6 restarts rather than
patching cdot-5 (pointing to `cdot-5/T24_The_Cosmological_Sector_Closed.md`), the
rejected DVFT/EID papers, the Atkinson deep-dive, the T8/T22 gap, and working notes
behind the cosmological derivation. Updated project memory with the full rationale.

**Files updated:** `cdot-6/Foundation.md` (created), `cdot-6/ResearchNotes.md`
(created), project memory (updated).

---

## Entry 6

**Prompt (verbatim):**
> Good! Do a double check now that the bits in the Foundation document that are taken directly from Atkinson63 are cited as such, and that the relevant bit in the paper that is used is actually included in the summary.

**Summary:** Cross-checked every piece of `Foundation.md` §1–§2 against
`references/Atkinson63.md` and found none of it was actually attributed to Atkinson by
name — the "no cross-references to earlier iterations" instruction had been
over-applied to external academic citation too. Added explicit citations (footnote plus
inline attributions) at each point §2 uses Atkinson's own equations ($\psi$'s
definition, both postulates, the redshift relation, the exact-reproduction claim, the
exponent-generalization result), and confirmed each is covered in the reference notes.

**Files updated:** `cdot-6/Foundation.md` (citations added).

---

## Entry 7

**Prompt (verbatim):**
> Let's just go through the Foundation, and I will question some statements so that we can sharpen them for clarity. In premise 2, "ψ→0 far from any mass" means taking r to infinity, I presume. But then c approaches 0 with a power 2. So does it really go to zero?

**Summary:** Confirmed $c_r\to c$ (the fixed reference, not zero) as $\psi\to0$, and
explained why there's no self-reference in §2 for a power of $c$ to act back on (that
only happens in §3's cosmological closure). Re-deriving the exact isotropic-coordinate
location of $\psi=1$ in the process turned up a real error: `Foundation.md` had stated
the Schwarzschild radius as $r=2GM/c^2$, but the correct isotropic-coordinate value is
$r=GM/2c^2$ — a quarter of the more commonly quoted figure, which is the horizon's
location in the *Schwarzschild* coordinate, not the isotropic one this document uses.

**Files updated:** `cdot-6/Foundation.md` (§2.1 corrected).

---

## Entry 8

**Prompt (verbatim):**
> Next point. I don't really care for the c_∞ construction. At z = ∞ c should also go to ∞. I prefer to use 0, and keep the rule that the subscript on c referes to an observer at a given z.

**Summary:** Worked through what "$z=\infty$" could mean in this construction and found
a genuine ambiguity (standard past-looking redshift, where Machian reasoning demands
$c\to0$ at genesis, versus the future-direction blowup that only §3.5's crude fallback
relation actually has). Also flagged that $c_\infty$ was already shakier than it looked,
independent of the objection: §3.4's own non-monotonic $R_h(\psi_h)$ result means
$\psi_h=0$ isn't even an unambiguous stand-in for genesis in the exact construction.
Asked the author to confirm which direction was meant before editing.

**Files updated:** None (clarifying question only).

---

## Entry 9

**Prompt (verbatim):**
> No, no. Keep the standard past-looking redshift. I misconstructed the second sentence badly in the previous prompt. It was the sentence "some fixed, never-varying reference speed c_∞" that threw me off from the obvious z=∞ reading, becase we have agreed before that at z=∞ c must be 0, and then the equation for c(t) appears to become zero everywhere.

**Summary:** Confirmed the reductio precisely: genesis is $\psi_h=0$ (from
$M_h\propto R_h^3$), and substituting into Atkinson's rational function gives
$c=c_\text{ref}\cdot1=c_\text{ref}$, not zero — forcing $c_\text{ref}=0$ to fix this
collapses $c(t)\equiv0$ for all time, since that constant multiplies the whole function.
Rewrote `Foundation.md` §3: the direct "reuse Atkinson's local rational function for the
cosmological closure" construction is now **rejected outright** (not left as an open
technical wrinkle), with the earlier non-monotonicity finding kept as corroborating,
secondary evidence. Retired the `$c_\infty$` symbol entirely — every value of $c$ in the
document is now either $c_0$ (us, $z=0$) or $c_z$ (an observer at redshift $z$). The
provisional fallback relation (§3.4) already gets the genesis limit right by
construction ($c_z\to0$ as $z\to\infty$), so it needed no repair. Updated the §5 open-
items list and `ResearchNotes.md` §4 to match (recording both the numerical finding and
the sharper reductio, in the order they actually happened).

**Files updated:** `cdot-6/Foundation.md` (§3 rewritten, §5 updated),
`cdot-6/ResearchNotes.md` (§4 rewritten).

---

## Entry 10

**Prompt (verbatim):**
> As to "Throughout this document, c_0 denotes the value we measure, today (z=0)". We don't really measure c, do we? It is also a bit hard since our rulers are all stretchy and time too in a cdot cosomology. In SI units we have defined c_0 according to a cycle count. I think that is fixed permanently for any observer since length and time scales inversely with c. So the SI definition of c should work as a c_0 for any redshift, shouldn't it? But they would determine different z's for the CMBR.

**Summary:** Agreed and sharpened: under the SI convention (cycle-count second,
light-travel-time metre), $c$'s numerical value is a tautology for any
self-consistently-calibrated local observer, at any epoch — no local measurement can
ever catch a difference. Rewrote `Foundation.md` §3.1 to state that $c_0,c_z$ are
cross-epoch *relational* bookkeeping (the same role redshift $z$ itself plays), not
instrument readings — using the CMB example directly (two observers at different epochs
intercepting the same photons would infer different $z$, because each compares against
their *own* local reference) and tying this to Atkinson's own $c_r$ playing the same
non-local, comparison-only role in §2. This also sharpened §3.6 item 3 (previously
ambiguous "does a clock's tick rate depend on $c(t)$") into the actually well-posed
question: do two independently-built local clocks (atomic vs. orbital/gravitational)
drift *relative to each other* over cosmic time — precisely what the T8/LLR precedent
tested. Recorded the motivation and the T8 connection in `ResearchNotes.md`.

**Files updated:** `cdot-6/Foundation.md` (§3.1 rewritten, §3.6 item 3 sharpened),
`cdot-6/ResearchNotes.md` (new §6 added, subsequent sections renumbered).

---

## Entry 11

**Prompt (verbatim):**
> Could you please also write a SessionLog as we had in the subfolders of cdot-5. Start with the first prompt from today (ignore all earlier discussions as they are not related to cdot-6), include the verbatim user prompt with a timestamp, and a summary of the discussion and which files were updated as a result. Make the filename SessionLog-<date>.md, and keep appending to this file until the date changes.

**Summary:** Reconstructed today's prompt sequence from the start of the date (skipping
the prior day's DVFT/EID discussion, per instruction) and wrote this log, entries 1–10,
each with the verbatim prompt, a summary of what was discussed/derived, and the files
touched. Established the ongoing convention: append further entries to this same file
for the rest of 2026-07-07; start a new `SessionLog-<date>.md` when the date changes.

**Files updated:** `cdot-6/SessionLog-2026-07-07.md` (created).

---

## Entry 12

**Prompt (verbatim):**
> "The horizon grows at the local light speed" you say. Does it really? The distance to the horizon passes through any z from infinity to the current z, so on the map it must be an integral like we had in earlier versions of the Core, or do I misread this statement?

**Summary:** Confirmed no inconsistency: $\dot R_h=c(t)$ and $R_h(t)=\int_{-\infty}^t
c(t')\,dt'$ are the same relation in differential vs. integral form (fundamental
theorem of calculus), and checked this explicitly against §3.4's actual $c(t)$,
confirming the ODE solution matches the integral exactly given $H_0^\text{hor}\equiv
c_0/R_{h,0}$. Found a bonus consequence worth stating outright: in this single-relation
picture, $D_p(z\to\infty)=R_{h,0}$ — today's horizon radius and the total particle
horizon are the same quantity, unlike in more complex closures. Added the integral form
and this consequence to §3.2. While making that edit, caught and self-corrected two
accidental cross-references to earlier cdot iterations that had crept into the new
text — a standing-instruction violation, fixed before it needed to be pointed out.

**Files updated:** `cdot-6/Foundation.md` (§3.2 expanded, then corrected).

---

## Entry 13

**Prompt (verbatim):**
> Since the current foundation has a cosmologically varying mass, we need to check the LLR result from T8 in this framework.

**Summary:** Redid T8's self-consistent LLR calculation for cdot-6's own relations,
rather than leaving it as an open item. Took the natural first-try answer to §3.6 items
1–2 (strict $G$ and $\mu$ invariance, hence static orbits — removing T8's largest
contributor, orbital expansion) and used §3.4's provisionally-imported $\nu\propto c^2$
clock relation for item 3. Result: a residual, decisive exclusion survives from the
clock-rate channel alone — $\dot r_\text{LLR}/r_\text{LLR}=H_0^\text{hor}\approx13.8$
mm/yr against the $<0.058$ mm/yr bound, a $\times238$ exclusion — even with $G$ already
invariant and orbits already static. Cross-checked against T8's own published
three-channel sum ($-1+2+2=+3$ powers of $H_0^\text{hor}\to41.4$ mm/yr) and confirmed
this is the same arithmetic with the orbital-expansion term ($+2$) removed, leaving
$-1+2=+1$. Also flagged, as a retroactive note (not an edit to the closed document),
that cdot-4's own T8 doesn't appear to have re-checked this residual channel after
adopting invariant $G$ — it declared the problem solved once orbital expansion vanished.
For cdot-6, this means invariant $G$ alone is not sufficient: the framework's survival
now hinges on §5 item 4 (deriving the redshift/clock mechanism from §2's own closure)
producing something other than the imported $\nu\propto c^2$ relation — elevated to the
single most urgent open item.

**Files updated:** `cdot-6/Foundation.md` (§3.6 elevated from open question to computed
result), `cdot-6/ResearchNotes.md` (new §7.1 added).

---

## Entry 14

**Prompt (verbatim):**
> I see a bigger problem there. Even as far as cdot-3's T8 the LLR calculation is done with varying G and constant mass. PV requires both to vary.

**Summary:** Verified directly against `cdot-4/T8_Gravitational_Constant.md`: correct —
T8's self-consistent LLR calculation tests $G\propto c^{-2}$ against mass already taken
invariant (from T4's SN Hubble diagram fit, a separate test), not against PV's own
paired claim $m\propto c^{-3/2}$. T8's own text admits this ("the model already
abandoned PV for the mass scaling... once PV is abandoned for mass, the PV-native value
of $G$ loses its privileged status"), but `ResearchNotes.md` §3 had nonetheless
described T8 as having "decisively refuted [PV]" — an overclaim. Derived a general
two-parameter version of T8's calculation ($G\propto c^g$, universal mass $m\propto
c^s$, applied to Earth, Moon, *and* the electron mass setting atomic clock rates via the
Rydberg formula) and found the net LLR range-rate exponent is $E=-2s-g+1$ — reproduces
T8's own $E=3$ at $(g,s)=(-2,0)$, but gives $E=6$ at PV's actual point $(g,s)=(-2,-3/2)$
— **twice** T8's tested exponent, i.e. genuine PV is excluded by $\times1429$, more
decisively than T8's own $\times717$, not less. The softer clock-rate scaling under
running mass is more than offset by a much steeper orbital-radius scaling. Corrected the
overclaim in `ResearchNotes.md` §3 and added the full derivation as new §3.2, which also
unifies cleanly with cdot-6's own just-computed check ($E=1$ at $(g,s)=(0,0)$).

**Files updated:** `cdot-6/ResearchNotes.md` (§3 correction, new §3.2 added).

---

## Entry 15

**Prompt (verbatim):**
> Good. That was a necessary reality check. Now we need to decide where to go with the variable mass relation. If the varying rest mass of Atkinson is a blocker for getting consistent results as we have established before, and Atkinsons proofs holds for our case then that means that either our cdot model is wrong, or that GR only emerges under local conditions when cosmological conditions can be ignored.

**Summary:** Checked whether Atkinson's own $\mu_r(\psi)$, applied cosmologically via
§3.4's adopted closure, gives a different answer than the borrowed $\nu\propto c^2$
relation — found it reduces to invariant $\mu$ trivially (since $\psi_h$ is constant
under Sciama-type scaling by construction), which doesn't resolve item 3 since the
$c^2$ dependence actually comes from the electromagnetic sector ($\epsilon_0\propto
c^{-1}$), not from mass. Checked whether any mass-scaling exponent could cancel the LLR
signal: solving the general formula gives a unique value, $s=+1/2$, mathematically real
but unmotivated (opposite sign from every physical candidate, no basis in Atkinson's
postulates) — repeating exactly the "selected to fit, not derived" move already flagged
as a standing debt in cdot-4's own T8. Derived the sharper, decisive result: even with
*zero* local-physics coupling assumed (invariant $G$, static orbit, perfectly fixed
clock rate), the light-travel-time bookkeeping alone produces the same $\times238$-level
signal (opposite sign) — this is not a mass-law problem, it is an irreducible
consequence of $c(t)$ genuinely differing from its value 50 years ago, which is
premise 3's entire content. Recorded this as a load-bearing conclusion in `Foundation.md`
§3.6, and flagged (in `ResearchNotes.md` only) that a local/cosmological decoupling
premise, if pursued, would need to be structurally sharper than T22's withdrawn
"Two-Regime Dictionary." Presented the author with the resulting three-way fork and
asked for direction rather than choosing unilaterally, given how consequential the
decision is.

**Files updated:** `cdot-6/Foundation.md` (§3.6 extended with the irreducible-floor
result), `cdot-6/ResearchNotes.md` (new §7.2 added).

---

## Entry 16

**Prompt (verbatim):**
> Hold on. The original premise, disregarding PV or Atkinson, is that there exists a conformal transformation that applies to all local physics that translates from an expanding frame with constant c to an Euclidian frame with varying c. This works fine for EM, but fails for the laws of gravity that we have tested. What we need to do is to find the right transformation equations for gravity. You said that s=+1/2 could do it, but is it the only option or is there a family of solutions that could ensure that orbits does not expand, but shrinks in lockstep with atomic radii.

**Summary:** Confirmed "orbit shrinks in lockstep with atomic radii" is exactly
equivalent to the earlier $E=0$ (LLR-cancellation) condition, via an independent
Bohr-radius-based derivation ($a_0\propto c^{-1-s}$ vs. orbital radius $r\propto
c^{-(3s+g)}$; equal exponents give the same $g=1-2s$ line). Found this is a genuine
one-parameter family mathematically, but not practically: the independent, much
tighter direct $\dot G/G$ bound pins $g$ to within $\sim0.4\%$ of zero, collapsing the
family to a thin sliver around $s\approx1/2$. Also found that $s\ne0$ isn't a free,
local choice — the currently-adopted redshift relation ($1+z=(c_0/c_z)^2$) implicitly
assumes $s=0$; changing $s$ changes the redshift exponent to $s+2$ and propagates into
the whole §3.4 cosmology (age, distance, $q_0$). Attempted a principled (not fitted)
derivation of the mass-transformation exponent via a guessed conformal factor
$\Omega=c_0/c_z$, borrowing the standard scalar-tensor "$m\to m/\Omega$" rule — got
$s=+1$, which does not cancel the signal either (gives $E=-1$), and flagged this
derivation as unverified speculation, since Foundation §1 never actually constructs the
FRW↔static correspondence explicitly.

**Files updated:** None (in-conversation derivation only).

---

## Entry 17

**Prompt (verbatim):**
> I don't think we have to include the full transformation equations from FRW to cdot. The assumption is just that a canonical transformation exists between an expanding universe framework and an Euclidian universe framework with varying c. The whole idea is that if we manage to find what ingredients are needed to get physics to work in the cdot framework, it will reveal what is missing in the FRW framework to get to MOND. MOND implies that FRW cosmology has a missing ingredient, so it is premature to search for the full transformation set yet.

**Summary:** Adopted the methodological correction: the FRW↔cdot correspondence is a
working assumption, not something to construct now; the actual strategy is to find what
cdot's own internal consistency (LLR safety, MOND phenomenology) requires, since that
result is the candidate for "what standard cosmology is missing." Recorded this as a new
methodological note in `Foundation.md` §0. Redirected effort to Foundation §4's MOND
conjecture instead of the FRW transformation. Derived an exact (non-perturbative) closed
form from Atkinson's own two postulates, $\mu_rc_r^2=\mu c^2(1-\psi)/(1+\psi)$, and used
it to test the additive conjecture ($\psi=\psi_\text{loc}+\psi_h$) exactly: the resulting
force law, $F=-GM\mu/[(1+\psi_h)r+k]^2$, reduces to ordinary $1/r^2$ gravity at every
radius (just a constant rescaling of $G$) — no MOND transition at any order. Rejected
the additive conjecture outright (not "unconfirmed," but checked and false) and
identified the likely fix: MOND's interpolating functions depend on the *ratio*
$\psi_\text{loc}/\psi_h$, not the sum, so a non-additive combination is needed instead.
Flagged this as the new single most important open calculation and checked with the
author before committing effort to a specific non-additive guess.

**Files updated:** `cdot-6/Foundation.md` (§0 methodological note added; §4 conjecture
section rewritten with the exact rejection and the new direction).

---

## Entry 18

**Prompt (verbatim):**
> Re-derive the two-mass Machian closure from scratch (selected via AskUserQuestion, over ratio-substitution and working backward from phenomenology).

**Summary:** Noted that Atkinson's $\psi(r)$ was never derived from a Machian principle
in the first place — it's imported directly from the known Schwarzschild solution, then
reverse-engineered into local postulates — so "re-derive from scratch" means asking what
a genuine two-source closure requires, not generalizing his formula. Proved a general
result covering far more than the additive guess: for *any* smooth function $f$ combining
$\psi_\text{loc}$ and $\psi_h$ additively, the force at large $r$ is $\propto f'(\psi_h)
k/r^2$ — ordinary $1/r^2$, for any $f$, any size of $\psi_h$. Checked this isn't an
artifact of naive potential-summing either, by directly computing the Newtonian potential
of a point mass in a uniform background out to the horizon (background contribution
varies as $r^2/R_h^2$ across a galactic region — negligible). Concluded no closure built
on "$c_r,\mu_r$ depend on a combined potential *value*" can produce MOND, regardless of
how the combination is constructed. Identified the likely fix by analogy to standard
modified-gravity formulations (AQUAL/QMOND), which modify the field/acceleration
$|\nabla\Phi|$, not the potential: since $\psi_h$ is spatially uniform ($\nabla\psi_h=0$),
it can't contribute via a gradient — but it does carry a *temporal* rate, $H_0^\text{hor}$,
already used throughout §3 as a MOND-scale candidate. Proposed splitting roles:
$\nabla\psi_\text{loc}$ sets the local field strength, $H_0^\text{hor}$ sets the reference
acceleration scale — structurally $a/a_0$, built from a gradient and a rate rather than
two summed potentials.

**Files updated:** `cdot-6/Foundation.md` (§4 extended with the general rejection and the
field-strength direction).

---

## Entry 19 — cdot-6 superseded

**Prompt (verbatim):**
> Ok. It is time to step away from Atkinson then. Let's go with your suggestion of using the 'spirit of AQUAL'. Please rewrite the Foundation into cdot-7, and start building everything again. I think we can settle on s=+1/2 exactly and write the equations under the premise that all local physics must scale the same way with c.

**Summary:** cdot-6 is superseded as of this entry. Author decided to drop Atkinson's
local closure entirely (per the general, structural MOND-rejection result found in
Entry 18) and start a new iteration, cdot-7, built on an AQUAL-spirit modified-gravity
postulate, with $s=+1/2$ (universal local mass scaling, $G$ exactly invariant) adopted
as an exact premise rather than a fitted number. Added a superseded-status header to
this document pointing to `cdot-7/`. Full continuation logged in
`cdot-7/SessionLog-2026-07-07.md` from this point forward.

**Files updated:** `cdot-6/Foundation.md` (superseded-status header added).
