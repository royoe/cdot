# Update — WP3: Sign Bug Confirmed, Forward Divergence Reproduced, Scheme-Test 1 Clears — but the Real Ambiguity Is Elsewhere, in My Own Construction

*Companion: `SessionLog-2026-07-13.md` (proposal side, Entry 5) and this
directory's session log, new entry below. Responds to
`Advisory-WP3-Step5Audit-SchemeTest-2026-07-13.md` and `c2_future_audit.py`.
Every claim independently re-derived or re-run before use, per standing
protocol — including re-examining my own prior "unique lapse convention" claim
from `Update-WP3-ClosedActionCouplingAudit-2026-07-13.md`, which this round
finds was underjustified.*

---

## 1. Sign bug — confirmed independently, with one nuance the advisor's writeup didn't flag

Reproduced the diagnosis from scratch: my own `corrected_backreaction.py` gives
$F/\Omega_s=-1.797$ in the matter era where the verified value is $+30/17=
+1.765$ — confirmed via a direct probe of what
`cumulative_trapezoid(integ[::-1], s[::-1], initial=0)[::-1]` actually computes
(it is $\int_0^s$, not $\int_s^0$ as my code's own comment mistakenly claimed).
Fixed ($F=Q^{2/3}(-5.0\,I_\text{full})$, not $-5.0\times(-I_\text{full})$) and
confirmed the closed-form ratio recovers $+1.797,+1.796,+1.822\to+30/17$
correctly.

**One nuance beyond what the advisor's writeup states**: the advisory says
"every $D$ magnitude... unchanged; every sign statement flips," true for the
**un-iterated** ($D_0$) value ($-0.0954\to+0.0954$, matches exactly). But the
**fully-iterated, converged** $D$ does *not* simply flip sign — it converges to
a different **magnitude**: $+0.0888$ (fixed sign, converged) vs. $0.1029$
(bug, converged), an $\sim14\%$ difference, because $\Omega_s^\text{corr}=
\Omega_s-D$ is not symmetric under $D\to-D$ once iterated (the iteration is
nonlinear in exactly the way sign matters). Worth recording precisely rather
than accepting "magnitudes unchanged" at face value for the number that
actually gets used downstream.

## 2. Forward divergence — reproduced exactly

Ran `c2_future_audit.py` directly: matches the advisory's table to the digit
(swing at $z=0$; forward growth exponents $1.728,1.323$; $C_2^*(s)$ drift
$-4.68\to-1.53\to-2.48$). No discrepancy found. Candidate 1
(future-boundedness fixing $C_2$) fails exactly as reported — confirmed, not
just accepted.

## 3. Scheme test 1 (uniform $N$ multiplying the whole constraint bracket) — no scheme dependence found

Tested the advisory's specific proposal: rewrite $S_{\mathcal N_i}=\int
p_i(\dot{\mathcal N}_i-\mathcal N_ig_i)dt\to\int\tilde p_iN(\dot{\mathcal
N}_i-\mathcal N_ig_i)dt$ (leaving $g_i$'s own form untouched). Derived the
tilde-scheme's own Euler-Lagrange equation directly (not assumed): $\dot{\tilde
p}_i=-\tilde p_i(g_i+\dot N/N)-\Lambda_Mq'/N$, whose homogeneous mode is
$p_i^\text{hom}/N$. **Since $p_i^\text{hom}$ already diverges as $t\to-\infty$
and $N\to0$ there, dividing by $N$ makes it diverge *faster*, not slower or
differently** — so "kill the divergent homogeneous mode" selects the identical
coefficient (zero) in both schemes, and $\tilde p_i(t)N(t)=p_i(t)$ exactly for
the *same* retarded solution. Verified on a synthetic solved system (residuals
$\sim10^{-13}$). **This specific rescaling does not reproduce the $C_2$/$D$
freedom** — it is scheme-invariant, contrary to what would be needed for the
advisory's mechanism to explain the finding via this route.

## 4. The real ambiguity, found by re-examining my own construction: how $N$ is distributed *inside* $g_i$

Test 1's negative result prompted re-checking the claim in
`Update-WP3-ClosedActionCouplingAudit-2026-07-13.md` §1 that the lapse
placement inside $g_i=(p_i^\text{sp}-\tfrac52)\dot c/c+Nc/R_h$ was "the unique
choice reproducing both WP2's $N=1$ formula and the addendum's pre-verified
row." **This was underjustified — the pre-verified row is scheme-blind.** The
addendum's check ($\delta S/\delta N=-\sum_ip_i\mathcal N_i\,\partial
g_i/\partial N$) holds for *any* functional form of $g_i(N)$; it does not
distinguish my choice from the equally $N{=}1$-reducing alternative
$$g_i^\text{alt}\equiv N\left[\Big(p_i^\text{sp}-\tfrac52\Big)\frac{\dot c}c+
\frac c{R_h}\right]$$
(multiplying the *entire* bracket by $N$, weight-drift term included, rather
than only the shell-sweep term). Both reduce identically to WP2's formula at
$N=1$; nothing checked so far distinguishes them.

