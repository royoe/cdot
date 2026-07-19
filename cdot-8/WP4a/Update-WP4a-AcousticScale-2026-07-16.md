# Update — WP4a: The CMB Acoustic Scale, First-Principles Attempt

*Companion: `SessionLog-2026-07-16.md` (this directory, new). Executes WP4a per
the cdot-8 proposal's Stage-1 confrontation, but treated with the same weight
as cdot-7 Foundation §6 item 6's own gated item, not as a "cheap, immediate"
afterthought — that section explicitly leaves this territory "not yet
authorized, pending an explicit decision," citing two prior, decisive
structural failures in cdot-4 and cdot-5. This attempt is first-principles
where the history flagged ambiguity (the distance convention, the recombination
redshift), reuses only what's already established and verified (the
matter+radiation+neutrino census trajectory from `census_closure.py`/cdot-8's
WP3 machinery), and reports the actual numerical result plainly.*

---

## 1. Resolving the historical ambiguities before computing anything

**The distance convention.** cdot-4/cdot-5's peak calculations used $D_A\equiv
D_p$ (no redshift suppression); cdot-7's own Foundation §5.5 derives and proves
the opposite, $d_A=D_p/(1+z)$, with exact Etherington duality — this is the
current, validated, load-bearing convention and supersedes the earlier stages'
usage. **Neither applies directly to $\theta_*$, and using either naively is
wrong.** $\theta_*=r_s(z_*)/D_A(z_*)$ with the physical $d_A=D_p/(1+z_*)$ would
compare a size measured *today's* units to a distance already in *today's*
units at the wrong power of $(1+z_*)$ — verified numerically first (gave
$100\theta_*\approx1456$, nonsensical) before being caught. The correct
statement, re-derived from Foundation §5.5's own lockstep formula
$\theta=\ell_0(1+z)/D_p$: $r_s(z_*)$ as computed by the standard integral
$\int_{z_*}^\infty c_s(z)/H(z)\,dz$ is a size **at the recombination epoch's own
scale**, not today's; converting it to today's units via the same lockstep
relation and then applying $\theta=\ell_0(1+z_*)/D_p$ makes the $(1+z_*)$
factors cancel exactly, giving
$$\boxed{\theta_*=\frac{r_s(z_*)}{D_p(z_*)}}$$
— structurally the same cancellation standard cosmology's own $r_s/D_M$
(comoving-over-comoving) convention exploits, now re-derived inside this
framework's own formalism rather than imported by analogy.

**The recombination redshift.** Not re-derived from a static-map/kinetics
argument the way cdot-5 attempted (and left genuinely unresolved, $z_\text{rec}$
swinging between $\sim1240$ and $\sim2\times10^6$ depending on an unsettled
sudden-vs-gradual assumption). Foundation §3.1 and §5.5 already establish, and
this update rests on, a stronger and already-verified fact: atomic/binding
energies are Planck-unit invariant (Bohr radius $\propto c^{-3/2}$, atomic
frequency $\propto c^{5/2}$, exactly the same scaling as every other local
ruler/clock), and the thermal sector is "reproduced exactly, with no new
assumptions" ($\hat T(z)=\hat T_0(1+z)$, verified against SZ and molecular-
absorber data). Recombination is a competition between the local photon
temperature and the local (invariant) hydrogen binding energy — since both
sides of that competition are local, invariant quantities behaving exactly as
in standard cosmology, **recombination occurs at the standard redshift**, not
a re-derived one. Adopted: $z_*=1089.80$ (Planck 2018 TT,TE,EE+lowE+lensing).
Checked for sensitivity: varying $z_*$ over $1089$–$1100$ changes $\theta_*$ by
$<1\%$ — the result does not hinge on this choice to within its own precision.

## 2. The calculation

