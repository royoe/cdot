# Session Log — cdot-8/WP3 (2026-07-13)

*Continues `SessionLog-2026-07-12.md` (eighteen entries after the duplicate-Entry-16
repair recorded below). Shared, single-writer-at-a-time log per the Entry-9 process
rule (2026-07-12): whoever writes next starts from the repo's current version,
**greps the last entry number before appending**, appends with continuing numbers
and a session-role tag, and delivers the full consolidated file. Times in SAST
(UTC+2).*

---

## Entry 1 — Adjoint-invariant round assessed; addendum delivered; 07-12 log repaired (advisor session, 2026-07-13, ~09:2x–09:4x SAST)

**Prompt (verbatim):**
> One more round...
> [uploaded: `Update-WP3-ExponentTable-2026-07-12.md` (worker: $C_1$-exactness
> verified including an own-slip caught; exponent table on the actual fitted
> trajectory, both directions; finds the radiation-weighted $p_{\mathcal N}$
> homogeneous mode grows as $e^{+3s/2}$ into the deep-MOND future — a genuinely
> new, forward-directed finding — and escalates before the quadrature),
> `Advisory-WP3-AdjointInvariant-2026-07-12.md` (stand-in: the finding is real but
> aimed at the wrong object — the pair obeys mirrored equations, so
> $p_{\mathcal N,i}\mathcal N_i$ is exactly conserved per species; the mode is
> marginal, MM's accepted class; physical couplings carry the product, never bare
> $p$; kicks freeze at injection weight; escalation gate closes subject to a
> three-item coupling audit; mis-specification assigned upstream to the
> advisories' bare-multiplier rows), current `SessionLog-2026-07-12.md`.]

**Summary (advisor):** Both endorsed. Worker numbers cross-checked against held
machinery ($g_\text{rad}(x_0)=-0.063$; critical $x=1.148$; the
$e^{+3s/2}\leftrightarrow1/\mathcal N_\text{rad}$ mirror; the $-0.96$ saturation).
Stand-in's identity verified (one line, airtight); adjoint framing correct;
"marginal by identity" correctly placed in MM's accepted class. **Upstream
correction accepted and extended: this advisor's fifth-round addendum also framed
the open rows as bare-multiplier rows — the mis-specification was shared across
both advisory chairs.** Addendum
(`Addendum-AdjointRound-CoupledInvariant-2026-07-13.md`) adds: (1) the
coupled-system generalization — M5's closure loop makes every $g_i$ depend on the
background hence on $\mathcal N_\text{tot}$, so the per-species product is the
diagonal case of the true conserved object (the symplectic pairing of the full
linearized state–costate system, $\pm\lambda$ structure); audit item 2 sharpened
to: exhibit the coupled linearization's symplectic spectrum at variation time;
(2) audit item 1's first row pre-verified — the lapse channel delivers
$-\sum p_i\mathcal N_i\,\partial g_i/\partial N$, the invariant combination, one
line for the worker to confirm on the closed action; (3) a calibration note: two
priors now coexist (worker-corrections ×4; dissolving-alarms ×3) and neither
decides a round — the bounded check does; the coupling audit is exactly where a
real failure would hide behind the second prior. **Escalation gate closed;
quadrature redo cleared to proceed.**

**Log hygiene executed:** the merged 07-12 log carried a duplicate Entry 16 (the
stand-in's 16–17 collided with this advisor's fifth-round entry); repaired — the
trailing advisor entry renumbered to Entry 18 with a renumber note, content
unchanged. Rule refinement adopted: grep the last entry number before appending.
Worker's private companion numbering ("Entry 11") flagged again for reconciliation
at next delivery. Date rollover: this file opens 2026-07-13.

**Files produced (Entry 1):**
`Addendum-AdjointRound-CoupledInvariant-2026-07-13.md`,
`SessionLog-2026-07-12.md` (repaired, eighteen entries, final pending author
merge), `SessionLog-2026-07-13.md` (this file).

**Open items handed forward:** quadrature redo against the coefficient-$\tfrac12$
constraint with $C_1=0$ (cleared); the coupling audit — items 1 (with its first
row seeded), 2 (sharpened to the coupled symplectic spectrum), 3 ($(R_h,p_R)$
explicitly, not by analogy) — discharging at variation time; then the step-5
confrontation with the Flag 1(d) invariance audit; WP2 finalization still
hard-blocking; WP4a/WP4b and all cdot-7 consolidation-log handoffs unchanged;
**the KATRIN clock remains the program's most time-critical item.**

---

## Entry 2 — $C_2$ round: quadrature verified, the kernel classification, sole-advisor review (advisor session, 2026-07-13, ~10:0x–10:2x SAST)

**Prompt (verbatim):**
> The stand-in has spent his tokens for this month, so now it is you that must do
> the full review. Here is the worker's next flagged issue.
> [uploaded: `Update-WP3-QuadratureRedo-2026-07-13.md` — adjoint identity verified
> to $2\times10^{-16}$; corrected quadrature run ($F=Q^{2/3}[-5\int Q^{-2/3}
> \Omega_s\,ds'+C_2]$, matter-era $F\propto Q^{1.77}$, $s$-grid discipline); a
> second integration constant $C_2$ found, with $F$ "changing sign and diverging"
> in deep radiation under the today-anchor; worker refuses to fix $C_2$ by
> convenience, notes it is not $C_1$, escalates before choosing.]

**Summary (advisor, sole reviewer this round; full verification in
`quadrature_c2.py`):** All worker algebra confirmed — quadrature re-derived
independently, slope $1.773$ reproduced, integrand exponent $-26/9$ confirmed,
grid discipline endorsed. **Resolution: $C_2$ multiplies the kernel of the
corrected Hamiltonian constraint** ($\tfrac12QF_Q-\tfrac13F=0$ for $Q^{2/3}$,
verified) — it is the corrected-coefficient transform of Flag 1(d)'s old $C$
($CQ\to C_2Q^{2/3}$ under the coefficient change), carries identically zero
background energy density, and is asymptotically subdominant in *both* time
directions (verified: $C_2$ varied over four orders of magnitude leaves the
deep-past $F$ unchanged to $10^{-6}$). Hence **no regularity argument applies or
is needed** — the background cannot see it; its channels (pressure shift, current
shift into $\Lambda_M$) all land at step 5, where it either cancels identically
(gauge) or is closure-selected (derived); surviving un-selected in observables
would be the razor failing, i.e. the kill announcing itself. **Directive: carry
$C_2$ symbolically into step 5; do not zero it beforehand.** The reported
"divergence" is the particular solution correctly tracking the invoice —
closed-form pointwise attractors derived and matched against the worker's own
solution ($F/\Omega_s\to30/17$ matter, $15/13$ radiation; numerics $1.80$,
$1.150$) — and the sign change tracks the invoice's zero-crossing, already the
stability sub-directive's target. Two corrections issued: the worker's
$a^{-10/9}$ density figure for the kernel mode is the *old-accounting* value
(zero under the corrected accounting; verify against LapseBackreaction's
definition, not in this advisor's possession); the $C_1$-ambush analogy is
structurally closed for $C_2$ (constraint contribution zero, not small). **A
constant taxonomy recorded** for reuse: current constants → regularity;
kernel constants → step-5 audit; multiplier constants → adjoint pairing +
anchor; classification test: what does the mode contribute to the constraint,
and what does it multiply in the couplings. Worker's private companion numbering
("Entry 12") flagged again.

**Files produced (Entry 2):** `Advisory-WP3-C2Kernel-2026-07-13.md`,
`quadrature_c2.py`, `SessionLog-2026-07-13.md` (this file).

**Open items handed forward:** quadrature output stands with $C_2$ symbolic;
solver validation against the closed-form ratios (one line each); the coupling
audit (items 1–3, item 2 in coupled-symplectic form) at variation time; **step 5
with the now-$(C_2,\Lambda_M)$ invariance audit — the last unexamined slot in the
construction**; WP2 finalization still hard-blocking; WP4a/WP4b and all cdot-7
consolidation-log handoffs unchanged; **the KATRIN clock remains the program's
most time-critical item.**

---

## Entry 3 — Closed-action round: coupling audit endorsed, back-reaction magnitude computed (advisor session, sole reviewer, 2026-07-13, ~11:0x–11:3x SAST)

**Prompt (verbatim):**
> Next round...
> [uploaded: `Update-WP3-ClosedActionCouplingAudit-2026-07-13.md` — the action
> closed over all dynamical variables for the first time (species-resolved census
> pairs with general-lapse $g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+Nc/R_h$; $R_h$
> promoted with $\dot R_h=Nc$; all EOMs verified against a solved coupled system,
> residuals $10^{-9}$–$10^{-11}$); coupling audit discharged (item 1: passes for
> $p_i$, genuine bare exception for $p_R$; item 2: species coupled through the
> shared $\Lambda_M$ source, sourced identity
> $\dot\pi_i=-\Lambda_Mq'(\mathcal N_\text{tot})\mathcal N_i$ supersedes exact
> conservation; item 3: $(R_h,p_R)$ a pure sourced integral needing its own
> past-regularity condition); NEW FINDING: $S_{\mathcal N}$/$S_{R_h}$ back-react
> on the Hamiltonian constraint via
> $+\tfrac{8\pi G}{3a^3}[\sum_i\pi_i c/R_h+p_Rc]$; magnitude deliberately
> deferred for lack of the real machinery; check-in requested before step 5.]

**Summary (advisor):** Closed action endorsed. Lapse placement validated three
ways — $N=1$ reduction, the pre-verified lapse row, and (new) an independent
reconstruction of the unseen LapseBackreaction document's $\tfrac13\to\tfrac12$
coefficient shift from $\Lambda_M=Na^3F_Q/16\pi\tilde G$, cross-validating the
whole convention chain. Audit dispositions all confirmed, with two additions: the
frozen-kick stability conclusion survives the sourcing (the source is
$p$-independent, so $\delta\dot\pi_i=0$ for kicks), and $g_i$'s
$\dot a$-dependence puts the census sector into the *acceleration* equation — a
named step-5 ledger item. **The deferred magnitude computed with the real
machinery** (`backreaction_magnitude.py`; trajectory-exact
$q'\mathcal N_\text{tot}=\dot Q/(d\ln\mathcal N_\text{tot}/dt)$, species-resolved
$\bar g=d\ln S/ds+3\kappa\lambda x-\tfrac12$; retarded integrals, convergence
verified): the new term is **late-time and few-percent** — $D/E^2$ peaks at
$-4.85\%$ exactly at $z=0$ ($p_R$ channel $0.8\%$), falls to $-1.7\%$ at $z=1$,
$-10^{-5}$ at $z=100$, $-7\times10^{-8}$ at recombination, $10^{-12}$ deep
radiation; $C_2$ channel bounded at $\sim10^{-2}$ per unit and stays symbolic.
**Consequences:** the constraint shifts a third time but perturbatively —
$\Omega_s^\text{corr}=\Omega_s-D$ (scalar supplies up to $+4.85\%$ more, at
$z\lesssim2$ only); one self-consistent quadrature iteration (feedback second
order at $\sim5\%$ per pass) suffices; **WP4a/WP4b inputs untouched; step 5
cleared** on the once-iterated constraint with the full ledger (continuity
contributions of the $\pi_i$/$p_R$ sectors, the acceleration channel, the
$(C_2,\Lambda_M)$ audit). Proposed recording WP2 as discharged-by-incorporation
(the closed action embeds its evolution equation as the $S_{\mathcal N_i}$
constraints), pending worker confirmation. Worker's private companion numbering
("Entry 14") flagged again.

**Files produced (Entry 3):** `Advisory-WP3-BackreactionMagnitude-2026-07-13.md`,
`backreaction_magnitude.py`, `SessionLog-2026-07-13.md` (this file).

**Open items handed forward:** worker verification of the working relations; the
one-pass quadrature iteration with its convergence delta; **step 5 — the razor /
total-Bianchi confrontation — now genuinely unobstructed**; WP2
discharge-by-incorporation decision; WP4a Stage-1 acoustic scale
(promoted-immediate, inputs confirmed stable); WP4b BBN gated on the
$e^+e^-$/QCD census kinks; all cdot-7 consolidation-log handoffs unchanged;
**the KATRIN clock remains the program's most time-critical item.**

---

## Entry 4 — Worker's normalization correction confirmed; advisor's bug owned; step 5 cleared on the corrected constraint (advisor session, 2026-07-13, ~12:0x–12:2x SAST)

**Prompt (verbatim):**
> Next one...
> [uploaded: `Update-WP3-BackreactionMagnitudeCorrected-2026-07-13.md` — worker
> finds a normalization bug in the advisor's `backreaction_magnitude.py`: the
> $\pi_\text{tot}$ and $P$ sources are genuine $d/dt$ rates integrated as if per
> unit $s$; missing factor $\dot s=\tfrac23NE$; found by independent from-scratch
> cross-check (gold-standard $t$-axis integration), verified three ways;
> corrected peak $D/E^2=-9.5\%$ at $z=0$ (~double the advisory's $-4.85\%$);
> two-pass iteration converges ($-1.028\times10^{-1}$, $0.4\%$ second-pass
> delta); WP4a/WP4b untouched; audit dispositions unaffected; requests advisor
> confirmation before step 5.]

**Summary (advisor):** **Confirmed on every count; the bug was the advisor's.**
Hand re-derivation reproduces the diagnosis exactly — the parametrization-free
ratio $q'\mathcal N_\text{tot}=(dQ/ds)/\bar g$ made
$\dot{\tilde\pi}=\tfrac52a^3F_Q/\bar g$ (a $d/dt$ rate with no visible dots) look
$s$-native; the $P$-source lost its $\dot s$ between derivation and script.
Independent numerical confirmation (`backreaction_corrected.py`, including a
from-scratch rebuild of the worker's gold-standard $t$-axis method, agreement
$1.5\times10^{-4}$): all seven table points reproduced to the digit; iteration
deltas exactly $7.38\%$/$0.40\%$, converged $D_2/E^2=-1.0284\times10^{-1}$ at
$z=0$; recombination $-6.8\times10^{-7}$ (WP4a untouched). The gold-standard
$t$-axis method adopted as standard verification for any future cross-axis
computation; "booby-trapped expression" (internally cancelled Jacobians) named
for the pattern library. Clarification pinned: **M7's invoice
$\Omega_s=E^2-\Omega_\text{census}$ is unchanged throughout** — only the internal
decomposition shifted ($F$-sector supplies $\Omega_s-D$, up to $+10.3\%$ at
$z=0$; multiplier sectors supply $D$). **Step 5 formally cleared** on the
twice-iterated constraint with the full ledger ($\pi$/$p_R$ continuity
contributions, the acceleration channel, the $(C_2,\Lambda_M)$ audit; $C_2$
symbolic). Protocol note recorded: second advisor error caught by downstream
independent reconstruction (first conceptual, this one numerical) — the
program's error-catching is demonstrably bidirectional.

**Files produced (Entry 4):**
`Advisory-WP3-MagnitudeCorrectionConfirmed-2026-07-13.md`,
`backreaction_corrected.py`, `SessionLog-2026-07-13.md` (this file).

**Open items handed forward:** **step 5 — the razor / total-Bianchi
confrontation on $\Omega_s^\text{corr}=\Omega_s-D_2$ — is the entire remaining
queue for WP3**, plus: WP2 discharge-by-incorporation confirmation (unblock
before or with step 5); worker log-numbering reconciliation (standing); WP4a
Stage-1 acoustic scale (promoted-immediate, inputs stable); WP4b BBN gated on
the $e^+e^-$/QCD census kinks; all cdot-7 consolidation-log handoffs unchanged;
**the KATRIN clock remains the program's most time-critical item.**

---

## Entry 5 — Step-5 audit round: worker confirmed and extended; forward divergence universal; scheme-dependence hypothesis with decisive test; advisor sign bug owned (advisor session, 2026-07-13, ~13:0x–13:4x SAST)

**Prompt (verbatim):**
> One more check, please.
> [uploaded: `Update-WP3-Step5Confrontation-2026-07-13.md` — step 5 run in full:
> acceleration channel derived and verified (convergence-swept finite
> differences); total-Bianchi correctly stated as structural; the razor
> recognized as holding by construction (not an independent test once the
> action closed); the $(C_2,\Lambda_M)$ audit finds $C_2$ does NOT cancel —
> converged $D/E^2(z{=}0)$ swings $-0.10\to+0.97$ over trial $C_2$; the one
> internal closure candidate ($D\equiv0$) has no common root; three resolution
> candidates listed; escalated rather than resolved alone.]

**Summary (advisor; full treatment in `c2_future_audit.py` + sign-diagnosis
snippet):** Three findings. **(1) Advisor sign bug owned** — the magnitude
scripts' reversed-grid quadrature carried $F/\Omega_s=-1.764$ where the
validated value is $+30/17$; propagated to the worker's cross-check via the
inherited quadrature block (their independently-built kernel channel matches
exactly, confirming the diagnosis). All magnitudes, convergence, and
WP4a/WP4b-negligibility unchanged; all sign statements flip ($D(z{=}0)=+9.5\%$;
multiplier sector *adds*, $F$-sector supplies *less*). Rule adopted: inline
closed-form ratio check in any script consuming a reconstructed $F$. **(2)
Worker's audit confirmed and extended** — with iteration off,
$D=D_\text{part}+C_2D_\text{ker}$ exactly; swing reproduced; and the FORWARD
integration (never before run for this sector: to $s{=}3$, $x{=}0.011$,
$\bar g{=}1.5\times10^{-2}$) shows **both channels diverge into the deep-MOND
future with unequal slopes (1.73, 1.32 measured; 1, 5/6 asymptotic)** —
$C_2^*(s)$ drifts with no limit — so candidate 1 (future-boundedness) fails
universally: no $C_2$ bounds the future. Root cause localized: not $q'$
($\to0$), not the M5 constraint share ($\to0$, benign) — the census/horizon
multiplier integrals, whose source carries $\Lambda_M\propto Na^3F_Q$, the
coordinate-volume factor. **(3) The suspect promoted with mechanism**: $D$ is
plausibly scheme-dependent — on-shell-equivalent constraint rewritings
$\mathcal C\to f\mathcal C$ rescale multipliers $p\to p/f$, and past-regularity
("$p\to0$") selects different solutions when $f$ is unbounded ($f{=}N$ is); $D$
is an integrated multiplier functional and inherits the choice. The
$C_2$-swing and the divergence read as two symptoms of the un-pinned
census/M5 constraint normalization. **Decisive bounded test assigned**:
recompute $D$ in the $N$-normalized and orientation-flipped schemes; if $D$
moves → prove the invariance theorem for physical outputs (zero-freedom
survives for observables; $D$'s decomposition recorded as gauge); if $D$ is
scheme-invariant and still $C_2$-swung → **WP3's kill condition triggers, in
earnest, for the first time**. Pinned for the record: $E(z)$, M7's invoice, the
$F$ reconstruction, and all WP4a/WP4b inputs verified $C_2$-robust — the
episode concerns only whether the covariant bookkeeping sector is gauge or
physical; nothing cdot-7 owns is touched. WP2 discharge held pending the test
(the constraint normalization IS WP2's final form).

**Files produced (Entry 5):** `Advisory-WP3-Step5Audit-SchemeTest-2026-07-13.md`,
`c2_future_audit.py`, `SessionLog-2026-07-13.md` (this file).

**Open items handed forward:** **the scheme test — the single next WP3 task,
decisive by construction, two-branch fork routed through the author either
way**; sign-errata propagation to the two magnitude documents; WP2 discharge
confirmation held; worker log-numbering reconciliation (standing); WP4a
Stage-1 acoustic scale (promoted-immediate, inputs re-verified robust); WP4b
BBN gated on the census kinks; all cdot-7 consolidation-log handoffs
unchanged; **the KATRIN clock remains the program's most time-critical item.**
