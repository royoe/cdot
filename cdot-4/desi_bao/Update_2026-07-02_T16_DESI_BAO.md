# Update to T16 — BAO in the Static Model: the DESI DR2 Confrontation (2026-07-02)

*Session type: constructive (adverse result). This update adds a BAO section to T16 and
reports the model's confrontation with the DESI DR2 BAO data — the sharpest
currently-available, candle-free geometric test. **Verdict, stated up front: the model
is excluded.** The full 13-point DR2 fit gives χ² = 150.9 against ΛCDM's 10.5
(Δχ² = +140 with one fewer parameter); the parameter-free Alcock–Paczyński test alone
gives χ² = 67.8 for six points with zero adjustable parameters; and a family-level
generalization shows the failure cannot be repaired by changing the counting exponents
without colliding with the supernova/age sector at ~7σ. Unlike the Pantheon+ tension
(T4), there is no candle systematic to appeal to: the exclusion applies directly to the
redshift–distance mapping, i.e., to premises 2 and 4. A serious collateral finding in
T4's time-dilation chain, discovered while validating which observables this test
depends on, is flagged in §8.*

---

## 1. What BAO Measures in a Static Model

In the static model, the acoustic feature imprinted at the recombination-analog epoch
is a **frozen proper length** $L$ (no expansion; structure retains its scale). The two
BAO observables are then purely geometric and spectroscopic:

- **Transverse:** the feature's angular size is $\theta = L/D_p(z)$ (straight-line
  propagation in the flat static map), so the pipeline's $D_M \equiv L/\theta = D_p(z)
  = R_0\big[1-(1+z)^{-1/6}\big]$, with $R_0 = 6c/H_0^\text{obs}$.
- **Radial:** the redshift extent of the feature is $\Delta z = L\,(dz/dD)$, so the
  pipeline's $D_H \equiv L/\Delta z = dD_M/dz = (c/H_0^\text{obs})(1+z)^{-7/6}$.

