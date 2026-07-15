# Session Log — cdot-8/WP3 (2026-07-15)

*Continues `SessionLog-2026-07-13.md` (five entries: adjoint-round addendum
with log repair; $C_2$-kernel classification; back-reaction magnitude
[buggy]; magnitude correction confirmed with second advisor error owned;
step-5 audit surfacing $C_2$-swing and forward divergence with scheme-test
directive). Two-day gap on cdot-8 side is real: platform storage outage
2026-07-13 (see Entry 5 tail there) followed by author-side scheduling.
Shared, single-writer-at-a-time log per the Entry-9 process rule
(2026-07-12): whoever writes next starts from the repo's current version,
greps the last entry number before appending, appends with continuing
numbers and a session-role tag, and delivers the full consolidated file.
Times in SAST (UTC+2).*

---

## Entry 1 — WP3 Step-5 Resolution: scheme-dependence confirmed, honest branch wins, WP3 closes with positive verdict (advisor session, 2026-07-15, ~10:0x–10:3x SAST)

**Prompt (verbatim):**
> [uploaded: `Update-WP3-SchemeTestPartial-2026-07-15.md`]
> Next step:

**Summary (advisor; full treatment in `scheme_species_test.py`):** Ran the
worker's identified scheme test 2 ($g_i$-internal lapse placement) numerically
on the species-resolved fitted trajectory — the closure the worker correctly
declined to attempt from memory. **Result: $D/E^2(z=0)=+0.138$ under Scheme
A** (advisor's original $g_i=(p^\text{sp}-\tfrac52)\dot c/c+Nc/R_h$) **vs
$-0.023$ under Scheme B** (worker's alternative with $N$ multiplying the whole
bracket) — order-unity difference, opposite sign near today, magnitudes
suppressed by factor $\sim6$–$100$ throughout under B. $C_2$ kernel channel
also differs (per-unit-$C_2$: $+2.8\times10^{-2}$ A, $-7.4\times10^{-3}$ B at
$z=0$). **Scheme-dependence proven by direct construction via the worker's
sharper mechanism.**

**Invariance theorem stated and verified**: $E(z)$, M7 invoice, $F(Q)$
reconstruction, $\hat a_0(z)$, WP4a's $\theta_*$, WP4b's BBN rate, matter and
census dynamics — all built from the closure ODE and quadrature, neither of
which reference $g_i$'s internal $N$-placement — therefore scheme-invariant
by construction. What is scheme-dependent: $\Lambda_M(t)$, $\pi_i(t)$,
$p_R(t)$, and their aggregate $D$ — bookkeeping-decomposition quantities only.
$C_2$'s "swing" is a swing of two gauge quantities in tandem, invisible to
every physical output. **Two-branch fork resolves on the honest branch: WP3
kill condition does not trigger; zero-freedom claim survives for observables;
$D$ decomposition is gauge.**

**Corrections and confirmations:** (a) worker's diagnosis of my prior
"uniqueness" claim was correct — the pre-verified lapse row is scheme-blind,
recorded as third advisor error caught by worker's discipline (first
conceptual: bare-multiplier stability variable; second numerical:
$\dot s$-normalization; third: this one); (b) worker's iteration-nonlinearity
observation ("sign-flip is not a general shortcut for iterated computations")
adopted into K6 pattern library alongside the inline closed-form check rule;
(c) worker's scheme test 1 (uniform bracket rescaling) negative result
confirmed by structure — $\tilde p N=p$ exactly for retarded solutions.
Inline closed-form check on this session's $F$ gave $+1.82$ vs target $+30/17=
+1.76$ — sign correct, small iteration residual within expected.

**WP2 discharge extended**: the $g_i$-internal $N$-placement gauge is *part
of WP2's final form*; the honest statement is "WP2 discharged, with the
internal placement recognized as gauge and the physical census evolution
fixed at $N=1$."

**Files produced (Entry 1):** `Advisory-WP3-Step5Resolution-2026-07-15.md`,
`scheme_species_test.py`, `SessionLog-2026-07-15.md` (this file).

**Open items handed forward:** **WP4a Stage-1 acoustic scale is now the next
work package**, inputs demonstrably robust under all identified gauge
freedoms; **WP3 write-up** stating the invariance theorem, $D$ as gauge,
$C_2$ as residual gauge parameter, all physical outputs zero-freedom; the
M5-orientation follow-up check (originally-assigned scheme test 2 in its
first version) as a deferrable follow-up for full theorem generality;
sign-errata propagation to the two `BackreactionMagnitude` documents plus
K6 pattern-library entries; worker log-numbering reconciliation (standing);
WP4b BBN gated on the $e^+e^-$/QCD census kinks; all cdot-7 consolidation-log
handoffs unchanged; **the KATRIN clock remains the program's most
time-critical item.**
