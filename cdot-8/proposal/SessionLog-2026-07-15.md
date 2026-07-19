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

---

## Entry 2 — WP3 positive-verdict retraction: closed-action $g_i$ frame-implicit; WP4a promotion held; four cumulative advisor errors owned (advisor session, 2026-07-15, ~14:2x SAST)

**Prompt (verbatim):**
> Seems we're good for WP4 now.
> [uploaded: `Update-WP3-Step5ResolutionAssessment-2026-07-15.md` — worker
> agrees observable-level resolution is solid; challenges the "$D$ is purely
> gauge" characterization on the grounds that it rests on an unverified
> assumption that $\mathcal N_i(t)$ is scheme-independent under real
> $N(t)\ne1$; proposes bounded test: integrate
> $\dot{\mathcal N}_\text{rad}/\mathcal N_\text{rad}=g_\text{rad}^{A,B}(t)$
> with real $N(t)$ along the fitted trajectory, check against $(1+z)^4$;
> recommends proceeding to WP4a immediately (nothing there blocked) but
> holding the gauge conclusion pending the test.]

**Summary (advisor):** **Worker's caution was correct and the test's finding is
larger than either party anticipated.** Ran §3's test (`census_scheme_check.py`):
scheme A saturates at $d\ln\mathcal N_\text{rad}/ds=-9/4$; scheme B decays to
zero; **target is $-6$**, missed by both by many orders of magnitude
(integrated ratio at $z=10^5$: A $2\times10^{-13}$, B $\to0$; target $1$).
Diagnosis: the $g_i$ formula written in the closed-action round is
frame-implicit — inherits WP2's $N=1$-gauge statement, is missing a
$dt/d\hat\tau$ factor somewhere, so *neither* scheme A nor scheme B is the
physically correct closed action. **WP3's "closes positive" verdict retracted;
the observable-level scheme-invariance of $E,F,\hat a_0,\theta_*,\text{BBN}$
survives intact for the reasons given, but the "$D$ is purely gauge" framing
was premature.** Fourth advisor error owned: not numerical (like $\dot s$ and
the sign flip) or derivational (like the uniqueness claim), but **scoping** —
verdict language exceeded what the specific test demonstrated. K6 pattern
library update: verdict-scoping rule adopted (assessment-round protocol
includes challenging verdict framing, not just numerics).

**Directives issued**: (1) retract "closes positive"; **WP4a promotion held**
until §4 frame test resolves — not blocked technically but promoting during
open WP3 sends the wrong signal to consolidator/downstream readers; (3) run
the frame test — compute $g_i$ unambiguously from M4's foliation-integral
definition, compare to A/B, produce the correct third form (or confirm one
of A/B if either survives); (4) re-audit scheme freedom in the corrected
$g_i$ — three possible outcomes all routing through author; (5) WP2 discharge
fully held; (6) consolidation log formalize the four advisor errors and K6
pattern updates in one compact entry (closed-form check rule; sign-flip
iteration rule; verdict-scoping rule). KATRIN clock still ticking.

**Files produced (Entry 2):**
`Advisory-WP3-Step5Retraction-FrameTest-2026-07-15.md`,
`census_scheme_check.py`, `SessionLog-2026-07-15.md` (this file, two entries).

**Open items handed forward:** **frame test of §4 — the single next WP3 task,
bounded, either party can run**; then re-audit of scheme freedom;
WP4a Stage-1 acoustic scale (technically ready, promotion held pending WP3);
WP4b BBN gated on the census kinks; WP2 discharge held; four-error K6
consolidation-log entry; worker log-numbering reconciliation (standing);
all cdot-7 consolidation-log handoffs unchanged; **the KATRIN clock remains
the program's most time-critical item.**

---

## Entry 3 — Worker's coefficient diagnosis confirmed; WP2 formula covariantly correct; fifth advisor error self-caught before publication (advisor session, 2026-07-15, ~16:0x SAST)

