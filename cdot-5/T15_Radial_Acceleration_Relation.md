# T15 — The Radial Acceleration Relation (RAR)

*Checked against the counting-law change, T6/T14's reconciliation, and T23's
percolation break. The RAR closure's functional form is confirmed unaffected — it is
local, galactic-scale physics with $g_\dagger$ entering as an external parameter, not
something the derivation itself fixes. The scale $g_\dagger$ inherits T6/T14's open
question (three candidate finite lengths, best within $1.63\times$ of $a_0$, not
resolved). The epoch-dependence section is **redone from scratch** — it depends
directly on how $H^\text{hor}(z)$ evolves, which changed with the counting law, and the
result is genuinely different, not just recalibrated, plus a new subtlety: the
observationally-relevant redshift range straddles the percolation break itself.*

---

## Observational Background

The **Radial Acceleration Relation** (McGaugh, Lelli, Schombert 2016) is the sharpest,
most theory-neutral statement of the rotation-curve anomaly. It is derived from
$\sim150$ galaxies spanning five decades in baryonic mass, covering spirals,
ellipticals, dwarfs, and low-surface-brightness galaxies.

The relation states: the observed centripetal gravitational acceleration
$g_\text{obs}$ (inferred from rotation curves or velocity dispersions) is a **tight
one-parameter function** of the baryonic Newtonian prediction $g_\text{bar}$:
$$g_\text{obs}=\frac{g_\text{bar}}{1-e^{-\sqrt{g_\text{bar}/g_\dagger}}},\qquad
g_\dagger\approx1.2\times10^{-10}\ \text{m/s}^2.$$

Key features, unchanged: scatter $\sim0.13$ dex; no residual dependence on galaxy
size, morphology, surface brightness, or environment; Newtonian limit
$g_\text{bar}\gg g_\dagger$; deep-MOND limit $g_\text{bar}\ll g_\dagger$,
$g_\text{obs}\to\sqrt{g_\text{bar}g_\dagger}$ (flat curves, BTFR). The BTFR (T6) is the
deep-MOND limit of the RAR.

---

## Dimensional Match: The Scale $g_\dagger\sim cH_0$ — Reopened, Narrowed

**Unaffected: the dimensional statement.** $cH_0$ is the only acceleration formable
from the model's two characteristic quantities — this is forced by dimensional
analysis alone, independent of any counting law, and remains a necessary condition
shared by MOND and every cosmologically-motivated proposal, not a distinctive
prediction.

**Reopened: the specific coefficient.** cdot-4 read off $g_\dagger=c^2/R_0=cH_0/6$
from the occupancy law's clean horizon radius $R_0=6c/H_0$, matching observation to
$\sim6\%$. Connectivity counting (T23) has no single horizon-of-a-given-size — three
finite candidate lengths now exist ($L$, $R_\text{now}$, $D_p(\infty)$; T6/T14), and
$g_\dagger=c_0^2/\ell$ for the three misses $a_0$ by $2.83\times$, $2.04\times$, and
$1.63\times$ respectively — real progress from the initial "no finite length exists"
finding, but not resolved. See T6 and T14 for the full accounting; not repeated here.

---

## Status in This Model

**1. Scale.** $g_\dagger\sim cH_0$ — robust, inevitable, unaffected by the
counting-law change (dimensional analysis doesn't care which law generates the
history). The specific coefficient is open (above).

**2. Mechanism — confirmed unaffected.** The $\dot c/c$ retardation route is dead
(T5, re-verified explicitly for the new counting law): distance-keyed, not
acceleration-keyed, fails by $10^3$–$10^6$ at galactic scales using only
present-day $H_0,c_0$ and galactic distances — nothing here references cosmic
history. The **connecton foam-sea** (T14, confirmed unaffected) remains the leading
mechanism: Newtonian $1/r$ via diffusion through quantum foam, not distance-keyed. The
acceleration floor's *functional* identification as a kinematic scale survives; its
numerical coefficient is the open item above, not this mechanism.

