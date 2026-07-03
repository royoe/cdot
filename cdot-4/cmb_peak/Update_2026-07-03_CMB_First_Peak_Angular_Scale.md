# Update — The First Acoustic Peak's Angular Scale Is Geometrically Unreachable (2026-07-03)

*Session type: destructive / falsification-relevant. T16 open question: "Can the
self-similar baryon-photon plasma (first peak) be computed numerically in the model's
$c(t)$ background? Is the predicted peak position consistent with $\ell_1\approx220$?"
**Answer: no, by a wide and robust margin.** Using only formulas already adopted as
"Core, stable" (the $D_p(z)$/$D_A(z)$ distance relations, verified against Core's own
worked table) plus T16(C)'s own self-similarity argument for the sound speed, the
model's predicted sound-horizon angular scale $\theta_s$ has a floor that observed
$\ell_1\approx220$ cannot get under — by 9$\times$ to 765$\times$ depending on premise-2
branch, and the shortfall survives even granting the model total freedom over the
unresolved recombination redshift $z_\text{rec}$ (T16 item A). A secondary, independent
problem is found in the baryon-loading parameter itself. This substantially sharpens
T16(C)'s claim from "translates, promising, first peak needs no dark matter" to
"the geometry as currently formulated cannot place a peak anywhere near $\ell\sim220$,
regardless of baryon content or recombination epoch."*

---

## 1. What Was Computed

T16(C) argues the plasma physics of the first peak is self-similar and "translates
directly" because $R \equiv 3\rho_b/(4\rho_\gamma)$ is invariant across epochs (both
densities $\propto c^2$). That is a claim about the *shape* of the oscillator. It says
nothing yet about *where* the resulting peak lands in $\ell$-space — that requires the
model's own distance geometry. This update supplies that missing half of the
calculation.

**The standard relation** (model-independent, a consequence of flat spatial geometry
and the definition of angular diameter distance, which the model already adopts via the
Etherington relation, Core §4a): the angular scale of a physical length $r_s$ at the
last-scattering surface is $\theta_s = r_s/D_A(z_\text{rec})$, and the first peak sits
near $\ell_1 \approx \pi/\theta_s$.

**Inputs used, all already in the repository, none invented for this calculation:**
- $D_p(z) = R_\text{now}\left[1-(1+z)^{-1/(nP)}\right]$, $D_A(z)=D_p(z)/(1+z)$
  (Core §4/§4a; general form with horizon-law exponent $n$ and redshift power $P$).
  **Verified against Core's own comparison table**: this reproduces
  $D_p(z{=}1)=2804$ Mpc exactly for $n=3,P=2$.
- $R_\text{now} = 6c_0/H_0^\text{obs} \approx 25{,}700$ Mpc (Core §3/T3, $H_0=70$).
- The sound horizon, using $c_s/c$ constant (T16(C)'s self-similarity result):
  $r_s = (c_s/c)\times R_\text{rec}$, where $R_\text{rec}=R_\text{now}(1+z_\text{rec})^{-1/(nP)}$
  is the *same* bookkeeping variable used in $D_p(z)$ — the sound horizon is the proper
  distance sound has travelled from genesis ($R=0$, $t\to-\infty$, Core §3) to
  recombination, exactly analogous to how $D_p$ is the proper distance light has
  travelled from emission to now.

## 2. The Baryon-Loading Value $R$ Is Not Small

Before computing $\theta_s$, the constant $R$ needs a number, not just an invariance
claim. Self-similarity says $R$ equals its value at *any* epoch — including today. Using
today's directly measured, model-independent quantities ($\Omega_b h^2 = 0.0224$,
$T_0=2.725$ K, i.e. real baryon and photon number/energy densities, not a
$\Lambda$CDM-fit parameter):
$$R = \frac{3\rho_b}{4\rho_\gamma}\bigg|_\text{today} \approx 680.$$

**This is not a small number.** In $\Lambda$CDM, $R$ falls from this same $\approx680$
today to $\approx0.6$ at $z_\text{rec}\approx1090$ *because* $\rho_b\propto a^{-3}$ and
$\rho_\gamma\propto a^{-4}$ dilute at different rates as space expands. This model has no
dilution (static space, conserved comoving number densities) — so if $R$ is genuinely
invariant as T16(C) states, it is pinned at $\approx680$ at *every* epoch, including
recombination, not just today.

