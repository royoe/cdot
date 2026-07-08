# Session Log Entry — 2026-07-07 (Ω reconciliation; number per current log at merge)

## Entry — Consolidator's reconciliation request: closed analytically; four-term fit remains open, now de-risked

**Prompt (verbatim):**
> This is the feedback from the consolidator on the last response. It seems to want you to try to improve the four-parameter fit before merging this in. Please analyse the response and see if it can be accommodated, or if we should leave it as an open item.
> [Consolidator verified the Ω formula and fixed-point specialization exactly; found a three-way numerical gap (0.104 / 0.115 / 0.134) traced tentatively to ε₀ fit variants; verified the neutrino arithmetic; recommended holding falsification thresholds and the merge until reconciled; offered to either wait for the four-term fit or have the ε₀-variant question pinned down first.]

**Summary — accommodation assessment:** partially accommodated, decisively. The
*reconciliation* (the actual merge blocker) is closed in this session, analytically
and exactly; the *four-term fit itself* cannot be run here (requires the real SN
compilation, per-survey $a_0(z)$ likelihoods, local RAR data, and the other
sessions' fit infrastructure) and remains the open item — now with an
implementation spec that prevents the discrepancy from recurring.

**The reconciliation (all three numbers to three digits):** the exact formula
$\Omega=\tfrac89\kappa\lambda^2x_0^2\mu_0$ generates 0.1336 under the **$\kappa=1$
convention** ($\lambda=\kappa\lambda=0.307$, joint-fit $\varepsilon_0=-0.0678$),
0.1152 under the **$a_0$-anchored convention** ($\lambda=0.2647$, $\kappa=1.16$,
same $\varepsilon_0$), and 0.1044 ($a_0$-anchored, proxy $\varepsilon_0=-0.0752$).
The dominant split is the $\lambda$-convention, not the fit variant: $\kappa=1$
implicitly asserts $a_0=1.39\times10^{-10}$ m/s², 16% above the empirical anchor.
Ruling proposed: for mass-census statements, $\lambda$ is $a_0$-anchored and
$\kappa$ stated explicitly; retire 0.134 with a one-line convention note.

**The consolidator's offered question dissolved:** in the newly derived $H_0$-free
form $\rho_0=\tfrac{3}{4\pi}\kappa\mu_0x_0^2\,a_0^2/(Gc_0^2)$ (H₀ cancels — the
closure ties its density to the MOND scale alone), the entire $\varepsilon_0$-variant
spread is $F=\rho_0/\rho_b=2.28$–$2.52$, i.e. $\pm5\%$ — which variant feeds the
formula barely matters. What controls the falsification threshold is $a_0$'s
empirical value ($F\propto a_0$ linearly, since $\kappa\propto1/a_0$ at fixed
$\kappa\lambda$: $F\in[1.97,3.06]$ over $a_0=1.2\pm0.26$), then the
$\kappa\lambda$ posterior; escape line at $F\le1.60$ (KATRIN-limit neutrinos).
Central case fails by $\times1.6$; the $(-1\sigma\,a_0)\times$(high-$\kappa\lambda$)
corner reaches $F\approx1.4$ — the fit adjudicates.

**Recommendations recorded:** unblock the merge for the reconciled statement
($F=2.3$–2.5; $\Omega=0.10$–0.12 at $h=0.7$; convention rule stated); implement the
four-term fit in $F$-form with the $a_0$ (McGaugh) prior marginalized and
$\Sigma m_\nu$ a bounded nuisance; hold falsification thresholds for the fit (per
the consolidator), noting their precision is $a_0$-limited not variant-limited;
adopt the KATRIN clock as an explicit, dated external falsification condition —
the framework's first deadline set by someone else's experiment; seed-origin work
stays frozen.

**Files produced:** `Update-OmegaReconciliation-2026-07-07.md`,
`omega_reconciliation.py` (verified; reproduces the reconciliation table and
sensitivity budget), this log entry.
