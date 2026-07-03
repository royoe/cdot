# Update — T7: First-Order QED Treatment of $\alpha$ Running in a Variable-$c$ Vacuum (2026-07-03)

*Session type: constructive. Question posed: does one-loop QED vacuum polarization introduce
observable $\alpha$ drift when $c$ varies cosmologically ($\epsilon_0\propto\mu_0\propto c^{-1}$,
$m_e,e,\hbar$ invariant), as flagged in T7 and the Project Summary (naive estimate $\sim 500$
ppm at $z\sim1$ vs ESPRESSO's 1–2 ppm bound)? Answer: **the naive estimate uses the wrong
renormalization scale.** The physical atomic spectroscopy scale is $q\sim Z_\text{eff}\alpha\,m_e c$,
not $q\sim m_e c$. With cdot scaling, the one-loop dimensionless argument
$\mathcal{R}=q^2\hbar^2/(m_e^2 c^4)$ is epoch-independent; **$\Delta\alpha/\alpha=0$ to
first order** for the Many Multiplet (MM) observable. Tree-level $\alpha$-invariance is
extended to one-loop: relational $c$-scaling moves the renormalization point with the atomic
scale. **Status: Tier-1.3 QED threat discharged at first order; ESPRESSO consistent.**

---

## 1. The Open Question (from T7)

Tree-level $\alpha$ is exactly invariant:
$$\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c} \propto \frac{e^2}{c^{-1}\cdot\hbar\cdot c}
= \text{const},$$
forced by the EM relation $c=1/\sqrt{\epsilon_0\mu_0}$ with $\epsilon_0\propto\mu_0\propto c^{-1}$
(Core §2). T7 nonetheless flagged a one-loop threat: vacuum polarization depends on
$$\mathcal{R} \equiv \frac{q^2\hbar^2}{m_e^2 c^4} = \left(\frac{q}{m_e c}\right)^2,$$
and if $q\sim m_e c$ while $c$ changes by $\sqrt{2}$ from $z=1$ to today, then
$\Delta\ln\mathcal{R}=\ln 2$ and
$$\frac{\Delta\alpha}{\alpha}\sim\frac{\alpha}{3\pi}\ln 2\approx 5\times10^{-4}\quad(\sim 500\ \text{ppm}),$$
far above ESPRESSO ($|\Delta\alpha/\alpha|\lesssim 1$–$2$ ppm at $z\sim 1.15$). That
estimate was explicitly marked speculative; a clean first-order calculation had not been
completed. Multiple earlier attempts reportedly produced inconsistent magnitudes due to
confusing additive with multiplicative perturbations.

**What is needed for the MM observable:** does $\alpha_\text{eff}(z)$, inferred from spectral
line ratios at the absorber's epoch, differ from today's lab value when loop corrections are
included consistently with cdot's scaling laws?

---

## 2. Setup: Scaling Laws at Epoch $t$

From Core Principles and T7 (invariant $m_e,e,\hbar$; EM-forced $\epsilon_0\propto\mu_0\propto c^{-1}$):

| Quantity | Scaling | Notes |
|---|---|---|
| $\alpha_\text{tree}$ | $c^0$ | exact cancellation |
| $\lambda_C=\hbar/(m_e c)$ | $c^{-1}$ | Compton length |
| $a_B=4\pi\epsilon_0\hbar^2/(m_e e^2)$ | $c^{-1}$ | Bohr radius |
| $E_\text{Ryd}\propto m_e e^4/\epsilon_0^2$ | $c^{+2}$ | atomic energy scale |
| $m_e c^2$ | $c^{+2}$ | rest energy |

At $z=1$: $c_\text{emit}/c_\text{now}=(1+z)^{-1/2}=1/\sqrt{2}$.

The MM method compares transitions with different $\alpha$-sensitivities $K_i$:
$$\frac{\omega_i^\text{obs}}{\omega_i^\text{lab}}=(1+z)\left[1+K_i\,\frac{\Delta\alpha}{\alpha}+\cdots\right].$$
The target is $\Delta\alpha/\alpha\equiv[\alpha_\text{eff}(z)-\alpha_0]/\alpha_0$.

---

## 3. One-Loop Vacuum Polarization

At one loop, the effective coupling at momentum scale $q$ is (schematically, $q^2\ll m_e^2 c^4/\hbar^2$):
$$\alpha_\text{eff}(q^2)=\alpha_0\left[1+\frac{2\alpha_0}{3\pi}\,
\ln\!\frac{m_e^2 c^4/\hbar^2}{q^2}+\mathcal{O}(\alpha_0^2)\right].$$
All epoch dependence enters through the dimensionless ratio $\mathcal{R}=q^2\hbar^2/(m_e^2 c^4)$.
Vertices contribute only through $\alpha_0$; $\epsilon_0$ is already absorbed into $\alpha_0$
at tree level. Fermion propagators use the invariant mass shell $E^2-(pc)^2=(m_e c^2)^2$ with
$m_e$ invariant; when expressed dimensionlessly, the loop depends on $q/(m_e c)$ only.

