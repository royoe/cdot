# Static VSL Cosmology — Core Principles (cdot-5)

*Clean reference document. Contains the results that follow rigorously from the stated
premises. Disputed or unresolved derivations are tracked in the topic documents
(T1–T22 as inherited from cdot-4, re-examined one at a time for cdot-5). For the
motivation behind this iteration and a full accounting of what changed and why, see
`Change_Document_cdot4_to_cdot5.md` and, further back, `cdot-4/T23_The_Failed_Tests.md`.
cdot-4 is closed and unchanged; nothing here should be read as editing it.*

*What changed from cdot-4, in one paragraph: cdot-4's premise 2 — $c$ set by the
occupancy of a horizon growing into a uniform particle sea, $c\propto N\propto R^n$ for
some exponent $n$ — is excluded, for **every** exponent, by the DESI DR2 BAO
Alcock–Paczyński test (T23). The replacement counted here is **connectivity**, not
occupancy: $c$ tracks how much of the connecton network the local point currently
reaches, and that reach grows autocatalytically, $dN/dR=N/L$ for a fixed length $L$,
giving $c\propto e^{R/L}$. This single change is threaded through the sections below;
everything not tied to the counting law's functional form (mass invariance, $G$
invariance, the redshift mechanism itself, static geometry) is unchanged from cdot-4 and
stated briefly, with a pointer back rather than a re-derivation.*

---

## 0. The Relational Principle (foundational)

The model's premises are facets of a single relational (Machian) principle, unchanged
from cdot-4:

> **The global matter content of the universe sets the speed of light $c$; and $c$
> sets every energy, length, time, and coupling. Therefore all physical scales are
> referred to the cosmic matter content.**

What changes in cdot-5 is *how* the matter content is counted. cdot-4 counted
**occupancy** — particles physically present within a horizon of radius $R$, giving
$N\propto R^n$ for a horizon growing at $\dot R=c$. This is now excluded (T23). cdot-5
counts **connectivity** — not how many connectons occupy a volume, but how many the
local reference point currently *reaches* through the network of connections T14
describes. This is the ontological reading T12 already argued for on independent
grounds ("a connecton is not a field quantum but a conserved unit of relation between a
local degree of freedom and the cosmological horizon") now doing quantitative,
falsifiable work for the first time, rather than remaining a philosophical gloss on an
occupancy count that happened to use the same symbol $N$.

**Conservation laws — tested and restored.** An early cdot-5 draft relaxed connecton
conservation, permitting a net sink (motivated by cdot-4 T23 §1.6: a black hole cannot
be crossed by anything moving at $c$, so connectons falling into one are gone). This was
tried concretely — "Fork A" (BH-*confined mass* excluded from the count that sets $c$,
while connectons themselves stay conserved) was tested quantitatively against the
observed cosmic black-hole mass budget and **failed by 2–4 orders of magnitude**: the
population large enough to matter (PBHs, $\Omega_\text{PBH}\sim0.25$) is genesis-formed
and essentially time-constant over $0<z<2.3$, while the population that actually varies
over that range (accretion-grown SMBHs) is a $\sim10^{-5}$ sliver of the counted mass —
neither can supply the percent-level, redshift-varying degree of freedom the BAO shape
needs. Genuine connecton *sinks* (dropping conservation outright, rather than just
excluding confined mass from the count) were considered and explicitly not pursued, since
they collide with T12's photon-exclusion argument and T14's "conserved, never destroyed"
premise for no clear return. **Connectons are conserved, exactly as in cdot-4** —
absorbed and immediately re-emitted, zero net accumulation, no sink of either kind. The
resolution that actually works (T23 — see below) does not need one: it is a change in
the connecton *network's connectivity structure* (a percolation transition) as ordinary
continuous emission grows the network, not a change in whether individual connectons
are conserved.

The rest of §0's content — momentum and angular momentum conserved (space homogeneity,
isotropy), energy not conserved (time-translation broken by $c(t)$), and the reading
that this energy change is relational-to-$N$ rather than a disguised collisional
process — is unchanged from cdot-4 and not restated here; see cdot-4 Core Principles §0.

