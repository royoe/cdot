# Addendum — Fourth-Round Assessment: $C_1$ Is Not Gauge, and Three Minor Flags (for `cdot-8/WP3/`)

*2026-07-12. Addendum to
`Advisory-WP3-ExchangeTermWellPosedness-2026-07-12.md` (stand-in advisor), following
assessment of it and of `Update-WP3-ExchangeTermAttempt-2026-07-12.md` (worker).
Verdict of record: **both documents endorsed; the stand-in's central moves (A≡B
localization diagnosis, past-regularity boundary condition, integrated φ-equation,
forced $q(\mathcal N)$, no-external-functions completeness requirement) are correct
and its directives 1–7 remain in force.** Cheap cross-checks passed: the sign check
($g/(\dot c/c)=(p-\tfrac52)+3\kappa\lambda x$; $0.75$, $3.0$ reproduced),
$q\propto\mathcal N^{-10/9}$ ($9/4$ vs $5/2$), the three-faces-of-$9/10$ arithmetic,
the trivial integration of the φ-equation, and the localization/doubled-principle
literature characterization against held knowledge (paper-level verification still
required per the stand-in's own directive 6). The session log follows the Entry-9
rule (Entries 10–11, role-tagged, appended). This addendum supplies **one required
correction — flag 1 must be discharged before step 5 of the determination flow — and
three minor flags.** Derivations are spelled out for worker verification per
protocol.*

---

## Flag 1 (required before step 5) — $C_1$ is not gauge; it is the native dust mode, and it leaves step 5 a hidden knob

The stand-in's §4 folds the integration constant into "the standing additive-$CQ$
gauge caveat." The two ambiguities are different objects, and neither is as
innocent as the caveat's wording suggests.

**(a) What $C_1$ is.** The integrated φ-equation reads
$a^3F_Q=16\pi\tilde G\,\Lambda_M/N+C_1$. A constant contribution to $a^3F_Q$ is by
definition a **free-conserved shift current** — the solution of
$\tfrac{d}{dt}(a^3F_Q)=0$, i.e. precisely the amplitude of AeST's **native
dust-mimicking branch**, the component the proposal's §3 discards wholesale and the
invoice curve was computed without. $C_1\ne0$ is not a relabeling; it is
re-admitting, with adjustable amplitude, the very dark-matter mimicker whose
exclusion defines cdot-8.

**(b) Why it is physical (the degeneracy and where it breaks).** With $F$ fixed by
the quadrature and $Q(t)$ fixed by steps 1–2, the demanded current is
$a^3F_Q=kN$ with $k$ set by the invoice amplitude; the φ-equation then constrains
only the *combination* $16\pi\tilde G\,\Lambda_M/N+C_1=kN$. Any pair
$(\Lambda_M,C_1)$ on that line satisfies the scalar equation — but the pair is
**not** physically equivalent, because $\Lambda_M$ re-enters the lapse variation
on-shell:
$$S_{M5}=\int dt\,\Lambda_M\Big[\frac{\dot\phi}{N}-q(\mathcal N)\Big]
\ \Longrightarrow\
\frac{\delta S_{M5}}{\delta N}=-\Lambda_M\frac{\dot\phi}{N^2}=-\frac{\Lambda_MQ}{N}
\neq0\ \text{on-shell},$$
so different $C_1$ splits produce **different Friedmann constraints**. The
degeneracy of the φ-equation is broken at exactly step 5 — meaning the
confrontation, as currently specified, contains one adjustable constant. **The
zero-freedom claim does not survive unless $C_1$ is fixed by a stated principle
before step 5 is run.**

**(c) Candidate principles, in preference order — worker to determine which
applies, per the adopted-vs-derived discipline (K6):**
1. *Past regularity (derived, if it works):* determine the $C_1$ mode's behavior
   toward the eternal past on the census-closed background (a free dust current is
   subdominant to radiation in energy, so the divergence structure is not obvious
   in advance — this is a bounded computation, analogous to the
   $p_{\mathcal N}^\text{hom}$ check, and if the mode violates the eternal-past
   attractor structure, regularity forces $C_1=0$ and the constant is *derived*
   away, the project's preferred outcome).
2. *Census exhaustiveness (adopted, if 1 fails):* the Machian statement that the
   scalar sector carries **no unsourced current** — everything that gravitates is
   either counted ($\rho_\text{census}$) or determined by the count (the
   $\Lambda_M$-sourced piece). Philosophically native to the program, but if
   adopted rather than derived it must be flagged at point of introduction, per
   K6, and it joins premise 3's mechanism debt rather than the theorem list.

**(d) The $CQ$ caveat itself needs tightening while we are here.** For
$F\to F+CQ$: the energy density is untouched
($\Delta(F-QF_Q)=0$) and the piece has no $N$-dependence
($\Delta L=-\tfrac{C}{16\pi\tilde G}a^3\dot\phi$), so it drops from the Friedmann
constraint — *that* much of the caveat is right. But it is **not a total derivative
on FRW** ($\nabla_\mu A^\mu=3H\ne0$), it shifts $p_\phi$ by $CQ/8\pi\tilde G$, and
it shifts the current by $Ca^3$ — so it enters the razor's bookkeeping
($-\dot p_\phi$) and the $\Lambda_M$ determination (absorbable as
$\Delta\Lambda_M=Ca^3N/16\pi\tilde G$, time-dependent). **Directive:** treat
$(C,C_1,\Lambda_M)$ as a three-parameter family at step 5 and verify explicitly
that physical outputs (Friedmann constraint, total Bianchi closure) depend only on
the invariant combination — with $C$ expected to cancel identically between the
$F$-sector and $\Lambda_M$-sector contributions, and $C_1$ expected *not* to
(that is flag 1). If the $C$-cancellation fails, that is a finding about the
stress-energy extraction, not a nuisance — escalate it.

## Flag 2 (wording) — "the two radiation fixed points ($x=1.72,3.44$)"

Misnomer: $1.72$ is the *matter* fixed point. The computation itself is the right
one — the sign of the photon weight-drift term must be checked across the whole
$x$-range traversed, including the crossover where radiation weights coexist with
matter-era $x$ — so reword, don't redo: "$g>0$ for the radiation-weighted term at
both ends of the traversed range ($x=1.72$ matter, $3.44$ radiation)."

## Flag 3 (structural, cheap now, expensive later) — the census sector must be species-resolved in the action

The single-$p$ form $g(t)=(p-\tfrac52)\tfrac{\dot c}c+\tfrac{3c}{R_h}$ is a
per-species statement; the physical census is the three-component sum, with the
sweep term common and the weight-drift term species-specific
($p_\gamma=1$, $p_\text{cold}=\tfrac52$, and the neutrinos' $p_\nu(t)$ a smooth
interpolation from the FD census weight — machinery already in
`census_closure.py`). The §6 closure-over-dynamical-variables redo should therefore
be written species-resolved from the outset — either per-species pairs
$(\mathcal N_i,p_{\mathcal N_i})$ or the total with the weighted
$\bar g=\sum_i w_ig_i$ — because the era where the composition matters (the
crossover) is exactly where the stability/zero-crossing joint check runs. Retrofit
after the variation would mean redoing the variation.

## Flag 4 (reading caveat) — the determination "flow" is a coupled system

Steps 1–5 read as sequential; off the fixed point they are a self-consistent loop
($\mathcal N$'s evolution needs the background; the background is fixed at step 5).
Harmless on the fixed point, where the table is exact; on the fitted trajectory the
implementation should iterate (or solve simultaneously) rather than cascade, and
the convergence of that iteration is itself worth one line in the eventual
write-up.

---

**Net:** stand-in directives 1–7 in force; add: discharge flag 1(c) *before* the
step-5 confrontation and run the flag 1(d) invariance check *at* it; fold flags 2–4
into the §6 redo. Nothing here reopens the A-vs-B question — the resolution stands.

*Proposed location: `cdot-8/WP3/Addendum-FourthRound-C1NotGauge-2026-07-12.md`.*
