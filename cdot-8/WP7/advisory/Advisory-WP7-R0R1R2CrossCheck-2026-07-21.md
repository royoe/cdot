# Advisory — R0, R1, R2 Cross-Checked: All Three Confirmed Numerically and (Where Applicable) Against Primary Source — Plus One New Finding Neither the Main Advisor Nor the Worker Flagged: the Founding Paper's Own Stability Section States a Separate $\lambda_s>0$ Condition That R1's Own Recommended Direction ($\lambda_s\to-1$) Directly Contradicts (for `cdot-8/WP7/`)

*2026-07-21. Cross-check of `Advisory-WP7-InstabilityRecourses-2026-07-21.md`
(main advisor) and WP7 §44–46 (worker's R0/R1/R2 attempts). Every script
run directly; the R0(a) and R1 primary-source claims independently
re-checked against `references/arXiv.2007.00082/newRMONDLett.tex`
directly, not taken on citation. Gate 1(b) and Gate 4 (this item's own
paused status) both carried. **Verdict up front: R0 and R2 both
confirmed exactly — dominance decomposition, primary-source quote, and
the AeST-native stability contrast all reproduce to the reported
precision or better. R1's numerics also reproduce exactly. But reading
the same primary-source stability section the R0(a)/R1 work already
cites, one paragraph further, turns up a condition nobody has flagged
yet: the paper states its residual ($\omega=0$) vector mode's
Hamiltonian positivity "also requir[es] that $\lambda_s>0$" — directly
inside the same healthy-range discussion R1 draws $\lambda_s>-1$ from.
R1's own recommended sweet spot ($\lambda_s$ comfortably negative,
close to $-1$) sits squarely in the range this second condition
excludes. This doesn't overturn R0/R1/R2's verdicts, but it sharpens
exactly what the still-missing action-level derivation needs to
resolve, and it belongs in the record before $\lambda_s$ near $-1$ is
treated as more than a plausibility signal.**

---

## 1. R0(a) confirmed — checked against primary source directly, not on citation

Read `references/arXiv.2007.00082/newRMONDLett.tex` (the archived
source) at the "Stability and waves" section myself. Line 551 reads,
verbatim: *"where we have used the desired late Universe limit for
which $\partial^2\bar{\mathcal F}/\partial\mathcal Q^2\to-2\,d^2
\mathcal K/d\mathcal Q^2=-4\mathcal K_2$ and $\partial\mathcal F/
\partial\mathcal Q=\bar{\mathcal F}=0$."* Matches R0(a)'s quote exactly,
character for character. The vector mode's dispersion relation and mass
(line 558: $\omega^2=k^2+\mathcal M^2$, $\mathcal M^2=(2-\mathcal
K_B)(1+\lambda_s)\mathcal Q_0^2/\mathcal K_B$, healthy iff $0<\mathcal
K_B<2$ and $\lambda_s>-1$) and the scalar mode's dispersion (line 564:
$\omega^2=\big[(2-\mathcal K_B)/(\mathcal K_2\mathcal K_B)\big](1+
\tfrac12\mathcal K_B\lambda_s)k^2+\mathcal M^2$) both match the
worker's citations exactly. **R0(a)'s finding stands: the founding
paper's own stability argument is built on $F_\mathcal Q(\text{
background})=0$, a condition cdot-8's own trajectory never approaches
($F_Q\in[1.85,4473]$) — the paper's healthy-range claim simply doesn't
cover the region cdot-8 operates in.** The precise qualifier (the
cosmological equations of motion themselves were correctly imported in
general form, per Stage 2's own independent confirmation that the
$\mathcal E_\alpha$ equation's $d\mathcal K/d\mathcal Q$ coefficient was
never assumed zero) is exactly right and worth keeping — this is a gap
in the *stability argument's own domain of validity*, not in what was
imported.

## 2. R0(b) confirmed — re-derived the decomposition by hand before trusting the code

Worked out $\partial\dot{\mathcal E}_\alpha/\partial\alpha$'s four
pieces from `aEE_aEalpha`'s own defining substitutions independently
(not just read off the script): expanding $\dot{\mathcal E}_\alpha$'s
formula with $\partial\chi/\partial\alpha=\bar{\mathcal Q}$ and
$\partial\Pi/\partial\alpha=\text{kap3}\cdot(2-\mathcal K_B)\bar
{\mathcal Q}$ substituted in gives exactly the claimed four additive
terms $A,B,C,D$, term for term — $B$ is the only one carrying
$\text{kap3}=c_\text{ad}^2\kappa/(3\Omega_s)$, confirming by
construction (not merely by running the script) that it is the sole
$\kappa$-dependent piece. Ran `wp7_r0_instability_source_audit.py`
directly: reproduced the table exactly. **One thing worth stating more
strongly than the write-up did**: at $z=100$, $B\approx1.21\times10^9$
against $A+C+D\approx-4.0\times10^4$ — a **four-and-a-half order of
magnitude** dominance, not the "1–2 orders" quoted (which holds at
$z=0.5$–$1$, where the gap is closer to one order). This doesn't change
the conclusion, it strengthens it — $B$'s dominance is even more total
at high $z$ than reported.

## 3. R1 confirmed numerically — and a new primary-source finding that sharpens its risk

Ran `wp7_r1_gradient_completion_feasibility.py` directly: every
reported number reproduced exactly ($\lambda_s=-0.999$:
$\max\text{Re}(\lambda)=335584$ at $z=1090$, matching "reduces $3.4
\times10^8\to3.4\times10^5$"; $\lambda_s=-1$ exactly: $\text{Re}(
\lambda)=-0.5$ at every one of the five tested redshifts, exactly
$k$-independent as claimed).