A photon-baryon fluid with $R\approx680$ is baryon-dominated by nearly three orders of
magnitude, not the mildly baryon-loaded ($R\sim0.6$) oscillator that produces
$\Lambda$CDM's peak structure. Physically this means: (a) the restoring pressure from
radiation is negligible compared to baryon inertia at all epochs — the "acoustic"
oscillation is heavily overdamped/quenched rather than a clean standing wave, and (b)
the sound speed $c_s/c = 1/\sqrt{3(1+R)} \approx 0.022$ is $\sim20\times$ slower than
$\Lambda$CDM's recombination-epoch value ($c_s/c\approx1/\sqrt{3\times1.6}\approx0.45$).
This is a problem for the peak-*height* physics, independent of §3 below, which is a
problem for the peak-*position* physics.

## 3. The Angular Scale: A Floor That $\ell_1\approx220$ Cannot Clear

Combining the pieces: $\theta_s(z) = (c_s/c)\,(1+z)^{1-m}\big/\big[1-(1+z)^{-m}\big]$,
$m\equiv1/(nP)$. Two independent facts about this function, both verified numerically
(scanned $z=10^{-2}$ to $10^{20}$):

**(i) It is U-shaped in $z$**, diverging as $z\to0$ (source too close) *and* as
$z\to\infty$ (the model's own $D_A(z)\to R_\text{now}/(1+z)$ falls no faster than
$1/(1+z)$, but $r_s$ falls only as $(1+z)^{-m}$ with $m\le1$ — $\theta_s$ never shrinks
indefinitely the way it does in $\Lambda$CDM). There is a genuine finite minimum over
all possible $z_\text{rec}$, not a monotonic approach to some good value.

**(ii) At the model's own implied $R\approx680$, the minimum is far above what
$\ell_1\approx220$ needs** ($\theta_s^\text{target}=\pi/220\approx0.0143$ rad):

| Branch ($n$, $P=2$) | $\theta_s$ at $z_\text{rec}=1090$ | $\ell_1$ there | Best possible $\theta_s$ (any $z_\text{rec}$) | Best possible $\ell_1$ | Shortfall vs. $\ell_1=220$ |
|---|---:|---:|---:|---:|---:|
| Volume law $n=3$ (preferred) | 10.93 rad | 0.29 | 0.330 rad (at $z\sim2$) | 9.5 | **23$\times$** |
| Surface law $n=2$ | 5.08 rad | 0.62 | 0.210 rad (at $z\sim2$) | 15.0 | **15$\times$** |
| S$'$ law $n=2/3$ | 0.128 rad | 24.6 | 0.0468 rad (at $z\sim5$) | 67.1 | **3.3$\times$** |

