# Advisory — Connor et al. (2025) FRB Baryon Census Checked Against cdot-8's Own $\Omega_b=0.044204$: Consistent Within ~1.1$\sigma$ of the New Measurement's Own (Much Larger) Uncertainty — No Action Needed, the BBN Input Remains the Right One to Keep (for `cdot-8/` foundation, review of a user-flagged external paper)

*2026-07-21. Advisory in response to the author's request: assess
whether Connor et al. 2025 (Nature Astronomy,
[10.1038/s41550-025-02566-y](https://www.nature.com/articles/s41550-025-02566-y),
"A gas-rich cosmic web revealed by the partitioning of the missing
baryons") affects cdot-8's mass census. **Verdict up front: no, it
doesn't warrant any change.** The paper's FRB-dispersion-measure
baryon density, $\Omega_bh_{70}=0.051^{+0.006}_{-0.006}$, is directly
comparable to cdot-8's own inherited $\Omega_b=0.044204$ because both
use the exact same $H_0=70$ convention — a genuine, checkable
apples-to-apples comparison, not a coincidence of units. The two values
sit **1.1$\sigma$** apart using the new paper's own uncertainty, and
that uncertainty ($\pm12\%$) is roughly **13$\times$ larger** than the
BBN value's own ($\pm0.9\%$) — a mild, unremarkable consistency check
in favor of an independent, late-Universe method, not a reason to
revisit an input the project already treats as fixed acceptance data.*

---

## 1. What the paper reports, checked against the primary claim

Connor, Ravi et al. (2025) use 69 localized fast radio bursts (FRB
dispersion measures via the Macquart relation) to perform a **late-
Universe, direct census** of cosmic baryons — a genuinely independent
method from both CMB and BBN, tracing free electrons along FRB
sightlines rather than primordial light-element abundances or the
acoustic power spectrum. Their headline number:
$$\Omega_bh_{70}=0.051^{+0.006}_{-0.006},\qquad h_{70}\equiv H_0/70\
\text{km/s/Mpc}.$$
The paper's main scientific claim is about **where** the baryons are
(most in the diffuse intergalactic medium/cosmic web, not galaxies),
not primarily a claim that $\Omega_b$ itself has shifted — the total
matches expectations; the finding is about the partitioning.

## 2. Why this compares directly to cdot-8's own number, not just approximately

Traced cdot-8's own $\Omega_b=0.044204$ (Foundation.md §2,
"$\Omega_b=0.0442$, matching Planck's independent BBN $\omega_b$ to
3%") back to its source rather than taking the Foundation.md figure at
face value: `cdot-7/Fable-1/four_term_fit.py` fixes
$$\omega_b\equiv\Omega_bh^2=0.02166\pm0.00019\quad\text{(Cooke, Pettini
\& Steidel 2018, BBN deuterium abundance — not CMB)},$$
with $H_0=70\,\text{km/s/Mpc}$ **fixed throughout, not fit** (the
script's own comment: "H0 fixed at 70 km/s/Mpc throughout... the SN
likelihood alone cannot pin it down"), giving $\Omega_b=\omega_b/0.7^2=
0.044204$ exactly — reproduces the quoted figure precisely, confirming
the derivation, not merely the number.

**This is the same $H_0=70$ convention the new paper itself uses**
($h_{70}$ is explicitly normalized to 70 km/s/Mpc) — so $\Omega_
b^\text{cdot-8}=0.044204$ and $\Omega_bh_{70}^\text{Connor}=0.051$ are
directly comparable numbers in the same convention, not requiring any
extra $H_0$-dependent conversion on either side. Worth stating plainly
since a mismatched-convention comparison would be meaningless — this
one isn't.

## 3. The comparison itself

$$\Delta=0.051-0.044204=0.0068,\qquad\frac{\Delta}{\sigma_\text{Connor}}
=\frac{0.0068}{0.006}\approx1.13.$$
**About 1.1$\sigma$ apart, using the new paper's own uncertainty** — a
mild, unremarkable difference, well short of anything resembling
tension. **The relevant asymmetry**: Cooke et al. 2018's BBN value has
$\sigma_{\omega_b}/\omega_b\approx0.9\%$ relative precision, while
Connor et al.'s FRB value has $\sigma/\Omega_bh_{70}\approx12\%$ — the
FRB measurement's own uncertainty is **roughly 13 times larger**. Given
this, even a value sitting exactly on the new paper's own central
estimate would carry far less statistical weight than the already-
adopted BBN figure; the actual $\sim1\sigma$ offset carries essentially
no evidential weight against the BBN input.

## 4. Is there a reason to prefer the new number anyway, on grounds other than precision?

Considered and rejected, briefly: the FRB method is genuinely
independent and late-Universe (a different systematic-error profile
from both CMB and BBN, which is valuable as a cross-check), and its
consistency with the BBN value is itself a useful, positive data point
for the field generally. But it is **not** more fundamental or more
direct for the specific quantity cdot-8's census needs ($\Omega_b$ as
an input fixed from first principles, independent of the theory's own
free parameters) — if anything, the FRB method carries its own model
dependencies (host-galaxy and Milky Way dispersion-measure
subtraction, an assumed background cosmology to convert DM to distance)
that the primordial-abundance BBN measurement doesn't. There is no
methodological reason to swap a $0.9\%$-precision, first-principles
input for a $12\%$-precision one that already agrees with it within
1$\sigma$.

## 5. Status and recommendation

**No action needed.** cdot-8's $\Omega_b=0.044204$ (Cooke et al. 2018,
BBN) remains the right input, unaffected by this new paper — consistent
within the new measurement's own (much larger) uncertainty, and in no
sense superseded by it. Worth keeping this paper on file as a
positive, independent consistency check for the census's own external
inputs (in the same spirit as WP4b's own BBN-rate check), should a
future round want an updated "external anchors" summary — but nothing
in `Foundation.md`, `Progress.md`, or any WP's own census work needs to
change. This advisory is written to `cdot-8/foundation/` per the
program's own convention (this is a Foundation-level acceptance-data
question, not a WP7-specific one); nothing in `WP7/` or `cdot-7/` was
touched.

## Companion

- No new script — the comparison above is arithmetic only (§3), and the
  $\Omega_b=0.044204$ re-derivation (§2) was checked directly against
  `cdot-7/Fable-1/four_term_fit.py`'s own constants, not recomputed
  separately.
- This advisory: `cdot-8/foundation/Advisory-NewFRBBaryonCensusAssessed-2026-07-21.md`.
