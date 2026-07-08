# Update — The Photon Sector: an Internal Inconsistency in §3.3, the Corrected Redshift Law, and the Flux/Luminosity Sector (Open Item 2)

*Status: update document for cross-check and merge. Proposes replacements for
`Foundation.md` §3.3, §5.2, §5.3, §5.4, and revisions to §6 items 2 and 8; the
derivation trail below is intended for `ResearchNotes.md` (proposed new §8). Produced
2026-07-07 (cdot-7, session entry 4).*

**Summary of what this update does.** It finds that §3.3's redshift law rests on a
premise ("a photon's conserved frequency") that contradicts premise 1 + premise 2's own
propagation kinematics, corrects it (conserved *wavelength*, redshift exponent
$\tfrac32$ not $\tfrac52$), and then builds the flux/luminosity sector (open item 2) on
the corrected law. The corrected sector passes three observational tests the old law
failed or could not address (SN light-curve time dilation, Etherington distance duality,
Tolman surface-brightness dimming) — and fails two it previously appeared to pass or
left open (cosmic age; the SN Ia Hubble diagram, where the framework is now shown to be
photometrically *identical* to Einstein–de Sitter, hence decelerating). The net effect
is a framework that is more internally consistent and more falsifiable, with one large
new theoretical debt (a $\Lambda$-analog) replacing open item 2.

---

## 1. The Inconsistency in §3.3

Foundation §3.3 derives the redshift law by "comparing a photon's conserved frequency
against the local atomic standard." The conserved-frequency premise is not available
inside this framework. Two independent arguments, both using only premises 1–2:

### 1.1 Crest-transit kinematics (the same law that defines $R_h$)

Premise 2's horizon law, $\dot R_h = c(t)$, is a statement about how light propagates:
any signal front at time $t$ moves at $c(t)$. Apply it to two successive signals
(pulses, or wave crests) emitted a coordinate interval $\Delta t_e$ apart from a source
at fixed distance $D$ from the observer (space is static, premise 1; both endpoints at
rest):
$$\int_{t_e}^{t_0} c(t)\,dt = D = \int_{t_e+\Delta t_e}^{t_0+\Delta t_0} c(t)\,dt
\quad\Rightarrow\quad c(t_e)\,\Delta t_e = c(t_0)\,\Delta t_0 ,$$
to first order in the small intervals. The arrival rate exceeds the emission rate by
$c_0/c_z$. But the arrival rate of crests *is* the received frequency — frequency is not
a label carried by the photon separately from its crest kinematics. So the coordinate
frequency of light in flight is **not** conserved; it grows as $c(t)$.

Equivalently, and more physically: in spatially homogeneous space every crest moves at
the same instantaneous speed $c(t)$, so the *spacing* between crests — the wavelength —
cannot change in flight. Conserved frequency would require $\lambda(t)\propto c(t)$ to
stretch mid-flight, which needs crests at different positions to move at different
speeds, i.e. a position-dependent $c$ — precisely the Atkinson-type structure cdot-7
deliberately dropped. §3.3 as written is therefore not merely a different convention; it
contradicts the propagation law premise 2 itself relies on.

### 1.2 Wave mechanics (symmetry argument)

Premise 1 gives exact spatial translation invariance (static, homogeneous Euclidean
space; $\epsilon_0(t),\mu_0(t)\propto c^{-1}$ uniform in space), and premise 2 breaks
time-translation invariance ($c=c(t)$). By the usual correspondence, the conserved
quantity is the spatial wavenumber $k$, not the frequency. Explicitly, a mode
$\varphi = a(t)e^{ikx}$ of the wave equation $\ddot\varphi = c(t)^2\nabla^2\varphi$
obeys $\ddot a = -c(t)^2k^2 a$: an oscillator with slowly varying frequency
$\omega(t)=c(t)k$. The evolution is deeply adiabatic ($\dot c/c\sim10^{-18}\,
\text{s}^{-1}$ against optical frequencies $\sim10^{15}\,\text{s}^{-1}$), so the WKB
adiabatic invariant $E/\omega$ — the photon number — is conserved, and each photon's
energy grows in flight:
$$k=\text{const},\qquad \omega(t)=c(t)\,k,\qquad E_\gamma(t)=\hbar\,\omega(t)\propto c(t).$$
Photons *gain* energy in flight here, the exact mirror image of the energy a photon
loses to expansion in the standard picture — in both cases a time-dependent background,
not a local conservation violation.

