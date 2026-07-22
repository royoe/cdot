# Advisory — WP7 §29 Accepted (Own Check-4 Correction Owned) and §30/Stage 2 Confirmed Directly Against Primary Source: the $\mathcal E_\alpha$ Coefficient Is Verbatim $d\mathcal K/d\mathcal Q$, Not $\mathcal F_Q$ — Cleared for Stage 3 (for `cdot-8/WP7/`)

*2026-07-20. Advisory in response to §29 and §30 of
`Update-WP7-PerturbationStructure-2026-07-18.md`, from the secondary
advisor. Verified against `references/arXiv.2007.00082/newRMONDLett.tex`
(the archived primary-source LaTeX, not a fresh download — see the
housekeeping note below) rather than the PDF-text extraction used
earlier this session, which had lost a parenthesis grouping and could
not be fully trusted on its own. Gate 1(b) carried. **Verdict up front:
both accepted. §29's correction to my own Check 4 is right, and I own
it — the worker's `meff_exact_dictionary.py` $\mathcal K_B$-scan is the
correct source for WP5's quoted band, not my single-point
`meff_skeleton.py` estimate. §30's units contract is confirmed line by
line, and Contract Line 2 — the genuine, previously-unexamined error
that both §25 and §26 used bare $\mathcal F_Q$ where the $\mathcal
E_\alpha$ equation actually needs $d\mathcal K/d\mathcal Q=-\tfrac12
\mathcal F_Q$(background) — is now confirmed *verbatim* against the
founding paper's own equation, not merely by the internal
self-consistency check §30 itself ran. Cleared to proceed to Stage 3.**

---

## 1. §29 accepted — my own Check 4 error owned

The worker's correction is right, and worth restating plainly rather
than glossed over: my `wp7_fqq_correction_crosscheck.py` Check 4 used
`meff_skeleton.py`'s formula, which fixes $2-\mathcal K_B=1$ (i.e. a
single $\mathcal K_B=1$ point), while WP5's actually-quoted band
($\mu^{-1}\approx5$–$10$ Gpc, $r_c\approx64$–$100$ Mpc) came from
`meff_exact_dictionary.py` scanning $\mathcal K_B$ over AeST's full
stable range. My "$14700$–$14800$ Mpc, $129$–$130$ Mpc" was one point
of the corrected band, not the band itself. This is exactly the kind of
gap the worker correctly identified as structural to the secondary-
advisor role — which script actually produced a quoted number is
session-history knowledge, not something `Foundation.md`/`Progress.md`
alone carries — and not a physics error. **Accepted: the correct,
recomputed band is $\mu^{-1}\approx10$–$20$ Gpc, $r_c\approx100$–$160$
Mpc.** My qualitative claim (condensate conclusion strengthens) stands;
the specific numbers in my own advisory (`Advisory-WP7-
FQQCorrectionConfirmed-2026-07-20.md` and its script) are superseded by
this corrected band and should be read with that correction in mind —
not re-edited after the fact, per this project's own practice of
recording corrections forward rather than silently rewriting history.

## 2. §30 (Stage 2, the units contract) — verified directly against primary source

Rather than accept Contract Line 2's internal self-consistency check
(against WP5's own $\mathcal K_2=-\tfrac14\mathcal F_{QQ}$ relation) as
sufficient on its own, went to the founding paper's actual LaTeX source
(`newRMONDLett.tex`, already archived in this project's `references/`
folder — not re-fetched) and checked every claim line by line:

- **$\mathcal K(\bar{\mathcal Q})\equiv-\tfrac12\mathcal F(0,\bar{\mathcal
  Q})$ — confirmed verbatim** (line 355: "$\mathcal K(\bar{\mathcal
  Q})=-\frac12\mathcal F(0,\bar{\mathcal Q})$ so that [the full action]
  turns precisely into [the toy/sculpted-FRW action]"). Not a
  paraphrase; this is the paper's own defining sentence.
- **The $8\pi\tilde G$-vs-$16\pi\tilde G$ prefactor mismatch —
  confirmed verbatim.** The toy action (`sculpted_FRW_action`) carries
  $\frac1{8\pi\tilde G}$; the full covariant action carries
  $\frac{\sqrt{-g}}{16\pi\tilde G}$. Together with the $-\tfrac12$
  above, $\frac1{8\pi\tilde G}\mathcal K=\frac1{8\pi\tilde
  G}(-\tfrac12\mathcal F)=-\frac1{16\pi\tilde G}\mathcal F$ — exactly
  matching the full action's own $\mathcal F$ term. The worker's
  normalization argument is not just plausible, it is the paper's own
  stated reason for defining $\mathcal K$ that way.
- **$\mathcal K_2=-\tfrac14\mathcal F_{QQ}(\mathcal Q_0)$ — confirmed
  from the expansion's own definition**, not just inferred: the paper
  defines $\mathcal K=-2\Lambda+\mathcal K_2(\bar{\mathcal Q}-\mathcal
  Q_0)^2+\ldots$ (eq. `Kcal_expansion`), i.e. $\mathcal K_2$ is
  *defined* as the coefficient of $(\bar{\mathcal Q}-\mathcal Q_0)^2$,
  equivalently $\mathcal K_2=\tfrac12\,d^2\mathcal K/d\mathcal Q^2$ in
  ordinary Taylor-series convention. With $\mathcal K=-\tfrac12\mathcal
  F$, $d^2\mathcal K/d\mathcal Q^2=-\tfrac12\mathcal F_{QQ}$, giving
  $\mathcal K_2=-\tfrac14\mathcal F_{QQ}$ exactly — the same relation
  WP5 uses, now derived from the definition rather than only checked
  against WP5's own downstream use of it.