**Prompt (verbatim):**
> One more round...
> [uploaded: `Update-WP3-FrameTestFactorOfThree-2026-07-15.md` — worker
> reproduces retraction numerics but flags: (a) the target $(1+z)^4$ is wrong
> for $\mathcal N_\text{rad}$ (census not density fraction); (b) closed-action
> $g_i$ carries coefficient 1 on shell-sweep vs WP2's original 3, an
> arithmetic slip surviving three rounds; (c) the lapse promotion of
> census/horizon sector may itself have been unjustified; recommends direct
> covariant derivation before further scheme testing.]

**Summary (advisor):** **Worker's diagnosis fully confirmed by direct
covariant derivation** (`covariant_gi_derivation.py`): from M4's
foliation-integral $\mathcal N_i\propto c^{p_i^\text{sp}-5/2}R_h^3$ (with
$\dot R_h=c$, not $\dot R_h=Nc$), directly differentiate:
$$d\ln\mathcal N_i/dt=(p_i^\text{sp}-\tfrac52)\dot c/c+3c/R_h$$
— matches WP2's original verbatim, matches worker's algebraic target to
$\sim10^{-10}$ residuals on the fitted trajectory. **Coefficient 3, no
lapse promotion anywhere.** Consequences: $\partial g_i/\partial N=0$
identically, $\delta S_{\mathcal N_i}/\delta N=0$, the "back-reaction on
the Hamiltonian constraint" from the closed-action round **vanishes**
under corrected $g_i$; the entire $C_2$-swing / forward-divergence /
scheme-dependence apparatus of the last four rounds was a shadow cast by
the coefficient corruption, not a feature of the physical theory. The
Hamiltonian constraint reverts to the LapseBackreaction round's form
(no census-sector back-reaction); $C_2$-audit closes trivially with
$D\equiv0$; WP3's zero-freedom claim survives outright rather than
conditionally.

**Fifth advisor error, self-caught pre-publication:** initial
reverse-engineering pass claimed coefficient 2, from an arithmetic slip
conflating $\dot c/c$ (=$\dot s$) with $H_t$ (=$1.5\dot s$) — same
dot-convention family as the earlier $\dot s$-normalization bug.
Verify-before-publish caught it; first-principles derivation gives 3.
Recording as pattern: **inherited numerical conventions across scripts
must be re-verified against first principles at each new advisory**
(fourth K6 rule earned, joining closed-form check, sign-flip iteration,
verdict-scoping). Cumulative error tally: five caught, three by worker's
independent reconstruction, one self-corrected in a follow-up round, one
self-caught pre-publication. The verify-then-trust discipline now runs
symmetrically.

**Directives issued**: (1) worker verification pass on the covariant
derivation and coefficient; (2) re-run constraint contributions with
corrected $g_i$; (3) **WP3 closes on the honest schedule with positive
verdict if step 2 returns $D\equiv0$**; (4) WP4a promotion resumes
immediately after step 2 closes cleanly; (5) consolidation log entry
covers five-error tally + four K6 rules; KATRIN clock unchanged.

**Files produced (Entry 3):**
`Advisory-WP3-CoefficientAndNoLapse-2026-07-15.md`,
`covariant_gi_derivation.py`, `SessionLog-2026-07-15.md` (this file, three
entries).

**Open items handed forward:** worker verification of covariant $g_i$
derivation; re-run of $D$ with corrected formula (expect $D\equiv0$);
**WP3 close pending step 2**; WP4a Stage-1 acoustic scale (resumes on
close); WP4b BBN gated on census kinks; WP2 discharge reopens with
positive conclusion (formula correct as originally stated); consolidation
log entry (five errors + four K6 rules) as a compact combined delivery;
worker log-numbering reconciliation (standing); all cdot-7
consolidation-log handoffs unchanged; **the KATRIN clock remains the
program's most time-critical item.**