Both arguments give the same answer, and 1.1 uses nothing but the kinematics already in
§2 — so this is an internal-consistency correction, not a new assumption.

---

## 2. The Corrected Redshift Law

A photon emitted at $t_e$ (epoch $c_z$) from an atomic transition matches the emitter's
local standard, $\nu_e=\nu_\text{atom}(t_e)\propto c_z^{5/2}$ (§3.1). Its wavelength at
emission,
$$\lambda=\frac{c(t_e)}{\nu_e}\propto c_z^{-3/2},$$
is conserved in flight (§1). At reception it oscillates at $\omega_\text{rec}=c_0
k\propto c_0\,c_z^{3/2}$, compared against the receiver's standard
$\nu_\text{atom}(t_0)\propto c_0^{5/2}$:
$$\boxed{\,1+z=\frac{\nu_\text{atom}(t_0)}{\omega_\text{rec}}
=\left(\frac{c_0}{c_z}\right)^{3/2}\quad\Longleftrightarrow\quad
c_z=c_0\,(1+z)^{-2/3}.}$$

**The exponent is exactly the Bohr-radius exponent (§3.1), and that is not a
coincidence.** The identical result follows from comparing the conserved wavelength
against the local ruler: $\lambda$ fixed, $a_\text{Bohr}\propto c^{-3/2}$ shrinking, so
$1+z = (c_0/c_z)^{3/2}$ measured either way (frequency against clock, or wavelength
against ruler — consistent, as it must be, since locally $\omega_\text{rec}\lambda=c_0$).
The physical picture of redshift in this framework is now sharp: **light does not
stretch; the ruler shrank since emission.** For general mass exponent $s$ the law is
$1+z=(c_0/c_z)^{s+1}$; the value $\tfrac32$ is $s=\tfrac12$'s.

---

## 3. Light-Curve Time Dilation — Now Exact, and Empirically Mandatory

An event of duration $\Delta t_e$ (coordinate) at the source is received over
$\Delta t_0=\Delta t_e\,c_z/c_0$ (§1.1). Measured in each epoch's own clock ticks
($\nu\propto c^{5/2}$):
$$\frac{\Delta\tau_0}{\Delta\tau_e}
=\left(\frac{c_0}{c_z}\right)^{5/2}\cdot\frac{c_z}{c_0}
=\left(\frac{c_0}{c_z}\right)^{3/2}=1+z\qquad\text{exactly.}$$
Distant events dilate by exactly $(1+z)$ — and this equality of dilation factor and
redshift is *generic in $s$* (dilation $=(c_0/c_z)^{(s+2)-1}$, redshift exponent $s+1$),
because redshift and time dilation are physically the same measurement (frequency is an
inverse period). Under the old conserved-frequency law they would have differed —
dilation $(c_0/c_z)^{3/2}=(1+z)^{3/5}$ against redshift $(1+z)$ — which is both
internally incoherent and observationally excluded: SN Ia spectral aging measures the
dilation exponent as $\approx0.97\pm0.10$ (Blondin et al. 2008, reported from memory —
verify exact figure before merge), putting $(1+z)^{3/5}$ roughly $4\sigma$ out. **The
correction of §1–2 is therefore empirically mandatory, not merely formal.**

---

## 4. Cosmological Relations, Rebuilt on the Corrected Law

