# Session Log Entry — 2026-07-07 (for merge as Entry 7 of `cdot-7/SessionLog-2026-07-07.md`)

## Entry 7 — AQUAL-consistent closure built; EdS fixed point unstable; $\Lambda$-analog found; age → 13.0 Gyr

**Prompt (verbatim):**
> Good! Proceed with §3.

**Summary:** Executed the construction proposed in Entry 6 §3: rebuilt premise 2's
Sciama closure with the AQUAL field, self-consistently with $a_0=\lambda\dot c$.
Closure form decided and flagged: $c^2=\kappa g_hR_h$ with the exact spherical AQUAL
relation $\mu(g_h/a_0)g_h=GM_h/R_h^2$ (potential-based alternative rejected —
deep-MOND log potential carries an arbitrary reference scale; parameters enter only
as $\kappa\lambda$). Because $a_0\propto\dot c$, the closure becomes a genuine 2D
autonomous dynamical system — one integration constant beyond the old algebraic
closure. Results:

1. **Fixed point:** the scale-free solution $R_h\propto c^{3/4}$ survives at
   $x_*=3/(4\kappa\lambda)$ *for every* $\lambda$ — Entry 6's hope of deriving
   $\lambda$ from self-consistency is dead (recorded). All EdS-equivalent photometric
   results hold on the fixed point for any $\mu,\lambda$.
2. **Instability:** linear analysis gives $\dot\varepsilon=(3/2\nu_*)H\varepsilon$,
   $\nu_*=d\ln\mu/d\ln x|_{x_*}$, so $\varepsilon(z)=\varepsilon_0(1+z)^{-1/\nu_*}$ —
   negligible in the past, emerging recently: $\Lambda$ phenomenology from an
   instability. Verified numerically (5.79 vs predicted 5.83). Cosmography:
   $q_0=(4-2j)/3$ (checked: fixed point $j=5/4\Rightarrow q_0=+1/2$); linear
   $q_0=1/2+\varepsilon_0(\nu_*+2)/\nu_*^2$; $\varepsilon_0<0$ branch (slide toward
   deep MOND) gives acceleration and an older universe.
3. **Nonlinear numerics** (validated: $\varepsilon_0=0$ reproduces EdS and
   age$\cdot H_0=2/3$ to $\sim10^{-10}$): with the *same* $\lambda=0.26$ the empirical
   $a_0$ requires, simple $\mu$, and one fitted constant $\varepsilon_0=-0.063$, the
   model matches $\Lambda$CDM ($\Omega_m=0.3$) $d_L(z)$ to **0.015 mag rms** over
   $z\in[0.02,1.4]$; $q_0=-0.68$; **age 13.0 Gyr** (from 9.3). History is EdS to
   $0.1\%$ by $z\sim5$; closure has slid from $x_*=2.88$ to $x_0=1.88$. Nonlinearity
   strong (fitted $\varepsilon_0$ twice the linear estimate).
4. **$\mu$ discrimination:** standard-$\mu$ fits $\sim4\times$ worse (0.060 mag rms)
   — the expansion history now constrains the interpolating function independently of
   rotation curves. Consistency triangle: $a_0$-value gives $\kappa\lambda=0.26$; SN
   shape prefers $\kappa\lambda\approx0.35$ (simple $\mu$, rms 0.004) — agreement to
   $\sim35\%$, within the unknown $O(1)$ $\kappa$.
5. **Asymptotic future:** runaway with $c\propto(t_\ast-t)^{-2/5}$ at finite
   coordinate time; proper time diverges logarithmically — constant proper time per
   e-fold of $c$, numerically $\approx16.5$ Gyr, essentially $\Lambda$CDM's de Sitter
   rate ($1/\sqrt{\Omega_\Lambda}H_0\approx16.7$ Gyr; plausibly fit-induced but the
   EdS correspondence thereby extends to the asymptotic future: deep-MOND runaway
   $\leftrightarrow$ de Sitter phase). Genesis-mirror (infinite proper time to the
   future singularity) survives, weakened from power-law to logarithmic.
6. **Ledger:** derived — mechanism, deviation shape, branch structure, cosmography,
   asymptotics; fitted — $\varepsilon_0$ (one number, the $\Omega_\Lambda$-analog)
   and $\kappa\lambda$ (doubly measured); assumed — closure form, $\kappa=1$,
   $\Lambda$CDM curve as SN-data proxy. Entry 6's premise 2/4 inconsistency is
   resolved. New hardest question: the origin/amplitude of the seed $\varepsilon_0$.
   Successor items: real SN-compilation fit jointly with RAR data; BAO/CMB sector.

**Files produced:** `Update-ClosureRebuild-2026-07-07.md`, `closure_dynamics.py`
(self-contained, reproduces every quoted number; verified end-to-end), this log
entry.
