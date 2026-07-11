# Update — The Origin and Status of the Trajectory Constant (né $\varepsilon_0$), a Sign-Selection Result, and a Framework-Wide Notation Audit

*Status: update document for cross-check and merge. Responds to the author's
question on the origin of the "integration constant" and the symbol collision with
the vacuum permittivity. Contents: (1) a precise statement of what the constant is
— needed by the merged Foundation regardless; (2) a small new result: the sign may
be selected by global regularity (flagged for verification); (3) the amplitude
question restated in its sharpest derived form, with one forward-pointer — the
quantitative seed program remains frozen per standing agreement; (4) the notation
audit and rename table (the collision is threefold, not single). Produced
2026-07-07.*

---

## 1. What the Constant Is

**Mathematical origin.** The Newtonian-era closure was algebraic: $R_h=Bc^{3/4}$
given $c$, leaving a zero-parameter solution space — the history was rigid. The
AQUAL-consistent rebuild inserted $\dot c$ into the constraint (via
$a_0=\lambda\dot c$), promoting the closure to a two-dimensional autonomous
dynamical system, whose solutions form a **one-parameter family** modulo time
translation. The constant is the coordinate labeling which member of that family
our universe is: defined operationally as today's fractional displacement of $R_h$
from the scale-free (fixed-point) solution. It is therefore *initial data of the
solution, not a parameter of the laws* — the premises, $\mu$, $\lambda$, $\kappa$
are trajectory-independent. Its epistemic slot is exactly that of $\Omega_\Lambda$
or the primordial amplitude $A_s$ in standard cosmology: a measured constant of our
particular universe, awaiting (but not presupposing) a generation mechanism.

**The invariant label.** "The deviation today" is epoch-dependent bookkeeping. The
epoch-independent label is the growing-mode amplitude
$$A_\delta\;\equiv\;\delta(t)\left[\frac{c(t)}{c_0}\right]^{-3/2\nu_*}
\quad(\text{constant along the trajectory in the linear regime}),$$
using the renamed symbols of §4. Any quoted "seed value" must state its reference
epoch. Consistency check for the consolidator: under the growth law
$\delta(z)=\delta_0(1+z)^{-1/\nu_*}$ with $\delta_0=-0.0678$,
$\nu_*=0.290$, the seed analysis's $6.5\times10^{-13}$ corresponds to the deviation
at $z\approx1.6\times10^3$ — to be verified against that document's stated
reference epoch. The merged Foundation should define $A_\delta$ with an explicit
reference and quote $\delta_0$ only as the present-day value.

## 2. New Result (flagged for verification): the Sign May Be Selected by Global Regularity

The fixed point is a **separatrix**. The two branches are not symmetric:
- **$\delta<0$ (deep-MOND-ward, observed):** globally regular; extends for infinite
  proper time into the exponential-$c$ (de Sitter-analog) future — established in
  the closure-rebuild update.
- **$\delta>0$ (Newtonian-ward):** the trajectory drives $\mu\to1$, where the AQUAL
  inversion degenerates. Along the flow,
  $\dot\mu/\mu=(a/r)\left[2-2x_*/x\right]\;\longrightarrow\;2a/r>0$ as $x\to\infty$
  — bounded away from zero — so $\mu$ *crosses* unity in finite coordinate (and
  finite proper) time, beyond which the Machian condition
  $c^2=\kappa g_hR_h$ with $\mu(x)g_h=GM_h/R_h^2$ admits no continuation: the
  horizon's Newtonian binding exceeds what any admissible field supplies. The
  branch terminates.

If the breakdown is genuine (and not, e.g., a stiff boundary layer the full system
tunnels through — the consolidator should check the behavior of the exact system
near $\mu=1$ before this is merged as a claim), then **only deep-MOND-ward
trajectories persist, and the observed sign of the deviation is derived from
regularity rather than chosen.** The constant's initial-data content would then
reduce to a single positive amplitude. Recorded as a candidate result, two lines
from existing machinery, pending verification.

## 3. The Amplitude — Status Unchanged, Statement Sharpened