Matching §2.2's closure $c(w)=c_0(1+w/\tau)^{-4}$ (unchanged — it never used the
redshift law) against $c_z=c_0(1+z)^{-2/3}$:
$$w(z)=\tau\left[(1+z)^{1/6}-1\right],\qquad
R_h(t_e)=R_{h,0}(1+z)^{-1/2},\qquad
D_p(z)=R_{h,0}\left[1-(1+z)^{-1/2}\right].$$
Low-$z$ expansion, $D_p\approx R_{h,0}z/2$, identifies
$$H_0^\text{obs}=\frac{6}{\tau}=\frac{3}{2}\,H_0^\text{hor},\qquad
H_0^\text{hor}=\frac{4}{\tau}=\frac{2}{3}H_0^\text{obs},$$
replacing the old ratio $\tfrac52$ (that ratio is fixed by the redshift exponent alone,
as §5.2 already noted — so it changes when the exponent does). Numerically, with
$H_0^\text{obs}=70$ km/s/Mpc:
- $\tau=6/H_0^\text{obs}\approx8.38\times10^{10}$ yr (was $1.40\times10^{11}$ yr);
- $H_0^\text{hor}\approx1.51\times10^{-18}\,\text{s}^{-1}\approx4.77\times10^{-11}\,
  \text{yr}^{-1}$ (was $2.86\times10^{-11}\,\text{yr}^{-1}$ — **so the "robustness" of
  $H_0^\text{hor}$ and $a_0$ claimed in §5.2–5.3 held against the closure rebuild but
  does *not* hold against this redshift-law correction**);
- proper age $\tau_\infty=\tau/9=\dfrac{2}{3H_0^\text{obs}}\approx9.3$ Gyr (was 15.5);
- particle horizon $D_p(\infty)=R_{h,0}=\tau c_0/3=2c_0/H_0^\text{obs}\approx8.6$ Gpc
  (was 14.3).

The age result is a genuine new problem: $9.3$ Gyr is below globular-cluster ages
($\approx12.5$–$13$ Gyr). See §5.3 below for why this is not an accident.

---

## 5. The Flux/Luminosity Sector (Open Item 2)

### 5.1 Luminosity distance

A standard candle emits, in its own local units, a fixed luminosity. Converting between
local and coordinate units (energy unit $\propto c^{5/2}$, clock rate $\propto c^{5/2}$),
and propagating to a receiver at fixed distance $D_p$ in static space, the received
bolometric flux in the receiver's local units picks up exactly two factors of
$(1+z)^{-1}$:
1. **Per-photon energy.** The photon's energy grows in flight ($\propto c$, §1.2) but
   the receiver's energy unit grew faster ($\propto c^{5/2}$): net
   $(c_0/c_z)\,(c_z/c_0)^{5/2}=(c_z/c_0)^{3/2}=(1+z)^{-1}$.
2. **Arrival rate.** Arrivals are compressed in coordinate time by $c_0/c_z$ but the
   receiver's clock ticks faster by $(c_0/c_z)^{5/2}$: net per-tick rate
   $(c_z/c_0)^{3/2}=(1+z)^{-1}$.

(Both factors are generic in $s$, by the same cancellation as §3.) Hence
$$F=\frac{L}{4\pi D_p^2\,(1+z)^2}\qquad\Longrightarrow\qquad
\boxed{\,d_L(z)=(1+z)\,D_p(z)\,}$$
— formally identical to the standard-cosmology relation, emerging here from shrinking
units rather than expanding space.

### 5.2 Angular sizes, distance duality, and the Tolman test

A bound object of fixed size in local units was *physically larger* in the past:
$\ell_\text{phys}(t_e)\propto c_z^{-3/2}=\ell_0(1+z)$ (premise 3, §3.2 — orbits and
atoms shrink together). Light travels in straight lines in static Euclidean space, so
$$\theta=\frac{\ell_0(1+z)}{D_p}\qquad\Longrightarrow\qquad d_A=\frac{D_p}{1+z},$$
and therefore
$$\frac{d_L}{d_A}=(1+z)^2\qquad\text{— the Etherington duality relation, exactly.}$$
This is a nontrivial pass: distance duality is observationally tested and is the
standard executioner of tired-light models (which get $d_L=(1+z)^{1/2}D$ and fail).
It follows immediately that surface brightness dims as
$F/\theta^2\propto(1+z)^{-4}$ — **the exact Tolman signature of an expanding universe,
reproduced by a static space with shrinking matter.** Both results are generic in $s$
(the angular factor is $(c_0/c_z)^{s+1}=(1+z)$ for every $s$): they are structural
consequences of "everything local scales together," not of the specific exponent.