---

## 1. Foundational Premises

Four premises, as in cdot-4, with premise 2 replaced:

1. **Static geometry.** Unchanged from cdot-4: flat, absolute, static coordinate space,
   $\dot a=0$, $a(t)=1$. No recessional motion, no spatial curvature.

2. **Connectivity counting, in two phases** (replaces cdot-4's horizon/occupancy
   counting). The local speed of light is set by the connecton network's **reach**
   from the local point — how many connectons the local point is transitively
   connected to, not how many occupy the growing causal volume. This reach grows
   through a genuine **percolation transition**: at redshifts above a break $z_*$, the
   network is subcritical and reach grows the old occupancy way ($N\propto R^n$,
   volume-like); below $z_*$ (including the entire present and future), a spanning
   component has formed and reach grows autocatalytically,
   $$\frac{dN}{dR}=\frac{N}{L}\quad\Longrightarrow\quad N\propto e^{R/L},\qquad
   c\propto N,$$
   with $L$ fixed at the network's correlation length at the moment of percolation.
   **Full derivation, the percolation mechanism, the DESI fit ($z_*\approx1.2$), and
   everything else premise 2 now entails are in T23 — Autocatalytic Counting**, the
   dedicated home for this premise; this section states the headline only. (An
   earlier cdot-5 draft used the pure, single-phase exponential law with no break;
   T23 §0 records why the two-phase law replaced it and what changed as a result.)
   $L$ is a **fixed length**, not a fraction of $R$ — see T23 for why this distinction
   is the whole content of the connectivity phase, and for the three named assumptions
   the mechanism rests on (network supercriticality; the endpoint-only $1/L$
   recruitment rate, reused from T12/T14; mean-field independence at the recruitment
   frontier), none of which is derived from anything deeper yet.

3. **Invariant rest mass and $G$.** Unchanged from cdot-4: $m\propto c^0$, $G\propto c^0$,
   both local invariants. See cdot-4 T4 (mass), T8 ($G$; LLR-forced).

4. **Local quantization preservation.** Unchanged from cdot-4: $e$, $h$ strictly
   invariant; a photon in flight loses no energy, $\nu$ constant from emission to
   observation. (Distinct from the connecton-population statement in §0 above — this
   premise is about individual photons, not connectons, and is unaffected by anything
   in this section.)

---

## 2. Redshift Mechanics

**Unchanged from cdot-4 in full — this section does not depend on the counting law.**
The squared redshift law,
$$1+z=\left(\frac{c_\text{now}}{c_\text{emit}}\right)^2,$$
follows from EM-forced $\epsilon_0\propto c^{-1}$, invariant $e,h,m$, and the Rydberg
scaling $E_\text{Ryd}\propto c^2$ — none of which reference the counting law at all. The
general form $1+z=(c_\text{now}/c_\text{emit})^P$, $P=s+2$ ($s=0\Rightarrow P=2$), and
everything in cdot-4 Core §2, carries forward without change. See cdot-4 Core Principles
§2 for the full derivation.

---

## 3. Horizon Evolution Law

*This section gives the **post-percolation** ($z<z_*\approx1.2$) branch only — the
regime containing today, and everything in T1/T3/T4's current cdot-5 tables, which
were computed before the percolation break was identified and have **not yet been
rechecked against the two-phase law** (flagged as an open follow-up, not yet done).
For $z>z_*$ the network is subcritical and reach reverts to occupancy counting; that
branch is fit empirically in T23 but not yet derived from first principles. Because
today and the entire future lie at $z\le0<z_*$, the future-singularity analysis below
is entirely within the post-percolation branch and is unaffected by the break — only
statements reaching back past $z_*$ (the total age, T1; the high-$z$ tail of any
distance table, T3/T4) need the two-phase law and are currently provisional.*

