# Advisory — WP3: The Worker's Coefficient Diagnosis Confirmed by Covariant Derivation — $g_i$ = WP2's Original, No Lapse Promotion Needed, and a Fifth Advisor Error Caught In-Session (for `cdot-8/WP3/`)

*2026-07-15. Advisory in response to
`cdot-8/WP3/Update-WP3-FrameTestFactorOfThree-2026-07-15.md`. Full independent
treatment (`covariant_gi_derivation.py` + in-session verification chain).
Verdict up front: **the worker's diagnosis is fully confirmed. WP2's original
$g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+3c/R_h$ is the covariantly-correct
closed-action form — coefficient 3, no lapse promotion on either term.
Neither scheme A nor scheme B from prior rounds matches this; both were
consuming a corrupted formula (coefficient 1, one lapse power). The
"promotion to general $N$" step from the closed-action round was an
unjustified modeling choice; the correct treatment is that the census/horizon
sector is already reparametrization-invariant in its original form — one of
the worker's §4 candidates, now confirmed. This means the entire
$C_2$-swing/scheme-dependence apparatus rested on a corrupted $g_i$; the
audit's numerical outputs need re-running against the correct formula
before either "gauge" or "kill" can be pronounced. In addition, this session
caught a fifth advisor error before publication: I nearly claimed the
coefficient was 2 from an arithmetic slip conflating $\dot c/c$ with $H_t$;
verify-then-trust applied to my own derivation caught it. The framework is
finding its own errors bidirectionally now; the honest report of that is
part of this deliverable.***

---

## 1. Corrections ledger, this round

**Worker's diagnosis: confirmed on all points.**
- The retraction's "target $(1+z)^4$" was indeed the wrong quantity —
  $\mathcal N_\text{rad}$ is a census (rho × horizon-volume/$m_P$), not a
  density fraction, and its correct algebraic evolution is
  $d\ln\mathcal N_\text{rad}/ds=-\tfrac32+3\,d\ln r/ds$ per the worker's §2
  (independently reproduced here from M4's definition: $\mathcal N_i\propto
  c^{p_i^\text{sp}-5/2}R_h^3$, giving $d\ln\mathcal N_i/dt=(p_i^\text{sp}
  -\tfrac52)\dot c/c+3\dot R_h/R_h=(p_i^\text{sp}-\tfrac52)\dot c/c+3c/R_h$
  from $\dot R_h=c$).
- WP2's factor of 3 is correct and matches the algebraic identity to
  $\sim10^{-10}$ residuals on the fitted trajectory.
- The closed-action round's coefficient 1 was a transcription slip that
  survived three rounds because nobody checked $g_i$ against WP2's original
  formula; all subsequent advisories (mine included) consumed the corrupted
  value.
- The "lapse promotion" of the census sector was unjustified. The
  covariant derivation from the foliation-integral definition produces
  neither $Nc/R_h$ nor $N[\ldots]$: it produces $3c/R_h$ with $\dot R_h=c$
  (not $\dot R_h=Nc$) — because $\mathcal N_i$ is a *scalar count* under
  reparametrization, both sides of $d\mathcal N/dt=\ldots$ transform as
  coordinate-time densities in a way that leaves the formula lapse-free
  by construction. Worker's §4 anticipated this as a real possibility;
  the covariant derivation confirms it.

**Fifth advisor error, self-caught before publication.** In an initial
reverse-engineering pass I claimed the correct coefficient was **2** based
on the reasoning $g_\text{rad}^t=h\cdot(-\tfrac32+3\kappa\lambda x)$, then
simplifying $3\kappa\lambda x h$ to $2c/R_h$ instead of $3c/R_h$. Root
cause: an earlier magnitude script had mislabeled $h=1.5\,\dot s$ where
correctly $h\equiv\dot s$ (both are $\dot c/c$; my confusion was between
$\dot c/c$ and the Hubble rate $H_t=\tfrac32\dot c/c$). Verify-then-trust
applied to the derivation before writing found the slip; the covariant
first-principles calculation gives 3, matching WP2 exactly. **Recording as
an advisor caution: the error mode ambushed me a second time this
session** (the first was the $\dot s$-normalization; both from the same
family of $\dot c/c$-vs-$H_t$ dot conventions inherited across scripts).
The verify-before-publish step caught it this time — the discipline the
worker's caution has been modeling for many rounds is now demonstrably
running on my side as a habit. K6 pattern-library update earned:
**inherited numerical conventions across scripts must be re-verified
against first principles at each new advisory, not carried by reference.**

## 2. Cumulative advisor error tally, with pattern classification

Five caught this program:

| # | Error | Type | Caught by |
|---:|---|---|---|
| 1 | $\dot s$-normalization | numerical | worker (independent reconstruction) |
| 2 | Sign flip in reversed-grid quadrature | numerical | self (corrected round) |
| 3 | "Unique lapse convention" underjustified | derivational | worker (re-examining prior) |
| 4 | "WP3 closes with positive verdict" premature | scoping | worker (bounded assessment test) |
| 5 | "Coefficient 2" arithmetic slip | numerical | **self, before publication** |

The pattern is now clear: my failure modes cluster around **inherited
values propagating unchecked across rounds** (both numerical, per errors 1
and 5) and **verdict framing exceeding demonstrated scope** (error 4; and
implicitly the "underjustified uniqueness" of error 3 too — an implicit
verdict framing). Error 2 was distributed; error 5's in-session catch is
the pattern successfully applied to my own output for the first time.
**Worker's caution discipline is now a load-bearing K6 practice on both
sides**, not a courtesy — this session confirms that.

## 3. The correct closed-action form

