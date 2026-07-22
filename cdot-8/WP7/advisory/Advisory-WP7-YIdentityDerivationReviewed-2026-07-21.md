# Advisory — §5's $\mathcal Y$-Identity Derivation Confirmed (Bug-Fix Included), and the "Uniform Substitution Too Crude" Finding Independently Verified Directly From the Action — With a Concrete, Grounded Path Through the Remaining Attribution Problem (for `cdot-8/WP7/`)

*2026-07-21. Review of `Advisory-WP7-RecourseRoundAssessed-2026-07-21.md`
(main advisor, §4 of `Update-WP7-InstabilityRecourses-2026-07-21.md`)
and the worker's subsequent progress (§5): the first piece of the
commissioned action-level FRW derivation. Gate 1(b) and Gate 4 both
carried. **Verdict up front: the main advisor's §4 assessment stands —
nothing here revisits it. §5's own result reproduces exactly under an
independent rerun of the symbolic derivation, including the bug the
worker caught and fixed. The worker's own caution — that R1's "uniform
substitution" hypothesis is now known to be too crude — is not just
plausible, it is directly confirmed by reading the actual action in the
primary source: $(2-\mathcal K_B)$ appears in at least three structurally
distinct places (a bare $-(2-\mathcal K_B)\mathcal Y$ term, a separate
$+2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi$ term, and implicitly through
$\mathcal F(\mathcal Y,\mathcal Q)$ itself), only one of which receives
an $F_\mathcal Y$ correction. A further, useful negative result: the
paper's own linear-perturbation section was derived with $\mathcal
Y\equiv0$ built in from line 1, so there is no shortcut to be found by
reading further in the primary source — the attribution work is
necessary, not avoidable. The worker's own proposed shortcut (vary the
new term alone, add linearly) is mathematically sound and, combined
with the structural clue below, gives a concrete, bounded next step.**

---

## 1. §4 (main advisor's round assessment) — reviewed, nothing to add

Already cross-checked in full in
`Advisory-WP7-R0R1R2CrossCheck-2026-07-21.md` (this file's immediate
predecessor), which covered R0/R1/R2 themselves. The three additions in
§4 ((a) $\lambda_s\to-1$ as "honest dust," (b) the $\lambda_s>0$
tension's scale location at $k\lesssim\mu$, (c) the $\mathcal K_B$-squeeze
protecting the vector-mass corner) are each independently checkable
claims dressed as reframings rather than new numerics, and
`r1_viability_additions.py`'s two verified numbers ($\mu$'s
$11$–$56\times$ separation from the ISW band; $M^2/\mathcal Q_0^2
\approx8$ at the pulsar-squeezed $\mathcal K_B$ even at $(1+\lambda_s)=
10^{-5}$) were not independently rerun again here since they were
already the main advisor's own new script, not the worker's, and
nothing since has cast doubt on them. Standing.

## 2. §5's core result — reran the symbolic derivation independently, matches exactly

Ran `wp7_derivation_Y_identity.py` directly rather than reading the
printed output on trust:

```
Y via D_mu-projection identity, eps^2 coefficient:
(dalpha**2*phibar_dot**2 + 2*dalpha*dvarphi*phibar_dot + dvarphi**2)/a**2

Y via direct sum (g^{mu nu} grad grad + Q^2), eps^2 coefficient:
(dalpha**2*phibar_dot**2 + 2*dalpha*dvarphi*phibar_dot + dvarphi**2)/a**2

Both methods agree: True

Predicted (1/a^2)(d_i chi)^2, chi = varphi + phibar_dot*alpha:
(dalpha*phibar_dot + dvarphi)**2/a**2
Matches exactly: True
```

**Confirmed: $\mathcal Y=a^{-2}(\nabla_i\chi)^2$ to quadratic order,
exactly as claimed**, with $\chi\equiv\varphi+\dot{\bar\phi}\alpha$ —
the same $\chi$ already load-bearing throughout this program's imported
system (it is literally the paper's own line-433 definition, confirmed
directly: *"Setting $\chi\equiv\varphi+\dot{\bar\phi}\alpha$..."*). The
claimed exact algebraic identity ($D_i\phi=\partial_i\chi$, from
$D_\mu\phi\equiv\nabla_\mu\phi+A_\mu\mathcal Q$ being the
$A$-orthogonal projection) is not asserted but *demonstrated* by the
script itself: it computes $\mathcal Y$ two structurally independent
ways (direct sum vs. projection) and shows they agree — the right way
to earn trust in an identity, not cite it.

