
# T16 — The CMB Power Spectrum

*Note: this is the model's hardest observational constraint — the place where
alternative cosmologies most often fail. The analysis here is at the level of
qualitative ingredients and candidate mechanisms; no spectrum has been computed.
The path described below is a research program, not an answer.*

---

## Observational Background

The Cosmic Microwave Background (CMB) angular power spectrum is the tightest
quantitative success of $\Lambda$CDM. A six-parameter fit accounts for thousands
of multipoles at sub-percent residuals. For a static $c(t)$ model with $a = 1$,
the CMB is the hardest test on the table — harder than rotation curves, because
the baryon-photon acoustic physics is tightly quantitative and cannot be fudged.

The key features to explain:

1. **The near-perfect blackbody spectrum** ($T \approx 2.725$ K, deviations $< 10^{-5}$),
   implying genuine thermalization in an optically thick early phase.

2. **The acoustic peak structure.** The angular positions of the peaks encode the
   sound horizon at recombination (hence the angular-diameter distance to the
   last-scattering surface). The *relative heights* of the peaks encode the
   baryon-to-photon ratio and, crucially, whether pressureless dark matter is
   present before recombination.

3. **The third-to-first peak height ratio** is $\Lambda$CDM's cleanest argument
   for cold dark matter: photons oscillate; DM does not. More DM → deeper potential
   wells driving the photon-baryon fluid → enhanced odd peaks. The third peak being
   of comparable height to the first requires $\Omega_\text{DM} \approx 5\Omega_b$.

4. **The primordial power spectrum** ($n_s \approx 0.96$, nearly scale-invariant),
   attributed to inflation in $\Lambda$CDM.

---

## Translating the CMB: Four Ingredients

The CMB has four physically distinct ingredients. Each has a different status in
the model.

### (A) Thermal Origin

In $\Lambda$CDM the CMB is hot because $a$ was small — the photon gas was compressed
to high $T$ by metric contraction. In this model $a = 1$ always; there is no
compression heating.

The candidate translation: in the low-$c$ genesis epoch (T13) all energies scale
as $c^2$. "Recombination" becomes a **$c$-threshold** — the epoch when the atomic
binding energy ($\propto c^2$) equals the thermal bath energy ($\propto c^2$).
Since both scale identically, the threshold is not a temperature-drop event but a
$c$-value event. In principle this is translatable, but the mechanism is unworked.

### (B) Blackbody Thermalization

A near-perfect Planck spectrum requires genuine thermalization in an optically thick
early phase ($\tau_\text{opt} \gg 1$). In $\Lambda$CDM, the high photon density at
small $a$ ensures this. In the static model, the density at genesis must provide the
required optical depth from the model's own initial conditions (not from $a^{-3}$
compression). Whether the genesis density suffices is unworked and is noted as a
genuine difficulty.

### (C) Acoustic Peaks — The Crux

This is where the model's prospects are most interesting.

**The baryon-photon plasma physics.** The sound speed is:
$$c_s = \frac{c}{\sqrt{3(1 + R)}}, \quad R \equiv \frac{3\rho_b}{4\rho_\gamma}.$$

This is a *ratio* — it depends on $c$ only through $c_s/c = 1/\sqrt{3(1+R)}$, which
is dimensionless and depends only on the baryon-to-photon energy ratio $R$.

**The first peak's plasma physics is self-similar — but its angular position is a
decisive quantitative failure (2026-07-03 update).** Since every energy scales as $c^2$
(T1, T7, the relational principle), both $\rho_b \propto mc^2 \propto c^2$ and
$\rho_\gamma \propto h\nu \propto c^2$ scale identically. Therefore $R = 3\rho_b/(4\rho_\gamma)$
is invariant under the epoch-to-epoch $c$-scaling, and the plasma physics — oscillation
frequency, sound speed structure — is **self-similar** across epochs. That part of the
original claim stands. But *where the resulting peak lands in $\ell$-space* depends on
the model's own distance geometry, and working that out (see
`new_tests/Update_2026-07-03_CMB_First_Peak_Angular_Scale.md`) reverses the headline
conclusion:

