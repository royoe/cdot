# Session Log Entry — 2026-07-07 (Fable-2 session, entry 1; for merge into `cdot-7/SessionLog-2026-07-07.md` as Entry 6)

## Entry 6 — Open item 1 executed: joint fit to real Pantheon+ data + the $a_0(z)$ sector

**Prompt (verbatim):**
> Project files have been updated with data from all sessions. Please reassess the conclusions and see if we can proceed further on the open issues.

**Summary:** Reassessed the consolidated Foundation (spot-checked merged numbers
against the Fable-1 derivations — faithful) and identified §6 item 1, the decisive
joint statistical fit, as the highest-value tractable item, with ResearchNotes §11's
zero-point question folded in. Executed it at first-pass level with **real data**:

1. **Data acquired:** the official Pantheon+ release (1701 SNe, `m_b_corr`, full
   33 MB STAT+SYS covariance) downloaded from the PantheonPlusSH0ES GitHub;
   $a_0$-sector constraints taken from the published record (SPARC $1.20\pm0.26$;
   MIGHTEE-HI $1.69\pm0.13$ at $z\approx0.05$; MUSE-DARK III $2.38\pm0.055$ at
   $z_\text{eff}\approx0.9$ and slope $1.59\pm0.054$; MUSE point/slope correlation
   flagged as a known double-count in this first pass).
2. **Pipeline validated:** flat $\Lambda$CDM on the identical likelihood
   ($z_\text{HD}>0.01$, 1590 SNe, offset marginalized) returns
   $\Omega_m=0.331\pm0.018$, $\chi^2=1403.7$ — reproducing the published Pantheon+
   SN-only result.
3. **The framework passes.** Rigid joint fit ($\kappa=1$, no zero-point freedom,
   simple $\mu$): $\varepsilon_0=-0.0678$, $\kappa\lambda=0.307$;
   $\chi^2_\text{SN}=1405.3$ ($\Delta\chi^2=+1.6$ vs $\Lambda$CDM at equal SN-side
   parameter count) and $\chi^2_{a_0}=6.5$ for four constraints — versus $20.0$ for
   the best *free linear* $a_0(z)$ law. The trajectory's SN-fit-suppressed low-$z$
   growth is the only smooth shape that threads SPARC→MIGHTEE→MUSE.
4. **The amplitude shortfall resolved:** the Fable-1 confrontation's 15–20% deficit
   was an artifact of anchoring $a_0(0)$ to SPARC's 1.2; the joint fit *predicts*
   $a_0^\text{loc}=1.39\times10^{-10}$ m/s², sitting between SPARC ($0.7\sigma$) and
   MIGHTEE ($2.1\sigma$) — arbitrating the zero-point dispute, falsifiably.
5. **$\kappa$ measured $\approx1$:** freeing the amplitude entirely, the data land on
   $\kappa=1.01$ ($0.91$ with 0.1-dex zero-point tolerance; $\propto1/H_0$). The
   coefficient assumed unity by fiat is now empirically unity — nothing forced this.
6. **$\mu$-form selected, reasoning corrected:** on SNe alone with $\kappa\lambda$
   free, simple/standard are degenerate (the proxy-era "4× rms" claim conflated
   $\mu$-form with the $\kappa\lambda$ choice — amended). The $a_0$ amplitude pins
   $\kappa\lambda$, and then standard $\mu$ fails both sectors: joint
   $\Delta\chi^2=42$ for simple.
7. **Revised fiducial cosmology:** $q_0=-0.56$ (numerically $\Lambda$CDM's value,
   unforced), age $12.8$ Gyr (the tightest remaining squeeze), $x_0=1.61$.
8. **Residual softness for the definitive version:** MUSE per-bin values and
   covariance (removes double-counting; $z_\text{eff}=0.7$ shifts $\kappa\lambda$ by
   $\sim13\%$), local RAR shape likelihood, proper MCMC posteriors. Internal pull
   noted: SN-only prefers $\kappa\lambda\approx0.48$ ($2\sigma$ from the joint
   solution).

**Files produced:** `Update-JointFit-2026-07-07.md`, `joint_fit.py` (self-contained;
verified to reproduce every quoted number, including the $\Lambda$CDM validation),
this log entry.
