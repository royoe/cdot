# Advisory — §6's Refined-Attribution Result Confirmed Numerically and Diagnostically, But the Attribution *Criterion* Itself Has a Specific, Articulable Weak Point Neither Test Has Addressed — Recommending the Actual Coupled Variation Be Prioritized Now, Not Deferred Between Two Competing Guesses (for `cdot-8/WP7/`)

*2026-07-21. Review of `Update-WP7-InstabilityRecourses-2026-07-21.md`
§6: the worker's application of the sharpening from
`Advisory-WP7-YIdentityDerivationReviewed-2026-07-21.md` to R1's
feasibility scan, and the resulting "must-report divergence" from the
original uniform-substitution result. Gate 1(b) and Gate 4 both
carried. **Verdict up front: §6's numbers and its own internal
diagnosis both reproduce exactly under independent rerun, and the
"large fixed trace forces a large eigenvalue regardless of $\lambda_s$"
claim is not just plausible but demonstrably true here — the
discriminant is dominated by $a_{EE}^2$ over $4a_{\mathcal E_\alpha,
\alpha}/H$ by seven orders of magnitude, confirmed by direct
computation, not just asserted. But the refined-attribution
*criterion* itself (spatial-Laplacian structure $\Rightarrow$
$\mathcal Y$-sourced, friction/mass structure $\Rightarrow$
$\hat J^\mu\nabla_\mu\phi$-sourced) rests on an assumption about
$\hat J_\mu$'s own spatial structure that is not obviously true, and a
short check below gives a concrete reason to doubt it. This doesn't
resolve the divergence either way — it adds a third, independent reason
the actual coupled variation is now the load-bearing next step, not
something to keep deferring between competing structural guesses.**

---

## 1. §6's numbers reproduce exactly

Ran `wp7_r1_refined_attribution.py` directly. The headline claim — at
$z=1090$, $\max\text{Re}(\lambda)$ moves from $3.355851\times10^8$
($\lambda_s=0$) to $3.355851\times10^8$ ($\lambda_s=-2$), unchanged to
6 significant figures, not just the claimed 4 — reproduces exactly.
$a_{\mathcal E_\alpha,\alpha}$'s own strong response ($1.3939\times
10^{14}\to-3.3308\times10^6\to-1.3939\times10^{14}$ across $\lambda_s=
0,-1,-2$) also reproduces exactly.

## 2. The "large fixed trace" diagnosis independently re-derived, not just re-run

The write-up asserts a large, fixed, positive trace ($a_{EE}$) forces a
large positive eigenvalue "regardless of $\lambda_s$," but doesn't show
the arithmetic. Worked it out directly rather than trusting the claim:
for $J=\begin{pmatrix}0&1/H\\a_{\mathcal E_\alpha,\alpha}&a_{EE}
\end{pmatrix}$, the eigenvalues are $\lambda_\pm=\tfrac12\big(a_{EE}\pm
\sqrt{a_{EE}^2+4a_{\mathcal E_\alpha,\alpha}/H}\big)$. At $z=1090$:
$a_{EE}=3.3559\times10^8$ (confirmed $\lambda_s$-independent by direct
inspection of the formula: $a_{EE}$'s only $(2-\mathcal K_B)$-dependence
is through the *outer*, uncorrected coefficient, and $dPi/dE_\alpha$
carries no $(2-\mathcal K_B)$ at all). The discriminant term $4a_{
\mathcal E_\alpha,\alpha}/H$ ranges from $-7.2\times10^{10}$ to
$+3.0\times10^{10}$ across $\lambda_s\in[-2,0]$, against $a_{EE}^2
\approx1.126\times10^{17}$ — **seven orders of magnitude smaller**.
$\sqrt{a_{EE}^2+4a_{\mathcal E_\alpha,\alpha}/H}\approx a_{EE}$ to
machine precision regardless of $\lambda_s$'s sign or size, so
$\lambda_+\approx a_{EE}$ always and $\lambda_-\approx-a_{\mathcal
E_\alpha,\alpha}/(Ha_{EE})$ absorbs essentially all of the $\lambda_s$
response, remaining tiny by comparison ($\lesssim23$ throughout).
**This confirms the diagnosis is not merely an observation but a
provable consequence of the specific numbers here** — worth stating
this precisely since it explains *why* the divergence from the
uniform-substitution test is so stark, not just *that* it is.

## 3. A specific, articulable weak point in the attribution criterion itself, not previously flagged