**Went back to the same primary-source paragraph R0(a)/R1 already cite,
one sentence further, and found something neither the main advisor's
advisory nor the worker's R1 write-up mentions.** Immediately after the
vector/scalar mode dispersion relations, the paper states (lines
565–571, quoted in full since the exact wording matters):

> *"Thus, we require that $\mathcal K_2>0$ in addition to the vector
> stability conditions. Only two normal modes exist implying the
> presence of constraints. These are revealed through a Hamiltonian
> analysis which also shows that these conditions lead to a positive
> Hamiltonian [...] for the $\omega\neq0$ modes. The $\omega=0$ case
> leads to a constant mode with zero Hamiltonian but, also, to a mode
> varying linearly with $t$. The Hamiltonian for the latter is positive
> for momenta larger than $\sim\mu$ and otherwise negative, also
> requiring that $\lambda_s>0$."*

Read plainly, this states a **second, separate condition** — $\lambda_s
>0$ — tied to a residual, non-propagating ($\omega=0$) vector mode's
own Hamiltonian, distinct from the $\lambda_s>-1$ condition on the
propagating ($\omega\neq0$) modes R1 draws its "healthy range" from.
**R1's own recommended direction — $\lambda_s$ comfortably negative,
approaching $-1$ from above (e.g. $-0.9$ to $-0.999$) — sits entirely
inside the range this second condition appears to exclude.** I could
not fully resolve from the compact PRL text alone how binding this
condition is in practice (the Hamiltonian analysis itself is cited to
two in-preparation companion papers, not available here, and "positive
for momenta larger than $\sim\mu$, otherwise negative" is itself framed
in the very next sentence as an expected, tolerated Jeans-type feature
at low momenta — not obviously fatal) — but the text is explicit that
$\lambda_s>0$ is *also required*, and R1's own favored operating point
is $\lambda_s<0$. This is exactly the kind of thing that needs settling
before $\lambda_s$ near $-1$ moves past "feasibility signal."

**This adds a second, independent open question to R1's own genuinely
flagged gap** (the missing action-level FRW derivation), not a
replacement for it: even granting the $(2-\mathcal K_B)\to(2-\mathcal
K_B)(1+\lambda_s)$ structural hypothesis outright, the specific
$\lambda_s$ values that suppress the ISW-scale instability may conflict
with a *different* stability requirement the same founding paper states
for a different mode. Recommend this be carried forward explicitly
alongside the already-flagged gap, and — if the eventual action-level
derivation is attempted — that it also work out what the residual
$\omega=0$ mode's Hamiltonian actually requires in the FRW (not
Minkowski) setting, since it is not obvious the Minkowski-background
condition transfers unchanged.

## 4. R2 confirmed — one trivial, inconsequential artifact noted for completeness

Ran `wp7_r2_aest_native_crosscheck.py` directly: $c_\text{ad}^2$ at
recombination $\approx-6.51\times10^{-4}$ (matches "$\approx-6.5\times
10^{-4}$"); the transient at $z=1090$ for the two larger $k$'s
reproduced almost exactly ($2.59$ and $13.28$ against the reported
"$2.6$ and $13.3$"); full stability ($\text{Re}(\lambda)=-0.5$) at
every ISW $k$ from $z=10$ down to $z=0$, confirmed. **One small thing
worth a passing note, not a substantive one**: the printed $c_\text{
ad}^2(z=0)$ shows a small sign flip and magnitude jump ($+1.08\times
10^{-10}$, versus a smooth $\sim-3\times10^{-13}$ trend at $z=0.1$ and
nearby) — almost certainly the same `np.gradient` array-edge effect
flagged in §43, surfacing here despite `edge_order=2` already being
used, apparently because it's evaluated at the literal last grid point
of *this* script's own array. **It doesn't affect the actual verdict**:
the eigenvalue at $z=0$ is a clean $-0.5$, identical to $z=0.1,1,10$ —
at these tiny $|c_\text{ad}^2|$ values the $\kappa$-independent terms
already dominate, so the artifact never reaches the reported stability
conclusion. Flagged only so the general "watch array edges near $z=0$
for derivative-built quantities" lesson from §43 is recorded as
recurring, not resolved once and for all.

## 5. Overall assessment

R0 and R2 together stand as reported: the pathology is confirmed
cdot-8-specific (AeST's own native, minimum-tracking $F(\mathcal Q)$
stays stable at the same $k$'s where cdot-8's forced, non-tracking
$F(\mathcal Q)$ never restabilizes), and the unstable direction is
confirmed to sit in exactly the $\kappa$-linear slot an $F_\mathcal
Y(0,\mathcal Q)$ completion would renormalize. R1 remains what the
worker correctly called it — a genuine, quantitatively well-defined
feasibility signal, not a validated recourse — and the new $\lambda_s>0$
finding means the honest gap list for R1 now has two items, not one:
(i) no action-level FRW derivation of how $F_\mathcal Y$ enters this
system exists yet; (ii) the Minkowski-background stability analysis
itself, read in full, states a condition ($\lambda_s>0$) that the
numerically-favored suppression range ($\lambda_s\to-1^-$) appears to
violate, and whether that condition survives, transfers, or relaxes in
the FRW setting is unknown. Both belong in whatever gets reported back
to the author alongside R0/R1/R2's own results — this remains routed
for a sequencing decision, not resolved here.

## 6. Housekeeping

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, Gate 4's paused
status, $Q_2$/EFE sequencing, and KATRIN watch are all unchanged.

## Companion

- No new script — all four checks reused the existing R0/R1/R2 scripts
  and `isw_instability_recourses.py` directly, plus a direct read of
  `references/arXiv.2007.00082/newRMONDLett.tex` for §1/§3's
  primary-source claims.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-R0R1R2CrossCheck-2026-07-21.md`.
