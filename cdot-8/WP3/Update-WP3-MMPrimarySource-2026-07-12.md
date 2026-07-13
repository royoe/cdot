# Update — WP3: Maggiore & Mancarella, Fully Verified, and a Concrete Method for Flag 1

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 10. The source
extraction failed the first time and was re-delivered; read in full. This upgrades
the second citation from abstract-level to fully verified, and — more valuably — hands
this construction a concrete, precedented, already-tested method for exactly the
open problem `Update-WP3-ExchangeTermWellPosedness` and `Addendum-FourthRound-
C1NotGauge` left unresolved (Flag 1: how to fix $C_1$/the homogeneous mode).*

---

## 1. The auxiliary-field technique, confirmed exactly as claimed — this time it's the
right paper

`arXiv:1402.0448` (Maggiore & Mancarella, *Nonlocal gravity and dark energy*, PRD 90,
023005 (2014)) constructs $S_\text{NL}=\frac1{16\pi G}\int\sqrt{-g}[R-\frac{d-1}{4d}m^2
R\Box^{-2}R]$ and localizes it *exactly* as the well-posedness advisory described:
introduce $U=-\Box^{-1}R$, $S=-\Box^{-1}U=\Box^{-2}R$, rewrite the action with **two**
Lagrange multipliers $\xi_1,\xi_2$:
$$S_\text{NL}=(16\pi G)^{-1}\!\int\!\sqrt{-g}\big[R(1-\mu S)-\xi_1(\Box U+R)-\xi_2(\Box
S+U)\big].$$
Varying gives $G_{\mu\nu}=\mu K_{\mu\nu}+8\pi GT_{\mu\nu}$, $\Box U=-R$, $\Box S=-U$ —
this *is* the two-multiplier, auxiliary-field structure my own $(\mathcal N,
p_{\mathcal N})$-plus-$\Lambda_M$ construction mirrors. **Unlike the Deser-Woodard
correction, this citation is now fully, precisely confirmed** — the earlier
abstract-level check attributed the right technique to the right paper after all.

**The homogeneous-mode issue, confirmed in the paper's own words, precisely**:
*"The choice of the homogeneous solution is part of the definition of the $\Box^{-1}$
operator and therefore of the original nonlocal theory... in the local formulation...
given a solution for $U$ we can add to it an arbitrary solution of the homogeneous
equation $\Box U=0$. However, such a general solution of the local equation is not a
solution of the integro-differential equation of motion of the original nonlocal
model... All other solutions of the local formulation are spurious."* This is exactly
the "candidate A's extra freedom is B's boundary-condition ambiguity relocated"
diagnosis from `Advisory-WP3-ExchangeTermWellPosedness`, now confirmed against the
paper that actually establishes it.

---

## 2. A concrete method for Flag 1, more tractable than an eternal-past limit

Rather than analyze the $t\to-\infty$ limit abstractly (this session's own approach so
far), Maggiore & Mancarella fix the homogeneous mode **practically**: they give an
explicit FRW retarded definition of $\Box^{-1}$ anchored at $t_*$, "some initial value
of time... deep into the radiation dominance epoch," and note this choice is
*insensitive* to exactly how deep, "since in RD the Ricci scalar $R$ vanishes." Their
numerical integration (§"Cosmological evolution and dark energy") **starts in RD with
$U=S=0$ as the initial condition** — not an asymptotic regularity argument, a direct,
finite-time boundary condition where the sourcing term is already small.

**They also did exactly the stability check Flag 1(c) asks for, and report the
result**: with $\zeta_0\equiv h'/h=\{-2,-\tfrac32,0\}$ in RD, MD, and de Sitter
respectively, the homogeneous modes for their $U,W$ go as $u_1e^{-(3+\zeta_0)x}$,
$w_1e^{-(3-\zeta_0)x}+w_2e^{2\zeta_0x}$ — **all constant or exponentially decreasing
for $-2\le\zeta_0\le0$**, i.e. stable (not growing into the past) across RD, MD, *and*
a preceding inflationary stage. They flag, as a genuine counter-example worth taking
seriously: a *related* model they built from $(g_{\mu\nu}\Box^{-1}R)^T$ is stable in MD
and RD **but not** in an inflationary stage — i.e. this kind of stability is sensitive
to the precise nonlocal term chosen, not automatic. **This directly informs how to
treat the well-posedness advisory's own eventual $C_1$/$p_{\mathcal N}$ check**: don't
assume stability by analogy; redo their explicit exponent calculation (homogeneous
mode $\propto e^{-(\text{coefficient})\,x}$ across each era this project's own census
trajectory traverses — matter, radiation, and the crossover) using this project's own
$g(t)$, the way they did for theirs.

**Adopted for this construction, replacing the abstract eternal-past approach**:
anchor $p_{\mathcal N}$ (and, separately, $C_1$'s determination) at a finite,
deep-radiation-era initial condition where the sourcing term is small and the choice
of exact starting point is shown not to matter — mirroring their $t_*$, $U=S=0$
practice — rather than attempting an analytic $t\to-\infty$ limit on cdot-7's own
eternal-past structure, which (per `Update-WP3-BudgetTension`'s earlier finding) is a
less standard, less-charted regime than ordinary RD.

---

## 3. Status

Both remaining citations (Deser-Woodard, corrected; Maggiore-Mancarella, now fully
confirmed and directly useful) are settled. The concrete next step this unlocks:
redo the $F(Q)$ quadrature against the corrected (coefficient-$\tfrac12$) Hamiltonian
constraint from `Update-WP3-LapseBackreaction`, fixing $C_1$ via a Maggiore-Mancarella-
style deep-RD initial condition rather than an eternal-past limit, and running their
same homogeneous-mode stability check on this project's own $g(t)$ across the
matter/radiation/crossover eras before trusting the result. Not yet done — this is the
concrete plan, reported before executing it given how much has already shifted this
session.