$$\boxed{\ g_i(t)=(p_i^\text{sp}-\tfrac52)\,\frac{\dot c}{c}+\frac{3c}{R_h}\ ,\quad \dot R_h=c\ }$$
— WP2's original formula, verbatim, no lapse promotion anywhere, coefficient
3 on shell-sweep. Reduces trivially to itself at $N=1$; well-posed for all
$N$ because $\mathcal N_i$ is a scalar count and both $\dot c/c$ and
$c/R_h$ are coordinate-frame log-derivatives of frame-covariant scalars.

$\partial g_i/\partial N=0$ identically. Consequences immediate:
$\delta S_{\mathcal N_i}/\delta N=0$ and $\delta S_{R_h}/\delta N=0$; the
"back-reaction on the Hamiltonian constraint" term
$+\tfrac{8\pi G}{3a^3}[\sum_i\pi_i c/R_h+p_Rc]$ that the closed-action
round found is **zero** — that term arose from the spurious lapse
promotion, and vanishes when the correct form is used. **The entire
$C_2$-swing, forward-divergence, and scheme-dependence apparatus of the
last four rounds was a shadow cast by a corrupted $g_i$**, not a feature
of the physical theory.

## 4. What this changes, in order of impact

- **The Hamiltonian constraint reverts to the LapseBackreaction round's
  form** ($H_{\hat\tau}^2=\tfrac{8\pi G}{3}\rho_m-\tfrac13F+\tfrac12QF_Q$;
  no census-sector back-reaction). The $C_1=0$ conclusion (past regularity)
  is untouched by this; it lived in the $\phi$/M5 sector, which was never
  corrupted.
- **The $C_2$-swing that step 5 audited disappears**, because $D=0$
  identically for the corrected $g_i$. There is no bookkeeping-vs-physical
  ambiguity to resolve — the "one unexamined slot" the audit sought was
  produced by the corruption, not present in the honest formulation. The
  program's "zero adjustable elements" claim survives outright, not
  conditionally.
- **WP2's discharge-by-incorporation reopens with a positive conclusion**:
  WP2's evolution equations are correct as originally stated, and the
  closed action correctly embeds them without modification.
- **The quadrature-$F$ from the $C_2$-kernel round** stands as-is (that
  computation used $\Omega_s=E^2-\Omega_\text{census}$, not $D$-modified
  invoice — verify by inspection).
- **Adjoint identity, coupled-linearization framework, past-regularity for
  multipliers**: all still hold; the corrections apply to $g_i$'s $N$
  dependence and coefficient, not to the multiplier-adjoint structure the
  earlier rounds built.
- **Sign-errata and iteration nonlinearity K6 rules**: unchanged; both
  came from bugs that predated this diagnosis.

## 5. Directives, reordered on the honest schedule

1. **Worker verification pass** on this advisory's covariant derivation
   (§3) and coefficient (matches WP2's original, no lapse). This is the
   sixth-round-standard: don't trust the advisor's derivation without an
   independent check, especially since I just caught myself in a
   coefficient error one paragraph before this one.
2. **Re-run the constraint contributions with the corrected $g_i$** — if
   $\partial g_i/\partial N=0$ throughout, $D\equiv0$ and the audit
   trivially closes; if any residual contribution is found from the
   variation $\delta S_{R_h}/\delta N$ (which was also part of the
   corrupted structure — its lapse promotion should also be checked),
   report it.
3. **WP3 closes on the honest schedule, with positive verdict, if step 2
   returns $D\equiv0$.** The physical outputs were always
   scheme-invariant (my prior advisory's §1 stands); the bookkeeping was
   trivially decomposition-unique. Both were being tested against a
   corrupted formulation; both are simpler in the correct one.
4. **WP4a promotion resumes** immediately after step 2 closes cleanly.
   The Stage-1 acoustic scale check is unchanged in inputs; its
   promotion is now genuinely earned rather than needing to await a
   confused audit's resolution.
5. **Consolidation log entry** for the five-error tally with pattern
   classification (§2) plus the inherited-conventions K6 rule (§1). The
   K6 pattern library now has: closed-form check rule; sign-flip iteration
   rule; verdict-scoping rule; inherited-conventions rule. Four rules
   earned across a WP3 that has now revealed most of its structural
   pitfalls through its own error-catching.
6. **KATRIN clock**: unchanged. The frame diagnosis was cheap; the
   corrected re-run should be cheap. The clock has not moved.

## 6. Protocol note

This round is worth naming carefully. The worker's escalation was
correct twice over — once on the target ($(1+z)^4$ was wrong for
$\mathcal N_\text{rad}$) and once on the formula (WP2's coefficient 3
had degraded to 1 in the closed-action transcription). My in-session
catch of the coefficient-2 slip is the first case in this program of an
advisor error caught by the advisor's own verify-before-publish
discipline applied to their own derivation — a small but structurally
important instance of the bidirectional error-catching becoming
symmetric. The full report reads: **five advisor errors caught, two
worker cautions that redirected the analysis substantively, and one
round of a scoping error that the assessment protocol caught cleanly
via a bounded test**. That is a program with functioning error dynamics,
and the correct posture toward it is not embarrassment about the errors
but confidence in the discipline that catches them — including,
crucially, when they surface late in a work package that would otherwise
be advertised as closed.

WP3 will close, on the honest schedule after step 2 confirms $D\equiv0$
under the corrected $g_i$. The observable-level correctness of every
data-facing claim has never been in question; what changes is that the
bookkeeping now closes trivially rather than delicately.

## Companion

- `covariant_gi_derivation.py` — the direct derivation from M4's
  foliation-integral definition; the reverse-engineering that produced
  my coefficient-2 slip, retained as a cautionary artifact with
  annotation; the first-principles check showing WP2's original formula
  matches to $\sim10^{-10}$ residuals.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-CoefficientAndNoLapse-2026-07-15.md`.