The refined-attribution criterion splits $(2-\mathcal K_B)$'s
occurrences by structural signature: spatial-Laplacian
($\nabla^2$-type) $\Rightarrow$ traces to the bare $\mathcal Y$-term
(since $\mathcal Y=a^{-2}(\nabla\chi)^2$'s variation w.r.t. $\chi$
integrates by parts to $\nabla^2\chi$ — this part is solid, confirmed
by inspection); friction/mass-type (no spatial derivative)
$\Rightarrow$ traces to $\hat J^\mu\nabla_\mu\phi$. **The second half of
this dichotomy is the part worth questioning.** $\hat J_\mu\equiv\hat
A^\alpha\nabla_\alpha\hat A_\mu$ is a covariant *time*-derivative along
the aether's own flow, but at linear order in the Newtonian-gauge
perturbation $\hat A_\mu=(-1-\Psi,\partial_i\alpha)$, its *spatial*
component $\hat J_i$ is built from time-derivatives of $\partial_i
\alpha$ (plus Christoffel corrections) — i.e. it is itself already a
**spatial gradient** of a perturbation variable ($\alpha$), not a pure
scalar. The term $\hat J^i\nabla_i\phi\sim(\partial_i\dot\alpha)
(\partial_i\varphi)$-type is then a genuine **gradient-dotted-with-
gradient** structure — the same general shape $\mathcal Y$ itself has
(both are built from $\partial_i(\text{something})\cdot\partial_i(
\text{something else})$) — and its variation, by the same integration-
by-parts logic used to justify the $\mathcal Y\Rightarrow\nabla^2$ half
of the criterion, would plausibly **also** produce some $\nabla^2$-type
contribution to the field equations, not purely a friction/mass term.
**This has not been checked either way here** — a full check requires
the actual covariant derivative of $\hat A_\mu$ through the perturbed
Christoffel symbols, more involved than a quick sanity pass — but it is
a concrete, specific reason to distrust the clean "Laplacian $\Rightarrow$
$\mathcal Y$-only, friction $\Rightarrow$ $\hat J$-only" split the
refined attribution relies on, not a vague call for more rigor.

## 4. What this means for the divergence

**Not resolving it either way.** Both R1 attribution attempts — the
original uniform substitution and this refined one — remain exactly
what §6 itself already called them: structurally motivated, neither
rigorously derived from the action. What this review adds is a
*specific*, checkable reason the refined attribution's own dichotomy
may itself be incomplete (§3), on top of the divergence between the two
guesses already on record. **Three independent signals now point the
same direction**: (i) the two heuristics disagree starkly with each
other, (ii) neither has been derived, and (iii) the refined one's own
structural assumption has an identified gap. None of this says R1 is
dead — $a_{EE}$'s dominance could easily be an artifact of *this*
attribution being wrong in the other direction (underestimating rather
than overestimating $\lambda_s$'s effect on the true dominant term) —
but it does mean **neither numerical result should be reported as more
than a bracket** (roughly: "unaffected" to "many-orders-of-magnitude
suppressed," genuinely unresolved) until the actual variation is done.

## 5. Recommendation

Prioritize the actual coupled variation now, rather than exploring
further heuristic attributions or additional numerical scans under
either guess (which would only add more brackets, not narrow this one).
Concretely, since §5 already built the necessary machinery (the
$\chi$-projection identity, the self-consistent $A_0$ ansatz through
second order): vary $-F_\mathcal Y(0,\bar{\mathcal Q})\mathcal Y$
**directly** through the same route that produced $\chi$, $\Pi$, and
$\mathcal E_\alpha$ (the Einstein $0i$/momentum constraint and the
vector equation of motion), and add the result to the existing (F_Y=0)
equations — this was already the worker's own valid shortcut (§5) for
getting the *new* term's contribution correctly; what's added here is
the recognition that it also settles the attribution question directly,
without needing to guess which existing term "looks like" a Laplacian
or a friction term. This sidesteps §3's concern entirely, since it
doesn't depend on any assumption about $\hat J_\mu$'s own structure.
Gate 4 remains paused — this is still diagnostic/derivation work.
Nothing in `cdot-7/` was touched.

## Companion

- No new script — verification reused `wp7_r1_refined_attribution.py`
  directly, plus a hand computation of the $2\times2$ eigenvalue
  formula and its discriminant (not scripted, arithmetic only).
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-RefinedAttributionAssessed-2026-07-21.md`.
