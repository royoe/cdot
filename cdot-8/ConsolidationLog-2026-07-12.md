# Consolidation Log — Candidate Improvements to cdot-7, Harvested from cdot-8

*Status: proposals only. Nothing here has been applied to any `cdot-7/` file — per the
proposal's own charter, "nothing from cdot-8 is citable inside cdot-7 except as
'proposed,'" and this document does not change that. Purpose: cdot-8 is a completion
attempt running alongside cdot-7, not a replacement, and its work-package sessions
(WP0–WP1 addendum, as of 2026-07-12) have produced several findings that are true and
useful independent of whether cdot-8 itself ultimately passes its gates or is killed.
This log exists so that value is not lost either way — **if cdot-8 fails, these items
should still go through the normal consolidation process into cdot-7**, since none of
them depend on AeST, the census foliation, or any other cdot-8-specific machinery
surviving. Each item states its source, its confidence level, and a concrete proposed
action, so the consolidator can triage quickly rather than re-derive.*

---

## Item 1 — The two-clock dictionary (HIGH confidence, HIGH value)

**Source**: `cdot-8/WP1/Update-WP1-Addendum-TwoClockDictionary-2026-07-12.md`.

**The finding**: Foundation nowhere states that cdot-7 has *two* distinct time-like
quantities — the coordinate time $t$ that $\dot R_h=c$ and $a_0=\lambda\dot c$ are
defined on, and matter's own proper time $\tau$ (what atomic clocks, ages, and
astrophysical processes actually measure) — related by
$$\frac{d\tau}{dt}=\left(\frac{c}{c_0}\right)^{5/2}.$$
This is not new physics cdot-8 introduced: **`cdot-7/Fable-1/closure_dynamics.py`
already implements this distinction silently**, tracking `tau_proper` and `t_coord` as
separate ODE state variables since 2026-07-07 (predating cdot-8 entirely), with its own
validation line confirming `tau_proper` — not `t_coord` — gives the finite,
EdS-matching $\tfrac23H_0^{-1}$ age quoted in Foundation §5.2. The project's own code
already had this right; the prose never said so, and that gap is exactly what caused a
several-hour debugging detour in cdot-8/WP3 chasing what looked like (but was not) a
fatal internal inconsistency.

**Why this matters independent of cdot-8**: anyone reading Foundation.md's equations
literally — using $t$ as a single, undifferentiated symbol in both $\dot R_h=c$ and in
age/distance discussions — will derive an apparently-divergent particle horizon and an
apparently-contradictory age, exactly as cdot-8's WP3 initially did. This is a landmine
for any future reader or session, with or without a covariant completion in the
picture.

**Proposed action**: add one paragraph to Foundation §2 (near the $R_h$/$\dot R_h=c$
definition, or as a new remark in §3), stating explicitly:

> *Two distinct time-like quantities appear in this document under the shared symbol
> $t$: the coordinate time on which $\dot R_h=c$ and $a_0=\lambda\dot c$ are defined,
> and the proper time $\tau$ of an ordinary (atomic-clock, astrophysical) observer,
> related by $d\tau/dt=(c/c_0)^{5/2}$. The two coincide today ($c=c_0$) and diverge
> into the past. Ages (§5.2's $\tau_\infty$, the four-term fit's quoted age) are always
> $\tau$-quantities; the closure ODE's own "dot" is always a $t$-derivative.*

**Recommended verification before merging**: confirm the exact provenance script for
the four-term fit's quoted 12.9 Gyr age (see Item 2) — the paragraph above should cite
it once confirmed.

---

## Item 2 — Confirm which clock the four-term fit's 12.9 Gyr age is on (MEDIUM
confidence — open verification task, not yet a finding)

**Source**: same document, §6.

**The situation**: `closure_dynamics.py` (the fixed-point demonstration script)
unambiguously uses `tau_proper` for its age output, confirmed against the $\tfrac23
H_0^{-1}$ EdS value. But the actual four-term-fit trajectory's age (12.9 Gyr, Foundation
§5.5, the number compared against globular-cluster ages) was not found computed by any
standalone script in `cdot-7/Fable-1/` during this session's search — `four_term_fit.py`
computes distances but does not track an age/$\tau$ state at all. The 12.9 Gyr figure's
exact origin (which script, and on which clock) was not directly traced.

