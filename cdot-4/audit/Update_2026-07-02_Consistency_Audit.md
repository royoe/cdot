# Update — Full-Repository Consistency Audit (2026-07-02)

*Session type: consistency audit across Core Principles and T1–T21. All 22 documents were
read in full; key numerical claims were independently re-computed. This update lists (I)
confirmed-consistent results, (II) concrete inconsistencies requiring edits, ordered by
severity, with proposed corrections, and (III) two structural tensions that are not mere
documentation errors and need a substantive resolution in a future session.*

---

## I. What Checks Out (independently verified)

The following load-bearing chains were re-derived or numerically re-checked and are
internally consistent across all documents that use them:

- **The c(τ) map and age.** $\tau_\infty = 3/(2H_0^{\text{obs}}) = 20.95$ Gyr ($H_0=70$);
  $c(\tau)/c_0 = (1-\tau/\tau_\infty)^{3/4}$ (T20) is an exact restatement of T1's
  solution — verified ($c(4.5\,\text{Gyr})/c_0 = 0.834$, matching T18's 0.84 and T21's
  table). T1's lookback table, Core §4a's τ column, and T20/T21's tables all agree.
- **The two-Hubble-constant bookkeeping.** $H_0^{\text{obs}} = P\,H_0^{\text{hor}}$,
  $R_0 = 3Pc_0/H_0^{\text{obs}} = 25.7$ Gpc, and the derived coefficient
  $g_\dagger = c^2/R_0 = cH_0^{\text{obs}}/6 = 1.13\times10^{-10}$ m/s² are used
  consistently in Core, T3, T6, T14, T15, T19. T19's alternative form
  $g_\dagger = cH^{\text{hor}}/3$ is equivalent. ✓
- **Distance/redshift pipeline.** $D_p(1)=0.1091R_0=2804$ Mpc, $D_L=5607$ Mpc,
  $\Delta\mu(z{=}1)=-0.36$ — Core §4a table and T4 agree. Etherington relation exact. ✓
- **T20 ceiling algebra.** $M_\text{Ch}(\tau)/M_{\text{Ch},0}=(1-\tau/\tau_\infty)^{9/8}$
  and the inverse ceiling formula verified; spot-check $\tau_\text{ceiling}(1.20\,M_\odot;
  1.40) = 2.68$ Gyr reproduces the table. ✓
- **T21 dimensional restorations.** $\Gamma_\text{weak}\propto G_F^2(Qc^2)^5/(\hbar^7c^6)
  \propto c^4$ and $\Gamma_\text{plasmon}\propto c^{-1}$ (fixed density) both check
  dimensionally and in exponent-tracking. The Mestel conversion $\Delta A/A\approx(5/2)\delta$
  checks. The plasmon-enhancement table matches the c(τ) map. ✓
- **Epoch-dependence scalings.** $g_\dagger(z)\propto(1+z)^{-5/6}$ (T15) re-derived from
  $c\propto(1+z)^{-1/2}$, $R\propto c^{1/3}$; T19's derived chain ($v_f\propto(1+z)^{-5/24}$,
  $r_t\propto(1+z)^{+5/12}$, $\omega_L^2\propto(1+z)^{-5/12}$) is consistent with it. ✓
- **T14 closure algebra.** $g_x(g_x+g_\text{bar})=g_\text{bar}g_\dagger$ gives MOND's simple
  interpolation; crossover $g_x=g_\text{bar}$ at $g_\text{bar}=g_\dagger/2$; T19's
  $g_x/g_\text{bar}=1/\varphi$ at $g_\text{bar}=g_\dagger$ is the same equation evaluated at
  a different point — no contradiction. ✓
- **T8 LLR budget.** The three-effect decomposition ($+2H, -H, +2H$ → $3H_0^{\text{hor}}
  = \tfrac{3}{2}H_0^{\text{obs}}$) and the ×717–720 verdict are internally consistent. ✓
- **T4 magnitude bound.** $E_\text{total}\propto c^{7/2}$ → $\Delta m = 4.375\log_{10}(1+z)$
  verified ($+1.32$ mag at $z=1$). ✓

---

## II. Inconsistencies Requiring Edits (ordered by severity)

### II.1 — MAJOR: Core Principles, T8, and T9 still carry the superseded $L\propto c^4$ / $X\propto c^{-1/2}$; T18 and T4 carry the corrected $L\propto c^0$ / $X\propto c^{-3/2}$

