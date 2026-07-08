# Update — The Chandrasekhar Candle Check, and the Planck-Unit Invariance Principle (Open Items 1 and 7)

*Status: update document for cross-check and merge. Follows directly from
`Update-PhotonSector-2026-07-07.md` (same date), prompted by the author's suggestion to
check whether the Chandrasekhar mass's $c$-dependence can mitigate the SN Ia / EdS
conflict found there. Proposes: a new subsection for the flux/luminosity sector
(candle invariance), a reformulation of Foundation §3's framing, resolution of §6 item
7, and a substantial upgrade of §6 item 1. Produced 2026-07-07 (cdot-7, session
entry 5).*

**Summary.** The suggested mitigation — SN Ia peak luminosity tracks the Chandrasekhar
mass, $M_\text{Ch}\propto(\hbar c/G)^{3/2}m_H^{-2}$, which is $c$-dependent — was
checked and found unavailable in cdot-7: $M_\text{Ch}\propto c^{1/2}$, exactly premise
3's universal mass law, so the candle is epoch-invariant in local units. The failure is
not an accident of $s=\tfrac12$; the candle's drift exponent is *identical* to the LLR
cancellation exponent, so any candle evolution large enough to mimic acceleration
violates LLR by roughly two orders of magnitude, for every $(g,s)$. However, the check
surfaced a structural fact of independent and larger value: **the LLR-safety condition
is exactly the statement that the gravitational fine-structure constant
$\alpha_G=Gm_p^2/\hbar c$ is epoch-invariant**, and the single principle "all
dimensionless couplings are invariant" (equivalently: all local physics is constant in
Planck units) *derives* both $s=+\tfrac12$ and the auxiliary $\epsilon_0\propto c^{-1}$
— upgrading open item 1 and dissolving open item 7's tension.

---

## 1. The Chandrasekhar Mass in cdot-7

$$M_\text{Ch}\;\propto\;\frac{(\hbar c/G)^{3/2}}{m_H^{2}}
\;\propto\;\frac{c^{3/2}}{c^{1}}\;=\;c^{1/2},$$
using $\hbar,G$ invariant and $m_H\propto c^{1/2}$ (premise 3). So $M_\text{Ch}$ scales
with epoch **exactly as every rest mass does** — it is epoch-invariant in local mass
units, and the number of baryons in a Chandrasekhar-mass white dwarf,
$$N_\text{Ch}=\frac{M_\text{Ch}}{m_H}\;\propto\;\alpha_G^{-3/2},\qquad
\alpha_G\equiv\frac{Gm_p^2}{\hbar c}\;\propto\;c^{2s+g-1}\Big|_{(g,s)=(0,\frac12)}=c^{0},$$
is exactly constant. A white dwarf approaching collapse at $z=1$ contains the same
number of nucleons, with the same dimensionless structure, as one today. With the
photon-sector update's unit bookkeeping (energy unit $\propto c^{5/2}$, clock
$\propto c^{5/2}$), the peak luminosity in local units is therefore epoch-invariant:
**the standard candle is exactly standard, and the Chandrasekhar mitigation is
unavailable at cdot-7's adopted exponents.**

The same holds for the ingredients downstream of $M_\text{Ch}$, checked explicitly:
$^{56}$Ni energy release per nucleus in local energy units (all energy scales
$\propto mc^2\propto c^{5/2}$, dimensionless nuclear structure invariant — assuming the
strong sector scales like the mass sector, an extension of premise 3 flagged below);
ejecta velocities ($v/c$ invariant); Thomson opacity in local units
($\sigma_T/m_p\propto c^{-7/2}$, exactly the local area-per-mass unit); hence diffusion
times in local ticks. Every dimensionless ratio entering Arnett-rule physics is
epoch-invariant. The one unspecified sector is the weak interaction ($^{56}$Ni decays
by electron capture); the natural extension — weak dimensionless couplings invariant,
decay rates scaling as local clocks — is assumed here and flagged as such.

---

## 2. Why No $(g,s)$ Rescues It: Candle Drift *Is* LLR Drift

