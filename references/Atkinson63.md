# Reference Notes — Atkinson (1963), "General Relativity in Euclidean Terms"

**Citation:** R. d'E. Atkinson, "General Relativity in Euclidean Terms," *Proceedings of
the Royal Society of London. Series A, Mathematical and Physical Sciences*, Vol. 272,
No. 1348 (Feb. 19, 1963), pp. 60–78. Communicated by M. H. L. Pryce, F.R.S. Received 21
June 1962, revised 27 September 1962.

**JSTOR stable URL:** `http://links.jstor.org/sici?sici=0080-4630%2819630219%29272%3A1348%3C60%3AGRIET%3E2.0.CO%3B2-2`

**Source on disk:** `/mnt/data/roy/sync/docs/cosmology/Atkinson63.pdf` (scanned copy;
`pdftotext` fails on it — read directly via multimodal OCR instead). This notes file is
a citation aid and summary only, not a substitute for the source; go back to the PDF for
anything beyond what's captured here.

*These are working notes for the cdot project, not a full transcription (the paper
remains under copyright). Equations are reproduced where needed for technical reference;
everything else is paraphrase and summary.*

---

## What the paper actually does

Atkinson's aim is narrow and precisely scoped: show that every observable relativistic
prediction for a test particle and light ray near a **single stationary mass** can be
reproduced **exactly** — not approximately — starting from a strictly Euclidean 3-space
and an independent (Newtonian-style) time, provided the *local* speed of light and the
*local* rest mass of a test particle are allowed to vary with position according to two
specific rules. He is explicit that this is a matter of practical/conceptual convenience
between two mutually exclusive but equally self-consistent starting points (postulate
constant $c$ and infer curved space-time from measurement, or postulate Euclidean space
and infer how $c$ and rest mass "really" behave) — not a claim that curved-spacetime GR
is wrong. He restricts the entire treatment to one mass at rest and Einstein's vacuum
equations ($G_{\mu\nu}=0$), and states plainly that the paper assumes essentially nothing
about the *origin* of gravitation — no field equation sourcing $c_r$ or $\mu_r$ from a
mass distribution is given or attempted.

## Section-by-section notes

**§1 (pp. 60–62), motivation and setup.** Surveys earlier partial attempts (notably
Eddington 1920, who worked with a variable refractive index in Euclidean space but only
to first order) and frames the two "mutually exclusive lines of argument" mentioned
above. States the isotropic-coordinate Schwarzschild line element as the target to
reproduce:
$$ds^2=\left(\frac{1-\psi}{1+\psi}\right)^2c^2dt^2-(1+\psi)^4\left[dr^2+r^2(d\theta^2+\sin^2\theta\,d\phi^2)\right],\qquad \psi\equiv\frac{fM}{2rc^2},\tag{3}$$
where $f$ is Newton's constant and $M$ the central mass in grams; $\psi=1$ at the
Schwarzschild radius. This isotropic form is obtained from the standard Schwarzschild
form via $r_1=r(1+\psi)^2$.

**§2 (pp. 62–64), the target equations.** Derives (by standard means, from the geodesic
equations of (3)) the rigorous particle-motion equations (his eqs. 12, 15, 16) and the
light-deflection equation (his eq. 20) that any alternative derivation must reproduce.
Explicitly notes (p. 64) that *"nothing either new or even old is assumed (at least
expressly) about gravitation"* in what follows — the two postulates below are about
$c_r$ and $\mu_r$, not about a force law or a mass-sourcing mechanism.

**§3 (pp. 64–65), the two ad hoc postulates.** The core of the paper. First postulate,
for the local ("actual, Euclidean") speed of light at radius $r$:
$$c_r=\frac{1-\psi}{(1+\psi)^3}\,c.\tag{21}$$
Combined with a Snell's-law argument for a spherically-stratified refractive index, this
reproduces the light-bending equation (20) exactly. Working the deflection integral to
first order in $\psi$ recovers the standard $D\approx4m/r_0$ result (his eq. 30) — the
full relativistic bending, not the Newtonian half.

