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
