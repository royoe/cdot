# Session Log — 2026-07-10

*Running log for cdot-7 work, appended per-prompt, per this project's convention. A new
calendar date gets a new file; continues from `SessionLog-2026-07-07.md`.*

---

## Entry 1 — Opening the radiation-era question (2026-07-10, 09:5x CEST)

**Prompt (verbatim):**
> This iteration of the cdot project, cdot-7, has so far avoided the radiation dominated
> era in order to work on a premise of uniformity and tie the expanding horizon to the
> massive particles. If we were to take the step into earlier epochs, how would varying
> c and particle numbers work to drive changes in c? It would seem to me that if there
> are periods where certain particles dominates these would correspond to bursts in
> changing c and thereby possibly leave acoustic signatures.

**Summary:** Distinguished two mechanisms the question conflates: (1) background-history
"step" features — a species-domination transition changing the functional form of
whatever sources $c(t)$, producing a kink in $\dot c(t)$'s history, closely paralleling
standard cosmology's $g_*(T)$ steps (QCD transition, $e^+e^-$ annihilation, neutrino
decoupling) — real and tractable; (2) genuine acoustic oscillations (BAO), which need
density *perturbations* and a coupled photon-baryon fluid, not just a smooth background
— `Foundation.md` §6 item 6, explicitly gated and flagged by this project's own history
(cdot-4/cdot-5's decisive BAO failures) as its most dangerous territory. Noted premise 3
(Planck-unit invariance) means local particle-physics thresholds are exactly
standard-model-like in local units — reusable, not a hard part. Noted §6 item 9
("$n$ constant") is not merely unproven pre-BBN but *known false* once species undergo
freeze-out/annihilation. **New consideration, not yet on the ledger:** §2.2's fixed
point $x_*=g_h/a_0\approx1.7$ holds arbitrarily far into the past on the current
matter-only closure, because $a_0=\lambda\dot c$ is tied to the same self-similar
solution as $g_h$ — unlike standard cosmology, this framework does *not* automatically
simplify to deep-Newtonian Sciama early on; adding a radiation term with a different
$c$-scaling will likely break the pure-power-law ansatz that gives a fixed point at all,
meaning $x(t)$ would have to evolve through a radiation-dominated stretch rather than
sit still. Proposed opening item 5 (radiation-era closure) as a bounded next step,
explicitly keeping item 6 (actual acoustic peaks) out of scope.

**Status:** conceptual only; no files produced (this project's "inquisitive sessions
need not produce output" convention applied at this point). Author asked for a first
crack at item 5 itself, proceeding one step at a time — see Entry 2.

---

## Entry 2 — Step 1: coordinate-frame scaling of a radiation source term (2026-07-10, 10:0x CEST)

**Prompt (verbatim):**
> First crack, sure. Please proceed carefully one step at the time.

*(followed by, after the derivation below was presented:)* "Please record this as Step 1."

**Summary:** Derived the coordinate-frame scaling law needed to extend §2.1's
$M_h(t)$ with a radiation term.

**Step 1 derivation.** Matter's term is built from *conserved coordinate particle
number* $n$ times per-particle mass $m(t)\propto c^{1/2}$ (premise 3), giving
$\rho_m(t)\propto c^{1/2}$. For photons: extending premise 2's "number conserved"
logic symmetrically (a **new assumption**, not yet justified — see open question 1
below) gives conserved coordinate photon number density $n_\gamma$; combined with
§3.3's already-established per-photon coordinate energy law $E_\gamma(t)=\hbar kc(t)$
(from the conserved spatial wavenumber $k$, not conserved frequency), every photon
present at time $t$ has energy $\propto c(t)$ regardless of emission time, so
$$u_\gamma(t)=n_\gamma\langle\hbar k\rangle\,c(t)\ \propto\ c(t)^{+1},\qquad
\rho_\gamma^\text{eff}(t)\equiv u_\gamma(t)/c(t)^2\ \propto\ c(t)^{-1}.$$
This is the **opposite sign** from matter's $c^{+1/2}$: toward genesis ($c\to0$) matter's
contribution vanishes while radiation's diverges, so a crossover epoch — this
framework's own analog of $z_\text{eq}$ — must exist. This follows from premise 3 and
§3.3 alone; no AQUAL/deep-MOND machinery was needed to see it.

**Cross-check (independent route).** Built a general coordinate→local ("hatted")
dictionary from §3.1's own local length ($\propto c^{-3/2}$) and frequency
($\propto c^{5/2}$) scalings: a coordinate energy density $\propto c^p$ maps to a local
density $\propto c^{p-7}$. Applied to the radiation result ($p=1$): predicts
$\hat u_\gamma\propto c^{-6}\propto(1+z)^4$ — **exactly** ResearchNotes §10's
already-established result. Applied to matter's rest-mass-energy density
$\rho_mc^2\propto c^{5/2}$ ($p=5/2$): predicts $\hat\rho_m\propto(1+z)^3$ — not
previously stated anywhere in `Foundation.md`, but exactly the standard matter-dilution
law. Two independent hits on quantities not fitted to produce them; the scaling is
trusted on this basis, not merely asserted.

**Two open sub-questions, flagged rather than resolved, before this feeds the closure:**
1. Coordinate photon-number conservation is unforced — the radiation-era analog of item
   9, and likely to fail at exactly the transition epochs (pair annihilation, etc.) the
   opening question was pointing at. Recorded as a companion to item 9, not resolved.
2. The $u/c^2$ mass-equivalence prescription ignores pressure. A $w=1/3$ fluid sources
   gravity in GR via $\rho+3p/c^2=2u/c^2$ — twice the naive estimate, the same factor
   behind light bending being 2× the Newtonian value. Since this framework's local
   dynamics is explicitly Newtonian (§0), it is not obvious whether that GR factor
   belongs here at all. A real prefactor ambiguity, not a rounding detail — not yet
   decided.

**Status:** Step 1 of a multi-step attempt at `Foundation.md` §6 item 5. Not yet merged
into `Foundation.md`/`ResearchNotes.md` — no update document produced yet, pending
further steps (building the two-term closure; locating the crossover; checking what
happens to the AQUAL operating point $x(t)$ through the transition). Recorded here per
author's explicit request, ahead of the session's natural conclusion.

---

## Entry 3 — Step 2: the extended closure, two fixed points, and the crossover (2026-07-10, 10:1x CEST)

**Prompt (verbatim):** *(continuing without further author prompt, per Entry 2's
proposal)* — presented, then confirmed by "Yes." at the top of Entry 4.

**Summary.** Extended §2.2's dynamical system to $x=\mu^{-1}\!\left(\frac{R_h^2}
{B_m^2c^{3/2}}+\frac{R_h^2}{B_\gamma^2c^3}\right)$ — a sum of two differently-scaling
terms, so the existing $x=$const solution can only be an asymptote. Re-derived the
matter-only fixed point's own method for a general source $\rho\propto c^n$: kinematics
force $R_h\propto c^{1-n/2}$ and pin $x_*=(1-n/2)/(\kappa\lambda)$, independent of
$\mu$'s functional form. Matter ($n=\tfrac12$) reproduces Foundation's $x_*=3/(4\kappa
\lambda)\approx1.72$ exactly (validation). Radiation ($n=-1$, from Step 1) gives a
**second, clean fixed point** $x_*^{(\text{rad})}=3/(2\kappa\lambda)\approx3.45$ —
exactly double, also $\mu$-independent. Located the crossover: $1+z_\text{eq}=\rho_0/
\rho_\gamma^\text{eff}(t_0)$, a closed form using only already-fitted quantities.
Computed numerically across the three standing $\Omega_\text{closure}$ conventions
(§6 item 1 / ResearchNotes §13) and both $\eta$ options from Step 1: $z_\text{eq}\in
[730,2660]$ — systematically below standard cosmology's $\approx3400$, as expected
since $\Omega_\text{closure}\ll\Omega_m^{\Lambda\text{CDM}}$ by design. Flagged the
sharper point: depending on which $(\eta,\Omega_\text{closure})$ combination, $z_\text{eq}$
can land on either side of $z_\text{recomb}\approx1100$ (fixed independently, by the
known local recombination temperature) — a live, consequential ambiguity, not a
rounding detail.

**Status:** Step 2 of the item-5 attempt. Not yet merged. Author confirmed ("Yes.") and
asked whether to proceed to Step 3 (numerical integration through the crossover) or
pause on the $\eta$/convention ambiguity — resolved by doing Step 3 first, using the
integration itself to sharpen the ambiguity's consequences rather than resolve it in
the abstract.

---

## Entry 4 — Step 3: numerically integrating the trajectory through the crossover (2026-07-10, 10:2x CEST)

**Prompt (verbatim):**
> Yes.

**Summary.** Recast the two-term closure as a single ODE in $r(s)\equiv R_h/R_{h,0}$
with $s\equiv\ln(c/c_0)$: $dr/ds=\kappa\lambda\,x(r,s)\,r$, $x=\mu^{-1}(y)$,
$y=r^2[Y_me^{-3s/2}+Y_\gamma e^{-3s}]$, with $Y_m,Y_\gamma$ fixed by today's actual
operating point ($x_0=1.10$) and the density ratios from Step 2. Integrated backward
from today ($s=0$) to $s=-10$ ($z\sim10^6$) using `scipy.integrate.solve_ivp`
(`rtol=1e-9`), for all four $(\eta,\Omega_\text{closure})$ combinations. Result: $x(z)$
**recovers to the matter fixed point ($1.72$) by $z\sim10$** — numerically confirming
§2.2's "negligible in the past" instability claim — holds near $1.72$–$2.0$ out to
$z\sim400$, then rises smoothly (**2–3 e-folds in $z$**, not a sudden jump) through the
crossover, and **settles at the radiation fixed point ($3.45$) by $z\sim10^5$–$10^6$**,
matching Step 2's prediction exactly in every case. Sharper finding than Step 2's static
crossover alone: $x(z_\text{recomb}{=}1100)\in[2.15,2.67]$ across **all four**
combinations tried — recombination sits inside the transition in every case, and the
AQUAL operating point there is substantially (25–55%) above the matter-only value
regardless of how the $\eta$/convention ambiguity resolves. Reframed the original
question's "burst" as a real, quantified, ~2–3-e-fold-wide kink, not a discontinuity.

**Status:** Step 3 of the item-5 attempt. Not yet merged. Flagged as a two-fluid
(matter+radiation) picture only — resolving multiple species in sequence (the
original question's "particle domination bursts") would need further terms. Author
asked to investigate the $\eta$ prefactor (Step 1's open question 2) before deciding
between that multi-species extension and other directions.

---

## Entry 5 — Step 4: resolving the $\eta$ prefactor (2026-07-10, 10:3x CEST)

**Prompt (verbatim):**
> Take time to investigate eta first?

**Summary.** Investigated whether $\eta=1$ (naive $u/c^2$) or $\eta=2$ (GR's
$\rho+3p/c^2$ for $w=1/3$) is the right radiation-sourcing prefactor, rather than
picking one. Traced the $\eta=2$ factor to its origin: it is a genuine feature of *GR's
field equations* responding to the full stress-energy tensor (appearing already in
GR's own weak-field/Tolman-mass limit, not only in the Friedmann acceleration
equation) — not something AQUAL's literal, non-relativistic Poisson equation
($\nabla^2\Phi=4\pi G\rho$ in the $\mu\to1$ limit, mass density only, no pressure term)
has any structure to express. Concluded $\eta=1$ is not merely the conservative
default but **the only value actually licensed by what premise 4 says as written** —
$\eta=2$ would import GR's relativistic completion (§6 item 7, explicitly deferred)
without having built it. Checked whether an internal conservation law (analogous to
the Bianchi-identity origin of $\rho+3p/c^2$ in standard cosmology) could force a
value instead of relying on a scope argument: no — that mechanism relies on an
expanding volume doing work against pressure, which has no analog under premise 1's
static space, and the matter sector isn't "energy conserving" in the naive sense
either ($m(t)\propto c^{1/2}$ already grows rest energy over time), so there is no
internal principle here to appeal to. **Adopted $\eta=1$ as the working choice**,
explicitly flagged as scope-consistent rather than derived, to be revisited if/when
item 7 is tackled. Consequence for Step 3's numbers: $x(z_\text{recomb})\in[2.15,2.49]$
under $\eta=1$ alone (vs. $[2.15,2.67]$ across both $\eta$ options) — same qualitative
conclusion, tighter spread.

**Status:** Step 4 of the item-5 attempt; resolves Step 1's open question 2. Open
question 1 (coordinate photon-number conservation) still stands. Not yet merged — this
entry and Entries 2–4 together are now substantial enough to warrant a consolidated
update document once the author decides how much further to take this before
concluding the session.

---

## Entry 6 — Step 5: multi-species (2026-07-10, 10:4x CEST)

**Prompt (verbatim):**
> Try the multi species first, then write up for review/update.

**Summary.** Investigated whether additional species (neutrinos, $e^+e^-$, beyond)
produce further kinks, as the opening question anticipated. **Neutrinos:** if treated
as always-relativistic, only rescale $\rho_{\gamma,0}$ by the standard $1+\tfrac78
N_\text{eff}(4/11)^{4/3}\approx1.69$ — no new structure. But using this project's own
fitted mass (§5.6, $\Sigma m_\nu=1.374$ eV, three quasi-degenerate), the
relativistic$\to$non-relativistic transition happens at $1+z_{\nu,\text{nr}}\approx
2733$ (using $\hat T_{\nu,0}=(4/11)^{1/3}\hat T_{\gamma,0}\approx1.945$ K and
$m_\nu=0.458$ eV per species) — landing at the top edge of Step 2/3's own $z_\text{eq}$
range ($730$–$2660$). **A previously unnoticed connection between §5.6's mass-census
resolution and this session's radiation closure**: the same neutrinos closing the
mass budget are dynamically active almost exactly at the matter-radiation crossover.
Flagged as requiring a genuine third (mass-threshold) term, not yet built — the
finding is real, the fix is not attempted here. **$e^+e^-$ annihilation:** standard
entropy-transfer bookkeeping gives a real kink, $u_\gamma$ boosted by
$(11/4)^{4/3}\approx3.85\times$ relative to naive pre-transition extrapolation, at
$1+z\approx2.2\times10^9$ — confirmed that Step 1's coordinate law needs **no
correction anywhere already computed** (recombination through $z\sim10^6$), since it
only breaks down past this much deeper epoch. QCD transition and earlier: real,
deeper still, explicitly not attempted. Reiterated the standing caveat: all of this is
background-history structure (kinks in a smooth trajectory), not acoustic oscillation
— item 6 remains untouched.

**Status:** Step 5 of the item-5 attempt — order-of-magnitude/estimate-level, not
derived to the rigor of Steps 1–4; the neutrino-mass coincidence is the one finding
here judged solid enough to flag as a first-class open item rather than a footnote.
Author asked for the write-up; consolidated update document and finalized session log
follow in this entry's files.

**Files produced:** `Update-RadiationEraClosure-2026-07-10.md` (proposed
`Foundation.md`/`ResearchNotes.md` changes, Steps 1–5), `radiation_closure.py`
(archived derivation/numerics, independently re-runnable), this log.

---