**Proposed action**: a bounded, cheap follow-up task — locate or reconstruct the
calculation behind the 12.9 Gyr figure (likely an ad hoc extension of
`closure_dynamics.py`'s `tau_proper` integration to the fitted $\epsilon_0=-0.0909$
trajectory rather than the pure fixed point) and confirm it used $\tau$, not $t$. If
confirmed, no cdot-7 number changes — only Item 1's documentation paragraph needs to
cite it. If it turns out the figure was computed on $t$ rather than $\tau$, this would
be a real numerical correction to Foundation §5.5, not merely a documentation gap, and
should be flagged back with higher priority.

---

## Item 3 — An explicit evolution equation for the Planck-unit census (MEDIUM
confidence, LOW–MEDIUM value — optional addition)

**Source**: `cdot-8/WP2/Update-WP2-CovariantCensus-2026-07-12.md`, §2.

**The finding**: cdot-7 defines $\mathcal N(t)\equiv\sum E_i(t)/E_P(t)$ (Foundation
§2.1) and $M_h=\mathcal N m_P$, but only ever uses $\mathcal N$ algebraically — it never
writes down $\dot{\mathcal N}$. This is derivable **purely from cdot-7's own existing
definitions**, with no AeST or covariant machinery needed at all:
$$\frac{\dot{\mathcal N}}{\mathcal N}=\left(p-\frac52\right)\frac{\dot c}{c}+\frac{3c}{R_h},$$
for a species of coordinate energy-density exponent $p$ (matter $p=\tfrac52$, radiation
$p=1$) — a clean split into a "weight-drift" term (how an already-enclosed entity's own
census weight changes) and a "shell-sweep" term (new entities entering as the horizon
grows). For matter, the weight-drift term vanishes identically — a direct, derived
consequence of premise 3's invariance ("epoch-invariant by premise 3," Foundation
§2.1) rather than merely an assertion about a ratio.

**Why this might be worth adding**: it's a small, free, self-contained result — cdot-7
already has every ingredient needed to state it, and it upgrades a previously
qualitative claim ("epoch-invariant... the counting law is the Machian face of Planck-
unit invariance") into an explicit, checkable differential statement. Not essential —
flagged as optional, lower priority than Items 1–2, since it doesn't fix a bug or
prevent confusion, it just adds a derivable corollary.

**Proposed action**: if the consolidator has bandwidth, add this as a short remark in
Foundation §2.1 or §2.4, alongside the existing census discussion. No urgency.

---

## Item 4 — The recurring "one scalar, two incompatible jobs" pattern, as explicit
self-knowledge (LOW priority, easy add)

**Source**: `cdot-8/WP0/Update-WP0-FullPass-2026-07-11.md`, Part A.

**The finding**: tracing cdot-1 through cdot-8's history directly (not merely
cdot-6/7's own back-references) shows the "two dictionaries" obstruction that motivated
cdot-6→7's abandonment of GR-compatibility (Foundation's own D1-adjacent framing) is not
a single lesson — it is the same structural failure, independently rediscovered **at
least five times** under five different names: cdot-2's conformal-projection Branch A/B
fork (killed by Etherington reciprocity); cdot-3/4's PV mass/$G$ pairing (killed by
LLR); cdot-4/T22's Two-Regime-Dictionary-vs-river uniqueness theorem; cdot-4/T23's
$D_H=dD_p/dz$ "lock"; cdot-6's LLR-floor-plus-MOND-no-go.

**Why this is worth recording regardless of cdot-8**: this convergence is stronger
evidence that the obstruction is real and structural, not an artifact of any one
formulation — a fact worth having explicitly on record in `ResearchNotes.md` for
whoever next considers a relativistic or GR-adjacent extension of cdot-7's line,
whether or not cdot-8 is the vehicle that does it.

**Proposed action**: add a short table (stage, local name, the two incompatible jobs)
to `cdot-7/ResearchNotes.md`, cross-referencing the existing per-stage accounts already
scattered across `cdot-2` through `cdot-6`'s own `ResearchNotes.md` files. Low cost,
pure historical bookkeeping — no technical content to verify.

---