Two structural points. First, $D_H = dD_M/dz$ holds in *any* static model with a
monotonic $z(D)$ — exactly as it does in FRW — so the comparison is convention-clean.
Second, both observables are immune to photon-rate effects (§8): the transverse
measurement is geometry, the radial one is simultaneous spectroscopy. The sound-horizon
value $r_d$ is not computed by the model (T16's standing gap), so it enters as one free
nuisance parameter $A \equiv (c/H_0)/r_d$; the AP ratio $F_\text{AP} = D_M/D_H$ is
independent of it. DESI's published values are fiducial-cosmology-independent per the
DR2 papers.

## 2. Data

DESI DR2 (arXiv:2503.14738/14739): 13 measurements from 7 tracers, $0.295 \le z_\text{eff}
\le 2.330$ — BGS ($D_V/r_d = 7.942\pm0.075$ at $z=0.295$) plus six anisotropic tracers
(LRG1/LRG2/LRG3+ELG1/ELG2/QSO/Lyα) each giving $(D_M/r_d,\ D_H/r_d)$ with per-tracer
correlations $\rho_{M,H} \approx -0.40$ to $-0.46$ (ELG2, QSO correlations approximated
at $-0.44$, $-0.50$; results insensitive). Fractional precisions: 0.7–2.5%.

## 3. The Fit: Model vs ΛCDM

One-parameter model fit (per-tracer 2×2 covariances included):

| | χ² | points | params | best fit |
|---|---|---|---|---|
| **Static model** | **150.9** | 13 | 1 | $A = 35.19 \Rightarrow r_d = 121.7$ Mpc ($H_0{=}70$) |
| **Flat ΛCDM** | **10.5** | 13 | 2 | $\Omega_m = 0.297$ (matches published DESI 0.2975 — pipeline validated) |

$\Delta\chi^2 = +140$ with one fewer parameter — a ~12σ-equivalent exclusion. Per-bin
pulls at the model's best fit show the signature shape failure: $D_M$ pulled high at
low $z$ (+2.6, +3.6, +2.7σ), $D_H$ pulled hard low in the middle (−6.9σ at $z=0.934$,
−4.5σ at 1.321), $D_V$(BGS) at +7.1σ, with signs rotating by $z = 2.33$ — a
$z$-dependent anisotropy no normalization can absorb. (The required $r_d \approx 122$
Mpc, 17% below the standard 147 Mpc, is not itself the problem — the model has no
$r_d$ computation to contradict — the *shape* is.)

## 4. The Parameter-Free Kill: Alcock–Paczyński

$F_\text{AP} = D_M/D_H = 6\big[1-(1+z)^{-1/6}\big](1+z)^{7/6}$ — no free parameters at
all:

| tracer | $z$ | $F_\text{AP}^\text{obs}$ | σ | model | pull |
|---|---|---|---|---|---|
| LRG1 | 0.510 | 0.622 | 0.017 | 0.644 | +1.3 |
| LRG2 | 0.706 | 0.892 | 0.021 | 0.953 | +3.0 |
| LRG3+ELG1 | 0.934 | 1.223 | 0.019 | 1.348 | **+6.7** |
| ELG2 | 1.321 | 1.947 | 0.045 | 2.098 | +3.4 |
| QSO | 1.484 | 2.381 | 0.136 | 2.440 | +0.4 |
| Lyα | 2.330 | 4.517 | 0.097 | 4.436 | −0.8 |

**χ² = 67.8 for 6 points, zero parameters.** The same content viewed as a
required-ruler analysis: matching $D_M$ alone demands $r_d = 119$–126 Mpc while
matching $D_H$ alone demands 112–122 Mpc, with the two disagreeing by up to 10% *at the
same redshift* ($z=0.934$). No ruler evolution $L(z)$ can reconcile a transverse ruler
and a radial ruler that must be the same physical object — this is the AP statement
restated, and it forecloses escape route (b) below.

## 5. The Family-Level Result: the Exclusion Reaches the Premises

Every static counting model in this framework has the two-observable family
$$D_M/r_d = \tfrac{A}{\alpha}\big[1-(1+z)^{-\alpha}\big],\qquad
D_H/r_d = A(1+z)^{-(1+\alpha)},\qquad \alpha = \tfrac{1}{nP},$$
with $D_p = R_0 - R_e$ an exact consequence of the horizon growing at $c$. Fitting
$\alpha$ freely:

- Best fit: $\alpha = 0.095 \pm 0.010$, χ² = 102.8 (dof 11) — **still hopeless** vs
  ΛCDM's 10.5; the AP-only fit wants $\alpha \approx 0.05$ and still leaves χ² = 35.7.
- The model's $\alpha = 1/6$ sits **7.1σ** from even this least-bad member.
- The least-bad member requires $nP \approx 10.5$ — but $P = 2$ is pinned by the
  squared redshift law (mass invariance, T2/T4) and $n = 3$ by volume counting
  (premise 2), and $q_0 = \alpha$ ties to the SN/age sector. **No member of the family
  fits the BAO data, and the least-bad member contradicts the rest of the model.**

The general theorem behind this: in any static model, $F_\text{AP}(z)$ determines the
mapping completely via $D(z) \propto \exp\int dz/F_\text{AP}$. The data's
$F_\text{AP}$ run therefore *dictates* a redshift–distance mapping — and it is
ΛCDM's comoving-distance shape, which no horizon-counting solution
$R_0[1-(1+z)^{-\alpha}]$ reproduces. The exclusion is thus not of a parameter choice
but of the counting-law mapping itself: **premises 2 + 4 as currently constituted.**

## 6. Escape Routes, Honestly Assessed

1. **RSD / template systematics.** The only formally open route. DESI's BAO peak
   positions are reconstruction-hardened and fiducial-independent, with systematic
   budgets at the 0.1–0.5% level; the model needs biases up to **+10% in
   $F_\text{AP}$** at $z\approx0.93$ — a 20–100× larger systematic than the DESI
   budget. To claim it, the model must build its own full anisotropic clustering
   pipeline (its peculiar-velocity theory differs: $u \approx$ const, no Hubble drag).
   Formally open; not credible as stated.
2. **Ruler evolution $L(z)$.** Foreclosed by §4 (the radial/transverse required-ruler
   split at fixed $z$).
3. **Different counting exponents.** Foreclosed by §5 (family-level failure + 7σ
   collision with the SN/age sector).
4. **Abandon the horizon-counting mapping.** The only route that fits the data — and
   it is not an escape but a falsification of the cosmological sector as constituted.

## 7. Status Change

T16's verdict updates from "not yet dead" to: **the CMB question is now moot relative
to the BAO result — the model's geometric sector carries a candle-free,
calibration-light exclusion at Δχ² = +140.** Combined with Pantheon+ (T4,
Δχ² = +195, gated by the candle systematic), the expansion-history sector now has two
independent failures, and the new one has no candle-type escape. Per the program's own
falsifiability framing (Core §7: "the model lives or dies on the reality of cosmic
acceleration and the geometry it implies"), this is the death criterion being met in
the geometric channel, subject only to escape route 1.

**What this does and does not touch.** The local-gravity program (T14/T22: connecton
diffusion, the river, the RAR closure, the two-fluid structure) is logically
independent of the cosmological counting law — it requires a sea and a horizon scale,
not the specific $z(D)$ mapping. Those results stand or fall on their own tests
(ephemerides, Lense–Thirring, the entrainment law) and on whichever cosmology supplies
$g_\dagger \sim cH_0$. Likewise T20/T21's nuclear/weak-sector machinery is
mapping-independent. The falsification, if it stands, is of the static counting
cosmology — the program's MOND-derivation core is a separable survivor.

## 8. Collateral Finding (flagged, assigned out): T4's Time-Dilation Chain Omits Photon Arrival-Rate Compression

Discovered while establishing that the BAO observables are rate-immune. In a spatially
uniform medium with growing $c(t)$, two photons emitted $dt_e$ apart both travel at the
*same* $c(t)$ at all times, so their spatial gap is frozen at $c_e\,dt_e$ and is closed
at reception at $c_0$: the coordinate arrival interval is
$$dt_0 = dt_e\,(c_e/c_0) = dt_e\,(1+z)^{-1/2}$$
— an arrival-rate **compression** unique to VSL-in-static-space (the opposite of FRW's
stretching). T4's derivation ("arrival duration stretched by $(1+z)$") applies the
clock-rate ratio alone, implicitly setting $dt_0 = dt_e$. Including the compression:
observed light-curve dilation $= (1+z)\cdot(1+z)^{-1/2} = (1+z)^{1/2}$, and the
bolometric chain gives $D_L = (1+z)^{3/4}D_p$, not $(1+z)D_p$. The per-photon
*frequency* is unaffected (with $\omega$ conserved and $\lambda \propto c(t)$
stretching in flight, premise 4 and the squared redshift law survive; the compression
acts on photon *counting*, not photon energy). Consequences if confirmed: (i) the
predicted SN light-curve dilation exponent becomes 1/2 — against DES-SN's measured
exponent of 1 at sub-percent precision, an enormous independent exclusion; (ii) T4's
Hubble-diagram fit changes ($D_L$ exponent 3/4). **BAO (this update) is unaffected**
— spectroscopic $\Delta z$ and geometric $\theta$ involve no photon-rate bookkeeping.
This finding needs its own session: verify the kinematics against T2/T4's premises,
and re-derive the dilation and flux chains. It is potentially a second, independent
falsification of the cosmological sector — or a sign that photon propagation in the
model needs a premise-level statement it currently lacks.

## 9. Consolidated Edits

| # | File | Edit | Type |
|---|------|------|------|
| 1 | T16 | Add this BAO section (§1–§6); update the verdict per §7 | **Major adverse result** |
| 2 | Core §7 / status table | Record the BAO exclusion alongside the T4 tension; note the candle-free character and the premise-level reach | Status change |
| 3 | T4 | Cross-reference §5's α-collision (the BAO-preferred mapping contradicts the SN sector within the family) | Cross-link |
| 4 | T2/T4 | Open the §8 photon-compression finding as a top-priority consistency session (dilation exponent; $D_L$ chain) | **New major open item** |
| 5 | T22 §4 / T14 | Note the separability statement (§7): the local-gravity program's status is independent of this exclusion | Clarification |
| 6 | Test battery (pending T-doc) | Mark the DESI/AP row: executed, failed; chronometer-vs-BAO split now moot in its original form | Sync |

**Bottom line.** The DESI DR2 confrontation was the model's sharpest available test,
and the model fails it decisively: Δχ² = +140 overall, χ² = 68/6 points in the
zero-parameter AP channel, no ruler or exponent rescue available within the framework,
and the exclusion landing directly on the horizon-counting redshift–distance mapping.
The honest reading under the project's own ethos: the static counting cosmology, as
constituted, is falsified in its geometric sector pending only the (quantitatively
implausible) RSD-template escape — while the connecton local-gravity program, which
never depended on the mapping, separates cleanly and remains the framework's living
core. The collateral time-dilation finding (§8) should be resolved next: if it stands,
it independently confirms the same verdict through a completely different channel.
