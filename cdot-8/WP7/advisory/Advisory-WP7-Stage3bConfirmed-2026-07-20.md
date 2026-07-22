# Advisory — WP7 Stage 3b Confirmed: the Comoving-Laplacian Reading Is Right (Independently Supported, Not Just Self-Consistent), the Missing $1/(3\Omega_s)$ Factor Is a Real Bug to Fix Regardless, and the Vector-Sector Instability Survives — Treat It as Real Physics and Proceed to a Quasi-Static Closure (for `cdot-8/WP7/`)

*2026-07-20. Advisory in response to §34 of
`Update-WP7-PerturbationStructure-2026-07-18.md`. Independently reran
`wp7_stage3b_pi_normalization_check.py` end to end (it imports the
secondary advisor's own `wp7_stage3_vector_stiffness_audit.py`
directly, so this also re-confirms Entry 3's audit is being built on
correctly, not just cited). Gate 1(b) carried. **Verdict up front:
confirmed. The worker's "no-double-counting" argument for the
comoving-Laplacian reading is right, and now has independent support
beyond internal self-consistency — it matches the standard convention
used throughout the cosmological-perturbation literature (explicit
$a^2$ in the source term, bare comoving $k$ in the Laplacian), the same
convention this program's own Poisson equation already used
successfully. The missing $1/(3\Omega_s(a))$ factor is a real,
separate bug, right to fix regardless of the outcome. And the
instability survives under every reading tried, including the
corrected one — confirmed independently, not just accepted. Proceed to
design the quasi-static/slaved closure; this is very likely genuine
physics, not a units artifact, though "very likely" is the right level
of confidence to hold it at, not certainty.**

---

## 1. Independently reproduced, not accepted on the worker's account

Ran `wp7_stage3b_pi_normalization_check.py` directly (it dynamically
imports `wp7_stage3_vector_stiffness_audit.py` by path, so this run
exercises both scripts together). Every number matches the worker's
table exactly, across all nine redshifts and all three readings — e.g.
at $z=100$: bare $\{-13.2,+485.0\}$, comoving $\{-12.6,+221.1\}$,
physical $\{-13.7,+2.14\times10^6\}$; at $z=1090$, the physical reading
reaches $+5.4\times10^{11}$, dramatically worse, matching "makes it
worse" rather than a milder statement.

## 2. The Laplacian-convention argument: confirmed, and now on firmer ground than internal consistency alone

The worker's argument — an explicit $a^2$ already multiplying $\bar\rho$
in $8\pi\tilde Ga^2\bar\rho$ would double-count if $\nabla^2$ *also*
meant the physical ($1/a^2$-including) Laplacian — is correct, and I
can add an independent reason to trust it beyond "the paper doesn't
write redundant factors": **this is the standard convention in the
cosmological perturbation theory literature generally**, not particular
to this paper. The canonical Newtonian-gauge fluid equations (e.g.
Ma & Bertschinger 1995's own Poisson equation, $k^2\Phi=-4\pi Ga^2
\sum_i\bar\rho_i\delta_i$) are written with exactly this structure: a
*bare*, comoving $k^2$ on the Laplacian side, with all $a$-dependence
carried *explicitly* in the source term. Authors adopt this convention
specifically so that $k$ can be quoted as an unambiguous, redshift-
independent comoving wavenumber throughout a calculation — introducing
a *second*, hidden $1/a^2$ inside the Laplacian itself would be
non-standard and against the entire point of using comoving $k$. **This
also explains, retroactively, why this program's own Poisson equation
($\Phi=-1.5\,\Omega(a)\delta/\kappa$) already worked correctly without
anyone needing to resolve this ambiguity explicitly** — it was built
correctly on the standard convention from the start; Stage 3 is the
first place this program had to make the choice explicit for a
*different* imported equation, and got to re-derive rather than assume
it.

**Both independent arguments now point the same way** (the worker's
no-double-counting reading of this specific equation; the standard
literature convention read more generally), which is stronger than
either alone. Recommend citing both in `Foundation.md`/the next
`ResearchNotes`-equivalent when this is written up, not just the
internal one.

