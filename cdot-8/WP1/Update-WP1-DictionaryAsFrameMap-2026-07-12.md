# Update — WP1: The Dictionary as a Frame Map

*Companion: `SessionLog-2026-07-12.md` (this directory). Executes Proposal §6 WP1:
"Derive K5's dictionary and the $3/2$ redshift law from $(g,A,\phi,\hat g)$ kinematics.
Success: exponents $3/2,5/2,p{-}7$ reproduced exactly. Kill: no disformal map
reproduces the photon sector." Grounded in the WP0 full-pass extraction of AeST's actual
action and FRW background equations (`cdot-8/WP0/`), re-verified here at the abstract/
equation level, not re-derived from memory.*

**Scope, stated first, per this project's own standing discipline (Foundation §0's
"deliberate scope boundary" test, applied here to WP1).** This work package is
*kinematic* only: it asks whether cdot-7's coordinate$\leftrightarrow$local dictionary
and redshift law can be recovered from AeST's field content and an FRW background,
given AeST's actual matter coupling. It does **not** ask why the background evolves the
way cdot-7's closure says it does (that is $\rho(a)$'s sourcing — the census, WP2, and
the closure constraint, WP3). The headline result below is, in fact, precisely that
these two questions are different in kind, and WP1 answers only the first.

---

## 0. A correction to the proposal's own language, established before deriving anything

