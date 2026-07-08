# Update — Aligning AQUAL with the Invariance Principle: $a_0=\lambda\dot c$, the Breached-Invariance Portal, and a Premise 2 / Premise 4 Inconsistency (Toward the $\Lambda$-Analog)

*Status: update document for cross-check and merge. Responds to the author's request
for an assessment of how the Planck-unit invariance principle
(`Update-ChandrasekharCandle-2026-07-07.md`) and the corrected photon sector
(`Update-PhotonSector-2026-07-07.md`) best align with premise 4's AQUAL sector.
Proposes: a sharpened, epoch-dependent premise 4; a new falsifiable prediction
($g_\dagger(z)$ evolution); a caveat to §5.1's exactness claim; and identifies an
internal inconsistency between premises 2 and 4 whose repair is the leading
$\Lambda$-analog candidate. Produced 2026-07-07 (cdot-7, session entry 6).*

---

## 1. An Identity Hiding in Premise 4: $a_0=\lambda\,\dot c$

Foundation §4 sets $a_0\equiv\lambda c_0H_0^\text{hor}$, and §2.2 defines
$H_0^\text{hor}\equiv(\dot c/c)|_{t_0}$. Composing the two:
$$a_0=\lambda\,c_0\cdot\frac{\dot c}{c}\Big|_{t_0}=\lambda\,\dot c(t_0).$$
**The MOND acceleration scale is, up to $\lambda$, the acceleration of the speed of
light itself.** Premise 4 already asserts — without having noticed — that Newtonian
gravity fails precisely where gravitational accelerations fall below the rate at which
$c$ is changing: below that threshold, local dynamics cannot "keep up" with the
cosmological drift. Numerically, $\dot c(t_0)=c_0H_0^\text{hor}\approx4.5\times10^{-10}
\,\text{m/s}^2$ and the empirical $a_0\approx1.2\times10^{-10}\,\text{m/s}^2$ gives
$\lambda\approx0.26$ (values per the photon-sector update). We note without leaning on
it that $\lambda=\tfrac{3}{2}\cdot\tfrac{1}{2\pi}\approx0.24$ — i.e.
$a_0\approx c_0H_0^\text{obs}/2\pi$, the long-standing MOND numerology — sits within
$\sim10\%$; recorded as numerology, not a result.

**Proposed sharpening of premise 4: make $a_0$ epoch-dependent,**
$$a_0(t)=\lambda\,\dot c(t)\;\propto\;c(t)^{5/4}.$$
Foundation §4 as written freezes $a_0$ at today's value, which makes the present epoch
special — un-Machian on its face. The dynamical reading is also *required* for the
EdS correspondence (photon-sector update §7) to extend to the AQUAL sector: in local
units (acceleration unit $\propto c^{7/2}$),
$$\hat a_0(z)=\hat a_0(0)\,(c_z/c_0)^{5/4-7/2}=\hat a_0(0)\,(1+z)^{3/2},$$
which is exactly $c\,H_\text{EdS}(z)$ with $H_\text{EdS}(z)=H_0(1+z)^{3/2}$ — the
$a_0\sim cH(z)$ relation transported to the corresponding expanding description. The
frozen reading breaks this correspondence and has no Machian motivation; the dynamical
reading is adopted here.

---

## 2. AQUAL as the Unique Sanctioned Breach of Planck-Unit Invariance

The invariance principle (Chandrasekhar update §3) governs *local couplings*. $a_0$ is
not a local coupling: it is cosmological data ($\dot c$) imported into local dynamics.
The aligned statement of the whole framework is therefore:

> **Local physics is Planck-unit invariant, except through a single portal: the
> acceleration scale $\dot c(t)$ entering AQUAL's interpolating function.**

This is consistent with, and completes, the localization result of the Chandrasekhar
update: all of the framework's distinguishable physics flows through this one portal.
Three consequences:

**2.1 A falsifiable prediction: the RAR scale evolves.** In local units — which is what
galaxy dynamics at epoch $z$ compares against —
$$g_\dagger(z)=g_\dagger(0)\,(1+z)^{3/2},$$
so MOND effects were *stronger* in the past: at fixed baryonic mass,
$v_\text{flat}\propto\hat a_0^{1/4}$ gives rotation velocities enhanced by
$(1+z)^{3/8}$ ($\approx30\%$ at $z=1$). This is the framework's most distinctive
near-term test. Status flagged, not resolved: high-$z$ rotation-curve data are murky
(reported *declining* outer curves at $z\sim1$–$2.5$ probe baryon-dominated,
high-acceleration regions; RAR-evolution analyses disagree) — logged as a new
data-comparison open item rather than claimed as a pass or fail. Note also the
qualitative early-universe implication: $\hat a_0\to\infty$ toward genesis, so early
local dynamics is entirely deep-MOND — relevant to any future structure-formation
sector, out of scope here.