**3. RAR closure — confirmed unaffected.** The constitutive law $D(g)=g/(g+g_\dagger)$
(MOND's "simple" interpolation) is derived from connecton indistinguishability — excess
connectons relaxing against the *total* ambient population, not against the excess
alone (T14, restated in full there). This derivation treats $g_\dagger$ as an external
parameter throughout; none of its four steps references $R_0$, $L$, or any
cosmological length. **The 0.020 dex match to McGaugh-Lelli-Schombert, and the
exclusion of the two alternative relaxation laws, stand exactly as in cdot-4.**

---

## The $\sqrt M$ Requirement

**Confirmed unaffected** — local force-law mathematics. The deep-MOND regime
$g_\text{obs}=\sqrt{g_\text{bar}g_\dagger}$ gives $g_\text{MOND}\propto\sqrt M/r$, MOND's
irreducible nonlinear signature, and the BTFR $v^4=GMg_\dagger$ follows directly. Any
direct-source mechanism linear in $M$ gives the wrong slope; the resolution (T14) is
that the quarter power comes from *where the surviving population sits*
($r_t\propto\sqrt M$), not the source coupling — the field equations stay linear. None
of this references the cosmological counting law.

---

## Relationship to T6 (MOND $a_0$) and T5 (Rotation Curves)

Unaffected in structure: the three problems remain at different stages, and progress
on the RAR (via connecton indistinguishability) remains independent of T5's dead
retardation route. T6/T14: $g_\dagger$'s coefficient reopened, narrowed to three
candidates (above). T15 (this document): closure functional form unaffected,
substantially derived. T5: retardation dead, attractor-convergence question open,
confirmed unaffected by the counting-law change.

**Open tension with PBH dark matter — unaffected, still open.** The RAR closure is
derived from baryons alone with no residual halo term; the project simultaneously
wants PBH dark matter at $\Omega_\text{PBH}\sim0.25$ in galactic halos (T13, T16). Not
reconciled here, exactly as in cdot-4 — see T5's discussion. T13's cdot-5 rewrite adds
one new wrinkle (an extrapolated $r_s/R$ exponent $n_\text{eff}\approx1.35$ for PBH
genesis) but does not touch this specific tension.

---

## Observational Discriminant: Epoch Dependence — Redone, With a New Subtlety

*This section changes substantively, not just numerically — it depends directly on
$H^\text{hor}(z)$'s functional form, which is different under connectivity counting,
and a genuinely new complication appears: the redshift range where this is
observationally tested straddles the percolation break itself.*

**The construction.** $g_\dagger$, read as a kinematic crossing-rate acceleration
$c(t)\times[c(t)/\ell]$ evaluated at epoch $t$ rather than fixed at today's value,
scales as $c(t)^2/\ell$ for whatever length $\ell$ sets the crossing distance. Of the
three candidates in play (above), **only $L$ is a natural choice for this specific
purpose**: $R_\text{now}$ and $D_p(\infty)$ are both defined with respect to *today*
and have no obvious meaning "evaluated as of an earlier epoch," whereas $L$ is, by
T23's own percolation construction, a fixed length frozen in at the moment of
percolation — it does not change with epoch by definition, making it the only one of
the three that can be substituted into a genuine $\ell(t)$ if needed, or held fixed if
not.

**Using $\ell=L$ (fixed):**
$$g_\dagger(z)=\frac{c(z)^2}{L}=g_\dagger(0)\,(1+z)^{-1}\qquad(z<z_*),$$
using $c(z)=c_0(1+z)^{-1/2}$ (T2, unaffected) — **a different exponent from cdot-4's
$(1+z)^{-5/6}$**, but the same sign: $g_\dagger(z)<g_\dagger(0)$ for $z>0$, so the MOND
threshold was smaller in the past, exactly as in cdot-4. The transition radius
$r_t=\sqrt{GM/g_\dagger}$ then scales as
$$r_t(z)=r_t(0)\,(1+z)^{+1/2}\qquad(z<z_*)$$
(cdot-4 had $+5/12$) — larger in the past, same direction, different magnitude. At
$z=1$: $g_\dagger$ down by $2\times$, $r_t$ up by $\sqrt2\approx1.41\times$
(cdot-4: down by $1.78\times$, up by $1.35\times$ — broadly comparable magnitudes,
not wildly different).

**The qualitative prediction survives, unaffected in direction:** high-$z$ disks are
more Newtonian/baryonic, with more steeply declining outer rotation curves and a lower
BTFR zero-point at fixed $M_\text{bar}$ — still qualitatively the direction of the
reported declining rotation curves at $z\sim1$–2.5 (Genzel et al. 2017; Lang et al.
2017), still a live, $\Lambda$CDM-orthogonal signature.

**The new subtlety.** This formula is derived for, and only valid within, the
post-percolation branch, $z<z_*\approx1.2$ (T23). The observational test range
($z\sim1$–2.5) **straddles the break** — roughly the lower half sits inside the
regime this calculation covers, the upper half does not. For $z>z_*$, $g_\dagger(z)$
would follow whatever the pre-percolation (occupancy) branch's own dynamics give,
which is not derived (T13, T16 — the same $q\approx1.37$-extrapolation uncertainty
that produced T16's CMB tension applies here too, though at a far less extreme
extrapolation distance: $z\sim2.5$ vs. the DESI fit's own $z\le2.33$ is barely an
extrapolation at all, unlike reaching to $z\approx1090$). **Practical consequence**:
predictions for the lower end of the Genzel/Lang sample ($z\lesssim1.2$) rest on a
reasonably solid footing (the post-percolation branch is well within its fitted
domain); predictions for the upper end ($z\gtrsim1.2$–2.5) are on shakier ground,
though not nearly as shaky as T16's CMB extrapolation.

**Caveat, unchanged from cdot-4 and still open:** this should be claimed cautiously —
pressure support and high gas dispersions are the mainstream explanation for the
observed decline, and this remains a *consistent-with*, not *uniquely-explained-by*,
signature.

---

## Open Questions

- **Force-law derivation of $g_\dagger$ and resolution of the three-candidate-length
  question** — superseding cdot-4's narrower framing; see T6, T14 for the full
  statement. This section's epoch-dependence result additionally depends on which
  length is correct: only the $\ell=L$ choice was used above because it is the only
  one of the three with an unambiguous meaning at earlier epochs; if a different
  length turns out to be physically correct, this section's exponents change again.
- **Transport kernel** — unaffected, unchanged from cdot-4: replacing the
  relaxation-time ansatz with a full Boltzmann derivation remains the deepening task.
- **Attractor convergence** — unaffected, unchanged from cdot-4 (T14, T17).
- **Epoch dependence beyond $z_*$** — new: does the pre-percolation branch's own
  (undetermined) dynamics give a $g_\dagger(z)$ that smoothly connects to the
  post-percolation $(1+z)^{-1}$ result at the break, or a discontinuity? Not examined;
  relevant to interpreting the upper half of the Genzel/Lang redshift range.
- **RAR scatter** — unaffected, unchanged from cdot-4: can the observed 0.13 dex
  scatter be predicted from the coherence-factor $f=v_\text{rot}/\sigma$ variation
  (T17)?