The horizon still grows into the connecton network at the instantaneous light speed
(unchanged): $\dot R=c(t)$. What's new is $c$'s dependence on $R$:
$$c(R)=c_0\,e^{(R-R_\text{now})/L}.$$
Substituting into $\dot R=c$ and solving (let $u=t_\text{now}-t\ge0$ be lookback time,
as in cdot-4):
$$\boxed{\,c(u)=\frac{c_0}{1+c_0u/L}=\frac{L}{t_*-t}\,,\qquad
R(u)=R_\text{now}-L\ln\!\left(1+\frac{c_0u}{L}\right),}$$
where $t_*-t_\text{now}\equiv L/c_0$ is a finite future coordinate time.

**Two structural points, both now resolved and, read in proper time, symmetric:**
- **No finite origin in coordinate time.** $c\to0$ only as $u\to\infty$ ($R\to-\infty$):
  no Big Bang in map time. Unchanged from cdot-4 despite the different functional form.
- **A finite future coordinate time $t_*$ — resolved: it is a coordinate artifact, not a
  physical endpoint.** $t$ is not what any clock measures; proper time is (§5a,
  $d\tau=(c/c_0)^2dt$ — literally a clock-cycle count, ticks of a clock whose native
  frequency is $\nu\propto c^2$). Counting cycles forward from today: let $v\equiv t_*-t$
  (remaining coordinate time, $c=L/v$). The proper time elapsed reaching a future $v$ is
  $$\Delta\tau(v)=\int_v^{v_0}\left(\frac{c}{c_0}\right)^2dv'=\left(\frac{L}{c_0}\right)^2
  \left(\frac1v-\frac1{v_0}\right)\ \xrightarrow[v\to0^+]{}\ \infty,\qquad v_0\equiv\frac{L}{c_0}.$$
  **A clock never reaches $t_*$ — it ticks infinitely many times first.** This is the
  exact mirror of the already-established past: genesis sits at coordinate $t\to-\infty$
  but a finite proper time away (§4a, $\tau_\infty=L/c_0$); the future singularity sits
  at a finite coordinate $t_*$ but an *infinite* proper time away. Both come from the
  same integral, $\int(c/c_0)^2dt\sim\int dv^2/v'^2$: convergent toward $v'\to\infty$
  (the past tail), divergent toward $v'\to0$ (the future tail) — a property of the power,
  not a coincidence. **In every operationally meaningful (proper-time) sense, this model
  has a finite proper past (a real beginning) and an infinite proper future (no end is
  ever reached)** — a cleaner structure than it first appeared, not an unexplained
  liability. (Verified numerically as well as in closed form.)