---

## 4. The Error in the Naive Estimate

T7's naive estimate sets $q\sim m_e c$, giving $\mathcal{R}=1$ and
$$\Delta\ln\mathcal{R}=\Delta\ln(c^2)=\ln\frac{c_\text{now}^2}{c_\text{emit}^2}=\ln 2\quad(z=1\to\text{now}),$$
hence $\Delta\alpha/\alpha\sim(\alpha_0/3\pi)\ln 2\approx 540$ ppm.

**This is not the atomic spectroscopy scale.** For hydrogenic binding,
$$E_n\sim\frac{\alpha^2 m_e c^2}{2n^2},\qquad p_n\sim\sqrt{m_e E_n}\sim\alpha\,m_e c,$$
so the physical probe momentum is
$$\frac{q}{m_e c}\sim Z_\text{eff}\,\alpha\quad\text{(pure number, no explicit }c\text{)}.$$
For Mg II, Fe II, and other MM ions, internal momenta have the same structure: always
$(\text{dimensionless atomic factor})\times m_e c$, with the dimensionless factor built from
$Z_\text{eff},n,\ell$ and $\alpha$ itself.

Therefore:
$$\boxed{\mathcal{R}=\left(\frac{q}{m_e c}\right)^2\sim (Z_\text{eff}\alpha)^2\times f(n,\ell)
=\text{epoch-independent}}$$
and
$$\boxed{\left.\frac{\Delta\alpha}{\alpha}\right|_\text{1-loop}=0}$$
for any MM comparison between emission epoch and today.

---

## 5. Why This Is Structurally Forced (Not an Accidental Cancellation)

The tree-level identity $\alpha\propto e^2/(\epsilon_0\hbar c)=\text{const}$ is one instance
of a broader pattern: when $c$ is the sole cosmological dial, dimensionless QED ratios built
from the model's scaling laws do not carry residual $c$-dependence.

Examples (all epoch-independent):
$$\frac{E_\text{Ryd}}{m_e c^2}\propto\frac{c^2}{c^2}=\text{const},\qquad
\frac{a_B}{\lambda_C}=\frac{4\pi\epsilon_0\hbar c}{e^2}\propto\frac{1}{\alpha},\qquad
\frac{r_e}{a_B}=\text{const}.$$

The loop log depends only on $\mathcal{R}=(q/m_e c)^2$. When $q$ is the **physical** atomic
momentum $\propto\alpha\,m_e c$, $\mathcal{R}$ is a pure number at every epoch. The Compton
scale $\lambda_C\propto c^{-1}$ and the atomic scale $a_B\propto c^{-1}$ co-scale so their
dimensionless ratio is fixed. In standard constant-$c$ cosmology this is invisible; in cdot,
$c$ varies but atomic probes and vacuum loops are expressed in the same local $c$, so the
renormalization point moves with the physics and MM sees no drift.

**What MM actually measures:** at emission, all transitions are computed with the same local
$\alpha_\text{eff}(\mathcal{R}_i)$. Each $\mathcal{R}_i$ is $c$-independent, so
$\alpha_\text{eff}(z)=\alpha_\text{eff,now}$ and $\Delta\alpha/\alpha=0$. Loops are present
at every epoch (Lamb shift, fine structure, etc.) but constitute the **same fractional
correction** when expressed dimensionlessly. MM detects **differences** in $\alpha$ between
epochs, not the absolute offset from tree level.

---

## 6. Order-of-Magnitude Table

| Renormalization scale | $\mathcal{R}=q^2\hbar^2/(m_e^2 c^4)$ | $\Delta\ln\mathcal{R}$ ($z=1\to$now) | $\Delta\alpha/\alpha$ (1-loop) |
|---|---:|---:|---:|
| Naive: $q=m_e c$ | $1$ | $\ln 2\approx 0.69$ | $\sim 500$ ppm ❌ |
| Atomic: $q=\alpha m_e c$ | $\alpha^2\approx 5.3\times10^{-5}$ | $0$ | $\mathbf{0}$ ✓ |
| Fe II inner: $q\sim Z_\text{eff}\alpha m_e c$ | $\sim 10^{-4}$–$10^{-3}$ | $0$ | $\mathbf{0}$ ✓ |

ESPRESSO: $|\Delta\alpha/\alpha|\lesssim 1$–$2$ ppm at $z\sim 1.15$. **Prediction: consistent.**

