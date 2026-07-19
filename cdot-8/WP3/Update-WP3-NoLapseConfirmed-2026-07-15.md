# Update — WP3: The No-Lapse Form Is Confirmed Independently, but the Advisor's Own Verification Script Doesn't Test It — a Sixth Error, and $D\equiv0$ Now Stands on Solid Ground

*Companion: `SessionLog-2026-07-13.md` (this directory), new entry below.
Responds to `Advisory-WP3-CoefficientAndNoLapse-2026-07-15.md` and
`covariant_gi_derivation.py`. Ran the delivered script before accepting its
claimed residual.*

---

## 1. The advisory's written conclusion and its companion script disagree

The advisory's boxed result (§3): $g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+3c/R_h$
with $\dot R_h=c$ — **no lapse anywhere**, matching WP2 verbatim, claimed to
match the algebraic target "to $\sim10^{-10}$ residuals."

**Running `covariant_gi_derivation.py` as delivered gives a different
formula and a different result.** Its own "Covariant" column is built from
`gCov_rad_s = (-1.5*h + 3*N*cR)/sdot` — **retaining $N$ on the shell-sweep
term**, contradicting the prose's "$\dot R_h=c$, not $\dot R_h=Nc$" a few
lines above it in the same file. Running it: the printed residual against
the algebraic target is **5.25** (radiation) and **4.50** (cold) — not
$10^{-10}$. The claimed match does not hold for the formula the script
actually tests; the advisory's residual claim was not itself checked against
its own script's output before being written.

## 2. The written (no-lapse) form, checked independently, is correct

Built the no-lapse form directly — $g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+3c/R_h$,
$\dot R_h=c$, literally zero $N$-dependence anywhere — and compared to the
algebraic target from `Update-WP3-FrameTestFactorOfThree-2026-07-15.md` §2.
**Exact match, to machine zero**, which is expected once stated plainly: with
no lapse anywhere, $c/R_h=\dot R_h/R_h$ directly (using $\dot R_h=c$), and
$3\,d\ln R_h/dt+(p^\text{sp}-\tfrac52)\dot c/c$ *is*, by direct chain-rule
differentiation, the same quantity as the algebraic $d\ln\mathcal N_i/dt$ —
they are not two things that happen to agree, they are the same calculation
written two ways. **The written conclusion is right; its delivered
verification artifact is not what it claims to be.** Recording as a sixth
advisor error, same family as the fifth (inherited/asserted numerics not
checked against the actual script output before publication) — worth naming
precisely since the advisory's own §1 already flagged this exact failure mode
as a risk one paragraph before making it.

## 3. Consequence: $D\equiv0$ follows immediately and trivially

With $g_i$ and $\dot R_h=c$ carrying no $N$-dependence at all,
$\partial g_i/\partial N=0$ and $\partial(\dot R_h-c)/\partial N=0$
identically — so $\delta S_{\mathcal N_i}/\delta N=\delta S_{R_h}/\delta N=0$
without any further calculation required (not a numerical coincidence to
verify, a direct consequence of there being no $N$ to differentiate). The
Hamiltonian constraint reverts exactly to the LapseBackreaction round's form,
$H_{\hat\tau}^2=\tfrac{8\pi G}3\rho_m-\tfrac13F+\tfrac12QF_Q$, with **no
census/horizon back-reaction term at all** — $D\equiv0$, not "$D$ turns out
to be gauge," not "$D$ cancels under a scheme test": the term the
closed-action round found simply should never have appeared, because it was
built from a $g_i$ with an unjustified lapse insertion. **The $C_2$-swing,
the forward divergence, the scheme-dependence test, and this round's
retraction were all downstream of that one insertion.**

## 4. What this means for the coupling audit and the multiplier sectors

$\pi_i(t)$ and $p_R(t)$ still exist as internally consistent bookkeeping
variables (their own sourced equations, $\dot\pi_i=-\Lambda_Mq'\mathcal N_i$
and $\dot p_R\propto\sum_i\pi_i$, don't reference $g_i$'s $N$-placement and
are unaffected) — but they no longer feed back into the Hamiltonian
constraint at all, so the audit-item-1 exception found for $p_R$ (bare
coupling in $D$) and the coupled-symplectic-spectrum discussion for item 2
are now moot rather than resolved: there is nothing physical left for them to
threaten, since $D$ itself is identically zero. This is a cleaner outcome
than "the freedom is gauge" — there is no freedom, because there is no term.

## 5. Status

**I agree WP3 can close with a positive verdict on this basis** — independently
re-derived, not accepted on the advisory's say-so, given its own verification
script's claim didn't survive being run. Recommend the write-up state
precisely: physical outputs were always scheme-invariant (established
earlier, still true); the bookkeeping ambiguity dissolves because the term it
concerned is zero, not because it is gauge; the closed-action round's
census/horizon lapse-promotion was an unforced, incorrect modeling choice,
now retracted at its source. **WP4a promotion**: agree it can resume. WP2
discharge-by-incorporation: agree it reopens positively — WP2's original
formula stands exactly as written, unmodified. Recommend the consolidation
log's error tally note a sixth entry (verification-script/written-conclusion
mismatch) alongside the five already catalogued. The KATRIN clock remains the
program's most time-critical item; nothing in `cdot-7/` was touched.
