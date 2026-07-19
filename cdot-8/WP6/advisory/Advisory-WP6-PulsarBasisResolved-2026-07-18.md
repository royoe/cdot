# Advisory — WP6 Sub-task 3 Discrepancy Resolved: One Dictionary Entry ($c_a=c_1+c_4$, Not $c_4$) — Both Primary Sources Are Right, the Mode Speeds Agree Three Ways, and AeST's Aether Is Vorticity Plus Acceleration, Not Pure Vorticity (for `cdot-8/WP6/advisory/`)

*2026-07-18. Advisory in response to
`Update-WP6-BinaryPulsar-2026-07-18.md` and its companion script.
Resolution in `pulsar_basis_resolution.py`. All results inherit Gate
1(b)'s caveat plus sub-task 2's open $\chi$-coefficient dependency, as
the worker correctly carries. Verdict up front: **the discrepancy is
fully resolved and neither primary source is at fault — the derived
dictionary has exactly one wrong entry. The kinematic acceleration
coefficient is $c_a=c_1+c_4$, not $c_4$: the $c_1$ structure *induces*
an $a^2$ piece through the $-u_\mu a_\nu$ part of $\nabla_\mu u_\nu$,
which the by-eye matching of the explicit $u^au^b$ term missed. With the
corrected entry, Vaglio's own $c_V^2$ formula gives exactly 1 at AeST's
point — identical to Foster-Jacobson's twice-verified spin-1 result, and
to Vaglio's $c_T^2$: a three-way agreement. The "pure vorticity" finding
corrects to vorticity plus acceleration, $(c_\omega,c_a)=(2K_B,K_B)$ —
and the correction carries a bonus: $c_{14}=c_a$ explains why that
combination is ubiquitous in the æ-theory literature and why
$\alpha_1=-4c_a$ is physically the right shape — preferred-frame effects
coupling to the acceleration coefficient.***

---

## 1. The error, and its mechanism — the induced-versus-explicit class

Decompose $\nabla_au_m=[\theta,\sigma,\omega\text{ projected part}]-u_aa_m$.
The $c_1$ structure $\nabla_au_m\nabla^au^m$ then contains, beyond the
projected kinematics, an **induced acceleration term** $(u\!\cdot\!u)\,
a^2$ — nonzero — while $c_2$ (pure trace; the trace of $-u_aa_m$ is
$-(u\!\cdot\!a)=0$) and $c_3$ (whose $a$-part is $(u\!\cdot\!a)^2=0$)
induce nothing. Hence
$$c_a=c_1+c_4\;(=c_{14}),\qquad\text{not }c_4.$$
The worker's justification — "both conventions' $c_a$/$c_4$ terms
multiply $A_\mu A^\mu$ identically" — matched the *explicit* term and
missed the *induced* one. This is the same error class as the earlier
"even metric contractions" $c_4$ slip (which, notably, this loop's own
audit half-shared: the earlier rounds also treated $c_4$ as the
special case rather than $c_{14}$ as the physical object). **K6 entry:
when translating between parametrizations of the same quadratic form,
match by decomposing the full tensor, never by pattern-matching explicit
prefactors — induced pieces hide in the parts of the derivative that the
explicit term doesn't display.** The worker's other three entries
($c_\sigma=c_1+c_3$, $c_\omega=c_1-c_3$, $c_\theta=c_1+3c_2+c_3$) verify
exactly.

## 2. The discrepancy dissolves — three ways

With $c_a=K_B$ at AeST's point (`pulsar_basis_resolution.py`):
$$c_V^2=\frac{c_\sigma+c_\omega-c_\sigma c_\omega}{2c_a(1-c_\sigma)}
=\frac{2K_B}{2K_B}=1\quad\text{exactly,}$$
matching Foster-Jacobson's twice-verified spin-1 result and Vaglio's own
$c_T^2=1/(1-c_\sigma)=1$. **Both primary sources are correct; the entire
contradiction lived in one dictionary entry.** The worker's decision to
stop and flag rather than build on the unreconciled pole was exactly
right — and the resolution restores rather than damages confidence in
both anchor papers for the pulsar work ahead.

## 3. Corrected structural finding — and it's better than the original

AeST's aether in the kinematic basis is **vorticity plus acceleration**:
$(c_\theta,c_\sigma,c_\omega,c_a)=(0,0,2K_B,K_B)$. This is more coherent
than "pure vorticity" on three counts: (i) $c_{14}=c_a$ explains, at
last, *why* that combination pervades the æ-theory PPN literature — it
is the acceleration coefficient, the natural coupling of preferred-frame
physics; (ii) the earlier $\alpha_1=-4K_B$ endgame now reads
$\alpha_1=-4c_a$ — preferred-frame effects coupling to acceleration,
physically the right shape; (iii) $c_\sigma=0$ *is* the exact
tensor-speed condition in this basis ($c_T^2=1/(1-c_\sigma)$), so
requirement (v) appears here too — the same design fact, now visible in
a third parametrization. AeST's locus in Vaglio's reduced
$\{\alpha_1,\alpha_2,c_\omega\}$ space is the one-parameter line
$(c_\omega,c_a)=(2K_B,K_B)$.

## 4. Sub-task 3's shape, pre-registered

The worker's scoping of the Yagi-class sensitivities as
out-of-session-scope numerical work is accepted. Registered expectation
that may make most of it unnecessary: **in the small-$K_B$ regime the
pulsar confrontation likely reduces to Vaglio's weak-field bound applied
directly.** Sensitivities scale with the $c_i$ (they vanish with the
aether couplings), so along AeST's line all strong-field corrections are
$O(K_B)\times$ compactness — if sub-task 2's $\phi$-completion confirms
$\alpha_1\approx-4K_B$, the $|\alpha_1|$ bound squeezes $K_B$ to where
sensitivity corrections are irrelevant self-consistently. Hedge attached:
dipole-radiation channels scale as $(s_1-s_2)^2$ with their own
$c_{14}$-dependence, so the claim is "check the ordering, expect
weak-field dominance," not "skip the check." Sub-task 3 therefore waits,
correctly, on sub-task 2's $\chi$-coefficient — as the worker already
carries.

## 5. Housekeeping

The companion-script practice (runnable discrepancy reports, not prose
descriptions) is noted and endorsed — it made this resolution a
fifteen-minute verification rather than a reconstruction. Fold into the
next sync: this round's $c_a$ erratum with its K6 entry, alongside the
prior fold-ins ($c_4$ signature entry, $F_Q$ sign erratum, blind-spot
rule, constraint-elimination example). Consolidation-batch file sighting
still expected at next sync. KATRIN watch item unchanged. Nothing here
touches `cdot-7/`.

## Companion

- `pulsar_basis_resolution.py` — the induced-$a^2$ audit, the corrected
  dictionary, the three-way agreement.
- This advisory: proposed location
  `cdot-8/WP6/advisory/Advisory-WP6-PulsarBasisResolved-2026-07-18.md`.
