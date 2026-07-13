# Update — WP3: M5's Own Back-Reaction on the Friedmann Constraint (and a Citation Check)

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 8. Responds to
`Advisory-WP3-ExchangeTermWellPosedness-2026-07-12.md` and
`Addendum-FourthRound-C1NotGauge-2026-07-12.md`. Reports (1) the requested citation
verification, (2) confirmation of all "cheap algebra" claims, and (3) a genuinely new
finding from attempting directive 4 (run the confrontation with $\Lambda_M$ as
algebraic input): the $S_{M5}$ term back-reacts on the lapse/Hamiltonian constraint
directly, not only on the $\phi$-equation — something my own two prior updates missed.
Verified carefully (including catching and correcting a flawed sanity check of my own
before trusting the result) given the stakes of getting this wrong twice.*

---

## 1. Citation verification (directive 6)

Delegated and checked. All three references are real and support the claims made:
**Deser & Woodard, PRL 99, 111301 (2007), arXiv:0706.2151** — the nonlocal $Rf(\Box^{-1}
R)$ construction confirmed at abstract level; the auxiliary-field localization and
homogeneous-mode/retarded-Green's-function prescription is standard in the surrounding
school's literature (Woodard's review 1401.0254), not fully spelled out in the terse
original letter itself — high but not full-text-primary confidence.
**Maggiore & Mancarella, PRD 90, 023005 (2014), arXiv:1402.0448** — the $m^2R\Box^{-2}R$
"RR model" and its two-auxiliary-field localization, with the same retarded-boundary-
condition treatment of homogeneous modes, confirmed via abstract and the closely-related
companion literature. **Galley, PRL 110, 174301 (2013), arXiv:1210.2745** — confirmed:
doubled degrees of freedom, equality imposed at the *final* time, built specifically to
give genuinely retarded/dissipative equations of motion for open systems — an accurate
one-line summary, corroborated across independent secondary sources.

---

## 2. All "cheap algebra" claims independently reproduced

Sign check ($g/(\dot c/c)=(p-\tfrac52)+3\kappa\lambda x$): matter fixed point trivially
positive; radiation term at $x=1.72$ gives $0.747\approx0.75$, at $x=3.44$ gives
$2.994\approx3.0$ — both reproduced exactly (noting Flag 2's correction: $1.72$ is the
*matter* fixed point, used here only as one endpoint of the traversed range, not
mislabeled as "radiation" in this reproduction). Three-faces-of-$9/10$ arithmetic
($3/2\div5/3$; $d\ln Q/ds\div d\ln\mathcal N/ds=(-5/2)/(9/4)=-10/9$, giving $q(\mathcal
N)\propto\mathcal N^{-10/9}$) reproduced exactly. The trivial integration of the
$\phi$-equation ($a^3F_Q=16\pi\tilde G\Lambda_M/N+C_1$) confirmed — undoing a total time
derivative, no subtlety.

---

## 3. A finding from attempting directive 4: $S_{M5}$ back-reacts on the Hamiltonian
constraint too, not only on the $\phi$-equation

Setting up the full lapse variation, keeping $N$ general throughout (not the earlier
$N=1$ gauge used only to validate against AeST's *known* Friedmann equation) —
`Update-WP3-ActionLevelAttempt`'s derivation implicitly only tracked $S_\phi$'s
contribution to $\delta S/\delta N$. $S_{M5}=\int dt\,\Lambda_M[\dot\phi/N-q(\mathcal
N)]$ has its own, explicit $N$-dependence and must be varied too:
$$\frac{\delta S_{M5}}{\delta N}=-\Lambda_M\frac{\dot\phi}{N^2}=-\frac{\Lambda_MQ}{N}$$
— verified numerically against finite differences on concrete numbers before trusting
it (exact match). Combining with the (separately verified, term-by-term, against
finite differences) $S_\text{EH}$, $S_m$, $S_\phi$ contributions and dividing through by
$a^3$ gives the **complete** Hamiltonian constraint:
$$H_{\hat\tau}^2=\frac{8\pi G}3\rho_m-\frac13(F-QF_Q)+\frac{8\pi G}3\cdot\frac{\Lambda_MQ}
{Na^3}.$$
Substituting the integrated $\phi$-equation's own $\Lambda_M=\frac{N}{16\pi\tilde G}
(a^3F_Q-C_1)$ (taking $G=\tilde G$):
$$\boxed{\ H_{\hat\tau}^2=\frac{8\pi G}3\rho_m-\frac13F+\frac12QF_Q-\frac{QC_1}{6a^3}\ }$$
**The coefficient of $QF_Q$ shifts from $\tfrac13$ (the naive, $S_{M5}$-blind formula
every prior round used) to $\tfrac12$, plus a new, explicit $C_1$-dependent term.**
Re-verified the full chain numerically end-to-end (every individual $\delta S/\delta N$
term against finite differences, then the algebraic rearrangement into this boxed form)
— caught and corrected one flawed sanity-check design of my own along the way
(comparing two sides that only need to agree once the constraint is actually imposed,
not for arbitrary unconstrained inputs) before accepting the result.

**Why this matters.** Every reconstruction since the third escalation (`Update-WP3-
InverseReconstruction`, the stand-in/original-proposer resolution, this session's own
zero-freedom quadrature) built $F(Q)$ to match the invoice using the *naive* $-\tfrac13
(F-QF_Q)$ Friedmann term alone — never accounting for $S_{M5}$'s own contribution to
the *same* constraint. With the boxed equation, matching the invoice's $E^2(a)$ now
requires solving a **different** equation for $F(Q)$ (coefficient $\tfrac12$, not
$\tfrac13$, plus the $C_1$ term) — meaning the specific $F\propto Q^{9/5}$ result quoted
in every round so far was derived against the wrong version of the constraint and needs
re-solving. **This is also, likely, exactly the missing energy-exchange channel** the
previous update went looking for externally (the shell-sweep hypothesis): $S_{M5}$'s
own back-reaction on the Hamiltonian constraint may already supply what a bolted-on
exchange term was being sought for — the two candidates from the last update
(auxiliary-field vs. nonlocal-functional) were both examined only for their effect on
the $\phi$-equation; neither was checked against the lapse equation until now.

---

## 4. Status

Not yet re-solved: the quadrature needs to be redone against the boxed equation, and
then form (iii)'s razor (continuity source $=-\dot p_\phi$) needs re-deriving using the
*complete* stress-energy (φ-sector plus $S_{M5}$'s own contribution, including its
$a$-variation, not yet computed here). This is genuine forward progress, not a reversal
of the invoice's qualitative shape (dust-like plateau, late-time bend) — but the
specific exponents quoted since the third escalation ($9/5$, the $9/10$ family) are now
provisional pending this re-solve. Recommend a check-in before redoing the quadrature,
given how much has shifted in this single pass and the value the "verify before
building further" discipline has already demonstrated three times this program.