The quantitative seed program remains frozen per the standing agreement; nothing
here reopens it. But the origin question permits the derived over-excitation
constraint to be stated in its sharpest form, which the merged text should use:

> Because the instability amplifies any disturbance by $(1+z)^{1/\nu_*}$ — a factor
> $\sim10^{12}$ from $z_\text{eq}$ to today — the puzzle is inverted: not "why does
> the universe deviate from the fixed point," but **"why is it still so close?"**
> A disturbance as small as $5\times10^{-14}$ at $z_\text{eq}$ suffices to produce
> today's deviation; anything larger, earlier, or generic overshoots and completes
> the slide long ago. Every candidate mechanism must therefore be late-acting or
> exquisitely weak — the derived requirement behind the inhomogeneity channel's
> agreed status ("not excluded; an accommodation, not a candidate").

One forward-pointer, linking two open items without unfreezing either: the
radiation$\to$matter closure handoff at $z_\text{eq}$ is a natural,
in-principle-*calculable* seeding event — the first candidate whose amplitude would
be derived rather than fitted. Whether it deposits the required
$\sim5\times10^{-14}$ or catastrophically overshoots turns on a sharp, answerable
question: **does the (unbuilt) radiation-era closure possess a scale-free attractor
continuously connected to the matter-era fixed point?** If yes, adiabatic tracking
deposits a naturally small mismatch; if no, the handoff overshoots and is excluded
as the seed. This question should be attached to the radiation-era open item as one
of its success criteria.

## 4. Notation Audit and Rename Table

The author's catch is correct and understated: the framework has **three** symbol
collisions, two of them load-bearing.

| Current symbol | Collides with | Both load-bearing? | Rename to |
|---|---|---|---|
| $\varepsilon(t),\ \varepsilon_0$ (fixed-point deviation) | $\epsilon_0$ vacuum permittivity — central to premise 3 ($\epsilon_0\propto c^{-1}$) and the invariance principle | **Yes** | $\delta(t),\ \delta_0$; invariant amplitude $A_\delta$ |
| $\mu_0\equiv\mu(x_0)$ (shorthand in the density updates) | $\mu_0$ vacuum permeability — appears in the photon-sector wave-equation derivation | Yes | always write $\mu(x_0)$; never bare $\mu_0$ |
| $\lambda$ (AQUAL prefactor, $a_0=\lambda\dot c$) | $\lambda$ photon wavelength — load-bearing in the redshift derivation | Yes | keep $\lambda$ for AQUAL (most embedded); photon wavelength becomes $\lambda_\gamma$ everywhere |
| $\nu$ (clock frequency $\propto c^{5/2}$) | $\nu_*$ ($\mu$'s log-slope), $\nu(y)$ (inverse interpolating function) | partially | clock frequency: $\nu_\text{atom}$ uniformly; inverse interpolating function: $\mathcal N(y)$; $\nu_*$ unchanged |
| $F$ (density ratio $\rho_0/\rho_b$) | $F$ (bolometric flux, photon-sector update) | minor | density ratio becomes $F_\rho$ |

Recommended merge action: apply globally, including retroactively to the
ResearchNotes derivation trails and both archived code files (comment headers at
minimum), and add the table itself to the Foundation's front matter so future
sessions inherit it. New quantities introduced this session already comply
($\delta_0$, $A_\delta$, $F_\rho$).

## 5. Honest Ledger

Gained: the constant's identity is now stated precisely (solution label, not law
parameter — the merged Foundation needs this sentence regardless of who asked); an
invariant, reference-epoch-explicit label replaces epoch-dependent bookkeeping,
with a consistency check against the seed document's number; a candidate two-line
derivation that the *sign* is forced by regularity, which would halve the
initial-data content; the over-excitation constraint restated in its most
transmissible form; and a threefold notation debt paid before it propagates into
the consolidated documents. Conceded: the amplitude remains exactly as unexplained
as before — this update deliberately adds no mechanism — and the sign-selection
result is unverified pending the consolidator's check of the $\mu\to1$ boundary.