The "best possible" columns are maximally charitable: they grant the model total
freedom to place recombination at whatever redshift most favors it (standing in for
T16 item A's admission that the model does not yet derive $z_\text{rec}$), while holding
$R$ fixed at the value the model's own self-similarity argument and today's measured
densities actually imply (§2) — that value is not a free knob. Even so, **no branch and
no choice of $z_\text{rec}$ gets within an order of magnitude of the observed peak**,
except S$'$, which gets within $3.3\times$ only at an unphysical $z\sim5$ recombination
epoch (nowhere near any plausible ionization/thermal threshold), and remains $9\times$
short at the observationally-labeled $z\approx1090$.

**Closing the gap by raising $R$ instead is foreclosed.** $\theta_s\propto(1+R)^{-1/2}$,
so reaching $\ell_1=220$ at $z_\text{rec}=1090$ would require $R\sim4\times10^8$
(volume law) or $R\sim5.5\times10^4$ (S$'$) — many orders above the $\approx680$ the
model's own mechanism gives, and also inconsistent with the baryon-to-photon ratio
$\eta\approx6\times10^{-10}$ already adopted from BBN (T13). At such $R$ the fluid is
not oscillating at all in any meaningful sense — the "sound speed" argument the peak
itself depends on would no longer apply.

## 4. Why This Happens: the Root Cause

$\Lambda$CDM gets sharp, small-angle peaks because recombination is *early*
($a_\text{rec}/a_0\sim10^{-3}$) and the universe expands by three more decades of scale
factor afterward, compressing early-universe features to sub-degree angles via the
$(1+z)$ machinery in $D_A$. This model's redshift–distance law is much shallower:
$D_p\propto(1+z)^{-1/(nP)}$ with $1/(nP)\le1$, so even $z=1090$ only reaches
$R_\text{rec}/R_\text{now}=(1+z)^{-1/6}\approx0.31$ (volume law) — recombination has
already used up **31% of the total light-travel budget**, not $10^{-3}$ of it. There
simply isn't enough "distance left over" between recombination and now, relative to how
big the sound horizon is in the same units, to squeeze the acoustic scale down to a
sub-degree angle. This is a structural feature of the static-space $c(t)$ geometry
itself (already used elsewhere, e.g. the SN distance table, T4), not a new assumption —
which is exactly why the shortfall is so large and so hard to escape by tuning any
single free parameter.

## 5. Honest Caveats

- This is a **leading-order geometric argument**, not a full radiative-transfer/line-of-
  sight (Boltzmann-code-level) calculation. A full treatment could shift $\ell_1$ by an
  $O(1)$ factor via projection effects, but not by the 1–3 orders of magnitude found
  here — the gap is too large for line-of-sight subtleties to close.
- $z_\text{rec}$ is not derived in this model (T16 item A, still open): its value here
  is used two ways — as the observationally-labeled redshift ($\approx1090$) for the
  main check, and as a free parameter for the "best possible" charitable bound. Neither
  choice rescues the result.
- $R\approx680$ rests on treating today's measured $\Omega_b h^2$ and $T_0$ as
  literal, model-independent facts fed into the model's own self-similarity claim.
  If future work revises *how* $\rho_b,\rho_\gamma$ actually scale (i.e., if T16(C)'s
  "both $\propto c^2$" derivation itself needs revision — the microphysics of exactly
  how a static, non-diluting photon gas maintains a well-defined comoving $n_\gamma$
  through cosmic history is not derived anywhere in the repository), this number could
  change. But no plausible revision closes 2–3 orders of magnitude without breaking the
  BBN $\eta$ input (T13) or the self-similarity claim itself.
- This does not address peak *heights* (already flagged as needing PBH wells) or
  $B$/$D$ (blackbody thermalization, $n_s$) — it is specifically about *position*.

## 6. Consolidated Edits (for merge)

| # | File | Edit | Type |
|---|------|------|------|
| 1 | T16 §(C) "The first peak translates without dark matter" | Downgrade: the plasma self-similarity argument stands, but the *position* prediction fails by 9–765$\times$ depending on branch; add the full derivation and table | **Reversal of a headline claim** |
| 2 | T16 "Current Status and Fit Assessment" table | Change row "(C) First acoustic peak" from "Translates via self-similarity — no DM needed" to "Self-similar plasma physics stands; angular *position* is a decisive quantitative failure (9–765$\times$ short of $\ell_1\approx220$, robust to $z_\text{rec}$ and premise-2 branch)" | Status change |
| 3 | T16 Open Questions | Mark the $\ell_1$ question **resolved (negative)**; remove from open list; add new open item: "is there a different definition of angular/sound-horizon geometry in a static-$c(t)$ spacetime that could recover small angular scales, or is this a genuine falsification point?" | Resolution + new item |
| 4 | Core Principles §7 status table, row "CMB power spectrum" | Update from "Speculative — first peak translates" to "Speculative — first-peak plasma self-similarity stands, but angular position fails by 1–3 orders of magnitude (T16)" | Status change |
| 5 | Project memory / open-problems list | Add as new high-priority open problem, likely above or alongside item 0 (T22 ephemeris tension) given it is a *quantitative, order-of-magnitude* falsification-relevant result on the single hardest observational test the model faces | Priority reorganization |

**Bottom line.** T16(C)'s self-similarity argument for the acoustic plasma's *shape*
survives this check, but a load-bearing second half of the argument — where the
resulting feature lands in $\ell$-space — was missing, and supplying it from formulas
already adopted elsewhere in the model (Core §4/§4a, verified against Core's own table)
gives a result 9 to 765 times off from the observed first peak, depending on which
premise-2 branch is used, and the gap survives maximal charity toward the two genuinely
free/unresolved quantities ($z_\text{rec}$, and to a lesser extent $R$). This is now the
sharpest quantitative problem in the model's speculative program — sharper than the
$\ell_1$ question's previous "unworked" status suggested, and arguably sharper than the
T22 ephemeris tension (a factor of a few thousand vs. this section's factor of
hundreds-to-thousands, but on the model's self-declared *hardest* test). It does not by
itself kill the model (the static-geometry translation of angular scales may simply be
the wrong tool, rather than the model being wrong), but it should be treated as a live
falsification candidate, not a "promising, not yet computed" item.
