# Session Log Entry — 2026-07-07 (for merge as Entry 4 of `cdot-7/SessionLog-2026-07-07.md`)

## Entry 4 — Photon sector corrected; flux/luminosity sector built (open item 2)

**Prompt (verbatim):**
> This project has been revised substantially and is now in the cdot-7 iteration. Please check the current project documents and try to work on the open items.

**Summary:** Before working an open item directly, stress-tested the premises against
each other and found that §3.3's redshift law ("a photon's conserved frequency")
contradicts premise 1 + premise 2's own propagation kinematics: in static homogeneous
space every wave crest moves at the same instantaneous $c(t)$, so crest spacing
(wavelength) cannot change in flight — conserved frequency would require
position-dependent $c$, exactly the Atkinson-type structure cdot-7 dropped. Confirmed
independently by symmetry/wave mechanics (spatial homogeneity conserves $k$; broken
time-translation does not conserve $\omega=c(t)k$; adiabatic invariant conserves photon
number, so photon energy grows $\propto c$ in flight). Corrected redshift law:
$1+z=(c_0/c_z)^{3/2}$, i.e. $c_z=c_0(1+z)^{-2/3}$ — exponent equals the Bohr-radius
exponent, and the physical picture becomes "light doesn't stretch; the ruler shrank."

Consequences worked through (full derivations in the update document):
- **Time dilation:** exactly $(1+z)$, generically in $s$ (redshift and dilation are the
  same measurement under conserved $k$). Old law predicted $(1+z)^{3/5}$, excluded
  $\sim4\sigma$ by SN Ia spectral aging — so the correction is empirically mandatory,
  not just formal.
- **Rebuilt cosmological relations:** $w(z)=\tau[(1+z)^{1/6}-1]$,
  $D_p=R_{h,0}[1-(1+z)^{-1/2}]$, $H_0^\text{obs}=6/\tau=\tfrac32H_0^\text{hor}$ (ratio
  was $\tfrac52$; the closure-rebuild "robustness" of $H_0^\text{hor}$ does not survive
  a redshift-exponent change). Age $\to9.3$ Gyr (was 15.5), horizon $\to8.6$ Gpc,
  $a_0(\lambda{=}1)\to4.5\times10^{-10}$ m/s² ($\lambda\approx0.26$ to match, tension
  factor $\approx3.8$, was 2.3).
- **Flux/luminosity sector (open item 2) built:** two generic $(1+z)^{-1}$ flux factors
  give $d_L=(1+z)D_p$; shrinking bound systems ($r\propto c^{-3/2}$) were larger in the
  past by $(1+z)$, giving $d_A=D_p/(1+z)$ — hence Etherington duality
  $d_L=(1+z)^2d_A$ and Tolman $(1+z)^{-4}$ surface-brightness dimming hold *exactly*,
  both generic in $s$. These are the standard executioners of tired-light models; this
  framework passes them.
- **The headline result:** $d_L(z)=\frac{2c_0}{H_0}[(1+z)-\sqrt{1+z}]$ — *identical to
  Einstein–de Sitter at every $z$*, with $q_0=+\tfrac12$ and age $\tfrac{2}{3H_0}$.
  Every photometric/geometric observable computed so far coincides with $\Omega_m=1$.
  The framework therefore inherits EdS's two decisive failures: the SN Ia Hubble
  diagram (predicts high-$z$ SNe $\sim0.25$–$0.6$ mag too bright) and the age problem.
- **The failure is structural:** for general $s$, $q_0=(2-s)/(2(s+1))$, negative only
  for $s>2$ — which contradicts $\dot R_h=c>0$ (horizon would shrink), and LLR pins
  $s=\tfrac12$ anyway. No tuning of $s$ produces acceleration; the framework needs a
  $\Lambda$-analog via a modified closure or new sector. Proposed as the replacement
  for open item 2.
- **Open item 8 closed by reframing:** the lockstep shrinkage is unobservable in
  principle locally (LLR cancellation is the proof, not a special case); its only
  observable manifestation is the $(1+z)$ angular-size factor, i.e. it is subsumed
  into $d_A$.
- **Partial construction of §0's assumed correspondence** (photon sector $\leftrightarrow$
  EdS comoving frame), identifying in standard terms exactly what is missing: $\Lambda$.

Caveats flagged for cross-check before merge: the Blondin et al. (2008) dilation
constraint ($b\approx0.97\pm0.10$) and the SN magnitude offsets are quoted from memory
and should be verified against the literature; the precise SN comparison should be
recomputed against a current $\Lambda$CDM fit.

**Files produced:** `Update-PhotonSector-2026-07-07.md` (proposed replacements for
Foundation §3.3, §5.2, §5.3, §5.4; new §5.5; revised §6 items 1, 2, 7, 8; derivation
trail for ResearchNotes §8), this log entry.