**§3 continued (pp. 65–68), the second postulate and the Lagrangian.** For a test
particle's rest mass at radius $r$ (moving with local velocity $v$, using $c_r$ as the
local speed-of-light limit):
$$\frac{\mu_r}{\mu}=\frac{(1+\psi)^5}{1-\psi}.\tag{35}$$
With ordinary special-relativistic total energy $H=\mu_r c_r^2(1-v^2/c_r^2)^{-1/2}$ and a
standard Lagrangian $L=\mathbf p\cdot\mathbf v-H$ built from these two postulates,
Atkinson shows by direct substitution that the resulting equations of motion (his eqs.
44–46, 51–55) are *identical* to the target geodesic equations (12), (15), (16) from
§2 — including the conservation of angular momentum and the full relativistic perihelion
advance, not just the Newtonian limit. He credits Pryce with supplying the specific
Lagrangian used.

**§3, generalization (p. 70).** Shows that a *family* of exponent choices,
$c_r=(1+\psi)^j(1-\psi)^kc$ and $\mu_r=(1+\psi)^l(1-\psi)^p\mu$, all reduce to ordinary
Newtonian $1/r^2$ gravity at leading order regardless of $j,k,l,p$ — the inverse-square
law is not sensitive to the specific exponents. Only the *combination* satisfying
$2(k-j)+(p-l)=2$ (from matching the deflection) *and* $l-p=6$ (from matching the mass
relation) reproduces the full relativistic corrections; (21) and (35) are the specific
solution used throughout.

**§3, redshift (pp. 70–71).** Derives the gravitational redshift two independent ways
— from an "ideal clock" flywheel lowered into the field, and from energy conservation of
an atom emitting a photon at radius $r$ — both giving
$$\frac{\nu_r}{\nu}=\frac{1-\psi}{1+\psi}\tag{17}$$
matching the isotropic-metric target exactly. Notes this second derivation needs
postulate (35) but not the conservation of angular momentum.

**§4 (pp. 71–74), measuring rods and the meaning of $r$.** A notable side result:
proves that "ideal, incompressible" measuring rods (infinite Young's modulus) are a
relativistic impossibility (a tetrahedron/pentahedron rigidity argument, credited by
Atkinson as new), and discusses how radial coordinates must in practice be fixed by
calibrated, in-situ measurement (etalon interferometry) rather than by laying out rigid
rods — because tidal forces distort any real rod, "ideal" rods included, in ways that
would make the space appear non-Euclidean even when it is defined to be Euclidean by
convention.

**§4 continued (pp. 74–78), clock synchronization and a worked example.** Discusses why
synchronizing clocks across the solar system by the two-planet method requires a
frame-symmetric (Euclidean/absolute-time) convention to avoid a real, measurable closing
error, and worimg out that convention's agreement with actual (Telstar-era)
inter-observatory clock comparisons. Closes with a fully worked example: deriving the
radius of a circular orbit ($r$, in the Euclidean sense) from quantities directly
measurable by a crew in that orbit (fringe counts from a Fabry-Pérot interferometer
observing a star, and the orbital period), his eq. (86) — offered as a concrete
demonstration that the Euclidean $r$ is not a free convention but a rigorously
determinable quantity, on exactly the same footing as $r_1$ is in the standard
relativistic treatment.

## Why this matters for cdot-6

- Atkinson's own scope is a **single static mass, one epoch, no time-dependence** —
  there is nothing here about cosmology, nothing about how $G$, $\mu$ (the $\psi=0$
  reference mass), or the reference light speed $c$ itself might evolve. Any
  cosmological application (cdot-6 Foundation §3) is an extension **beyond** what
  Atkinson derived or claimed, not something already in the paper.
- The two postulates (21) and (35) are explicitly labeled *ad hoc* by Atkinson — adopted
  because they work, not derived from a deeper mass-sourcing principle. He states
  outright that nothing is assumed about gravitation's origin. This is the opening
  cdot-6 exploits: later "Polarizable Vacuum" work (Puthoff) turned this into a genuine
  field theory with cosmological consequences (variable $G$, variable rest mass) that
  are independently excluded elsewhere in this project (LLR, the SN Hubble diagram) —
  but those consequences are Puthoff's addition, not Atkinson's own content.
- The generalization in §3 (p. 70) — that Newtonian gravity is insensitive to the
  specific exponents, only the relativistic corrections pin them down — is a useful
  fact to remember if cdot-6 ever needs to consider *different* exponents than (21)/(35)
  for its own cosmological extension.