- Using only formulas already adopted as "Core, stable" ($D_p(z)$, $D_A(z)$, Core
  §4/§4a — verified against Core's own worked table) plus the self-similar sound speed
  above, the predicted angular scale $\theta_s=r_s/D_A(z_\text{rec})$ falls short of
  what $\ell_1\approx220$ requires by **9$\times$ (S$'$) to 765$\times$ (volume law,
  the preferred branch)** at the observationally-labeled $z_\text{rec}\approx1090$.
- The gap **survives granting the model total freedom over the unresolved
  $z_\text{rec}$** (item A below): the best achievable $\ell_1$, optimizing over all
  possible recombination redshifts, is still only 9.5–67 depending on branch, at
  unphysical $z\sim2$–5 — never within an order of magnitude of 220.
- The invariant $R$ itself is not small: self-similarity pins it at today's measured
  value, $R\approx680$ (from $\Omega_bh^2$, $T_0$), at *every* epoch — not the
  $R\approx0.6$ $\Lambda$CDM needs at recombination, which only arises there because
  of differential $a^{-3}$ vs. $a^{-4}$ dilution that this static-space model lacks.
  Tuning $R$ upward to compensate is foreclosed: it would need $R\sim10^4$–$10^8$,
  inconsistent with the BBN $\eta\approx6\times10^{-10}$ input (T13).
- **Root cause**: the model's shallow $D_p\propto(1+z)^{-1/(nP)}$ distance law means
  $z\sim1090$ has already used up ~31% of the total light-travel budget (volume law),
  unlike $\Lambda$CDM where $a_\text{rec}/a_0\sim10^{-3}$ leaves three decades of
  expansion to compress the sound horizon to sub-degree scale. There is no comparable
  compression mechanism here.

This is now the sharpest quantitative, falsification-relevant tension in the model's
speculative program — on the model's own self-declared hardest test. It is **not**
treated as a terminal result: it is a leading-order geometric argument (no
Boltzmann-code line-of-sight treatment), and it remains open whether a static-$c(t)$-
appropriate redefinition of the sound-horizon-to-angle mapping could recover small
angular scales, rather than borrowing the FRW-style $D_A$ machinery wholesale. See the
update document for the full derivation, branch table, and caveats.

**The higher peaks require clustered, pressureless wells.** The third-to-first peak
height ratio is set by the amplitude of photon driving by pressureless (non-oscillating)
gravitational wells present before last scattering. A smooth, uniform gravitating
component has the wrong structure — it drives all modes equally and does not enhance
the odd peaks.

A pressureless component that is:
- gravitating ✓
- pressureless ✓
- present before recombination ✓
- and **clustered** (localized potential wells) ✓

is required. In $\Lambda$CDM this is cold dark matter. What does this model offer?

### (D) Primordial Spectral Index

$n_s \approx 0.96$ is attributed to inflationary quantum fluctuations in $\Lambda$CDM.
In this model it would need to emerge from genesis (T13). This is unworked and not
obviously forbidden; the model currently has no prediction for $n_s$.

---

## The PBH Candidate: Dark Matter = Primordial Black Holes

The clustered, pressureless wells needed for the higher peaks are a natural output of
primordial black hole (PBH) formation at genesis (T13).

**PBH properties vs. the CMB requirements:**

| Requirement | PBH status |
|---|---|
| Gravitating | ✓ (by construction) |
| Pressureless | ✓ (massive, non-relativistic after formation) |
| Present before recombination | ✓ if formed at genesis |
| Clustered / localized wells | ✓ (by construction — spatially localized) |

**The key difference from the connecton sea.** The connecton field (T14) is also
gravitating and pressureless, but it is horizon-smooth — it does not cluster into
localized wells. A smooth pressureless component cannot drive the third-to-first
peak height ratio. PBHs, by contrast, are inherently localized and provide the
required clustered structure.

**PBH triple duty.** If PBHs are formed at genesis, one population serves three
separate roles:

1. **CMB higher-peak wells** — as discussed above.
2. **Galactic dark matter** (T5, T15) — providing the missing mass for rotation
   curves and the RAR, which the connecton mechanism alone cannot explain.
3. **Supermassive BH seeds** — through early-universe PBH mergers (see below).

This reframes the model from "no dark matter" to "dark matter is primordial and
baryonic in origin" — a more defensible claim, distinct from the original no-DM
aspiration but arguably more coherent with the model's other components. The
density required, $\Omega_\text{PBH} \sim 0.25$, is observationally constrained
(microlensing, evaporation) but viable in specific mass windows (asteroid-mass
$\sim 10^{17}$–$10^{23}$ g, where evaporation is negligible and microlensing bounds
are loose).

---

## PBH Mergers and Supermassive Black Holes

JWST and quasar surveys find supermassive black holes with $M \sim 10^9 M_\odot$ at
$z > 10$ — earlier than standard stellar-seed accretion models can grow them. This is
an active tension in standard cosmology.

If genesis produces a PBH population, early-universe PBH mergers could build the seeds
for these supermassive BHs. The economy is significant: the same population that
provides CMB wells and galactic dark matter also resolves the early-SMBH problem,
converting a mainstream tension into a potential prediction of the model.

**Cross-link to the M-σ relation (T17).** If the central SMBH and the galactic dark
matter halo share a common PBH origin, the M-σ and M-$B_c$ connection (T17) has a
natural common source. Both the central BH and the halo wells would be remnants of the
same primordial PBH population, related by the initial mass distribution and merger
history.

**Honest caveats:**
- The merger rate in a varying-$c$ early universe is unworked.
- The mass budget is severe: going from asteroid-mass PBHs
  ($\sim 10^{-16} M_\odot$) to SMBHs ($10^6$–$10^9 M_\odot$) requires
  $10^{22}$–$10^{25}$ mergers per SMBH, requiring either a higher-mass PBH
  spectrum or extended hierarchical merging.
- This thread is speculative; it is recorded as a direction, not a result.

---

## The Load-Bearing Gate: PBH Formation at Genesis

All of the above — CMB wells, galactic DM, SMBH seeds — is gated by one question:
**does genesis actually produce PBHs?**

The relevant constraint comes from the ratio $r_s/R$, where $r_s = 2GM/c^2$ is the
Schwarzschild radius of the enclosed mass and $R$ is the horizon radius. From the
horizon dynamics with invariant G ($G \propto c^0$) and $M \propto R^3$:
$$\frac{r_s}{R} \propto R^{2-2n},$$
where $n$ is the counting-law exponent ($c \propto R^n$).

(Under cdot-3's $G \propto c^{-2}$, the exponent was $2-4n$. Under invariant G, it is $2-2n$.
For volume law $n=3$: exponent $= -4$, still $\to \infty$ as $R \to 0$. For surface law $n=2$: exponent $= -2$, still $\to \infty$.
For S′ $n=2/3$: exponent $= +2/3$, $r_s/R \to 0$ as $R \to 0$ — S′ loses the PBH genesis argument under invariant G.
The conclusion that the volume law retains PBH genesis (Reading 2) is unchanged.)

For $n > 1$ (which includes the volume law $n=3$ and surface law $n=2$, but NOT S′ $n=2/3$ under invariant G), this ratio
$\to \infty$ as $R \to 0$ — the early universe is always super-Schwarzschild.

Two readings:

- **Reading 1 (old):** a super-Schwarzschild early universe means all local regions
  are inside their own gravitational radii → PBH formation forbidden.
- **Reading 2 (preferred):** the early super-Schwarzschild universe is a
  black-hole-like reservoir. As the horizon grows, $r_s/R$ decreases through a
  crossover at $r_s/R \sim 1$. The average region exits the super-Schwarzschild
  state into a normal universe, while overdense lumps stay super-Schwarzschild and
  are left behind as black holes — frozen out as **relics** of the crossover.

Reading 2 is favored because it flips the same cutoff that Reading 1 called a
barrier into the PBH-formation mechanism. Crucially, this applies to the volume law
and surface law (both undergo the $r_s/R \sim 1$ crossover), so PBH formation does
not require the S′ variant — the volume law can have both the mildest $q_0$ tension
and PBH formation.

**The unproven step:** Reading 2 requires that an overdense lump, once the average
goes sub-Schwarzschild, cleanly collapses to a black hole rather than merely
remaining a denser patch. Whether the inhomogeneity does this work is the single
highest-leverage unproven claim in the speculative program — it gates the CMB,
galactic DM, and SMBH threads simultaneously.

---

## Current Status and Fit Assessment

The CMB is not yet addressed quantitatively by the model. The honest assessment:

| Ingredient | Status |
|---|---|
| (A) Thermal origin | Candidate: $c$-threshold recombination — unworked |
| (B) Blackbody thermalization | Genuine difficulty — requires genesis density check |
| (C) First acoustic peak, plasma shape | Self-similar $R$, sound speed — stands |
| (C) First acoustic peak, angular position | **Decisive quantitative failure — 9$\times$–765$\times$ short of $\ell_1\approx220$, robust to $z_\text{rec}$ and branch (2026-07-03)** |
| (C) Higher peak heights | PBH candidate — gated by PBH formation check, and by the same heavy ($R\approx680$) baryon-loading problem above |
| (D) Primordial $n_s$ | Unworked; would come from genesis |

The plasma-shape self-similarity is a genuine partial result, but the angular-position
calculation (2026-07-03) is a sharp negative one — the sharpest quantitative tension
in the model's speculative program, on its own hardest test. The PBH candidate for
higher peaks is promising but rests on unproven genesis dynamics and inherits the same
baryon-loading concern. The model is no longer merely "not yet dead on the CMB" — the
first-peak position is actively in tension with data, pending either a fix to the
static-geometry angle mapping or acceptance as a falsification point.

---

## Open Questions

- **Resolved, negative (2026-07-03):** ~~Can the self-similar baryon-photon plasma
  (first peak) be computed numerically in the model's $c(t)$ background? Is the
  predicted peak position consistent with the observed $\ell_1 \approx 220$?~~ No —
  the predicted angular scale is 9$\times$–765$\times$ short of what $\ell_1\approx220$
  requires, robustly across premise-2 branches and independent of the unresolved
  recombination redshift. See above and
  `new_tests/Update_2026-07-03_CMB_First_Peak_Angular_Scale.md`.
- **New, replacing it:** is there a definition of the sound-horizon-to-angle mapping
  appropriate to a static, coordinate-fixed $c(t)$ spacetime that differs from the
  borrowed FRW-style $D_A(z)$ construction — one that could recover small angular
  scales for early-universe features — or does this stand as a genuine falsification
  point for the model? This is now the single highest-priority open question for the
  CMB program, ahead of the PBH questions below (which govern peak *heights*, moot if
  peak *position* cannot be placed correctly).
- Does genesis produce PBHs? Does Reading 2's relic-freezeout picture actually
  yield black holes (versus denser patches) as the average goes sub-Schwarzschild?
  This remains the single highest-leverage open question for the dark-matter/SMBH
  side of the speculative program.
- What is the PBH mass function from genesis? Does it fall in the observationally
  allowed window ($\sim 10^{17}$–$10^{23}$ g for $\Omega_\text{PBH} \sim 0.25$)?
- What sets the primordial power spectrum $n_s$ in this model? Is there a mechanism
  analogous to inflation that produces a nearly scale-invariant spectrum?
- Can the blackbody thermalization requirement be met by the model's genesis density
  without compression heating? This requires computing the optical depth at the
  $c$-threshold epoch.
- The PBH merger channel to SMBHs: what is the merger rate and mass buildup in a
  varying-$c$ early universe? Does it produce $10^6$–$10^9 M_\odot$ seeds by $z \sim 10$?
- **Double-counting with the baryon-only RAR (T15).** This document's galactic-halo
  PBH clustering and T15's baryon-sourced RAR closure (0.020 dex, no halo residual)
  are not yet reconciled: quantifying the maximum $\Omega_\text{PBH}(r\lesssim30\,
  \text{kpc})$ compatible with the RAR scatter is an open, load-bearing question for
  whether the CMB-motivated PBH population can coexist with the galaxy-scale result
  (see T5, T6, T15).