T18 (corrected) establishes, via the radius-free electron-scattering mass–luminosity
relation, a three-way cancellation $L\propto c^{-3}\cdot c^{+1}\cdot c^{+2} = c^0$, hence
$F\propto c^0$, $T_\text{eq}\propto c^{1/2}$, $X\propto c^{-3/2}$, and a **~30%**
habitability-ratio gain at 4.5 Gyr lookback. T18 explicitly documents why the earlier
$L\propto c^4$ routes were wrong (they assumed $T_\text{eff}$ tracks the atomic scale
$c^2$; the mass–luminosity relation forces $T_\text{eff}\propto c^1$). T4 already uses the
corrected result ("With $L\propto c^0$ (T18: corrected...)").

The following passages were **not updated** and contradict T18/T4:

1. **Core §5a**: "...and the stellar luminosity scaling $L\propto c^{4}$ (T18)."
   → Replace with "$L\propto c^{0}$ (T18, three-way cancellation: $a\propto c^{-3}$,
   explicit $c^{+1}$, $\kappa^{-1}\propto c^{+2}$)."
2. **Core §6 (entire section)**: currently derives $F\propto c^4$,
   $T_\text{eq}\propto c^{3/2}$, $X\propto c^{-1/2}$, ~9% / ~20 K.
   → Rewrite: $F\propto c^0$ (static orbits + $L\propto c^0$); $T_\text{eq}\propto c^{1/2}$;
   $X\propto c^{-3/2}$; ~30% at 4.5 Gyr; classification "supplementary, purely relational
   easing of the faint young Sun paradox" per T18.
3. **Core §7 status table**, rows "Stellar flux drifts $F\propto c^4$..." and
   "Habitability ratio $X\propto c^{-1/2}$" → update to $F\propto c^0$ and
   $X\propto c^{-3/2}$ (~30%).
4. **T9 §Received Stellar Flux**: "With static orbits and $L\propto c^4$, received flux
   drifts as $F\propto c^4$." → "$L\propto c^0$ (T18 corrected), so received flux is
   $c$-invariant, $F\propto c^0$."
5. **T8 §The Model's Choice: Invariant G**: "The constant-stellar-flux feature is also
   lost; received flux now drifts as $F\propto c^4$. However, the habitability ratio
   $X\propto c^{-1/2}$..." → constant flux is in fact **restored** under the corrected
   $L\propto c^0$ (via a different cancellation than cdot-3's); habitability
   $X\propto c^{-3/2}$, ~30%.

*Why this matters beyond bookkeeping:* the sign and size of the faint-young-Sun statement
is one of the model's few clean positive predictions; the repository currently states two
different exponents and two different magnitudes (9% vs 30%) for it depending on which
document is read.

### II.2 — Core §0 cites the superseded Sciama-drift exponent

Core §0: "...would drift the mass as $c^{-10/3}$ and break invariant mass; T12."
T11 and T12 both derive $c^{-4/3}$ under invariant $G$, explicitly noting that $c^{-10/3}$
was the cdot-3 ($G\propto c^{-2}$) value. → Change to $c^{-4/3}$ in Core §0.

### II.3 — T5 is stale relative to T14/T15/T6 (pre-dates the RAR-closure derivation)

T5 contains several statements superseded elsewhere:

1. "Rotation curves are an unsolved problem in this model... The model does not currently
   provide a mechanism for dark-matter-free flat rotation curves" — contradicts T14
   (RAR closure derived, 0.020 dex; BTFR analytic) and Core's own intro/status table.
2. "The Tully-Fisher normalization ($v_f^4=GM\,a_0$) remains open (it requires a
   non-analytic $B_c$ source)" — the non-analytic wall is explicitly **superseded** in
   T14/T6/T15 (quarter power from transition-radius geometry, not source coupling).
3. §"What Survives" still quotes $a_0\approx cH_0/2\pi$ — T6 now derives the coefficient
   as $cH_0/6$ and demotes $2\pi$ to a "cruder approximation."
4. Path ranking: T5 lists "PBH dark matter (current leading candidate)" ahead of the
   connecton route, while Core's intro calls the connecton route "the leading
   dark-matter-free direction." Whichever ranking the project intends, it should be
   stated once and mirrored (see also §III.1 below — the two candidates partially
   conflict at galactic scales).