## Item 5 — Etherington reciprocity as a standing, reusable diagnostic (LOW priority,
methodology note)

**Source**: `cdot-8/WP0/Update-WP0-FullPass-2026-07-11.md`, Part A.2.

**The finding**: cdot-2's OP-9 used the Etherington reciprocity theorem
($d_L=(1+z)^2d_A$, exact in any metric theory from photon-number conservation on null
geodesics alone) to decisively kill the conformal-projection hypothesis by showing a
claimed correspondence actually diverged from its target by up to $1.89\times$ at
$z=2$. This is a cheap, general-purpose, already-battle-tested tool for exactly one
recurring question this project keeps needing to ask: *is this claimed correspondence
between two descriptions genuine, or does it only hold to leading order / at low $z$?*

**Proposed action**: no Foundation edit needed — just a one-line methodology note in
`ResearchNotes.md`'s existing methods/lessons section (if one exists) or in the K6-style
methodology list, naming Etherington reciprocity explicitly as a standing check to run
whenever a new correspondence claim is made, rather than rediscovering the tool each
time it's needed.

---

## Item 6 — Item 9's status, flagged for re-examination but not resolved here (LOW
confidence, do not merge without independent re-derivation)

**Source**: `cdot-8/WP1/Update-WP1-DictionaryAsFrameMap-2026-07-12.md`, §5's "bonus
discharge" claim.

**Caveat, stated up front**: an earlier WP1 pass claimed Foundation §6 item 9 ("particle
number density $n$ is homogeneous and constant — assumed, not derived") is "discharged"
as ordinary FRW particle-number conservation. **On reflection while assembling this
log, that discharge leaned on the AeST/comoving-coordinates embedding specifically** —
within cdot-7's own native, standalone static-space picture (no expansion at all,
by premise 1), the honest statement is weaker: constant density follows trivially from
constant particle number *if* there is no bulk relative motion between particles, but
*why* particle number is conserved and *why* there is no bulk flow are still open
within cdot-7's own terms, without borrowing the AeST correspondence. **Do not merge
this as a resolved item** — flagging it here only so a future session revisits item 9
with a cdot-7-native argument, or explicitly imports the AeST-based one with that
dependency stated, rather than quietly treating it as closed.

---