$k$ (cdot-4's proportionality constant in $c=kR^3$) has no analogue here; the free
constant is now $L$ itself, fixed by one boundary condition ($c=c_0$ today) and one
data-driven scale (§4a).

---

## 4. Distance to a Source

Unchanged in *definition* from cdot-4 — space is static, so distance is still the
proper path length the photon traversed, $D=\int_{t_\text{emit}}^{t_\text{now}}c(t)\,dt
=R_\text{now}-R_\text{emit}$ — but the result is now a clean logarithm rather than a
shallow root. Using $c_\text{emit}/c_0=(1+z)^{-1/2}$ (§2, unchanged) in
$c(u)=c_0/(1+c_0u/L)$ gives $1+c_0u/L=(1+z)^{1/2}$, hence:
$$\boxed{\,D_p(z)=R_\text{now}-R_\text{emit}=L\ln\!\left[(1+z)^{1/2}\right]
=\frac{L}{2}\ln(1+z)\,.}$$
At $z=1$: $D_p=(L/2)\ln2\approx0.347\,L$ — compare cdot-4's $D_{z=1}=0.1091\,R_\text{now}$;
the two constants ($L$ here, $R_\text{now}$ there) are not the same quantity and the
numeric prefactors are not comparable directly.

**Angular-diameter distance.** cdot-4's late finding (T16/T4, 2026-07-03) — that the
borrowed Etherington relation $D_A=D_L/(1+z)^2$ does not apply to this model's
non-geodesic redshift mechanism, and that the physically correct construction in a
static Euclidean space is simply $D_A\equiv D_p$ (no $(1+z)$ suppression, since nothing
was ever closer) — is **adopted directly into cdot-5**, unaffected by the counting-law
change (the argument was about the redshift mechanism and the static geometry, not
about $c(R)$'s functional form). Use $D_A\equiv D_p$ throughout; do not reach for the
FRW-style reciprocity relation.

**Luminosity distance.** $D_L=(1+z)D_p$ — the clock-rate/photon-energy-bookkeeping
derivation (cdot-4 T4, "The Standard-Candle Assumption") is likewise independent of the
counting law and carries forward unchanged, using the new $D_p(z)$ above.

---

## 4a. Transformation Reference: Observables vs. Redshift

**The $P=2$ relation between the two Hubble constants survives unchanged**, because it
was never tied to the counting law's functional form — only to the mass-scaling
exponent $P=s+2$. Re-derived here for the new law to confirm this explicitly:
horizon rate $H_0^\text{hor}\equiv(\dot c/c)_0=c_0/L$; expanding $D_p(z)$ at low $z$
gives $H_0^\text{obs}=2c_0/L$, i.e.
$$\boxed{\,H_0^\text{obs}=2\,H_0^\text{hor}\,}\qquad\text{(same relation as cdot-4, }P=2\text{).}$$
So $L=2c_0/H_0^\text{obs}=c_0/H_0^\text{hor}$. Using $H_0^\text{obs}=70$ km/s/Mpc:
$L\approx8.57$ Gpc (compare cdot-4's $R_\text{now}=6c_0/H_0\approx25.7$ Gpc — a
different quantity playing a related role, not a rescaled version of the same number).

### Working formulae

$$D_p(z)=\frac{L}{2}\ln(1+z),\qquad D_H(z)\equiv\frac{dD_p}{dz}=\frac{L}{2(1+z)},$$
$$D_L=(1+z)D_p,\qquad D_A\equiv D_p\ \text{(§4)}.$$
$$\boxed{\,H_\text{obs}(z)\equiv\frac{c_0}{D_H(z)}\propto(1+z)\,}\quad\text{— linear, a
crisp new observable signature.}$$
This is directly distinguishable from both $\Lambda$CDM ($H(z)$ rises faster than
linear at moderate $z$) and cdot-4's volume law ($H_\text{obs}\propto(1+z)^{7/6}$) —
more BAO bins, or an independent $H(z)$ probe, could discriminate cleanly.

**Proper age.** $\tau_\infty=\int_0^\infty(c/c_0)^2\,du$ evaluates in closed form to
$$\boxed{\,\tau_\infty=\frac{L}{c_0}=\frac{2}{H_0^\text{obs}}\approx27.9\ \text{Gyr}\ (H_0=70)\,,}$$
**larger than cdot-4's $21$ Gyr** ($\tau_\infty=3/(2H_0)$ there). Still finite — the
finite-proper-age result survives structurally, but the number itself changed and needs
re-checking against every place cdot-4's $21$ Gyr was used as a consistency argument
(flagged in the Change Document; T1 and T20's territory for cdot-5).

### Comparison table ($H_0=70$) vs. flat $\Lambda$CDM ($\Omega_m=0.3,\Omega_\Lambda=0.7$)

Distances in Mpc, lookback proper time in Gyr. $\Delta\mu=5\log_{10}(D_L/D_L^{\Lambda\text{CDM}})$.

| $z$ | $c_e/c_0$ | $D_p$ | $D_L$ | $\tau_\text{lookback}$ (Gyr) | $D_L^{\Lambda\text{CDM}}$ | $\Delta\mu$ |
|------:|------:|------:|------:|------:|------:|------:|
| 0.1 | 0.954 | 408 | 449 | 1.30 | 460 | $-0.05$ |
| 0.5 | 0.816 | 1737 | 2605 | 5.13 | 2833 | $-0.18$ |
| 1.0 | 0.707 | 2969 | 5937 | 8.18 | 6608 | $-0.23$ |
| 2.0 | 0.577 | 4705 | 14115 | 11.81 | 15540 | $-0.21$ |
| 5.0 | 0.408 | 7674 | 46042 | 16.53 | 46652 | $-0.03$ |
| 10.0 | 0.301 | 10270 | 112965 | 19.51 | 103843 | $+0.18$ |

Compare cdot-4's version of this table ($\Delta\mu$ ranging to $-0.40$): the new law
tracks $\Lambda$CDM's luminosity distance markedly more closely. **This is a preview,
not a fit** — it does not by itself say anything about T4's Pantheon+ residual until the
actual fit is redone; flagged as the natural next check, not claimed as a result.

**Deceleration parameter — no longer a firm structural result.** cdot-4 stated
$q_0=1/(nP)>0$ as a firm, structural, model-wide claim ("cannot mimic apparent cosmic
acceleration for any power-law horizon"). Expanding the new $D_L(z)$ to second order in
$z$ gives $\boxed{q_0=0}$ — a **marginal, coasting case**, neither the old structural
deceleration nor genuine acceleration. This removes one of cdot-4's headline
distinguishing claims against $\Lambda$CDM and is a leading-order Taylor read, not a
fit; it needs to be checked properly (T4's job for cdot-5) before anything is asserted
about whether the model can or cannot mimic acceleration under the new law.

---

## 5. The Apparent Hubble Law

Low-$z$ behavior is unchanged in form from cdot-4 — $D_p(z)\approx(c_0/H_0^\text{obs})z$
recovers Hubble's law $v=H_0D$ for any smooth $D_p(z)$, by construction, regardless of
the counting law. The discriminating content is in the curvature ($q_0$, §4a) and in
$H_\text{obs}(z)$'s shape (§4a) — both changed, both flagged above. See cdot-4 Core §5
for the general low-$z$ argument, which carries forward unchanged.

---

## 5a. Atomic Frequency Scaling

**Unchanged from cdot-4.** $\nu\propto c^2$ under invariant mass, $\epsilon_0\propto c^{-1}$
(EM-forced) — this depends only on premises 3 and 4 and the electromagnetic argument of
§2, none of which reference the counting law. Governs $d\tau/dt=(c/c_0)^2$ as before
(used in §4a's age integral above), the stellar luminosity scaling, and everything else
cdot-4 Core §5a lists. See there for the derivation.

---

## 6. Stellar Flux and the Habitability Ratio

**Unchanged from cdot-4.** This sector depends on invariant $G$, static orbits ($r=$
const, T9), and T18's stellar-structure result ($L\propto c^0$) — none of it references
the cosmological counting law. $F\propto c^0$, $X\equiv T_\text{eq}/T_\text{mol}\propto
c^{-3/2}$, the $\sim30\%$ early-Earth warming result, all carry forward as in cdot-4.
See cdot-4 Core §6 and T18.

---

## 6a. Free-Particle Dynamics

**Unchanged from cdot-4.** Momentum conservation for free particles and angular-momentum
conservation for bound orbits (§0) are geometric/symmetry statements about the static
map, independent of the counting law. $u/c\propto(1+z)^{1/2}$ peculiar-velocity damping,
static orbit radii under invariant $G$ — all carry forward. See cdot-4 Core §6a and T11.

---

## 7. Status Summary

| Element | Status |
|---|---|
| Premise 1 (static geometry) | Unchanged from cdot-4. **Flagged (2026-07-05, T24): jointly with premises 3/4, this is the actual root of the CMB obstruction** — see the Premise 2 row below and T24 for the full diagnosis. |
| **Premise 2 (connectivity counting, two phases via a percolation transition)** | **Closed, 2026-07-05 — see `T24_The_Cosmological_Sector_Closed.md`.** This construction (and two further attempted repairs — see T24 Part I) is set aside: the percolation-broken law fit all six DESI bins at $\chi^2=6.8/8=0.85$, but its own microscopic mechanism was subsequently shown geometrically impossible, and every version tried (occupancy, autocatalytic, percolation-broken, hyperbolic-holographic) failed a downstream check. **The CMB failure that motivated the later attempts was traced to premises 1/3/4, not to premise 2** — no replacement counting law can fix it. T23 remains the detailed record of what was tried; not a live open item. |
| Premises 3, 4 (invariant $m,G$; quantization) | Unchanged from cdot-4 |
| Connecton conservation | **Tested and restored.** A "BH-confined mass" sink (Fork A) was tried and failed by 2–4 orders of magnitude against the observed BH mass budget; genuine connecton sinks (dropping conservation outright) were considered and not pursued. Connectons are conserved, exactly as in cdot-4 — the percolation resolution needs no sink. See T23 and T14. |
| Redshift $1+z=(c_\text{now}/c_\text{emit})^2$ | Unchanged from cdot-4 (T2) |
| Horizon law $c(u)=c_0/(1+c_0u/L)=L/(t_*-t)$ | **New, post-percolation branch only** (§3). No finite past (preserved from cdot-4); finite-future coordinate $t_*$ resolved as a coordinate artifact — infinite proper time to reach it (clock-cycle count diverges), so no physical endpoint. Pre-percolation ($z>z_*$) branch not yet in this document — see T23. |
| Distance $D_p(z)=(L/2)\ln(1+z)$ | **New, post-percolation branch only**, replacing cdot-4's $R_\text{now}[1-(1+z)^{-1/(nP)}]$; the full two-phase $D_p(z)$ (T23) has a **finite** $D_p(z\to\infty)$, unlike the single-phase law — T1/T3/T4's tables here still use the single-phase law and need rechecking (open) |
| $D_A\equiv D_p$ (no Etherington suppression) | Carried forward from cdot-4's late correction (T16/T4, 2026-07-03); unaffected by the counting-law change |
| $H_0^\text{obs}=2H_0^\text{hor}$ ($P=2$) | Unchanged in form from cdot-4; re-derived here for the new law, same relation |
| $H_\text{obs}(z)\propto(1+z)$ | **New, falsifiable signature** — was $\propto(1+z)^{7/6}$ in cdot-4 |
| Proper age $\tau_\infty=2/H_0^\text{obs}\approx27.9$ Gyr | **New number** (was $21$ Gyr); finiteness preserved; not yet cross-checked against T1/T20 |
| Deceleration $q_0=0$ | **Changed from cdot-4's firm $q_0=1/(nP)>0$.** Leading-order only; not yet fit; removes a headline cdot-4 claim |
| $L$'s value/origin | **Open.** One free scale, degenerate with the sound-horizon normalization exactly as $R_\text{now}/r_d$ was in cdot-4 — relocated, not removed |
| Network supercriticality | **Open, assumed not derived** — the mechanism requires it |
| Endpoint-$1/L$ recruitment rate | **Open** — reused from T12/T14's un-derived heuristic; now load-bearing for cosmology, not just local gravity |
| High-$z$ (QSO/Ly$\alpha$) fit | **Open, deferred** — the exponential law overshoots these excluded tracers; second component or running $L$, undecided |
| Connecton-sink mechanism | **Open** — named (T23 §1.6), not derived; relation to premise 2 undecided |
| Connecton local-gravity program (T14/T22) | **Unaffected, carries forward** — separable from the cosmological counting law per T23's own argument; $R_0$-based identifications ($g_\dagger=c^2/R_0$, etc.) flagged for a consistency check, not known to be broken |
| Everything else in cdot-4's status table not listed above (redshift–mass link, mass/$G$ invariance origins, RAR closure, disk flattening, white dwarfs, weak/strong-sector coupling, etc.) | Unchanged from cdot-4; not restated here — see cdot-4 Core Principles §7 |

**Why (unchanged from cdot-4, restated for cdot-5).** This is a project to see whether
VSL cosmology is viable as a rival to $\Lambda$CDM, treating it honestly — including
pursuing falsification attempts, not just consistency checks. cdot-4 found a
premise-level exclusion and closed honestly (T23). cdot-5 begins from the most
promising, best-fitting replacement found so far, with its own assumptions stated
up front and its own open items tracked from day one rather than discovered a year in.