For general exponents ($G\propto c^{g}$, $m\propto c^{s}$), define
$E'\equiv g+2s-1$, the drift exponent of $\alpha_G\propto c^{E'}$ (note
$E'=-E_\text{LLR}$ of `ResearchNotes.md` §3's cancellation formula $E_\text{LLR}=1-2s-g$
— the same quantity up to sign). Then, taking the standard varying-constants assumption
$L\propto M_\text{Ch}$ (in local units, $L_\text{local}\propto N_\text{Ch}\propto
\alpha_G^{-3/2}$), and the general redshift law $1+z=(c_0/c_z)^{s+1}$:
$$\frac{L(z)}{L_0}=\left(\frac{c_z}{c_0}\right)^{-\frac32E'}=(1+z)^{\frac{3E'}{2(s+1)}}.$$
To mimic the observed SN Ia Hubble diagram against this framework's exact-EdS
prediction requires past SNe intrinsically dimmer by $\approx0.22$ mag at $z=0.5$ and
$\approx0.5$ mag at $z=1$ (approximate $\Lambda$CDM-vs-EdS residuals), i.e.
$L(z)/L_0\approx(1+z)^{-0.6\ \text{to}\ -0.7}$. At $s=\tfrac12$ this demands
$$E'\approx-0.6\ \text{to}\ -0.7.$$
But LLR safety demands $E'$ consistent with zero, and the combination of the LLR
range-rate bound with the direct $\dot G/G$ bound (which pins $g$ to $\lesssim0.4\%$ of
zero, `ResearchNotes.md` §3) confines $|E'|$ to at most the percent level. **The
required candle evolution exceeds the allowed dimensionless drift by roughly two orders
of magnitude, for every $(g,s)$ in the family.** This is not a numerical coincidence:
LLR (gravitational orbit against atomic clock) and the SN candle (gravitational
collapse mass against atomic energy scales) are *the same dimensionless comparison*,
$\alpha_G$ against the atomic sector, measured at $z=0$ and $z\sim1$ respectively. A
framework cannot drift one without drifting the other.