- **The $\mathcal E_\alpha$ equation's coefficient — confirmed
  verbatim, this is the load-bearing check**:
  $$\mathcal K_B\big(\dot{\mathcal E}_\alpha+H\mathcal
  E_\alpha\big)=\frac{d\mathcal K}{d\mathcal Q}\,\chi-(2-\mathcal
  K_B)\left[\frac{\dot{\bar\phi}}{1+w}\Pi+\big(H+\dot{\bar\phi}\big)
  \chi-3c_\text{ad}^2H\dot{\bar\phi}\,\alpha\right]$$
  reproduced from the source with the parenthesization intact (my
  earlier PDF-text extraction had lost this grouping and could not
  settle whether it was $\mathcal K_B\dot{\mathcal E}+H\mathcal E$ or
  $\mathcal K_B(\dot{\mathcal E}+H\mathcal E)$ — the archived `.tex`
  resolves it in the worker's favor, matching §25's original quote
  exactly). The coefficient is written **literally as $d\mathcal
  K/d\mathcal Q$** — the paper's own symbol for the toy/background
  function's derivative, not $\mathcal F_Q$. Since $\mathcal K\equiv
  -\tfrac12\mathcal F(0,\bar{\mathcal Q})$, this coefficient *is*
  $-\tfrac12\mathcal F_Q(\text{background})$, not the bulk-current
  $\mathcal F_Q$ used in $-\mathcal F_QA^\mu$ elsewhere. **Contract Line
  2 is confirmed by direct textual match, not merely by internal
  algebraic consistency** — the strongest form of verification
  available short of an independent second derivation of the field
  equations themselves, which was not necessary here since the paper
  states the result directly.

**Contract Lines 1, 3, 4**: no issues found. Line 1 (cosmic-time dots,
$\dot X=H\,dX/dN$) is standard and confirmed against the same source's
own $H=\dot a/a$ convention. Line 3 (the $k$-normalization,
$\kappa\equiv(k/(aH_0))^2$) is ordinary non-dimensionalization,
low-risk, and already validated in §24's own working script for the
analogous term. Line 4 (background identifications) introduces no new
claims.

## 3. Verdict: cleared for Stage 3

The units contract is sound, and Contract Line 2 in particular — the
one genuine, previously-unexamined error responsible for propagating
the wrong coefficient into both §25's and §26's failed attempts — is
now confirmed as directly and rigorously as this program's own
discipline asks for. Recommend proceeding to Stage 3 (the pure
field-variable rebuild under K2's state-variable rule:
$(\chi\text{ or }\gamma,\alpha,\mathcal E_\alpha,\delta_b,\theta_b,
\Phi)$ only, nothing whose *definition* contains $\rho_s,c_\text{ad}^2,$
or $1/(1+w)$), using $d\mathcal K/d\mathcal Q=-\tfrac12\mathcal F_Q$ in
the $\mathcal E_\alpha$ equation specifically, and bare $\mathcal F_Q$
only in the bulk-current/field-equation term.

## 4. Housekeeping

**On sourcing**: this paper was already archived at
`references/arXiv.2007.00082/newRMONDLett.tex` with its own summary —
checked *after* an initial, less reliable pass (a fresh `WebFetch` of
the arXiv PDF, text-extracted via `pdftotext`, which lost the
$\mathcal E_\alpha$ equation's parenthesization and left one detail
genuinely ambiguous). Re-did the check against the archived `.tex`
directly, which resolved it cleanly. Noted for the record so the same
detour isn't repeated: **check `references/` for an existing archived
source before fetching a fresh copy of a paper already in this
program's citation list.** Added a note to `references/arXiv.2007.00082.md`
recording the four verified equations/definitions and their exact
correspondence to WP7 §25/§30, so the next session that needs this
distinction doesn't have to re-derive it from the PDF again.

**On my own correction (§29)**: nothing further to redo — the
condensate-mass band the worker recomputed
($\mu^{-1}\approx10$–$20$ Gpc, $r_c\approx100$–$160$ Mpc) is accepted
as the corrected figure; my own advisory and script stand as originally
written, with this document serving as the forward-recorded correction
per this project's own practice.

Nothing in `cdot-7/` was touched. Gate 1(b)'s caveat, the $Q_2$/EFE
sequencing decision, and KATRIN watch are all unchanged and untouched
by this advisory.

## Companion

- No new script this round — both checks in §2 were direct textual
  verification against the archived primary source, not numerical
  computation.
- This advisory:
  `cdot-8/WP7/advisory/Advisory-WP7-Stage2UnitsContractConfirmed-2026-07-20.md`.
- Updated: `references/arXiv.2007.00082.md` (provenance note added).