### 5.3 The Hubble diagram: exact Einstein–de Sitter degeneracy — and its failures

Substituting $D_p(z)$ and $R_{h,0}=2c_0/H_0^\text{obs}$:
$$d_L(z)=\frac{2c_0}{H_0^\text{obs}}\Big[(1+z)-\sqrt{1+z}\,\Big].$$
This is, term for term, the Einstein–de Sitter ($\Omega_m=1$) luminosity distance. The
low-$z$ expansion $d_L=(c_0/H_0)[z+\tfrac14z^2+\dots]$ gives
$$q_0=+\tfrac12 .$$
Together with §5.2, and with the age landing on EdS's $\tfrac{2}{3H_0}$ (§4): **every
purely photometric or geometric observable computed so far — $d_L(z)$, $d_A(z)$, time
dilation, Tolman dimming, distance duality, age — coincides exactly with Einstein–de
Sitter.** The framework is, at this stage, photometrically indistinguishable from
$\Omega_m=1$ despite a completely different ontology.

That cuts both ways:
- **Pass:** it inherits every test EdS passes — precisely the tests that kill
  tired-light and most static-universe proposals.
- **Fail:** it inherits EdS's two decisive failures. The SN Ia Hubble diagram excludes
  $q_0=+\tfrac12$: this framework predicts high-$z$ SNe *brighter* than observed
  (roughly $0.25$ mag at $z\sim0.5$ against the 1998-era data, growing to
  $\sim0.5$–$0.6$ mag against $\Lambda$CDM at $z\sim1$ — approximate figures, to be
  recomputed precisely at merge time). And the $9.3$ Gyr age is EdS's age problem,
  reborn.

### 5.4 Tuning $s$ cannot rescue acceleration — the failure is structural

For general $s$ (number-conserved closure, §2.2 generalized): $R_h\propto
c^{(2-s)/2}$, redshift exponent $s+1$, and the same construction gives
$$d_L(z)=R_{h,0}\left[(1+z)-(1+z)^{1-\beta}\right],\qquad
\beta\equiv\frac{2-s}{2(s+1)},\qquad q_0=\beta .$$
Acceleration ($q_0<0$) requires $\beta<0$, i.e. $s>2$ — but then $R_h\propto
c^{(2-s)/2}$ *shrinks* as $c$ grows, contradicting the kinematic $\dot R_h=c>0$. And
independently, LLR pins $s=\tfrac12$ given $g=0$ (§5.1 of the Foundation;
`ResearchNotes.md` §3). So within this closure family **no value of $s$ yields
acceleration**: the deceleration is structural to the Sciama-type closure plus static
geometry, not a tunable artifact of $s=\tfrac12$. Whatever plays the role of $\Lambda$
here must come from modifying the closure (or adding a sector), not from re-fitting the
scaling exponent. This becomes the sharpest open item in the framework (§7 below).

---

## 6. Two Sections of the Foundation Reframed

### 6.1 §5.3 ($a_0$ numerics) — revised, for the worse

$a_0\equiv\lambda c_0H_0^\text{hor}$ with the corrected
$H_0^\text{hor}=\tfrac23H_0^\text{obs}$:
$$a_0\approx4.5\times10^{-10}\ \text{m/s}^2\ \ (\lambda=1),\qquad
\lambda\approx0.26\ \text{to match}\ a_0^\text{emp}\approx1.2\times10^{-10}\ \text{m/s}^2.$$
The order-of-magnitude relation $a_0\sim cH_0$ survives, but the tension factor grows
from $\approx2.3$ to $\approx3.8$. Reported plainly; still not derived (§6 item 1).