**The bug-fix is genuine and correctly diagnosed.** Re-derived the
$O(\epsilon^2)$ correction to $A_0$ independently: the unit constraint
$A^\mu A_\mu=-1$ with $g_{00}=-(1+2\epsilon\Psi)$ (i.e. $A_0=-\sqrt{-g_{00}}$
when $A^i=0$ at the order needed) expands to $A_0=-(1+2\epsilon\Psi)^{1/2}
=-1-\epsilon\Psi-\tfrac12\epsilon^2\Psi^2+O(\epsilon^3)$ **before** the
spatial part of the constraint is folded in; once $A_i=\epsilon\,
\partial_i\alpha\neq0$ is included, the full unit constraint at
$O(\epsilon^2)$ pulls in an additional $-\tfrac1{2a^2}(\nabla\alpha)^2$
piece from $g^{ij}A_iA_j$ term entering the constraint at the same
order. This matches the script's $\delta_2=-\dfrac{(\nabla\alpha)^2}
{2a^2}+\dfrac{\Psi^2}2$ exactly. **The catch method (compute the same
quantity two independent ways, distrust either until they agree) is
exactly the discipline this program has needed every time a coefficient
derivation has come up** — worth naming as a positive pattern to keep,
not just a bug fixed.

## 3. The "uniform substitution too crude" finding — independently confirmed directly from the action, not just from the worker's own reasoning

Read the primary source's full covariant action (`newRMONDLett.tex`,
lines 336–347) directly, since §5 references it but the compact update
document doesn't quote it verbatim. It reads:

$$S=\int d^4x\frac{\sqrt{-g}}{16\pi\tilde G}\Big[R-\frac{\mathcal K_B}2
\hat F^{\mu\nu}\hat F_{\mu\nu}+2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi
-(2-\mathcal K_B)\mathcal Y-\mathcal F(\mathcal Y,\mathcal Q)-\lambda(
\hat A^\mu\hat A_\mu+1)\Big]+S_m[g]$$

**This confirms, independently and more strongly than the worker's own
write-up states it, exactly the concern §5 raises.** $(2-\mathcal K_B)$
appears in **three** structurally distinct places in the bare action
itself, before $\mathcal F(\mathcal Y,\mathcal Q)$ is even expanded:

1. the bare $-(2-\mathcal K_B)\mathcal Y$ term — **this** is the one
   §5's derivation correctly shows gets the $F_\mathcal Y(0,\bar{
   \mathcal Q})$ addition, since expanding $\mathcal F(\mathcal Y,
   \mathcal Q)=F(0,\mathcal Q)+F_\mathcal Y(0,\mathcal Q)\mathcal Y+
   O(\mathcal Y^2)$ combines with it to give total coefficient
   $-(2-\mathcal K_B)-F_\mathcal Y(0,\bar{\mathcal Q})$, i.e. exactly
   $(2-\mathcal K_B)\to(2-\mathcal K_B)+F_\mathcal Y(0,\bar{\mathcal Q})$
   — matching the paper's own $F_\mathcal Y\equiv(2-\mathcal K_B)
   \lambda_s$ convention, this **is** $(2-\mathcal K_B)(1+\lambda_s)$;