**2.2 The lockstep breaks in deep MOND — epoch-invariance is a high-acceleration
privilege.** Adiabatic evolution of a deep-MOND circular orbit
($v=(GMa_0)^{1/4}$, $L=mvr$ conserved) with $m\propto c^{1/2}$, $GM\propto c^{1/2}$,
$a_0\propto c^{5/4}$ gives $v\propto c^{7/16}$ and $r\propto c^{-15/16}$ — *not* the
Newtonian/atomic $r\propto c^{-3/2}$, $v\propto c$. In local units, deep-MOND orbits
slowly expand and slow down: $\hat r\propto c^{9/16}$, $\hat v\propto c^{-9/16}$
(equivalently $\hat v\propto(1+z)^{3/8}$ into the past, consistent with 2.1, as it must
be). Drift rates are $O(H)$ — utterly unobservable directly (a $10^4$ AU wide binary
drifts by tens of metres per year) — but this corrects §5.4/§6.2's reframing: the
statement "the shrinkage is locally unobservable in principle" is a theorem of the
*Newtonian* ($\mu=1$) sector only. Deep-MOND systems are the exception that carries
the portal's signature; its practical observable remains the $z$-evolution of 2.1.

**2.3 Conservation-law hygiene holds.** AQUAL's field equation is elliptic
(instantaneous), so it composes cleanly with premise 1's absolute time and an
adiabatically drifting background; spatial homogeneity preserves momentum conservation;
explicit time dependence of $a_0(t)$ and $m(t)$ in the Lagrangian makes energy
non-conserved at $O(H)$, exactly as in any time-dependent background (and exactly as
the photon sector already does). The place where alignment genuinely strains is the
relativistic completion (item 4), where varying-$c$ photons must couple to the AQUAL
field — deferred, as before.

---

## 3. The Inconsistency: Premise 2 Computes in a Regime Premise 4 Forbids

The Sciama closure's binding acceleration at the horizon is
$$g_h=\frac{c^2}{R_h}=\frac{3}{4}\,\dot c
\qquad\Longrightarrow\qquad
x_h\equiv\frac{g_h}{a_0}=\frac{3}{4\lambda}\approx2.9\ \ (\lambda\approx0.26),$$
using $c_0/R_{h,0}=3/\tau$ and $H_0^\text{hor}=4/\tau$ (photon-sector update §4).
**The cosmological closure operates squarely in AQUAL's transition regime** — yet
premise 2 evaluates the Machian binding with pure Newtonian gravity, which premise 4
declares invalid at $x\sim1$. As currently written, premises 2 and 4 contradict each
other at the closure's own operating point. This is the alignment question's sharpest
answer: the two sectors are not yet consistent, and repairing that is not optional.

**Why the repair is an opportunity, not just hygiene.** Rebuilding the closure with the
AQUAL-corrected potential does two things at once:

1. **It is the leading $\Lambda$-analog candidate.** The photon-sector update (§5.4)
   proved that no closure of pure power-law form $R_h\propto c^{p}$ can produce
   $q_0<0$; escape requires a non-power-law term in the closure ODE. The MOND-corrected
   potential supplies exactly that: in the deep/transition regime the potential of an
   enclosed mass goes as $\sqrt{GM_ha_0}\,\ln R$ rather than $GM_h/R$, so the Machian
   relation gains a term with structurally different $R_h$- and $c$-dependence —
   the same *kind* of modification that $\Lambda$ makes to the Friedmann equation. If
   the framework's two "dark" phenomena (MOND and apparent acceleration) both come from
   the single portal $\dot c$, the empirical numerology
   $a_0\approx\tfrac{c}{2\pi}\sqrt{\Lambda/3}$ would stop being a coincidence.