### 6.2 §5.4 / open item 8 — the "directional prediction" is not a local prediction

The lockstep shrinkage $r\propto c^{-3/2}$ is unobservable *in principle* by any local
measurement — §5.1's exact LLR cancellation is the proof, not a special case: every
local length standard shrinks identically, so there is no local residual to detect, at
any epoch. Its one observable manifestation is cosmological, and it is exactly the
$(1+z)$ angular-size factor of §5.2 above: objects at redshift $z$ subtend angles as if
$(1+z)$ times larger, which *is* the standard angular-diameter relation. Open item 8 is
therefore not a separate test to hunt a dataset for; it is subsumed into the photometric
sector, where the model currently sits exactly on EdS. Proposed: close item 8, replace
§5.4 with this reframing.

---

## 7. A Payoff for §0's Methodological Note, and the Revised Open Items

§0 assumes, without constructing, a canonical correspondence between this description
and an ordinary expanding one. For the photon sector, this update partially
*constructs* it: $D_p\leftrightarrow$ comoving distance, shrinking rulers
$\leftrightarrow$ expanding space, photon energy gain against faster-growing units
$\leftrightarrow$ photon energy loss against fixed units — mapping exactly onto EdS.
The correspondence also identifies, in the standard picture's terms, precisely what
this framework is missing: **whatever plays the role of $\Lambda$.**

**Proposed revisions to `Foundation.md` §6:**
1. *(item 1 — unchanged in substance)* Derive $s=+\tfrac12$ and $\lambda$; note
   $\lambda\approx0.26$ now.
2. *(item 2 — replaced)* ~~Build the flux/luminosity sector~~ **Done (this update).**
   New item: **find the framework's $\Lambda$-analog** — the modification (to the
   Sciama closure, or a new sector) that breaks the exact EdS degeneracy toward
   $q_0\approx-0.55$ and an age $\gtrsim13$ Gyr. §5.4 above proves this cannot come
   from re-tuning $s$.
3. *(items 3, 6 — unchanged)* Fix $\mu(x)$.
4. *(item 4 — unchanged)* Relativistic completion.
5. *(item 5 — unchanged)* Justify homogeneity of $n$.
6. *(item 7 — unchanged, slightly sharpened)* The EM-sector tension now matters more:
   the photon sector built here leans directly on $\epsilon_0\propto c^{-1}$ (via the
   wave equation of §1.2), so reconciling it with premise 3 is no longer cosmetic.
7. *(item 8 — closed)* Reframed per §6.2 above.
8. *(new)* Recompute the SN Ia magnitude comparison precisely (this update quotes
   1998-era approximate offsets) and verify the Blondin et al. dilation constraint
   figure before treating §3's exclusion as final.

**Proposed text edits at merge:** replace Foundation §3.3 with §2 above (recording the
old law's inconsistency in `ResearchNotes.md`, per project practice of keeping dead ends
visible); replace §5.2's numbers with §4 above; replace §5.3 with §6.1; replace §5.4
with §6.2; add the flux/luminosity results (§5 above) as a new Foundation §5.5; update
§6 per the list above.

---

## 8. Honest Ledger

Fixed by this update: an internal contradiction between §3.3 and §2's kinematics; three
observational tests now passed exactly and generically (time dilation $(1+z)$,
Etherington duality, Tolman $(1+z)^{-4}$) where the old law failed the first and had
nothing to say about the others. Broken or worsened by this update: the age
($15.5\to9.3$ Gyr, now below stellar ages), the $a_0$ prefactor ($\lambda\approx0.44\to
0.26$), and — the big one — an exact EdS degeneracy that puts the framework in direct
conflict with the SN Ia acceleration, shown to be unfixable by tuning $s$. The framework
is more consistent and much more falsifiable than it was this morning, and it now owes
an answer to the same question standard cosmology answered with $\Lambda$.
