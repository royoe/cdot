# Change Document — cdot-4 → cdot-5: Connectivity Counting Replaces Horizon Counting

**Date:** 2026-07-04
**Scope:** Replaces premise 2's occupancy-based horizon counting ($c\propto N\propto
R^n$, any exponent $n$) with **connectivity (reachability) counting**: an autocatalytic
law $dN/dR=N/L$, giving $c\propto e^{R/L}$ for a fixed length $L$, now understood as one
phase of a percolation transition (T23 — Autocatalytic Counting) with an occupancy
branch above a break redshift $z_*\approx1.2$. A relaxation of T14's connecton
conservation premise was tried and reverted (§3) — connectons remain conserved, as in
cdot-4. Affects: Core Principles (rewritten in full for cdot-5); every downstream topic
document is to be re-examined in turn (T1–T23 remain as cdot-4 left them; this document
and the new Core Principles are the first step of that re-examination, not its
completion).

**cdot-4 is closed and unchanged from this point on** (per the project's own rule:
"once a new stage has been created, the earlier ones should not be changed," README.md).
cdot-5 documents are written by copying the cdot-4 original, trimming what's now
obsolete, and pointing back to cdot-4 for anything worth preserving as history rather
than repeating in full.

---

## 1. Motivation: T23's Premise-Level Exclusion

