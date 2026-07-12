# Update — WP3: A Distance-Formula Tension Found Upstream of the Closure Constraint

*Companion: `SessionLog-2026-07-12.md` (this directory). This is **not** a completed
WP3 pass. Setting up WP3's actual question (§1) required a definite $H(a)$ for the
census-closed background, which required checking §2's derivation; that check surfaced
a concrete, numerically verified inconsistency (§3–5) between two things WP1 treated as
compatible. This is reported now, unresolved, rather than pushed through to a
kill/no-kill verdict — the finding bears on WP1's own success claim, not only on WP3,
and the right next step is a judgment call, not a unilateral one. Per K6, escalated
rather than smoothed over.*

---

## 1. Setting up WP3's actual question

M5 ($c^2=\kappa g_hR_h$ as a nonlocal constraint) combined with the AQUAL closure
($\mu(x)g_h=GM_h/R_h^2$) and $M_h=\mathcal N m_P$ (WP2) is, algebraically, already
cdot-7's *entire* closure ODE — it doesn't yet involve $Q(t)$ or AeST's field equations
at all. $Q(t)$ enters only through $a_0=\lambda\dot c\leftrightarrow$ some function of
$Q_0(t)$ (M2). So the real WP3 question is: **does AeST's own Friedmann equation**
($H^2=\frac{8\pi\tilde G}3\rho-\frac13(F-QF_Q)+\Lambda/3$, WP0 extraction) **admit a
solution whose $H(t)$ matches what cdot-7's closure ODE already requires** — checking
whether *some* admissible free function $F(Q)$ closes the gap, rather than assuming one
does. This requires knowing, concretely, what $H(a)$ cdot-7's closure demands. That
computation is what surfaced the problem below.

---

## 2. What $H(a)$ cdot-7's own fixed point requires, via WP1's dictionary

On the matter fixed point ($x=x_*$ const), $R_h\propto c^{3/4}$ and $\dot R_h=c$ give,
solved directly: $c(t)\propto|t-t_*|^{-4}$ near the future runaway, and $c(t)\propto
|t|^{-4}$ as $t\to-\infty$ (eternal past — matching Foundation §2.2's own statement,
"the backward attractor to $c\to0$ as $w\to\infty$"). Via WP1's forced $c(t)=c_0(a(t)/
a_0)^{2/3}$: $\dot c/c=\tfrac23H\Rightarrow H\propto c^{1/4}\propto a^{1/6}$.

**Cross-check before trusting this**: does $H\propto a^{1/6}$ reproduce Foundation
§5.4's independently-stated deep-MOND result, $a_0\propto c^{5/4}$? Using $a_0=\lambda\dot
c=\lambda c\cdot\tfrac23H$ with $c\propto a^{2/3}$, $H\propto a^{1/6}$: $a_0\propto
a^{2/3+1/6}=a^{5/6}=(c^{3/2})^{5/6}=c^{5/4}$. **Exact match** to Foundation's own quoted
exponent, obtained independently here. This cross-check passed convincingly, giving
confidence $H\propto a^{1/6}$ is the correct reading of cdot-7's own fixed point, not a
slip in this session's algebra.

---

## 3. The distance-formula check

A genuinely covariant proper distance for a flat FRW background with this $H(a)$:
$$D_p(z)=a_0c_*\int_{a_e}^{a_0}\frac{da}{a^2H(a)}=a_0c_*\int\frac{da}{a^2H_0(a/a_0)^{1/6}}
=\frac{6c_*}{7H_0}\left[(1+z)^{7/6}-1\right],$$
an **unbounded** function of $z$. Compare cdot-7's own quoted result (Foundation §5.2):
$$D_p^\text{cdot-7}(z)=R_{h,0}\left[1-(1+z)^{-1/2}\right],$$
**bounded**, approaching a finite particle horizon as $z\to\infty$. These are not close —
one diverges, the other saturates. Sanity check on the calculation method: substituting
literal EdS ($H^2\propto a^{-3}$, i.e. $\Omega_m=1$, the case the formula is *named*
for) into the identical integral gives $D_p(z)=\frac{2c_*}{H_0}[1-(1+z)^{-1/2}]$ —
**exactly cdot-7's quoted formula**, confirming the integration method is right and that
the quoted formula is genuinely the literal-EdS ($H^2\propto a^{-3}$) result, not some
other convention.

---

## 4. Confirming this isn't a slip — the same mismatch from cdot-7's own algebra alone

