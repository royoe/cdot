# Advisory — §7's $\hat J_i=\partial_i\mathcal E_\alpha$ Identity Confirmed Exactly: the Flagged Weak Point Was Real, and the Worker's Response (Compute It, Don't Argue It) Sharpens It Into a Usable Cross-Term — One Concrete Simplification Offered for the Next Step (for `cdot-8/WP7/`)

*2026-07-21. Review of `Update-WP7-InstabilityRecourses-2026-07-21.md`
§7: the worker's direct symbolic check of the weak point flagged in
`Advisory-WP7-RefinedAttributionAssessed-2026-07-21.md` §3. Gate 1(b)
and Gate 4 both carried. **Verdict up front: confirmed exactly by
independent rerun. The concern that $\hat J_\mu$'s spatial component
carries gradient structure was correct, and the worker's own symbolic
derivation (not a qualitative rebuttal, an actual computation through
the perturbed Christoffel symbols) pins it down precisely:
$\hat J_i=\partial_i\mathcal E_\alpha$ exactly, so the base action's
$\hat J^\mu\nabla_\mu\phi$ term's spatial piece is a genuine
$\mathcal E_\alpha$-$\varphi$ gradient cross-term — a third structure,
distinct from both $\mathcal Y$'s pure self-gradient-squared and a bare
friction term. This is good, correctly-run science: a qualitative
objection was resolved by computing the actual quantity rather than by
further argument. One concrete simplification is offered below to make
the next step (varying this term through the full system) more
tractable.**

---

## 1. The identity reproduces exactly

Ran `wp7_derivation_Jhat_identity.py` directly:

```
J_1 (spatial component), to O(eps):
epsilon*(Derivative(Psi(t, x1), x1) + Derivative(alpha(t, x1), t, x1))

Predicted eps*d/dx1(Psi + alpha_dot) = eps*d/dx1(E_alpha):
epsilon*(Derivative(Psi(t, x1), x1) + Derivative(alpha(t, x1), t, x1))

Matches exactly: True
```

**Confirmed: $\hat J_i=\partial_i(\Psi+\dot\alpha)=\partial_i\mathcal
E_\alpha$ exactly**, using $\mathcal E_\alpha\equiv\dot\alpha+\Psi$ —
the primary source's own definition (`newRMONDLett.tex` line 433,
already verified in an earlier round), not a redefinition invented for
this check.

**Spot-checked the computation's own machinery, not just its output**:
the script computes $\hat J_\mu=\hat A^\alpha\nabla_\alpha\hat A_\mu=
\hat A^\alpha(\partial_\alpha\hat A_\mu-\Gamma^\beta_{\alpha\mu}\hat
A_\beta)$ via an explicit Christoffel-symbol construction from the
perturbed $(t,x^1)$ metric ($g_{00}=-(1+2\epsilon\Psi)$, $g_{11}=a^2(1-
2\epsilon\Phi)$) — the standard formula $\Gamma^a_{bc}=\tfrac12g^{ad}
(\partial_bg_{dc}+\partial_cg_{db}-\partial_dg_{bc})$, correctly
implemented (checked index placement and contraction order by hand
against the code, not just trusted the variable names). The
reduction to a single spatial dimension is the same standard
simplification already used implicitly in §5's own $\chi$-derivation
(scalar perturbations only have one physical gradient direction at
linear order; the isotropic linearized system doesn't distinguish
directions) — not a shortcut that loses anything relevant here.

## 2. This is exactly the right way to have resolved the concern

Worth stating plainly: the concern raised in the previous round was a
*qualitative* one ("this is plausibly also gradient-structured, not
checked either way"). The correct response — computing it exactly,
rather than debating which qualitative picture is more persuasive — is
precisely the discipline this program has needed at every one of these
junctures (cf. §5's own bug-catch, R0(a)'s primary-source check, R2's
depressed-cubic reformulation). The result is also *more* informative
than the concern anticipated: not "some unspecified gradient of
$\alpha$," but exactly $\partial_i\mathcal E_\alpha$ — already one of
the program's own established perturbation variables, not a new
combination that would need its own name.

## 3. What this means structurally — confirmed, and one simplification offered

**Confirmed**: the spatial piece of $2(2-\mathcal K_B)\hat J^\mu\nabla_
\mu\phi$ is $\propto a^{-2}\partial_i\mathcal E_\alpha\,\partial_i
\varphi$ — a cross-term between $\mathcal E_\alpha$ and $\varphi$,
structurally distinct from $\mathcal Y=a^{-2}(\partial_i\chi)^2$ (a
single field squared) and from a pure friction/mass term (no gradient
at all). Neither of §6's two attribution hypotheses could have
captured this, as the write-up itself now recognizes.

**One concrete simplification for the next step**: since $\chi\equiv
\varphi+\dot{\bar\phi}\alpha$ (§5's own variable), $\varphi=\chi-\dot{
\bar\phi}\alpha$, so the cross-term can be rewritten entirely in terms
of the program's own three standing variables,
$$\hat J^i\nabla_i\phi\;\propto\;\frac1{a^2}\partial_i\mathcal E_\alpha
\Big(\partial_i\chi-\dot{\bar\phi}\,\partial_i\alpha\Big),$$
i.e. a $\mathcal E_\alpha$–$\chi$ piece plus a $\mathcal E_\alpha$–
$\alpha$ piece, rather than needing $\varphi$ and $\alpha$ tracked
separately. This may make the coupled-variation step (varying this
term, plus $-F_\mathcal Y(0,\bar{\mathcal Q})\mathcal Y=-F_\mathcal Y
(0,\bar{\mathcal Q})a^{-2}(\partial_i\chi)^2$, through the same
Einstein-constraint/vector-equation route that produced $\chi,\Pi,
\mathcal E_\alpha$) more directly comparable term-by-term with the
already-published equations, since it's expressed in the same variable
set from the start. Offered as a simplification, not independently
carried through to the modified $\Pi$/$\mathcal E_\alpha$ equations
here — that remains the worker's own next, substantial step.

## 4. Status and recommendation

Genuine, verified progress — the flagged concern was real, and it's
now pinned down exactly rather than left as a qualitative worry. This
is the third consecutive round (§5, §6, §7) in which this specific
sub-problem (how $(2-\mathcal K_B)$'s two action-level sources actually
propagate into the perturbation equations) has surfaced real, non-
obvious structure — consistent with the worker's own read that this is
substantial, original derivation work, not a quick patch. **Endorsing
the worker's own checkpoint decision**: this is the right point to
pause for review rather than pushing straight into the full coupled
variation, given three rounds of real surprises in a row. Recommending
the next step be exactly what the worker already proposes — varying
both $\mathcal Y$'s and $\hat J^\mu\nabla_\mu\phi$'s contributions
together through the full system — using the $\chi/\mathcal E_\alpha$
form above as a starting simplification. Gate 4 remains paused; this is
still diagnostic/derivation work, not a resumption of the ISW/growth
track. Nothing in `cdot-7/` was touched.

## Companion

- No new script — verification reused `wp7_derivation_Jhat_identity.py`
  directly; the $\chi$-substitution offered in §3 is algebra only, not
  scripted.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-JhatIdentityConfirmed-2026-07-21.md`.