cdot-4 closed (T23 — The Failed Tests) with a decisive, premise-level result: Core
Principles premises 1 (static geometry) + 2 (horizon counting, any exponent) + 4
(photon frequency conserved in flight), **taken together**, force a single function
$c(t)$ to fix both the observable redshift and the observable distance ruler at once
(the $D_H=dD_p/dz$ "lock"). DESI DR2's Alcock–Paczyński ratio shows no one-function
model of this kind can track the data's shape — not for the volume law ($\chi^2=93.9$,
zero free parameters), not for any other exponent (family-level best $\chi^2\approx35$,
still hopeless, and it requires $nP\approx10.5$ against $n=3,P=2$). T23's own closing
instruction: replace premise 2 with a structurally different mechanism, most likely one
with more than one independently-varying channel, while preserving the connecton
local-gravity program (T14/T22, separable and unaffected) and the redshift law's mass-
invariance derivation (T2/T4, likewise separable — $P=2$ does not depend on the
counting law's functional form, only on the mass-scaling exponent $s$).

## 2. The New Counting Law

`cdot-5/autocatalytic_counting/UPDATE_Autocatalytic_Counting_Law.md` (2026-07-04) fits
counting-law candidates directly to the clean DESI galaxy bins ($z<1.3$; QSO and Ly$\alpha$
excluded pending a decision on whether they need a second, high-$z$ component — see
Open Items below) and finds a single form selected over every power law tested:
$$D_p\propto\ln(1+z)\quad\Longleftrightarrow\quad c(R)\propto e^{R/L},$$
with $\chi^2=13.2/7$ (one free parameter, the length $L$) against eight data points —
competitive with two-parameter flat $\Lambda$CDM's $\chi^2=10.5/6$ on the same footing,
and decisively better than every power law tried ($n=3\to98$; $n=2\to178$; the family
gets *worse*, not better, as the exponent is lowered toward the values a naive
local-slope reading had suggested).

**A candidate derivation exists, conditional on three named assumptions** (network
supercriticality; the endpoint-only $1/L$ recruitment heuristic, reused from T12/T14 and
itself not yet derived from re-anchoring kinetics; mean-field independence at the
recruitment frontier). The mechanism: count *connectivity* (how many connectons the
local reference node currently reaches, transitively) rather than *occupancy* (particles
physically present in a growing volume). A new node joins the locally-reachable set only
if it links to a node already in that set, so the growth rate is proportional to the
current reachable count, not to the raw shell volume — $dN/dR=N/L$, autocatalytic,
$N\propto e^{R/L}$. This is explicitly the ontological shift T12 already prescribed for
what a connecton *is* (a unit of relation, not a particle) doing real quantitative work
for the first time, rather than remaining a philosophical reading.

**A sharp, falsifiable structural claim comes with it.** The law is exponential only if
$L$ is a *fixed* length. If recruitment instead scaled with a fixed *fraction* of the
horizon ($L\propto R$, scale-free), the same mechanism gives back a power law — the
excluded family. So DESI's preference for the exponential form is equivalent to: **the
connecton network recruits over a fixed length, not a fixed fraction of the horizon.**
This pins the open question precisely: what sets $L$? (Candidates on record: a
re-anchoring mean free path, T14's diffusive fraction; the Compton length of the
lightest massive species. Not the horizon itself — that would be scale-free and is
excluded.)

## 3. Relaxing Connecton Conservation — Tried, Failed, Reverted

An early cdot-5 draft relaxed T14's premise that connectons are "conserved — absorbed
and immediately re-emitted... with perfect conservation there is zero net energy
deposition," permitting a net sink. Motivation, from cdot-4 T23 §1.6: PBH mass fixed at
genesis acting as a permanent connecton sink (connectons, propagating at $c$, cannot
escape a horizon) had moved BAO fit quality in the right direction there
($\chi^2:93.9\to25$, though not sufficient alone).

**This was tested concretely in a follow-on cdot-5 session (`cz_inversion/`) and
failed.** "Fork A" — the conservation-preserving version, excluding BH-*confined mass*
from the count that sets $c$ while keeping connectons themselves conserved — was
checked against the real cosmic black-hole budget and **failed by 2–4 orders of
magnitude**: the population large enough to matter (PBHs, $\Omega_\text{PBH}\sim0.25$)
is genesis-formed and essentially constant over the BAO-relevant redshift range, while
the population that actually varies over that range (accretion-grown SMBHs) is a
$\sim10^{-5}$ sliver of the counted mass. Genuine sinks ("Fork B/C," dropping
conservation outright rather than just excluding confined mass from the count) were
considered and explicitly not pursued, since they collide with T12's photon-exclusion
argument and T14's conservation premise for no clear return once Fork A had failed.

**Connectons are conserved, exactly as in cdot-4** — this is reverted, not merely
re-flagged as uncertain. The resolution that actually improved the BAO fit
(`percolation_break/`, T23 — Autocatalytic Counting) needs no sink at all: it is a
percolation transition in the connecton network's *connectivity structure* as ordinary
continuous emission grows the network over time, fully compatible with strict
conservation of individual connectons. Core Principles §0 is edited back to assert full
conservation.

## 4. What Is and Isn't Touched

**Unaffected, carries forward unchanged:** premise 1 (static geometry); premise 3
(invariant $m$, $G$); premise 4 (photon frequency conserved in flight — a claim about
individual photons, distinct from connecton-population conservation); the squared
redshift law and $P=2$ (T2, depends on mass invariance, not on the counting law); the
atomic-frequency scaling $\nu\propto c^2$ (T1/Core §5a); the connecton local-gravity
program (T14/T22 — diffusion-sourced Newtonian gravity, the river derivation, the RAR
closure, $g_\dagger=c^2/R_0$-type identifications, though $R_0$'s definition itself may
need revisiting now that "the horizon" is no longer the counted quantity — flagged as an
open item, not yet checked).

**Directly touched, rewritten in Core Principles for cdot-5:** premise 2 (§1); the
horizon evolution law (§3) — now solved for $c(R)\propto e^{R/L}$, giving
$c(u)=L/(t_*-t)$, a finite-coordinate-time future "singularity" at $t_*$ that is
**resolved, not merely flagged**: counting clock cycles (proper time, $d\tau=(c/c_0)^2dt$)
forward from today, the elapsed proper time to reach $t_*$ diverges — a clock never
gets there. This mirrors the already-established past (genesis at $t\to-\infty$
coordinate but a finite proper time away) exactly: same integral, convergent tail one
way, divergent the other. In proper time — the only operationally meaningful clock —
the model has a finite past and an infinite future, cleaner than it first appeared, not
an unexplained liability; the distance formula (§4), now $D_p(z)=(L/2)\ln(1+z)$; the
observable Hubble law (§4a/§5) — $H_0^\text{obs}=2c_0/L$ (the $P=2$ relation
$H_0^\text{obs}=P\,H_0^\text{hor}$
survives unchanged, since it never depended on the counting law's functional form) and a
new, crisp, falsifiable signature, $H_\text{obs}(z)\propto(1+z)$ (linear — distinguishable
from both $\Lambda$CDM, steeper, and the old volume law, $\propto(1+z)^{7/6}$); the
proper age, now $\tau_\infty=L/c_0=2/H_0^\text{obs}\approx27.9$ Gyr ($H_0=70$) — **larger
than cdot-4's $21$ Gyr**, a new number that needs checking against every place cdot-4's
$21$ Gyr age was used as a consistency argument (T1, T20's white-dwarf population work
foremost).

**Flagged as changed but not yet re-derived — the deceleration parameter.** cdot-4's
Core Principles stated a firm, structural result: $q_0=1/(nP)>0$, "the model cannot mimic
apparent cosmic acceleration for any power-law horizon" (T4's whole framing leaned on
this). Expanding the new $D_L(z)=(1+z)(L/2)\ln(1+z)$ to second order in $z$ gives
$q_0=0$ — a **marginal, coasting case**, neither the old structural deceleration nor
genuine acceleration. This is a leading-order Taylor read, not a fit, and it removes one
of cdot-4's headline distinguishing claims against $\Lambda$CDM. A rough preview
comparison (below) suggests the new law tracks $\Lambda$CDM's distance modulus much more
closely than the old volume law did (max $|\Delta\mu|\approx0.23$ mag vs. up to $0.40$
mag), which — if it survives an actual Pantheon+ refit (T4's job, not done here) — would
soften or resolve T4's existing $\Delta\chi^2=+195$ SN tension. This is exactly the kind
of thing "examine each topic, check what needs adjusting" (the author's instruction) is
for; it is flagged here, not claimed.

| $z$ | $D_p$ (Mpc) | $D_L$ (Mpc) | $\tau_\text{lookback}$ (Gyr) | $\Delta\mu$ vs. $\Lambda$CDM |
|---:|---:|---:|---:|---:|
| 0.1 | 408 | 449 | 1.30 | $-0.05$ |
| 0.5 | 1737 | 2605 | 5.13 | $-0.18$ |
| 1.0 | 2969 | 5937 | 8.18 | $-0.23$ |
| 2.0 | 4705 | 14115 | 11.81 | $-0.21$ |
| 5.0 | 7674 | 46042 | 16.53 | $-0.03$ |
| 10.0 | 10270 | 112965 | 19.51 | $+0.18$ |

($H_0=70$, $L=2c_0/H_0\approx8.57$ Gpc; $\Lambda$CDM reference $\Omega_m=0.3$.)

## 5. Open Items Carried Into cdot-5

1. **What sets $L$?** **Reframed, not resolved (T23).** $L=R_*$, the network's
   correlation length at the moment of percolation — no longer a bare free scale, but
   attached to a physical transition. Deriving $R_*$ from the percolation condition
   $n_\text{node}\ell^3\sim1$ and the foam density evolution (T14) is the new gating
   task, replacing the old "what sets $L$" question with a narrower one.
2. **The endpoint-$1/L$ recruitment heuristic** — unchanged, still load-bearing, still
   not derived from re-anchoring kinetics.
3. **Network supercriticality** — unchanged; now specifically "supercriticality
   persists for $R>R_*$," per T23 item 3.
4. ~~**The high-$z$ (QSO/Ly$\alpha$) deferral.**~~ **Resolved in direction, not yet in
   derivation (T23).** The single-phase exponential law's high-$z$ failure is exactly
   the percolation break: above $z_*\approx1.2$ the network is subcritical and reverts
   to occupancy counting. The two-phase law fits all six DESI bins at
   $\chi^2/\text{dof}=0.85$. What remains open is deriving the subcritical index
   $q\approx1.37$ from branching statistics, and confirming $z_*$ against the full DESI
   covariance and DR3.
5. ~~The finite-future $t_*$.~~ **Resolved (2026-07-04, same day).** Counting clock
   cycles (proper time) forward from today, the elapsed proper time to reach $t_*$
   diverges — a clock never gets there. Mirrors the past exactly (same integral,
   opposite convergent/divergent tail). No physical endpoint; not a gating item. See
   Core Principles §3. (Unaffected by the percolation break — the future lies entirely
   in the post-percolation branch.)
6. ~~The connecton-sink mechanism.~~ **Retired — tested and reverted, not merely
   unreconciled.** See §3 above: Fork A failed by 2–4 orders of magnitude; genuine
   sinks were not pursued; connecton conservation is restored. The percolation
   mechanism needs no sink.
7. **$g_\dagger=c^2/R_0$ and every T14/T22 identification built on "$R_0$" as the
   horizon size.** **Reframed by the percolation break (T14 reconciliation, same
   session).** The particle horizon is finite again under the two-phase law
   ($D_p(\infty)\approx117\,r_d$, not the old $R_0=6c/H_0$) — the open question is no
   longer "does any finite length exist" but "which of three candidate finite lengths
   ($L$, $R_\text{now}$, $D_p(\infty)$) is the physically correct crossing/holographic
   scale," recomputed in T14's cdot-5 rewrite.
8. **The proper age (27.9 Gyr) and the $q_0=0$ marginal result** — still open, now
   additionally compounded by needing recomputation under the two-phase law rather
   than the single-phase one (T1/T3/T4's current cdot-5 tables predate the percolation
   break and have not been rechecked).

## 6. Procedure Going Forward

Per the author's instruction: cdot-4's documents are not to be edited further. cdot-5's
topic documents are produced by reading the matching cdot-4 document, determining what
survives unchanged (state it briefly, point back to cdot-4 for detail — do not repeat
cdot-4's full derivations), what needs adjustment (rework in cdot-5, citing what changed
and why), and what is now moot (name it, point back to cdot-4, do not carry the dead
material forward in full). Core Principles (this change) is the first document rewritten
under that rule; T1–T22 (and whatever replaces T23's role once cdot-5 has its own
results to report) follow next, topic by topic.
