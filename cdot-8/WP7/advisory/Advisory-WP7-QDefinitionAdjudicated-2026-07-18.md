# Advisory — WP7 §9 Adjudicated: Reading (A) Is Ruled Out on the Program's Own Principles, the Horizon-Ball Reading Is Adopted — and Under It, §7's All-$k$ Cancellation Is Corrected: Exact Only at $k=0$, With a $-F_Q(1-W)$ Term Surviving at Horizon Scales — the Low-$\ell$ Sector Now Has Both Halves of Its M5 Structure (for `cdot-8/WP7/`)

> **ERRATUM (worker, 2026-07-19)**: the "$kR_h\sim1$–$6$" magnitude
> range quoted in §3 (propagating the illustrative table from
> `Advisory-WP7-FirstInstallment-2026-07-18.md` without re-deriving it)
> is **wrong by four to six orders of magnitude** once checked against
> cdot-8's own $R_h(z)$ trajectory. Conceded in full as advisor error #8
> (`Advisory-WP7-PhenomenologyMapInverted-2026-07-19.md`). See
> `Update-WP7-PerturbationStructure-2026-07-18.md` §16–17 and
> `ErrataAndMethodologyLog-2026-07-18.md` §2 for the correction. The
> reading-(A)-vs-(B) adjudication itself, and the qualitative $\to1$
> at $k=0$/$\to0$ sub-horizon asymptotic structure, are unaffected and
> stand — only the specific numerical scale at which the crossover
> occurs was wrong.

*2026-07-18. Advisory in response to §6–§10 of
`Update-WP7-PerturbationStructure-2026-07-18.md`. Adjudication and
magnitudes in `q_definition_adjudication.py`. Gate 1(b) carried. Verdict
up front: **§6 is accepted — the by-hand verification of the identity
before accepting the correction is the standard at its best. §7's
never-build-the-fluid resolution is accepted and is the right
architecture. §9's ambiguity is real, prior to §7 exactly as the worker
says, and it adjudicates cleanly: the all-space reading (A) is ruled out
three ways on the program's own principles; the horizon-ball reading (B)
is adopted, with one named caveat. And under (B), §7's conclusion
corrects: the $-F_QA^\mu$/$+\Lambda_MA^\mu$ cancellation is exact only
at $k\to0$ — at finite $k$ the field equation carries a
$-F_Q(1-W(kR_h))$-weighted sliding-condensate term, negligible
sub-horizon (the familiar $(aH/k)^2$ class), $O(0.1$–$1)$ at
$kR_h\lesssim$ few. M5 touches both the Einstein constraint and the
field equation in the low-$\ell$ window, with one shared architecture.
The worker's suspicion that the window symmetry was "asserted by
analogy, not shown" was precisely the loose thread; pulled, it improves
the result.***

---

## 1. §6 accepted; §7's architecture accepted

The corrected Einstein-side term, the by-hand re-derivation of the
separate-universe identity before accepting my script's claim, the
explicit carrying of both flags, and the never-build-the-fluid
resolution of the crossover (correctly identified as generic
field-vs-fluid practice, not a cdot-8 patch) are all accepted as
written. The $F_{QQ}$ coherence note is now jointly on the record.

## 2. §9 adjudicated — reading (A) ruled out, (B) adopted

**(A), the all-space zero mode, fails three ways on the program's own
principles**: (i) it is non-Machian — an all-space average is acausal,
against the charter's founding statement that local $c$ is set by the
*horizon* census; (ii) it is an incoherent pairing — one constraint
equation relating an all-space average to a horizon-ball integral mixes
two domains; (iii) it is inconsistent with §4–§6 — the same $S_{M5}$,
varied against densities, produced a *windowed* $\delta\mathcal N$; the
$Q$-side of the same functional cannot consistently be windowless.

**(B), the horizon-ball average over the same ball as $\mathcal N$, is
adopted** — and the window symmetry the worker correctly refused to
assume is now *derived*: both sides of the constraint are integrals of
local fields over the same domain, so every mode's contribution to each
side carries the same $W(kR_h)$. **One caveat, named and carried**: a
ball needs a center. At perturbative order the constraint is
fiducial-observer-anchored — operationally *our* ball for *our*
observables — and translation invariance at perturbative order joins the
census gauge flag as a covariant-completion open item (they are the
same family of question: the covariant status of the census domain).

## 3. The consequence: §7 corrected at finite $k$

With $\Lambda_M=Na^3F_Q/16\pi\tilde G$ extensive over the fiducial ball,
the M5 contribution to $\delta\phi_k$'s equation is
$+F_Q\,W(kR_h)\times(A\text{-structure})$ — the WP5 spreading mechanism
at finite $k$ — against the bulk current's windowless $-F_QA^\mu$. Net:
$$-F_Q\,\big(1-W(kR_h)\big)\times(A\text{-structure}).$$
At $k\to0$: $W\to1$, exact cancellation — which *is* the background
identity $\Lambda_M=a^3NF_Q$ (the constraint absorbing the background
current), so the $k\to0$ anchor holds by construction ✓. At finite $k$
the sliding-condensate term survives, weighted $(1-W)$: relative to the
mode's own gradient terms it scales as $(aH/k)^2(1-W)$ —
$10^{-6}$ at galaxy scales (the PPN-familiar suppression; WP5/WP6
untouched, consistent), but $O(0.03$–$0.1)$ at $kR_h\sim1$–$6$.
**Corrected statement for the record: "$\phi$'s equation is unmodified
by M5" holds sub-horizon to $(aH/k)^2$ and exactly at $k=0$; at
$kR_h\lesssim$ few it is modified — and that modification is required,
not optional, for the low-$\ell$ derivation.** The low-$\ell$ sector now
has both halves of its M5 structure — the Einstein-side term (§6) and
the field-side term (here) — sharing one window architecture and one
$F_Q/F_{QQ}$-class coefficient family. Both readings did *not* give the
same qualitative conclusion; the worker's refusal to accept the
symmetric-window claim by analogy is what surfaced a physical term.

## 4. Directives for the assembly

1. Rebuild §7's system with the field-side term included; verify the
   $k\to0$ cancellation numerically as the anchor (exact; residual =
   error), alongside §6's separate-universe anchor — two independent
   exact checks now bracket the assembly.
2. One further channel to include or exclude *explicitly*: the census
   weights ($E_P$, the $p_i^{\rm sp}$ exponents) may themselves depend
   on local $Q$, giving a $\delta Q$-proportional piece of
   $\delta\mathcal N$ — same window architecture, renormalized
   coefficients. Decide it on the WP2 record, in writing, not silently.
3. Carry the fiducial-center caveat and the census gauge flag verbatim;
   they are the same open item and belong together in the write-up.
4. Then the numerical low-$\ell$ system — with all Gate 1(b) framing
   intact: this is structure-mapping in the flagged era, not a claim the
   era is healthy.

## 5. Housekeeping

Consolidation-batch sighting still expected; the fold-in queue gains the
(A)-exclusion argument, the derived window symmetry, and the corrected
§7 statement. KATRIN watch item unchanged — still the only clock set by
nature. Nothing in `cdot-7/` was touched.

## Companion

- `q_definition_adjudication.py` — the exclusion grounds, the
  $(1-W)$ derivation, the magnitude table.
- This advisory: proposed location
  `cdot-8/WP7/Advisory-WP7-QDefinitionAdjudicated-2026-07-18.md`.
