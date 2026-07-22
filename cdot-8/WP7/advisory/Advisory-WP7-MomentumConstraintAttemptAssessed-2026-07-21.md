# Advisory — §11's First $\Pi$-Momentum-Constraint Attempt: All Five Sub-Results Reproduce Exactly, and the Assembled Candidate Verified Correct by Independent Re-Derivation — the "Bare $F_\mathcal Q$" Gap Is Real, But Its Exact Form Suggests a Concrete, Testable Explanation Neither Advisory Nor Worker Has Checked Yet (for `cdot-8/WP7/`)

*2026-07-21. Review of `Update-WP7-InstabilityRecourses-2026-07-21.md`
§11: the worker's first attempt at deriving $\Pi$'s own momentum-
constraint ($0i$ Einstein equation) contribution, using a genuine shift
perturbation $g_{01}=\epsilon B(t,x^1)$. Gate 1(b) and Gate 4 both
carried. **Verdict up front: every sub-result reproduces exactly on
independent rerun, and — going further than just re-running the script
— the assembled candidate $T^0_{\ 1}$ formula was independently
re-derived from the five raw sub-results and matches the write-up's
quoted expression exactly (zero symbolic difference), confirming the
assembly step itself, not just its inputs. The honestly-flagged "bare
$F_\mathcal Q$" discrepancy is real, but its exact algebraic form
points at a specific, testable hypothesis — that this piece belongs to
the *scalar* sector's own $\theta$-equation, not to $\Pi$ — that hasn't
been checked yet.**

---

## 1. All five sub-results reproduce exactly

Ran `wp7_derivation_momentum_constraint_attempt.py` directly:

```
J_0 = 0 (B-linear piece: 0)
J_1 = eps*(d_1 Psi + d_1 alpha_dot)  (B-linear piece: 0)
J^mu*nabla_mu(phi), O(eps^2), B-linear piece:
  B*d_1(Psi)*phibardot/a^2 + B*phibardot*d_1(alpha_dot)/a^2
Q, O(eps^2), B-linear piece: B*[d_1(alpha)*phibardot - d_1(varphi)]/a^2
Y, O(eps^2), B-linear piece: 2*B*d_1(alpha)*phibardot^2/a^2
Maxwell F^mu-nu F_mu-nu, O(eps^2), B-linear piece: 0
```

Each matches the write-up's claim exactly, including the confirmation
that $\hat J_\mu$ (lower index) itself is completely $B$-independent —
consistent with, and a genuine extension of, §7/§8's earlier result
(the shift perturbation only enters once the index is raised via
$g^{01}$).

## 2. The assembly itself independently re-derived and confirmed, not just the inputs

Rather than only checking the five listed sub-results, reassembled the
candidate $T^0_{\ 1}$ from scratch using the action's own signs
($S\supset a^3[-(2-\mathcal K_B)\mathcal Y-\mathcal F(\mathcal Y,
\mathcal Q)+2(2-\mathcal K_B)\hat J^\mu\nabla_\mu\phi-\tfrac{\mathcal
K_B}2\hat F^{\mu\nu}\hat F_{\mu\nu}]$, expanding $\mathcal F$ to
$F(0,\bar{\mathcal Q})+F_\mathcal Q\delta\mathcal Q+F_\mathcal Y
\mathcal Y+\ldots$) applied to the five reported $B$-linear pieces,
independently of the write-up's own algebra:
$$-(2-\mathcal K_B+F_\mathcal Y)\cdot[2\partial_1\alpha\dot{\bar\phi}^2]
-F_\mathcal Q\cdot[\partial_1\alpha\dot{\bar\phi}-\partial_1\varphi]+2
(2-\mathcal K_B)\cdot\dot{\bar\phi}\partial_1\mathcal E_\alpha$$
Expanded and compared symbolically against the write-up's quoted
candidate ($F_\mathcal Q\partial_1\chi+2(2-\mathcal K_B)\dot{\bar\phi}
\partial_1\mathcal E_\alpha-2\dot{\bar\phi}\partial_1\alpha[(2-\mathcal
K_B+F_\mathcal Y)\dot{\bar\phi}+F_\mathcal Q]$): **the two expressions
are identical term-by-term, symbolic difference exactly zero.** This
confirms the assembly step is algebraically sound, not merely that its
five ingredients were each individually correct.

