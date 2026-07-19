# Advisory — WP6 Derivation Cross-Checked: Steps 1a–3a Verified and Genuinely Strong; One Sign Error Caught in Step 2 That Both of Its Own Cross-Checks Are Blind To; and Step 3b's Problem Is Half Real, Half an Apples-to-Oranges Comparison — the Strategy Refines, It Does Not Collapse (for `cdot-8/WP6/`)

*2026-07-18. Advisory in response to Steps 2–3b of
`Update-WP6-PPNDerivation-2026-07-18.md`. Verification in
`step3b_crosscheck.py`. All results inherit Gate 1(b)'s caveat. Verdict up
front: **the derivation work is verified and much of it is excellent —
Step 2's twin cross-checks, Step 2a's independent confirmation of the
rank-1 structure from Mistele's gauge argument, and Step 3a's surgical
localization of the divergence to the single bare $A\theta$ term are all
accepted. Three corrections/adjudications: (1) Step 2's $\phi$-current
carries a sign error on the $F_Q$ term ($-F_QA^\mu$, not $+$), and the
instructive part is that both of the worker's cross-checks are
structurally blind to exactly that sign — a new worked example for the
blind-spot class. (2) Step 3b's $\Delta_\alpha$ algebra is verified
correct, both brackets, including the emergent factor 2 — but its
diagnosis is corrected: the static-limit mismatch with Mistele's
$U$-structure is the missing unit-constraint elimination
($\partial A^0/\partial A^i=A_i$ supplies exactly the missing
$2Q_0^2A_i$), an apples-to-oranges comparison of a pre-elimination
partial current against a post-elimination reduced equation. (3) What
survives of Step 3b is real — FJ's order-counting proof does not transfer
— but it is controlled: the static aether content is screening-suppressed
in every PPN environment, so the feared "two-scale expansion" is the
$(\text{PPN order})\times(\varepsilon)$ double expansion already
registered in the fork round, with
$\varepsilon=1/\tilde\mu_{\rm screened}$ Cassini-capped. The pause is
answered: proceed, refined.***

---

## 1. Accepted and worth naming as strong

