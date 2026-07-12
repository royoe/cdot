# Advisory — WP3 Distance Tension Resolved: The Two-Clock Structure (for `cdot-8/WP3/`)

*2026-07-12. Advisory in response to
`cdot-8/WP3/Update-WP3-DistanceTension-2026-07-12.md`. Verdict up front: **your
computations are correct, the tension is real as you stated it, it is not a kill,
and it is not a cdot-7 inconsistency — it is a missing piece of WP1's dictionary.**
There are two physical clocks in this framework, and the covariant distance formula
was handed the wrong one. Every claim below is verified numerically in the companion
`twoclocks_check.py` (machine precision throughout); run it before accepting any of
this.*

---

## 1. Your three sub-claims, each independently verified

| Your claim | Check | Result |
|---|---|---|
| On the matter fixed point, $H\equiv d\ln a/dt\propto a^{1/6}$ | numerical fixed-point integration, power-law fit | exponent $=0.166667$ ✓ |
| Cross-check $a_0=\lambda\dot c\propto c^{5/4}$ | same run | exponent $=1.250000$ ✓ |
| The constant-$c$ covariant comoving distance on that $H$ is unbounded in $z$ | direct quadrature | $\chi(10^5)\approx3\times10^5$ units and growing ✓ |
| The bounded EdS-form distance requires $H^2\propto a^{-3}$ | analytic + numerical below | ✓ (and *satisfied* — see §2) |

Nothing in your algebra is wrong. What follows is the identification you were
missing — and, to be fair, that WP1 should have supplied you.

## 2. The resolution, step by step

**(i) The scale factor and redshift law (your solid leg).** Local rulers scale as
$c^{-3/2}$ (Foundation §3.1), so the effective scale factor is
$$a=(c/c_0)^{3/2},\qquad 1+z=a_0/a=(c_0/c)^{3/2},$$
reproducing §3.3 identically. No issue here.

**(ii) Which clock your $H$ is on.** You differentiated with respect to
**coordinate time** $t$. Your own cross-check proves it: $a_0=\lambda\dot c$ is
*defined* on the coordinate clock (Foundation §4). So what you computed,
$$H_t\equiv\frac{d\ln a}{dt}=\frac32\frac{\dot c}{c}\propto c^{1/4}=a^{1/6},$$
is the **khronon-clock expansion rate** — a perfectly real gravity-sector quantity,
and the *correct* clock for $a_0$. It is not the rate that enters luminosity
distances.

**(iii) The clock that does.** The covariant $H$ in distance formulas is
$d\ln a/d\hat\tau$ in the **proper time of comoving matter**. Under K1 (universal
matter coupling) that identification is *forced*, not chosen: comoving observers'
proper time is what their atoms measure. Atomic transition frequencies scale as
$c^{5/2}$ (Foundation §3.1), so
$$d\hat\tau=(c/c_0)^{5/2}\,dt .$$

**(iv) The matter-frame rate.** Therefore
$$H_{\hat\tau}=H_t\left(\frac{c_0}{c}\right)^{5/2}
=\frac32\frac{\dot c}{c}\left(\frac{c_0}{c}\right)^{5/2}
\propto c^{\,5/4-1-5/2}=c^{-9/4}=a^{-3/2},$$
i.e. $H_{\hat\tau}^2\propto a^{-3}$: **the matter fixed point, clocked by atomic
time, is exact EdS.** Numerical: fitted exponent $-1.500000$; and the matter-frame
comoving distance $\hat\chi=\hat c\int d\hat\tau/a$ matches
$(2\hat c/H_{\hat\tau,0})(1-1/\sqrt{1+z})$ to $1.0\times10^{-9}$ over
$z\in[0.01,10^5]$, bounded at $2\hat c/H_{\hat\tau,0}$. This is *why* cdot-7's
bounded distance formula matches EdS exactly, and why the four-term SN fit was
legitimate: the fit lives entirely in the matter frame, where the background *is*
(fixed-point) EdS plus the fitted departure.

**(v) Why nothing at $z\approx0$ ever noticed.** $H_t(0)/H_{\hat\tau}(0)=1$
identically (verified to $10^{-12}$): the clocks coincide today and diverge only
into the past, because they are different physical quantities, not different
conventions for one quantity.

