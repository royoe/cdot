# Update — WP3: Primary-Source Review of arXiv:0706.2151 (Deser & Woodard), and a Gap

*Companion: `SessionLog-2026-07-12.md` (this directory), Entry 9. The earlier citation
check (`Update-WP3-LapseBackreaction-2026-07-12.md` §1) only had abstract-level access
to Deser & Woodard and Maggiore & Mancarella, flagged explicitly as "high but not
full-text-primary confidence." With the actual source now available for the former,
this upgrades that citation to fully verified — and corrects one specific overclaim in
how it was attributed. The latter source was not actually delivered; flagged below.*

---

## 1. What arXiv:0706.2151 actually does — a correction, not just a confirmation

Read the full `.tex` source directly. The paper is real, matches the abstract
previously checked, and does construct the nonlocal $R\,f(\mathcal G[R])$ action
(eq. DL2) with $\mathcal G\equiv\Box^{-1}$ the retarded Green's function, given
explicitly as a double time-integral (eq. genf) — all as previously reported.

**Correction**: the earlier verification (delegated, abstract-level) reported that
"the standard localization is: define auxiliary fields via $\Box X\equiv R$ and $\Box
U\equiv Rf'(X)$, enforced by Lagrange multipliers... requiring a choice of homogeneous-
mode boundary condition," and attributed this to "the surrounding Deser-Woodard-school
literature." **This 2007 letter itself does not use that technique at all** — no
auxiliary field, no Lagrange multiplier, and the phrase "homogeneous mode" does not
appear. Its own method is more direct: derive the field equations by varying the
nonlocal action *naively* (which yields both advanced and retarded Green's functions),
then **replace the advanced Green's functions with retarded ones by hand**, justified
by citing Soussa & Woodard (*Class. Quant. Grav.* 20, 2737 (2003), astro-ph/0302030)
for the general principle that conservation only requires the Green's function to be
*some* inverse of the differential operator (either sign works for conservation; only
retarded is causal). The paper's own words: *"Naively varying a nonlocal action...
would result in advanced Green's functions as well as the retarded ones we desire.
However, because conservation only depends on the Green's function being the inverse
of a differential operator, one gets causal and conserved equations by simply
replacing the advanced Green's functions by the retarded ones."*

**This is the same underlying physical move** (a causality ambiguity from time-
nonlocality, resolved by choosing the retarded branch) that the well-posedness
advisory invoked to justify this session's own past-regularity treatment of
$p_{\mathcal N}$'s homogeneous mode — but it is a *different specific technique*
(direct Green's-function substitution after naive variation, vs. auxiliary-field
localization with a multiplier). The auxiliary-field/Lagrange-multiplier technique is
real and standard in this literature (later Woodard-school papers, and reportedly
Maggiore & Mancarella's own construction, per the earlier abstract-level check) — but
citing *this specific 2007 letter* for that specific technique was imprecise. The
underlying justification for "choose retarded" is not original to this paper either;
it traces to Soussa & Woodard (2003), which has not been checked.

**A genuine, useful connection found only by reading the primary source**: this paper's
own footnote grounds the retarded-vs-advanced choice in the Schwinger-Keldysh (in-in)
formalism (citing R.D. Jordan, *Phys. Rev.* D33, 444 (1986)) as the rigorous quantum
derivation of causal equations of motion. This is the *same lineage* as Galley's later,
classical "doubled" variational principle (PRL 110, 174301 (2013)) — Galley's method is
explicitly the classical-mechanics analogue of what Schwinger-Keldysh does at the
quantum level. **Two of the three cited papers are linked by a shared causality
principle, not merely a shared subject area** — a stronger structural justification for
invoking them together than "both are about nonlocal/dissipative systems," and worth
recording as such.

---

## 2. A useful, secondary technical result found in the primary source

Eq. (mod2) gives the *exact* modification to $G_{\mu\nu}$ from varying $R\,f(\mathcal
G[R])$ for a general metric (not just FRW): $\Delta G_{\mu\nu}=[G_{\mu\nu}+g_{\mu\nu}
\Box-D_\mu D_\nu]\{f(\mathcal G[R])+\mathcal G[Rf'(\mathcal G[R])]\}+(\text{gradient
terms enforcing the Bianchi identity for any }g_{\mu\nu})$. The paper states these
extra gradient terms exist *specifically* to guarantee Bianchi consistency for an
arbitrary metric, not only the symmetric background. This is a structurally different
nonlocal form (bilinear in $\mathcal G$, built from $R$ alone) from this session's own
$S_{M5}$ (linear in a multiplier, coupling $Q$ to the census $\mathcal N$) — so it does
not directly resolve the open well-posedness question from `Update-WP3-
LapseBackreaction`, but it is a useful, concrete existence proof that nonlocal terms
*can* be built with automatic Bianchi consistency, worth keeping in mind if the current
construction's own consistency check runs into trouble.

---

## 3. Gap: arXiv:1402.0448 (Maggiore & Mancarella) was not actually delivered

`references/arXiv.1402.0448/` exists but is empty — no `.tex`, no PDF, nothing.
Confirmed by direct directory listing, not just a quick glance. **This citation
remains at the earlier, abstract-level confidence** — the auxiliary-field localization
technique and its homogeneous-mode/retarded-boundary treatment, which this session's
own $(\mathcal N,p_{\mathcal N})$ construction most closely resembles, is *not yet*
verified against primary source. Recommend re-adding the actual source file(s) (the
`.tex` didn't transfer, or the directory was created without its contents) before this
citation is treated as fully checked.