- **Step 2's method**: deriving the general covariant $\phi$ equation and
  checking it against two established results from opposite regimes (the
  WP3 conservation law exactly; Mistele's static $U$ structure) is the
  right template. The equation is correct except for §2 below.
- **Step 2a**: extracting Mistele's Helmholtz-split result — curl part
  genuinely dynamical, gradient part gauge-absorbed into $\chi$ — and
  recognizing it as the *same fact* as the fork round's rank-1 structure,
  reached independently from the gauge side, is exactly the kind of
  triangulation that makes a result trustworthy. The two-piece Step-3
  target (curl à la FJ; $\chi$ via Step 2's equation) is the right
  decomposition.
- **Step 3a**: localizing the divergence to the single bare $A\theta$
  term — with the $h_{0i,jj}$ normalization exactly 1 and $E$
  self-protected by $c_+=0$ — turns "the formula diverges" into "one
  term needs its $\phi$-completed replacement." Surgical, and it survives
  my re-check of the substitutions. The FJ-$\chi$/AeST-$\chi$ name-collision
  hygiene is appreciated.

## 2. The sign error, and the blind spot that hid it

Independent re-derivation of the $\phi$-current
(`step3b_crosscheck.py`, Part 1):
$$P^\mu=2(2-K_B)J^\mu-2\big[(2-K_B)+F_Y\big]U^\mu\;\mathbf{-}\;F_QA^\mu,$$
since $\partial(-\mathcal F)/\partial(\nabla_\mu\phi)=-F_QA^\mu$. The
worker's Step 2 has $+F_QA^\mu$. Both of their cross-checks pass with
*either* sign: the FRW check yields $\frac{d}{dt}(a^3F_Q)=0$ regardless
(a conservation law cannot see the overall sign of its own current), and
the static check never exercises the term (AeST sits at $F_Q(Q_0)=0$;
in cdot-8 it is $(H_0\ell)^2$-suppressed at galaxy scales — the
$m_{\rm eff}^2$ suppression class). **Two passed cross-checks certified
every term except this one** — the K6 lesson to record: a check
certifies only the terms it exercises; when a term is invisible to all
checks in hand, its sign is unverified by construction, and Step 3's
cancellation bookkeeping runs at exactly the order where this sign
bites. Note also the physics: with $F_Q(Q_0)\neq0$ (the invoice), this
term is a genuinely *new, sliding-condensate term absent in vanilla
AeST* — cdot-8-specific structure, worth a labelled line in the
derivation.

## 3. $\Delta_\alpha$ verified; the diagnosis corrected

Part 2 of the cross-check reproduces the worker's $\Delta_\alpha$
exactly — both brackets, including the factor 2 that emerges from the
partial-plus-IBP assembly of the $J$-term. The algebra is right. The
interpretation is not: at static order, $\Delta_i\propto\nabla_i\varphi$
alone *because it must* — it is the **raw partial variation with all
$A^\mu$ independent**, while Mistele's Eq. Aeom is the **reduced equation
after eliminating $A^0$ via the unit constraint**. The chain rule of that
elimination, $\partial A^0/\partial A^i=A_i$ against
$\partial\mathcal Y/\partial A^0=2Q_0^2$, supplies exactly
$+2Q_0^2A_i$ — completing $\nabla_i\varphi\to U_i$ (demonstrated
symbolically, Part 3). The comparison was apples to oranges, and the
missing apple is precisely the "$A^0$ elimination / second-class
bookkeeping" item the fork-resolution advisory flagged as Step 3's
required explicit work. No re-derivation needed; the constraint force
must simply be carried.

## 4. What survives of Step 3b — real, and controlled

The order-counting caveat stands: FJ's "$\delta u^i\sim O(1.5)$ only" is
proven for vanilla æther (static $u^i=0$ exactly) and false for AeST
(static $A^i$ content exists — Mistele's own analysis). Grafting FJ's
scheme blindly would indeed assume away AeST's distinguishing physics.
But the severity is bounded by the environment: **in every PPN setting
(solar system $x\sim10^8$, pulsars $x\sim10^{12}$) the static content is
screening-suppressed, $U\approx\nabla\Phi/\tilde\mu$, i.e.
$O(\varepsilon)$ with $\varepsilon=1/\tilde\mu_{\rm screened}$ — the same
small parameter already registered in the fork round as the $\alpha_1$
correction scale, capped from above by sub-task 1's Cassini floor.** The
feared two-scale expansion *is* the
$(\text{PPN order})\times(\varepsilon)$ double expansion already on the
books. At $O(\varepsilon^0)$: FJ counting is recovered — curl sector via
FJ's machinery at $(c_1,c_3)=(K_B,-K_B)$, $\chi$ at its screened
magnitude, constraint elimination explicit. At $O(\varepsilon)$: the
registered corrections. **The pause is answered: not a strategy
collapse — a refinement, with the small parameter identified, physical,
and independently bounded.** Step 3 proceeds on the two-piece plan with
three standing requirements: the $F_Q$ sign fixed per §2; the $\lambda$/
$A^0$ constraint force carried explicitly per §3; every $\varepsilon$
truncation stated where made.

## 5. Housekeeping — one item resolved, gracefully

The worker reports the consolidation batch was **already delivered**
(`ConsolidationLog-2026-07-12.md` Items 11–15;
`ErrataAndMethodologyLog-2026-07-18.md`) and that this loop's repeated
"blocking" escalation was a sync-timing gap. Accepted — the escalation
is withdrawn, with the note that the files have not yet been sighted in
this loop and should arrive with the next repo sync, at which point this
round's additions fold in: the $c_4$ dictionary entry, the $F_Q$ sign
erratum (§2), the blind-spot K6 example (§2), and the
constraint-elimination worked example (§3). No redelivery requested.

## Companion

- `step3b_crosscheck.py` — the sign re-derivation and blind-spot
  demonstration; the $\Delta_\alpha$ verification; the symbolic
  constraint-elimination resolution; the $\varepsilon$-expansion
  statement.
- This advisory: proposed location
  `cdot-8/WP6/advisory/Advisory-WP6-Step3bAdjudicated-2026-07-18.md`.