2. the separate $+2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi$ term
   ($\hat J_\mu\equiv\hat A^\alpha\nabla_\alpha\hat A_\mu$, built purely
   from the aether's own covariant acceleration) — **this term carries
   the same bare $(2-\mathcal K_B)$ coefficient but is not part of
   $\mathcal F(\mathcal Y,\mathcal Q)$ at all**, so it receives **no**
   $F_\mathcal Y$ correction under any admissible completion;
3. whatever $(2-\mathcal K_B)$-proportional pieces already exist
   implicitly inside $F(0,\mathcal Q)$'s own background-level
   contributions (already present in the existing, Y=0 derivation, and
   already correctly handled there — not a new concern).

**So the worker's own caution is not merely "possible" — it is
structurally guaranteed by the action's own form.** Any occurrence of
$(2-\mathcal K_B)$ in the already-derived $\chi$/$\Pi$/$\mathcal
E_\alpha$ formulas (`newRMONDLett.tex` lines 437, 456, 481–489) that
traces back to source (1) needs the $F_\mathcal Y$ correction; anything
tracing to source (2) does not; and the paper's own compact
presentation gives no way to tell which is which just by inspection —
confirming exactly what §5 already concluded.

## 4. A useful negative result: there is no shortcut to be found by reading further in the primary source

Checked directly: the paper's entire linear-perturbation section
(lines 425–490, the one this whole WP7 arc imports from) is derived
**with $\mathcal Y\equiv0$ assumed from its very first line** ("perturb
the scalar as $\phi=\bar\phi+\varphi$ and the vector as $\hat A_\mu=\{-1
-\Psi,\nabla_i\alpha\}$" — i.e. $\mathcal Y=0$ is never carried as a
free quantity anywhere in this derivation; the paper had no reason to,
since its own stability analysis of $F_\mathcal Y\neq0$ lives entirely
in the separate Minkowski-background section). **This means the
attribution question §5 poses cannot be resolved by finding an
already-worked-out general-$\mathcal Y$ version of $\chi$/$\Pi$/
$\mathcal E_\alpha$ anywhere in this source** — it doesn't exist here.
The worker's "harder remaining piece" is a genuine, necessary, original
derivation, not something a more careful reading would shortcut.
Worth stating explicitly so effort isn't spent re-searching the text
for a formula that isn't there.

## 5. The worker's proposed shortcut is valid — with one sharpening

§5 proposes: rather than redo the entire coupled variation, compute the
correction to the equations of motion by varying $-F_\mathcal Y(0,\bar{
\mathcal Q})\mathcal Y$ **alone** and adding it linearly to the paper's
already-derived (F_Y=0) equations. **This is mathematically sound, and
worth confirming explicitly why**: $\mathcal Y$ is exactly zero on the
background and, per §5's own result, starts at *quadratic* order in
perturbations with no linear piece. Since the action must be expanded
only to quadratic order to produce linear-order equations of motion,
$F_\mathcal Y(0,\bar{\mathcal Q})\cdot\mathcal Y$ is already the
complete contribution from $\mathcal F(\mathcal Y,\mathcal Q)$'s
$\mathcal Y$-dependence at this order — no higher term in the Taylor
expansion, and no linear-in-perturbation correction to the coefficient
itself (which would require a term linear in $\delta\mathcal Q$
multiplying $\mathcal Y$, i.e. cubic order overall, negligible), enters.
Varying the action is linear in its own terms, so this one new term's
contribution to the field equations can indeed simply be added to what
already exists — standard, correctly reasoned.

**The sharpening**: because this new term is *functionally identical*
to the bare $-(2-\mathcal K_B)\mathcal Y$ term already in the action
(same $\mathcal Y$, different coefficient), its contribution to every
field equation must have **exactly the same functional form** as that
bare term's own contribution, differing only by an overall factor of
$F_\mathcal Y(0,\bar{\mathcal Q})/(2-\mathcal K_B)=\lambda_s$ (using the
paper's own convention). **This turns the attribution problem into a
narrower, more tractable one**: rather than deriving the new term's
contribution from scratch, it is enough to identify — within the
already-published $\chi$, $\Pi$, $\mathcal E_\alpha$ formulas — which
specific $(2-\mathcal K_B)$-proportional pieces trace to the bare
$\mathcal Y$-term's own variation (source (1) above) as opposed to the
$\hat J^\mu\nabla_\mu\phi$ term's (source (2)). Every piece in the
first category picks up the same relative $\lambda_s$ correction the
new term contributes automatically (by the functional-identity
argument above, with no further variation needed); every piece in the
second category does not. This is still real work — it requires
knowing which terms in the (unpublished, only-results-shown) full
derivation came from varying $\mathcal Y$ specifically — but it is
bounded and checkable (e.g. by symbolic re-derivation of just the
Einstein $0i$/vector-equation pieces sourced by $\mathcal Y$ alone,
reusing exactly the same $\chi$-projection machinery §5 already built,
rather than re-deriving the full system with matter/Einstein tensors
included).

## 6. Overall assessment

§5 is genuine, correctly verified progress, not merely asserted — the
symbolic identity reproduces exactly, the bug-fix is legitimate and
correctly diagnosed, and the worker's own caution about "uniform
substitution" being too crude is independently confirmed by the action
itself, more sharply than the worker's own write-up states it (three
structurally distinct sources of $(2-\mathcal K_B)$, not implied
generically). The proposed shortcut for the remaining step is
mathematically valid and, combined with the structural clue above
(match the functional form of the bare $\mathcal Y$-term, not every
occurrence of $(2-\mathcal K_B)$), gives a concrete, bounded path
forward rather than requiring the full from-scratch coupled variation
the worker was bracing for. **Recommend the worker proceed on this
narrower footing**: identify the $\mathcal Y$-sourced pieces of
$\chi$/$\Pi$/$\mathcal E_\alpha$ specifically (reusing the
$\chi$-projection identity already established), rather than the full
system, as the next checkpoint. Gate 4 remains paused — this is still
diagnostic/derivation work informing a possible future recourse, not a
resumption of the ISW/growth track itself. Nothing in `cdot-7/` was
touched.

## Companion

- No new script — verification reused
  `wp7_derivation_Y_identity.py` directly, plus a direct read of
  `references/arXiv.2007.00082/newRMONDLett.tex` (lines 336–490,
  covering both the full covariant action and the linear-perturbation
  section) for the action-structure and no-shortcut findings.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-YIdentityDerivationReviewed-2026-07-21.md`.