2. **It could derive $\lambda$.** With $a_0=\lambda\dot c$, the closure that determines
   $\dot c$ now *contains* $a_0$: closure and MOND scale become one self-consistency
   problem, with $x_h=3/(4\lambda)$ sitting at the transition where $\mu$'s form
   matters. A consistent solution would fix $\lambda$ (given $\mu$), clearing the last
   piece of open item 1 alongside the $\Lambda$-analog. Conversely, failure to find a
   consistent solution would falsify the $a_0$–closure link — either way, decisive.

This construction — solve
$\;c^2\propto\Phi_\text{AQUAL}[M_h,R_h;a_0=\lambda\dot c]$ self-consistently with
$\dot R_h=c$ and premise 3 — is proposed as the next building session. It requires
committing to a $\mu$ (or carrying a family), which is why §4 below matters first.

---

## 4. $\mu(x)$ Is Now Squeezed from Both Ends (Items 3/6 Become Data-Driven)

- **High $x$ (solar system / LLR):** Foundation §5.1's "exact at every epoch" claim is
  a theorem of the $\mu=1$ sector only. At lunar accelerations $x\sim10^{7}$, simple
  interpolating functions ($\mu=x/(1+x)$) leave relative residuals $\sim1/x\sim
  10^{-7}$, within reach of LLR-class precision; exponentially saturating families
  ($1-\mu\sim e^{-\sqrt x}$-type) do not. Proposed merge: add this caveat to §5.1, and
  let LLR/solar-system data select the high-$x$ asymptotics — consistent with existing
  solar-system MOND constraints.
- **Low/transition $x$ (galaxies *and now cosmology*):** the RAR fixes $\mu$ near
  $x\sim1$ as before — but §3 adds a second, independent probe at the *same* $x$: the
  closure's own operating point $x_h\approx3/(4\lambda)$. The same function fitted to
  galaxies gets tested by the expansion history. Items 3/6 thereby stop being aesthetic
  choices and become doubly constrained.

---

## 5. Proposed Merges

- **Foundation §4:** rewrite around $a_0(t)=\lambda\dot c(t)$ (the identity of §1, the
  epoch-dependence, and the portal framing of §2); record the frozen-$a_0$ reading as
  considered and rejected (un-Machian; breaks the EdS correspondence).
- **Foundation §5.1:** add the $\mu$-sector caveat (§4 above); "exact" applies to the
  Newtonian sector, with high-$x$ residuals constraining $\mu$.
- **Foundation §5.4/§6.2-reframed (per photon-sector update):** amend — local
  unobservability of the lockstep is a $\mu=1$ theorem; deep-MOND systems drift
  ($\hat r\propto c^{9/16}$), observable only as $g_\dagger(z)$ evolution.
- **Foundation §5.5 (flux/luminosity, per prior updates):** add the prediction
  $g_\dagger(z)=g_\dagger(0)(1+z)^{3/2}$ and its hedged observational status.
- **Foundation §6:** replace the $\Lambda$-analog item (photon-sector update, item 2's
  successor) with the concrete program of §3: *rebuild the Sciama closure with the
  AQUAL-corrected potential, self-consistently with $a_0=\lambda\dot c$; targets:
  $q_0<0$, age $\gtrsim13$ Gyr, derived $\lambda$.* Add a new data item: compare
  $g_\dagger(z)\propto(1+z)^{3/2}$ against high-$z$ rotation-curve/RAR literature.
  Note items 3/6's new double constraint. Record the premise 2/4 inconsistency as
  standing until the rebuild lands.
- **ResearchNotes:** record §1's identity, §2.2's broken-lockstep derivation, and §3's
  $x_h$ computation as the session's derivation trail.

---

## 6. Honest Ledger

Gained: premise 4 acquires a Machian identity ($a_0=\lambda\dot c$) and an
epoch-dependent form demanded by the correspondence; the framework's single falsifiable
portal is now explicit, with a concrete new prediction ($g_\dagger\propto(1+z)^{3/2}$);
$\mu$ becomes doubly data-constrained; and the $\Lambda$-analog debt acquires its first
credible candidate mechanism — one that would also derive $\lambda$. Cost: a new
*acknowledged internal inconsistency* (premises 2 and 4 disagree at the closure's own
operating point $x_h\approx3$) that did not appear on any prior open-items list —
though it was always present, unnoticed, and the framework is better for having it on
the books. §5.1's "exact" claim is honestly demoted to sector-exact. Nothing in this
update yet fixes the SN Ia conflict or the age; it identifies where the fix must come
from and what solving it would buy.