Independent of any $a(t)$ identification: cdot-7's own $R_h\propto c^{3/4}$ combined
*only* with the redshift law ($c_z/c_0=(1+z)^{-2/3}$) gives, directly,
$$D_p(z)\equiv R_h(t_0)-R_h(t_e)=R_{h,0}\left[1-(c_z/c_0)^{3/4}\right]
=R_{h,0}\left[1-(1+z)^{-1/2}\right]$$
— **matching cdot-7's quoted formula exactly**, with no reference to $a(t)$ needed.
Combined with §3's finding that *this same formula* requires $H^2\propto a^{-3}$
covariantly, while §2 independently derives $H^2\propto a^{1/3}$ from the *same* fixed
point via the *same*, separately-forced redshift-law identification $c\propto a^{2/3}$
— **the two calculations of "$H(a)$ implied by the fixed point" disagree with each
other**, depending on whether one goes through $R_h\propto c^{3/4}$ (giving $a^{1/3}$)
or demands the quoted distance formula hold covariantly (requiring $a^{-3}$).

---

## 5. What this means, stated as precisely as it can be at this point

**Robust, unaffected by this finding**: the redshift law itself, and the *local*,
single-epoch Planck-unit exponents (mass $c^{1/2}$, length $c^{-3/2}$, frequency
$c^{5/2}$) — these are instantaneous statements about a single photon or a single fixed
object, not integrals over the trajectory, and nothing above touches them.

**In question**: cdot-7's own $R_h(t)\equiv\int c(t')dt'$ is built entirely within its
static-space ontology (premise 1 — no scale factor at all, by construction) and its own
closure ODE ($\dot R_h=c$, $\dot c=c^2/(\kappa\lambda xR_h)$) determines $c(t)$'s *actual*
history self-consistently. **That history, mapped to $a(t)$ via the redshift-forced
$c\propto a^{2/3}$, is not the same $a(t)$ that would make cdot-7's own claimed
distance formula a genuine covariant distance** — the formula's covariant meaning
requires literal matter-domination ($H^2\propto a^{-3}$), while the closure's actual
solution (via the same dictionary) gives $H^2\propto a^{1/3}$. A single power-law tie
between the bookkeeping $c(t)$ and a covariant $a(t)$ appears unable to make both the
redshift law and the distance formula hold simultaneously as genuinely covariant
statements about the same spacetime — at least under every identification checked here
(comoving distance, proper distance now, proper distance at emission).

**What this is not (yet)**: a proof that no resolution exists. Not checked: whether a
non-power-law, or a two-parameter (not one forced exponent), relation between $c(t)$ and
$a(t)$ resolves it; whether $R_h$ is better read as some other standard distance measure
not yet tried; whether the fixed point specifically (as opposed to the actual, perturbed
$\delta_0\ne0$ four-term-fit trajectory) is simply the wrong object to be checking this
against, given Foundation itself treats the fixed point as an unstable, non-physical
reference solution and the *real* working cosmology as the perturbed trajectory. That
last possibility is the most promising unexplored escape route and is flagged as the
first thing to check next, not ruled out here.

**Consequence for WP3 as chartered**: WP3's question (does AeST's field equations admit
a solution whose $H(t)$ matches what the census closure requires) cannot be posed
precisely without first knowing, unambiguously, what $H(a)$ the closure *does* require
— and this session has shown that depends on a choice (which distance/redshift
quantity is taken as ground truth) that WP1 did not previously recognize as a choice.
**WP3 is therefore not passed, not killed — blocked, pending resolution of this
upstream question**, which is more naturally WP1's to resolve than WP3's.

---

## 6. Recommendation, stated as a decision point rather than a unilateral call

This finding is consequential enough — it touches cdot-7's own four-term SN fit, the
single most validated result in the whole project, once that fit is asked to mean
something in a genuinely covariant spacetime — that how to proceed is the author's call,
not this session's to make alone. Three live options, not mutually exclusive:

1. **Reopen WP1** specifically to resolve which of the redshift law or the distance
   formula (or neither, cleanly) survives contact with a genuine covariant embedding,
   and what that implies for the $c(t)\leftrightarrow a(t)$ dictionary.
2. **Check the actual (perturbed, $\delta_0\ne0$) trajectory** rather than the exact
   fixed point — Foundation itself treats the fixed point as an unstable reference
   solution, not the physical trajectory; it is possible (not yet checked) that the
   real, data-fitted trajectory's distance-redshift relation behaves differently enough
   from the fixed point's that this tension is an artifact of checking the wrong
   solution.
3. **Treat this as informative about cdot-7 itself**, independent of cdot-8: if cdot-7's
   own $R_h$/$D_p$ formula does not correspond to a genuine covariant distance for *any*
   sensible embedding, that is worth knowing about cdot-7's four-term fit's own
   interpretation, whether or not cdot-8 proceeds.

No file in `cdot-7/` is touched by this session — this is reported entirely within
cdot-8's own space, as WP0's charter requires (cdot-7 stands unaffected pending
resolution).
