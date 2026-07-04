# SESSION LOG — First-Principles Derivation of R at Recombination

**Topic:** Deriving the baryon-to-photon ratio $R=3\rho_b/4\rho_\gamma$ at
recombination in a static-$a$ model from first principles, to determine whether
the T16 draft's $R\approx680$ is correct and whether the CMB first-peak failure
is a counting-law or a static-$a$ problem.
**Date:** 2026-07-04 (UTC).
**Outcome:** Constructive — decisive structural result. One update document.

---

## Timeline

**Prompt (prior turn):** established that $R\approx680$ is upstream and diagnostic;
agreed to attempt a first-principles derivation, letting the value fall where it
falls rather than steering to $R\sim0.6$.

**Prompt:** "A first principles derivation should definitely be attempted."

**Derivation (6 steps + self-check):**
1. $R_0=679.8$ reproduced from $\Omega_bh^2$, $T_0$ — confirmed $680$ is the
   *today* value; equivalently $\eta\approx6.1\times10^{-10}$.
2. LCDM $R_\text{rec}=R_0/(1+z)=0.62$ from $n_b\propto(1+z)^3$, $\rho_\gamma\propto(1+z)^4$.
3. Showed the draft's "$\rho_b,\rho_\gamma\propto c^2 \Rightarrow R$ invariant"
   argument is void: the $c^2$ factors cancel identically; $R\propto n_b/T^4$ is
   what matters.
4. Isolated the two decisive quantities: $T_\text{rec}$ and $n_b^\text{rec}$.
   Found the model's "$c$-threshold recombination with both energies $\propto c^2$"
   implies a constant Saha ratio (no recombination event) unless $T$ has an
   independent history. Naive $T\propto c^2$ gives a *colder* past (backwards).
5. Kinematic $T_\text{rec}=T_0(1+z)=2973$ K (forced by the model's redshift law),
   matching atomic ~3000 K. With $n_b$=const (forced by $a=1$): $R_\text{rec}=
   R_0/(1+z)^4\approx5\times10^{-10}$. Reaching $R\sim0.6$ needs $n_b\propto(1+z)^{2.99}$
   ≈ LCDM's $p=3$; static map forces $p=0$.
6. Found a photon-sector contradiction: "$\rho_\gamma\propto c^2$" ($\propto(1+z)^{-1}$,
   colder past) vs kinematic "$\rho_\gamma\propto(1+z)^4$" (hotter past) differ by
   $(1+z)^5\sim10^{15}$; only the latter supports a hot relic CMB.

**Self-check (3 escape routes, all fail):** cold-threshold recombination kills the
peaks; non-constant $n_b$ abandons $a=1$; $\rho_\gamma\propto c^2$ is excluded by
observed peak heights ($R=680\Rightarrow(1+R)\sim681$ suppresses 2nd/3rd peaks;
Planck sees them). Concluded the obstruction is robust and model-internal.

**Result:** $R_\text{rec}$ is neither $680$ nor $0.6$; static-$a$ forces
$R_\text{rec}\approx R_0/(1+z)^4\ll1$ (radiation-dominated), failing the peaks in a
new way, independent of the counting law. LCDM's $R\sim0.6$ is a direct
consequence of expansion, which $a=1$ cannot reproduce.

**Wrote:** UPDATE_R_at_Recombination_Derivation.md (with a §5 caveats block:
thermalization assumed, $z_\text{rec}$ borrowed, peak-height proxy not a Boltzmann
code, result bears on $a=1$ not the counting law).

---

## Key numbers
- $R_0=679.8$ (today); $\eta=6.1\times10^{-10}$.
- LCDM $R_\text{rec}=0.62$.
- Static-$a$ forced $R_\text{rec}=680/(1+z)^4\approx4.8\times10^{-10}$.
- $n_b$ exponent needed for $R\sim0.6$: $p\approx2.99$ (LCDM 3; static map 0).
- $T_\text{rec}$ kinematic $=T_0(1+z)=2973$ K $\approx$ atomic 3000 K.

## Artifacts produced
- `UPDATE_R_at_Recombination_Derivation.md`
- `SESSION_LOG_R_at_Recombination.md` (this log)

## Relationship to prior session output
- Confirms and deepens REVIEW_NOTE_T16_First_Peak: the CMB first-peak tension is
  dominantly a static-$a$ baryon-loading problem, upstream of and independent of
  T23's counting law, which is thereby substantially exonerated on the first peak.

## Open next steps
1. Full Boltzmann (CAMB/CLASS) confirmation of the peak-height exclusion of both
   $R=680$ and $R\ll1$.
2. Search for any static-$a$-compatible mechanism giving effective $O(1)$ baryon
   loading at recombination (none currently in the model).
3. Derive $z_\text{rec}$ within the model to remove the circularity in $T_\text{rec}$.
4. Decide, at Core level, whether the static-$a$ premise survives this obstruction
   or must be amended.
