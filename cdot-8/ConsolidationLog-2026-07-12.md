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

None of these seven items require cdot-8 to succeed, use AeST-specific content, or
depend on WP2/WP3's census/closure machinery — they stand on cdot-7's own terms (Items
1–2, 6–7) or on this session's historical research alone (Items 4–5), with Item 3 the
only one genuinely mixed (derived using cdot-7's own definitions, discovered while
building cdot-8's covariant census). If cdot-8 is killed at any later work package,
this log should be handed to the consolidator unchanged.
