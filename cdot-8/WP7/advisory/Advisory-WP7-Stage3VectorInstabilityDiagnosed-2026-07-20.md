# Advisory — WP7 Stage 3's Fast-Onset Blowup Diagnosed: a Genuine, Large, Real Eigenvalue in the Untested Vector Sector, Switched On by the $\Pi$-Feedback Term Above a Tiny Critical $k$ — One Normalization Question Left Open, Not Adjudicated (for `cdot-8/WP7/`)

*2026-07-20. Advisory in response to §32 of
`Update-WP7-PerturbationStructure-2026-07-18.md` (Stage 3's checkpoint).
Diagnostic in `wp7_stage3_vector_stiffness_audit.py`, reusing
`wp7_stage3_field_variable.py`'s own trajectory and the Stage-2-confirmed
$d\mathcal K/d\mathcal Q=-\tfrac12\mathcal F_Q$ coefficient. Gate 1(b)
carried. **Verdict up front: the blowup is real and precisely
characterized, not a numerical-conditioning issue — a genuine large
positive real eigenvalue in the $(\alpha,\mathcal E_\alpha)$ subsystem's
own local dynamics, confined to $\kappa$ above a tiny, epoch-dependent
critical value, switched on entirely by the $\Pi$-feedback term (setting
$\kappa=0$ gives a stable, damped complex pair at every epoch checked).
This is exactly the sector Stage 0's audit never touched. One thing I
could **not** settle: the $\Pi$-formula's own $\kappa$/$a^2$-Fourier
normalization — the one sub-term Stage 2's contract didn't separately
itemize — and two plausible conventions I tried by hand give very
different answers. Recommend resolving that specific normalization
before deciding whether this is a real physical feature of the theory
(requiring quasi-static/slaved treatment) or partly a units artifact.**

---

## 1. §32 accepted — the checkpoint call was right

Two solo attempts already failing at the same general wall (§25, §26)
and now a *third*, more carefully-closed attempt (§32) hitting a
different, fast-onset failure mode is exactly the pattern this
program's own staging discipline exists for. Checkpointing rather than
patching a third time was the right call, and the dust-sector
improvement (regression $\Phi/\Phi_i=0.50$ by $z=0$, better than §24's
own $2.4\times$ growth) and the $\chi=\bar Q(\theta_s+\alpha)$
simplification are genuine, independent progress worth keeping
regardless of how the vector sector resolves.

## 2. The diagnosis: a real, large, $\kappa$-driven eigenvalue in a sector never audited

Stage 0 (`wp7_stiffness_audit.py`) checked only the scalar condensate
sector's effective mass ($\mu_\text{eff}^2\propto\mathcal F_{QQ}$,
exonerated, $|\mu_\text{eff}|/H<1$ everywhere). It did not touch the
vector sector's own $(\alpha,\mathcal E_\alpha)$ dynamics. Built the
local $2\times2$ Jacobian of that pair alone (freezing $\delta_s,
\theta_s,\Phi$ as external, slowly-varying sources — the standard way
to audit a fast subsystem independent of the slow one it's embedded
in), reusing the trajectory and the confirmed Stage-2 coefficient
directly:

- **At $z=100$, $k=10^{-4}\,\text{Mpc}^{-1}$** (the exact case that
  blew up in §32): eigenvalues $\{-13.2,\ +485\}$ — a genuine large
  positive real eigenvalue, not a complex/oscillatory pair. At $z=90,
  70,50$: $+347,+159,+59$ — decreasing but still large and real. By
  $z=10$: a stable, damped complex pair, $-0.30\pm5.68i$. **This
  matches the symptom exactly**: reproduced the actual blowup
  ($\delta_b,\delta_s\sim10^{10}$–$10^{22}$ within one step past
  $z=100$) directly from `wp7_stage3_field_variable.py`, unmodified.
- **Setting $\kappa=0$ at $z=100$ gives a stable complex pair**,
  $-0.5\pm8.37i$ — the instability is switched on entirely by the
  $\Pi$-feedback term, not by any other part of the equations (the
  $d\mathcal K/d\mathcal Q\,\chi$ term, the $(H+\bar Q)\chi$ term, and
  the $3c_\text{ad}^2H\bar Q\alpha$ term are all present at
  $\kappa=0$ too, and are stable on their own).
- **Scanning $\kappa$ at fixed $z=100$** shows a clean bifurcation:
  stable complex pair at $\kappa=1.87$, already a small positive-real
  pair at $\kappa=18.7$, growing to $\{-13.2,+485\}$ by
  $\kappa=1871.6$. **The critical $\kappa$ is tiny and translates to a
  tiny comoving $k$**: $k_\text{crit}\approx3.6\times10^{-7}$
  ($z=1090$) to $3.1\times10^{-4}\,\text{Mpc}^{-1}$ ($z=10$) —
  **essentially every cosmologically relevant wavenumber sits on the
  unstable side of this threshold once $z$ is a few tens or more.**
  This is not a corner case restricted to extreme sub-horizon scales.

**Analytic trace, cross-checked against the numeric Jacobian by hand**:
the dominant term in $\partial\dot{\mathcal E}_\alpha/\partial\alpha$
scales as $-(2-\mathcal K_B)^2c_\text{ad}^2\kappa\bar{\mathcal
Q}^2/\big[\mathcal K_BH_c(1+w)\big]$ — quadratic in the background
$\bar{\mathcal Q}$ (which is itself large and legitimately so,
$\bar{\mathcal Q}\propto(1+z)^{5/3}\approx2200$ at $z=100$, an
already-established, correct scaling, not itself a bug), linear in
$\kappa$, linear in $c_\text{ad}^2$ (negative). At $z=100$ this formula
gives $\approx3.7\times10^6$, matching the coded Jacobian's
$3.68\times10^6$ entry to within rounding — confirming the source of
the large eigenvalue is understood, not merely observed.