## Item 7 — A deep-radiation expansion-rate marker, $\Delta N_\text{eff}\approx-0.5$
(MEDIUM confidence — a flag about the shared background, not about cdot-8's embedding)

**Source**: `cdot-8/WP3/Update-WP3-BudgetTension-2026-07-12.md` and
`cdot-8/proposal/Advisory-WP3-BudgetInvoice-2026-07-12.md`, via `budget_invoice.py`.

**The finding**: Friedmann-accounting the actual, already-fitted census trajectory
(the same $H(z)$ history cdot-7's own four-term fit already commits to — this is a
statement about cdot-7's background, not about AeST or any covariant embedding) gives
a deep-radiation-era expansion rate $H/H_\text{standard}\approx0.966$, an effective
$\Delta N_\text{eff}\approx-0.5$ relative to the standard $N_\text{eff}=3.044$ —
roughly a $3\sigma$-scale tension against primordial-abundance/CMB constraints on
$N_\text{eff}$, at face value.

**Explicit caveats, not yet resolved**: (i) the trend value was read at the edge of the
computed grid ($z\sim5\times10^5$), not extrapolated to the actual BBN epoch; (ii) the
$e^+e^-$/QCD census re-weighting kinks — a "well-posed, uncomputed" item already
handed off in the 2026-07-11 session (`cdot-7/Radiation-1/`) — sit exactly at the BBN
epoch and are now load-bearing for trusting this number. **This is not yet a confirmed
tension** — it is a marker worth cdot-7 computing properly (finishing the already-queued
$e^+e^-$/QCD kink calculation, then re-checking $N_\text{eff}$ against the completed
census trajectory) regardless of cdot-8's fate, since it concerns cdot-7's own
background history, independently of any covariant completion.

**Proposed action**: hand to whoever next picks up the 2026-07-11 $e^+e^-$/QCD census
kink handoff — compute the kinks, then re-derive $N_\text{eff}$ from the completed
(not deep-radiation-extrapolated) census trajectory and compare against current
Planck/BBN bounds. If the tension survives, it is a genuine, external
falsification-relevant result for cdot-7 itself; if the kinks absorb it, no action
needed beyond noting the check was done.

---

## Item 8 — Foundation §5.5's $\hat a_0(z)$ equation is mislabeled: absolute values
presented as a ratio (HIGH confidence, MEDIUM priority)

**Source**: `cdot-8/proposal/Advisory-WP3-InverseReconstruction-2026-07-12.md` §3,
`inverse_reconstruction_check.py` part 1; independently confirmed in
`cdot-8/WP3/Update-WP3-ReconstructionResolved-2026-07-12.md` §1 against the actual
Foundation.md source (not merely the advisory's script).

**The finding**: Foundation.md line 869 states
$$\hat a_0(z)/\hat a_0(0)=1.69,\ 2.35,\ 2.57,\ 3.30\quad\text{at }z=0.33,\ 0.85,\ 1.00,\ 1.44$$
explicitly labeled as a ratio. Recomputing the true ratio from the four-term-fit
trajectory (`Fable-1/a0_confrontation.py`'s own formula) gives $1.22,\,1.70,\,1.86,\,
2.38$ — the quoted values are these true ratios multiplied by $1.385$–$1.386$
uniformly across all four points, matching the fit's own anchor $a_0(0)=1.39\times
10^{-10}$ m/s² (Foundation §2.2) to three digits. Independently corroborated: the
same section's own figure (Foundation.md lines 895–902) plots this quantity directly
against MUSE-DARK's and MIGHTEE-HI's *absolute* measurements ($2.38\times10^{-10}$,
$1.69\times10^{-10}$ m/s²) on one consistent axis — only coherent if Foundation's own
numbers are also absolute, not a dimensionless ratio.

**Proposed action**: relabel the equation (or divide the displayed values by $1.39$
and state that explicitly); one line. True ratios for the corrected display:
$1.22,\,1.70,\,1.86,\,2.38$.

---

## Item 9 — An exact identity: $\hat a_0(z)=\tfrac23\lambda c_0H_{\hat\tau}(z)$, on any
trajectory (HIGH confidence, LOW–MEDIUM priority, optional)

**Source**: same advisory §4(i); independently re-derived from scratch in
`cdot-8/WP3/Update-WP3-ReconstructionResolved-2026-07-12.md` §1 (checked algebraically
at five arbitrary points, not just the fixed point or today).

**The finding**: from $a_0=\lambda\dot c$ (Foundation's own definition), $H_t=\tfrac32
\dot c/c$ (exact, from the redshift law alone), the acceleration Planck-unit exponent
$7/2$ (dimensional analysis), and the two-clock dictionary's $H_\tau=H_t(c/c_0)^{-5/2}$
— $\hat a_0(z)=\tfrac23\lambda c_0H_\tau(z)$ follows as a three-line algebraic identity,
holding *exactly*, on *every* trajectory, not merely as a fixed-point coincidence. The
long-noted "$a_0\sim cH_0$" MOND numerology is, in this framework, not an
approximate coincidence to be explained — it is enforced exactly by construction.

**A consequence worth flagging alongside it (from the same advisory pair's audit,
`Addendum-ThirdEscalation-Assessment-2026-07-12.md` Flag 1)**: this identity means
Foundation §5.5's $\hat a_0(z)$ data confrontation and the four-term SN Hubble-diagram
fit are *the same prediction* ($H_\tau(z)$'s shape) tested against two different
datasets — not two independent successes, which is how the evidence currently reads.
This is a genuine strengthening (one function, two data channels, both passing) but a
bookkeeping correction the evidence ledger owes itself. The sharpest surviving,
genuinely independent discriminator against parameter-$a_0$ theories is the *locking*
itself: measure $\hat a_0(z)$ and $H(z)$ separately from independent data; this
framework demands their ratio be constant, which no parameter-$a_0$ theory is obliged
to satisfy.

**Proposed action**: add the identity as a one-line remark in Foundation §5.3/§5.5
(costs nothing, strengthens existing prose); separately, adjust the evidence-ledger
language wherever $\hat a_0(z)$ agreement and the SN fit are cited as independent
confirmations, to note they share one underlying prediction.

---

## Item 10 — Canonical value request: is $x_0=1.10$ exact-by-convention or rounded?
(LOW priority, reproducibility hygiene)

**Source**: `Addendum-ThirdEscalation-Assessment-2026-07-12.md` Flag 5.

**The finding**: cross-script comparison this session found `cdot-7/Fable-1/*.py`
scripts using the quoted $x_0=1.10$, while a cdot-8 advisory's independent
re-fit used the evidently-unrounded $x_0=1.0958$. Three-digit agreement in all
downstream comparisons survives either choice, so this is not urgent, but future
scripts would benefit from Foundation stating which is canonical.

**Proposed action**: one line in Foundation §2.2/§5.5 stating whether $1.10$ is the
adopted, rounded display value or whether a more precise value should be used in
scripts going forward.

---

## Item 11 — Methodology: verify the solution is the physical one before verifying
algebra on it (MEDIUM priority, general lesson)

**Source**: recurring across WP3's rounds 2026-07-12 through 2026-07-15
(`cdot-8/WP3/Update-WP3-BudgetTension-2026-07-12.md` through
`Update-WP3-SchemeTestPartial-2026-07-15.md`), stated explicitly as the
advisory's own lesson after round 2.

**The finding**: several of WP3's escalations (traced back afterward) turned out to
be checking correct algebra against the WRONG solution — an idealized fixed point
instead of the actual fitted trajectory, or a free-field equation of motion instead
of the census-constrained one. This is a general methodology trap, not specific to
AeST or cdot-8's action-level machinery: **before trusting any confrontation number,
confirm which solution branch is actually being evaluated, separately from checking
the algebra is right on it.**

**Proposed action**: a one-line methodology note in `ResearchNotes.md`'s existing
lessons section, alongside Item 5's Etherington-reciprocity entry. No technical
content to verify; purely a process reminder.

---

## Item 12 — BBN physics: use true-equilibrium (not frozen/decoupled) statistics for
$e^+e^-$ in any census/closure calculation reaching BBN-era redshifts (HIGH
confidence, MEDIUM-HIGH value if cdot-7 ever computes its own BBN confrontation)

**Source**: `cdot-8/WP4b/Update-WP4b-BBN-2026-07-16.md` and the correction rounds
through `Update-WP4b-RebuttalWithdrawn-2026-07-17.md`.

**The finding**: $e^+e^-$ pairs stay in full thermal *and chemical* equilibrium
through the annihilation epoch and genuinely annihilate away — the correct
distribution is the true equilibrium Fermi-Dirac form (energy, not momentum, in the
exponent). This is the opposite of neutrinos, which decouple and free-stream (frozen
distribution, momentum in the exponent). Reusing the frozen/neutrino-style treatment
for $e^\pm$ (an easy mistake — caught and corrected twice this session, including once
by the author's own advisor loop) gives qualitatively wrong behavior (density growing
instead of Boltzmann-suppressing).

**Why this matters independent of cdot-8**: this is a plain physics fact about
statistical mechanics near the QED epoch, not anything AeST- or census-specific. Any
future cdot-7-native BBN/$N_\text{eff}$ calculation (see Item 7, still gated on this
exact kink) needs this distinction to get the $e^+e^-$ contribution right.

**Proposed action**: fold into whichever script eventually computes Item 7's deferred
$e^+e^-$/QCD census kink for cdot-7 directly — flag this distinction explicitly in
that script's own documentation so it isn't rediscovered the hard way a third time.

---

## Item 13 — BBN physics: the photon-temperature boost $(11/4)^{1/3}$ follows from
entropy conservation, not energy conservation (HIGH confidence, LOW-MEDIUM value,
mostly a derivation-hygiene note)

**Source**: same WP4b rounds as Item 12, particularly
`Update-WP4b-Converged-2026-07-17.md`.

**The finding**: naive coordinate-energy conservation across the $e^+e^-$ annihilation
transition gives the wrong exponent, $(11/4)^{1/4}$; the correct derivation needs
entropy conservation (the right principle for a bulk, many-body conversion, as opposed
to single-particle energy bookkeeping), which reproduces the standard $(11/4)^{1/3}$
boost from first principles. cdot-7 already *uses* this factor
(`Fable-1`'s $T_{\nu,0}=(4/11)^{1/3}T_{\gamma,0}$) but, as far as this session's
search found, without deriving it in-repo.

**Proposed action**: optional — if cdot-7 ever wants this factor derived rather than
cited, this is the correct principle to use. No urgency; the currently-used numerical
value is already right.

---

## Item 14 — CMB methodology: the correct acoustic-scale distance convention is
$\theta_*=r_s(z_*)/D_p(z_*)$, NOT $r_s/D_A$ (HIGH confidence, HIGH value — directly
corrects a historical cdot-4/cdot-5 methodology error)

**Source**: `cdot-8/WP4a/Update-WP4a-AcousticScale-2026-07-16.md` §2; the historical
error itself flagged in `cdot-8/WP0/Update-WP0-FullPass-2026-07-11.md` (cdot-4/cdot-5's
CMB attempts used $D_A\equiv D_p$, while cdot-7's own §5.5 proves $d_A=D_p/(1+z)$ — a
live cross-stage contradiction, not previously reconciled).

**The finding**: in a variable-$c$/lockstep-ruler framework of this kind, the correct
acoustic-scale formula is $\theta_*=r_s(z_*)/D_p(z_*)$ (proper-motion distance, the
"comoving-type" quantity whose $(1+z_*)$ factors cancel against $r_s$'s own), derived
directly from Foundation §5.5's own lockstep-ruler formula — *not* the angular-diameter
distance $D_A=D_p/(1+z)$ cdot-4/cdot-5 used, which produced the historical 9$\times$–
765$\times$ CMB failures WP0 found (later "corrected" to a 1.3–1.4$\times$ overshoot,
with $z_*$ never resolved from first principles in that earlier work either).

**Why this matters independent of cdot-8**: this is a convention/derivation fix
applicable to cdot-7's own machinery directly, useful for any future cdot-7-side CMB
attempt regardless of cdot-8's fate — the historical failures were, at least partly,
a distance-convention bug, not necessarily evidence the underlying physics was as badly
wrong as 9–765$\times$ suggested.

**Proposed action**: flag prominently in `ResearchNotes.md`/wherever cdot-7's CMB
attempt history is recorded, so a future attempt starts from the corrected convention
rather than repeating cdot-4/cdot-5's own error.

---

## Item 15 — Methodology: a "z=0 sanity check" is not always the right diagnostic —
verify what the compared quantities actually decompose into first (MEDIUM priority,
general lesson, cautionary rather than a fix)

**Source**: `cdot-8/WP4b/Update-WP4b-RebuttalWithdrawn-2026-07-17.md`.

**The finding**: a plausible-looking, seemingly decisive check — "any correctly
normalized ratio must equal 1 at $z=0$" — was applied to $E(0)/\sqrt{\hat u(0)}$ and
wrongly read as a bug (ratio $=3.67$). It was in fact correct: $\hat u$ is only the
matter+radiation census content, deliberately excluding a separate dark-energy-like
"invoice" sector that dominates today. The check itself wasn't wrong as a *tool* — it
was applied without first confirming what's actually being compared decomposes into.

**Why this matters independent of cdot-8**: a general caution for this project's own
future normalization/consistency checks (of exactly the kind Items 2, 9, and 10 above
already involve) — a quick sanity check can look decisive and still be a category
error if the two sides of the comparison aren't verified to mean the same thing first.

**Proposed action**: fold into the same `ResearchNotes.md` methodology-lessons section
as Items 5 and 11 — one more line, not a technical change.

---

## Item 16 — FLAGGED CONCERN (not an improvement): a new, external, recent measurement is in serious tension with cdot-7's own established interpolating-function/$a_0$ choice (HIGH severity, requires author review, not a fix to merge)

**Source**: `cdot-8/WP6/Update-WP6-TensorSpeedStructure-2026-07-18.md`
(new sub-task, 2026-07-19), `wp6_q2_efe_check.py`,
`references/arXiv.2602.17884.md`. Unlike every other item in this log,
this is **not a candidate improvement** — it is a flagged external
tension, routed here per this program's standing convention (findings
relevant to cdot-7, cdot-7 itself never touched) because it bears
directly on cdot-7's own headline fit result, not anything cdot-8-
specific.

**The finding**: Park, Hees, Famaey, Desmond & Durakovic (2026,
arXiv:2602.17884) report an improved Cassini/DE440 bound on the Solar
System quadrupole $Q_2=(1.6\pm1.8)\times10^{-27}$ s$^{-2}$ — the
"External Field Effect" (EFE) of AQUAL/QUMOND-type MOND, which depends
*solely* on the interpolating function's (IF's) shape near $a_0$ (the
Milky Way's external field at the Sun, $e_N=O(1)$–$O(2)$ in $a_0$
units), not on how sharply the IF approaches Newtonian gravity far
above $a_0$. **cdot-7's own established, explicitly-preferred fit**
(Foundation.md: the Simple IF, $\kappa=1$, $\mu(x)=x/(1+x)$, preferred
over the standard IF at every fit stage, $\Delta\chi^2\approx13$ at the
four-term fit; $a_0=1.39\times10^{-10}$ m/s²) **predicts $Q_2\approx
3.71\times10^{-26}$ s$^{-2}$ — roughly $23\times$ the new bound's
central value, $\sim21\sigma$ in tension.** Checked whether switching
to the RAR alternative IF (also explored, though not preferred, by
cdot-7) helps: using cdot-7's own RAR-alone-preferred $a_0\approx1.26
\times10^{-10}$ m/s² gives essentially the *same* tension ($\sim23
\times$, $\sim21\sigma$) — **not a quirk of one IF family, a generic
feature of any shallow-transition ($n,\delta,\gamma\sim1$) IF
calibrated near cdot-7's own $a_0$.** The computation machinery was
validated against the paper's own published number before being
applied (reproduced their $\delta=1$ RAR-IF/$a_0=1.02\times10^{-10}$
case to 4 significant figures: $e_N=1.6433$ vs. their quoted $1.643$,
$Q_2=3.3869\times10^{-26}$ vs. their quoted $3.387\times10^{-26}$) —
this is not an assumed or hand-waved number.

**Why this matters independent of cdot-8's own fate**: this is a test
of cdot-7's own AQUAL-based galaxy/Solar-System framework directly — it
does not depend on AeST, the census, or any cdot-8-specific machinery
surviving. If cdot-8 is killed at any later stage, this finding still
applies to cdot-7 as it stands today.

**What this does NOT establish**: whether AeST's/cdot-8's own
quasistatic completion (a separate, not-yet-derived object from cdot-8's
own first principles — see WP6 sub-task 1) shares this tension; that
depends on AeST's own near-$a_0$ IF shape, not yet derived. This item is
about cdot-7's own established fit specifically.

**Proposed action**: **NOT a bounded task ready to merge — requires
author review.** This is a genuine, quantified ($\sim20\sigma$-class)
tension between cdot-7's headline four-term-fit result and a recent,
carefully-validated Solar-System measurement, surfaced by the user
supplying the citation and asking for it to be checked. No unilateral
verdict is offered here (consistent with this program's standing
discipline of escalating rather than deciding consequential findings
alone). Recommend: author decides whether/how to route this into
cdot-7's own record (e.g., a new flagged tension in Foundation.md's own
gating structure, alongside its existing SN/RAR/mass-census tension
already documented in the four-term fit write-up), independent of
cdot-8's own trajectory.

**Advisor assessment added, 2026-07-19** (`cdot-8/WP6/advisory/
Advisory-WP6-Q2EFEAssessed-2026-07-19.md`): verified independently
(paper, authorship, 40% improvement figure all confirmed via live
search); the worker's validation-before-computation discipline was
specifically called out as the absolute-anchor rule applied correctly.
**Mechanism named**: the EFE quadrupole is imprinted at the MOND
transition radius $r_t\sim\sqrt{GM_\odot/a_0}\approx6500$ AU (checked
directly against cdot-7's own $a_0$); Saturn at $9.5$ AU sits deep
*inside* this radius, in a region that is Newtonian regardless of
screening — an interior point cannot screen an externally-imposed
tidal term, it only transmits it. This is *why* sub-task 1's screening
resolution doesn't transfer here. **Precise scope, sharpened**: the
Simple IF and $a_0=1.39\times10^{-10}$ m/s² are program *choices*
(Foundation's own preferred fit among alternatives considered), not
census-derived structure — the tension strikes a revisable input, not
the framework's derived core. **Constructive path identified**: this
gives a *second, independent, quantified* motivation (alongside WP6's
own earlier $24$–$41\%$ Cassini-safe $\mu$-swap exposure finding) for
re-fitting cdot-7's interpolating function as a sharpness-parameterized
family with both $Q_2$ and the T22 Cassini bound in the likelihood.
**Recommendation for the author, not decided here**: consider promoting
this IF re-fit to the top of the post-cdot-8-WP7 revisit queue — this is
now the second external, already-ticking measurement clock this program
tracks (alongside KATRIN), and unlike KATRIN, the bound is already
published today.

**Sequencing decided (author, 2026-07-20)**: postponed until after WP7,
on the same logic as Gate 1(b)'s own deferral of the radiation-era
assumptions — see `proposal/DecisionGates-2026-07-18.md` Gate 3. The
finding itself stands unchanged; only the timing of any re-fit is
deferred, joining the post-WP7 revisit queue (`Progress.md` §4b).

---

## Priority summary for the consolidator

| Item | Priority | Action needed before merge |
|---|---|---|
| 1 — two-clock dictionary | **High** | Confirm Item 2 first, then merge the paragraph |
| 2 — age provenance | **Medium** | Bounded verification task, not yet a finding |
| 3 — census evolution equation | Low–Medium | Optional; ready to merge as-is if wanted |
| 4 — recurring pattern table | Low | Ready to merge as-is; pure bookkeeping |
| 5 — Etherington as standing tool | Low | Ready to merge as-is; one-line methodology note |
| 6 — item 9 re-examination | Low | **Not ready** — needs a fresh, cdot-7-native pass |
| 7 — $\Delta N_\text{eff}\approx-0.5$ marker | Medium | Gated on the queued $e^+e^-$/QCD kink calculation |
| 8 — §5.5 labeling bug | **High confidence, Medium priority** | Ready to merge; one-line relabel |
| 9 — $\hat a_0=\tfrac23\lambda c_0H_\tau$ identity + evidence-ledger note | Low–Medium | Ready to merge as-is |
| 10 — canonical $x_0$ value | Low | Ready to merge as-is; one line |
| 11 — verify-solution-first methodology | Medium | Ready to merge as-is; one line |
| 12 — $e^\pm$ true-equilibrium statistics | Medium–High | Ready; fold into Item 7's eventual script |
| 13 — entropy vs. energy for $(11/4)^{1/3}$ | Low–Medium | Ready to merge as-is; optional derivation |
| 14 — $\theta_*=r_s/D_p$ convention fix | **High** | Ready to merge; corrects historical cdot-4/5 error |
| 15 — "z=0 check" category-error caution | Medium | Ready to merge as-is; one line |
| 16 — $Q_2$/EFE tension with cdot-7's own fit | **HIGH severity, flagged concern, not an improvement** | **Requires author review — not a bounded merge task** |

**Consolidation batch delivered 2026-07-18** (Items 11–15), in response to the
advisor loop's repeated request across the WP5/WP6 rounds. None of these five
additions require cdot-8 to succeed or depend on AeST/census-closure machinery
surviving — Items 11, 15 are pure methodology; 12–13 are BBN physics facts usable by
any future cdot-7-native calculation; 14 directly corrects a historical cdot-4/cdot-5
methodology bug, independently of cdot-8's outcome. Combined with Items 1–10, none of
these fifteen items require cdot-8 to succeed, use AeST-specific content, or depend on
WP2/WP3's census/closure machinery — they stand on cdot-7's own terms (Items 1–2, 6–15)
or on this session's historical research alone (Items 4–5), with Item 3 the only one
genuinely mixed (derived using cdot-7's own definitions, discovered while building
cdot-8's covariant census). If cdot-8 is killed at any later work package, this log
should be handed to the consolidator unchanged. **cdot-8-internal bookkeeping (the K6
methodology-rule library, the full advisor/worker error tally, and jointly-verified
AeST-specific program results like the $\mu_\text{eff}$ dictionary) is deliberately
NOT included here** — those are AeST/cdot-8-specific and are tracked instead in
`cdot-8/proposal/ErrataAndMethodologyLog-2026-07-18.md`.
