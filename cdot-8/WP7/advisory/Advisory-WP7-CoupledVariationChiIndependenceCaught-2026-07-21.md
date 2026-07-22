# Advisory — §8 Confirmed Exactly; §9's First Coupled-Variation Attempt Reproduces as Reported, But a Check of Its Own Stated Convention Finds a Real Fix: $\chi$ Is Not Actually Independent of $\alpha$, and Varying at Fixed $\varphi$ Instead Resolves Residual Mismatch (1) Exactly — With a New, Third Open Item Surfacing in Its Place (for `cdot-8/WP7/`)

*2026-07-21. Review of `Update-WP7-InstabilityRecourses-2026-07-21.md`
§8 ($\hat J_0=0$) and §9 (the first coupled-variation attempt). Gate
1(b) and Gate 4 both carried. **Verdict up front: §8 reproduces exactly
— genuine, clean progress, no notes. §9's own reported numbers
reproduce exactly too, and the Maxwell-friction sanity check is real.
But checking the script's own stated convention — treating $\chi$ as
independent of $\alpha$ during the variation, "the paper's own
convention" per its docstring — turns up a real issue: $\chi\equiv
\varphi+\dot{\bar\phi}\alpha$ is not actually independent of $\alpha$;
the genuinely independent fields are $(\varphi,\alpha)$. Redoing the
variation at fixed $\varphi$ (methodologically correct) and rewriting
the result in terms of $\chi$ afterward reproduces the worker's own
"residual mismatch (1)" exactly and for free — no Pi/momentum-
constraint input needed, contrary to the worker's own speculated
explanation. But it does not resolve everything: a $(2-\mathcal
K_B)\dot\chi$ term already present in the original attempt persists
unchanged (a third open item, not on the worker's list), and mismatch
(2) shifts rather than resolves. Net: real progress, offered as a
correction to try, not a completed derivation.**

---

## 1. §8 confirmed exactly, no notes

Ran `wp7_derivation_Jhat_identity.py`'s extended output directly:
$\hat J_0=0$ and the orthogonality check $\hat A^\mu\hat J_\mu=0$ both
confirmed identically. Clean, no issues.

## 2. §9's reported numbers reproduce exactly

Ran `wp7_derivation_coupled_variation_attempt.py` directly. The
Maxwell-alone sanity check reproduces $K_B(\dot{\mathcal E}_\alpha+H
\mathcal E_\alpha)$ exactly (confirmed by hand: the four printed terms
$K_BH\Psi+K_BH\dot\alpha+K_B\dot\Psi+K_B\ddot\alpha$ regroup exactly
into $K_B[(\ddot\alpha+\dot\Psi)+H(\dot\alpha+\Psi)]$). The full-
Lagrangian result and both reported residual mismatches reproduce
exactly as stated.

## 3. A check of the script's own stated convention finds a fix for mismatch (1)

The script's docstring states $\chi$ is "treated as independent of
alpha (paper's own convention)" during the $\alpha$-variation. **This
is worth checking rather than accepting, since $\chi$'s own definition
($\chi\equiv\varphi+\dot{\bar\phi}\alpha$, established in §5 and
matching the primary source's line 433) makes it explicitly dependent
on $\alpha$.** The two fields that are genuinely independent in this
system are $\varphi$ and $\alpha$ — $\chi$ is a convenient combination
of them, not a third independent degree of freedom. Varying the action
while holding $\chi$ fixed is therefore **not** equivalent to varying
at fixed $\varphi$ (holding $\chi$ fixed as $\alpha$ changes forces
$\varphi$ to silently co-vary to compensate) — these are two different
variations, and only the fixed-$\varphi$ one is physically correct.

**Redid the derivation the correct way** (`wp7_chi_dependence_check.py`,
new, `cdot-8/WP7/advisory/`): assembled the identical Lagrangian with
$\chi$ replaced by its actual definition $\varphi+\dot{\bar\phi}\alpha$
throughout, varied directly w.r.t. $\alpha$ holding $\varphi$
independent, then rewrote the result back in terms of $\chi$ via the
same substitution (a pure relabeling of an already-correct result, not
a re-variation). **Two independent routes were tried before trusting
this — the first (comparing two previously-computed results by hand)
initially disagreed with the second (a single, direct re-derivation);
tracing the discrepancy found the first route had silently conflated
"fixed $\chi$" with "fixed $\varphi$" in its own algebra — exactly the
distinction under test. The direct re-derivation is the one reported
here, and it has been checked by running it as a clean, standalone
script, not just inline.**

**Result**: the corrected $\chi$-coefficient becomes exactly
$$(2-\mathcal K_B)H+(2-\mathcal K_B)\dot{\bar\phi}+\frac{F_Q}2+F_
\mathcal Y\dot{\bar\phi}$$
— matching the published total, $(2-\mathcal K_B)(H+\dot{\bar\phi})+
F_Q/2$ (using $-dK/dQ=F_Q/2$, already established), **exactly**, plus
one additional term, $F_\mathcal Y\dot{\bar\phi}\chi$. **This extra term
is plausibly genuine new physics, not an error**: the published
equation was derived at $F_\mathcal Y=0$, so its absence there is
exactly what should happen — this is the very completion term the whole
exercise exists to find. **This resolves the worker's own reported
mismatch (1) exactly, and for free**, via a mechanical correction (vary
at fixed $\varphi$, not fixed $\chi$) rather than requiring the
not-yet-derived $\Pi$/momentum-constraint contribution the worker's own
docstring speculated as the likely explanation.

## 4. What this does not resolve — reported honestly, not smoothed over

**A third open item, not on the worker's original list**: a $(2-
\mathcal K_B)\dot\chi$ term is present in *both* the original and the
corrected derivation, unchanged by this fix, and it has **no
counterpart anywhere in the published $\mathcal E_\alpha$ equation** —
not a coefficient mismatch on an existing term, but an entire term
structure the published compact form doesn't contain at all. This is
distinct from mismatches (1) and (2) and needs its own accounting —
plausibly (matching the worker's own instinct about mismatch (1), now
redirected) exactly where the $\Pi$/momentum-constraint's separate
origin re-enters, since $\Pi$'s own formula is not a raw field-variation
object and could plausibly supply a compensating $\dot\chi$-type piece
once properly included.

**Mismatch (2) shifts, doesn't resolve**: the corrected alpha-
coefficient drops the bare $F_Q\dot{\bar\phi}/2$ piece present in the
original attempt, but introduces a new, also-unaccounted $\dot\alpha$
coefficient ($-(2-\mathcal K_B)\dot{\bar\phi}$). The worker's own
proposed resolution path (substitute the background scalar's equation
of motion to convert $F_Q,F_{QQ}$-parametrized pieces into $c_\text{
ad}^2$ notation) is still needed, now starting from a different
intermediate expression.

## 5. Status and recommendation

Genuine progress on one specific front (mismatch (1), now understood
and mechanically resolved) with a new, honestly-reported open item
(the $\dot\chi$ term) surfacing in its place — net informative, not a
completed derivation. **Recommending the worker adopt the fixed-$
\varphi$ variation for the next iteration** (straightforward: assemble
the same Lagrangian with $\chi\to\varphi+\dot{\bar\phi}\alpha$
substituted throughout before varying, as done in
`wp7_chi_dependence_check.py`), and treat the $\dot\chi$ term as the
next concrete target — most plausibly resolved by finally bringing in
$\Pi$'s own momentum-constraint derivation (already flagged as the
missing piece in every round since §9 began), rather than by further
adjustment of the vector-equation variation alone. This checked, not
asserted, correction should itself be independently re-verified before
being treated as final, consistent with this program's own standing
discipline (cf. §5's and §9's own bug-catches) — flagging this
explicitly since two different manual approaches to the same check
briefly disagreed before the source of the discrepancy was found. Gate
4 remains paused — this is still diagnostic/derivation work. Nothing in
`cdot-7/` was touched.

## Companion

- New script: `wp7_chi_dependence_check.py`
  (`cdot-8/WP7/advisory/`) — standalone, reruns cleanly, reproduces the
  quoted coefficients exactly.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-CoupledVariationChiIndependenceCaught-2026-07-21.md`.