Reused, without modification, the matter+radiation+neutrino census trajectory
already established and verified this session ($\kappa\lambda=0.4355$,
$x_0=1.10$, the same closure ODE, $E(z)=H_{\hat\tau}(z)/H_{\hat\tau,0}$) —
extending the existing integration range from $z\sim10^6$ (WP2/WP3's range) to
$z\sim10^{10}$ to safely cover the sound-horizon integral's tail, and
explicitly checking convergence: the naive range (to $z=10^7$) gave $r_s=174.5$
Mpc, not yet converged (contaminated by an extrapolation artifact past the
solved trajectory); extending to $z=10^{10}$ and confirming the last three
significant figures stop moving gives the converged $r_s=173.36$ Mpc.

**Baryon fraction**: not independently fit — taken directly from the
already-established mass census, $\Omega_b=\Omega_\text{closure}-
\Omega_\nu^\text{census}=0.074-0.0298=0.0442$ (Foundation §2.4), consistent
with this program's own "zero adjustable parameters" discipline rather than
importing an external, independently-fit $\Omega_b$.

**Sound speed and horizon**: standard, unmodified formula ($c_s=c_0/
\sqrt{3(1+R)}$, $R(z)=3\Omega_b/(4\Omega_{\gamma,0}(1+z))$ — local baryon-photon
physics, invariant, no reason to modify it) integrated against cdot-8's own
$E(z)$:
$$r_s(z_*)=\int_{z_*}^\infty\frac{c_s(z)}{H_0E(z)}\,dz=173.36\text{ Mpc}.$$

**Comoving distance**, same $E(z)$, standard integral:
$$D_p(z_*)=\int_0^{z_*}\frac{c_0}{H_0E(z)}\,dz=13074.3\text{ Mpc}.$$

## 3. Result

$$\theta_*=\frac{r_s(z_*)}{D_p(z_*)}=1.326\times10^{-2}\text{ rad},\qquad
100\,\theta_*=1.326.$$

**Planck 2018: $100\,\theta_*=1.04109\pm0.00030$. Ratio: $1.274$ — cdot-8's
first-principles value is $27\%$ high.**

This is neither a success nor a repeat of the historical failures (which
ranged from a $9\times$ shortfall to a $765\times$ shortfall in cdot-4's
worst branch, down to a $1.3$–$1.4\times$ overshoot in cdot-4/5's later,
corrected passes). A $27\%$ discrepancy is a real, assessable tension —
resolved conventions this time (no ambiguity left in $z_*$ or the distance
formula), computed from already-established, zero-additional-knob inputs.

## 4. What's driving the discrepancy, and what isn't

Compared term by term against standard $\Lambda$CDM reference values ($r_s
\approx144$–$147$ Mpc, $D_M(z_*)\approx13870$ Mpc): $r_s$ comes out
$\sim18$–$20\%$ **larger** than standard (traceable to $\Omega_b=0.0442$ here
vs. $\Omega_b\approx0.049$ in $\Lambda$CDM — a smaller baryon fraction gives a
larger sound speed, hence a larger horizon), and $D_p$ comes out $\sim6\%$
**smaller** than standard (traceable to cdot-8's own fitted $E(z)$ differing
from $\Lambda$CDM's across the full integration range, not a recombination-era
effect). The two effects compound in the same direction. **Neither is a free
parameter tuned to produce this number** — $\Omega_b$ comes from the already-
fixed mass census (§2.4), and $E(z)$ from the already-fitted SN/RAR/mass-census
trajectory (§2.2) — so this is a genuine, zero-knob output of the theory as
currently built, not a result that could be adjusted away without touching
already-validated fits.

## 5. Status

**A real number, honestly reported, not a resolution.** $27\%$ is not
negligible — this is the theory's first genuine data confrontation beyond the
SN diagram, and it does not pass cleanly. It is also not a "decisive structural
failure" in the sense Foundation §6 item 6 flagged from cdot-4/5's history
(those were factor-of-9-to-765 misses with an unresolved recombination
redshift; this is a factor-of-1.27 miss with every convention question
resolved and checked). **Recommend**: report this precisely as WP4a's actual
result, escalate for review given Foundation's own standing requirement that
this territory needs "an explicit decision" before further extension (not a
unilateral call to declare either "WP4a passes" or "this kills cdot-8"),
and flag the two identified, non-tunable levers (the mass-census $\Omega_b$,
the fitted $E(z)$) as the concrete place any future refinement would have to
locate a correction, if one exists. WP4b (BBN) remains queued, gated on the
$e^+e^-$/QCD census kinks per Foundation §6 item 5. The KATRIN clock remains
the program's most time-critical item; nothing in `cdot-7/` was touched.
