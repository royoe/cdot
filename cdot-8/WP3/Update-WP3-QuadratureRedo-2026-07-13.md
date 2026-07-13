# Update — WP3: The Corrected Quadrature, and a Second Integration Constant Nobody Has Fixed Yet

*Companion: `SessionLog-2026-07-13.md` (this directory), Entry 12. Executes the
now-cleared directive from `Advisory-WP3-AdjointInvariant-2026-07-12.md` §5.4 and
`Addendum-AdjointRound-CoupledInvariant-2026-07-13.md`: verify the adjoint identity,
then proceed to the quadrature redo against the corrected (coefficient-$\tfrac12$,
$C_1=0$) Hamiltonian constraint. The identity checks out exactly. The quadrature
surfaces a genuinely new issue — not a repeat of the $C_1$ question, a second one —
reported before choosing an answer arbitrarily.*

---

## 1. Adjoint identity verified to machine precision

Built $\mathcal N_\text{rad}(s)$ and $p_{\mathcal N,\text{rad}}^\text{hom}(s)$
independently from the shared $g_\text{rad}(s)$ on the actual fitted trajectory
(forward branch, where the growth was found) and checked their product directly:
constant to $2\times10^{-16}$ at every sampled point from $s=0$ to $s=2.9$. The
identity is exact, as the algebra guarantees, and the "instability" from
`Update-WP3-ExponentTable` is confirmed to be the bare multiplier's adjoint growth,
exactly compensating $\mathcal N_\text{rad}$'s decay, not a physical runaway.

---

## 2. The corrected quadrature

Solving $\tfrac12QF_Q-\tfrac13F=\Omega_s(a)$ (the coefficient-$\tfrac12$ constraint
with $C_1=0$) as a linear ODE in $F(Q)$ gives, via the integrating factor $Q^{-2/3}$:
$$F(Q)=Q^{2/3}\left[-5\int_{s_\text{ref}}^{s}Q(s')^{-2/3}\Omega_s(s')\,ds'+C_2\right]$$
— integrated over the well-resolved, uniform $s$-grid (not naively in $Q$ itself,
which spans **ten orders of magnitude** and produces spurious numerical noise under
naive trapezoidal integration — caught this and redid it properly before trusting any
number). With the reference point taken at today ($s_\text{ref}=0$, $C_2=0$ there):
matter-era power law $F\propto Q^{1.77}$ — close to, but not exactly, the previous
(coefficient-$\tfrac13$) round's $Q^{9/5}=Q^{1.8}$, a small but real shift from the
corrected coefficient, worth noting even though it isn't the main finding here.

---

## 3. A second integration constant, unaddressed by any prior round

**With this same, arbitrary choice ($C_2$ fixed by starting the integral at today),
$F(Q)$ changes sign and diverges in the deep radiation era** ($z\gtrsim10^5$): the
integrand $Q^{-2/3}\Omega_s$ scales as $a^{-26/9}$ there (using $\Omega_s\propto
-0.07\,a^{-4}$, the invoice's own small-negative radiation-era value, and
$Q^{-2/3}\propto a^{10/9}$) — a genuinely divergent integrand, not a numerical
artifact (reproduced identically after fixing the integration-grid issue). Whether
this divergence is physical or an artifact of the reference-point choice depends
entirely on **where $C_2$ is anchored** — exactly the same category of question
Flag 1 raised for $C_1$, but for a *different* constant, arising specifically once
the corrected ODE is actually solved (which no prior round had done).

**This is not the same constant as $C_1$.** $C_1$ entered the *original* integrated
$\phi$-equation ($a^3F_Q=16\pi\tilde G\Lambda_M/N+C_1$) and was resolved by past
regularity acting on the $a^{-3}$-scaling dust mode it represents. $C_2$ is the
homogeneous solution of *this* ODE ($F\propto Q^{2/3}$) — a solution that only
appears once $C_1=0$ is substituted and the resulting equation for $F$ itself is
actually integrated. It has not been discussed by either advisory, because the
quadrature had not yet been run.

*Correction, 2026-07-13 (see `Update-WP3-C2KernelConfirmed-2026-07-13.md`): the
$\rho\propto a^{-10/9}$ figure above is the density this mode would carry under the
**old**, $\phi$-sector-only accounting ($\rho\propto-(F-QF_Q)$). Under the
**corrected** accounting — the actual constraint this quadrature solves,
$\tfrac12QF_Q-\tfrac13F$ — this mode is the operator's kernel and contributes
identically zero. The distinction matters and is not cosmetic; see the confirmation
update for the resolution this implies.*

**Following the now-established discipline (do not anchor arbitrarily at today; use
the Maggiore-Mancarella-style deep-RD anchor, checked for insensitivity, or the exact
past-regularity scaling argument the fifth-round addendum used for $C_1$) rather than
picking $C_2=0$-at-today by convenience** — this has not yet been done. The $a^{-10/9}$
scaling is mild enough that a naive "does it diverge relative to radiation ($a^{-4}$)"
check would say no (it's subdominant) — but the $C_1$ episode already showed that
"subdominant-looking" is not the same as "harmless," since $C_1$'s own $a^{-3}$ scaling
looked subdominant to radiation too until weighted correctly against $Q$. The correct
resolution needs the same care, not an assumption by analogy.

---

## 4. Status

The escalation gate the adjoint-invariant round closed was for the $p_{\mathcal N}$
stability question specifically — that is genuinely resolved. Running the actual
quadrature it cleared the way for has surfaced a new, structurally similar but
distinct question (a second integration constant) that no round has addressed. Not
proceeding to fix $C_2$ by the same convenient-but-unjustified choice that would have
been made for $C_1$ if the fourth-round addendum hadn't caught it. Reporting before
choosing, per the pattern that has caught a real issue in essentially every round
this program has run.