Proposal §4 (M3) and §2 (K5) refer to "$\hat g$-proper quantities" and a frame map
built from $(g,A,\phi,\hat g)$ — presupposing a second, disformally-related metric
$\hat g_{\mu\nu}$ distinct from the gravitational metric $g_{\mu\nu}$, in the manner of
TeVeS ($\hat g_{\mu\nu}=e^{-2\phi}g_{\mu\nu}-2\sinh(2\phi)A_\mu A_\nu$, matter coupled to
$\hat g$, not $g$). **This is not how AeST is built.** The founding paper's action
(Skordis & Złośnik, PRL 127, 161302 (2021), arXiv:2007.00082, eq. 5) has a single matter
term $S_m[g]$, and the paper is explicit that this is a deliberate departure from TeVeS:
*"matter couples only to"* $g_{\mu\nu}$; the disformal transformation is named as
Sanders/Bekenstein's TeVeS mechanism specifically being **replaced**, and its removal is
presented as what fixes both the lensing problem (via the shear equation "remain[ing] as
in GR... since [photons] couple only to $g_{\mu\nu}$") and the GW170817 tensor-speed
constraint (no disformal admixture to push the tensor mode off $c$). **There is no
$\hat g$ in AeST.** Wherever the proposal's K5/M3 say "$\hat g$-proper quantities," read
"$g$-proper quantities" — AeST has one metric, and this derivation uses only it. This
is not a defect: it makes the WP1 kill condition ("no disformal map reproduces the
photon sector") easier to clear, not harder, since no disformal map is available or
needed (§5 below). Recommend this correction be carried into the next proposal
consolidation.

---

## 1. Setup: two frames, one metric

**The physical/proper frame.** AeST's matter sector, minimally coupled to $g_{\mu\nu}$
with $G,\hbar,e$ (hence $\alpha,\alpha_G$, all particle masses, all atomic transition
frequencies) strictly constant, is *ordinary* physics: nothing in a laboratory, an atom,
or a bound orbit varies with cosmic time. On the symmetric (FRW) background, $A^\mu=
\delta^\mu_t$ (the aether is exactly the cosmic-time-slicing congruence; verified
directly in both arXiv:2309.06232 and arXiv:2402.04091's FRW ansätze), so $Q\equiv
A^\mu\nabla_\mu\phi=\dot\phi$ in the $N=1$ gauge, and the physical scale factor $a(t)$
evolves according to AeST's own Friedmann equations (WP0 extraction, §2).

**The coordinate/bookkeeping frame.** cdot-7's "coordinate" quantities — $c(t)$, and
every $m(t),\ell(t),\nu(t),\rho(t)$ built from it — are, on this reading, **quantities
expressed in a Planck-unit system built from a running bookkeeping variable $c(t)$,
with $G,\hbar$ held at their true, constant values** (exactly cdot-7's own stated
convention, Foundation §3: *"the conventional choice of which dimensionful constants to
hold fixed ($G,\hbar,e$) is a units convention, not physics"* — this document takes
that sentence at face value and shows it is load-bearing, not throwaway). $c(t)$ itself
is not a claim about light propagation varying locally (§1's static-space premise
already disclaims that); it is the free parameter of a Dicke-type unit rescaling, whose
value is fixed, order by order, by requiring the rescaled description to reproduce
actual observables. **What follows is that fixing.**

---

## 2. M1 — the foliation, read off directly

No derivation is needed here beyond noting the identification: AeST's FRW cosmic time
$t$ (the aether-comoving congruence's proper time) *is* cdot-7's coordinate time; the
$t=\text{const}$ comoving spatial sections (flat, static *in comoving coordinates* —
which is what FRW spatial homogeneity always means) *are* cdot-7's "static Euclidean
space." Premise 1's "nothing expands" is, read this way, simply the standard comoving
description of FRW cosmology — a coordinate choice always available in ordinary
cosmology, not a novel claim. **M1 is confirmed, and the confirmation is trivial once
stated** — cdot-7's "static space, independent time" premise was comoving coordinates
all along; what it lacked, absent a metric theory underneath, was the rest of the
dictionary (§§3–5).

---

## 3. The Planck-unit relabeling — mass, length, frequency

For a **locally fixed** quantity $X$ (a particle's rest mass, an atom's Bohr radius, an
atomic transition frequency) with Planck dimension $[X]\propto G^a\hbar^b c^{n_X}$ ($G,
\hbar$ held fixed by convention), define the coordinate value as
$$X_\text{coord}(t)\ \equiv\ X_\text{phys}\times\left(\frac{c(t)}{c_0}\right)^{n_X},$$
i.e. "$X$ expressed in Planck units built from the running bookkeeping $c(t)$, with the
dimensionless ratio $X_\text{phys}/X_\text{Planck}$ *frozen at its own, genuinely
constant, physical value*." Since $m_\text{Pl}=\sqrt{\hbar c/G}\propto c^{1/2}$,
$\ell_\text{Pl}=\sqrt{\hbar G/c^3}\propto c^{-3/2}$, $t_\text{Pl}=\sqrt{\hbar G/c^5}
\propto c^{-5/2}$ (so $\nu_\text{Pl}\propto c^{+5/2}$):
$$m_\text{coord}(t)=m_0\!\left(\frac{c}{c_0}\right)^{1/2},\qquad
\ell_\text{coord}(t)=\ell_0\!\left(\frac{c}{c_0}\right)^{-3/2},\qquad
\nu_\text{coord}(t)=\nu_0\!\left(\frac{c}{c_0}\right)^{+5/2},$$
**exactly cdot-7 Foundation §3/§3.1's premise-3 exponents ($s=+\tfrac12$ for mass, the
Bohr-radius $c^{-3/2}$, the atomic frequency $c^{5/2}$) — now obtained as a direct
consequence of a stated convention (freeze $G,\hbar$; a physical quantity's own
Planck-unit ratio is trivially, boringly constant since every ingredient on both sides
is a true constant in AeST's matter sector) rather than adopted as an unexplained
scaling law.** $G_\text{coord}(t)=G_0$ follows immediately and trivially from the same
convention (holding $G$ fixed is the *input*, not a derived result) — this is exactly
cdot-7's own stated $G(t)=G_0$, now visibly a choice rather than a mystery.

**What this section does and does not establish.** This is a *bookkeeping identity*: it
shows the scheme is internally consistent and reproduces cdot-7's exponents for objects
whose *physical* properties are genuinely time-independent. It does not yet connect
$c(t)$ to anything physically measured — that requires the redshift law, §4, which is
where the scheme either does or doesn't survive contact with an actual observable.

---

## 4. The redshift law — where the bookkeeping choice is forced, not free

**cdot-7's own derivation (Foundation §3.3) reproduces its redshift law from wavenumber
conservation and $\nu_\text{atom}\propto c^{5/2}$ alone, for *any* function $c(t)$** —
substituting §3's steps: $\lambda_\gamma=c(t_e)/\nu_\text{atom}(t_e)\propto c_z^{-3/2}$
(conserved in flight), $\omega_\text{rec}=c_0k\propto c_0c_z^{3/2}$, compared against
$\nu_\text{atom}(t_0)\propto c_0^{5/2}$, gives $1+z=(c_0/c_z)^{3/2}$ identically,
regardless of how $c(t)$ relates to the true scale factor $a(t)$. **This is the point at
which the bookkeeping scheme stops being free.** The *actual*, physical redshift a real
detector measures — computed directly from AeST's null geodesics of the single metric
$g_{\mu\nu}$, with photons minimally coupled — is the ordinary $1+z=a_0/a_e$. Requiring
cdot-7's internally-consistent bookkeeping redshift to equal this physical one:
$$\left(\frac{c_0}{c_z}\right)^{3/2}=\frac{a_0}{a_e}\quad\Longrightarrow\quad
\boxed{\,c(t)=c_0\left(\frac{a(t)}{a_0}\right)^{2/3}\,}$$
is **forced**, with no remaining freedom. This is the one genuinely new physical input
this derivation supplies: cdot-7's $c(t)$ *is* the scale factor, raised to the $2/3$
power, and nothing else could have worked.

**A strong, independent cross-check.** Differentiating, $\dot c/c=\tfrac23(\dot a/a)=
\tfrac23H$. cdot-7 Foundation §2.2 already derived, from its own closure dynamics and
independent of this exercise, $H_0^\text{obs}=\tfrac32\dot c_0/c_0$ — i.e. exactly
$\dot c_0/c_0=\tfrac23H_0^\text{obs}$. **This is the identical relation**, obtained here
from AeST kinematics alone with zero reference to cdot-7's own closure. This is a
genuine, non-trivial consistency check passed, not built in by construction — the
proposal's own K5 flagged the $\tfrac32$ redshift exponent as "used but flagged, to be
re-derived"; it is now derived, and it independently reproduces a relation cdot-7 needed
elsewhere for unrelated reasons.

---

## 5. The density map, $p\to p-7$ — a corollary, not a separate fact

Coordinate energy density for a species with fixed comoving number density $n_\text{com}$
and coordinate per-particle energy $E_\text{coord}(t)\propto c(t)^{q}$ is $u_\text{coord}
(t)=u_0(c/c_0)^{q}\equiv u_0(c/c_0)^p$. Two cases, checked directly against actual AeST/
FRW physics (not assumed):

- **Matter.** $E_{m,\text{coord}}=m_\text{coord}(t)\cdot c(t)^2\propto c^{1/2+2}=c^{5/2}$
  ($p=5/2$, §3's mass exponent plus the bookkeeping "$c^2$" of $E=mc^2$ built the same
  way). Physical energy density: $u_{m,\text{phys}}(t)=n_0m_\text{phys}c_*^2(a_0/a)^3$
  (ordinary matter dilution, a true AeST/FRW fact, $c_*$ the true, constant light
  speed). Substituting $a/a_0=(c/c_0)^{3/2}$ (inverting §4's boxed relation):
  $u_{m,\text{phys}}\propto(c/c_0)^{-9/2}$. **$p-7=5/2-7=-9/2$ — exact match.**
- **Radiation.** $E_{\gamma,\text{coord}}=\hbar k c(t)\propto c^1$ ($p=1$, $k$ the
  conserved comoving wavenumber). Physical energy density: photon number dilutes as
  $a^{-3}$ *and* each photon's physical energy redshifts as $a^{-1}$ (an independent,
  ordinary null-geodesic fact), giving $u_{\gamma,\text{phys}}\propto a^{-4}\propto
  (c/c_0)^{-6}$. **$p-7=1-7=-6$ — exact match.**

**Both cases check out because they are not two separate coincidences — they are the
same relabeling identity applied twice.** Once §4's tie $c\propto a^{2/3}$ is fixed by
the redshift requirement, *every* correctly-computed relation between coordinate and
physical quantities is guaranteed to match, by the elementary fact that a self-consistent
change of units cannot alter any relation between physically measurable quantities — it
can only relabel them. cdot-7 Foundation §2.4 found both exponents by direct computation
and called them *"two independent hits on exponents not fitted to produce them"*; WP1
shows they were never independent — they are one theorem (§4's boxed relation) wearing
two species' clothing.

**A bonus discharge.** cdot-7 Foundation §2.1/§6 item 9 lists *"space is homogeneous...
[and comoving number density is] assumed, not derived"* as an open debt. §5's matter
case used ordinary comoving particle-number conservation ($n\,a^3=\text{const}$) — the
standard FRW continuity equation for a pressureless, conserved species, a theorem given
an FRW background and conserved particle number, not a free assumption. **Item 9 is
discharged, on the same footing standard cosmology's own homogeneity assumption always
stands on** (justified empirically, e.g. by CMB isotropy, not derived from nothing) —
cdot-7 is no worse off here than $\Lambda$CDM.

---

## 6. What this derivation shows, stated as plainly as the result deserves

**At the kinematic level, cdot-7's entire "variable $c$, Planck-unit-invariant local
physics" apparatus is exactly equivalent to ordinary FRW cosmology with genuinely fixed
local physics, related by one Dicke-type unit rescaling with exponent fixed by the
redshift law.** This is not a weakness particular to today's check — it is cdot-7's own
"methodological note on scope" (Foundation §0: *"the correspondence... has been
partially constructed... not merely assumed"*) made fully rigorous and complete, at
least for the photon/units sector. The corollary, stated as directly as the historical
record (`cdot-8/WP0/Update-WP0-FullPass-2026-07-11.md`, Part A) already anticipates:
**cdot-7's distinctive physical content was never in the existence of a "variable $c$"
as such — that is bookkeeping, full stop — it is entirely in the *dynamics*: the
specific closure ($c^2=\kappa g_hR_h$, the census, the AQUAL $a_0=\lambda\dot c$
portal) that determines what $a(t)$ actually does.** WP1 does not touch that; it
confirms the translation dictionary connecting whatever $a(t)$ the dynamics produces to
cdot-7's coordinate description is valid and, in fact, forced. The genuinely open,
novel physics is entirely WP2 (the covariant census as a foliation integral) through
WP4 (the $\Lambda$-analog) — exactly as the proposal's own §5 ("what is genuinely
novel") already says, now with the kinematic half of the proposal's own hedge removed.

---

## 7. M2's status — appropriately out of WP1's scope

The proposal's M2 ($a_0=\lambda\dot c\leftrightarrow Q_0(t)$, with $Q_0$ fixed by the
census closure) is a **dynamical** statement — it requires knowing how $Q$ (or $F(Q)$)
sources $H$ through AeST's actual Friedmann equations (WP0 extraction: $H^2+k/a^2=
\tfrac{8\pi\tilde G}{3}\rho-\tfrac13(F-QF_Q)+\Lambda/3$, with $F_Q\propto a^{-3}$ from
the scalar's own equation of motion). §4 above gives $\dot c/c=\tfrac23H$ unconditionally
(a kinematic fact, independent of what sources $H$); *identifying* this $H$ with a
specific combination of $Q_0$ via the census-closure constraint is precisely WP2/WP3's
content, not WP1's. Recorded here so M2 is not mistakenly treated as discharged by this
pass — it is untouched, correctly deferred.

---

## 8. Success/kill verdict

**Proposal §6 WP1 success condition — exponents $\tfrac32,\tfrac52,p{-}7$ reproduced
exactly — is met**, along with the mass ($\tfrac12$) and length ($-\tfrac32$) exponents
not separately named in the success condition but part of the same K5 dictionary.
**Kill condition — no disformal map reproduces the photon sector — does not trigger,
and is in fact moot**: no disformal map was available (§0) or needed; the single-metric
AeST kinematics reproduces the photon sector exactly with a *simpler* mechanism than
the proposal anticipated. **Recommend promoting WP1 to passed and proceeding to WP2**,
carrying forward: (i) the $\hat g\to g$ correction (§0) into K5/M3's wording; (ii) the
$c(t)=c_0(a(t)/a_0)^{2/3}$ relation as a load-bearing, re-derivable identity for WP2's
own foliation integral (the census $\mathcal N(t)$ will need to be expressed on
$\Sigma_t$ in terms of the same $a(t)$); (iii) the explicit statement that cdot-7's
kinematic content is fully accounted for, so WP2–WP4's success is now the *entire*
remaining test of cdot-8's worth.

**Caveat on what this derivation did and did not depend on.** Every load-bearing step
above used only: (a) AeST's matter sector minimally coupled to $g_{\mu\nu}$ alone (high
confidence — direct quotes, not a paraphrase); (b) the generic FRW/aether-comoving
ansatz $A^\mu=\delta^\mu_t$ (a symmetry statement, not paper-specific); (c) ordinary
Planck-unit dimensional analysis. **None of it depended on the AeST action's specific
free parameter $K_B$ or the precise form of $F(Y,Q)$**, where WP0's extraction flagged
possible ar5iv sign/coefficient transcription risk — so this result is robust to that
flagged uncertainty. What *is* still adopted, not derived, exactly as in ordinary
cosmology: FRW spatial homogeneity itself (§6 above already states this is on par with,
not worse than, $\Lambda$CDM's own homogeneity assumption).