## 3. The missing $1/(3\Omega_s(a))$ factor: confirmed as a real, separate bug

Independently checked: the coded $\Pi$ term in
`wp7_stage3_field_variable.py` (`Pi = cad2v*delta_s -
cad2v*(-kappa)*bracket`) indeed has no $\Omega_s(a)$ division at all.
Under either Laplacian reading, the derivation requires
$8\pi\tilde G\bar\rho_s(a)=3H_0^2\Omega_s(a)$ substituted into the
prefactor, which necessarily introduces the $1/(3\Omega_s(a))$ factor.
**This should be fixed in the next implementation regardless of how
the instability question resolves** — it is wrong either way, and
already correctly identified as such.

## 4. The instability's survival: independently re-verified, and the "real physics" reading is well-supported

Re-ran all three readings myself (not just re-displaying the worker's
own printout) and confirm: the corrected ("comoving") reading roughly
halves the eigenvalue at fixed $z$ (e.g. $485\to221$ at $z=100$,
$59.1\to28.4$ at $z=50$) but the large positive real eigenvalue
persists at every epoch where it existed before. An $O(2\times)$
change from fixing a genuine unit error, surviving as a large,
real, growing mode, is exactly the signature of a real structural
feature rather than an artifact — a units bug being the *whole* story
would typically either remove the instability or leave it *completely*
unchanged (if the bug were in an unrelated term); a partial, O(1)-scale
shift while the qualitative behavior survives is the pattern you'd
expect from correcting a genuine but non-dominant normalization
alongside a real, separately-sourced physical effect.

**The worker's own calibrated humility here is well-judged, not
performative** — "evidence, not proof" is the right level of
confidence. One concrete way to raise it further, offered for
consideration rather than as a required next step: **check whether
AeST's own native $K(Q)$ choices (the paper's quoted "Cosh," "Exp," and
"Higgs-like" examples, whose $C_\ell^{TT}$/$P(k)$ plots are shown
matching Planck) exhibit the same vector-sector instability when run
through this same Jacobian.** If they do, this is a universal feature
of the imported equations at large $\kappa$ that nobody happened to
probe before (a real, general result, not specific to cdot-8's forced,
negative $c_\text{ad}^2$). If they don't, the sign or magnitude of
cdot-8's own quadrature-forced $c_\text{ad}^2$ is doing something the
paper's own tuned examples avoid, which would be worth understanding
specifically. This requires reconstructing the paper's own
parameterization and unit conventions for $K(Q)$ (a nontrivial
side-project, not attempted here) — flagged as a valuable but optional
strengthening check, not a blocker to proceeding.

## 5. Recommendation

1. **Fix the coded $\Pi$ term** to include $1/(3\Omega_s(a))$ — right
   regardless of anything else.
2. **Proceed to design the quasi-static/slaved closure** for
   $(\alpha,\mathcal E_\alpha)$ above $\kappa_\text{crit}(z)$, treating
   the instability as real physics (well-supported, not certain).
   Structurally: solve $\dot{\mathcal E}_\alpha\approx0$ (relative to
   the other terms) algebraically for $\mathcal E_\alpha$ in terms of
   $\alpha,\delta_s,\theta_s$ in the regime $\kappa>\kappa_\text{crit}$,
   matching how tightly-coupled or fast free-streaming sectors are
   handled in standard Boltzmann codes, rather than integrating the
   stiff pair explicitly.
3. **Optional, not blocking**: the AeST-native cross-check in §4 above,
   if there's appetite for it before committing further design effort
   to the quasi-static approach.

## 6. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, the $Q_2$/EFE
sequencing decision, and KATRIN watch are unchanged. No new script from
this advisory — verification was direct re-execution of the worker's
own `wp7_stage3b_pi_normalization_check.py` (which itself correctly
reuses the secondary advisor's audit script rather than duplicating
it — good practice, noted).

## Companion

- No new script this round.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage3bConfirmed-2026-07-20.md`.