## 3. What I could *not* settle: the $\Pi$-formula's own Fourier normalization

The imported equation (11) is $\Pi=c_\text{ad}^2\delta-\big[c_\text{ad}^2/
(8\pi\tilde Ga^2\bar\rho)\big]\nabla^2[\mathcal K_B\mathcal E_\alpha+(2-
\mathcal K_B)\chi]$. Converting $\nabla^2$ and $8\pi\tilde G\bar\rho_s$
into this program's own $\kappa\equiv(k/(aH_0))^2$, $\Omega_s(a)$
(today-normalized) convention admits at least two readings that I
worked out by hand and did **not** get to agree:

- **Comoving-Laplacian reading** ($\nabla^2\to-k^2$, no extra $a$):
  gives a prefactor $\kappa/(3\Omega_s)$ on the bracket term — an
  $O(1)$ correction to the code's current bare-$\kappa$ coefficient,
  nowhere near enough to tame a $10^2$–$10^6$-scale eigenvalue.
- **Physical-Laplacian-of-a-comoving-mode reading** ($\nabla^2\to
  -k^2/a^2$, matching how the already-validated Poisson equation's own
  $\kappa$ was built): gives $\kappa/(3a^2\Omega_s)$ — and since $a\ll1$
  at high $z$, this **increases** the coefficient by orders of
  magnitude rather than suppressing it (checked numerically: the
  eigenvalue at $z=100$ grows to $\sim2\times10^6$ under this reading,
  not shrinks).

Neither resolves the instability, and the two readings disagree with
each other by the same $1/a^2$ factor that made the *Poisson* equation
work correctly — meaning I cannot yet rule out that the coded
$\Pi$-term's normalization is simply inconsistent with *itself* in a
way I haven't isolated, only that neither of my two candidate fixes
removes the effect. **This is the one sub-term Stage 2's units contract
did not separately itemize** (Contract Lines 1–4 covered the time
variable, the $\mathcal E_\alpha$ coefficient, the $k$-normalization
used in the *momentum-constraint*-type terms, and background
identifications — none of them re-derived the $\Pi$-formula's own
$8\pi\tilde Ga^2\bar\rho\to$-convention specifically). Recommend this
be written out as an explicit fifth dictionary line, cross-checked
against the same rigor Contract Line 2 got (ideally against the
primary source's own worked example, if one exists, or by an
independent route such as comparing to how a standard $\Lambda$CDM dark
energy perturbation code implements the analogous $c_s^2\neq c_\text{ad}^2$
pressure term) **before** deciding whether the instability found here
is a genuine physical feature or partly a normalization artifact.

## 4. What this does and does not mean for the theory

**If the normalization is confirmed correct as coded**: this is a real,
structural finding, not a bug — the vector sector has a genuine
fast-growing mode for essentially all cosmologically relevant $k$ once
$z\gtrsim$ a few tens, sourced by the same negative $c_\text{ad}^2$
already established in §23/§26 (the sign that makes the scalar sector
*cluster*, per §27's tachyonic-mass finding, may be the same sign
responsible for destabilizing the *vector* sector's explicit evolution
here). In that case the correct numerical treatment is very likely
**not** a further explicit-ODE patch but a **quasi-static/slaved
treatment of $(\alpha,\mathcal E_\alpha)$ for $\kappa$ above the
critical threshold** — structurally the same move standard Boltzmann
codes make for tightly-coupled or fast free-streaming sectors: solve
the *algebraic* quasi-equilibrium condition (setting $\dot{\mathcal
E}_\alpha\approx0$ relative to the other terms, in the regime where
that's justified) rather than integrate the stiff ODE explicitly.

**If the normalization is not correct as coded**: fixing it may remove
the instability's onset threshold and change the picture substantially
— this is why I'm not recommending the quasi-static route yet as the
single next action; the normalization check should come first, since
it's cheaper and could make the whole question moot.

**Not affected either way**: the dust-sector regression result (§32's
own genuine win, $\Pi=0$ throughout), the scalar condensate mass and
stability sign (§7/§27/§28/§30, all specific to $\mathcal F_{QQ}$, not
this term), and Stage 2's own confirmed contract lines 1–4.

## 5. Recommendation

1. Write out the $\Pi$-formula's $8\pi\tilde Ga^2\bar\rho\to
   3H_0^2\Omega_s(a)$-and-Laplacian substitution as an explicit,
   independently-cross-checked dictionary line (the fifth), resolving
   the comoving-vs-physical-Laplacian ambiguity found here.
2. If the coefficient survives that check unchanged, treat the
   instability as physical and design a quasi-static/slaved closure for
   $\kappa>\kappa_\text{crit}(z)$ rather than attempting a fourth
   explicit-ODE pass.
3. Either way, this is exactly the kind of finding that should get a
   dedicated stage of its own (call it Stage 3b: the $\Pi$-normalization
   check) rather than being folded silently into the next full attempt
   — small, sharply scoped, and it gates everything downstream of it.

## 6. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, the $Q_2$/EFE
sequencing decision, and KATRIN watch are unchanged. `references/`
was not needed this round — the primary source's eq. (11) is already
quoted correctly in §25; the ambiguity is in this program's own
*conversion* of it, not in what the paper says.

## Companion

- `wp7_stage3_vector_stiffness_audit.py` — the Jacobian construction,
  the $\kappa=0$ stability check, and the critical-$\kappa$ scan, all
  reproducible end to end from `wp7_stage3_field_variable.py`'s own
  trajectory.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage3VectorInstabilityDiagnosed-2026-07-20.md`.
