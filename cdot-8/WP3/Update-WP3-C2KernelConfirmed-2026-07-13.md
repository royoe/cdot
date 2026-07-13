# Update — WP3: $C_2$-Kernel Resolution Confirmed Independently

*Companion: `SessionLog-2026-07-13.md` (this directory), Entry 13. Responds to
`Advisory-WP3-C2Kernel-2026-07-13.md` (sole-advisor round). Every load-bearing claim
re-derived or re-run independently before acceptance, per protocol — not a rubber
stamp of an already fully-verified-looking advisory.*

---

## 1. Independent verification

**Closed-form attractor ratios**, re-derived from scratch (not from the advisory's own
script): for a pure-power source $\Omega_s\propto Q^n$, trying $F=AQ^n$ in $\tfrac12QF_Q
-\tfrac13F=\Omega_s$ gives $A/C=1/(\tfrac n2-\tfrac13)$. Matter era ($n=\tfrac95$, from
$\Omega_s\propto a^{-3}$ and the exact kinematic $Q\propto a^{-5/3}$): $30/17=1.76471$.
Radiation era ($n=\tfrac{12}5$, from $\Omega_s\propto a^{-4}$): $15/13=1.15385$. Both
confirmed by hand.

**Kernel-zero property**: $F=Q^{2/3}$ gives $\tfrac12QF_Q-\tfrac13F$ via finite
difference — residual $2.3\times10^{-10}$, i.e. zero to numerical precision, confirming
$Q^{2/3}$ solves the corrected equation's homogeneous part identically.

**Background invisibility**, checked on my own independent trajectory computation
(not the advisory's script): varying $C_2$ from $-500$ to $+100$ leaves $F(z=2\times
10^6)$ unchanged to 8 decimal places (ratio $1.00000000$ in every case) — the kernel
is genuinely invisible to the deep-past behavior, not merely "small." The $F/\Omega_s$
ratio independently reproduces the claimed attractors: $\approx1.80$–$1.82$ around
$z=20$–$100$ (approaching, not yet at, the asymptotic $30/17=1.765$ — expected, since
this range isn't deep enough into pure matter domination to have fully converged), and
$1.136\to1.150$ across $z=3\times10^5$ to $5\times10^6$, converging cleanly toward
$15/13=1.154$.

---

## 2. What this means, confirmed

$C_2$ is not a second instance of the $C_1$ problem. $C_1$ entered the Hamiltonian
constraint directly (a term $\propto QC_1/a^3$) and could dominate the energy budget —
past regularity was needed and did the work. $C_2$ multiplies the *kernel* of the
corrected constraint operator: by construction it contributes exactly zero to the
constraint (verified above), so no regularity or anchor argument has anything to act
on — there is no "wrong" choice for the background to rule out, because the background
cannot see $C_2$ at all. Its only channels into physics are through pressure
bookkeeping and $\Lambda_M$'s own determination, both of which land at the still-
pending step-5 confrontation, not here. Per directive, $C_2$ is carried *symbolically*
through the quadrature rather than set to zero now — zeroing it prematurely would mask
exactly the kind of non-cancellation the eventual step-5 audit exists to catch.

**Correction applied**: `Update-WP3-QuadratureRedo-2026-07-13.md`'s $\rho\propto
a^{-10/9}$ figure for this mode was the old, $\phi$-sector-only accounting; under the
corrected accounting relevant to this construction, the mode's constraint contribution
is zero, not merely small. Corrected in place there.

---

## 3. Status

The quadrature stands as computed, with $F\propto Q^{1.77}$ (matter era, the
corrected-coefficient bend from the earlier $Q^{9/5}$) and $C_2$ carried symbolically.
A three-slot constant taxonomy is now established for this construction (current
constants → regularity; kernel constants → step-5 audit; multiplier constants →
adjoint pairing + anchor) — worth keeping as a standing classification test for
whatever the next constant turns out to be, rather than re-deriving the category from
scratch each time. Remaining, explicitly still open: the coupling audit (three items,
one pre-seeded, from the adjoint-invariant round) and the step-5 confrontation itself
(the $(C_2,\Lambda_M)$ invariance check, now the last unexamined slot in the whole
construction) — both substantial pieces of remaining work, not yet attempted.