*Caveat, flagged honestly:* $L\propto M_\text{Ch}$ is the standard assumption of the
varying-$G$ SN literature but is model-dependent at the $O(1)$ level (the $^{56}$Ni
mass fraction's response to $M_\text{Ch}$ is debated). No plausible $O(1)$ revision
closes a two-order-of-magnitude gap, so the conclusion stands; the caveat matters only
if a mechanism *outside* the $\alpha_G$ channel is proposed.

---

## 3. The Positive Discovery: One Invariance Principle Behind $s=+\tfrac12$ *and* $\epsilon_0\propto c^{-1}$

The identity in §2 — LLR safety $\Leftrightarrow$ $\alpha_G$ invariance — reads in the
other direction as a *characterization* of the adopted exponents:

> **Given $G$ and $\hbar$ invariant, $s=+\tfrac12$ is the unique mass exponent for
> which the gravitational fine-structure constant $\alpha_G=Gm^2/\hbar c$ is
> epoch-invariant.**

Equivalently: the Planck mass $m_\text{Pl}=\sqrt{\hbar c/G}\propto c^{1/2}$ obeys
premise 3's law automatically, so premise 3 is precisely the statement that **all
masses are constant in Planck units**. And the same move covers the electromagnetic
sector: the Planck charge is $q_\text{Pl}=\sqrt{4\pi\epsilon_0\hbar c}$, and
$e/q_\text{Pl}=\sqrt{\alpha}$ is invariant *iff* $\epsilon_0\propto c^{-1}$ given
$e,\hbar$ fixed — which is exactly Foundation §3's auxiliary assumption.

So the two separately-postulated scaling laws are both consequences of a single
principle:

> **Planck-unit invariance:** all local physics — every dimensionless coupling
> ($\alpha$, $\alpha_G$, mass ratios, and by extension the strong and weak sectors) —
> is epoch-invariant; only $c(t)$ carries cosmological time-dependence, and the
> conventional choice of which dimensionful constants to hold fixed ($G,\hbar,e$) is a
> units convention, not physics.

Three consequences for the Foundation:

1. **Open item 7 is resolved by dissolution.** The flagged "tension" — masses scale as
   $c^{1/2}$ but $\epsilon_0$ as $c^{-1}$, so "all local physics scales the same way"
   is false as stated — was an artifact of the slogan. The correct statement is that
   all *dimensionless* physics is invariant; dimensionful quantities then scale with
   whatever (different) powers that requires. Both exponents follow from the one
   principle; there is nothing left to reconcile. Proposed: close item 7, rewrite
   premise 3's framing accordingly.
2. **Open item 1 is substantially upgraded, not closed.** $s=+\tfrac12$ moves from
   "adopted because it cancels LLR" (a fitted number — the move this project line has
   tried to avoid since T8) to "the unique exponent under Planck-unit invariance" (a
   symmetry statement). What remains owed is a *mechanism* for the symmetry — but that
   is the normal epistemic status of an invariance principle, a far better debt than an
   unexplained numerical coincidence. $\lambda$ remains fully underived.
3. **The principle retro-explains the framework's structural results** rather than
   merely surviving them: the exact LLR cancellation (§5.1), the exactly-standard
   candles (§1 above), the genericity of time dilation and distance duality found in
   the photon-sector update — all are instances of "dimensionless cross-sector
   comparisons cannot drift." It also makes clean falsifiable predictions at zero cost:
   no drift in $\alpha$ (atomic-clock bounds $\sim10^{-17}/\text{yr}$), in
   $\mu=m_p/m_e$, or in any laboratory dimensionless constant — all trivially satisfied
   at exactly zero, where generic varying-$c$ proposals must tune.

---

## 4. Consequences for the SN / EdS Problem, Stated Plainly

With Planck-unit invariance adopted, *every* locally-calibrated standard candle or
ruler — SNe Ia, Cepheids, TRGB, gravitational systems — is exactly standard across
epochs. The EdS degeneracy of the photon-sector update therefore stands with **no
astrophysical escape hatch**: the framework's conflict with the SN Ia Hubble diagram
(and the 9.3 Gyr age) cannot be attributed to candle evolution, in this framework, as a
matter of principle. The $\Lambda$-analog open item is now unavoidable and must come
from the cosmological closure itself or from a genuinely new sector — not from local
physics.

This also sharpens the correspondence question raised in the photon-sector update: with
the local sector exactly dual to standard physics by symmetry, and the photometric
sector exactly EdS, the framework's *only* loci of distinguishable physics are (a) the
AQUAL sector and its $a_0=\lambda c_0H_0^\text{hor}$ link — which standard cosmology
does not have — and (b) whatever modification of the closure supplies the
$\Lambda$-analog. Everything else is, demonstrably now rather than by assumption, a
change of description. This is worth recording in §0's methodological note at merge:
the framework's falsifiable content has been *localized*.

---

## 5. Proposed Merges

- **Foundation §3:** reframe the premise. Lead with the Planck-unit invariance
  principle; derive $m\propto c^{1/2}$ (from $\alpha_G$) and $\epsilon_0\propto c^{-1}$
  (from $\alpha$) as its consequences under the $G,\hbar,e$-fixed convention; state the
  convention as a convention. Keep the "adopted, not derived" flag but attach it to the
  principle, not the exponent.
- **Foundation §5 (flux/luminosity, new §5.5 from the photon-sector update):** add the
  candle-invariance result (§1–§2 above), including the two-orders-of-magnitude
  LLR-vs-SN exclusion and its $O(1)$ caveat.
- **Foundation §6 item 1:** rewrite — the debt is now a mechanism for Planck-unit
  invariance (plus $\lambda$), not a justification of a numerical exponent.
- **Foundation §6 item 7:** close, with the dissolution recorded.
- **Foundation §0:** note the localization of falsifiable content (§4 above).
- **ResearchNotes:** record the failed mitigation attempt (this document's §1–§2) per
  standing practice, so the Chandrasekhar route isn't retried, and the
  $E'$-vs-$E_\text{LLR}$ identity with its sign convention.
- **New assumption to log explicitly:** strong- and weak-sector dimensionless couplings
  invariant (used in §1's decay-rate and nuclear-energetics reasoning) — natural under
  the principle, but now load-bearing for the candle result.

---

## 6. Honest Ledger

Gained: the Chandrasekhar mitigation is decisively closed (better a clear "no" than a
lingering "maybe"); the LLR$\;\Leftrightarrow\;\alpha_G$ identity; a single invariance
principle replacing two unconnected postulates, resolving item 7 and upgrading item 1;
localization of the framework's distinguishable physics to the AQUAL sector and the
closure. Lost: the last plausible astrophysical escape from the SN Ia conflict — the
$\Lambda$-analog debt is now strictly a cosmological-sector problem, and the framework's
most falsified prediction has no remaining softening. The correct next target is
unambiguous.