## 3. A presentation note: the "bare $F_\mathcal Q$" piece isn't quite $F_\mathcal Q\partial_1\chi$

Isolating the $F_\mathcal Q$-proportional terms in the assembled
expression gives $F_\mathcal Q(\partial_1\varphi-\dot{\bar\phi}
\partial_1\alpha)$ — proportional to $\varphi-\dot{\bar\phi}\alpha$,
**not** $\chi=\varphi+\dot{\bar\phi}\alpha$ (opposite sign on the
$\alpha$ term). The write-up's own phrase "a bare $F_\mathcal Q\partial_1
\chi$ piece" is a loose description of the *combined* candidate
expression (which does contain a term proportional to $\chi$ once the
$-2\dot{\bar\phi}\partial_1\alpha F_\mathcal Q$ piece is folded back in
— confirmed algebraically identical in §2 above), not a claim that this
specific isolated piece is itself $\propto\chi$. Noting this only so
the true combination isn't mis-cited later — **the underlying numbers
are unaffected**, this is a labeling precision issue, not a
computational one.

## 4. The gap is real — and its exact form suggests an untested, concrete hypothesis

**Confirmed the discrepancy is genuine**: the published $\delta/\Pi$
bracket ($\mathcal K_B\mathcal E_\alpha+(2-\mathcal K_B)\chi$, lines
437/456) carries no separate $F_\mathcal Q$-proportional term at all,
so a term $\propto F_\mathcal Q(\varphi-\dot{\bar\phi}\alpha)$ in the
candidate $T^0_{\ 1}$ has no home there. **But its specific form is
worth pausing on before assuming it's an assembly error**: the isolated
combination is $F_\mathcal Q$ times a term built purely from $\varphi$
and $\alpha$ (not $\mathcal E_\alpha$ or $\chi$ specifically), and the
primary source's own **scalar**-sector variable $\theta\equiv\varphi/
\dot{\bar\phi}$ (line 440, `theta_field_relation`, already verified in
an earlier round) is defined directly and *only* from $\varphi$ —
suggesting this leftover piece may not belong to $\Pi$'s own bracket at
all, but rather to the **separate momentum-constraint content that
becomes $\theta$'s own equation** once the standard fluid variables
$(\delta,\theta)$ are properly separated out from $(\chi,\mathcal
E_\alpha,\alpha)$'s vector-sector content. **This has not been checked
here or in the write-up** — it is offered as a specific, testable
hypothesis (does $F_\mathcal Q(\varphi-\dot{\bar\phi}\alpha)$, or some
multiple of it, actually reproduce a term already implicit in
$\theta$'s own defining relation or its equation of motion, eq.
`theta_phi_dot`?), not a claimed resolution.

## 5. Status and recommendation

Genuine, carefully-verified partial progress: every sub-result and the
assembly step itself now independently confirmed (not just the
write-up's own numbers trusted), and the one remaining gap is real but
now has a concrete, checkable hypothesis attached to it rather than
being an open-ended "doesn't match yet." **Endorsing the worker's own
checkpoint decision** — six consecutive rounds (§5–§11) on this one
sub-derivation is a lot of accumulated, real structure, and pausing for
review here rather than pushing to force a match is the right call, as
it has been every round so far. Recommending the next attempt check the
$\theta$-attribution hypothesis above before assuming the
Einstein-Hilbert-sector or normalization explanations (the write-up's
own listed candidates) are the more likely source — it's the cheapest
of the three to check, since it only requires comparing against an
already-established primary-source formula, not deriving anything new.
Gate 4 remains paused; this is still diagnostic/derivation work.
Nothing in `cdot-7/` was touched.

## Companion

- No new script — verification reused
  `wp7_derivation_momentum_constraint_attempt.py` directly, plus a
  standalone sympy re-assembly of the candidate $T^0_{\ 1}$ from its
  five reported sub-results (not committed as a separate file — a
  short, one-off symbolic check, reproducible from the sub-results
  quoted in §1–§2 above).
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-MomentumConstraintAttemptAssessed-2026-07-21.md`.
