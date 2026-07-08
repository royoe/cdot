# Consolidation Map — Merging Session 2026-07-07 (Entries 4–9) into the cdot-7 Foundation

*Status: merge guide, not new physics. Cross-check each update document against this
map when consolidating. Update documents in dependency order:
`Update-PhotonSector`, `Update-ChandrasekharCandle`, `Update-AqualAlignment`,
`Update-ClosureRebuild`, `Update-A0Evolution-Confrontation`,
`Update-PreConsolidation` (all dated 2026-07-07). Code artifacts:
`closure_dynamics.py`, `a0_confrontation.py`.*

---

## 1. Section-by-Section Merge Map

| Foundation section | Action | Source |
|---|---|---|
| §0 Purpose/scope | Amend: correspondence partially *constructed* (photon sector ↔ EdS; asymptotic future ↔ de Sitter); falsifiable content localized to the $\dot c$ portal; scope-limit to $z\ll z_\text{eq}$ | PhotonSector §7; ClosureRebuild §5; Chandrasekhar §4; PreConsolidation §3 |
| §1 Premise 1 | Unchanged | — |
| §2.1 | Unchanged in substance | — |
| §2.2 | **Replace**: algebraic Sciama closure → the 2D dynamical system; old solution renamed "the fixed-point solution"; record closure-form decision ($c^2=\kappa g_hR_h$) and $\kappa\lambda$ degeneracy; genesis structure (backward attractor) unchanged | ClosureRebuild §1–2 |
| §2.3 | Unchanged | — |
| §3 preamble | **Reframe**: lead with the Planck-unit invariance principle; derive $m\propto c^{1/2}$ (from $\alpha_G$) and $\epsilon_0\propto c^{-1}$ (from $\alpha$) as consequences; "adopted, not derived" flag moves to the principle | Chandrasekhar §3 |
| §3.1, §3.2 | Unchanged | — |
| §3.3 | **Replace**: conserved wavelength, $1+z=(c_0/c_z)^{3/2}$; record the old conserved-frequency law's inconsistency in ResearchNotes | PhotonSector §1–2 |
| §3.4 | Keep; append the invariance-principle upgrade of the $s$-debt | Chandrasekhar §3 |
| §4 | **Rewrite**: $a_0(t)=\lambda\dot c(t)$; portal framing; frozen-$a_0$ reading rejected; note premise 2/4 inconsistency found and resolved | AqualAlignment §1–3; ClosureRebuild |
| §5.1 | Add caveat: exactness is $\mu{=}1$-sector; high-$x$ residuals constrain $\mu$ | AqualAlignment §4 |
| §5.2 | **Recompute**: fixed-point relations with exponent $3/2$; trajectory values for observables; see §2 below for every stale number | PhotonSector §4; ClosureRebuild §4 |
| §5.3 | Update: $a_0(\lambda{=}1)=4.5\times10^{-10}$; $\lambda\approx0.26$ (twice-measured); Lemma 1 (trajectory-invariance of today's $a_0$) | PhotonSector; AqualAlignment; PreConsolidation §4 |
| §5.4 | **Replace** with the reframing (locally unobservable in the $\mu{=}1$ sector; deep-MOND drift $\hat r\propto c^{9/16}$; observable as $\hat a_0(z)$) | PhotonSector §6.2; AqualAlignment §2.2 |
| §5.5 (new) | Flux/luminosity sector; candle invariance; working cosmology (fiducial trajectory, fit table); $d_L,d_A$, duality, Tolman; DES time dilation ($b=1.003\pm0.005\pm0.010$, replaces Blondin); thermal sector; $\hat a_0(z)$ prediction + MUSE-DARK III confrontation; BTFR/M–σ evolution channels | PhotonSector §5; Chandrasekhar §1–2; ClosureRebuild §4–5; A0Confrontation; PreConsolidation §1–2, §4 |
| §6 | **Rewrite** per §3 below | all |
| SessionLog | Append entries 4–9 | log entry files |
| ResearchNotes | New sections: photon-sector derivation trail (incl. superseded law), invariance principle, closure perturbation/cosmography algebra, dead $\lambda$-derivation hope, confrontation table + chronology note, thermal derivation, DES citation update; archive both code files | all |

## 2. Stale-Number Checklist (every instance must be updated)

| Quantity | Old (pre-session) | New |
|---|---|---|
| Redshift law | $c_z=c_0(1+z)^{-2/5}$ | $c_z=c_0(1+z)^{-2/3}$ |
| Redshift exponent | $5/2$ | $3/2$ |
| $H_0^\text{obs}/H_0^\text{hor}$ | $5/2$ | $3/2$ |
| $w(z)$ | $\tau[(1+z)^{1/10}-1]$ | $\tau[(1+z)^{1/6}-1]$ (fixed point) |
| $D_p(z)$ | $R_{h,0}[1-(1+z)^{-3/10}]$ | $R_{h,0}[1-(1+z)^{-1/2}]$ (fixed point) |
| Proper age | 15.5 Gyr | **13.0 Gyr** (trajectory); 9.3 Gyr (fixed point, superseded) |
| Particle horizon $R_{h,0}$ | 14.3 Gpc | **$\approx13.2$ Gpc** (trajectory, $=3.07\,c_0/H_0$); 8.6 Gpc (fixed point) |
| $q_0$ | not derived | **$-0.68$** (trajectory); $+1/2$ (fixed point) |
| $a_0(\lambda{=}1)$ | $2.7\times10^{-10}$ m/s² | $4.5\times10^{-10}$ m/s² |
| $\lambda$ to match $a_0$ | 0.44 | **0.26** |
| "$H_0^\text{hor},a_0$ robust to closure rebuild" claim (§5.2/§5.3) | as stated | **Overturned** by the redshift-law correction; superseded by Lemma 1 (today's $a_0$ depends only on $H_0^\text{obs},\lambda$ — trajectory-invariant) |
| SN dilation constraint | Blondin $b=0.97\pm0.10$ | DES $b=1.003\pm0.005\pm0.010$ |

## 3. Final Open-Items List (proposed §6)

**Resolved this session** (record, then strike): flux/luminosity sector (old item 2 —
built); EM-sector tension (old item 7 — dissolved by the invariance principle);
directional-prediction dataset hunt (old item 8 — reframed into $d_A$/$\hat a_0(z)$);
the premise 2/4 inconsistency (found and resolved within the session); the Blondin
verification caveat.

**Open, in priority:**
1. **Joint statistical fit** — SN compilation + binned $a_0(z)$
   (SPARC/MIGHTEE/MUSE-DARK, zero-point nuisances) + local RAR, over
   $(\varepsilon_0,\kappa\lambda,\mu)$. The decisive near-term test; the framework
   has ~one shape degree of freedom left after the SN fit. Includes resolving the
   15–20% $a_0(z)$ amplitude residual and the MIGHTEE zero-point puzzle.
2. **Origin and amplitude of the seed $\varepsilon_0$** — the $\Omega_\Lambda$-value
   analog; what perturbs the fixed point, and why passage through the few-percent
   range coincides with stellar-age epochs.
3. **Mechanism for the Planck-unit invariance principle** (successor to "derive
   $s$"); with it, a derivation of $\lambda$ (twice-measured, never derived) and a
   determination of $\kappa$ (currently set to 1 by fiat).
4. **Radiation-era closure** (new) — include radiation energy in the Machian source;
   prerequisite for BBN, $z_\text{eq}$, and all CMB-era physics; until then every
   cosmological statement is scope-limited to the matter era.
5. **Perturbation/structure sector** — BAO, CMB anisotropies, growth of structure;
   the enhanced early $\hat a_0$ (helpful direction for early massive galaxies) is
   motivation, not a result.
6. **Relativistic completion** — untouched this session and now more urgent: the
   lensing-RAR channel proposed for item 1's successors *requires* a prediction for
   light bending, which the framework still lacks entirely.
7. **Finalize $\mu(x)$** — simple form currently favored by the SN residual shape and
   consistent with the RAR; high-$x$ asymptotics constrained by LLR precision.
8. **Homogeneity of $n$** — unchanged from the original list.

## 4. Terminology to Standardize at Merge

"Fixed-point solution" (the EdS-equivalent scale-free history) vs "the trajectory"
(the fitted $\varepsilon_0=-0.0627$ history); "the portal" ($a_0=\lambda\dot c$ as
the unique sanctioned breach of Planck-unit invariance); $\tilde\lambda\equiv
\kappa\lambda$ where the degeneracy matters; $\nu_*$ (log-slope of $\mu$ at $x_*$);
$\hat{\ }$ for quantities in local units.