At $z=3$ ($c_\text{emit}/c_\text{now}=1/2$): the naive wrong estimate would give
$\Delta\alpha/\alpha\sim(\alpha_0/3\pi)\ln 4\approx 1000$ ppm; the corrected prediction
remains **0**.

---

## 7. Predicted $\Delta\alpha/\alpha(z)$ and Honest Ledger

**Prediction:**
$$\boxed{\frac{\Delta\alpha}{\alpha}(z)=0\quad\text{(one-loop; and, under the scaling argument
above, all orders in the leading log)}}.$$

Equivalently, $\alpha_\text{eff}(z)=\alpha_0\times[1+C\ln(1/\alpha_0^2)+\cdots]$ with the
**same** $C$ at all $z$; MM measures only the difference, which vanishes.

**Still zero at leading log:**
- Two-loop: $\mathcal{O}(\alpha_0^2)$ times the same dimensionless $\mathcal{R}_i$ — still
  $c$-free.
- Different transitions (Mg vs Fe): different $\mathcal{R}_i$, but each $\mathcal{R}_i$ is
  epoch-independent; internal running within one epoch cancels in the MM difference.
- Absolute Lamb shift $\propto\alpha^5 m_e c^2\ln(1/\alpha^2)$: scales as $c^2$ like all
  atomic energies; no extra $\alpha$ drift.

**Not covered (remain separate T7 items):**
1. **Asymmetric $\epsilon_0/\mu_0$ split** — breaks tree-level $\alpha$ invariance; premise
   question, not QED running.
2. **Analysis systematics** — fitting codes assuming constant-$c$ QED; physical prediction
   remains $\Delta\alpha/\alpha=0$.
3. **Line-by-line verification** for specific MM ions — scaling argument extends to any
   transition whose momentum scale is $\propto m_e c$ times a dimensionless atomic factor
   (the standard case); a dedicated Fe II/Mg II check would be confirmatory, not load-bearing.

**What would falsify this result within cdot:** any dimensionless ratio entering loops that
depends on $c$ while the MM probe does not. The earlier inconsistent magnitudes are diagnosed
as using $q\sim m_e c$ ($\mathcal{O}(1)$ in $q/(m_e c)$) instead of $q\sim\alpha m_e c$
(multiplicatively smaller by $\alpha$).

---

## 8. Consolidated Edits (for merge)

| # | File | Edit | Type |
|---|------|------|------|
| 1 | T7 §"The Open Question: QED Corrections" | Replace the speculative 500 ppm estimate with this result: naive estimate wrong (wrong $q$); corrected $\Delta\alpha/\alpha=0$ at one loop; add §reference to this update | Major correction |
| 2 | T7 §"Observational Implications" | Reword: model is **safe** at first-order QED; ESPRESSO is a passed consistency check, not a pending threat | Status upgrade |
| 3 | T7 §"Open Questions" | Strike the first bullet (clean first-order QED calculation); add optional confirmatory bullet (line-by-line MM ion check); retain asymmetric $\epsilon_0/\mu_0$ split and Bohr-radius observational items | Open questions |
| 4 | Core_Principles.md §7 status table | Row "Fine-structure drift $\dot\alpha$": change from **Open** to **Resolved at one-loop QED** ($\Delta\alpha/\alpha=0$ for MM; T7 update 2026-07-03) | Status upgrade |
| 5 | audit/Project_Summary_2026-07-02.md §5 item 2 | Add cross-note: QED $\alpha$-drift threat discharged at first order (T7 update 2026-07-03) | Cross-note |
| 6 | new_tests/Update_2026-07-02_Observational_Test_Battery.md | Tier-3 item 10 ($\mu$ invariance): add sibling note that $\Delta\alpha/\alpha=0$ is likewise forced at one-loop QED, not only tree level | Cross-note |

**Bottom line.** The highest-leverage unfinished theory calculation identified in the
Project Summary (QED running of $\alpha$, T7) is **resolved at first order**: the naive
$\sim 500$ ppm estimate at $z\sim 1$ used the Compton scale $q\sim m_e c$ as the probe
scale instead of the Bohr scale $q\sim\alpha m_e c$. With cdot's relational scaling, the
one-loop dimensionless argument $\mathcal{R}=q^2\hbar^2/(m_e^2 c^4)$ is epoch-independent
at the physical atomic scale, so $\Delta\alpha/\alpha=0$ for the MM observable. Tree-level
$\alpha$-invariance extends to one-loop vacuum polarization; ESPRESSO is consistent. The
earlier "additive vs multiplicative" confusion in T7 is diagnosed as a **multiplicative**
error: $q/(m_e c)$ is $\mathcal{O}(\alpha)$, not $\mathcal{O}(1)$.
