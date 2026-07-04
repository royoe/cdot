# T9 — Orbital Dynamics under Invariant G

*Checked carefully against the counting-law change (Core Principles §1), as with
T5–T8. Result: **confirmed unaffected**, and for the same structural reason as T8: this
document's physics comes entirely from premise 3 (invariant $G$, invariant mass) and
T11's angular-momentum conservation argument, plus one present-day rate,
$H_0^\text{hor}$, whose value ($H_0^\text{hor}=H_0^\text{obs}/P=35$ km/s/Mpc) is fixed
by the redshift law's $P$ and is identical under both counting laws. Nothing here
integrates over cosmic history, so nothing here is sensitive to how that history
changed.*

## Observational Background

### Lunar and Planetary Orbital Stability

The Earth-Moon distance is known to be increasing at $\approx3.8$ cm/year from tidal
dissipation — a purely local mechanical effect driven by angular-momentum transfer
through ocean tides. Earth's orbit around the Sun shows no secular expansion at
measurable levels; planetary perturbations dominate over any hypothetical cosmological
drift.

---

## Orbital Evolution under Invariant G

Under the model's premise 3 — invariant $G$ ($G\propto c^0$) and invariant mass
($m\propto c^0$) — the orbital radius is fixed. This section is unchanged from cdot-4
in every particular: it never references the cosmological counting law.

### Derivation

For an adiabatic circular orbit:
$$\frac{mv^2}{r}=\frac{GMm}{r^2}\implies v^2=\frac{GM}{r}.$$
Angular-momentum conservation: $L=mvr=\text{const}$ (the isotropic vacuum exerts no
torque — T11; this follows from the static map's isotropy, Core Principles §0, and is
independent of premise 2's counting law).

Combining: $v=L/(mr)$ and $v^2=GM/r$, so $L^2/(m^2r^2)=GM/r$, giving:
$$r=\frac{L^2}{m^2GM}.$$
With invariant $m$, invariant $L$, and invariant $G$: **$r=\text{const}$**. Orbits do
not expand. The orbit radius $r=L^2/(m^2GM)$ is a constant of motion.

This is the direct consequence of adopting invariant $G$ (T8). The prior claim of
orbital expansion $r\propto c^2$ (cdot-3) followed from $G\propto c^{-2}$, which was
refuted by LLR (T8, $\times720$ tension) — a premise-3 result, unaffected by cdot-5's
premise-2 revision.

### Orbital velocity and period

With $r=\text{const}$ and $G=\text{const}$: $v=\sqrt{GM/r}=\text{const}$ in coordinate
units, so the coordinate period $T_\text{coord}=2\pi r/v=\text{const}$ as well. In
atomic clock time (which accumulates ticks at $\nu\propto c^2$, Core Principles §5a),
one orbit contains $T_\text{coord}\cdot\nu$ ticks, so the atomic period grows gently as
$T_\text{atomic}=T_\text{coord}\cdot(\nu/\nu_0)\propto c^2$: early-Earth years were
slightly shorter than today's in atomic time. This drift is cosmologically slow,
$$\frac{\dot T}{T}=2H_0^\text{hor}\approx7\times10^{-11}\ \text{yr}^{-1},$$
and irrelevant to LLR — the *coordinate* orbit is frozen. **This number is identical
under both counting laws** — verified directly: $H_0^\text{hor}=H_0^\text{obs}/2=35$
km/s/Mpc regardless of whether $c(t)$'s cosmological history follows the old
occupancy-counting law or the new connectivity-counting law (Core Principles §4a, T3),
because the relation $H_0^\text{hor}=H_0^\text{obs}/P$ comes from the redshift law's
mass-scaling exponent $P$, not from the counting law.

**Consequence for LLR and planetary radar:** no cosmological contribution to the
Earth-Moon distance evolution or to the Earth-Sun distance. LLR and planetary ranging
are therefore consistent with the model (T8).

---

## Received Stellar Flux

Unchanged from cdot-4. With static orbits and $L_\text{lum}\propto c^0$ (T18,
corrected), received flux is $c$-invariant: $F\propto c^0$. The full derivation of
stellar luminosity, the habitability ratio $X=T_\text{eq}/T_\text{mol}\propto c^{-3/2}$,
and the implications for the faint young Sun paradox are in T18 — none of this
references the cosmological counting law, only invariant $G$, static orbits, and T18's
opacity treatment.

---

## Broader Structural Notes

**Binary pulsars.** Unchanged from cdot-4. Under invariant $G$ with invariant mass,
$G(t)=\text{const}$, and there is no cosmological orbital expansion in binary pulsars.
The Hulse-Taylor system's orbital decay is purely from gravitational-wave emission
(unchanged from GR); there is no additional $\dot G$ term. This removes a potential
additional source of tension (cdot-3 flagged this as a concern) and is trivially
consistent — a premise-3 result, unaffected by cdot-5's premise-2 revision.

---

## Open Questions

Unchanged from cdot-4 — neither question is counting-law-sensitive:

- **Angular-momentum conservation (T11).** The proof that $L=mvr=\text{const}$
  requires the vacuum to be exactly isotropic (no torque). Are there corrections from
  local anisotropy (the Sun's own gravity, galactic tidal field) that break this at
  measurable levels? Likely negligible, but should be verified.
- See T18 for open questions on stellar luminosity $L(c)$, climate modelling, albedo,
  and molecular temperature scaling.