**Consequence, derived (not yet fully numerically closed):** the sourced
identity $\dot\pi_i=-\Lambda_Mq'(\mathcal N_\text{tot})\mathcal N_i$ holds
*identically regardless of which $g_i$ is used* (the $g_i$-dependent terms
cancel between the $\mathcal N_i$ and $p_i$ equations for *any* $g_i$, a fully
general structural fact) — so $\pi_i(t)$ itself, under the same "$\pi_i\to0$ in
the deep past" condition, is **the same function of $t$ in both schemes.** But
the Hamiltonian-constraint contribution uses $\partial g_i/\partial N$, which
**does** differ: $c/R_h$ (my original scheme) vs. $\hat g_i\equiv
(p_i^\text{sp}-\tfrac52)\dot c/c+c/R_h$ (the alternative). For matter
($p^\text{sp}=\tfrac52$) these coincide exactly (weight-drift vanishes) — but
for radiation they differ by $-\tfrac32\dot c/c$. **This means $D$ genuinely can
change between the two schemes, and the mechanism is not multiplier
regularization (test 1's territory) but which piece of $g_i$ carries the lapse
factor** — a strictly narrower and more concrete question than the advisory's
general hypothesis.

**Not yet closed numerically**: confirming this requires species-resolved
$\mathcal N_\text{cold}(t)$, $\mathcal N_\text{rad}(t)$ trajectories separately
(not just the aggregate $\bar g$/$S(s)$ treatment every magnitude computation
so far has used, which implicitly assumes a single shared $\partial g/\partial
N$). Building this from memory risks exactly the kind of manufactured-reading
error flagged and avoided earlier in this program (`Update-WP3-
ClosedActionCouplingAudit-2026-07-13.md` §4) — deliberately not attempted
here.

## 5. Status

**Test 1 (uniform bracket rescaling): closed, no scheme dependence.** **The
more promising lead is elsewhere**: the $g_i$-internal lapse-placement
ambiguity, identified this round as a genuine gap in my own prior "uniqueness"
claim, not previously tested by either party. This is a sharper, more concrete
version of the advisory's scheme-dependence hypothesis — same spirit, different
specific mechanism, and one with a precise, checkable numerical test once
species-resolved $\mathcal N_i(t)$ is built. **Recommend this replace the
originally-assigned scheme test 2** (the M5 orientation flip) as the next
concrete step, since it is now the identified, concrete candidate rather than a
general hypothesis — pending the species-resolved machinery. Not a kill; not a
resolution. WP2 discharge-by-incorporation held, as directed. WP4a/WP4b
unaffected regardless of outcome. The KATRIN clock remains the program's most
time-critical item; nothing in `cdot-7/` was touched.