→ Proposed edit: add a header note to T5 (matching T15's) stating the retardation results
stand but the "unsolved / non-analytic wall / leading-candidate" framing is superseded by
T14; update items 1–3 in place.

### II.4 — T6 retains the withdrawn "stand or fall together" gating sentence, and a wrong "range" claim

1. T6 §RAR: "The MOND acceleration scale (T6), rotation curves (T5), and RAR (T15)
   **stand or fall together**: solving any one solves all three, and the $\sim10^{-6}$
   order problem of T5 must be resolved first." T15's header explicitly reverses this
   ("progress on the RAR is no longer gated on T5"), and T6's own later sections agree.
   → Delete or replace with the T15 formulation.
2. T6 §"What the model has": "The observed MOND scale $a_0\approx1.2\times10^{-10}$ m/s²
   **sits within this range**" — the quoted range is $3.4$–$6.8\times10^{-10}$ m/s²;
   $a_0$ sits a factor ~3 **below** its lower end (verified numerically). The correct
   statement is that the model's natural acceleration is of the right order of magnitude,
   with the exact value $cH_0^{\text{obs}}/6$ derived from $R_0$. → Fix wording.

### II.5 — T14 internal: factor-3 ambiguity in the connecton quantum, load-bearing for the $\pi/6$ identity

T14 defines the connecton quantum in two inequivalent ways:

- §"The Idea" / §"Energy Scale": $E_\text{connecton} = \hbar c/R_0 = \hbar H_0/6
  \approx 2.5\times10^{-34}$ eV (horizon-mode energy).
- §"Sea density — holographic saturation": $m_c = \hbar H^{\text{hor}}/c^2 =
  \hbar H_0/(2c^2)$, i.e. energy $\hbar H_0/2$ — **a factor 3 larger** (since
  $H^{\text{hor}} = 3c/R_0$).

The celebrated $\hbar$-free identity $\rho_\text{bg} = H_0^2/16G = (\pi/6)\rho_\text{crit}$
depends on the second choice. Using the first (the document's own "minimal quantum of the
observable universe") gives $\rho_\text{bg} = H_0^2/48G = (\pi/18)\rho_\text{crit}
\approx 0.17\rho_\text{crit}$ — verified numerically — which would spoil the claimed
proximity to $\rho_\Lambda\approx0.68\rho_\text{crit}$ (already 23% off at $\pi/6$).
The choice $m_c\propto H^{\text{hor}}$ vs $\propto c/R_0$ is not argued anywhere.
→ Required edit: either justify $m_c = \hbar H^{\text{hor}}/c^2$ physically (e.g. the
quantum is tied to the *rate* $\dot c/c$, not the crossing frequency $c/R_0$) or carry
the factor-3 uncertainty explicitly and demote "exact" to "exact up to an $O(1)$
quantum-definition choice ($\pi/6$ vs $\pi/18$)." The dark-energy identification claim
should be hedged accordingly.

### II.6 — T14 typo: "$H^{\text{hor}}=3H_0^{\text{obs}}$"

§"Toward the RAR": "$R_0 = 3P\,c_0/H_0^{\text{obs}} = 6c_0/H_0^{\text{obs}}\quad(P=2,\
H^{\text{hor}}=3H_0^{\text{obs}})$". As written this is wrong by a factor 6: the model has
$H_0^{\text{hor}} = H_0^{\text{obs}}/2$. The intended parenthetical is presumably
$H^{\text{hor}} = 3c_0/R_0$. → Fix.

### II.7 — T3: garbled $H(z)$ formula and an unexplained apparent contradiction

T3 states (correctly, in coordinate time) that $H^{\text{hor}}$ **grows** over cosmic
time — i.e. $H^{\text{hor}}(z) = H_0^{\text{hor}}/(1+z)^{1/3} < H_0^{\text{hor}}$ for
$z>0$ — yet the comparison table shows "$H(z)$ (model)$/H_0$" **rising** with $z$
(1.28, 1.59, 2.12), and the parenthetical formula below the table is garbled
(its factors do not reproduce the tabulated values). Numerically the table matches
$H(z)/H_0 \approx (1+z)^{2/3}$, which is the horizon rate converted to **proper (atomic)
time**: $H_\tau = H^{\text{hor}}\,(dt/d\tau) = H^{\text{hor}}(c_0/c)^2 \propto
(1+z)^{-1/3}\cdot(1+z) = (1+z)^{2/3}$. The document never says this, so it reads as a
self-contradiction. → Edits: (a) state that the tabulated quantity is the proper-time
rate (the BAO-relevant observable), define it explicitly, and replace the garbled formula
with $H_\tau(z) = H_0^{\text{obs}}(1+z)^{2/3}/P\cdot P = H_0^{\text{obs}}(1+z)^{2/3}$
(or whichever definition the project intends — this must be pinned down before any BAO
comparison, which is itself an open task); (b) note that the small residuals between
$(1+z)^{2/3}$ and the tabulated 1.28/2.12 values should be re-derived.

### II.8 — Minor wording drift on the "leading direction"

Core intro: connecton route is "the leading dark-matter-free direction." T5: "PBH dark
matter (current leading candidate)." T14 verdict: "potentially complementary rather than
exclusive." One canonical statement should exist (suggested: Core's, with the
complementarity caveat), mirrored in T5. Ties into §III.1.

---

## III. Structural Tensions (substantive, not editorial)

### III.1 — PBH halo dark matter vs the baryon-only RAR: a double-counting problem

The repository simultaneously advances:
(a) a **derived, baryon-sourced RAR** (T14/T15) that reproduces observed rotation curves
from $g_\text{bar}$ alone at 0.020 dex — i.e. *no halo dark matter is needed, and any
significant extra clustered mass in the disk-relevant region would spoil the fit*; and
(b) **PBH dark matter at $\Omega_\text{PBH}\sim0.25$, clustered in galactic halos**
(T5, T13, T16), motivated by the CMB higher peaks and rotation curves.

T6 gestures at the resolution ("PBHs sit inertly below it") but this is not a mechanism:
in the connecton picture PBHs gravitate like any mass and would enter $g_\text{bar}$ (or
worse, add an un-modelled term), breaking the observed baryon-only tightness (0.13 dex,
no halo residuals). The clean resolutions are mutually exclusive at galaxy scale:
either (i) PBHs are needed for the CMB epoch but must *not* dominate galactic-halo mass
budgets at $r\lesssim$ tens of kpc (constraining their clustering), or (ii) PBHs are the
halo mass and the connecton RAR derivation is superfluous/epiphenomenal at galaxy scale.
The current documents assert both programs in parallel. **Recommended action:** a
dedicated session to state the intended division of labour quantitatively — e.g. compute
the maximum $\Omega_\text{PBH}(r<30\,\text{kpc})$ compatible with the RAR scatter — and
propagate the conclusion to T5, T6, T15, T16.

### III.2 — Same growing $B_c$, opposite morphological arrows (T17 vs T19)

T14/T17: $B_c$ grows with time → the Lorentz filter strips progressively slower disk
stars → **disk fraction falls toward $z=0$** (more ellipticals late), claimed consistent
with observation. T19: the same $B_c$'s vertical spring strengthens with time
($\omega_L^2\propto(1+z)^{-5/12}$) → **thin-disk fraction rises toward $z=0$** (settled
thin disks emerge late), also claimed consistent with observation. Both trends are
individually defensible (radial ejection of the fastest stars vs vertical compression of
survivors), and both observational statements are individually true in the right
sub-populations — but the repository nowhere confronts the competition: the same field is
credited with *destroying* disks and with *perfecting* them, both increasingly over time.
A minimal reconciliation would compute, for a fiducial disk, the ratio of the stripping
timescale (T17) to the thinning timescale (T19) as a function of $r/r_t$ and
$v_\phi/v_f$, and state in which regime each channel dominates. Until then, T17 Link 4
and T19 §6's "evolutionary predictions" should each cross-reference the other as an
unresolved competition. **Recommended action:** add the cross-caveat now (editorial);
schedule the timescale-ratio calculation (substantive).

---

## IV. Consolidated Edit List (for merge)

| # | File | Edit | Severity |
|---|------|------|----------|
| 1 | Core_Principles.md §5a, §6, §7 table | $L,F\propto c^0$; $X\propto c^{-3/2}$; ~30% | Major |
| 2 | T9 §Received Stellar Flux | same correction | Major |
| 3 | T8 §The Model's Choice | constant flux restored; $X\propto c^{-3/2}$ | Major |
| 4 | Core_Principles.md §0 | Sciama drift $c^{-10/3}\to c^{-4/3}$ | Moderate |
| 5 | T5 (four passages) | de-stale vs T14/T15/T6; unify leading-direction statement | Moderate |
| 6 | T6 (two passages) | delete "stand or fall together"; fix "within this range" | Moderate |
| 7 | T14 §Energy Scale / §holographic | resolve factor-3 quantum definition; hedge $\pi/6$ | Moderate (substantive) |
| 8 | T14 §Toward the RAR | fix "$H^{\text{hor}}=3H_0^{\text{obs}}$" typo | Minor |
| 9 | T3 §H(z) table | define proper-time rate; fix garbled formula; re-derive values | Moderate |
| 10 | T5/T6/T15/T16 + new session | PBH-vs-RAR double counting (§III.1) | Structural |
| 11 | T17 Link 4, T19 §6 | cross-caveat stripping-vs-thinning competition (§III.2) | Structural |

None of the findings above touches the model's firm core (squared redshift law, 21 Gyr
age, two-$H_0$ structure, $q_0=1/(nP)$, invariant-$G$ adoption) — those chains verified
clean. The audit's substantive discoveries are items 7, 10, and 11.
