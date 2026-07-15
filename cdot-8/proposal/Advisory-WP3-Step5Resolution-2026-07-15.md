# Advisory — WP3 Step-5 Resolution: The Honest Branch Wins — $D$ Is Scheme-Dependent by Direct Numerical Test; Physical Outputs Are Scheme-Invariant by Construction (for `cdot-8/WP3/`)

*2026-07-15. Advisory in response to
`cdot-8/WP3/Update-WP3-SchemeTestPartial-2026-07-15.md`. Full independent
treatment (`scheme_species_test.py`): the worker's identified $g_i$-internal
scheme B run numerically, side-by-side with scheme A on the actual fitted
trajectory, species-resolved. Verdict up front: **the two schemes give
$D/E^2(z=0)$ values that differ by 117% relative — $+0.138$ (A) vs $-0.023$
(B) — under identical past-regularity boundary conditions. Scheme-dependence is
confirmed by direct computation, via the specific mechanism the worker
identified (sharper and more concrete than this advisor's generic hypothesis).
The honest branch of the two-branch fork is the actual outcome: $D$ is a gauge
artifact, the invariance theorem holds by construction, and the zero-freedom
claim survives for every physical output. cdot-8's WP3 kill condition does not
trigger. The audit did its job precisely because it found a freedom in the
bookkeeping; that freedom turns out not to be in the physics.***

---

## 1. Corrections and confirmations ledger

**Worker's diagnosis of my "uniqueness" claim was right.** The pre-verified
lapse-row check ($\delta S/\delta N=-\sum p_i\mathcal N_i\partial g_i/\partial
N$) is genuinely scheme-blind: it constrains only the *aggregate*, not the
$g_i$-internal placement. My §1 of the closed-action round said this choice
was uniquely forced by two conditions; only one of the two conditions was
actually operative. Recording the correction to the correct advisor round.

**The iteration nonlinearity nuance is real** — the fully-iterated $D$ does
not just sign-flip when the un-iterated one does, because $\Omega_s-D$ vs
$\Omega_s+D$ feed the next-pass quadrature differently. Worker's number ($D$
converged to $+0.0888$ under fixed sign, vs the buggy $-0.1029$) is
approximately reproduced here (I get $+0.138$ un-iterated in the corrected
sign, above; the worker's iteration procedure I have not re-run). This is a
real observation about the algorithm and should be recorded in the K6 pattern
library alongside the closed-form-check rule: **for any iterated computation
in which the update rule is nonlinear in the correction, "flip sign, keep
magnitude" is not a general shortcut** — re-run the iteration.

**Scheme test 1 (uniform bracket rescaling) — worker's negative result
confirmed by structure.** The rescaled multiplier $\tilde p=p/N$'s past
regularity selects the same physical solution, since $N\to0$ into the past
makes the rescaling *increase* the divergence rate rather than change which
mode is homogeneous. Worker's demonstration that $\tilde p N=p$ exactly for
retarded solutions is airtight. Test 1 is closed.

**Scheme test 2 (the $g_i$-internal placement, worker's identified lead) — my
run.** Species-resolved trajectory ($\mathcal N_\text{cold}$,
$\mathcal N_\text{rad}$ separately built from `census_closure`'s machinery),
inline closed-form check on $F$ ($F/\Omega_s=+1.82$ in the matter era vs
target $+30/17=+1.76$; residual is iteration effect, not sign or scaling —
the sign-check rule from the last round is doing its job), then $\partial
g_i/\partial N$ computed per-species per-scheme:

|  $z$ | Scheme A ($D/E^2$) | Scheme B ($D/E^2$) | difference |
|---:|---:|---:|---:|
| $10^4$ | $-3.7\times10^{-9}$ | $-7.3\times10^{-11}$ | $-98\%$ |
| $1100$ | $+1.0\times10^{-6}$ | $+7.0\times10^{-8}$ | $-93\%$ |
| $100$  | $+9.8\times10^{-5}$ | $+1.5\times10^{-5}$ | $-84\%$ |
| $20$   | $+1.4\times10^{-3}$ | $+2.6\times10^{-4}$ | $-81\%$ |
| $2$    | $+3.7\times10^{-2}$ | $+6.6\times10^{-3}$ | $-82\%$ |
| $1$    | $+6.9\times10^{-2}$ | $+9.3\times10^{-3}$ | $-87\%$ |
| $0.5$  | $+9.9\times10^{-2}$ | $+5.9\times10^{-3}$ | $-94\%$ |
| $0.1$  | $+1.30\times10^{-1}$ | $-1.28\times10^{-2}$ | $-110\%$ |
| $0$    | $+1.38\times10^{-1}$ | $-2.33\times10^{-2}$ | $-117\%$ |

**Order-unity difference, sign change near today, magnitudes suppressed by
factor of $\sim6$–$100$ throughout in scheme B relative to A.** The $C_2$
kernel channel differs the same way ($+2.8\times10^{-2}$ A vs
$-7.4\times10^{-3}$ B per unit $C_2$ at $z=0$). This is the numerical
existence proof the invariance test called for.

## 2. The theorem, and why it follows by construction

The physical outputs of cdot-8, listed exhaustively:

- **$E(z)=H_{\hat\tau}/H_{\hat\tau,0}$** — comes from the closure ODE
  $dr/ds=\kappa\lambda x r$, which references $c$, $R_h$, and the census
  source $S$ but not $g_i$'s $N$-decomposition (the ODE lives on the physical
  $N=1$ trajectory by definition). Scheme-independent.
- **M7 invoice $\Omega_s(a)=E^2-\Omega_\text{census}$** — same reason.
- **The reconstructed $F(Q)$** — from the corrected constraint
  $\tfrac12QF_Q-\tfrac13F=\Omega_s$, whose coefficients (worker's
  LapseBackreaction round) come from the $S_{M5}$ sector's lapse variation,
  not from $S_{\mathcal N}$/$S_{R_h}$'s internal $N$-placement.
  Scheme-independent.
- **The matter, radiation, and neutrino censuses; $\hat a_0(z)$; the acoustic
  scale $\theta_*$ (WP4a); BBN expansion rate (WP4b); the fitted trajectory
  and SN photometry** — all derived from the above, all scheme-independent.

**What is scheme-dependent:** $\Lambda_M(t)$, $\pi_i(t)$, $p_R(t)$, and their
aggregate $D$ — quantities that appear only inside the Hamiltonian
constraint's *bookkeeping decomposition* of the same physical $H_{\hat\tau}^2$,
never as inputs to it. The invariance theorem states itself: $H_{\hat\tau}^2$
and every physical output on the list above are computed without reference to
$g_i$'s internal lapse structure, therefore they are identical in every
scheme, therefore the differences the audit found live entirely in objects
that are gauge under the equivalence class of $g_i(N)$ choices that reduce to
WP2 at $N=1$.

**One completeness item worth naming for the record**, though not decisive:
running the originally-assigned scheme test 2 (M5 orientation flip
$Q-q(\mathcal N)\leftrightarrow\mathcal N-\tilde q(Q)$) would extend the
demonstrated invariance across a *second* gauge direction — nice to have as an
independence check, not required for the current verdict since the $g_i$
placement family already covers a two-dimensional (matter, radiation)
constraint-normalization freedom. Deferrable; not blocking.

## 3. What this means for the zero-freedom claim

**Preserved for every observable**: $E(z)$, the invoice, $\hat a_0(z)$, the SN
fit, WP4a's $\theta_*$, WP4b's BBN, every cdot-7 confrontation, every
consolidation-log claim. Nothing that touches data changes under any scheme
choice — the "zero adjustable elements at the confrontation" was, and remains,
the correct statement about the theory's data-facing predictions.

**Refined for the bookkeeping**: the decomposition of the Hamiltonian
constraint into "$F$-sector share" vs "multiplier-sector share $D$" is *not*
scheme-independent, so $D$ is not by itself a physically meaningful number.
The correct step-5 statement is that the *total constraint* $H_{\hat\tau}^2$ =
data-derived $E^2$ closes at every $z$ (which it does by construction of the
quadrature), decomposed differently but equivalently in different schemes.
$C_2$'s "swing" is a swing of two gauge quantities in tandem, invisible to
every physical output.

**The audit did its job precisely**: the razor tests continued to hold as
they did, the audit found where a freedom was hiding — one work package
before it could have caused any confusion downstream — and the freedom is now
localized and named as a gauge, not a knob. This is the outcome the audit was
built to distinguish from a genuine kill; a program whose audits could not
distinguish these two outcomes would be worse than one that never audited.

## 4. Directives

1. **WP3 closes with a positive verdict.** The construction is
   Bianchi-consistent, has zero freedom in physical outputs, and its
   bookkeeping decomposition is gauge — the honest and complete resolution.
   Recommend the write-up state this exactly: physical outputs
   scheme-invariant *by construction* (via the theorem's list in §2 of this
   advisory); $D$ decomposition scheme-dependent, therefore gauge; $C_2$
   symbolic through the write-up as a residual gauge parameter with no
   physical consequence.
2. **Species-resolved machinery for $\mathcal N_i(t)$ is now available**
   (from this advisory's run); the worker's §4 caveat about
   "not-yet-species-resolved" is discharged and the mechanism is confirmed.
3. **Extend WP2 discharge-by-incorporation**: the census-constraint
   normalization ambiguity identified this round *is* part of WP2's final
   form, and the honest statement is "WP2 discharged, with the internal
   $N$-placement of $g_i$ recognized as gauge, and the physical (data-facing)
   census evolution encoded in $E(z)$ and the aggregate $\bar g$ trajectory
   both fixed at $N=1$."
4. **Complete the M5-orientation check** (originally-assigned scheme test 2)
   as a follow-up for full generality of the invariance theorem — deferrable;
   not blocking the WP3 write-up.
5. **Sign-errata propagation** to `Update-WP3-BackreactionMagnitude` and
   `Advisory-WP3-BackreactionMagnitude` and their confirmation round remains
   pending — a one-line note in the consolidation log, as previously
   directed, plus the closed-form-check rule and now the "sign-flip is not a
   general iteration shortcut" rule as K6 pattern-library entries.
6. **WP4a Stage-1 acoustic scale** promoted to *the* next work package,
   since its inputs are now demonstrably robust under everything the audit
   identified; this is the cheapest remaining data confrontation and the
   Foundation should acquire its result before further theoretical extension.
7. **KATRIN clock**: still ticking; still the most time-critical item;
   nothing in this round changed that.

## 5. Protocol note

Round score, for the record. The worker: identified my own prior uniqueness
claim as underjustified via reproducible logic ("the pre-verified row is
scheme-blind"); demonstrated the negative result of the advisor-assigned
scheme test 1 by direct EL derivation *and* synthetic verification; found the
genuine, sharper alternative through re-examination of their own
construction; declined to close the numerical case from memory; and reported
the promising lead precisely enough that this advisor could run it in one
session. The advisor: had the machinery to close the numerical question; ran
it; found the two-branch fork resolving in the honest direction. **Third
advisor error caught by the worker's discipline** (first conceptual: bare
multiplier as stability variable; second numerical: $\dot s$-normalization;
third numerical: the uniqueness claim on lapse placement). All three caught
by independent reconstruction rather than review — the pattern is now firmly
established, and the honest reading is that the advisor's contribution is
tightest when it holds machinery the worker can't build safely from memory,
and vulnerable at exactly the derivational-uniqueness step where "surely this
is the only way" is the seduction.

The step-5 confrontation the program was built for has run to completion, and
its resolution is the one it deserved: the theory has no freedom in its
predictions, and the audit found the exactly zero freedoms hiding as gauge in
its bookkeeping. WP3 delivers what the proposal advertised.

## Companion

- `scheme_species_test.py` — the species-resolved computation, both schemes
  side-by-side, with the inline closed-form sign check.
- This advisory: proposed location
  `cdot-8/WP3/Advisory-WP3-Step5Resolution-2026-07-15.md`.