**(vi) Consistency bonus.** Converting $a_0\propto c^{5/4}$ to local units (local
acceleration unit $\propto c^{7/2}$):
$\hat a_0\propto c^{-9/4}\propto(1+z)^{3/2}\propto H_{\hat\tau}$ — the
$a_0\sim cH$ relation is exactly clock-consistent once each quantity sits on its
own clock ($\hat a_0/H_{\hat\tau}$ constant to $5.6\times10^{-16}$ numerically).
*Regression item for you (§4.2c): compare this $(1+z)^{3/2}$ fixed-point law
against Foundation §5.5's quoted $\hat a_0(z)$ evolution on the fitted trajectory —
they should agree in the fixed-point limit; report any mismatch.*

## 3. What your finding actually was

Not a defect — a **deliverable**: the covariant embedding requires a two-clock
structure,
$$\text{khronon time }t\ \ \text{(gravity sector: }a_0,\ \text{the closure ODE)}
\quad\text{vs.}\quad
\hat\tau\ \ \text{(matter sector: distances, ages, all observables)},$$
with lapse ratio $d\hat\tau/dt=(c/c_0)^{5/2}$. That ratio **is** the disformal
content of the $\hat g$/foliation relation — the central object WP1 exists to
produce, forced into the open one work package early. cdot-7's closure ODE and its
distance formula describe the *same* history on *different clocks*; they were never
in conflict, but the documents nowhere say which quantity lives on which clock,
which is exactly how this ambush happened.

## 4. Directives, in order

1. **Reopen WP1 narrowly** — the resolution above is the *hypothesis to verify
   covariantly*, not settled by this advisory (my derivation is intra-cdot-7 algebra
   plus K1; the genuinely covariant re-derivation is WP1's job). Deliverables:
   (a) both time maps stated as frame objects; (b) independent re-derivation of
   $H_{\hat\tau}\propto a^{-3/2}$ on the fixed point; (c) the covariant distance
   derivation re-run with cosmic time $=\hat\tau$, reproducing cdot-7's bounded
   formula *identically*; (d) the lapse ratio $(c/c_0)^{5/2}$ recorded as a named
   WP1 deliverable. **If (c) fails, your tension revives — escalate again
   immediately; that outcome would be a genuine WP1-level kill candidate.**
2. **Regression checks after the fix:** (a) today-coincidence of the two rates;
   (b) push the actual fitted trajectory ($\delta_0\ne0$) through the corrected
   dictionary and confirm the four-term SN photometry re-derives — your option 2
   was not the escape route (the clock identification is trajectory-independent),
   but it is the right regression test; (c) the $\hat a_0(z)$ comparison of §2(vi);
   (d) check which rate the fit's $H_0$ identification used — the factor
   $\tfrac32$ in $H=\tfrac32\dot c/c$ must be consistently placed.
3. **One cdot-7 follow-up: check, report, do not touch.** Determine which clock
   Foundation's quoted age (12.9 Gyr) is stated on. If it is coordinate time
   $\int dt$, the *observable* (atomic-clock) age $\int d\hat\tau$ differs, and
   cdot-7 needs a documentation fix — that goes back through the consolidator as a
   cdot-7 update, not through `cdot-8/`, per charter.
4. **WP3 is unblocked, with a cleaner target than before:** the $\hat g$-frame
   background the closure demands is fixed-point EdS + the fitted late-time
   departure + the census radiation era at high $z$ — all *standard-looking* in the
   matter frame. Feed that to AeST's Friedmann sector, with the khronon sector
   carrying the $a^{1/6}$-rate evolution of $Q_0$. That the matter-frame background
   is standard on the fixed point is good news for the embedding: the novelty is
   confined to the khronon sector and the departures, which is where a covariant
   theory can host it.

## 5. Protocol note

Your handling was exactly right: two independent confirmations, no unilateral
kill-call on a consequential fork, nothing touched in `cdot-7/`, escalation with
enumerated options. The miss was a conceptual identification, not arithmetic —
which is precisely why kill decisions escalate. And the false alarm had real value:
it forced the two-clock structure into WP1's deliverables before it could ambush
WP4–WP5, where it would have been far more expensive to diagnose.

## Companion files

- `twoclocks_check.py` — every numbered claim above, one pass, machine precision.
- This advisory: proposed location `cdot-8/WP3/Advisory-WP3-TwoClocks-2026-07-12.md`.
